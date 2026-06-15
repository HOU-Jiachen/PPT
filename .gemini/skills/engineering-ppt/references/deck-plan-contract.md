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

## Page Fulness

Fill unused space with the next most relevant source-backed object:

1. original figure or relevant crop
2. original/recreated table
3. formula or calculation sequence
4. exact project parameters
5. faithful explanatory text

Do not fill space with invented KPIs, decorative dashboards, unsupported comparisons, or
internal labels such as "报告原文摘录".
