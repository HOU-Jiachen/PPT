#!/usr/bin/env python3
"""Build report-content inventory and a PPT content blueprint.

This stage sits between source cataloging and slide planning. It recovers the
report's heading hierarchy, source paragraphs, table/figure captions, tables,
figures, and the first-pass PPT use of each object so the agent can reason over
content before authoring deck_plan.json or slides.
"""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime
from pathlib import Path
from typing import Any


KEY_TERMS = (
    "目的",
    "任务",
    "范围",
    "结论",
    "建议",
    "问题",
    "风险",
    "危险性",
    "预测",
    "验证",
    "涌水",
    "突水",
    "岩溶",
    "富水",
    "导水",
    "隔水",
    "径流",
    "补给",
    "排泄",
    "模型",
    "边界",
    "参数",
    "措施",
    "治理",
    "防治水",
)

LIST_MARKER_RE = re.compile(r"(?:^|[。；;\n]\s*)(（\d+）|\(\d+\)|\d+[、.．]|[①②③④⑤⑥⑦⑧⑨⑩])")
INLINE_ITEM_RE = re.compile(r"([①②③④⑤⑥⑦⑧⑨⑩]|[一二三四五六七八九十][是为、]|[；;]\s*[^；;。]{3,24}[：:])")

SOURCE_MODES = {
    "paragraph": "ORIGINAL_TEXT",
    "table": "ORIGINAL_TABLE",
    "figure": "ORIGINAL_FIGURE",
    "calculation": "CALCULATION",
}


def clean_text(value: str | None) -> str:
    return re.sub(r"\s+", " ", value or "").strip()


def text_preview(value: str | None, limit: int = 180) -> str:
    value = clean_text(value)
    return value if len(value) <= limit else value[: limit - 1] + "…"


def emphasis_candidates(text: str, max_items: int = 8) -> dict[str, list[str]]:
    """Return source-backed terms/numbers that should be visually emphasized later."""

    numbers = []
    for token in re.findall(r"[-+]?\d+(?:\.\d+)?\s*(?:%|万?m3|万?m³|km2|km²|hm2|hm²|m|km|万元|亿元|t|d|年|月|日)?", text):
        token = clean_text(token)
        if token and token not in numbers:
            numbers.append(token)

    terms = []
    for term in KEY_TERMS:
        if term in text and term not in terms:
            terms.append(term)
    for phrase in re.findall(r"(?:防治责任范围|水土流失|表土剥离|临时防护|排水沟|沉沙池|投资估算|监测时段|验收管理)", text):
        if phrase not in terms:
            terms.append(phrase)

    return {"numbers": numbers[:max_items], "terms": terms[:max_items]}


def split_numbered_segments(text: str, max_segments: int = 6) -> list[dict[str, str]]:
    """Detect report paragraphs that contain several speaker-worthy numbered segments."""

    matches = list(LIST_MARKER_RE.finditer(text))
    segments: list[dict[str, str]] = []
    if len(matches) < 2:
        inline_parts = [part.strip(" ，,；;。") for part in re.split(r"[；;]", text) if part.strip()]
        if len(inline_parts) >= 3 or INLINE_ITEM_RE.search(text):
            for index, body in enumerate(inline_parts[:max_segments], start=1):
                title = re.split(r"[：:，,。]", body, maxsplit=1)[0].strip()
                if len(title) > 18:
                    title = title[:18].rstrip()
                segments.append(
                    {
                        "number": f"{index:02d}",
                        "source_marker": "",
                        "title": title or f"要点{index}",
                        "text_preview": text_preview(body, 120),
                    }
                )
        return segments

    for index, match in enumerate(matches[:max_segments]):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        body = clean_text(text[start:end]).strip(" ；;。")
        if not body:
            continue
        title = re.split(r"[：:，,；;。]", body, maxsplit=1)[0].strip()
        if len(title) > 18:
            title = title[:18].rstrip()
        segments.append(
            {
                "number": f"{index + 1:02d}",
                "source_marker": match.group(1),
                "title": title or f"要点{index + 1}",
                "text_preview": text_preview(body, 120),
            }
        )
    return segments


