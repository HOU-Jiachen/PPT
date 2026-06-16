# Release Gates

Run the following gates in order. A later success never cancels an earlier failure.

1. `project_contract.py`: required project directories and contracts exist.
2. `build_source_catalog.py`: source inventory and addressable source catalog exist.
3. Evidence review: all used evidence has `verification_status: verified`.
4. Deck-plan audit: every content page has chapter, source mode, evidence IDs, and proof object.
5. Content-richness audit: original text/table/figure/calculation slides meet the configured
   minimum ratio, and interpretation-only runs do not replace the report's technical process.
6. `svg_quality_checker.py`: zero errors.
7. Font audit: non-template PPT body text, table text, and chart labels are at least 14 pt.
8. Chart verification: required for every data-driven chart.
9. Full render: inspect every page at full size and as a contact sheet.
10. `release_audit.py --strict`: zero errors.
11. PPTX export: native DrawingML, with no empty media.
12. `release_audit.py --strict --pptx <file>`: package, XML, slide count, aspect ratio,
   forbidden wording, and parser checks pass.
13. GitHub upload: commit and push this run's relevant artifacts, contracts, QA records,
    exports, and local agent-rule changes to `origin`.

## Blocking Defects

- visible internal workflow labels or caveats
- unsupported or newly calculated values not declared as verified calculations
- source conflicts hidden from the audience
- major chapter represented only by Agent conclusions
- text outside a container or canvas
- text reduced below the readability floor to preserve decoration
- key source table, map, or figure too small to inspect
- sparse page containing neither adequate explanation nor substantive source evidence
- technical chapters reduced to summary cards without enough original text, tables, figures,
  formulas, or source-backed mixed layouts
- non-template body/table/chart text smaller than 14 pt
- corrupt PPTX, slide-count mismatch, empty media, or invalid XML
- completed local run that has not been uploaded to GitHub and has no explicit blocker report

`qa/release_audit.json` and `qa/release_audit.md` are required release records.
