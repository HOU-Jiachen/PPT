---
name: engineering-ppt
description: Generate, rebuild, review, or optimize editable, source-faithful engineering and project-report PowerPoint decks from PDF, DOCX, XLSX, PPTX, Markdown, URLs, images, or raw text. Use for Chinese engineering reports, technical reviews, feasibility studies, water resources, municipal infrastructure, construction, planning, and any PPT where chapter coverage, original evidence, quantitative accuracy, readable layout, and Office-compatible PPTX output matter. Uses the vendored hugohe3/ppt-master kernel with mandatory evidence and release gates.
---

# Engineering PPT

Use this skill as the evidence and release-control layer. Use
`../../../.vendor/ppt-master/skills/ppt-master/` as the immutable rendering kernel.

## 1. Resolve And Diagnose

Set:

```text
REPO_ROOT=<workspace root>
CORE_DIR=<REPO_ROOT>/.vendor/ppt-master/skills/ppt-master
PROJECT_NAME=<explicit user project, otherwise CURRENT_PROJECT.txt>
PROJECT_DIR=<REPO_ROOT>/projects/<PROJECT_NAME>
LOCAL_SKILL=<REPO_ROOT>/.codex/skills/engineering-ppt
```

Read `<REPO_ROOT>/AGENT.md`, this file, and `<CORE_DIR>/SKILL.md`. Run:

```powershell
scripts\ppt-agent.cmd doctor
```

Do not patch `.vendor/ppt-master`. Put all local behavior in this skill.

## 2. Select One Mode

| Mode | Trigger |
|---|---|
| `create` | Build a new deck from source material |
| `template-fill` | Explicitly reuse an existing PPTX design |
| `targeted-edit` | Change selected pages while preserving the rest |
| `review` | Diagnose story, evidence, visual, or technical defects |
| `resume` | Continue a project with complete contracts and specs |

Use upstream workflows for rendering, template-fill, live preview, and export. Use the
local evidence workflow below for all engineering-report content.

## 3. Initialize Project Contracts

Run:

```powershell
scripts\ppt-agent.cmd prepare "<project>"
```

This creates:

```text
evidence_ledger.json
deck_plan.json
analysis/
qa/release_policy.json
```

Never begin slide authoring without these files.

## 4. Build The Source Catalog

Preserve original files. Copy sources into `sources/` or pass explicit source paths, then run:

```powershell
scripts\ppt-agent.cmd catalog "<project>"
```

The catalog must recover:

- heading hierarchy and chapter boundaries
- paragraphs whose wording matters
- tables with rows, columns, units, and notes
- figures, maps, captions, and appendices
- formulas and calculation sequences
- source locations for every extracted object

The catalog must treat only user/source material as source. Agent-generated planning,
coverage, design, QA, and deck-contract files are backend records and must not become
visible-content candidates.

Read [evidence-contract.md](references/evidence-contract.md). Review the original Office/PDF
object before marking evidence `verified`; extracted text alone is not authoritative when it is
damaged, merged, or incomplete.

Read [frontier-agent-fusion.md](references/frontier-agent-fusion.md) before planning or
reviewing a deck. Use it to apply DeepPresenter-style rendered-artifact reflection,
AeSlides-style deterministic layout metrics, and MemSlides-style scoped revision memory
without replacing the local evidence-first workflow.

## 5. Build The Report Content Inventory And PPT Blueprint

Run:

```powershell
scripts\ppt-agent.cmd analyze "<project>"
```

This creates:

```text
analysis/report_content_inventory.json
analysis/ppt_content_blueprint.md
```

This stage is mandatory before `evidence_ledger.json`, `chapter_coverage.md`,
`deck_plan.json`, `design_spec.md`, or any slide authoring is completed.

The inventory must preserve the report's material before presentation shaping:

- all available heading levels and parent-child title paths
- important original paragraphs and their source locators
- original tables with captions/titles, row/column scale, units, and split hints
- original figures/maps/charts with captions/titles, asset links, and source locators
- formula/calculation-bearing paragraphs and parameter/result tables
- candidate PPT content units with catalog IDs, source modes, layout hints, and split hints

Then read `analysis/ppt_content_blueprint.md` and think through the PPT content before
planning pages. For every report chapter or dense subsection, decide:

