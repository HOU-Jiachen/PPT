#!/usr/bin/env python3
"""Extract DOCX table structure, including merged cells, into a PPT-friendly model."""

from __future__ import annotations

import argparse
import json
import re
import zipfile
from pathlib import Path
from typing import Any
from xml.etree import ElementTree as ET


NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
W_NS = NS["w"]


def w_tag(name: str) -> str:
    return f"{{{W_NS}}}{name}"


def attr(element: ET.Element, name: str) -> str | None:
    return element.attrib.get(w_tag(name))


def clean_text(value: str) -> str:
    value = re.sub(r"\s+", " ", value or "")
    return value.strip()


def cell_text(tc: ET.Element) -> str:
    parts: list[str] = []
    for text in tc.findall(".//w:t", NS):
        if text.text:
            parts.append(text.text)
    return clean_text("".join(parts))


def grid_span(tc: ET.Element) -> int:
    node = tc.find("./w:tcPr/w:gridSpan", NS)
    if node is None:
        return 1
    try:
        return max(1, int(attr(node, "val") or "1"))
    except ValueError:
        return 1


def vmerge_state(tc: ET.Element) -> str | None:
    node = tc.find("./w:tcPr/w:vMerge", NS)
    if node is None:
        return None
    return attr(node, "val") or "continue"


def grid_widths(tbl: ET.Element) -> list[int]:
    values: list[int] = []
    for grid_col in tbl.findall("./w:tblGrid/w:gridCol", NS):
        try:
            values.append(max(1, int(attr(grid_col, "w") or "1")))
        except ValueError:
            values.append(1)
    return values


def parse_table(tbl: ET.Element, locator: str, source: str) -> dict[str, Any]:
    rows_xml = tbl.findall("./w:tr", NS)
    row_count = len(rows_xml)
    cells: list[dict[str, Any]] = []
    rows: list[list[str]] = []
    occupancy: dict[tuple[int, int], str] = {}
    active_vmerge: dict[int, dict[str, Any]] = {}
    max_col = 0

    for r_idx, tr in enumerate(rows_xml):
        row_values: list[str] = []
        c_idx = 0
        for tc in tr.findall("./w:tc", NS):
            while (r_idx, c_idx) in occupancy:
                row_values.append("")
                c_idx += 1

            colspan = grid_span(tc)
            vmerge = vmerge_state(tc)
            text = cell_text(tc)

            if vmerge == "continue" and c_idx in active_vmerge:
                origin = active_vmerge[c_idx]
                if origin["row"] + origin["row_span"] == r_idx:
                    origin["row_span"] += 1
                for offset in range(origin["col_span"]):
                    occupancy[(r_idx, origin["col"] + offset)] = origin["id"]
                row_values.extend([""] * origin["col_span"])
                c_idx = origin["col"] + origin["col_span"]
                max_col = max(max_col, c_idx)
                continue

            cell_id = f"{locator}:r{r_idx}c{c_idx}"
            cell = {
                "id": cell_id,
                "row": r_idx,
                "col": c_idx,
                "row_span": 1,
                "col_span": colspan,
                "text": text,
                "is_header": r_idx == 0,
                "vmerge": vmerge,
            }
            cells.append(cell)

            for offset in range(colspan):
                occupancy[(r_idx, c_idx + offset)] = cell_id
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

    for row_values in rows:
        while len(row_values) < max_col:
            row_values.append("")

    spans = [
        {
            "row": cell["row"],
            "col": cell["col"],
            "row_span": cell["row_span"],
            "col_span": cell["col_span"],
        }
        for cell in cells
        if cell["row_span"] > 1 or cell["col_span"] > 1
    ]
    return {
        "locator": locator,
        "source": source,
        "row_count": row_count,
        "column_count": max_col,
        "grid_widths": grid_widths(tbl),
        "rows": rows,
        "cells": cells,
        "spans": spans,
        "has_merged_cells": bool(spans),
    }


def parse_docx_tables(docx_path: Path) -> list[dict[str, Any]]:
    with zipfile.ZipFile(docx_path) as archive:
        document_xml = archive.read("word/document.xml")
    root = ET.fromstring(document_xml)
    tables = root.findall(".//w:tbl", NS)
    source = docx_path.name
    return [parse_table(tbl, f"T{index:03d}", source) for index, tbl in enumerate(tables, start=1)]


def write_docx_table_models(docx_path: Path, output_path: Path) -> dict[str, Any]:
    models = parse_docx_tables(docx_path)
    payload = {
        "schema_version": "1.0",
        "source_file": docx_path.name,
        "table_count": len(models),
        "tables": models,
        "by_locator": {table["locator"]: table for table in models},
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("docx", type=Path)
    parser.add_argument("-o", "--output", type=Path, required=True)
    args = parser.parse_args()
    payload = write_docx_table_models(args.docx, args.output)
    print(json.dumps({"tables": payload["table_count"], "output": str(args.output)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