def paragraph_structure(text: str, section_title: str) -> dict[str, Any]:
    segments = split_numbered_segments(text)
    return {
        "requires_numbered_segments": bool(segments),
        "segment_count": len(segments),
        "segment_title_basis": "report numbered paragraph leading phrases"
        if segments
        else "report section heading",
        "fallback_title": text_preview(section_title, 24),
        "suggested_segments": segments,
    }


def heading_level(entry: dict[str, Any]) -> int:
    style = str(entry.get("style") or "")
    match = re.search(r"heading\s*(\d+)", style, flags=re.I)
    if match:
        return int(match.group(1))
    return 6


def is_table_caption(entry: dict[str, Any]) -> bool:
    text = clean_text(entry.get("text"))
    return str(entry.get("style") or "") == "表名" or bool(re.match(r"^表\s*\d", text))


def is_figure_caption(entry: dict[str, Any]) -> bool:
    text = clean_text(entry.get("text"))
    return str(entry.get("style") or "") == "图名" or bool(re.match(r"^图\s*\d", text))


def strip_caption_prefix(text: str) -> str:
    text = clean_text(text)
    text = re.sub(r"^[图表]\s*\d+(?:\.\d+)?-\d+\s*", "", text)
    return text.strip(" ：:，,。") or text


def score_paragraph(text: str, entry: dict[str, Any]) -> tuple[int, list[str]]:
    score = 0
    reasons: list[str] = []
    if len(text) >= 80:
        score += 1
        reasons.append("long-report-paragraph")
    if len(text) >= 180:
        score += 1
        reasons.append("content-rich")
    if entry.get("numbers"):
        score += 2
        reasons.append("quantitative-values")
    matched_terms = [term for term in KEY_TERMS if term in text]
    if matched_terms:
        score += min(3, len(matched_terms))
        reasons.append("key-technical-terms:" + "、".join(matched_terms[:5]))
    if re.search(r"^(主要目的|主要任务|总体上|综上|建议|结论|存在问题|预测结果|计算结果)", text):
        score += 2
        reasons.append("report-emphasis-signal")
    if re.search(r"[（(]\d+[）)]|^\d+[.、]", text):
        score += 1
        reasons.append("enumerated-item")
    return score, reasons


def classify_paragraph(text: str) -> str:
    if any(term in text for term in ("公式", "计算", "参数", "模型")):
        return "calculation"
    return "paragraph"


def make_section(section_index: int, entry: dict[str, Any], stack: list[dict[str, Any]]) -> dict[str, Any]:
    level = heading_level(entry)
    title = clean_text(entry.get("text"))
    parent_titles = [item["title"] for item in stack if item["level"] < level]
    return {
        "id": f"SEC-{section_index:03d}",
        "level": level,
        "title": title,
        "heading_catalog_id": entry.get("id"),
        "source_locator": entry.get("locator"),
        "path_titles": parent_titles + [title],
        "important_paragraphs": [],
        "tables": [],
        "figures": [],
        "captions": [],
        "content_unit_ids": [],
    }


def fallback_section() -> dict[str, Any]:
    return {
        "id": "SEC-000",
        "level": 0,
        "title": "未分章前置内容",
        "heading_catalog_id": "",
        "source_locator": "",
        "path_titles": ["未分章前置内容"],
        "important_paragraphs": [],
        "tables": [],
        "figures": [],
        "captions": [],
        "content_unit_ids": [],
    }


def section_summary(section: dict[str, Any]) -> str:
    bits = []
    if section["important_paragraphs"]:
        bits.append(f"{len(section['important_paragraphs'])}段关键文字")
    if section["tables"]:
        bits.append(f"{len(section['tables'])}张表")
    if section["figures"]:
        bits.append(f"{len(section['figures'])}张图")
    return "、".join(bits) if bits else "仅标题或低密度材料"


def table_ppt_use(item: dict[str, Any]) -> dict[str, str]:
    rows = int(item.get("row_count") or len(item.get("rows") or []))
    cols = int(item.get("column_count") or max((len(row) for row in item.get("rows", [])), default=0))
    if rows > 12 or cols > 6:
        split = "拆分为重点行/重点列，必要时分两页呈现"
        layout = "left_table_right_text or top_text_bottom_table"
    else:
        split = "可整表呈现，并保留单位、脚注和口径"
        layout = "left_table_right_text"
    return {
        "slide_role": "source table with explanation",
        "layout_hint": layout,
        "split_hint": split,
    }


