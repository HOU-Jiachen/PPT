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
from pptx.enum.text import MSO_AUTO_SIZE, PP_ALIGN
from pptx.util import Inches, Pt


PROJECT_DIR = Path(__file__).resolve().parents[1]
REPO_ROOT = PROJECT_DIR.parents[1]
CATALOG_PATH = PROJECT_DIR / "analysis" / "source_catalog.json"
PLAN_PATH = PROJECT_DIR / "deck_plan.json"
LEDGER_PATH = PROJECT_DIR / "evidence_ledger.json"
MEDIA_DIR = PROJECT_DIR / "sources" / "大旺塘水文地质勘察报告_files"
MARKDOWN_PATH = PROJECT_DIR / "sources" / "大旺塘水文地质勘察报告.md"
EXPORTS_DIR = PROJECT_DIR / "exports"
TEMPLATE_DIR = PROJECT_DIR / "template"


COLORS = {
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


def template_pptx() -> Path | None:
    candidates = sorted(TEMPLATE_DIR.glob("*.pptx"))
    return candidates[0] if candidates else None


def collect_template_profile() -> dict[str, Any]:
    path = template_pptx()
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
    slide_shapes: list[dict[str, Any]] = []

    def walk(shapes):
        for shape in shapes:
            yield shape
            if getattr(shape, "shape_type", None) == 6 and hasattr(shape, "shapes"):
                yield from walk(shape.shapes)

    for index, slide in enumerate(prs.slides, start=1):
        pictures = 0
        tables = 0
        texts = []
        for shape in walk(slide.shapes):
            if getattr(shape, "shape_type", None) == 13:
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
        if index <= 9:
            slide_shapes.append(
                {
                    "slide": index,
                    "pictures": pictures,
                    "tables": tables,
                    "sample_text": texts[:4],
                }
            )

    return {
        "available": True,
        "path": str(path.relative_to(PROJECT_DIR)),
        "slide_count": len(prs.slides),
        "canvas_inches": [round(prs.slide_width / 914400, 3), round(prs.slide_height / 914400, 3)],
        "dominant_fonts": fonts.most_common(8),
        "dominant_font_sizes": sizes.most_common(8),
        "dominant_text_colors": text_colors.most_common(8),
        "dominant_fill_colors": fill_colors.most_common(8),
        "layout_observations": slide_shapes,
        "adopted_rules": [
            "16:9 canvas, deep-blue technical review identity",
            "large chapter/section titles with restrained body text",
            "source figures shown without asset filenames or extraction IDs",
            "tables are simplified to readable key rows rather than dense dumps",
        ],
    }


def text_preview(text: str, max_len: int = 480) -> str:
    text = sanitize_visible_text(text)
    return text if len(text) <= max_len else text[: max_len - 1] + "…"


def sanitize_visible_text(text: str) -> str:
    text = re.sub(r"\s+", " ", text or "").strip()
    text = re.sub(r"\s*\|\s*", "；", text)
    for pattern in INTERNAL_VISIBLE_PATTERNS:
        text = re.sub(pattern, "", text, flags=re.I)
    text = text.replace("证据解读", "报告说明")
    return re.sub(r"\s+", " ", text).strip(" ，,;；")


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
        for cid in ev.get("catalog_ids", []):
            entry = catalog_entries.get(cid)
            if not entry:
                continue
            if entry.get("kind") == "paragraph":
                add(entry.get("text"))
    for ev in evidence:
        add(ev.get("summary"))

    return text_preview(" ".join(parts), max_len)


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


def add_textbox(slide, x, y, w, h, text, size=18, color="ink", bold=False, align=None, font="Microsoft YaHei"):
    box = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = box.text_frame
    tf.clear()
    tf.word_wrap = True
    tf.auto_size = MSO_AUTO_SIZE.NONE
    p = tf.paragraphs[0]
    p.text = text
    p.font.name = font
    p.font.size = pt(size)
    p.font.bold = bold
    p.font.color.rgb = rgb(COLORS[color])
    if align:
        p.alignment = align
    return box


def add_fill(slide, x, y, w, h, color="paper", line="line"):
    shape = slide.shapes.add_shape(1, Inches(x), Inches(y), Inches(w), Inches(h))
    shape.fill.solid()
    shape.fill.fore_color.rgb = rgb(COLORS[color])
    shape.line.color.rgb = rgb(COLORS[line])
    shape.line.width = Pt(0.6)
    return shape


def add_title(slide, page: dict[str, Any]):
    add_textbox(slide, 0.42, 0.20, 11.85, 0.50, page["title"], 24, "ink", True)
    add_textbox(slide, 0.43, 0.68, 7.0, 0.24, page["chapter"], 9.5, "accent")
    add_textbox(slide, 11.65, 0.66, 0.7, 0.20, f"{page['page']:02d}", 9, "muted", align=PP_ALIGN.RIGHT)
    line = slide.shapes.add_shape(1, Inches(0.42), Inches(0.88), Inches(11.84), Inches(0.015))
    line.fill.solid()
    line.fill.fore_color.rgb = rgb(COLORS["accent"])
    line.line.fill.background()


def add_footer(slide, source_note: str):
    if source_note:
        add_textbox(slide, 0.45, 6.95, 11.5, 0.22, f"资料来源：{source_note}", 8.5, "muted")


def table_from_catalog(catalog_entries: dict[str, dict[str, Any]], evidence: list[dict[str, Any]]):
    for ev in evidence:
        for cid in ev.get("catalog_ids", []):
            entry = catalog_entries.get(cid)
            if entry and entry.get("kind") == "table" and entry.get("rows"):
                return entry
    return None


def paragraph_from_evidence(evidence: list[dict[str, Any]]) -> str:
    parts = []
    for ev in evidence:
        if ev.get("exact_text"):
            parts.append(ev["exact_text"])
        elif ev.get("summary"):
            parts.append(ev["summary"])
    return "\n".join(parts[:3])


def add_table(slide, entry: dict[str, Any], x, y, w, h, max_rows=8, max_cols=5):
    rows = entry.get("rows") or []
    if not rows:
        add_textbox(slide, x, y, w, h, text_preview(entry.get("text", ""), 720), 13, "ink")
        return
    clean = [[text_preview(str(cell), 70) for cell in row[:max_cols]] for row in rows[:max_rows]]
    col_count = max(len(row) for row in clean) if clean else 1
    for row in clean:
        while len(row) < col_count:
            row.append("")
    shape = slide.shapes.add_table(len(clean), col_count, Inches(x), Inches(y), Inches(w), Inches(h))
    tbl = shape.table
    for i, row in enumerate(clean):
        for j, cell_text in enumerate(row):
            cell = tbl.cell(i, j)
            cell.text = cell_text
            for p in cell.text_frame.paragraphs:
                p.font.name = "Microsoft YaHei"
                p.font.size = pt(10.5 if len(clean) > 6 or col_count > 4 else 12)
                p.font.color.rgb = rgb(COLORS["ink"])
                if i == 0:
                    p.font.bold = True
            cell.fill.solid()
            cell.fill.fore_color.rgb = rgb(COLORS["secondary"] if i == 0 else "FFFFFF")
    return shape


def extract_figure_ids(text: str) -> list[str]:
    normalized = (text or "").replace("\\", "")
    return re.findall(r"图\s*\d+(?:\.\d+)?-\d+", normalized)


def figure_image_index() -> dict[str, list[str]]:
    if not MARKDOWN_PATH.exists():
        return {}
    lines = MARKDOWN_PATH.read_text(encoding="utf-8").splitlines()
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


def image_paths_from_text(text: str, figure_index: dict[str, list[str]] | None = None) -> list[Path]:
    names = re.findall(r"image_\d+\.(?:png|jpe?g|wmf)", text, flags=re.I)
    if figure_index:
        for figure_id in extract_figure_ids(text):
            names.extend(figure_index.get(figure_id, []))
    paths: list[Path] = []
    seen: set[Path] = set()
    for name in names:
        p = MEDIA_DIR / name
        if p.exists() and p.suffix.lower() != ".wmf" and p not in seen:
            seen.add(p)
            paths.append(p)
    return paths


def add_image(slide, path: Path, x, y, w, h):
    try:
        with Image.open(path) as im:
            iw, ih = im.size
    except Exception:
        add_textbox(slide, x, y, w, h, "报告图件暂无法嵌入", 14, "warn")
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
    slide.shapes.add_picture(str(path), Inches(final_x), Inches(final_y), width=Inches(final_w), height=Inches(final_h))


def add_image_panel(slide, paths: list[Path], x, y, w, h):
    if not paths:
        add_fill(slide, x, y, w, h, "soft")
        add_textbox(slide, x + 0.25, y + 0.25, w - 0.5, h - 0.5, "报告相关图件", 18, "muted", True, align=PP_ALIGN.CENTER)
        return
    n = min(len(paths), 4)
    if n == 1:
        add_fill(slide, x, y, w, h, "paper")
        add_image(slide, paths[0], x + 0.08, y + 0.08, w - 0.16, h - 0.16)
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
        add_fill(slide, cx, cy, cell_w, cell_h, "paper")
        add_image(slide, path, cx + 0.05, cy + 0.05, cell_w - 0.1, cell_h - 0.1)


def add_bullets(slide, x, y, w, h, items: list[str], size=13):
    box = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = box.text_frame
    tf.clear()
    tf.word_wrap = True
    tf.auto_size = MSO_AUTO_SIZE.NONE
    for idx, item in enumerate(items):
        p = tf.paragraphs[0] if idx == 0 else tf.add_paragraph()
        p.text = item
        p.level = 0
        p.font.name = "Microsoft YaHei"
        p.font.size = pt(size)
        p.font.color.rgb = rgb(COLORS["ink"])
        p.space_after = pt(4)
    return box


def evidence_lookup(ledger: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {item["id"]: item for item in ledger["evidence"]}


def slide_evidence(page: dict[str, Any], ev_by_id: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    return [ev_by_id[eid] for eid in page.get("evidence_ids", []) if eid in ev_by_id]


def create_design_spec(plan: dict[str, Any], template_profile: dict[str, Any]) -> str:
    allocation = plan["coverage"]["chapter_allocation"]
    lines = [
        "# 大旺塘 - Design Spec",
        "",
        "## I. Project Information",
        "",
        "| Item | Value |",
        "| ---- | ----- |",
        "| **Project Name** | 大旺塘矿山地下水治理专项水文地质勘察工程评审汇报 |",
        "| **Canvas Format** | PPT 16:9 (1280x720) |",
        "| **Page Count** | 74 |",
        "| **Design Style** | 参考既有最终评审PPT的深蓝工程评审风格 |",
        "| **Target Audience** | 业主单位、矿山安全与水文地质评审专家、设计及治理实施相关方 |",
        "| **Use Case** | 专项勘察工程评审汇报 |",
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
        "- **Style**: General Consulting + restrained government engineering review",
        "- **Theme**: Light theme",
        "- **Tone**: evidence-first, source-faithful, technical, restrained",
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
        "**Typography direction**: CJK-primary professional sans with serif emphasis for report quotations.",
        "",
        "| Role | Chinese | English | Fallback tail |",
        "| ---- | ------- | ------- | ------------- |",
        '| **Title** | `"Microsoft YaHei"` | `Arial` | `sans-serif` |',
        '| **Body** | `"Microsoft YaHei"` | `Arial` | `sans-serif` |',
        "| **Emphasis** | `SimSun` | `Georgia` | `serif` |",
        '| **Code** | — | `Consolas, "Courier New"` | `monospace` |',
        "",
        '- Title: `"Microsoft YaHei", Arial, sans-serif`',
        '- Body: `"Microsoft YaHei", Arial, sans-serif`',
        "- Emphasis: `Georgia, SimSun, serif`",
        '- Code: `Consolas, "Courier New", monospace`',
        "",
        "**Baseline**: Body font size = 18px.",
        "",
        "## V. Layout Principles",
        "",
        "- Header area: 90px, title + chapter + page number.",
        "- Content area: 560px, prioritizing original figure/table readability.",
        "- Footer area: 30px, concise source note.",
        "- Layouts: left_text_right_figure, top_figure_bottom_text, left_table_right_text, top_text_bottom_table, evidence_chain, decision_matrix.",
        "- Dense technical pages avoid decorative cards; tables and figures use framed source panels.",
        "- Visible copy uses report-facing language: `报告阐述`, `报告对图件的说明`, `报告对表格的说明`, `报告计算口径`.",
        "- Internal planning metadata, evidence IDs, asset filenames and row/column diagnostics remain only in backend contracts/QA.",
        "",
        "## VI. Icon Usage Specification",
        "",
        "- Built-in icon library: `tabler-outline`",
        "- Usage is sparse; icons only support agenda, chain and decision pages.",
        "",
        "| Purpose | Icon Path | Page |",
        "| ------- | --------- | ---- |",
        "| Objective | `tabler-outline/target` | P02 |",
        "| Evidence | `tabler-outline/chart-bar` | P12 |",
        "| Safety | `tabler-outline/shield` | P72 |",
        "",
        "## VII. Visualization Reference List",
        "",
        "Catalog read: no chart templates used. The deck uses report-native tables, maps, figures and formulas because source fidelity is more important than restyling source data.",
        "",
        "Runners-up considered:",
        "- `bar_chart` | rejected: most numeric pages require precise source tables rather than simplified bars.",
        "- `process_flow` | rejected:防治水措施使用报告原文和证据链矩阵，不替代为流程模板。",
        "- `timeline_horizontal` | rejected:工作经过页保留报告原文时间节点即可。",
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
                f"- Adopted rules: {'; '.join(template_profile.get('adopted_rules', []))}",
                "",
            ]
        )
    lines.extend([
        "## VIII. Image Resource List",
        "",
        "| Filename | Dimensions | Ratio | Purpose | Type | Layout pattern | Acquire Via | Status | Reference | text_policy | page_role |",
        "| -------- | ---------- | ----- | ------- | ---- | -------------- | ----------- | ------ | --------- | ----------- | --------- |",
    ])
    for name in ["image_003.jpeg", "image_034.png", "image_060.png", "image_143.jpeg", "image_194.jpeg", "image_195.jpeg", "image_207.png", "image_216.png"]:
        path = MEDIA_DIR / name
        if path.exists():
            with Image.open(path) as im:
                w, h = im.size
            lines.append(f"| {name} | {w}x{h} | {w/h:.2f} | Key report source figure | Source figure | source-faithful figure panel | user | Existing | Extracted from DOCX | none | local |")
    lines.extend([
        "",
        "## IX. Content Outline",
        "",
    ])
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
    lines.extend([
        "## X. Speaker Notes Requirements",
        "",
        "- One notes file per slide under `notes/`.",
        "- Notes use formal engineering review language and cite source notes.",
        "- Target duration: 55-70 minutes for 74 slides.",
        "",
        "## XI. Technical Constraints Reminder",
        "",
        "- Final PPTX must remain natively editable.",
        "- Keep body text readable; do not shrink source tables below readable floor.",
        "- Source conflicts and limitations remain visible when relevant.",
    ])
    return "\n".join(lines) + "\n"


def create_spec_lock(plan: dict[str, Any]) -> str:
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
        "## icons",
        "- library: tabler-outline",
        "- stroke_width: 2",
        "- inventory: target, chart-bar, shield, map, droplet, table, alert-triangle",
        "",
        "## images",
    ]
    for img in sorted(MEDIA_DIR.glob("image_*.*")):
        if img.suffix.lower() in {".png", ".jpg", ".jpeg"}:
            lines.append(f"- {img.stem}: sources/大旺塘水文地质勘察报告_files/{img.name} | no-crop")
    lines.extend(["", "## page_rhythm"])
    for page in plan["slides"]:
        if page["page"] in {1, 2, 7, 13, 19, 31, 41, 53, 63, 69, 74}:
            rhythm = "anchor"
        elif page["density"] == "dense":
            rhythm = "dense"
        else:
            rhythm = "breathing" if page["type"] in {"conclusion", "chapter_summary"} else "dense"
        lines.append(f"- P{page['page']:02d}: {rhythm}")
    lines.extend([
        "",
        "## forbidden",
        "- rgba()",
        "- `<style>`, `class`, `<foreignObject>`, `textPath`, `@font-face`, `<animate*>`, `<script>`, `<iframe>`",
        "- `<g opacity>`",
        "- HTML named entities in visible text",
    ])
    return "\n".join(lines) + "\n"


def add_agenda_slide(slide, plan: dict[str, Any], page: dict[str, Any]) -> None:
    add_fill(slide, 0, 0, 13.333, 7.5, "paper", "paper")
    add_textbox(slide, 0.75, 0.62, 5.8, 0.62, "目录", 30, "primary", True)
    add_textbox(slide, 0.78, 1.15, 4.0, 0.25, "CONTENTS", 10, "accent")
    chapters = list(plan["coverage"]["chapter_allocation"].keys())
    for idx, chapter in enumerate(chapters, start=1):
        col = 0 if idx <= 5 else 1
        row = idx - 1 if idx <= 5 else idx - 6
        x = 0.85 + col * 6.0
        y = 1.75 + row * 0.82
        add_textbox(slide, x, y, 0.42, 0.28, f"{idx:02d}", 12, "accent", True)
        add_textbox(slide, x + 0.55, y - 0.03, 4.95, 0.36, chapter, 14, "ink", True)
    add_textbox(
        slide,
        0.8,
        6.75,
        9.8,
        0.30,
        "汇报按报告章节展开，依次呈现勘察任务、基础工作、区域与矿区水文地质条件、勘探试验、分区评价、涌水量预测、模型校核及防治水建议。",
        10.5,
        "muted",
    )
    add_textbox(slide, 11.65, 6.82, 0.7, 0.2, f"{page['page']:02d}", 9, "muted", align=PP_ALIGN.RIGHT)


def build_deck():
    plan = load_json(PLAN_PATH)
    ledger = load_json(LEDGER_PATH)
    catalog = load_json(CATALOG_PATH)
    catalog_entries = {entry["id"]: entry for entry in catalog["entries"]}
    ev_by_id = evidence_lookup(ledger)
    template_profile = collect_template_profile()
    fig_index = figure_image_index()
    (PROJECT_DIR / "analysis" / "template_profile.json").write_text(
        json.dumps(template_profile, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    (PROJECT_DIR / "analysis" / "figure_image_index.json").write_text(
        json.dumps(fig_index, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    (PROJECT_DIR / "design_spec.md").write_text(create_design_spec(plan, template_profile), encoding="utf-8")
    (PROJECT_DIR / "spec_lock.md").write_text(create_spec_lock(plan), encoding="utf-8")

    prs = Presentation()
    prs.slide_width = Inches(13.333333)
    prs.slide_height = Inches(7.5)
    blank = prs.slide_layouts[6]

    for page in plan["slides"]:
        slide = prs.slides.add_slide(blank)
        bg = slide.background.fill
        bg.solid()
        bg.fore_color.rgb = rgb(COLORS["bg"])

        if page["page"] == 1:
            add_fill(slide, 0, 0, 13.333, 7.5, "primary", "primary")
            add_textbox(slide, 0.8, 1.45, 11.5, 1.0, "大旺塘矿山地下水治理专项", 34, "paper", True)
            add_textbox(slide, 0.8, 2.38, 11.4, 0.8, "水文地质勘察工程评审汇报", 28, "paper", True)
            add_textbox(slide, 0.85, 4.0, 10.8, 0.6, "华润水泥（封开）有限公司 | 专项勘察 | 工程编号 K062601", 15, "paper")
            add_textbox(slide, 0.85, 6.7, 4.0, 0.3, datetime.now().strftime("%Y年%m月"), 11, "paper")
            continue

        if page["type"] == "agenda":
            add_agenda_slide(slide, plan, page)
            continue

        add_title(slide, page)
        evidence = slide_evidence(page, ev_by_id)
        body_text = report_text_from_evidence(evidence, catalog_entries)
        source_note = page.get("source_note", "")
        image_paths = image_paths_from_text(page.get("visual_proof", "") + " " + source_note, fig_index)
        table_entry = table_from_catalog(catalog_entries, evidence)

        if page["source_mode"] in {"ORIGINAL_FIGURE"} or image_paths:
            add_image_panel(slide, image_paths, 0.55, 1.10, 7.5, 5.55)
            add_textbox(slide, 8.35, 1.18, 4.25, 0.32, report_heading(page["source_mode"]), 15, "accent", True)
            add_textbox(slide, 8.35, 1.58, 4.15, 3.75, text_preview(body_text or page["title"], 620), 13.5, "ink")
        elif page["source_mode"] in {"ORIGINAL_TABLE"} and table_entry:
            add_table(slide, table_entry, 0.55, 1.18, 8.35, 4.95, max_rows=7, max_cols=4)
            add_textbox(slide, 9.25, 1.25, 3.2, 0.32, report_heading(page["source_mode"]), 15, "accent", True)
            add_textbox(slide, 9.25, 1.65, 3.1, 3.45, text_preview(body_text or table_entry.get("text", ""), 520), 12.8, "ink")
        elif page["source_mode"] == "CALCULATION":
            add_fill(slide, 0.55, 1.18, 5.5, 4.95, "paper")
            formula = "; ".join([ev.get("formula", "") for ev in evidence if ev.get("formula")])
            inputs = []
            for ev in evidence:
                inputs.extend(ev.get("inputs", []) or [])
            add_textbox(slide, 0.85, 1.45, 4.9, 0.3, report_heading(page["source_mode"]), 16, "accent", True)
            add_textbox(slide, 0.85, 1.9, 4.9, 1.25, text_preview(formula or body_text or "报告按公式、参数表和结果表列示计算过程。", 280), 12.8, "ink")
            add_bullets(slide, 0.85, 3.35, 4.9, 2.0, [text_preview(i, 130) for i in inputs[:4]] or [text_preview(body_text, 130)], 10.8)
            if table_entry:
                add_table(slide, table_entry, 6.35, 1.18, 5.9, 4.95, max_rows=7, max_cols=4)
            else:
                add_textbox(slide, 6.45, 1.3, 5.5, 3.5, text_preview(body_text, 620), 13.5, "ink")
        else:
            add_fill(slide, 0.65, 1.25, 12.0, 4.9, "paper")
            add_textbox(slide, 0.95, 1.55, 11.35, 0.35, report_heading(page["source_mode"]), 16, "accent", True)
            points = report_points_from_evidence(evidence, catalog_entries, max_points=5)
            if len(points) >= 2:
                add_bullets(slide, 0.95, 2.08, 10.95, 3.30, points, 14.0)
            else:
                add_textbox(slide, 0.95, 2.08, 11.1, 3.15, text_preview(body_text or page["title"], 720), 15, "ink")

        add_footer(slide, source_note)

    EXPORTS_DIR.mkdir(exist_ok=True)
    out = EXPORTS_DIR / f"大旺塘工程评审汇报_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pptx"
    prs.save(out)

    notes_dir = PROJECT_DIR / "notes"
    notes_dir.mkdir(exist_ok=True)
    total = []
    for page in plan["slides"]:
        note = f"# Slide {page['page']:02d} - {page['title']}\n\n讲解要点：围绕“{page['title']}”展开，按报告对应章节、图表或计算口径说明；资料来源：{page['source_note']}。\n"
        (notes_dir / f"{page['page']:02d}.md").write_text(note.replace("# Slide", "Slide"), encoding="utf-8")
        total.append(note)
    (notes_dir / "total.md").write_text("\n\n".join(total), encoding="utf-8")

    print(out)


if __name__ == "__main__":
    build_deck()
