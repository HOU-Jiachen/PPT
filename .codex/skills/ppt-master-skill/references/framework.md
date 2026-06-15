# PPT Annotation Framework Reference

This document describes the "Annotation Framework" used by the `ppt-master-skill`.

## Tag Syntax
Placeholders in your PPTX template should use the following syntax:
`{{TAG_NAME}}`

### Examples:
- `{{ProjectName}}`
- `{{Date}}`
- `{{Summary}}`
- `{{Milestone1}}`

## Best Practices
1.  **Tag Integrity**: PowerPoint often splits text into multiple XML nodes if you edit it piecemeal. To ensure the script finds your tags, try to type the entire `{{TAG_NAME}}` in one go, or copy-paste it from a plain text editor.
2.  **Naming**: Use descriptive, camelCase or PascalCase names for tags to make it easy for the AI agent to map report data to them.
3.  **Consistency**: Use the same tags across different templates for similar report types (e.g., all weekly reports should use `{{WeeklySummary}}`).

## Data Extraction
The AI agent will analyze your report and attempt to fill these tags. You can guide the agent by providing a list of tags you've included in your template.

## Technical Details
The `generate_ppt.cjs` script performs a literal string replacement in the slide XML files. It does not currently support complex logic like repeating rows in tables or conditional slides. For advanced needs, consider using the `python-pptx` library if available.