- what the audience needs to understand or decide
- which exact original text/table/figure/formula must remain visible
- which source objects should be paired on the same slide
- which dense objects should be split across multiple slides
- what the visible small title should be, preferring the report heading or table/figure caption
- what interpretation is needed beside the source evidence, without replacing it
- whether each figure is better served by a side-by-side layout or a top-figure/bottom-text
  layout; horizontal maps and paired wide figures normally need the latter so the figures stay
  inspectable

Do not treat the generated blueprint as final thinking. It is the structured workspace.
The agent must refine it mentally or in writing before `deck_plan.json`, and each
substantive planned page should be traceable to one or more content-unit IDs or to a
recorded reason that no suitable source object exists.

## 6. Build The Evidence Ledger

Select source-catalog entries into `evidence_ledger.json`.

Classify each record as:

```text
FACT | ORIGINAL_TEXT | ORIGINAL_TABLE | ORIGINAL_FIGURE |
CALCULATION | INTERPRETATION | RECOMMENDATION
```

Mandatory rules:

- Record every visible quantitative value with unit and time basis.
- Store calculation formulas and verified inputs. Do not calculate missing values.
- Keep conflicting source values separate and disclose the conflict.
- Keep interpretation as interpretation. Never promote it to fact.
- Treat old PPT decks and outlines as leads, not authoritative sources.
- Keep workflow notes and extraction warnings out of visible slides.
- Use `analysis/report_content_inventory.json` and `analysis/ppt_content_blueprint.md`
  as the primary selection workspace; do not select evidence only from memory or from
  an old deck outline.

## 7. Build Chapter Coverage And Deck Plan

Create `chapter_coverage.md`, then read
[deck-plan-contract.md](references/deck-plan-contract.md) and complete `deck_plan.json`.

Preserve the report's major chapter order. Within each chapter prefer:

```text
source context -> original text/table/figure/calculation -> explanation -> chapter conclusion
```

Insert a chapter divider page before each substantive report chapter. The divider must show
the chapter sequence number and the report chapter name; it is a structural slide and does
not replace the chapter's source evidence pages.

No major chapter may be represented only by a conclusion slide.

Allocate slides from evidence volume and readability:

- short chapter: 1-2 slides
- normal chapter: 3-5 slides
- table-, figure-, or calculation-heavy chapter: 6+ slides

Treat page-count requests as guidance unless explicitly hard. Split pages before shrinking key
text, tables, maps, or figures.

Each substantive slide must declare:

```text
chapter | source_mode | evidence_ids | visual_proof | layout_pattern | source_note | density
```

In the backend plan or notes, also keep the selected content-unit IDs from
`analysis/report_content_inventory.json` whenever possible. These IDs do not belong in
visible slide text.

Original-source modes must form a meaningful part of technical chapters. Do not make the deck
a sequence of Agent-generated summary cards.

For engineering review decks, original-source modes should normally cover at least 55% of
substantive slides. Do not place more than two interpretation / conclusion / management-action
slides in a row unless the source chapter truly has no usable original figure, table, formula,
or important source text and the exemption is recorded.

Use mixed evidence layouts as the default for source-heavy pages:

```text
left_text_right_figure | left_figure_right_text |
top_text_bottom_figure | top_figure_bottom_text |
left_text_right_table | left_table_right_text |
top_text_bottom_table | top_table_bottom_text
```

Use standalone summary cards sparingly: primarily for cover/agenda/chapter openers, decision
summaries, and final conclusions. Technical process pages should pair original evidence with
faithful explanation.

Visible text rules:

- Small titles and panel headings must prefer report section headings, figure captions, table
  captions, or the paragraph's corresponding subsection title.
- Never show backend labels such as `原始对象`, `必讲内容`, `保留理由`, `证据`, asset filenames,
  evidence IDs, or source-mode strings.
- Never show ellipses (`...`, `…`, `……`) as a substitute for long source text. Summarize to
  complete, source-faithful sentences or split the page.
- Never leave a visible bullet, paragraph, or numbered item semantically unfinished. If a
  source paragraph is too long for the frame, rewrite it into complete report-language
  points or split the page before export.
