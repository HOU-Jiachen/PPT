#!/usr/bin/env python3
"""Reusable helpers for source-faithful engineering review PPTX generation.

Project scripts should orchestrate project-specific page choices. Shared behavior
such as template profiling, visible-text hygiene, source evidence extraction, and
basic PPTX drawing belongs here so each project does not grow a one-off runtime.
"""

from __future__ import annotations

import json
import re
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any

from PIL import Image
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE_TYPE
from pptx.enum.text import MSO_AUTO_SIZE, PP_ALIGN
from pptx.util import Inches, Pt


DEFAULT_COLORS = {
    "bg": "F7F9FC",
    "paper": "FFFFFF",
    "ink": "01203C",
    "muted": "566B7F",
    "primary": "01203C",
    "secondary": "EAF2F8",
    "accent": "4489C8",
    "line": "CCD8E2",
    "soft": "F1F6FA",
    "good": "2E7D32",
    "warn": "A33A2B",
}

INTERNAL_VISIBLE_PATTERNS = [
    r"来源模式[:：]?\s*\S+",
    r"证据编号[:：]?\s*\S+",
    r"本页用于[:：]?.*",
    r"原表定位[:：]?.*",
    r"行列规模[:：]?.*",
    r"密集表按重点行重排.*",
    r"完整数据回看报告原表.*",
    r"\bE-\d(?:-[A-Z0-9]+)+\b",
    r"\bimage_\d+\.(?:png|jpe?g|wmf|emf)\b",
]


def rgb(hex_color: str) -> RGBColor:
    h = hex_color.strip("#")
    return RGBColor(int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16))


def pt(value: float):
    return Pt(value)


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def sanitize_visible_text(text: str) -> str:
    text = re.sub(r"\s+", " ", text or "").strip()
    text = re.sub(r"\s*\|\s*", "；", text)
    for pattern in INTERNAL_VISIBLE_PATTERNS:
        text = re.sub(pattern, "", text, flags=re.I)
    text = text.replace("证据解读", "报告说明")
    return re.sub(r"\s+", " ", text).strip(" ，,;；")


def text_preview(text: str, max_len: int = 480) -> str:
    text = sanitize_visible_text(text)
    return text if len(text) <= max_len else text[: max_len - 1] + "…"


def split_report_points(text: str, max_points: int = 5, max_len: int = 130) -> list[str]:
    text = sanitize_visible_text(text)
    if not text:
        return []
    sentences = [item.strip(" ；;。") for item in re.split(r"[。；;]\s*", text) if item.strip()]
    if len(sentences) <= 1:
        sentences = [item.strip() for item in re.split(r"，|,\s*", text) if item.strip()]

    points: list[str] = []
    current = ""
    for sentence in sentences:
        candidate = sentence if not current else f"{current}；{sentence}"
        if len(candidate) <= max_len:
            current = candidate
            continue
        if current:
            points.append(text_preview(current, max_len))
        current = sentence
        if len(points) >= max_points:
            break
    if current and len(points) < max_points:
        points.append(text_preview(current, max_len))
    return points[:max_points] or [text_preview(text, max_len)]


def report_heading(source_mode: str) -> str:
    mode = source_mode.upper()
    if mode == "ORIGINAL_FIGURE":
        return "报告对图件的说明"
    if mode == "ORIGINAL_TABLE":
        return "报告对表格的说明"
    if mode == "CALCULATION":
        return "报告计算口径"
    if mode in {"CONCLUSION", "RECOMMENDATION", "MANAGEMENT_ACTION"}:
        return "报告结论与建议"
    return "报告阐述"


def template_pptx(project_dir: Path) -> Path | None:
    candidates = sorted((project_dir / "template").glob("*.pptx"))
    return candidates[0] if candidates else None


def iter_shapes(shapes):
    for shape in shapes:
        yield shape
        if getattr(shape, "shape_type", None) == MSO_SHAPE_TYPE.GROUP and hasattr(shape, "shapes"):
            yield from iter_shapes(shape.shapes)


