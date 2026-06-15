# PPT

工程汇报 PPT agent 项目。

本仓库以 `hugohe3/ppt-master` 作为核心渲染与导出内核，在本地
`.gemini/skills/engineering-ppt` 增加工程报告专用的证据、章节覆盖、页面规划、
文本适配和发布审计流程。

## 常用命令

```powershell
.\scripts\ppt-agent.cmd doctor
.\scripts\ppt-agent.cmd prepare "项目名称"
.\scripts\ppt-agent.cmd catalog "项目名称" -Source "报告.docx"
.\scripts\ppt-agent.cmd audit "项目名称" -Strict -Pptx "exports\成果.pptx"
```

## 核心原则

- 按报告章节展开，不用结论页替代原文、原表、原图和计算过程。
- 所有数字、表格和图件必须可回溯到源文件。
- 不把 agent 后台提示语放进 PPT 页面。
- 字体、表格和图件以评审可读为第一优先级。
- 每次修改后提交并同步到 GitHub。
