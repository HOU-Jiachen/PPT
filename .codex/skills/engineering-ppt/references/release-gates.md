# Release Gates

Run the following gates in order. A later success never cancels an earlier failure.

1. `project_contract.py`: required project directories and contracts exist.
2. `build_source_catalog.py`: source inventory and addressable source catalog exist.
3. `build_ppt_content_blueprint.py`: report-content inventory and PPT content blueprint exist.
4. Evidence review: all used evidence has `verification_status: verified`.
5. Deck-plan audit: every content page has chapter, source mode, evidence IDs, and proof object.
6. Content-richness audit: original text/table/figure/calculation slides meet the configured
   minimum ratio, and interpretation-only runs do not replace the report's technical process.
7. `svg_quality_checker.py`: zero errors.
8. Font audit: non-template PPT body text, table text, and chart labels are at least 14 pt.
9. Layout-collision audit after final font sizing and PPTX export: visible text stays
   inside the safe frame, text boxes do not overlap each other, and body text does not
   cover large source images, figures, or tables.
10. Chart verification: required for every data-driven chart.
11. Full render: inspect every page at full size and as a contact sheet.
12. `release_audit.py --strict`: zero errors.
13. PPTX export: native DrawingML, with no empty media.
14. `release_audit.py --strict --pptx <file>`: package, XML, slide count, aspect ratio,
   forbidden wording, and parser checks pass.
15. GitHub upload: commit and push this run's relevant artifacts, contracts, QA records,
    exports, and local agent-rule changes to `origin`.

## Blocking Defects

- visible internal workflow labels or caveats
- unsupported or newly calculated values not declared as verified calculations
- source conflicts hidden from the audience
- major chapter represented only by Agent conclusions
- text outside a container or canvas
- text outside the slide safe frame, text overlapping text, or text covering large images
  and figures
- text reduced below the readability floor to preserve decoration
- key source table, map, or figure too small to inspect
- sparse page containing neither adequate explanation nor substantive source evidence
- technical chapters reduced to summary cards without enough original text, tables, figures,
  formulas, or source-backed mixed layouts
- non-template body/table/chart text smaller than 14 pt
- corrupt PPTX, slide-count mismatch, empty media, or invalid XML
- completed local run that has not been uploaded to GitHub and has no explicit blocker report

`qa/release_audit.json` and `qa/release_audit.md` are required release records.
