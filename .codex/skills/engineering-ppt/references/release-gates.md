# Release Gates

Run the following gates in order. A later success never cancels an earlier failure.

1. `project_contract.py`: required project directories and contracts exist.
2. `build_source_catalog.py`: source inventory and addressable source catalog exist.
3. `build_ppt_content_blueprint.py`: report-content inventory and PPT content blueprint exist.
4. Evidence review: all used evidence has `verification_status: verified`.
5. Deck-plan audit: every content page has chapter, source mode, evidence IDs, and proof object.
6. Content-richness audit: original text/table/figure/calculation slides meet the configured
   minimum ratio, and interpretation-only runs do not replace the report's technical process.
   Summary / overview / conclusion / management-action pages must not exceed the configured
   maximum of three unless explicitly overridden.
7. `svg_quality_checker.py`: zero errors.
8. Font audit: non-template PPT body text, table text, and chart labels are at least 14 pt,
   with table text at least 12 pt when the project policy distinguishes table minimums.
9. Frontier layout metrics: source images preserve aspect ratio, occupied area is not
   excessively sparse or overcrowded, visual balance stays within policy thresholds, and
   severe element collisions are blocked.
10. Layout-collision and capacity audit after final font sizing and PPTX export: visible
    text stays inside the safe frame, text boxes do not overlap each other, body text does
    not cover large source images/figures/tables, and text boxes/table cells have enough
    line capacity for their content.
10a. Paragraph and emphasis audit after PPTX export: multi-paragraph text blocks must carry
    visible item numbers or short paragraph names, and content slides with key values/terms
    must contain visible bold/color/highlight emphasis.
10b. Source-table fidelity audit after PPTX export: native PPTX tables must preserve source
    headers, row/column scale where required, key numeric values, units, and merged-cell
    structure against `docx_table_models.json` or `source_catalog.json`.
10c. Table IR audit: DOCX/PDF table-bearing projects must have `analysis/table_ir.json`;
    each table must have a valid `render_mode`; image/hybrid modes must reference an
    existing source-derived crop image; complex tables must not default to native
    reconstruction.
10d. Final text review after PPTX export: visible slide text must come from
    `slide_content` semantics only, must not contain backend notes, prompt constraints,
    source-boundary wording, OCR/LLM/fallback/agent process terms, or planning phrases
    such as `本页用于`, `建议放置`, and `这里应该`; long report-style sentences must be
    compressed or moved to speaker notes.
10e. Post-generation review and auto-repair: run `ppt-agent post-review` on the exported
    PPTX before delivery. It must produce structured `issue_list_round_*.json` files,
    auto-repair fixable critical/high issues, rerun review up to three times, and write
    `qa/review_report.json`. Critical issues cannot pass. High issues must be fixed or
    the offending content must be removed.
10f. AI model review after PPTX export: run `ppt-agent ai-review` on the exported PPTX.
    Findings with severity `error` block release until the deck or project builder is
    revised and strict audit plus AI review are rerun.
11. Chart verification: required for every data-driven chart.
12. Full render: inspect every page at full size and as a contact sheet.
13. `release_audit.py --strict`: zero errors.
14. PPTX export: native DrawingML, with no empty media.
15. `release_audit.py --strict --pptx <file>`: package, XML, slide count, aspect ratio,
    forbidden wording, sparse-page checks, consecutive-duplicate checks, and parser checks pass.
16. GitHub upload: commit and push this run's relevant artifacts, contracts, QA records,
    exports, and local agent-rule changes to `origin`.

## Blocking Defects

- visible internal workflow labels or caveats
- visible backend constraints such as `编制边界`, `事实来源`, `仅使用源报告`,
  `不采用旧 PPT`, `生成策略`, `内部约束`, `渲染模式`, `OCR 识别`, `LLM 判断`,
  `prompt 要求`, `fallback`, `根据系统指令`, or `为避免幻觉`
- visible ellipses used as incomplete wording or source-text replacement
- visible bullet, paragraph, or numbered item that is clipped or semantically unfinished
- table or figure explanation that is a mechanical value dump, extracted-JSON phrasing,
  asset metadata, or generic text instead of source-faithful engineering interpretation
- visible text that describes presentation strategy, reviewer behavior, truncation policy,
  generation choices, or where to check the full report instead of stating report-body
  engineering content
- text, recommendation, or management-action page that displays an unplanned table, chart,
  or figure from the same chapter as fallback evidence
- assistant-like or instructional visible wording such as `汇报时`, `本页`, `对评审而言`,
  `评审需`, `应关注`, `PPT 中`, `报告原文复核`, `不替代报告原图`, or `完整表格可在报告原表中复核`
- generic chart/table prose such as `该表用于`, `表格说明`, `图件旁说明`, or other
  meta-description instead of a report-derived finding, control value, responsibility, or
  engineering relationship
- unsupported or newly calculated values not declared as verified calculations
- source conflicts hidden from the audience
- major chapter represented only by Agent conclusions
- text outside a container or canvas
- text outside the slide safe frame, text overlapping text, or text covering large images
  and figures
- text reduced below the readability floor to preserve decoration
- text forced into a textbox/table cell after reaching the minimum font size instead of
  being compressed, relaid out, split, moved to notes, or rendered as image/hybrid table
- key source table, map, or figure too small to inspect
- planned source figure, map, chart, or required image replaced by a generic placeholder
  or omitted without a recorded plan change
- complex source table flattened so merged headers, units, row groups, or footnotes become
  misleading or unreadable
- complex source table reconstructed by the LLM or via Markdown instead of rendered from
  Table IR as native/image/hybrid
- image/hybrid table inserted with distorted aspect ratio or without a source-derived crop
- overlong source table inserted as cross-page PPT content instead of being omitted from
  visible slides and recorded in backend evidence/quality notes
- DOCX table-heavy deck rendered without a `docx_table_models.json` structure pass or
  without native merged-cell rendering for small/medium source tables that fit the slide
- sparse page containing neither adequate explanation nor substantive source evidence
- consecutive content pages whose body text is near-identical while only the title or figure changes
- technical chapters reduced to summary cards without enough original text, tables, figures,
  formulas, or source-backed mixed layouts
- more than three high-level summary / overview / conclusion / management-action pages
  unless the user explicitly approved the exception
- split paragraphs shown as anonymous text stacks without visible item numbers or short
  paragraph names
- content slides with important values or terms but no visible emphasis treatment
- native PPTX table headers, numbers, row/column scale, or merge structure inconsistent
  with the source table model/catalog
- non-template body/table/chart text smaller than 14 pt
- corrupt PPTX, slide-count mismatch, empty media, or invalid XML
- completed local run that has not been uploaded to GitHub and has no explicit blocker report

`qa/release_audit.json` and `qa/release_audit.md` are required release records.
