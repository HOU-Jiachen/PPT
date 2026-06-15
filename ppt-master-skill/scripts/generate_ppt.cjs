const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const [,, templatePath, dataPath, outputPath] = process.argv;

if (!templatePath || !dataPath || !outputPath) {
    console.error('Usage: node generate_ppt.cjs <template.pptx> <data.json> <output.pptx>');
    process.exit(1);
}

if (!fs.existsSync(templatePath)) {
    console.error(`Error: Template not found at ${templatePath}`);
    process.exit(1);
}

if (!fs.existsSync(dataPath)) {
    console.error(`Error: Data file not found at ${dataPath}`);
    process.exit(1);
}

const data = JSON.parse(fs.readFileSync(dataPath, 'utf8'));
const tmpDir = path.resolve(process.cwd(), `tmp_ppt_${Date.now()}`);

try {
    // 1. Unzip
    fs.mkdirSync(tmpDir, { recursive: true });
    console.log(`Extracting ${templatePath}...`);
    execSync(`tar -xf "${templatePath}" -C "${tmpDir}"`);

    // 2. Replace in slides and notes
    const searchDirs = [
        path.join(tmpDir, 'ppt', 'slides'),
        path.join(tmpDir, 'ppt', 'notesSlides')
    ];

    searchDirs.forEach(dir => {
        if (fs.existsSync(dir)) {
            const files = fs.readdirSync(dir);
            for (const file of files) {
                if (file.endsWith('.xml')) {
                    const filePath = path.join(dir, file);
                    let content = fs.readFileSync(filePath, 'utf8');
                    
                    let modified = false;
                    for (const [key, value] of Object.entries(data)) {
                        const tag = `{{${key}}}`;
                        if (content.includes(tag)) {
                            content = content.split(tag).join(String(value));
                            modified = true;
                        }
                    }
                    
                    if (modified) {
                        fs.writeFileSync(filePath, content);
                    }
                }
            }
        }
    });

    // 3. Rezip
    console.log(`Packaging ${outputPath}...`);
    const absoluteOutputPath = path.resolve(outputPath);
    
    // On Windows, we use powershell to change directory and zip everything
    // We use tar -a -cf to create a zip (pptx) file.
    // Ensure the output file is deleted first if it exists to avoid merging.
    if (fs.existsSync(absoluteOutputPath)) {
        fs.unlinkSync(absoluteOutputPath);
    }
    
    execSync(`powershell -NoProfile -Command "Set-Location '${tmpDir}'; tar -a -cf '${absoluteOutputPath}' *"`);

    console.log(`✅ Success: Generated ${outputPath}`);
} catch (err) {
    console.error('❌ Error generating PPT:', err.message);
    process.exit(1);
} finally {
    // Clean up
    if (fs.existsSync(tmpDir)) {
        try {
            fs.rmSync(tmpDir, { recursive: true, force: true });
        } catch (e) {
            console.warn(`Warning: Could not clean up temp directory ${tmpDir}`);
        }
    }
}
