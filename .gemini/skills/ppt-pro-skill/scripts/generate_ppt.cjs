const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const [,, templatePath, dataPath, outputPath] = process.argv;

if (!templatePath || !dataPath || !outputPath) {
    console.error('Usage: node generate_ppt.cjs <template.pptx> <data.json> <output.pptx>');
    process.exit(1);
}

const absTemplatePath = path.resolve(templatePath);
const absDataPath = path.resolve(dataPath);
const absOutputPath = path.resolve(outputPath);

if (!fs.existsSync(absTemplatePath)) {
    console.error(`Error: Template not found at ${absTemplatePath}`);
    process.exit(1);
}

if (!fs.existsSync(absDataPath)) {
    console.error(`Error: Data file not found at ${absDataPath}`);
    process.exit(1);
}

const data = JSON.parse(fs.readFileSync(absDataPath, 'utf8'));

// Helper to escape XML special characters
function escapeXml(unsafe) {
    return String(unsafe).replace(/[<>&"']/g, function (c) {
        switch (c) {
            case '<': return '&lt;';
            case '>': return '&gt;';
            case '&': return '&amp;';
            case '"': return '&quot;';
            case "'": return '&apos;';
        }
    });
}

/**
 * Robustly replaces tags in PPTX XML.
 * Handles split tags and multiline text correctly.
 */
function processXml(content, data) {
    // 1. "Heal" split tags. PowerPoint often splits {{Tag}} into multiple <a:r> nodes.
    // We look for patterns where a tag is split across text nodes with the same formatting.
    // This regex joins adjacent text nodes within the same paragraph if they seem to be part of a tag.
    let healed = content;
    
    // Healer Pattern: </a:t></a:r><a:r><a:rPr>...</a:rPr><a:t>
    // If the rPr is identical, we can merge. For simplicity, we merge all adjacent text nodes 
    // that don't have different rPr.
    healed = healed.replace(/<\/a:t><\/a:r><a:r>(?:<a:rPr[^>]*\/>)?<a:t>/g, '');
    healed = healed.replace(/<\/a:t><\/a:r><a:r><a:rPr>([\s\S]*?)<\/a:rPr><a:t>/g, (match, rPr) => {
        // Only merge if the rPr is empty or very simple (common in auto-splits)
        return ''; 
    });

    // 2. Perform replacements
    let modified = false;
    for (const [key, value] of Object.entries(data)) {
        const tag = `{{${key}}}`;
        if (healed.includes(tag)) {
            const escapedValue = escapeXml(value);
            const lines = escapedValue.split('\n');
            
            // We need to replace the tag but ensure <a:br/> is OUTSIDE <a:t>
            // Logic: split by tag, then join with XML fragments that close and reopen tags.
            healed = healed.split(tag).map((part, i, arr) => {
                if (i === arr.length - 1) return part;
                
                // Find the preceding run properties to preserve formatting
                const rStart = part.lastIndexOf('<a:r');
                const rPrMatch = part.substring(rStart).match(/<a:rPr[^>]*>[\s\S]*?<\/a:rPr>/);
                const rPr = rPrMatch ? rPrMatch[0] : '';
                
                // Join lines with: close current t/r, add br, open new r/t with same properties
                const replacement = lines.join(`</a:t></a:r><a:br/><a:r>${rPr}<a:t>`);
                modified = true;
                return part + replacement;
            }).join('');
        }
    }
    
    return { healed, modified };
}

const tmpDir = path.resolve(process.cwd(), `tmp_ppt_${Date.now()}`);

try {
    // 1. Unzip using tar
    const contentDir = path.join(tmpDir, 'content');
    fs.mkdirSync(contentDir, { recursive: true });
    console.log(`Extracting ${templatePath}...`);
    execSync(`tar -xf "${absTemplatePath}" -C "${contentDir}"`);

    // 2. Process all XML files
    const walker = (dir) => {
        const files = fs.readdirSync(dir);
        for (const file of files) {
            const fullPath = path.join(dir, file);
            if (fs.statSync(fullPath).isDirectory()) {
                walker(fullPath);
            } else if (file.endsWith('.xml')) {
                let content = fs.readFileSync(fullPath, 'utf8');
                const { healed, modified } = processXml(content, data);
                if (modified) {
                    fs.writeFileSync(fullPath, healed, 'utf8');
                }
            }
        }
    };
    walker(contentDir);

    // 3. Re-zip using .NET ZipFile
    console.log(`Packaging ${outputPath}...`);
    if (fs.existsSync(absOutputPath)) {
        fs.unlinkSync(absOutputPath);
    }
    
    const tmpZipOutput = path.join(tmpDir, 'output.zip');
    const psCommand = `Add-Type -AssemblyName System.IO.Compression.FileSystem; [System.IO.Compression.ZipFile]::CreateFromDirectory('${contentDir}', '${tmpZipOutput}')`;
    execSync(`powershell -NoProfile -Command "${psCommand}"`);
    
    fs.renameSync(tmpZipOutput, absOutputPath);
    console.log(`✅ Success: Generated ${outputPath}`);
} catch (err) {
    console.error('❌ Error generating PPT:', err.message);
    process.exit(1);
} finally {
    if (fs.existsSync(tmpDir)) {
        try {
            fs.rmSync(tmpDir, { recursive: true, force: true });
        } catch (e) {
            console.warn(`Warning: Could not clean up temp directory ${tmpDir}`);
        }
    }
}
