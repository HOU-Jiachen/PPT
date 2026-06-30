# Deck Plan Contract

Create `deck_plan.json` after the evidence ledger and before `design_spec.md`.

Each slide must declare:

```json
{
  "page": 12,
  "type": "table",
  "chapter": "第3章 水资源开发利用状况",
  "title": "2015—2024年水资源量年际波动明显",
  "source_mode": "ORIGINAL_TABLE",
  "evidence_ids": ["E-3.2-T01"],
  "content_unit_ids": ["UNIT-0042"],
  "visual_proof": "Recreated source table split across two readable pages",
  "layout_pattern": "left_text_right_table",
  "source_note": "报告表3.2-1",
  "density": "dense",
  "density_exempt_reason": ""
}
```

Allowed `source_mode` values:

```text
ORIGINAL_TEXT | ORIGINAL_TABLE | ORIGINAL_FIGURE | CALCULATION |
INTERPRETATION | CONCLUSION | MANAGEMENT_ACTION
```

## Planning Rules

- Preserve the report's top-level chapter order for full-report briefings.
- Insert a structural divider page before each substantive report chapter, carrying the
  chapter sequence number and the report chapter name.
- Allocate pages from evidence volume and readability, never from a fixed quota.
- Give every substantive slide one or more evidence IDs.
- Derive every substantive slide from `analysis/report_content_inventory.json` or
  `analysis/ppt_content_blueprint.md`; keep `content_unit_ids` in the backend plan
  whenever possible.
- Give each chapter at least one original text, table, figure, or calculation slide.
- Present original evidence before interpretation or conclusion when review accuracy matters.
- Preserve significant original wording for legal, regulatory, technical, and conclusion text.
- Split dense tables, maps, formulas, and long quotations instead of shrinking them.
- Do not use conclusion cards as a substitute for a chapter's technical process.
- Use three to five stable layout families. Do not add decorative components merely to fill space.
- Add richer overview, chapter-synthesis, conclusion, or management-action pages only when
  they improve the report story. Across the whole deck, these high-level synthesis pages are
  capped at three unless the user explicitly changes the cap.
- At least 55% of substantive slides should be `ORIGINAL_TEXT`, `ORIGINAL_TABLE`,
  `ORIGINAL_FIGURE`, or `CALCULATION`; use interpretation slides to connect evidence,
  not to replace it.
- Do not place more than two interpretation / conclusion / management-action slides in
  a row unless a chapter has no extractable source figure, table, or calculation and the
  exemption is recorded.
- For original figures and tables, prefer mixed evidence layouts over standalone summary
  cards. Declare one of:

```text
left_text_right_figure | left_figure_right_text |
top_text_bottom_figure | top_figure_bottom_text |
left_text_right_table | left_table_right_text |
top_text_bottom_table | top_table_bottom_text
```

- Use a full-bleed or figure-only page only when the original map, drawing, chart, or
  table must be inspected at large scale; follow it with an explanatory text page if needed.
- `visual_proof` must identify the actual preserved object, not only say `table` or
  `figure`; for example, `original figure + right-side source explanation`.
- Visible small titles should prefer report headings, table captions, or figure captions
  from the content inventory. Do not invent generic labels for source panels.
- Never use backend-analysis phrases such as `原始对象`, `必讲内容`, `保留理由`, `证据`,
  source-mode names, evidence IDs, or asset filenames as visible titles or body text.
- Never place visible ellipses (`...`, `…`, `……`) in titles, captions, bullets, table
  summaries, or source explanations. Shorten to a complete sentence/phrase or split the slide.
- When one source paragraph is divided into multiple visible paragraphs, each visible item
  must have a number and a short report-derived name. A plain stack of anonymous paragraphs
  is a planning defect.
- Mark key terms, control values, units, conclusion clauses, and risk/action words for
  visible emphasis. Use emphasis sparingly but consistently so the presenter can locate the
  engineering point quickly.
- Native PPTX tables must be matched back to source table structure. Small/medium DOCX
  tables with merged headers or vertical merges should use real PPTX merged cells, while
  dense tables must record the split/excerpt reason.
- Choose figure layout from source aspect ratio: paired horizontal figures, maps, profiles,
  and wide charts should normally use `top_figure_bottom_text` or `top_text_bottom_figure`
  instead of narrow side-by-side figure panels.
- Consecutive pages may share a chapter theme, but their body text must not be near-identical;
  different figures/tables need object-specific explanation.

## Page Fulness

Fill unused space with the next most relevant source-backed object:

1. original figure or relevant crop
2. original/recreated table
3. formula or calculation sequence
4. exact project parameters
5. faithful explanatory text

Default fill pattern for engineering review pages is evidence pairing: put original
text/table/figure next to the explanation using the declared `layout_pattern`. A page
that contains only generated summary statements is not considered full unless it is a
chapter opener, agenda, or final decision page.

Do not fill space with invented KPIs, decorative dashboards, unsupported comparisons, or
internal labels such as "报告原文摘录".
