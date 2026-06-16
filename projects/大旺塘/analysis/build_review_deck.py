from __future__ import annotations

import json
import re
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
EXPORTS_DIR = PROJECT_DIR / "exports"


COLORS = {
    "bg": "F7F9F9",
    "paper": "FFFFFF",
    "ink": "1B2A2F",
    "muted": "5E6B70",
    "primary": "0E5E6F",
    "secondary": "DCE8E8",
    "accent": "B65A24",
    "line": "C7D3D4",
    "soft": "EEF3F3",
    "good": "2E7D32",
    "warn": "B65A24",
}


def rgb(hex_color: str) -> RGBColor:
    h = hex_color.strip("#")
    return RGBColor(int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16))


def pt(value: float):
    return Pt(value)


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def text_preview(text: str, max_len: int = 480) -> str:
    text = re.sub(r"\s+", " ", text or "").strip()
    return text if len(text) <= max_len else text[: max_len - 1] + "…"


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
    add_textbox(slide, 0.42, 0.20, 11.85, 0.45, page["title"], 22, "ink", True)
    add_textbox(slide, 0.43, 0.64, 7.0, 0.20, page["chapter"], 8.5, "muted")
    add_textbox(slide, 11.65, 0.62, 0.7, 0.18, f"{page['page']:02d}", 8.5, "muted", align=PP_ALIGN.RIGHT)
    line = slide.shapes.add_shape(1, Inches(0.42), Inches(0.88), Inches(11.84), Inches(0.015))
    line.fill.solid()
    line.fill.fore_color.rgb = rgb(COLORS["line"])
    line.line.fill.background()


def add_footer(slide, source_note: str):
    add_textbox(slide, 0.45, 6.95, 11.5, 0.22, f"来源：{source_note}", 8, "muted")


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
                p.font.size = pt(8.5 if len(clean) > 7 or col_count > 4 else 10)
                p.font.color.rgb = rgb(COLORS["ink"])
                if i == 0:
                    p.font.bold = True
            cell.fill.solid()
            cell.fill.fore_color.rgb = rgb(COLORS["secondary"] if i == 0 else "FFFFFF")
    if len(rows) > max_rows:
        add_textbox(slide, x, y + h + 0.05, w, 0.2, f"表格共{len(rows)}行，PPT展示关键行；完整数据见报告原表。", 8, "muted")


def image_paths_from_text(text: str) -> list[Path]:
    names = re.findall(r"image_\d+\.(?:png|jpe?g|wmf)", text, flags=re.I)
    paths: list[Path] = []
    for name in names:
        p = MEDIA_DIR / name
        if p.exists() and p.suffix.lower() != ".wmf":
            paths.append(p)
    return paths


def add_image(slide, path: Path, x, y, w, h):
    try:
        with Image.open(path) as im:
            iw, ih = im.size
    except Exception:
        add_textbox(slide, x, y, w, h, f"图像无法预览：{path.name}", 14, "warn")
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
        add_textbox(slide, x + 0.25, y + 0.25, w - 0.5, h - 0.5, "本页依据报告原文、原表或图件生成；未定位到可直接嵌入的单独图片。", 14, "muted")
        return
    n = min(len(paths), 4)
    if n == 1:
        add_fill(slide, x, y, w, h, "paper")
        add_image(slide, paths[0], x + 0.08, y + 0.08, w - 0.16, h - 0.16)
        add_textbox(slide, x + 0.15, y + h - 0.25, w - 0.3, 0.18, paths[0].name, 7.5, "muted")
        return
    cols = 2
    rows = 1 if n <= 2 else 2
    gap = 0.12
    cell_w = (w - gap * (cols - 1)) / cols
    cell_h = (h - gap * (rows - 1)) / rows
    for idx, path in enumerate(paths[:n]):
        cx = x + (idx % cols) * (cell_w + gap)
        cy = y + (idx // cols) * (cell_h + gap)
        add_fill(slide, cx, cy, cell_w, cell_h, "paper")
        add_image(slide, path, cx + 0.05, cy + 0.05, cell_w - 0.1, cell_h - 0.22)
        add_textbox(slide, cx + 0.08, cy + cell_h - 0.17, cell_w - 0.16, 0.12, path.name, 6.5, "muted")


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


def create_design_spec(plan: dict[str, Any]) -> str:
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
        "| **Design Style** | General Consulting + 政府/工程咨询评审详版 |",
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
        "| **Background** | `#F7F9F9` | Page background |",
        "| **Secondary bg** | `#EEF3F3` | Technical bands and table surfaces |",
        "| **Primary** | `#0E5E6F` | Chapter headers and emphasis |",
        "| **Accent** | `#B65A24` | Key engineering warnings and control values |",
        "| **Body text** | `#1B2A2F` | Main body text |",
        "| **Secondary text** | `#5E6B70` | Captions, source notes |",
        "| **Border/divider** | `#C7D3D4` | Table and figure frames |",
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
        "## VIII. Image Resource List",
        "",
        "| Filename | Dimensions | Ratio | Purpose | Type | Layout pattern | Acquire Via | Status | Reference | text_policy | page_role |",
        "| -------- | ---------- | ----- | ------- | ---- | -------------- | ----------- | ------ | --------- | ----------- | --------- |",
    ]
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
        "- bg: #F7F9F9",
        "- paper: #FFFFFF",
        "- primary: #0E5E6F",
        "- accent: #B65A24",
        "- secondary_accent: #DCE8E8",
        "- text: #1B2A2F",
        "- text_secondary: #5E6B70",
        "- border: #C7D3D4",
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