def collect_template_profile(project_dir: Path) -> dict[str, Any]:
    path = template_pptx(project_dir)
    if not path:
        return {"available": False}
    try:
        prs = Presentation(path)
    except Exception as exc:
        return {"available": False, "error": str(exc)}

    fonts: Counter[str] = Counter()
    sizes: Counter[float] = Counter()
    text_colors: Counter[str] = Counter()
    fill_colors: Counter[str] = Counter()
    picture_counts: Counter[int] = Counter()
    table_counts: Counter[int] = Counter()
    layout_keys: Counter[tuple[int, int, int]] = Counter()
    samples: list[dict[str, Any]] = []

    for index, slide in enumerate(prs.slides, start=1):
        pictures = 0
        tables = 0
        texts: list[str] = []
        text_count = 0
        for shape in iter_shapes(slide.shapes):
            if getattr(shape, "shape_type", None) == MSO_SHAPE_TYPE.PICTURE:
                pictures += 1
            if getattr(shape, "has_table", False):
                tables += 1
            try:
                fill = shape.fill
                if fill and fill.type and fill.fore_color.type == 1:
                    fill_colors[str(fill.fore_color.rgb)] += 1
            except Exception:
                pass
            if getattr(shape, "has_text_frame", False):
                value = shape.text.strip()
                if value:
                    text_count += 1
                    texts.append(value.replace("\n", " | ")[:120])
                for paragraph in shape.text_frame.paragraphs:
                    for run in paragraph.runs:
                        if run.font.name:
                            fonts[run.font.name] += 1
                        if run.font.size:
                            sizes[round(run.font.size.pt, 1)] += 1
                        try:
                            if run.font.color.rgb:
                                text_colors[str(run.font.color.rgb)] += 1
                        except Exception:
                            pass
        picture_counts[pictures] += 1
        table_counts[tables] += 1
        layout_keys[(min(pictures, 4), min(tables, 2), min(text_count, 8))] += 1
        if index <= 12 or index == len(prs.slides):
            samples.append(
                {
                    "slide": index,
                    "pictures": pictures,
                    "tables": tables,
                    "sample_text": texts[:5],
                }
            )

    return {
        "available": True,
        "path": str(path.relative_to(project_dir)),
        "slide_count": len(prs.slides),
        "canvas_inches": [
            round(prs.slide_width / 914400, 3),
            round(prs.slide_height / 914400, 3),
        ],
        "dominant_fonts": fonts.most_common(12),
        "dominant_font_sizes": sizes.most_common(12),
        "dominant_text_colors": text_colors.most_common(12),
        "dominant_fill_colors": fill_colors.most_common(12),
        "picture_count_distribution": picture_counts.most_common(),
        "table_count_distribution": table_counts.most_common(),
        "layout_keys": [
            {"pictures": k[0], "tables": k[1], "text_boxes": k[2], "count": v}
            for k, v in layout_keys.most_common(16)
        ],
        "sample_slides": samples,
        "adopted_rules": [
            "16:9 canvas, deep-blue technical review identity",
            "large section titles and restrained body text",
            "source figures shown without asset filenames or extraction IDs",
            "dense tables are split or simplified into readable key rows",
            "engineering report pages pair original evidence with report-facing explanation",
        ],
    }


def extract_figure_ids(text: str) -> list[str]:
    normalized = (text or "").replace("\\", "")
    return re.findall(r"图\s*\d+(?:\.\d+)?-\d+", normalized)


def figure_image_index(markdown_path: Path) -> dict[str, list[str]]:
    if not markdown_path.exists():
        return {}
    lines = markdown_path.read_text(encoding="utf-8").splitlines()
    index: dict[str, list[str]] = {}
    pending_images: list[str] = []
    image_re = re.compile(r"image_\d+\.(?:png|jpe?g|wmf)", re.I)
    for line in lines:
        names = image_re.findall(line)
        if names:
            pending_images = names
        figure_ids = extract_figure_ids(line)
        if figure_ids and pending_images:
            for figure_id in figure_ids:
                index.setdefault(figure_id, [])
                for name in pending_images:
                    if name not in index[figure_id]:
                        index[figure_id].append(name)
            pending_images = []
    return index


