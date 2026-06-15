# Release Gates

Run the following gates in order. A later success never cancels an earlier failure.

1. `project_contract.py`: required project directories and contracts exist.
2. `build_source_catalog.py`: source inventory and addressable source catalog exist.
3. Evidence review: all used evidence has `verification_status: verified`.
4. Deck-plan audit: every content page has chapter, source mode, evidence IDs, and proof object.
5. `svg_quality_checker.py`: zero errors.
6. Chart verification: required for every data-driven chart.
7. Full render: inspect every page at full size and as a contact sheet.
8. `release_audit.py --strict`: zero errors.
9. PPTX export: native DrawingML, with no empty media.
10. `release_audit.py --strict --pptx <file>`: package, XML, slide count, aspect ratio,
   forbidden wording, and parser checks pass.

## Blocking Defects

- visible internal workflow labels or caveats
- unsupported or newly calculated values not declared as verified calculations
- source conflicts hidden from the audience
- major chapter represented only by Agent conclusions
- text outside a container or canvas
- text reduced below the readability floor to preserve decoration
- key source table, map, or figure too small to inspect
- sparse page containing neither adequate explanation nor substantive source evidence
- corrupt PPTX, slide-count mismatch, empty media, or invalid XML

`qa/release_audit.json` and `qa/release_audit.md` are required release records.