def build_deck():
    plan = load_json(PLAN_PATH)
    ledger = load_json(LEDGER_PATH)
    catalog = load_json(CATALOG_PATH)
    catalog_entries = {entry["id"]: entry for entry in catalog["entries"]}
    ev_by_id = evidence_lookup(ledger)

    (PROJECT_DIR / "design_spec.md").write_text(create_design_spec(plan), encoding="utf-8")
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
            add_textbox(slide, 0.8, 1.5, 11.5, 1.0, "大旺塘矿山地下水治理专项", 28, "paper", True)
            add_textbox(slide, 0.8, 2.35, 11.4, 0.8, "水文地质勘察工程评审汇报", 24, "paper", True)
            add_textbox(slide, 0.85, 4.0, 10.8, 0.6, "华润水泥（封开）有限公司 | 专项勘察 | 工程编号 K062601", 14, "paper")
            add_textbox(slide, 0.85, 6.7, 4.0, 0.3, datetime.now().strftime("%Y年%m月"), 11, "paper")
            continue

        add_title(slide, page)
        evidence = slide_evidence(page, ev_by_id)
        body_text = paragraph_from_evidence(evidence)
        source_note = page.get("source_note", "")
        image_paths = image_paths_from_text(page.get("visual_proof", "") + " " + source_note)
        table_entry = table_from_catalog(catalog_entries, evidence)

        if page["source_mode"] in {"ORIGINAL_FIGURE"} or image_paths:
            add_image_panel(slide, image_paths, 0.55, 1.10, 7.5, 5.55)
            add_textbox(slide, 8.35, 1.18, 4.25, 0.32, "证据解读", 15, "primary", True)
            add_textbox(slide, 8.35, 1.58, 4.15, 2.2, text_preview(body_text or page["visual_proof"], 420), 12.5, "ink")
            add_bullets(slide, 8.35, 4.0, 4.15, 1.9, [
                f"来源模式：{page['source_mode']}",
                f"证据编号：{', '.join(page['evidence_ids'][:3])}",
                "保留原图比例，避免裁切关键标注。"
            ], 10.5)
        elif page["source_mode"] in {"ORIGINAL_TABLE"} and table_entry:
            add_table(slide, table_entry, 0.55, 1.18, 8.4, 4.8, max_rows=9, max_cols=5)
            add_textbox(slide, 9.25, 1.25, 3.2, 0.32, "表格说明", 15, "primary", True)
            add_textbox(slide, 9.25, 1.65, 3.1, 2.35, text_preview(body_text or table_entry.get("text", ""), 380), 12, "ink")
            add_bullets(slide, 9.25, 4.2, 3.1, 1.8, [
                f"原表定位：{source_note}",
                f"行列规模：{table_entry.get('row_count', '?')}行 × {table_entry.get('column_count', '?')}列",
                "密集表按重点行重排，完整数据回看报告原表。"
            ], 10)
        elif page["source_mode"] == "CALCULATION":
            add_fill(slide, 0.55, 1.18, 5.5, 4.95, "paper")
            formula = "; ".join([ev.get("formula", "") for ev in evidence if ev.get("formula")])
            inputs = []
            for ev in evidence:
                inputs.extend(ev.get("inputs", []) or [])
            add_textbox(slide, 0.85, 1.45, 4.9, 0.3, "计算链", 16, "primary", True)
            add_textbox(slide, 0.85, 1.9, 4.9, 1.1, text_preview(formula or "按报告公式、参数表和结果表保留计算链。", 240), 12.5, "ink")
            add_bullets(slide, 0.85, 3.25, 4.9, 2.2, [text_preview(i, 120) for i in inputs[:5]] or ["参数来自报告原表。"], 10.5)
            if table_entry:
                add_table(slide, table_entry, 6.35, 1.18, 5.9, 4.95, max_rows=8, max_cols=4)
            else:
                add_textbox(slide, 6.45, 1.3, 5.5, 3.5, text_preview(body_text, 620), 13, "ink")
        else:
            add_fill(slide, 0.65, 1.25, 12.0, 4.9, "paper")
            add_textbox(slide, 0.95, 1.55, 11.35, 2.3, text_preview(body_text or page["visual_proof"], 760), 15, "ink")
            add_bullets(slide, 0.95, 4.15, 11.1, 1.35, [
                f"来源模式：{page['source_mode']}",
                f"证据编号：{', '.join(page['evidence_ids'])}",
                f"本页用于：{page['visual_proof']}"
            ], 12)

        add_footer(slide, source_note)

    EXPORTS_DIR.mkdir(exist_ok=True)
    out = EXPORTS_DIR / f"大旺塘工程评审汇报_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pptx"
    prs.save(out)

    notes_dir = PROJECT_DIR / "notes"
    notes_dir.mkdir(exist_ok=True)
    total = []
    for page in plan["slides"]:
        note = f"# Slide {page['page']:02d} - {page['title']}\n\n讲解要点：围绕“{page['title']}”展开，引用来源：{page['source_note']}。证据编号：{', '.join(page['evidence_ids'])}。\n"
        (notes_dir / f"{page['page']:02d}.md").write_text(note.replace("# Slide", "Slide"), encoding="utf-8")
        total.append(note)
    (notes_dir / "total.md").write_text("\n\n".join(total), encoding="utf-8")

    print(out)


if __name__ == "__main__":
    build_deck()
