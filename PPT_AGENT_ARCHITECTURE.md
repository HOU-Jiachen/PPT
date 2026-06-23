# PPT Agent Architecture

## Design

This repository uses a three-layer model:

1. `.vendor/ppt-master/skills/ppt-master/` is the pinned upstream execution kernel.
2. `.codex/skills/engineering-ppt/` is the local engineering-report orchestration layer.
3. `.codex/skills/engineering-ppt/references/frontier-agent-fusion.md` is the
   frontier-method fusion layer for public PPT agent research.

The local layer adds source traceability, claim-first story design, Chinese engineering
defaults, project routing, Windows commands, and mandatory visual QA. It does not fork
or patch upstream implementation files.

## Frontier Baseline

As of 2026-06, the strongest open public PPT-generation line is
`icip-cas/PPTAgent`, especially its `DeepPresenter` branch. It supports reflective
generation, PPTX export, offline mode, MCP integration, sandboxed tools, and a
published PPT-specialized model:

- Full model: `Forceless/DeepPresenter-9B`
- Lightweight local model: `Forceless/DeepPresenter-9B-GGUF`

This repo does not vendor those models by default. They are optional generation
backends that can be connected later through an approved local OpenAI-compatible
endpoint. The current integration takes the ideas that improve reliability without
adding heavyweight runtime dependencies:

- DeepPresenter: render, observe, revise, and keep reflection grounded in actual
  slide artifacts.
- AeSlides: audit aspect preservation, occupied area, collisions, and visual balance
  with deterministic layout metrics.
- MemSlides: keep persistent rules in the skill, run-specific decisions in project
  contracts, and targeted edits scoped to the smallest affected slide region.
- SlideBot/PreGenie: retain modular multimodal analysis and retrieval-grounded
  planning where useful, while keeping verified project sources as the authority.

## Commands

```powershell
.\scripts\ppt-agent.cmd doctor
.\scripts\ppt-agent.cmd status
.\scripts\ppt-agent.cmd init "项目名称" -Format ppt169
.\scripts\ppt-agent.cmd update
```

`update` fast-forwards the vendored upstream repository. Review upstream release notes
and run `doctor` after updating.

`audit` also runs deterministic frontier layout checks through
`qa/release_policy.json > aesthetic_layout`.

## Project Artifacts

Each project should converge on:

```text
projects/<name>/
  sources/          source documents and extracted material
  analysis/
    source_catalog.json addressable paragraphs, tables, figures, and values
    source_corpus.txt normalized corpus used by quantitative audit
  images/           verified images and generated assets
  evidence_ledger.json reviewed facts, source objects, calculations, and interpretations
  deck_plan.json    machine-readable chapter, evidence, and visual-proof plan
  source_map.md     fact, metric, conflict, and provenance index
  chapter_coverage.md report-chapter coverage and source-preservation plan
  claim_spine.md    slide-level argument and evidence plan
  design_spec.md    human-readable design rationale
  spec_lock.md      machine-readable execution contract
  svg_output/       authored slide SVGs
  notes/            speaker notes
  qa/text-fit.md    full-size text overflow and minimum-font audit
  qa/source-coverage.md original text/table/figure coverage audit
  qa/release_policy.json project release thresholds and forbidden wording
  qa/release_audit.json machine-readable final gate
  exports/          final editable PPTX files
```

## Evidence Pipeline

```text
Original files
  -> source catalog
  -> human/agent verification
  -> evidence ledger
  -> chapter coverage
  -> deck plan
  -> design spec and spec lock
  -> SVG authoring
  -> strict release audit
  -> native PPTX
  -> strict package audit
```

Visible slide content may reference only verified evidence. Extraction warnings and workflow
labels remain in project records and never appear in the deck.

## Planning Policy

- Derive slide count from chapter complexity, source evidence volume, and readable layout.
- Preserve the report's major chapter sequence for full-report presentations.
- Balance original evidence and interpretation: show important source paragraphs, tables,
  figures, maps, and calculations before summarizing conclusions.
- Prefer a restrained, consistent visual grammar over forced layout novelty.
- Treat text overflow, undersized key content, and unreadable source figures as release blockers.
- Treat unsupported numbers, unverified evidence, visible internal labels, and chapters without
  original evidence as release blockers.
- Treat disabled image aspect preservation and severe visual imbalance/element collision as
  release blockers under strict audit.

## Upgrade Policy

- Never edit `.vendor/ppt-master` for local behavior.
- Put local rules in `engineering-ppt`.
- Put reusable local scripts under `scripts/`.
- Keep the upstream commit visible in QA reports for reproducibility.
