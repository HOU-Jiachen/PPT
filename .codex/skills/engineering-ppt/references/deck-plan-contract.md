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
- Allocate pages from evidence volume and readability, never from a fixed quota.
- Give every substantive slide one or more evidence IDs.
- Give each chapter at least one original text, table, figure, or calculation slide.
- Present original evidence before interpretation or conclusion when review accuracy matters.
- Preserve significant original wording for legal, regulatory, technical, and conclusion text.
- Split dense tables, maps, formulas, and long quotations instead of shrinking them.
- Do not use conclusion cards as a substitute for a chapter's technical process.
- Use three to five stable layout families. Do not add decorative components merely to fill space.
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
