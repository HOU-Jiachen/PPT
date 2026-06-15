import fs from "node:fs/promises";
import path from "node:path";

const source = path.resolve(
  "C:/Gemini cli/gemini-ppt/projects/当阳玉泉水库/exports/玉泉水库水资源论证_完整章节汇报_49页_Office2021.pptx",
);
const output = path.resolve(
  "C:/Gemini cli/gemini-ppt/projects/当阳玉泉水库/exports/玉泉水库水资源论证_完整章节汇报_49页_标准化.pptx",
);

const { FileBlob, PresentationFile } = await import(
  "file:///C:/Users/12054/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/@oai/artifact-tool/dist/artifact_tool.mjs"
);
const presentation = await PresentationFile.importPptx(await FileBlob.load(source));
const pptx = await PresentationFile.exportPptx(presentation);
await fs.mkdir(path.dirname(output), { recursive: true });
await pptx.save(output);
const stat = await fs.stat(output);
console.log(JSON.stringify({ output, bytes: stat.size }, null, 2));