- After final font sizing, verify text-box capacity and table-cell capacity; if text does not
  fit at the minimum font size, shorten, enlarge, or split the page.

## 8. Confirm Design Once

Present one concise confirmation bundle:

1. canvas and evidence-derived page estimate
2. audience and decision objective
3. report chapter flow
4. report-content inventory and PPT blueprint summary
5. source-preservation plan
6. visual system and typography
7. image, table, and chart policy
8. source-rich layout mix and minimum original table/figure/text coverage

Wait once for explicit confirmation. Then write `design_spec.md` and `spec_lock.md` and continue
automatically.

Default Chinese engineering choices:

- 16:9
- Microsoft YaHei-led font stack
- restrained government/consulting visual language
- three to five stable layout families
- source-backed charts only
- no decorative pseudo-data
- no progress bars, badges, ribbons, or repeated framing unless meaningful

## 9. Author With The Upstream Kernel

Follow the serial upstream pipeline. Re-read `spec_lock.md` before every page.
Also keep `analysis/ppt_content_blueprint.md` open as the content authority for
chapter order, small titles, source pairings, and split decisions.

Local source-preservation overrides:

- Use verified original figures at source resolution.
- Give key maps and figures at least 45% of slide area.
- Before rebuilding a complex table, inspect its source structure: merged cells, multi-row
  headers, units, subtotal rows, footnotes, and row groups. Preserve that structure as a
  native table when practical; otherwise use a source crop/image plus a simplified key-row
  table. Do not flatten merged-cell tables into unreadable rows.
- Center table cell content horizontally and vertically by default unless the source table
  clearly requires another alignment.
- Split or crop source tables instead of shrinking them.
- Planned source figures are mandatory evidence. If a planned figure cannot be located or
  embedded, stop and repair the source/media mapping or change the deck plan with a recorded
  reason. Never silently replace a required figure with a generic placeholder.
- Prefer original-source mixed pages over empty summary pages: left text / right figure,
  left figure / right text, top text / bottom figure, top figure / bottom text, left text /
  right table, left table / right text, top text / bottom table, or top table / bottom text.
- When a source page would otherwise feel sparse, add the nearest relevant original chart,
  map, table crop, formula, or exact source parameter before adding decorative cards.
- Retain units, time basis, footnotes, and uncertainty notes.
- Put interpretation beside or after original evidence, never in its place.
- Figure and table side explanations must be agent-authored, source-faithful engineering
  interpretation grounded in the report, not a mechanical dump of extracted JSON fields,
  row counts, asset filenames, or naked values. Generic text such as `报告列示数值` is a
  content defect.
- Agent-authored visible text must be report-body prose only. It may paraphrase the
  report's engineering meaning, but it must not describe presentation strategy, review
  behavior, generation choices, truncation policy, or where the audience should look later.
  Phrases such as `汇报时`, `本页`, `对评审而言`, `评审需`, `PPT 中`, `报告原文复核`,
  `完整表格可在报告原表中复核`, and `不替代报告原图` are visible-content defects.
- De-AI visible prose: use concise Chinese engineering-report style with project nouns as
  subjects, such as `工程特性表明确...`, `防治责任范围为...`, `措施体系包括...`.
  Avoid assistant-like guidance words including `应优先`, `应关注`, `不能理解为`,
  `只保留`, `不只展示`, and other instructions to a presenter or reviewer.
- Use topic titles for faithful source pages; do not force every title into a new conclusion.
- Prefer report headings and table/figure captions for visible small titles.
- Keep visible source notes concise and professional.

Never show internal labels such as:

```text
报告原文摘录 | 工程原文摘录 | 缺失项沿用提取状态 |
不做补造 | 审查提示 | 数据提示 | 口径A | 口径B
```

Never show planning or extraction metadata such as:

```text
来源模式 | 证据编号 | 本页用于 | 证据解读 | 原表定位 |
行列规模 | 密集表按重点行重排 | 完整数据回看报告原表 |
source_mode | evidence_ids | visual_proof | layout_pattern | source_note |
image_003.png | E-1-OBJECTIVE
```

Never show generic panel headings such as:

```text
报告对图件的说明 | 报告对表格的说明 | 报告计算口径 | 报告阐述
```