def figure_ppt_use(item: dict[str, Any]) -> dict[str, str]:
    return {
        "slide_role": "source figure/map/diagram with report-language explanation",
        "layout_hint": "left_figure_right_text or top_figure_bottom_text",
        "split_hint": "关键图件至少占页面45%，复杂图件可单页放大后接解释页",
    }


def paragraph_ppt_use(item: dict[str, Any]) -> dict[str, str]:
    kind = classify_paragraph(item["text"])
    if kind == "calculation":
        return {
            "slide_role": "calculation logic or parameter explanation",
            "layout_hint": "left_text_right_table or top_text_bottom_table",
            "split_hint": "公式、输入参数和结果分区呈现，不压缩为小字说明",
        }
    return {
        "slide_role": "source text / section context / faithful explanation",
        "layout_hint": "left_text_right_figure or text_with_keypoints",
        "split_hint": "长段落改写为3-5条报告原意要点，保留关键原文措辞",
    }


def build_inventory(catalog: dict[str, Any]) -> dict[str, Any]:
    sections: list[dict[str, Any]] = []
    content_units: list[dict[str, Any]] = []
    stack: list[dict[str, Any]] = []
    current = fallback_section()
    pending_caption: dict[str, str] | None = None
    section_index = 0

    for entry in catalog.get("entries", []):
        kind = str(entry.get("kind") or "")
        text = clean_text(entry.get("text"))
        if not text:
            continue

        if kind == "heading":
            section_index += 1
            level = heading_level(entry)
            stack = [item for item in stack if item["level"] < level]
            current = make_section(section_index, entry, stack)
            sections.append(current)
            stack.append(current)
            pending_caption = None
            continue

        if current["id"] == "SEC-000" and current not in sections:
            sections.append(current)

        if kind == "paragraph" and (is_table_caption(entry) or is_figure_caption(entry)):
            caption_kind = "table" if is_table_caption(entry) else "figure"
            pending_caption = {
                "catalog_id": entry.get("id", ""),
                "kind": caption_kind,
                "title": strip_caption_prefix(text),
                "raw_text": text,
                "source_locator": entry.get("locator", ""),
            }
            current["captions"].append(pending_caption)
            continue

        if kind == "paragraph":
            score, reasons = score_paragraph(text, entry)
            if score >= 2:
                item = {
                    "catalog_id": entry.get("id"),
                    "source_locator": entry.get("locator"),
                    "text": text,
                    "text_preview": text_preview(text),
                    "numbers": entry.get("numbers", []),
                    "importance_score": score,
                    "reasons": reasons,
                    "paragraph_structure": paragraph_structure(text, current["title"]),
                    "emphasis_candidates": emphasis_candidates(text),
                    "ppt_use": paragraph_ppt_use({"text": text}),
                }
                current["important_paragraphs"].append(item)
                unit_id = f"UNIT-{len(content_units) + 1:04d}"
                item["content_unit_id"] = unit_id
                content_units.append(
                    content_unit(unit_id, current, "paragraph", item, [entry.get("id")])
                )
            continue

        if kind == "table":
            caption = pending_caption if pending_caption and pending_caption["kind"] == "table" else None
            item = {
                "catalog_id": entry.get("id"),
                "source_locator": entry.get("locator"),
                "caption": caption["title"] if caption else "",
                "caption_catalog_id": caption["catalog_id"] if caption else "",
                "row_count": entry.get("row_count", len(entry.get("rows", []))),
                "column_count": entry.get("column_count", 0),
                "text_preview": text_preview(text, 260),
                "numbers": entry.get("numbers", []),
                "emphasis_candidates": emphasis_candidates(text),
                "ppt_use": table_ppt_use(entry),
            }
            current["tables"].append(item)
            unit_id = f"UNIT-{len(content_units) + 1:04d}"
            item["content_unit_id"] = unit_id
            ids = [entry.get("id")]
            if caption:
                ids.append(caption["catalog_id"])
            content_units.append(content_unit(unit_id, current, "table", item, ids))
            pending_caption = None
            continue

        if kind in {"figure", "image"}:
            caption = pending_caption if pending_caption and pending_caption["kind"] == "figure" else None
            item = {
                "catalog_id": entry.get("id"),
                "source_locator": entry.get("locator"),
                "caption": caption["title"] if caption else "",
                "caption_catalog_id": caption["catalog_id"] if caption else "",
                "asset": entry.get("asset", ""),
                "text_preview": text_preview(text, 220),
                "emphasis_candidates": emphasis_candidates(text),
                "ppt_use": figure_ppt_use(entry),
            }
            current["figures"].append(item)
            unit_id = f"UNIT-{len(content_units) + 1:04d}"
            item["content_unit_id"] = unit_id
            ids = [entry.get("id")]
            if caption:
                ids.append(caption["catalog_id"])
            content_units.append(content_unit(unit_id, current, "figure", item, ids))
            pending_caption = None

    for unit in content_units:
        section = next((item for item in sections if item["id"] == unit["section_id"]), None)
        if section is not None:
            section["content_unit_ids"].append(unit["id"])

    return {
        "schema_version": "1.0",
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "source_catalog": "analysis/source_catalog.json",
        "summary": {
            "sections": len(sections),
            "important_paragraphs": sum(len(item["important_paragraphs"]) for item in sections),
            "tables": sum(len(item["tables"]) for item in sections),
            "figures": sum(len(item["figures"]) for item in sections),
            "content_units": len(content_units),
        },
        "sections": sections,
        "content_units": content_units,
    }


