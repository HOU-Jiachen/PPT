const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const [,, planPath] = process.argv;

if (!planPath) {
    console.error('Usage: node apply_plan.cjs <fill_plan.json>');
    process.exit(1);
}

const plan = JSON.parse(fs.readFileSync(path.resolve(planPath), 'utf8'));
const templatePath = path.resolve(plan.source_pptx);
const outputPath = path.resolve(plan.output_pptx);
const tmpDir = path.resolve(`tmp_apply_${Date.now()}`);
const contentDir = path.join(tmpDir, 'content');

// Helper to escape XML
function escapeXml(unsafe) {
    return String(unsafe).replace(/[<>&"']/g, function (c) {
        switch (c) {
            case '<': return '&lt;'; case '>': return '&gt;';
            case '&': return '&amp;'; case '"': return '&quot;';
            case "'": return '&apos;';
        }
    });
}

try {
    fs.mkdirSync(contentDir, { recursive: true });
    console.log(`Extracting template: ${templatePath}...`);
    execSync(`tar -xf "${templatePath}" -C "${contentDir}"`);

    // 1. Prepare Slide Registry
    // We need to move existing slides out of the way or keep them as sources
    const slidesSourceDir = path.join(contentDir, 'ppt', 'slides');
    const relsSourceDir = path.join(slidesSourceDir, '_rels');
    
    // Create a backup of original slides to use as blueprints
    const blueprintDir = path.join(tmpDir, 'blueprints');
    fs.mkdirSync(blueprintDir, { recursive: true });
    fs.mkdirSync(path.join(blueprintDir, '_rels'), { recursive: true });
    
    fs.readdirSync(slidesSourceDir).forEach(f => {
        if (f.endsWith('.xml')) fs.copyFileSync(path.join(slidesSourceDir, f), path.join(blueprintDir, f));
    });
    fs.readdirSync(relsSourceDir).forEach(f => {
        if (f.endsWith('.xml.rels')) fs.copyFileSync(path.join(relsSourceDir, f), path.join(blueprintDir, '_rels', f));
    });

    // Clear existing slides from contentDir (we'll rebuild the list)
    fs.readdirSync(slidesSourceDir).forEach(f => {
        const fullPath = path.join(slidesSourceDir, f);
        if (fs.lstatSync(fullPath).isFile()) fs.unlinkSync(fullPath);
    });
    fs.readdirSync(relsSourceDir).forEach(f => {
        fs.unlinkSync(path.join(relsSourceDir, f));
    });

    const newSlideFiles = [];
    const mediaDir = path.join(contentDir, 'ppt', 'media');
    if (!fs.existsSync(mediaDir)) fs.mkdirSync(mediaDir, { recursive: true });

    // 2. Clone and Fill Slides
    plan.slides.forEach((plannedSlide, index) => {
        const targetNum = index + 1;
        const sourceNum = plannedSlide.source_slide;
        const sourceFile = `slide${sourceNum}.xml`;
        const targetFile = `slide${targetNum}.xml`;
        
        console.log(`Creating slide ${targetNum} from blueprint ${sourceNum}...`);
        
        let content = fs.readFileSync(path.join(blueprintDir, sourceFile), 'utf8');
        let rels = fs.readFileSync(path.join(blueprintDir, '_rels', `${sourceFile}.rels`), 'utf8');

        // Heal split tags and perform text replacement
        content = content.replace(/<\/a:t><\/a:r><a:r>(?:<a:rPr[^>]*\/>)?<a:t>/g, '');
        
        plannedSlide.replacements.forEach(rep => {
            const tag = `{{${rep.tag}}}`;
            if (content.includes(tag)) {
                const escapedText = escapeXml(rep.text).replace(/\n/g, '</a:t></a:r><a:br/><a:r><a:t>');
                content = content.split(tag).join(escapedText);
            }
        });

        // Media Replacement
        if (plannedSlide.media) {
            for (const [targetMediaName, sourcePath] of Object.entries(plannedSlide.media)) {
                const absSource = path.resolve(sourcePath);
                if (fs.existsSync(absSource)) {
                    // Copy file to media dir (use a unique name if multiple slides use different images for same target)
                    const uniqueMediaName = `planned_s${targetNum}_${targetMediaName}`;
                    fs.copyFileSync(absSource, path.join(mediaDir, uniqueMediaName));
                    // Update the .rels file for THIS specific slide
                    rels = rels.split(targetMediaName).join(uniqueMediaName);
                }
            }
        }

        fs.writeFileSync(path.join(slidesSourceDir, targetFile), content, 'utf8');
        fs.writeFileSync(path.join(relsSourceDir, `${targetFile}.rels`), rels, 'utf8');
        newSlideFiles.push(targetFile);
    });

    // 3. Update Presentation Structure
    // presentation.xml.rels defines rIds for slides
    let presRelsPath = path.join(contentDir, 'ppt', '_rels', 'presentation.xml.rels');
    let presRels = `<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">`;
    
    // We need to keep non-slide relationships (themes, styles, etc. - actually theme1 is standard)
    // For simplicity, we assume the template's presentation.xml.rels has a set of standard rels we should keep
    // but the slides must be overwritten.
    // Actually, it's safer to just rebuild the slide part of it.
    
    // Let's get the original presentation.xml to extract slide masters and other non-slide rIds
    let presXmlPath = path.join(contentDir, 'ppt', 'presentation.xml');
    let presXml = fs.readFileSync(presXmlPath, 'utf8');

    // Rebuild presentation.xml.rels
    // We need rIds for themes and slide masters. Let's just create new ones for slides starting at 100
    let nextRId = 100;
    const slideMappings = [];
    newSlideFiles.forEach((f, i) => {
        const rid = `rId${nextRId++}`;
        presRels += `<Relationship Id="${rid}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide" Target="slides/${f}"/>`;
        slideMappings.push({ id: (i + 256).toString(), rid: rid }); // id usually starts high
    });
    // Add other standard relationships (this is a shortcut, but template usually has them)
    presRels += `<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideMaster" Target="slideMasters/slideMaster1.xml"/>`;
    presRels += `<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/theme" Target="theme/theme1.xml"/>`;
    presRels += `</Relationships>`;
    fs.writeFileSync(presRelsPath, presRels, 'utf8');

    // Rebuild presentation.xml slide list
    let sldIdLst = `<p:sldIdLst>`;
    slideMappings.forEach(m => {
        sldIdLst += `<p:sldId id="${m.id}" r:id="${m.rid}"/>`;
    });
    sldIdLst += `</p:sldIdLst>`;
    
    presXml = presXml.replace(/<p:sldIdLst>[\s\S]*?<\/p:sldIdLst>/, sldIdLst);
    fs.writeFileSync(presXmlPath, presXml, 'utf8');

    // 4. Update [Content_Types].xml
    let ctPath = path.join(contentDir, '[Content_Types].xml');
    let ct = fs.readFileSync(ctPath, 'utf8');
    // Remove all existing slide overrides
    ct = ct.replace(/<Override PartName="\/ppt\/slides\/slide\d+\.xml"[\s\S]*?\/>/g, '');
    // Add new ones
    let overrides = "";
    newSlideFiles.forEach(f => {
        overrides += `<Override PartName="/ppt/slides/${f}" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slide+xml"/>`;
    });
    ct = ct.replace('</Types>', overrides + '</Types>');
    fs.writeFileSync(ctPath, ct, 'utf8');

    // 5. Package
    console.log(`Packaging to ${outputPath}...`);
    if (fs.existsSync(outputPath)) fs.unlinkSync(outputPath);
    const tmpZip = path.join(tmpDir, 'output.zip');
    const psCommand = `Add-Type -AssemblyName System.IO.Compression.FileSystem; [System.IO.Compression.ZipFile]::CreateFromDirectory('${contentDir}', '${tmpZip}')`;
    execSync(`powershell -NoProfile -Command "${psCommand}"`);
    fs.renameSync(tmpZip, outputPath);

    console.log(`✅ Final PPT generated: ${outputPath}`);
} catch (err) {
    console.error('❌ Error during apply:', err);
} finally {
    if (fs.existsSync(tmpDir)) fs.rmSync(tmpDir, { recursive: true, force: true });
}
