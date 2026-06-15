---
name: ppt-master-skill
description: AI agent specialized in generating project report PPTs from text reports and PPT templates using an annotation framework. Use this skill when you need to read a project report, extract key data, and fill placeholders in a PPTX template.
---

# PPT Master: Annotation Framework Agent

This skill enables you to act as an "Annotation Framework Agent" to automate the generation of project report presentations.

## Core Workflow

1.  **Identify Inputs**: Ask the user for the path to the project report (text or markdown) and the PPT template (.pptx).
2.  **Extract Data**: Read the project report. Identify key information like Project Name, Summary, Milestones, Risks, etc.
3.  **Map to Template**: Identify placeholders in the PPT template (typically in `{{VariableName}}` format).
4.  **Prepare JSON**: Create a JSON file containing the mapping of tags to extracted content.
    *   Example: `{"ProjectName": "Codex PPT", "Summary": "Automated PPT generation."}`
5.  **Generate PPT**: Execute the `generate_ppt.cjs` script bundled with this skill.

## Usage Guide

To generate a PPT:
1. Use `read_file` to understand the report content.
2. Formulate a JSON object representing the data for the template.
3. Use `run_shell_command` to execute the generation script:
   ```bash
   node scripts/generate_ppt.cjs <template.pptx> <data.json> <output.pptx>
   ```

## Tagging Convention
The annotation framework uses the `{{TAG_NAME}}` syntax. Ensure the PPT template contains these placeholders in text boxes.

For detailed framework documentation, see [references/framework.md](references/framework.md).