def image_paths_from_text(
    media_dir: Path,
    text: str,
    figure_index: dict[str, list[str]] | None = None,
) -> list[Path]:
    names = re.findall(r"image_\d+\.(?:png|jpe?g|wmf)", text, flags=re.I)
    if figure_index:
        for figure_id in extract_figure_ids(text):
            names.extend(figure_index.get(figure_id, []))
    paths: list[Path] = []
    seen: set[Path] = set()
    for name in names:
        path = media_dir / name
        if path.exists() and path.suffix.lower() != ".wmf" and path not in seen:
            seen.add(path)
            paths.append(path)
    return paths


def evidence_lookup(ledger: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {item["id"]: item for item in ledger["evidence"]}


def slide_evidence(page: dict[str, Any], ev_by_id: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    return [ev_by_id[eid] for eid in page.get("evidence_ids", []) if eid in ev_by_id]


def table_from_catalog(
    catalog_entries: dict[str, dict[str, Any]],
    evidence: list[dict[str, Any]],
) -> dict[str, Any] | None:
    for ev in evidence:
        for catalog_id in ev.get("catalog_ids", []):
            entry = catalog_entries.get(catalog_id)
            if entry and entry.get("kind") == "table" and entry.get("rows"):
                return entry
    return None


def report_text_from_evidence(
    evidence: list[dict[str, Any]],
    catalog_entries: dict[str, dict[str, Any]],
    max_len: int = 620,
) -> str:
    parts: list[str] = []
    seen: set[str] = set()

    def add(value: str | None) -> None:
        value = sanitize_visible_text(value or "")
        if not value or value in seen:
            return
        seen.add(value)
        parts.append(value)

    for ev in evidence:
        add(ev.get("exact_text"))
    for ev in evidence:
        for catalog_id in ev.get("catalog_ids", []):
            entry = catalog_entries.get(catalog_id)
            if entry and entry.get("kind") == "paragraph":
                add(entry.get("text"))
    for ev in evidence:
        add(ev.get("summary"))

    return text_preview(" ".join(parts), max_len)


def report_points_from_evidence(
    evidence: list[dict[str, Any]],
    catalog_entries: dict[str, dict[str, Any]],
    max_points: int = 5,
) -> list[str]:
    points: list[str] = []
    seen: set[str] = set()

    for ev in evidence:
        raw = ev.get("exact_text") or ev.get("summary") or ""
        if ev.get("summary") and (
            str(ev.get("kind", "")).upper() in {"ORIGINAL_TABLE", "CALCULATION"}
            or "..." in str(raw)
        ):
            raw = ev.get("summary")
        value = sanitize_visible_text(raw)
        if value and value not in seen:
            seen.add(value)
            points.append(text_preview(value, 132))
        if len(points) >= max_points:
            return points

    if not points:
        merged = report_text_from_evidence(evidence, catalog_entries, max_len=680)
        points = split_report_points(merged, max_points=max_points)
    return points[:max_points]


def add_textbox(
    slide,
    x,
    y,
    w,
    h,
    text,
    size=18,
    color="ink",
    bold=False,
    align=None,
    font="Microsoft YaHei",
    colors: dict[str, str] | None = None,
):
    palette = colors or DEFAULT_COLORS
    box = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = box.text_frame
    tf.clear()
    tf.word_wrap = True
    tf.auto_size = MSO_AUTO_SIZE.NONE
    p = tf.paragraphs[0]
    p.text = sanitize_visible_text(text)
    p.font.name = font
    p.font.size = pt(size)
    p.font.bold = bold
    p.font.color.rgb = rgb(palette[color])
    if align:
        p.alignment = align
    return box


def add_fill(slide, x, y, w, h, color="paper", line="line", colors: dict[str, str] | None = None):
    palette = colors or DEFAULT_COLORS
    shape = slide.shapes.add_shape(1, Inches(x), Inches(y), Inches(w), Inches(h))
    shape.fill.solid()
    shape.fill.fore_color.rgb = rgb(palette[color])
    shape.line.color.rgb = rgb(palette[line])
    shape.line.width = Pt(0.6)
    return shape


def add_title(slide, page: dict[str, Any], colors: dict[str, str] | None = None):
    palette = colors or DEFAULT_COLORS
    add_textbox(slide, 0.42, 0.20, 11.85, 0.50, page["title"], 24, "ink", True, colors=palette)
    add_textbox(slide, 0.43, 0.68, 7.0, 0.24, page["chapter"], 9.5, "accent", colors=palette)
    add_textbox(
        slide,
        11.65,
        0.66,
        0.7,
        0.20,
        f"{page['page']:02d}",
        9,
        "muted",
        align=PP_ALIGN.RIGHT,
        colors=palette,
    )
    line = slide.shapes.add_shape(1, Inches(0.42), Inches(0.88), Inches(11.84), Inches(0.015))
    line.fill.solid()
    line.fill.fore_color.rgb = rgb(palette["accent"])
    line.line.fill.background()


def add_footer(slide, source_note: str, colors: dict[str, str] | None = None):
    if source_note:
        add_textbox(slide, 0.45, 6.95, 11.5, 0.22, f"资料来源：{source_note}", 8.5, "muted", colors=colors)


def add_table(
    slide,
    entry: dict[str, Any],
    x,
    y,
    w,
    h,
    max_rows=8,
    max_cols=5,
    colors: dict[str, str] | None = None,
):
    palette = colors or DEFAULT_COLORS
    rows = entry.get("rows") or []
    if not rows:
        add_textbox(slide, x, y, w, h, text_preview(entry.get("text", ""), 720), 13, "ink", colors=palette)
        return None
    clean = [[text_preview(str(cell), 70) for cell in row[:max_cols]] for row in rows[:max_rows]]
    col_count = max(len(row) for row in clean) if clean else 1
    for row in clean:
        while len(row) < col_count:
            row.append("")
    shape = slide.shapes.add_table(len(clean), col_count, Inches(x), Inches(y), Inches(w), Inches(h))
    table = shape.table
    for i, row in enumerate(clean):
        for j, cell_text in enumerate(row):
            cell = table.cell(i, j)
            cell.text = cell_text
            for paragraph in cell.text_frame.paragraphs:
                paragraph.font.name = "Microsoft YaHei"
                paragraph.font.size = pt(10.5 if len(clean) > 6 or col_count > 4 else 12)
                paragraph.font.color.rgb = rgb(palette["ink"])
                if i == 0:
                    paragraph.font.bold = True
            cell.fill.solid()
            cell.fill.fore_color.rgb = rgb(palette["secondary"] if i == 0 else "FFFFFF")
    return shape


def add_image(slide, path: Path, x, y, w, h, colors: dict[str, str] | None = None):
    try:
        with Image.open(path) as im:
            iw, ih = im.size
    except Exception:
        add_textbox(slide, x, y, w, h, "报告图件暂无法嵌入", 14, "warn", colors=colors)
        return
    ratio = iw / ih
    box_ratio = w / h
    if ratio > box_ratio:
        final_w = w
        final_h = w / ratio
        final_x = x
        final_y = y + (h - final_h) / 2
    else:
        final_h = h
        final_w = h * ratio
        final_x = x + (w - final_w) / 2
        final_y = y
    slide.shapes.add_picture(
        str(path),
        Inches(final_x),
        Inches(final_y),
        width=Inches(final_w),
        height=Inches(final_h),
    )


def add_image_panel(
    slide,
    paths: list[Path],
    x,
    y,
    w,
    h,
    colors: dict[str, str] | None = None,
):
    palette = colors or DEFAULT_COLORS
    if not paths:
        add_fill(slide, x, y, w, h, "soft", colors=palette)
        add_textbox(
            slide,
            x + 0.25,
            y + 0.25,
            w - 0.5,
            h - 0.5,
            "报告相关图件",
            18,
            "muted",
            True,
            align=PP_ALIGN.CENTER,
            colors=palette,
        )
        return
    n = min(len(paths), 4)
    if n == 1:
        add_fill(slide, x, y, w, h, "paper", colors=palette)
        add_image(slide, paths[0], x + 0.08, y + 0.08, w - 0.16, h - 0.16, colors=palette)
        return

    ratios = []
    for path in paths[:n]:
        try:
            with Image.open(path) as im:
                ratios.append(im.size[0] / im.size[1])
        except Exception:
            pass
    if n <= 3 and ratios and sum(ratios) / len(ratios) > 2.4:
        cols = 1
        rows = n
    else:
        cols = 2
        rows = 1 if n <= 2 else 2
    gap = 0.12
    cell_w = (w - gap * (cols - 1)) / cols
    cell_h = (h - gap * (rows - 1)) / rows
    for idx, path in enumerate(paths[:n]):
        cx = x + (idx % cols) * (cell_w + gap)
        cy = y + (idx // cols) * (cell_h + gap)
        add_fill(slide, cx, cy, cell_w, cell_h, "paper", colors=palette)
        add_image(slide, path, cx + 0.05, cy + 0.05, cell_w - 0.1, cell_h - 0.1, colors=palette)


def add_bullets(
    slide,
    x,
    y,
    w,
    h,
    items: list[str],
    size=13,
    colors: dict[str, str] | None = None,
):
    palette = colors or DEFAULT_COLORS
    box = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = box.text_frame
    tf.clear()
    tf.word_wrap = True
    tf.auto_size = MSO_AUTO_SIZE.NONE
    for idx, item in enumerate(items):
        paragraph = tf.paragraphs[0] if idx == 0 else tf.add_paragraph()
        paragraph.text = sanitize_visible_text(item)
        paragraph.level = 0
        paragraph.font.name = "Microsoft YaHei"
        paragraph.font.size = pt(size)
        paragraph.font.color.rgb = rgb(palette["ink"])
        paragraph.space_after = pt(4)
    return box


def add_agenda_slide(
    slide,
    plan: dict[str, Any],
    page: dict[str, Any],
    colors: dict[str, str] | None = None,
) -> None:
    palette = colors or DEFAULT_COLORS
    add_fill(slide, 0, 0, 13.333, 7.5, "paper", "paper", colors=palette)
    add_textbox(slide, 0.75, 0.62, 5.8, 0.62, "目录", 30, "primary", True, colors=palette)
    add_textbox(slide, 0.78, 1.15, 4.0, 0.25, "CONTENTS", 10, "accent", colors=palette)
    chapters = list(plan["coverage"]["chapter_allocation"].keys())
    for idx, chapter in enumerate(chapters, start=1):
        col = 0 if idx <= 5 else 1
        row = idx - 1 if idx <= 5 else idx - 6
        x = 0.85 + col * 6.0
        y = 1.75 + row * 0.82
        add_textbox(slide, x, y, 0.42, 0.28, f"{idx:02d}", 12, "accent", True, colors=palette)
        add_textbox(slide, x + 0.55, y - 0.03, 4.95, 0.36, chapter, 14, "ink", True, colors=palette)
    add_textbox(
        slide,
        0.8,
        6.75,
        9.8,
        0.30,
        "汇报按报告章节展开，依次呈现勘察任务、基础工作、区域与矿区水文地质条件、勘探试验、分区评价、涌水量预测、模型校核及防治水建议。",
        10.5,
        "muted",
        colors=palette,
    )
    add_textbox(
        slide,
        11.65,
        6.82,
        0.7,
        0.2,
        f"{page['page']:02d}",
        9,
        "muted",
        align=PP_ALIGN.RIGHT,
        colors=palette,
    )


def create_engineering_design_spec(
    plan: dict[str, Any],
    media_dir: Path,
    template_profile: dict[str, Any],
    project_title: str,
    audience: str,
    use_case: str,
    design_style: str,
    image_names: list[str] | None = None,
) -> str:
    allocation = plan["coverage"]["chapter_allocation"]
    lines = [
        f"# {plan.get('project', 'Engineering Project')} - Design Spec",
        "",
        "## I. Project Information",
        "",
        "| Item | Value |",
        "| ---- | ----- |",
        f"| **Project Name** | {project_title} |",
        "| **Canvas Format** | PPT 16:9 (1280x720) |",
        f"| **Page Count** | {len(plan.get('slides', []))} |",
        f"| **Design Style** | {design_style} |",
        f"| **Target Audience** | {audience} |",
        f"| **Use Case** | {use_case} |",
        f"| **Created Date** | {datetime.now().strftime('%Y-%m-%d')} |",
        "",
        "## II. Canvas Specification",
        "",
        "| Property | Value |",
        "| -------- | ----- |",
        "| **Format** | PPT 16:9 |",
        "| **Dimensions** | 1280x720 |",
        "| **viewBox** | `0 0 1280 720` |",
        "| **Margins** | left/right 40-60px, top 30px, footer 24px |",
        "| **Content Area** | 1200x600px |",
        "",
        "## III. Visual Theme",
        "",
        "- **Style**: source-faithful Chinese engineering review presentation",
        "- **Theme**: light technical pages with deep-blue section rhythm",
        "- **Tone**: evidence-first, technical, restrained",
        "",
        "| Role | HEX | Purpose |",
        "| ---- | --- | ------- |",
        "| **Background** | `#F7F9FC` | Page background |",
        "| **Secondary bg** | `#F1F6FA` | Technical bands and table surfaces |",
        "| **Primary** | `#01203C` | Chapter headers and emphasis |",
        "| **Accent** | `#4489C8` | Section labels and engineering highlights |",
        "| **Warning** | `#A33A2B` | High-risk values and limitations |",
        "| **Body text** | `#01203C` | Main body text |",
        "| **Secondary text** | `#566B7F` | Captions, source notes |",
        "| **Border/divider** | `#CCD8E2` | Table and figure frames |",
        "",
        "## IV. Typography System",
        "",
        "**Typography direction**: CJK-primary professional sans with serif fallback for report quotations.",
        "",
        "| Role | Chinese | English | Fallback tail |",
        "| ---- | ------- | ------- | ------------- |",
        '| **Title** | `"Microsoft YaHei"` | `Arial` | `sans-serif` |',
        '| **Body** | `"Microsoft YaHei"` | `Arial` | `sans-serif` |',
        "| **Emphasis** | `SimSun` | `Georgia` | `serif` |",
        '| **Code** | — | `Consolas, "Courier New"` | `monospace` |',
        "",
        "**Baseline**: Body font size = 18px.",
        "",
        "## V. Layout Principles",
        "",
        "- Header area: title + chapter + page number.",
        "- Content area prioritizes original figure/table readability.",
        "- Footer area contains concise source note only.",
        "- Dense technical pages avoid decorative cards; tables and figures use framed source panels.",
        "- Visible copy uses report-facing language such as `报告阐述`, `报告对图件的说明`, `报告对表格的说明`, `报告计算口径`.",
        "- Internal planning metadata, evidence IDs, asset filenames and row/column diagnostics remain only in backend contracts/QA.",
        "",
        "## VI. Icon Usage Specification",
        "",
        "- Icons are sparse; source figures and tables carry most visual meaning.",
        "",
        "## VII. Visualization Reference List",
        "",
        "The deck uses report-native tables, maps, figures and formulas because source fidelity is more important than restyling source data.",
        "",
    ]
    if template_profile.get("available"):
        lines.extend(
            [
                "## VII-A. Template Learning Profile",
                "",
                f"- Template file: `{template_profile.get('path')}`",
                f"- Template slides: {template_profile.get('slide_count')}",
                f"- Canvas inches: {template_profile.get('canvas_inches')}",
                f"- Dominant fonts: {template_profile.get('dominant_fonts')}",
                f"- Dominant text colors: {template_profile.get('dominant_text_colors')}",
                f"- Picture distribution: {template_profile.get('picture_count_distribution')}",
                f"- Layout keys: {template_profile.get('layout_keys')}",
                f"- Adopted rules: {'; '.join(template_profile.get('adopted_rules', []))}",
                "",
            ]
        )
    lines.extend(
        [
            "## VIII. Image Resource List",
            "",
            "| Filename | Dimensions | Ratio | Purpose | Type | Layout pattern | Acquire Via | Status | Reference | text_policy | page_role |",
            "| -------- | ---------- | ----- | ------- | ---- | -------------- | ----------- | ------ | --------- | ----------- | --------- |",
        ]
    )
    names = image_names or []
    for name in names:
        path = media_dir / name
        if path.exists():
            with Image.open(path) as im:
                w, h = im.size
            lines.append(
                f"| {name} | {w}x{h} | {w / h:.2f} | Key report source figure | Source figure | source-faithful figure panel | user | Existing | Extracted from source | none | local |"
            )
    lines.extend(["", "## IX. Content Outline", ""])
    for chapter, count in allocation.items():
        lines.append(f"### {chapter} ({count} pages)")
        for page in plan["slides"]:
            if page["chapter"] == chapter:
                lines.append(f"#### Slide {page['page']:02d} - {page['title']}")
                lines.append(f"- **Layout**: {page['layout_pattern']}")
                lines.append(f"- **Core message**: {page['title']}")
                lines.append(f"- **Source mode**: {page['source_mode']}")
                lines.append(f"- **Evidence**: {', '.join(page['evidence_ids'])}")
                lines.append(f"- **Source note**: {page['source_note']}")
        lines.append("")
    lines.extend(
        [
            "## X. Speaker Notes Requirements",
            "",
            "- One notes file per slide under `notes/`.",
            "- Notes use formal engineering review language and cite source notes.",
            "",
            "## XI. Technical Constraints Reminder",
            "",
            "- Final PPTX must remain natively editable.",
            "- Keep body text readable; do not shrink source tables below readable floor.",
            "- Source conflicts and limitations remain visible when relevant.",
        ]
    )
    return "\n".join(lines) + "\n"


def create_engineering_spec_lock(
    plan: dict[str, Any],
    media_dir: Path,
    important_anchor_pages: set[int] | None = None,
) -> str:
    anchor_pages = important_anchor_pages or {1, 2, len(plan.get("slides", []))}
    lines = [
        "## canvas",
        "- viewBox: 0 0 1280 720",
        "- format: PPT 16:9",
        "",
        "## colors",
        "- bg: #F7F9FC",
        "- paper: #FFFFFF",
        "- primary: #01203C",
        "- accent: #4489C8",
        "- warning: #A33A2B",
        "- secondary_accent: #EAF2F8",
        "- text: #01203C",
        "- text_secondary: #566B7F",
        "- border: #CCD8E2",
        "",
        "## typography",
        '- font_family: "Microsoft YaHei", Arial, sans-serif',
        '- title_family: "Microsoft YaHei", Arial, sans-serif',
        '- body_family: "Microsoft YaHei", Arial, sans-serif',
        "- emphasis_family: Georgia, SimSun, serif",
        '- code_family: Consolas, "Courier New", monospace',
        "- body: 18",
        "- title: 32",
        "- subtitle: 24",
        "- annotation: 14",
        "- footer: 10",
        "",
        "## images",
    ]
    for img in sorted(media_dir.glob("image_*.*")):
        if img.suffix.lower() in {".png", ".jpg", ".jpeg"}:
            lines.append(f"- {img.stem}: {img.as_posix()} | no-crop")
    lines.extend(["", "## page_rhythm"])
    for page in plan["slides"]:
        if page["page"] in anchor_pages:
            rhythm = "anchor"
        elif page["density"] == "dense":
            rhythm = "dense"
        else:
            rhythm = "breathing" if page["type"] in {"conclusion", "chapter_summary"} else "dense"
        lines.append(f"- P{page['page']:02d}: {rhythm}")
    lines.extend(
        [
            "",
            "## forbidden",
            "- rgba()",
            "- `<style>`, `class`, `<foreignObject>`, `textPath`, `@font-face`, `<animate*>`, `<script>`, `<iframe>`",
            "- `<g opacity>`",
            "- HTML named entities in visible text",
            "- Visible internal metadata labels such as 来源模式, 证据编号, 本页用于, 原表定位, image_*.png, or E-* evidence IDs",
        ]
    )
    return "\n".join(lines) + "\n"
