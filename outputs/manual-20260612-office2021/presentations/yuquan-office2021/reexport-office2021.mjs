import fs from "node:fs/promises";
import path from "node:path";

const workspace = path.resolve(
  "C:/Gemini cli/gemini-ppt/outputs/manual-20260612-office2021/presentations/yuquan-office2021",
);
const source = path.resolve(
  "C:/Gemini cli/gemini-ppt/projects/当阳玉泉水库/exports/玉泉水库水资源论证_专家审查汇报_20260612.pptx",
);
const output = path.resolve(
  "C:/Gemini cli/gemini-ppt/projects/当阳玉泉水库/exports/玉泉水库水资源论证_专家审查汇报_Office2021兼容版.pptx",
);

await fs.mkdir(workspace, { recursive: true });
const { FileBlob, PresentationFile } = await import(
  "file:///C:/Users/12054/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/@oai/artifact-tool/dist/artifact_tool.mjs"
);
const presentation = await PresentationFile.importPptx(await FileBlob.load(source));

await fs.mkdir(path.dirname(output), { recursive: true });
const pptx = await PresentationFile.exportPptx(presentation);
await pptx.save(output);

const stat = await fs.stat(output);
console.log(JSON.stringify({ output, bytes: stat.size }, null, 2));
