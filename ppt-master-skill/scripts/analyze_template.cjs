const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const templatePath = path.resolve('templates/模板_tagged.pptx');
const outputDir = path.resolve('projects/当阳玉泉水库/analysis');
const tmpDir = path.resolve('tmp_analyze');

if (!fs.existsSync(outputDir)) fs.mkdirSync(outputDir, { recursive: true });

try {
    if (fs.existsSync(tmpDir)) fs.rmSync(tmpDir, { recursive: true, force: true });
    fs.mkdirSync(tmpDir, { recursive: true });
    execSync(`tar -xf "${templatePath}" -C "${tmpDir}"`);

    const library = {
        template: templatePath,
        slides: []
    };

    const slidesDir = path.join(tmpDir, 'ppt', 'slides');
    const files = fs.readdirSync(slidesDir).filter(f => f.startsWith('slide') && f.endsWith('.xml'));
    files.sort((a, b) => parseInt(a.replace(/\D/g, '')) - parseInt(b.replace(/\D/g, '')));

    files.forEach((file, index) => {
        const slidePath = path.join(slidesDir, file);
        const content = fs.readFileSync(slidePath, 'utf8');
        const slideId = index + 1;
        
        const slideInfo = {
            source_slide: slideId,
            xml_file: file,
            text_summary: "", // Will be filled below
            slots: []
        };

        // Extract tags and their context
        // Healer Pattern to join split tags in memory for analysis
        let healed = content.replace(/<\/a:t><\/a:r><a:r>(?:<a:rPr[^>]*\/>)?<a:t>/g, '');
        healed = healed.replace(/<\/a:t><\/a:r><a:r><a:rPr>([\s\S]*?)<\/a:rPr><a:t>/g, '');

        const tagMatches = healed.match(/\{\{([^{}]+)\}\}/g);
        if (tagMatches) {
            tagMatches.forEach(tag => {
                const tagName = tag.replace(/\{\{|\}\}/g, '');
                // Find shape geometry for capacity estimate
                // This is a rough estimation: looking for the <p:sp> containing the tag
                const spRegex = new RegExp(`<p:sp>[\\s\\S]*?${tag}[\\s\\S]*?<\/p:sp>`, 'g');
                const spMatch = healed.match(spRegex);
                let capacity = "medium";
                if (spMatch) {
                    const extMatch = spMatch[0].match(/<a:ext cx="(\d+)" cy="(\d+)"\/>/);
                    if (extMatch) {
                        const cx = parseInt(extMatch[1]);
                        const cy = parseInt(extMatch[2]);
                        // Convert EMU to something readable (1 cm approx 360,000 EMU)
                        const widthCm = cx / 360000;
                        if (widthCm < 5) capacity = "short";
                        else if (widthCm > 15) capacity = "long";
                    }
                }

                slideInfo.slots.push({
                    tag: tagName,
                    capacity: capacity,
                    role: tagName.includes('Title') ? 'title' : (tagName.includes('Org') ? 'label' : 'body')
                });
            });
        }
        
        // Semantic summary
        const allText = (healed.match(/<a:t>(.*?)<\/a:t>/g) || []).map(m => m.replace(/<\/?a:t>/g, '')).join(' ');
        slideInfo.text_summary = allText.substring(0, 100);

        library.slides.push(slideInfo);
    });

    fs.writeFileSync(path.join(outputDir, 'slide_library.json'), JSON.stringify(library, null, 2));
    console.log('✅ slide_library.json generated successfully.');
} catch (err) {
    console.error('❌ Error during analysis:', err.message);
} finally {
    if (fs.existsSync(tmpDir)) fs.rmSync(tmpDir, { recursive: true, force: true });
}