Small titles beside figures, tables, formulas, and source text must name the
specific engineering content being shown, for example `图件重点：矿区强径流带分布`
or `表格重点：不同标高涌水量预测结果`. Treat a generic label as a content defect,
not a style preference.

Visible slide text must be audience-facing report language: use the report's original
wording or a faithful, layout-shortened paraphrase of what the report says about the
current text, table, figure, formula, conclusion, or recommendation. Keep extraction
IDs, asset filenames, row/column counts, and workflow rationale in backend contracts,
speaker notes, or QA records only.

Communicate source conflicts with neutral report language, not Agent-process language.

### Keep Project Builders Thin

Do not let per-project `.py` builders become the permanent home for reusable agent logic.
Project scripts should mostly orchestrate:

- project paths and source filenames
- project-specific cover text, anchor pages, and special slide choices
- calls into shared skill helpers
- output, notes, and QA artifact paths

Reusable behavior belongs under `<LOCAL_SKILL>/scripts/` or skill references, including:

- template PPTX profiling and learned style rules
- visible-text hygiene and forbidden metadata scrubbing
- evidence-ledger lookup and report-language extraction
- figure/table matching, image panel layout, and table simplification
- design/spec-lock generation and repeatable QA helpers

When a user supplies or replaces a reference PPTX under `projects/<project>/template`,
run a template profile pass and write the result to `analysis/template_profile.json`.
Use that profile as backend design guidance only; never make the reference PPT a new
source of engineering facts unless the user explicitly says it is authoritative source
material. The visible deck should still cite the report, source figures, source tables,
or faithful report-language paraphrases.

## 10. Enforce Text Fit And Page Fulness

Every text container must have explicit width, height, font size, and line plan.

Resolve overflow in this order:

1. remove repetition
2. add deliberate line breaks
3. enlarge the text area
4. split the page
5. reduce font only within minimum-size rules

Do not rely on PowerPoint auto-fit. Do not let text cross a border or overlap another object.
Do not reduce key body text below 18 pt merely to preserve decoration.
Apart from template/meta text such as page numbers, page footers, and source notes, visible
PPT body text, table text, and chart labels must never be below 14 pt.
The strict audit must check text fit geometrically after final font sizing and final PPTX
export: text cannot cross the slide safe frame, visible text boxes cannot overlap each
other, and body text cannot cover large source images, figures, or tables. Treat any such
collision as a blocking layout defect, then fix by shortening, moving, widening, or
splitting the page.

For a sparse page, add the next relevant source-backed object:

1. original figure or crop
2. original/recreated table
3. formula or calculation sequence
4. exact project parameters
5. faithful explanatory text

Do not fill space with invented metrics or decorative cards.

## 11. Run Release Gates

Read [release-gates.md](references/release-gates.md) and
[frontier-agent-fusion.md](references/frontier-agent-fusion.md). Run:

1. upstream `svg_quality_checker.py`
2. upstream `verify-charts` for data-driven charts
3. render every slide and inspect contact sheet plus full-size pages
4. local strict audit before export
5. native PPTX export
6. local strict audit with the PPTX
7. GitHub upload gate: commit and push this run's relevant project artifacts,
   contracts, QA records, exports, and local agent-rule changes to `origin`

Commands:

```powershell
scripts\ppt-agent.cmd audit "<project>" -Strict
scripts\ppt-agent.cmd audit "<project>" -Strict -Pptx "<file>"
```

Fix every error. Do not call the deck complete merely because a PPTX exists.
Do not call the run complete if GitHub upload has not succeeded, unless the final response
clearly reports the upload blocker (missing remote, authentication failure, network failure,
or permission failure) and lists what remains local-only.

## 12. Deliver

Deliver the native editable PPTX from `exports/` and report:

- output path and slide count
- chapter and original-source coverage
- source conflicts preserved
- QA checks passed
- GitHub branch, commit, and push status
- any remaining human review

The final PPTX must pass ZIP, XML, slide-count, media, aspect-ratio, forbidden-wording, and
`python-pptx` parser checks.

Before the final response, run the GitHub sync procedure from `<REPO_ROOT>/AGENT.md`.
Stage only files changed or generated by the current run; do not stage unrelated user work.
