---
name: ppt-pro-skill
description: High-fidelity PPT generation skill based on the 'ppt-master' methodology. Uses semantic template mapping, XML normalization to heal split tags, and robust .NET compression to ensure corruption-free outputs.
---

# PPT Pro: Semantic Generation & Robust Engine

This skill implements an advanced workflow for generating professional PowerPoint presentations, inspired by the `hugohe3/ppt-master` project. It moves beyond simple text replacement to ensure structural integrity and semantic alignment.

## Advanced Workflow

### Step 1: Semantic Template Analysis
- **Action**: Extract the template and scan all XML files for placeholders.
- **Goal**: Identify *every* tag, even those split by PowerPoint's XML engine (e.g., `{{` in one node, `Tag}}` in another).
- **Tool**: Use `list_tags.cjs` or a similar script with "healing" logic.

### Step 2: Contextual Data Mapping
- **Action**: Analyze the project report and map key findings to the *actual* placeholders found in Step 1.
- **Goal**: Ensure content fits the visual intent of the slide (e.g., mapping summary points to bullet-point boxes).

### Step 3: Robust XML Injection
- **Action**: Use the overhauled `generate_ppt.cjs` engine.
- **Key Features**:
    - **Tag Healing**: Automatically joins adjacent text nodes to find split tags.
    - **Multiline Support**: Breaks out of `<a:t>` and `<a:r>` tags to insert `<a:br/>`, preserving formatting while maintaining XML validity.
    - **Entity Escaping**: Ensures all characters are XML-safe.

### Step 4: High-Fidelity Packaging
- **Action**: Use .NET `ZipFile` via PowerShell to archive the PPTX.
- **Goal**: Ensure critical files like `[Content_Types].xml` and `_rels/.rels` are correctly preserved and the archive is 100% compatible with MS Office.

## Best Practices
- **Analyze First**: Never assume the tags in `data.json` match the template. Always scan the template first.
- **Formatting**: Use `\n` for bullet points. The engine will handle the complex XML restructuring.
- **Validation**: After generation, verify the file with `tar -tf` to ensure `[Content_Types].xml` exists.

## Bundled Resources
- `scripts/generate_ppt.cjs`: The robust generation engine.
- `references/framework.md`: Tagging conventions.
