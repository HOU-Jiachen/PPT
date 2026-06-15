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

const data = JSON.parse(fs.readFileSync(absDataPath, 'utf8'));

// Helper to escape XML
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

function processXml(content, textData) {
    let result = content;
    // Simple healing for split tags
    result = result.replace(/<\/a:t><\/a:r><a:r>(?:<a:rPr[^>]*\/>)?<a:t>/g, '');
    
    let modified = false;
    for (const [key, value] of Object.entries(textData)) {
        if (key === 'media') continue; // Skip media mapping
        const tag = `{{${key}}}`;
        if (result.includes(tag)) {
            const escapedValue = escapeXml(value);
            const lines = escapedValue.split('\n');
            
            // Handle multiline by breaking tags
            result = result.split(tag).map((part, i, arr) => {
                if (i === arr.length - 1) return part;
                const rStart = part.lastIndexOf('<a:r');
                const rPrMatch = part.substring(rStart).match(/<a:rPr[^>]*>[\s\S]*?<\/a:rPr>/);
                const rPr = rPrMatch ? rPrMatch[0] : '';
                const replacement = lines.join(`</a:t></a:r><a:br/><a:r>${rPr}<a:t>`);
                modified = true;
                return part + replacement;
            }).join('');
        }
    }
    return { result, modified };
}

const tmpDir = path.resolve(process.cwd(), `tmp_ppt_final_${Date.now()}`);

try {
    const contentDir = path.join(tmpDir, 'content');
    fs.mkdirSync(contentDir, { recursive: true });
    
    console.log(`Extracting ${templatePath}...`);
    execSync(`tar -xf "${absTemplatePath}" -C "${contentDir}"`);

    // 1. Text Replacement
    const walker = (dir) => {
        const files = fs.readdirSync(dir);
        for (const file of files) {
            const fullPath = path.join(dir, file);
            if (fs.statSync(fullPath).isDirectory()) {
                walker(fullPath);
            } else if (file.endsWith('.xml')) {
                let content = fs.readFileSync(fullPath, 'utf8');
                const { result, modified } = processXml(content, data);
                if (modified) fs.writeFileSync(fullPath, result, 'utf8');
            }
        }
    };
    walker(contentDir);

    // 2. Media Replacement
    if (data.media) {
        console.log('Replacing media files...');
        const mediaDir = path.join(contentDir, 'ppt', 'media');
        if (!fs.existsSync(mediaDir)) fs.mkdirSync(mediaDir, { recursive: true });
        
        for (const [targetName, sourcePath] of Object.entries(data.media)) {
            const absSource = path.resolve(sourcePath);
            const absTarget = path.join(mediaDir, targetName);
            if (fs.existsSync(absSource)) {
                fs.copyFileSync(absSource, absTarget);
                console.log(`  Replaced ${targetName} with ${sourcePath}`);
            }
        }
    }

    // 3. Packaging
    console.log(`Packaging ${outputPath}...`);
    if (fs.existsSync(absOutputPath)) fs.unlinkSync(absOutputPath);
    const tmpZip = path.join(tmpDir, 'output.zip');
    const psCommand = `Add-Type -AssemblyName System.IO.Compression.FileSystem; [System.IO.Compression.ZipFile]::CreateFromDirectory('${contentDir}', '${tmpZip}')`;
    execSync(`powershell -NoProfile -Command "${psCommand}"`);
    fs.renameSync(tmpZip, absOutputPath);

    console.log(`✅ Success: Generated ${outputPath}`);
} catch (err) {
    console.error('❌ Error:', err.message);
    process.exit(1);
} finally {
    if (fs.existsSync(tmpDir)) fs.rmSync(tmpDir, { recursive: true, force: true });
}
