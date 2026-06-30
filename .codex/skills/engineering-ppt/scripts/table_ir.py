#!/usr/bin/env python3
"""Build deterministic table IR and source-derived table image assets.

The LLM may decide whether a table belongs in a deck and what conclusion it
supports. This module owns table structure, style extraction, render-mode
selection, and fallback image generation.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import zipfile
from pathlib import Path
from typing import Any, Iterable

from lxml import etree

try:
    import fitz
except ImportError:  # pragma: no cover
    fitz = None

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:  # pragma: no cover
    Image = ImageDraw = ImageFont = None


WORD_NS = {
    "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
}
W = WORD_NS["w"]
EMU_PER_INCH = 914400
DXA_PER_INCH = 1440
SUPPORTED_TABLE_SOURCES = {".docx", ".pdf"}


def w_attr(node: etree._Element | None, name: str, default: str = "") -> str:
    if node is None:
        return default
    return node.get(f"{{{W}}}{name}", default)


def clean_text(value: str) -> str:
    return re.sub(r"\s+", " ", value or "").strip()


def twips_to_inches(value: str | int | float | None, default: float = 0.0) -> float:
    try:
        return max(0.0, float(value) / DXA_PER_INCH)
    except (TypeError, ValueError):
        return default


def half_points(value: str | None, default: float = 10.5) -> float:
    try:
        return max(1.0, float(value) / 2.0)
    except (TypeError, ValueError):
        return default


def normalize_color(value: str | None, default: str = "#FFFFFF") -> str:
    if not value or value.lower() == "auto":
        return default
    value = value.strip().lstrip("#")
    if len(value) == 6 and re.fullmatch(r"[0-9a-fA-F]{6}", value):
        return f"#{value.upper()}"
    return default


def source_hash(path: Path) -> str:
    return hashlib.sha1(str(path.resolve()).encode("utf-8")).hexdigest()[:8]


def table_id(index: int) -> str:
    return f"T-{index:03d}"


def locator_for_index(index: int) -> str:
    return f"T{index:03d}"


def cell_text(tc: etree._Element) -> str:
    return clean_text("".join(tc.xpath(".//w:t/text()", namespaces=WORD_NS)))


def grid_span(tc: etree._Element) -> int:
    node = tc.find("./w:tcPr/w:gridSpan", namespaces=WORD_NS)
    try:
        return max(1, int(w_attr(node, "val", "1")))
    except ValueError:
        return 1


def vmerge_state(tc: etree._Element) -> str | None:
    node = tc.find("./w:tcPr/w:vMerge", namespaces=WORD_NS)
    if node is None:
        return None
    return w_attr(node, "val", "continue") or "continue"


def table_grid_widths(tbl: etree._Element, col_count: int) -> list[float]:
    values: list[float] = []
    for grid_col in tbl.findall("./w:tblGrid/w:gridCol", namespaces=WORD_NS):
        values.append(twips_to_inches(w_attr(grid_col, "w"), 0.0))
    if len(values) != col_count or not any(values):
        return [1.0] * max(1, col_count)
    return values


def row_height(tr: etree._Element) -> float:
    node = tr.find("./w:trPr/w:trHeight", namespaces=WORD_NS)
    return twips_to_inches(w_attr(node, "val"), 0.34)


def border_style(tc_pr: etree._Element | None) -> dict[str, Any]:
    result: dict[str, Any] = {
        "border": "single",
        "border_color": "#000000",
        "border_complexity": 0.0,
    }
    if tc_pr is None:
        return result
    borders = tc_pr.find("./w:tcBorders", namespaces=WORD_NS)
    if borders is None:
        return result
    styles = []
    colors = []
    diagonal = False
    for child in borders:
        local = etree.QName(child).localname
        if local in {"tl2br", "tr2tl", "tr2bl"}:
            diagonal = True
        styles.append(w_attr(child, "val", "single"))
        colors.append(normalize_color(w_attr(child, "color", "000000"), "#000000"))
    unique_styles = {item for item in styles if item and item != "nil"}
    if unique_styles:
        result["border"] = sorted(unique_styles)[0]
    if colors:
        result["border_color"] = colors[0]
    complexity = min(1.0, (len(unique_styles) + max(0, len(styles) - 4)) / 8.0)
    result["border_complexity"] = complexity
    result["has_diagonal_header"] = diagonal
    return result


def paragraph_align(tc: etree._Element) -> str:
    node = tc.find(".//w:pPr/w:jc", namespaces=WORD_NS)
    value = w_attr(node, "val", "center")
    return {
        "left": "left",
        "right": "right",
        "both": "justify",
        "center": "center",
    }.get(value, "center")


def vertical_align(tc_pr: etree._Element | None) -> str:
    node = tc_pr.find("./w:vAlign", namespaces=WORD_NS) if tc_pr is not None else None
    return {"top": "top", "bottom": "bottom", "center": "middle"}.get(w_attr(node, "val", "center"), "middle")


def run_style(tc: etree._Element) -> dict[str, Any]:
    r_pr = tc.find(".//w:rPr", namespaces=WORD_NS)
    if r_pr is None:
        return {"font_size": 10.5, "bold": False, "color": "#000000"}
    sz = r_pr.find("./w:sz", namespaces=WORD_NS)
    color = r_pr.find("./w:color", namespaces=WORD_NS)
    return {
        "font_size": half_points(w_attr(sz, "val", None), 10.5),
        "bold": r_pr.find("./w:b", namespaces=WORD_NS) is not None,
        "color": normalize_color(w_attr(color, "val", "000000"), "#000000"),
    }


def cell_style(tc: etree._Element) -> dict[str, Any]:
    tc_pr = tc.find("./w:tcPr", namespaces=WORD_NS)
    shd = tc_pr.find("./w:shd", namespaces=WORD_NS) if tc_pr is not None else None
    borders = border_style(tc_pr)
    style = {
        "font_size": 10.5,
        "bold": False,
        "align": paragraph_align(tc),
        "valign": vertical_align(tc_pr),
        "fill": normalize_color(w_attr(shd, "fill", "FFFFFF"), "#FFFFFF"),
        "border": borders["border"],
        "border_color": borders["border_color"],
        "margin": {"left": 0.04, "right": 0.04, "top": 0.02, "bottom": 0.02},
    }
    style.update(run_style(tc))
    style["_border_complexity"] = borders["border_complexity"]
    style["_has_diagonal_header"] = borders.get("has_diagonal_header", False)
    return style


def parse_docx_table(tbl: etree._Element, source: Path, index: int) -> dict[str, Any]:
    locator = locator_for_index(index)
    rows_xml = tbl.findall("./w:tr", namespaces=WORD_NS)
    rows: list[list[str]] = []
    cells: list[dict[str, Any]] = []
    merged_cells: list[dict[str, int]] = []
    occupancy: dict[tuple[int, int], str] = {}
    active_vmerge: dict[int, dict[str, Any]] = {}
    max_col = 0
    border_complexities: list[float] = []
    has_diagonal_header = False
    has_nested_table = bool(tbl.xpath(".//w:tc/w:tbl", namespaces=WORD_NS))
    row_heights = [row_height(tr) for tr in rows_xml]

    for r_idx, tr in enumerate(rows_xml):
        row_values: list[str] = []
        c_idx = 0
        for tc in tr.findall("./w:tc", namespaces=WORD_NS):
            while (r_idx, c_idx) in occupancy:
                row_values.append("")
                c_idx += 1
            colspan = grid_span(tc)
            vmerge = vmerge_state(tc)
            if vmerge == "continue" and c_idx in active_vmerge:
                origin = active_vmerge[c_idx]
                if origin["row"] + origin["rowspan"] == r_idx:
                    origin["rowspan"] += 1
                for offset in range(origin["colspan"]):
                    occupancy[(r_idx, origin["col"] + offset)] = origin["id"]
                row_values.extend([""] * origin["colspan"])
                c_idx = origin["col"] + origin["colspan"]
                max_col = max(max_col, c_idx)
                continue

            style = cell_style(tc)
            has_diagonal_header = has_diagonal_header or bool(style.pop("_has_diagonal_header", False))
            border_complexities.append(float(style.pop("_border_complexity", 0.0)))
            text = cell_text(tc)
            cell = {
                "id": f"{locator}:r{r_idx}c{c_idx}",
                "row": r_idx,
                "col": c_idx,
                "rowspan": 1,
                "colspan": colspan,
                "text": text,
                "style": style,
                "is_header": r_idx == 0,
            }
            cells.append(cell)
            for offset in range(colspan):
                occupancy[(r_idx, c_idx + offset)] = cell["id"]
                if vmerge == "restart":
                    active_vmerge[c_idx + offset] = cell
                elif vmerge is None:
                    active_vmerge.pop(c_idx + offset, None)
            row_values.extend([text] + [""] * (colspan - 1))
            c_idx += colspan
            max_col = max(max_col, c_idx)
        while len(row_values) < max_col:
            row_values.append("")
        rows.append(row_values)

    for cell in cells:
        if int(cell.get("rowspan", 1)) > 1 or int(cell.get("colspan", 1)) > 1:
            merged_cells.append(
                {
                    "row": int(cell["row"]),
                    "col": int(cell["col"]),
                    "rowspan": int(cell.get("rowspan", 1)),
                    "colspan": int(cell.get("colspan", 1)),
                }
            )
    for row in rows:
        while len(row) < max_col:
            row.append("")
    col_widths = table_grid_widths(tbl, max_col)
    title = infer_table_title(rows, locator)
    ir = {
        "schema_version": "1.0",
        "table_id": table_id(index),
        "locator": locator,
        "title": title,
        "source": {
            "file": source.name,
            "source_type": "docx",
            "page": None,
            "section": "",
            "bbox": None,
        },
        "structure": {
            "rows": len(rows),
            "cols": max_col,
            "merged_cells": merged_cells,
            "is_cross_page": False,
            "has_diagonal_header": has_diagonal_header,
            "has_nested_table": has_nested_table,
            "merged_cell_count": len(merged_cells),
            "border_complexity": round(sum(border_complexities) / max(1, len(border_complexities)), 3),
        },
        "geometry": {"col_widths": col_widths, "row_heights": row_heights},
        "cells": cells,
        "rows": rows,
        "assets": {},
        "render_mode": "auto",
        "importance": {"is_important": False, "reason": ""},
    }
    ir["render_mode"] = choose_table_render_mode(ir)
    return ir


def infer_table_title(rows: list[list[str]], locator: str) -> str:
    for row in rows[:2]:
        values = [clean_text(cell) for cell in row if clean_text(cell)]
        if len(values) == 1 and re.search(r"^表\s*\d|^表\d|Table\s+\d", values[0], re.I):
            return values[0]
    return locator


def choose_table_render_mode(table: dict[str, Any]) -> str:
    source_type = str(table.get("source", {}).get("source_type", "")).lower()
    structure = table.get("structure", {})
    row_count = int(structure.get("rows") or table.get("row_count") or 0)
    col_count = int(structure.get("cols") or table.get("column_count") or 0)
    merged_count = int(structure.get("merged_cell_count") or len(structure.get("merged_cells") or []))
    border_complexity = float(structure.get("border_complexity") or 0.0)
    is_complex = (
        source_type in {"pdf_scan", "image_pdf"}
        or bool(structure.get("is_cross_page"))
        or bool(structure.get("has_diagonal_header"))
        or bool(structure.get("has_nested_table"))
        or row_count > 10
        or col_count > 6
        or merged_count >= 3
        or border_complexity > 0.6
    )
    if source_type in {"pdf_scan", "image_pdf"}:
        return "image"
    if is_complex and bool(table.get("importance", {}).get("is_important")):
        return "hybrid"
    if is_complex:
        return "image"
    return "native"


def render_docx_table_image(ir: dict[str, Any], output: Path, dpi: int = 220) -> None:
    if Image is None or ImageDraw is None or ImageFont is None:
        return
    col_widths = [float(v or 1.0) for v in ir.get("geometry", {}).get("col_widths", [])]
    row_heights = [float(v or 0.34) for v in ir.get("geometry", {}).get("row_heights", [])]
    rows = int(ir.get("structure", {}).get("rows") or len(row_heights))
    cols = int(ir.get("structure", {}).get("cols") or len(col_widths))
    if not col_widths:
        col_widths = [1.0] * max(1, cols)
    if not row_heights:
        row_heights = [0.34] * max(1, rows)
    scale = dpi
    x_edges = [24]
    for width in col_widths:
        x_edges.append(x_edges[-1] + max(42, int(width * scale)))
    y_edges = [24]
    for height in row_heights:
        y_edges.append(y_edges[-1] + max(36, int(height * scale)))
    image = Image.new("RGB", (x_edges[-1] + 24, y_edges[-1] + 24), "white")
    draw = ImageDraw.Draw(image)
    font_cache: dict[tuple[int, bool], Any] = {}

    def font(size_pt: float, bold: bool = False):
        key = (int(max(9, min(22, size_pt)) * dpi / 96), bold)
        if key not in font_cache:
            for name in ("msyhbd.ttc" if bold else "msyh.ttc", "simhei.ttf" if bold else "simsun.ttc", "arial.ttf"):
                try:
                    font_cache[key] = ImageFont.truetype(name, key[0])
                    break
                except OSError:
                    continue
            else:
                font_cache[key] = ImageFont.load_default()
        return font_cache[key]

    cell_map = {(int(c["row"]), int(c["col"])): c for c in ir.get("cells", [])}
    spanned: set[tuple[int, int]] = set()
    for cell in ir.get("cells", []):
        r0 = int(cell["row"])
        c0 = int(cell["col"])
        rs = int(cell.get("rowspan", 1))
        cs = int(cell.get("colspan", 1))
        for rr in range(r0, r0 + rs):
            for cc in range(c0, c0 + cs):
                if (rr, cc) != (r0, c0):
                    spanned.add((rr, cc))

    for r in range(rows):
        for c in range(cols):
            if (r, c) in spanned:
                continue
            cell = cell_map.get((r, c), {"rowspan": 1, "colspan": 1, "text": "", "style": {}})
            rs = int(cell.get("rowspan", 1))
            cs = int(cell.get("colspan", 1))
            x0 = x_edges[c]
            y0 = y_edges[r]
            x1 = x_edges[min(cols, c + cs)]
            y1 = y_edges[min(rows, r + rs)]
            style = cell.get("style", {})
            draw.rectangle([x0, y0, x1, y1], fill=str(style.get("fill", "#FFFFFF")), outline=str(style.get("border_color", "#000000")))
            text = clean_text(str(cell.get("text", "")))
            if text:
                fnt = font(float(style.get("font_size", 10.5)), bool(style.get("bold") or r == 0))
                max_chars = max(4, int((x1 - x0) / max(8, fnt.size * 0.58)))
                lines = wrap_text(text, max_chars)[: max(1, int((y1 - y0) / max(12, fnt.size + 4)))]
                line_h = fnt.size + 4
                total_h = line_h * len(lines)
                yy = y0 + max(4, int((y1 - y0 - total_h) / 2))
                for line in lines:
                    bbox = draw.textbbox((0, 0), line, font=fnt)
                    tw = bbox[2] - bbox[0]
                    align = style.get("align", "center")
                    if align == "right":
                        xx = x1 - tw - 8
                    elif align == "left":
                        xx = x0 + 8
                    else:
                        xx = x0 + max(4, int((x1 - x0 - tw) / 2))
                    draw.text((xx, yy), line, fill=str(style.get("color", "#000000")), font=fnt)
                    yy += line_h
    output.parent.mkdir(parents=True, exist_ok=True)
    image.save(output, "PNG")


def wrap_text(text: str, max_chars: int) -> list[str]:
    if len(text) <= max_chars:
        return [text]
    lines: list[str] = []
    current = ""
    for char in text:
        current += char
        if len(current) >= max_chars or char in "；;。":
            lines.append(current.strip())
            current = ""
    if current:
        lines.append(current.strip())
    return lines


def docx_tables_to_ir(source: Path, project: Path, start_index: int = 1) -> list[dict[str, Any]]:
    with zipfile.ZipFile(source) as archive:
        document = etree.fromstring(archive.read("word/document.xml"))
    tables = document.findall(".//w:tbl", namespaces=WORD_NS)
    records: list[dict[str, Any]] = []
    for offset, tbl in enumerate(tables):
        ir = parse_docx_table(tbl, source, start_index + offset)
        image_path = project / "tables" / f"{ir['table_id']}.png"
        render_docx_table_image(ir, image_path)
        if image_path.exists():
            ir["assets"]["crop_image"] = f"tables/{image_path.name}"
            ir["assets"]["source_table_image"] = f"tables/{image_path.name}"
        records.append(ir)
    return records


def pdf_tables_to_ir(source: Path, project: Path, start_index: int = 1, dpi: int = 300) -> list[dict[str, Any]]:
    if fitz is None:
        return []
    document = fitz.open(source)
    records: list[dict[str, Any]] = []
    next_index = start_index
    for page_number, page in enumerate(document, start=1):
        source_type = "pdf_scan" if not clean_text(page.get_text("text")) else "pdf"
        found = []
        if hasattr(page, "find_tables"):
            try:
                tables = page.find_tables()
                found = list(getattr(tables, "tables", []) or [])
            except Exception:
                found = []
        for table in found:
            bbox = [float(v) for v in getattr(table, "bbox", [])]
            if len(bbox) != 4:
                continue
            rows = []
            try:
                rows = table.extract() or []
            except Exception:
                rows = []
            tid = table_id(next_index)
            next_index += 1
            image_path = project / "tables" / f"{tid}.png"
            pix = page.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72), clip=fitz.Rect(bbox), alpha=False)
            image_path.parent.mkdir(parents=True, exist_ok=True)
            pix.save(str(image_path))
            row_count = len(rows)
            col_count = max((len(row) for row in rows), default=0)
            ir = {
                "schema_version": "1.0",
                "table_id": tid,
                "locator": f"PAGE{page_number:04d}-T{len(records) + 1:03d}",
                "title": f"PDF page {page_number} table",
                "source": {
                    "file": source.name,
                    "source_type": source_type,
                    "page": page_number,
                    "section": "",
                    "bbox": bbox,
                },
                "structure": {
                    "rows": row_count,
                    "cols": col_count,
                    "merged_cells": [],
                    "is_cross_page": False,
                    "has_diagonal_header": False,
                    "has_nested_table": False,
                    "merged_cell_count": 0,
                    "border_complexity": 1.0,
                },
                "geometry": {"col_widths": [], "row_heights": []},
                "cells": rows_to_cells(rows),
                "rows": rows,
                "assets": {"crop_image": f"tables/{image_path.name}", "source_table_image": f"tables/{image_path.name}"},
                "render_mode": "image",
                "importance": {"is_important": False, "reason": ""},
            }
            records.append(ir)
    return records


def rows_to_cells(rows: list[list[Any]]) -> list[dict[str, Any]]:
    cells = []
    for r, row in enumerate(rows or []):
        for c, value in enumerate(row or []):
            cells.append(
                {
                    "row": r,
                    "col": c,
                    "rowspan": 1,
                    "colspan": 1,
                    "text": clean_text("" if value is None else str(value)),
                    "style": {
                        "font_size": 10.5,
                        "bold": r == 0,
                        "align": "center",
                        "valign": "middle",
                        "fill": "#FFFFFF",
                        "border": "single",
                    },
                }
            )
    return cells


def build_table_ir(project: Path, sources: Iterable[Path]) -> dict[str, Any]:
    tables: list[dict[str, Any]] = []
    next_index = 1
    for source in sources:
        suffix = source.suffix.lower()
        if suffix == ".docx":
            records = docx_tables_to_ir(source, project, next_index)
        elif suffix == ".pdf":
            records = pdf_tables_to_ir(source, project, next_index)
        else:
            records = []
        tables.extend(records)
        next_index += len(records)
    return {
        "schema_version": "1.0",
        "description": "Deterministic table intermediate representation. LLM may reference table_id only; code owns structure, styles, screenshots, and render_mode.",
        "render_modes": ["native", "image", "hybrid", "auto"],
        "tables": tables,
        "by_table_id": {table["table_id"]: table for table in tables},
        "by_source_locator": {f"{table['source']['file']}::{table['locator']}": table for table in tables},
    }


def write_table_ir_for_sources(project: Path, sources: Iterable[Path]) -> dict[str, Any]:
    payload = build_table_ir(project, sources)
    analysis = project / "analysis"
    analysis.mkdir(parents=True, exist_ok=True)
    (analysis / "table_ir.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return payload


def legacy_models_from_ir(payload: dict[str, Any], source_file: str | None = None) -> dict[str, Any]:
    tables = []
    for table in payload.get("tables", []):
        if source_file and table.get("source", {}).get("file") != source_file:
            continue
        structure = table.get("structure", {})
        geometry = table.get("geometry", {})
        cells = []
        for cell in table.get("cells", []):
            cells.append(
                {
                    "id": f"{table.get('locator')}:r{cell.get('row')}c{cell.get('col')}",
                    "row": cell.get("row"),
                    "col": cell.get("col"),
                    "row_span": cell.get("rowspan", 1),
                    "col_span": cell.get("colspan", 1),
                    "text": cell.get("text", ""),
                    "is_header": cell.get("is_header", cell.get("row") == 0),
                    "style": cell.get("style", {}),
                }
            )
        tables.append(
            {
                "locator": table.get("locator"),
                "table_id": table.get("table_id"),
                "source": table.get("source", {}).get("file", ""),
                "row_count": structure.get("rows", 0),
                "column_count": structure.get("cols", 0),
                "grid_widths": [max(1, int(float(width) * DXA_PER_INCH)) for width in geometry.get("col_widths", [])],
                "row_heights": geometry.get("row_heights", []),
                "rows": table.get("rows", []),
                "cells": cells,
                "spans": [
                    {
                        "row": item.get("row"),
                        "col": item.get("col"),
                        "row_span": item.get("rowspan", 1),
                        "col_span": item.get("colspan", 1),
                    }
                    for item in structure.get("merged_cells", [])
                ],
                "has_merged_cells": bool(structure.get("merged_cells")),
                "render_mode": table.get("render_mode", "native"),
                "assets": table.get("assets", {}),
            }
        )
    return {
        "schema_version": "1.1",
        "source_file": source_file or "",
        "table_count": len(tables),
        "tables": tables,
        "by_locator": {table["locator"]: table for table in tables if table.get("locator")},
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("project", type=Path)
    parser.add_argument("--source", action="append", type=Path, default=[])
    args = parser.parse_args()
    project = args.project.resolve()
    sources = [path.resolve() for path in args.source if path and path.suffix.lower() in SUPPORTED_TABLE_SOURCES]
    if not sources:
        sources_root = project / "sources"
        if sources_root.exists():
            sources.extend(path.resolve() for path in sources_root.glob("*") if path.suffix.lower() in SUPPORTED_TABLE_SOURCES)
        sources.extend(path.resolve() for path in project.glob("*") if path.suffix.lower() in SUPPORTED_TABLE_SOURCES)
    unique = sorted({path: path for path in sources if path.exists()}.values(), key=lambda item: item.name.lower())
    payload = write_table_ir_for_sources(project, unique)
    print(json.dumps({"tables": len(payload.get("tables", [])), "output": str(project / "analysis" / "table_ir.json")}, ensure_ascii=False))


if __name__ == "__main__":
    main()
