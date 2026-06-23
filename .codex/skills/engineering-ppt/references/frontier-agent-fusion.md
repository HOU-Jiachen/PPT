# Frontier PPT Agent Fusion

This reference records the best currently useful ideas from public PPT-generation
agent research and how to apply them inside this engineering PPT skill without
replacing the local evidence-first workflow.

## Current Best Open Frameworks And Models

Use this ranking when choosing inspiration or external compatibility:

1. `DeepPresenter` / `PPTAgent` is the strongest open-source implementation line
   for general PPT generation as of 2026-06. It adds environment-grounded
   reflection: plan, render, observe the rendered artifact, then revise. Its
   project also publishes `DeepPresenter-9B`, a presentation-generation model
   based on Qwen3.5-9B, with full and GGUF weights.
2. `AeSlides` contributes the most practical quality-control idea: do not depend
   only on VLM judgement. Convert aesthetics into verifiable metrics such as
   aspect-ratio preservation, occupied area, element collision, and visual
   balance. Keep these as deterministic release checks.
3. `MemSlides` contributes the memory architecture for repeated user work:
   separate persistent user preference memory, per-run working memory, and tool
   memory. For this repo, persistent memory should remain in skill references and
   project contracts; per-run memory belongs in `design_spec.md`, `spec_lock.md`,
   `deck_plan.json`, QA records, and human feedback notes.
4. `PreGenie` and `SlideBot` are useful conceptual references for modular
   multimodal analysis, retrieval-grounded planning, and rendered-slide review,
   but they should not override native PPTX editability or source-evidence rules.

## Fusion Policy

Keep the local system as a three-layer agent:

1. Evidence layer: `source_catalog.json`, `report_content_inventory.json`,
   `ppt_content_blueprint.md`, `evidence_ledger.json`, and `deck_plan.json`.
2. Rendering layer: upstream `ppt-master` strict serial SVG/PPTX kernel.
3. Reflection layer: deterministic audits plus visual inspection after rendering.

Adopt frontier ideas this way:

- DeepPresenter-style environment observation: after SVG generation and again
  after PPTX export, inspect rendered output and revise pages whose observed
  state conflicts with evidence, layout, or readability requirements.
- AeSlides-style verifiable rewards: run deterministic layout checks for source
  image aspect preservation, excessive whitespace, visual imbalance, and
  element collisions. These checks are not a substitute for full-size visual QA.
- MemSlides-style memory: preserve reusable rules in this skill, project-specific
  decisions in contracts, and local human feedback in QA notes. Targeted edits
  should update only affected pages and contracts, not regenerate the whole deck
  unless the structure has changed.
- SlideBot-style reliability: retrieval or web research may support topic-only
  decks, but engineering report decks must prefer user-provided source files and
  verified source objects.

## Model Routing

When the user asks for open-source local generation models:

- Recommended PPT-specialized model: `Forceless/DeepPresenter-9B`.
- Lightweight local option: `Forceless/DeepPresenter-9B-GGUF` via llama.cpp,
  Ollama, LM Studio, or another OpenAI-compatible local server.
- General fallback models can plan text and code, but they must still pass this
  skill's evidence, layout, and PPTX release gates.

Do not automatically download or install these models during a PPT run. Treat
them as optional backends that require user approval, disk/GPU planning, and a
configured local endpoint.

## Reflection Checklist

Before calling a deck complete, confirm all of the following:

- The rendered slides preserve source text, tables, figures, formulas, units,
  uncertainty, and conflicts.
- Source figures are not visibly distorted, and wide engineering figures are not
  forced into narrow panels.
- Occupied page area is high enough for substantive pages, without crowding.
- The visual center of mass is not unintentionally pushed to one edge.
- Text and source objects do not collide in SVG output or native PPTX output.
- Any targeted user revision changes the smallest affected slide region and
  leaves unrelated pages untouched.
