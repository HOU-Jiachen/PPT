# Evidence Contract

## Artifacts

Maintain two machine-readable files before slide authoring:

- `analysis/source_catalog.json`: deterministic extraction output. Its IDs address source
  paragraphs, tables, figures, pages, worksheets, and source slides.
- `evidence_ledger.json`: reviewed evidence selected for the presentation.

Each evidence record must contain:

```json
{
  "id": "E-4.2-T03",
  "kind": "FACT",
  "summary": "Annual requested withdrawal is 7.50 million m3.",
  "source_file": "report.docx",
  "source_locator": "Table 4.2-3",
  "catalog_ids": ["12ab34cd:T013"],
  "verification_status": "verified",
  "exact_text": "",
  "values": [{"value": 750, "unit": "万m3", "time_basis": "annual"}],
  "notes": ""
}
```

Allowed `kind` values:

```text
FACT | ORIGINAL_TEXT | ORIGINAL_TABLE | ORIGINAL_FIGURE |
CALCULATION | INTERPRETATION | RECOMMENDATION
```

## Rules

- Mark evidence `verified` only after checking the original DOCX/PDF/table/figure, not only
  OCR or flattened extraction.
- Store every visible quantitative value in `values`, including units and time basis.
- For a calculation, store the formula and all verified inputs. Never infer missing inputs.
- Keep conflicting source values as separate records. Do not merge or select one silently.
- Keep Agent reasoning as `INTERPRETATION`; do not relabel it as `FACT`.
- Keep internal workflow notes in the ledger, never in visible slide text.
- Use source files as the authority. Previous PPT decks and old outlines are leads, not facts.