def content_unit(
    unit_id: str,
    section: dict[str, Any],
    kind: str,
    item: dict[str, Any],
    catalog_ids: list[str | None],
) -> dict[str, Any]:
    title = item.get("caption") or section["title"]
    if kind == "paragraph":
        title = section["title"]
    mode = SOURCE_MODES.get("calculation" if kind == "paragraph" and "calculation" in item["ppt_use"]["slide_role"] else kind, "ORIGINAL_TEXT")
    return {
        "id": unit_id,
        "section_id": section["id"],
        "section_path": section["path_titles"],
        "title_basis": title,
        "source_mode": mode,
        "catalog_ids": [value for value in catalog_ids if value],
        "candidate_slide_title": text_preview(title, 42),
        "narrative_role": item["ppt_use"]["slide_role"],
        "layout_hint": item["ppt_use"]["layout_hint"],
        "split_hint": item["ppt_use"]["split_hint"],
        "content_preview": item.get("text_preview") or item.get("caption") or "",
        "paragraph_structure": item.get("paragraph_structure", {}),
        "emphasis_candidates": item.get("emphasis_candidates", {}),
    }


def write_blueprint(project: Path, inventory: dict[str, Any]) -> None:
    path = project / "analysis" / "ppt_content_blueprint.md"
    summary = inventory["summary"]
    lines = [
        "# PPT Content Blueprint",
        "",
        "This blueprint is the mandatory thinking workspace between report extraction and slide planning.",
        "The agent must read it, refine the narrative, and then derive `evidence_ledger.json`,",
        "`chapter_coverage.md`, and `deck_plan.json` from the selected content units.",
        "",
        "## Inventory Summary",
        "",
        f"- Sections: {summary['sections']}",
        f"- Important paragraphs: {summary['important_paragraphs']}",
        f"- Tables: {summary['tables']}",
        f"- Figures: {summary['figures']}",
        f"- PPT content units: {summary['content_units']}",
        "",
        "## Thinking Rules",
        "",
        "- Preserve the report's title hierarchy before summarizing.",
        "- Treat table and figure captions as the default small-title source.",
        "- Pair source objects with faithful explanation; do not replace technical process with summary cards.",
        "- Split dense tables, long formulas, and complex maps before reducing font size.",
        "- When one source paragraph contains several numbered or semicolon-separated points, keep visible item numbers and short item names.",
        "- Mark key report terms, controlling values, units, conclusions, and risk words for bold/color/highlight treatment in the visible slide.",
        "- Every planned slide should point back to one or more content unit IDs or explain why no source object exists.",
        "",
        "## Content Units By Report Section",
        "",
    ]
    units_by_section: dict[str, list[dict[str, Any]]] = {}
    for unit in inventory["content_units"]:
        units_by_section.setdefault(unit["section_id"], []).append(unit)

    for section in inventory["sections"]:
        units = units_by_section.get(section["id"], [])
        if not units:
            continue
        path_title = " > ".join(section["path_titles"])
        lines.extend(
            [
                f"### {section['id']} {path_title}",
                "",
                f"- Source locator: {section.get('source_locator', '')}",
                f"- Material density: {section_summary(section)}",
                "- Agent synthesis draft before slide planning:",
                f"  - Audience-facing point: explain `{section['title']}` through source evidence, not a generic summary.",
                f"  - Must-keep original wording/data: {must_keep_summary(units)}",
                f"  - Best source pairing: {layout_summary(units)}",
                f"  - Slide split decision: {split_summary(units)}",
                f"  - Text structure and emphasis: {structure_summary(units)}",
                "",
                "| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |",
                "| --- | --- | --- | --- | --- | --- |",
            ]
        )
        for unit in units[:12]:
            lines.append(
                "| {id} | {mode} | {title} | {role} | {layout} | {catalog} |".format(
                    id=unit["id"],
                    mode=unit["source_mode"],
                    title=unit["candidate_slide_title"].replace("|", "；"),
                    role=unit["narrative_role"].replace("|", "；"),
                    layout=unit["layout_hint"].replace("|", "；"),
                    catalog=", ".join(unit["catalog_ids"]),
                )
            )
        if len(units) > 12:
            lines.append(f"| ... | ... | Additional {len(units) - 12} units in JSON inventory | ... | ... | ... |")
        lines.append("")

    lines.extend(
        [
            "## Deck Planning Gate",
            "",
            "Before authoring slides, update or review `deck_plan.json` so every substantive page is derived",
            "from selected content units, with report-native headings/captions used for visible small titles.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def must_keep_summary(units: list[dict[str, Any]]) -> str:
    if not units:
        return "none"
    picks = []
    for unit in units[:5]:
        label = unit["candidate_slide_title"] or unit["id"]
        picks.append(f"{unit['id']} {label}")
    return "；".join(picks)


def layout_summary(units: list[dict[str, Any]]) -> str:
    layouts = []
    for unit in units:
        layout = unit.get("layout_hint", "")
        if layout and layout not in layouts:
            layouts.append(layout)
    return "；".join(layouts[:3]) if layouts else "text_with_keypoints"


def split_summary(units: list[dict[str, Any]]) -> str:
    dense_tables = [unit for unit in units if unit["source_mode"] == "ORIGINAL_TABLE"]
    figures = [unit for unit in units if unit["source_mode"] == "ORIGINAL_FIGURE"]
    if len(units) >= 8:
        return "material is dense; split into source context, original object pages, and chapter conclusion."
    if dense_tables and figures:
        return "use separate table and figure pages, then connect them with one interpretation page if needed."
    if dense_tables:
        return "split or crop tables before reducing font size."
    if figures:
        return "reserve at least 45% of slide area for key figures."
    return "one source-text page may be sufficient if evidence remains readable."


def structure_summary(units: list[dict[str, Any]]) -> str:
    structured = [
        unit
        for unit in units
        if unit.get("paragraph_structure", {}).get("requires_numbered_segments")
    ]
    emphasized = []
    for unit in units:
        candidates = unit.get("emphasis_candidates", {})
        emphasized.extend(candidates.get("terms", [])[:2])
        emphasized.extend(candidates.get("numbers", [])[:2])
    pieces = []
    if structured:
        pieces.append(f"{len(structured)}个文字单元需要保留编号与短标题")
    if emphasized:
        pieces.append("重点强调：" + "、".join(dict.fromkeys(emphasized[:8])))
    return "；".join(pieces) if pieces else "常规短句呈现，保留关键数据与工程名词强调。"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("project", type=Path)
    args = parser.parse_args()
    project = args.project.resolve()
    catalog_path = project / "analysis" / "source_catalog.json"
    if not catalog_path.exists():
        raise SystemExit("Missing analysis/source_catalog.json. Run catalog first.")
    catalog = json.loads(catalog_path.read_text(encoding="utf-8-sig"))
    inventory = build_inventory(catalog)
    output = project / "analysis" / "report_content_inventory.json"
    output.write_text(json.dumps(inventory, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_blueprint(project, inventory)
    print(
        json.dumps(
            {
                "inventory": str(output),
                "blueprint": str(project / "analysis" / "ppt_content_blueprint.md"),
                **inventory["summary"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
