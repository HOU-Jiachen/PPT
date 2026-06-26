# PPT Content Blueprint

This blueprint is the mandatory thinking workspace between report extraction and slide planning.
The agent must read it, refine the narrative, and then derive `evidence_ledger.json`,
`chapter_coverage.md`, and `deck_plan.json` from the selected content units.

## Inventory Summary

- Sections: 85
- Important paragraphs: 297
- Tables: 50
- Figures: 38
- PPT content units: 385

## Thinking Rules

- Preserve the report's title hierarchy before summarizing.
- Treat table and figure captions as the default small-title source.
- Pair source objects with faithful explanation; do not replace technical process with summary cards.
- Split dense tables, long formulas, and complex maps before reducing font size.
- Every planned slide should point back to one or more content unit IDs or explain why no source object exists.

## Content Units By Report Section

### SEC-000 未分章前置内容

- Source locator: 
- Material density: 9段关键文字、4张表
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `未分章前置内容` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0001 未分章前置内容；UNIT-0002 未分章前置内容；UNIT-0003 未分章前置内容；UNIT-0004 未分章前置内容；UNIT-0005 未分章前置内容
  - Best source pairing: left_table_right_text；left_table_right_text or top_text_bottom_table；left_text_right_figure or text_with_keypoints
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0001 | ORIGINAL_TABLE | 未分章前置内容 | source table with explanation | left_table_right_text | ab432f50:T001 |
| UNIT-0002 | ORIGINAL_TABLE | 未分章前置内容 | source table with explanation | left_table_right_text | ab432f50:T002 |
| UNIT-0003 | ORIGINAL_TABLE | 未分章前置内容 | source table with explanation | left_table_right_text or top_text_bottom_table | ab432f50:T004 |
| UNIT-0004 | ORIGINAL_TEXT | 未分章前置内容 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0036 |
| UNIT-0005 | ORIGINAL_TEXT | 未分章前置内容 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0037 |
| UNIT-0006 | ORIGINAL_TEXT | 未分章前置内容 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0044 |
| UNIT-0007 | ORIGINAL_TEXT | 未分章前置内容 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0045 |
| UNIT-0008 | ORIGINAL_TEXT | 未分章前置内容 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0046 |
| UNIT-0009 | ORIGINAL_TEXT | 未分章前置内容 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0047 |
| UNIT-0010 | ORIGINAL_TEXT | 未分章前置内容 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0048 |
| UNIT-0011 | ORIGINAL_TEXT | 未分章前置内容 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0049 |
| UNIT-0012 | ORIGINAL_TEXT | 未分章前置内容 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0050 |
| ... | ... | Additional 1 units in JSON inventory | ... | ... | ... |

### SEC-003 项目基本情况

- Source locator: P0064
- Material density: 3段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `项目基本情况` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0014 项目基本情况；UNIT-0015 项目基本情况；UNIT-0016 项目基本情况
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0014 | ORIGINAL_TEXT | 项目基本情况 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0065 |
| UNIT-0015 | ORIGINAL_TEXT | 项目基本情况 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0066 |
| UNIT-0016 | ORIGINAL_TEXT | 项目基本情况 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0071 |

### SEC-004 项目前期工作概况

- Source locator: P0077
- Material density: 3段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `项目前期工作概况` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0017 项目前期工作概况；UNIT-0018 项目前期工作概况；UNIT-0019 项目前期工作概况
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0017 | ORIGINAL_TEXT | 项目前期工作概况 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0079 |
| UNIT-0018 | ORIGINAL_TEXT | 项目前期工作概况 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0080 |
| UNIT-0019 | ORIGINAL_TEXT | 项目前期工作概况 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0082 |

### SEC-005 自然简况

- Source locator: P0083
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `自然简况` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0020 自然简况
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0020 | ORIGINAL_TEXT | 自然简况 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0085 |

### SEC-007 法律法规

- Source locator: P0089
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `法律法规` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0021 法律法规
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0021 | ORIGINAL_TEXT | 法律法规 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0090 |

### SEC-008 规范性文件

- Source locator: P0096
- Material density: 8段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `规范性文件` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0022 规范性文件；UNIT-0023 规范性文件；UNIT-0024 规范性文件；UNIT-0025 规范性文件；UNIT-0026 规范性文件
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_text_right_table or top_text_bottom_table
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0022 | ORIGINAL_TEXT | 规范性文件 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0099 |
| UNIT-0023 | ORIGINAL_TEXT | 规范性文件 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0100 |
| UNIT-0024 | ORIGINAL_TEXT | 规范性文件 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0101 |
| UNIT-0025 | ORIGINAL_TEXT | 规范性文件 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0102 |
| UNIT-0026 | ORIGINAL_TEXT | 规范性文件 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0103 |
| UNIT-0027 | CALCULATION | 规范性文件 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | ab432f50:P0104 |
| UNIT-0028 | ORIGINAL_TEXT | 规范性文件 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0105 |
| UNIT-0029 | ORIGINAL_TEXT | 规范性文件 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0106 |

### SEC-009 技术规范与标准

- Source locator: P0107
- Material density: 7段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `技术规范与标准` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0030 技术规范与标准；UNIT-0031 技术规范与标准；UNIT-0032 技术规范与标准；UNIT-0033 技术规范与标准；UNIT-0034 技术规范与标准
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_text_right_table or top_text_bottom_table
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0030 | ORIGINAL_TEXT | 技术规范与标准 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0108 |
| UNIT-0031 | ORIGINAL_TEXT | 技术规范与标准 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0109 |
| UNIT-0032 | ORIGINAL_TEXT | 技术规范与标准 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0110 |
| UNIT-0033 | CALCULATION | 技术规范与标准 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | ab432f50:P0111 |
| UNIT-0034 | ORIGINAL_TEXT | 技术规范与标准 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0112 |
| UNIT-0035 | ORIGINAL_TEXT | 技术规范与标准 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0113 |
| UNIT-0036 | ORIGINAL_TEXT | 技术规范与标准 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0114 |

### SEC-010 设计文件及工程技术资料

- Source locator: P0115
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `设计文件及工程技术资料` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0037 设计文件及工程技术资料；UNIT-0038 设计文件及工程技术资料
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_text_right_table or top_text_bottom_table
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0037 | ORIGINAL_TEXT | 设计文件及工程技术资料 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0116 |
| UNIT-0038 | CALCULATION | 设计文件及工程技术资料 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | ab432f50:P0117 |

### SEC-011 设计水平年

- Source locator: P0120
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `设计水平年` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0039 设计水平年
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0039 | ORIGINAL_TEXT | 设计水平年 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0121 |

### SEC-012 水土流失防治责任范围

- Source locator: P0122
- Material density: 1段关键文字、1张表
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `水土流失防治责任范围` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0040 水土流失防治责任范围；UNIT-0041 本项目防治责任范围一览表 单位：m²
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_table_right_text
  - Slide split decision: split or crop tables before reducing font size.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0040 | ORIGINAL_TEXT | 水土流失防治责任范围 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0123 |
| UNIT-0041 | ORIGINAL_TABLE | 本项目防治责任范围一览表 单位：m² | source table with explanation | left_table_right_text | ab432f50:T006, ab432f50:P0125 |

### SEC-014 水土流失防治标准等级

- Source locator: P0127
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `水土流失防治标准等级` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0042 水土流失防治标准等级
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0042 | ORIGINAL_TEXT | 水土流失防治标准等级 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0128 |

### SEC-015 水土流失防治目标

- Source locator: P0129
- Material density: 3段关键文字、1张表
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `水土流失防治目标` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0043 水土流失防治目标；UNIT-0044 水土流失防治目标；UNIT-0045 水土流失防治目标；UNIT-0046 本工程水土流失防治目标值
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_table_right_text
  - Slide split decision: split or crop tables before reducing font size.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0043 | ORIGINAL_TEXT | 水土流失防治目标 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0131 |
| UNIT-0044 | ORIGINAL_TEXT | 水土流失防治目标 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0132 |
| UNIT-0045 | ORIGINAL_TEXT | 水土流失防治目标 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0133 |
| UNIT-0046 | ORIGINAL_TABLE | 本工程水土流失防治目标值 | source table with explanation | left_table_right_text | ab432f50:T007, ab432f50:P0134 |

### SEC-017 主体工程选址评价

- Source locator: P0136
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `主体工程选址评价` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0047 主体工程选址评价；UNIT-0048 主体工程选址评价
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0047 | ORIGINAL_TEXT | 主体工程选址评价 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0137 |
| UNIT-0048 | ORIGINAL_TEXT | 主体工程选址评价 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0138 |

### SEC-018 建设方案与布局评价

- Source locator: P0140
- Material density: 14段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `建设方案与布局评价` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0049 建设方案与布局评价；UNIT-0050 建设方案与布局评价；UNIT-0051 建设方案与布局评价；UNIT-0052 建设方案与布局评价；UNIT-0053 建设方案与布局评价
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_text_right_table or top_text_bottom_table
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0049 | ORIGINAL_TEXT | 建设方案与布局评价 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0141 |
| UNIT-0050 | ORIGINAL_TEXT | 建设方案与布局评价 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0142 |
| UNIT-0051 | ORIGINAL_TEXT | 建设方案与布局评价 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0143 |
| UNIT-0052 | ORIGINAL_TEXT | 建设方案与布局评价 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0144 |
| UNIT-0053 | ORIGINAL_TEXT | 建设方案与布局评价 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0146 |
| UNIT-0054 | ORIGINAL_TEXT | 建设方案与布局评价 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0148 |
| UNIT-0055 | ORIGINAL_TEXT | 建设方案与布局评价 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0149 |
| UNIT-0056 | CALCULATION | 建设方案与布局评价 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | ab432f50:P0150 |
| UNIT-0057 | ORIGINAL_TEXT | 建设方案与布局评价 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0151 |
| UNIT-0058 | ORIGINAL_TEXT | 建设方案与布局评价 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0152 |
| UNIT-0059 | ORIGINAL_TEXT | 建设方案与布局评价 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0154 |
| UNIT-0060 | ORIGINAL_TEXT | 建设方案与布局评价 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0156 |
| ... | ... | Additional 2 units in JSON inventory | ... | ... | ... |

### SEC-019 水土流失预测结果

- Source locator: P0161
- Material density: 3段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `水土流失预测结果` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0063 水土流失预测结果；UNIT-0064 水土流失预测结果；UNIT-0065 水土流失预测结果
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0063 | ORIGINAL_TEXT | 水土流失预测结果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0165 |
| UNIT-0064 | ORIGINAL_TEXT | 水土流失预测结果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0166 |
| UNIT-0065 | ORIGINAL_TEXT | 水土流失预测结果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0167 |

### SEC-020 水土保持措施布设成果

- Source locator: P0168
- Material density: 4段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `水土保持措施布设成果` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0066 水土保持措施布设成果；UNIT-0067 水土保持措施布设成果；UNIT-0068 水土保持措施布设成果；UNIT-0069 水土保持措施布设成果
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0066 | ORIGINAL_TEXT | 水土保持措施布设成果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0171 |
| UNIT-0067 | ORIGINAL_TEXT | 水土保持措施布设成果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0172 |
| UNIT-0068 | ORIGINAL_TEXT | 水土保持措施布设成果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0173 |
| UNIT-0069 | ORIGINAL_TEXT | 水土保持措施布设成果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0175 |

### SEC-021 水土保持投资及效益分析结果

- Source locator: P0179
- Material density: 5段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `水土保持投资及效益分析结果` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0070 水土保持投资及效益分析结果；UNIT-0071 水土保持投资及效益分析结果；UNIT-0072 水土保持投资及效益分析结果；UNIT-0073 水土保持投资及效益分析结果；UNIT-0074 水土保持投资及效益分析结果
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0070 | ORIGINAL_TEXT | 水土保持投资及效益分析结果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0180 |
| UNIT-0071 | ORIGINAL_TEXT | 水土保持投资及效益分析结果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0181 |
| UNIT-0072 | ORIGINAL_TEXT | 水土保持投资及效益分析结果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0182 |
| UNIT-0073 | ORIGINAL_TEXT | 水土保持投资及效益分析结果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0183 |
| UNIT-0074 | ORIGINAL_TEXT | 水土保持投资及效益分析结果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0184 |

### SEC-022 结论与建议

- Source locator: P0185
- Material density: 3段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `结论与建议` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0075 结论与建议；UNIT-0076 结论与建议；UNIT-0077 结论与建议
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0075 | ORIGINAL_TEXT | 结论与建议 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0186 |
| UNIT-0076 | ORIGINAL_TEXT | 结论与建议 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0187 |
| UNIT-0077 | ORIGINAL_TEXT | 结论与建议 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0188 |

### SEC-025 项目基本情况

- Source locator: P0195
- Material density: 2段关键文字、1张表
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `项目基本情况` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0078 项目基本情况；UNIT-0079 项目基本情况；UNIT-0080 建设项目工程特性表
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_table_right_text or top_text_bottom_table
  - Slide split decision: split or crop tables before reducing font size.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0078 | ORIGINAL_TEXT | 项目基本情况 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0200 |
| UNIT-0079 | ORIGINAL_TEXT | 项目基本情况 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0206 |
| UNIT-0080 | ORIGINAL_TABLE | 建设项目工程特性表 | source table with explanation | left_table_right_text or top_text_bottom_table | ab432f50:T008, ab432f50:P0207 |

### SEC-026 项目地理位置

- Source locator: P0210
- Material density: 1张表
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `项目地理位置` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0081 项目地理位置
  - Best source pairing: left_table_right_text
  - Slide split decision: split or crop tables before reducing font size.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0081 | ORIGINAL_TABLE | 项目地理位置 | source table with explanation | left_table_right_text | ab432f50:T009 |

### SEC-027 项目组成及工程布置

- Source locator: P0212
- Material density: 7段关键文字、3张表
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `项目组成及工程布置` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0082 项目组成及工程布置；UNIT-0083 项目组成及工程布置；UNIT-0084 项目组成及工程布置；UNIT-0085 项目组成及工程布置；UNIT-0086 项目组成及工程布置
  - Best source pairing: left_text_right_table or top_text_bottom_table；left_text_right_figure or text_with_keypoints；left_table_right_text
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0082 | CALCULATION | 项目组成及工程布置 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | ab432f50:P0213 |
| UNIT-0083 | ORIGINAL_TEXT | 项目组成及工程布置 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0216 |
| UNIT-0084 | ORIGINAL_TEXT | 项目组成及工程布置 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0217 |
| UNIT-0085 | ORIGINAL_TEXT | 项目组成及工程布置 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0218 |
| UNIT-0086 | ORIGINAL_TEXT | 项目组成及工程布置 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0220 |
| UNIT-0087 | ORIGINAL_TABLE | 项目组成及工程布置 | source table with explanation | left_table_right_text | ab432f50:T010 |
| UNIT-0088 | ORIGINAL_TEXT | 项目组成及工程布置 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0223 |
| UNIT-0089 | ORIGINAL_TABLE | 项目组成及工程布置 | source table with explanation | left_table_right_text | ab432f50:T011 |
| UNIT-0090 | ORIGINAL_TEXT | 项目组成及工程布置 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0225 |
| UNIT-0091 | ORIGINAL_TABLE | 检查井、沉泥井坐标表 | source table with explanation | left_table_right_text or top_text_bottom_table | ab432f50:T012, ab432f50:P0227 |

### SEC-029 施工组织

- Source locator: P0229
- Material density: 6段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `施工组织` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0092 施工组织；UNIT-0093 施工组织；UNIT-0094 施工组织；UNIT-0095 施工组织；UNIT-0096 施工组织
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0092 | ORIGINAL_TEXT | 施工组织 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0230 |
| UNIT-0093 | ORIGINAL_TEXT | 施工组织 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0231 |
| UNIT-0094 | ORIGINAL_TEXT | 施工组织 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0234 |
| UNIT-0095 | ORIGINAL_TEXT | 施工组织 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0236 |
| UNIT-0096 | ORIGINAL_TEXT | 施工组织 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0238 |
| UNIT-0097 | ORIGINAL_TEXT | 施工组织 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0240 |

### SEC-030 施工工艺

- Source locator: P0244
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `施工工艺` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0098 施工工艺；UNIT-0099 施工工艺
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0098 | ORIGINAL_TEXT | 施工工艺 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0247 |
| UNIT-0099 | ORIGINAL_TEXT | 施工工艺 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0248 |

### SEC-031 工程占地

- Source locator: P0250
- Material density: 1段关键文字、1张表
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `工程占地` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0100 工程占地；UNIT-0101 工程占地情况一览表 单位：m²
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_table_right_text
  - Slide split decision: split or crop tables before reducing font size.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0100 | ORIGINAL_TEXT | 工程占地 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0251 |
| UNIT-0101 | ORIGINAL_TABLE | 工程占地情况一览表 单位：m² | source table with explanation | left_table_right_text | ab432f50:T013, ab432f50:P0252 |

### SEC-033 表土剥离和利用分析

- Source locator: P0254
- Material density: 1张表
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `表土剥离和利用分析` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0102 表土剥离和利用分析
  - Best source pairing: left_table_right_text or top_text_bottom_table
  - Slide split decision: split or crop tables before reducing font size.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0102 | ORIGINAL_TABLE | 表土剥离和利用分析 | source table with explanation | left_table_right_text or top_text_bottom_table | ab432f50:T014 |

### SEC-034 土石方平衡分析

- Source locator: P0257
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `土石方平衡分析` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0103 土石方平衡分析
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0103 | ORIGINAL_TEXT | 土石方平衡分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0258 |

### SEC-035 土石方平衡汇总

- Source locator: P0261
- Material density: 1段关键文字、2张表
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `土石方平衡汇总` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0104 土石方平衡汇总；UNIT-0105 工程土石方平衡表 单位：m³；UNIT-0106 土石方平衡汇总
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_table_right_text or top_text_bottom_table；left_table_right_text
  - Slide split decision: split or crop tables before reducing font size.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0104 | ORIGINAL_TEXT | 土石方平衡汇总 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0262 |
| UNIT-0105 | ORIGINAL_TABLE | 工程土石方平衡表 单位：m³ | source table with explanation | left_table_right_text or top_text_bottom_table | ab432f50:T015, ab432f50:P0264 |
| UNIT-0106 | ORIGINAL_TABLE | 土石方平衡汇总 | source table with explanation | left_table_right_text | ab432f50:T016 |

### SEC-037 施工进度安排

- Source locator: P0271
- Material density: 1段关键文字、1张表
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `施工进度安排` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0107 施工进度安排；UNIT-0108 施工进度安排表
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_table_right_text or top_text_bottom_table
  - Slide split decision: split or crop tables before reducing font size.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0107 | ORIGINAL_TEXT | 施工进度安排 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0278 |
| UNIT-0108 | ORIGINAL_TABLE | 施工进度安排表 | source table with explanation | left_table_right_text or top_text_bottom_table | ab432f50:T017, ab432f50:P0279 |

### SEC-039 地形地貌

- Source locator: P0281
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `地形地貌` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0109 地形地貌
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0109 | ORIGINAL_TEXT | 地形地貌 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0283 |

### SEC-040 水文地质

- Source locator: P0284
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `水文地质` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0110 水文地质；UNIT-0111 水文地质
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0110 | ORIGINAL_TEXT | 水文地质 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0296 |
| UNIT-0111 | ORIGINAL_TEXT | 水文地质 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0297 |

### SEC-042 气象

- Source locator: P0300
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `气象` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0112 气象
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0112 | ORIGINAL_TEXT | 气象 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0302 |

### SEC-043 水文

- Source locator: P0303
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `水文` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0113 水文
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0113 | ORIGINAL_TEXT | 水文 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0306 |

### SEC-046 水土保持敏感区

- Source locator: P0311
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `水土保持敏感区` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0114 水土保持敏感区
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0114 | ORIGINAL_TEXT | 水土保持敏感区 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0313 |

### SEC-048 项目主体工程选址（线）水土保持评价

- Source locator: P0315
- Material density: 3段关键文字、3张表
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `项目主体工程选址（线）水土保持评价` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0115 项目主体工程选址（线）水土保持评价；UNIT-0116 项目主体工程选址（线）水土保持评价；UNIT-0117 水土保持法制约因素分析与评价结果一览表；UNIT-0118 项目主体工程选址（线）水土保持评价；UNIT-0119 GB50433-2018水土保持制约性因素分析与评价
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_table_right_text
  - Slide split decision: split or crop tables before reducing font size.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0115 | ORIGINAL_TEXT | 项目主体工程选址（线）水土保持评价 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0316 |
| UNIT-0116 | ORIGINAL_TEXT | 项目主体工程选址（线）水土保持评价 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0318 |
| UNIT-0117 | ORIGINAL_TABLE | 水土保持法制约因素分析与评价结果一览表 | source table with explanation | left_table_right_text | ab432f50:T018, ab432f50:P0319 |
| UNIT-0118 | ORIGINAL_TEXT | 项目主体工程选址（线）水土保持评价 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0321 |
| UNIT-0119 | ORIGINAL_TABLE | GB50433-2018水土保持制约性因素分析与评价 | source table with explanation | left_table_right_text | ab432f50:T019, ab432f50:P0322 |
| UNIT-0120 | ORIGINAL_TABLE | 《中华人民共和国长江保护法》水土保持制约性因素分析评价 | source table with explanation | left_table_right_text | ab432f50:T020, ab432f50:P0325 |

### SEC-049 项目建设方案与布局水土保持评价

- Source locator: P0326
- Material density: 7段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `项目建设方案与布局水土保持评价` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0121 项目建设方案与布局水土保持评价；UNIT-0122 项目建设方案与布局水土保持评价；UNIT-0123 项目建设方案与布局水土保持评价；UNIT-0124 项目建设方案与布局水土保持评价；UNIT-0125 项目建设方案与布局水土保持评价
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_text_right_table or top_text_bottom_table
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0121 | ORIGINAL_TEXT | 项目建设方案与布局水土保持评价 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0328 |
| UNIT-0122 | ORIGINAL_TEXT | 项目建设方案与布局水土保持评价 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0329 |
| UNIT-0123 | ORIGINAL_TEXT | 项目建设方案与布局水土保持评价 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0330 |
| UNIT-0124 | ORIGINAL_TEXT | 项目建设方案与布局水土保持评价 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0334 |
| UNIT-0125 | CALCULATION | 项目建设方案与布局水土保持评价 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | ab432f50:P0336 |
| UNIT-0126 | ORIGINAL_TEXT | 项目建设方案与布局水土保持评价 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0337 |
| UNIT-0127 | ORIGINAL_TEXT | 项目建设方案与布局水土保持评价 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0338 |

### SEC-050 施工组织评价

- Source locator: P0344
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `施工组织评价` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0128 施工组织评价；UNIT-0129 施工组织评价
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0128 | ORIGINAL_TEXT | 施工组织评价 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0345 |
| UNIT-0129 | ORIGINAL_TEXT | 施工组织评价 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0346 |

### SEC-051 施工工艺、方法

- Source locator: P0347
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `施工工艺、方法` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0130 施工工艺、方法
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0130 | ORIGINAL_TEXT | 施工工艺、方法 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0348 |

### SEC-052 管网工程区

- Source locator: P0350
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `管网工程区` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0131 管网工程区；UNIT-0132 管网工程区
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0131 | ORIGINAL_TEXT | 管网工程区 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0351 |
| UNIT-0132 | ORIGINAL_TEXT | 管网工程区 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0354 |

### SEC-053 主体工程设计中水土保持措施界定

- Source locator: P0355
- Material density: 11段关键文字、1张表
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `主体工程设计中水土保持措施界定` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0133 主体工程设计中水土保持措施界定；UNIT-0134 主体工程设计中水土保持措施界定；UNIT-0135 主体工程设计中水土保持措施界定；UNIT-0136 主体工程设计中水土保持措施界定；UNIT-0137 主体工程设计中水土保持措施界定
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_table_right_text or top_text_bottom_table
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0133 | ORIGINAL_TEXT | 主体工程设计中水土保持措施界定 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0357 |
| UNIT-0134 | ORIGINAL_TEXT | 主体工程设计中水土保持措施界定 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0358 |
| UNIT-0135 | ORIGINAL_TEXT | 主体工程设计中水土保持措施界定 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0359 |
| UNIT-0136 | ORIGINAL_TEXT | 主体工程设计中水土保持措施界定 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0360 |
| UNIT-0137 | ORIGINAL_TEXT | 主体工程设计中水土保持措施界定 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0361 |
| UNIT-0138 | ORIGINAL_TEXT | 主体工程设计中水土保持措施界定 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0362 |
| UNIT-0139 | ORIGINAL_TEXT | 主体工程设计中水土保持措施界定 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0367 |
| UNIT-0140 | ORIGINAL_TABLE | 本项目主体工程设计中应纳入水土保持的措施量及投资一览表 | source table with explanation | left_table_right_text or top_text_bottom_table | ab432f50:T021, ab432f50:P0369 |
| UNIT-0141 | ORIGINAL_TEXT | 主体工程设计中水土保持措施界定 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0370 |
| UNIT-0142 | ORIGINAL_TEXT | 主体工程设计中水土保持措施界定 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0371 |
| UNIT-0143 | ORIGINAL_TEXT | 主体工程设计中水土保持措施界定 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0373 |
| UNIT-0144 | ORIGINAL_TEXT | 主体工程设计中水土保持措施界定 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0374 |

### SEC-055 4.1水土流失现状

- Source locator: P0376
- Material density: 1段关键文字、1张表
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `4.1水土流失现状` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0145 黄州区水土流失面积及等级分布情况表；UNIT-0146 4.1水土流失现状
  - Best source pairing: left_table_right_text or top_text_bottom_table；left_text_right_figure or text_with_keypoints
  - Slide split decision: split or crop tables before reducing font size.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0145 | ORIGINAL_TABLE | 黄州区水土流失面积及等级分布情况表 | source table with explanation | left_table_right_text or top_text_bottom_table | ab432f50:T022, ab432f50:P0379 |
| UNIT-0146 | ORIGINAL_TEXT | 4.1水土流失现状 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0381 |

### SEC-056 4.2水土流失影响因素分析

- Source locator: P0384
- Material density: 2段关键文字、2张表
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `4.2水土流失影响因素分析` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0147 4.2水土流失影响因素分析；UNIT-0148 扰动地表面积表 单位：m²；UNIT-0149 4.2水土流失影响因素分析；UNIT-0150 植被损毁面积表 单位：m²
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_table_right_text
  - Slide split decision: split or crop tables before reducing font size.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0147 | ORIGINAL_TEXT | 4.2水土流失影响因素分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0391 |
| UNIT-0148 | ORIGINAL_TABLE | 扰动地表面积表 单位：m² | source table with explanation | left_table_right_text | ab432f50:T023, ab432f50:P0392 |
| UNIT-0149 | ORIGINAL_TEXT | 4.2水土流失影响因素分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0394 |
| UNIT-0150 | ORIGINAL_TABLE | 植被损毁面积表 单位：m² | source table with explanation | left_table_right_text | ab432f50:T024, ab432f50:P0395 |

### SEC-057 4.3土壤流失量预测

- Source locator: P0398
- Material density: 5段关键文字、2张表
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `4.3土壤流失量预测` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0151 4.3土壤流失量预测；UNIT-0152 4.3土壤流失量预测；UNIT-0153 本项目水土流失调查及预测单元划分表；UNIT-0154 4.3土壤流失量预测；UNIT-0155 4.3土壤流失量预测
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_table_right_text；left_text_right_table or top_text_bottom_table
  - Slide split decision: split or crop tables before reducing font size.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0151 | ORIGINAL_TEXT | 4.3土壤流失量预测 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0399 |
| UNIT-0152 | ORIGINAL_TEXT | 4.3土壤流失量预测 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0400 |
| UNIT-0153 | ORIGINAL_TABLE | 本项目水土流失调查及预测单元划分表 | source table with explanation | left_table_right_text | ab432f50:T025, ab432f50:P0401 |
| UNIT-0154 | ORIGINAL_TEXT | 4.3土壤流失量预测 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0402 |
| UNIT-0155 | ORIGINAL_TEXT | 4.3土壤流失量预测 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0404 |
| UNIT-0156 | CALCULATION | 4.3土壤流失量预测 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | ab432f50:P0405 |
| UNIT-0157 | ORIGINAL_TABLE | 水土流失预测范围与预测时段划分表 | source table with explanation | left_table_right_text | ab432f50:T026, ab432f50:P0407 |

### SEC-058 4.3.3.1 原地貌土壤侵蚀模数

- Source locator: P0409
- Material density: 2段关键文字、2张表
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `4.3.3.1 原地貌土壤侵蚀模数` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0158 4.3.3.1 原地貌土壤侵蚀模数；UNIT-0159 本项目区各地类土壤侵蚀模数取值表；UNIT-0160 4.3.3.1 原地貌土壤侵蚀模数；UNIT-0161 本项目区土壤侵蚀模数背景值计算表
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_table_right_text；left_text_right_table or top_text_bottom_table
  - Slide split decision: split or crop tables before reducing font size.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0158 | ORIGINAL_TEXT | 4.3.3.1 原地貌土壤侵蚀模数 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0411 |
| UNIT-0159 | ORIGINAL_TABLE | 本项目区各地类土壤侵蚀模数取值表 | source table with explanation | left_table_right_text | ab432f50:T027, ab432f50:P0412 |
| UNIT-0160 | CALCULATION | 4.3.3.1 原地貌土壤侵蚀模数 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | ab432f50:P0419 |
| UNIT-0161 | ORIGINAL_TABLE | 本项目区土壤侵蚀模数背景值计算表 | source table with explanation | left_table_right_text or top_text_bottom_table | ab432f50:T028, ab432f50:P0420 |

### SEC-059 4.3.3.2 扰动后土壤侵蚀模数

- Source locator: P0421
- Material density: 19段关键文字、3张表
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `4.3.3.2 扰动后土壤侵蚀模数` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0162 4.3.3.2 扰动后土壤侵蚀模数；UNIT-0163 土壤流失类型划分表；UNIT-0164 4.3.3.2 扰动后土壤侵蚀模数；UNIT-0165 4.3.3.2 扰动后土壤侵蚀模数；UNIT-0166 4.3.3.2 扰动后土壤侵蚀模数
  - Best source pairing: left_text_right_table or top_text_bottom_table；left_table_right_text；left_text_right_figure or text_with_keypoints
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0162 | CALCULATION | 4.3.3.2 扰动后土壤侵蚀模数 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | ab432f50:P0423 |
| UNIT-0163 | ORIGINAL_TABLE | 土壤流失类型划分表 | source table with explanation | left_table_right_text | ab432f50:T029, ab432f50:P0424 |
| UNIT-0164 | CALCULATION | 4.3.3.2 扰动后土壤侵蚀模数 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | ab432f50:P0426 |
| UNIT-0165 | CALCULATION | 4.3.3.2 扰动后土壤侵蚀模数 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | ab432f50:P0427 |
| UNIT-0166 | ORIGINAL_TEXT | 4.3.3.2 扰动后土壤侵蚀模数 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0428 |
| UNIT-0167 | CALCULATION | 4.3.3.2 扰动后土壤侵蚀模数 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | ab432f50:P0437 |
| UNIT-0168 | ORIGINAL_TEXT | 4.3.3.2 扰动后土壤侵蚀模数 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0441 |
| UNIT-0169 | ORIGINAL_TEXT | 4.3.3.2 扰动后土壤侵蚀模数 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0442 |
| UNIT-0170 | ORIGINAL_TEXT | 4.3.3.2 扰动后土壤侵蚀模数 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0443 |
| UNIT-0171 | CALCULATION | 4.3.3.2 扰动后土壤侵蚀模数 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | ab432f50:P0444 |
| UNIT-0172 | CALCULATION | 4.3.3.2 扰动后土壤侵蚀模数 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | ab432f50:P0447 |
| UNIT-0173 | ORIGINAL_TEXT | 4.3.3.2 扰动后土壤侵蚀模数 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0448 |
| ... | ... | Additional 10 units in JSON inventory | ... | ... | ... |

### SEC-060 4.3.3.3 自然恢复期土壤侵蚀模数

- Source locator: P0472
- Material density: 3段关键文字、2张表
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `4.3.3.3 自然恢复期土壤侵蚀模数` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0184 4.3.3.3 自然恢复期土壤侵蚀模数；UNIT-0185 管网工程区自然恢复期土壤侵蚀模数计算表；UNIT-0186 4.3.3.3 自然恢复期土壤侵蚀模数；UNIT-0187 本项目施工期和自然恢复期土壤侵蚀模数表；UNIT-0188 4.3.3.3 自然恢复期土壤侵蚀模数
  - Best source pairing: left_text_right_table or top_text_bottom_table；left_table_right_text；left_text_right_figure or text_with_keypoints
  - Slide split decision: split or crop tables before reducing font size.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0184 | CALCULATION | 4.3.3.3 自然恢复期土壤侵蚀模数 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | ab432f50:P0473 |
| UNIT-0185 | ORIGINAL_TABLE | 管网工程区自然恢复期土壤侵蚀模数计算表 | source table with explanation | left_table_right_text | ab432f50:T032, ab432f50:P0474 |
| UNIT-0186 | ORIGINAL_TEXT | 4.3.3.3 自然恢复期土壤侵蚀模数 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0475 |
| UNIT-0187 | ORIGINAL_TABLE | 本项目施工期和自然恢复期土壤侵蚀模数表 | source table with explanation | left_table_right_text | ab432f50:T033, ab432f50:P0476 |
| UNIT-0188 | ORIGINAL_TEXT | 4.3.3.3 自然恢复期土壤侵蚀模数 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0478 |

### SEC-061 4.3.4.1 预测方法

- Source locator: P0479
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `4.3.4.1 预测方法` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0189 4.3.4.1 预测方法；UNIT-0190 4.3.4.1 预测方法
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0189 | ORIGINAL_TEXT | 4.3.4.1 预测方法 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0490 |
| UNIT-0190 | ORIGINAL_TEXT | 4.3.4.1 预测方法 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0491 |

### SEC-062 4.3.4.2 预测结果

- Source locator: P0492
- Material density: 1段关键文字、1张表
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `4.3.4.2 预测结果` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0191 4.3.4.2 预测结果；UNIT-0192 工程建设可能造成的土壤流失量预测结果
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_table_right_text or top_text_bottom_table
  - Slide split decision: split or crop tables before reducing font size.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0191 | ORIGINAL_TEXT | 4.3.4.2 预测结果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0494 |
| UNIT-0192 | ORIGINAL_TABLE | 工程建设可能造成的土壤流失量预测结果 | source table with explanation | left_table_right_text or top_text_bottom_table | ab432f50:T034, ab432f50:P0496 |

### SEC-063 4.4项目水土流失危害分析

- Source locator: P0499
- Material density: 3段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `4.4项目水土流失危害分析` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0193 4.4项目水土流失危害分析；UNIT-0194 4.4项目水土流失危害分析；UNIT-0195 4.4项目水土流失危害分析
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0193 | ORIGINAL_TEXT | 4.4项目水土流失危害分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0501 |
| UNIT-0194 | ORIGINAL_TEXT | 4.4项目水土流失危害分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0502 |
| UNIT-0195 | ORIGINAL_TEXT | 4.4项目水土流失危害分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0503 |

### SEC-064 4.5指导性意见

- Source locator: P0504
- Material density: 4段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `4.5指导性意见` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0196 4.5指导性意见；UNIT-0197 4.5指导性意见；UNIT-0198 4.5指导性意见；UNIT-0199 4.5指导性意见
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0196 | ORIGINAL_TEXT | 4.5指导性意见 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0506 |
| UNIT-0197 | ORIGINAL_TEXT | 4.5指导性意见 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0507 |
| UNIT-0198 | ORIGINAL_TEXT | 4.5指导性意见 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0508 |
| UNIT-0199 | ORIGINAL_TEXT | 4.5指导性意见 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0509 |

### SEC-066 水土流失防治区划分

- Source locator: P0513
- Material density: 8段关键文字、1张表
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `水土流失防治区划分` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0200 水土流失防治区划分；UNIT-0201 水土流失防治区划分；UNIT-0202 水土流失防治区划分；UNIT-0203 水土流失防治区划分；UNIT-0204 水土流失防治区划分
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_table_right_text
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0200 | ORIGINAL_TEXT | 水土流失防治区划分 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0515 |
| UNIT-0201 | ORIGINAL_TEXT | 水土流失防治区划分 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0516 |
| UNIT-0202 | ORIGINAL_TEXT | 水土流失防治区划分 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0517 |
| UNIT-0203 | ORIGINAL_TEXT | 水土流失防治区划分 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0518 |
| UNIT-0204 | ORIGINAL_TEXT | 水土流失防治区划分 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0519 |
| UNIT-0205 | ORIGINAL_TEXT | 水土流失防治区划分 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0520 |
| UNIT-0206 | ORIGINAL_TEXT | 水土流失防治区划分 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0521 |
| UNIT-0207 | ORIGINAL_TEXT | 水土流失防治区划分 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0522 |
| UNIT-0208 | ORIGINAL_TABLE | 水土流失防治区划分表 | source table with explanation | left_table_right_text | ab432f50:T035, ab432f50:P0523 |

### SEC-067 措施总体布局

- Source locator: P0524
- Material density: 19段关键文字、1张表
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `措施总体布局` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0209 措施总体布局；UNIT-0210 措施总体布局；UNIT-0211 措施总体布局；UNIT-0212 措施总体布局；UNIT-0213 措施总体布局
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_table_right_text or top_text_bottom_table
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0209 | ORIGINAL_TEXT | 措施总体布局 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0526 |
| UNIT-0210 | ORIGINAL_TEXT | 措施总体布局 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0527 |
| UNIT-0211 | ORIGINAL_TEXT | 措施总体布局 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0528 |
| UNIT-0212 | ORIGINAL_TEXT | 措施总体布局 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0529 |
| UNIT-0213 | ORIGINAL_TEXT | 措施总体布局 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0530 |
| UNIT-0214 | ORIGINAL_TEXT | 措施总体布局 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0531 |
| UNIT-0215 | ORIGINAL_TEXT | 措施总体布局 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0532 |
| UNIT-0216 | ORIGINAL_TEXT | 措施总体布局 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0533 |
| UNIT-0217 | ORIGINAL_TEXT | 措施总体布局 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0535 |
| UNIT-0218 | ORIGINAL_TEXT | 措施总体布局 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0536 |
| UNIT-0219 | ORIGINAL_TEXT | 措施总体布局 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0537 |
| UNIT-0220 | ORIGINAL_TEXT | 措施总体布局 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0538 |
| ... | ... | Additional 8 units in JSON inventory | ... | ... | ... |

### SEC-068 分区布设

- Source locator: P0554
- Material density: 12段关键文字、1张表
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `分区布设` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0229 分区布设；UNIT-0230 分区布设；UNIT-0231 分区布设；UNIT-0232 分区布设；UNIT-0233 分区布设
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_table_right_text
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0229 | ORIGINAL_TEXT | 分区布设 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0556 |
| UNIT-0230 | ORIGINAL_TEXT | 分区布设 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0557 |
| UNIT-0231 | ORIGINAL_TEXT | 分区布设 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0558 |
| UNIT-0232 | ORIGINAL_TEXT | 分区布设 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0559 |
| UNIT-0233 | ORIGINAL_TEXT | 分区布设 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0560 |
| UNIT-0234 | ORIGINAL_TEXT | 分区布设 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0563 |
| UNIT-0235 | ORIGINAL_TEXT | 分区布设 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0564 |
| UNIT-0236 | ORIGINAL_TEXT | 分区布设 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0565 |
| UNIT-0237 | ORIGINAL_TEXT | 分区布设 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0567 |
| UNIT-0238 | ORIGINAL_TEXT | 分区布设 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0569 |
| UNIT-0239 | ORIGINAL_TEXT | 分区布设 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0570 |
| UNIT-0240 | ORIGINAL_TEXT | 分区布设 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0572 |
| ... | ... | Additional 1 units in JSON inventory | ... | ... | ... |

### SEC-069 施工要求

- Source locator: P0574
- Material density: 12段关键文字、1张表
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `施工要求` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0242 施工要求；UNIT-0243 施工要求；UNIT-0244 施工要求；UNIT-0245 施工要求；UNIT-0246 施工要求
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_table_right_text or top_text_bottom_table
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0242 | ORIGINAL_TEXT | 施工要求 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0576 |
| UNIT-0243 | ORIGINAL_TEXT | 施工要求 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0577 |
| UNIT-0244 | ORIGINAL_TEXT | 施工要求 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0578 |
| UNIT-0245 | ORIGINAL_TEXT | 施工要求 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0579 |
| UNIT-0246 | ORIGINAL_TEXT | 施工要求 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0581 |
| UNIT-0247 | ORIGINAL_TEXT | 施工要求 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0583 |
| UNIT-0248 | ORIGINAL_TEXT | 施工要求 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0584 |
| UNIT-0249 | ORIGINAL_TEXT | 施工要求 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0585 |
| UNIT-0250 | ORIGINAL_TEXT | 施工要求 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0594 |
| UNIT-0251 | ORIGINAL_TEXT | 施工要求 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0598 |
| UNIT-0252 | ORIGINAL_TEXT | 施工要求 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0599 |
| UNIT-0253 | ORIGINAL_TEXT | 施工要求 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0600 |
| ... | ... | Additional 1 units in JSON inventory | ... | ... | ... |

### SEC-072 6.1.1.1编制原则

- Source locator: P0608
- Material density: 6段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `6.1.1.1编制原则` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0255 6.1.1.1编制原则；UNIT-0256 6.1.1.1编制原则；UNIT-0257 6.1.1.1编制原则；UNIT-0258 6.1.1.1编制原则；UNIT-0259 6.1.1.1编制原则
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0255 | ORIGINAL_TEXT | 6.1.1.1编制原则 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0609 |
| UNIT-0256 | ORIGINAL_TEXT | 6.1.1.1编制原则 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0610 |
| UNIT-0257 | ORIGINAL_TEXT | 6.1.1.1编制原则 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0611 |
| UNIT-0258 | ORIGINAL_TEXT | 6.1.1.1编制原则 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0612 |
| UNIT-0259 | ORIGINAL_TEXT | 6.1.1.1编制原则 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0613 |
| UNIT-0260 | ORIGINAL_TEXT | 6.1.1.1编制原则 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0614 |

### SEC-073 6.1.1.2编制依据

- Source locator: P0615
- Material density: 10段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `6.1.1.2编制依据` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0261 6.1.1.2编制依据；UNIT-0262 6.1.1.2编制依据；UNIT-0263 6.1.1.2编制依据；UNIT-0264 6.1.1.2编制依据；UNIT-0265 6.1.1.2编制依据
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0261 | ORIGINAL_TEXT | 6.1.1.2编制依据 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0616 |
| UNIT-0262 | ORIGINAL_TEXT | 6.1.1.2编制依据 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0617 |
| UNIT-0263 | ORIGINAL_TEXT | 6.1.1.2编制依据 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0618 |
| UNIT-0264 | ORIGINAL_TEXT | 6.1.1.2编制依据 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0619 |
| UNIT-0265 | ORIGINAL_TEXT | 6.1.1.2编制依据 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0620 |
| UNIT-0266 | ORIGINAL_TEXT | 6.1.1.2编制依据 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0621 |
| UNIT-0267 | ORIGINAL_TEXT | 6.1.1.2编制依据 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0622 |
| UNIT-0268 | ORIGINAL_TEXT | 6.1.1.2编制依据 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0623 |
| UNIT-0269 | ORIGINAL_TEXT | 6.1.1.2编制依据 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0624 |
| UNIT-0270 | ORIGINAL_TEXT | 6.1.1.2编制依据 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0625 |

### SEC-074 6.1.2.1编制方法

- Source locator: P0627
- Material density: 10段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `6.1.2.1编制方法` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0271 6.1.2.1编制方法；UNIT-0272 6.1.2.1编制方法；UNIT-0273 6.1.2.1编制方法；UNIT-0274 6.1.2.1编制方法；UNIT-0275 6.1.2.1编制方法
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_text_right_table or top_text_bottom_table
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0271 | ORIGINAL_TEXT | 6.1.2.1编制方法 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0628 |
| UNIT-0272 | CALCULATION | 6.1.2.1编制方法 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | ab432f50:P0630 |
| UNIT-0273 | ORIGINAL_TEXT | 6.1.2.1编制方法 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0631 |
| UNIT-0274 | ORIGINAL_TEXT | 6.1.2.1编制方法 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0633 |
| UNIT-0275 | ORIGINAL_TEXT | 6.1.2.1编制方法 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0636 |
| UNIT-0276 | ORIGINAL_TEXT | 6.1.2.1编制方法 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0641 |
| UNIT-0277 | ORIGINAL_TEXT | 6.1.2.1编制方法 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0643 |
| UNIT-0278 | ORIGINAL_TEXT | 6.1.2.1编制方法 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0645 |
| UNIT-0279 | CALCULATION | 6.1.2.1编制方法 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | ab432f50:P0646 |
| UNIT-0280 | ORIGINAL_TEXT | 6.1.2.1编制方法 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0647 |

### SEC-075 6.1.2.2基础单价

- Source locator: P0648
- Material density: 6段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `6.1.2.2基础单价` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0281 6.1.2.2基础单价；UNIT-0282 6.1.2.2基础单价；UNIT-0283 6.1.2.2基础单价；UNIT-0284 6.1.2.2基础单价；UNIT-0285 6.1.2.2基础单价
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_text_right_table or top_text_bottom_table
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0281 | ORIGINAL_TEXT | 6.1.2.2基础单价 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0649 |
| UNIT-0282 | ORIGINAL_TEXT | 6.1.2.2基础单价 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0651 |
| UNIT-0283 | ORIGINAL_TEXT | 6.1.2.2基础单价 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0653 |
| UNIT-0284 | ORIGINAL_TEXT | 6.1.2.2基础单价 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0655 |
| UNIT-0285 | ORIGINAL_TEXT | 6.1.2.2基础单价 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0657 |
| UNIT-0286 | CALCULATION | 6.1.2.2基础单价 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | ab432f50:P0658 |

### SEC-076 6.1.2.3费用组成及费率

- Source locator: P0659
- Material density: 8段关键文字、1张表
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `6.1.2.3费用组成及费率` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0287 6.1.2.3费用组成及费率；UNIT-0288 6.1.2.3费用组成及费率；UNIT-0289 6.1.2.3费用组成及费率；UNIT-0290 水土保持措施定额费率表；UNIT-0291 6.1.2.3费用组成及费率
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_table_right_text or top_text_bottom_table
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0287 | ORIGINAL_TEXT | 6.1.2.3费用组成及费率 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0660 |
| UNIT-0288 | ORIGINAL_TEXT | 6.1.2.3费用组成及费率 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0662 |
| UNIT-0289 | ORIGINAL_TEXT | 6.1.2.3费用组成及费率 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0664 |
| UNIT-0290 | ORIGINAL_TABLE | 水土保持措施定额费率表 | source table with explanation | left_table_right_text or top_text_bottom_table | ab432f50:T039, ab432f50:P0665 |
| UNIT-0291 | ORIGINAL_TEXT | 6.1.2.3费用组成及费率 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0666 |
| UNIT-0292 | ORIGINAL_TEXT | 6.1.2.3费用组成及费率 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0668 |
| UNIT-0293 | ORIGINAL_TEXT | 6.1.2.3费用组成及费率 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0670 |
| UNIT-0294 | ORIGINAL_TEXT | 6.1.2.3费用组成及费率 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0671 |
| UNIT-0295 | ORIGINAL_TEXT | 6.1.2.3费用组成及费率 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0673 |

### SEC-077 6.1.2.4估算成果

- Source locator: P0675
- Material density: 3段关键文字、8张表
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `6.1.2.4估算成果` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0296 6.1.2.4估算成果；UNIT-0297 6.1.2.4估算成果；UNIT-0298 6.1.2.4估算成果；UNIT-0299 本项目水土保持估算总表 单位：万元；UNIT-0300 本方案工程措施估算表
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_table_right_text or top_text_bottom_table；left_table_right_text
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0296 | ORIGINAL_TEXT | 6.1.2.4估算成果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0676 |
| UNIT-0297 | ORIGINAL_TEXT | 6.1.2.4估算成果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0677 |
| UNIT-0298 | ORIGINAL_TEXT | 6.1.2.4估算成果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0678 |
| UNIT-0299 | ORIGINAL_TABLE | 本项目水土保持估算总表 单位：万元 | source table with explanation | left_table_right_text or top_text_bottom_table | ab432f50:T040, ab432f50:P0679 |
| UNIT-0300 | ORIGINAL_TABLE | 本方案工程措施估算表 | source table with explanation | left_table_right_text | ab432f50:T041, ab432f50:P0680 |
| UNIT-0301 | ORIGINAL_TABLE | 本方案植物措施估算表 | source table with explanation | left_table_right_text | ab432f50:T042, ab432f50:P0681 |
| UNIT-0302 | ORIGINAL_TABLE | 本方案临时措施估算表 | source table with explanation | left_table_right_text | ab432f50:T043, ab432f50:P0682 |
| UNIT-0303 | ORIGINAL_TABLE | 本方案独立费用估算表 | source table with explanation | left_table_right_text | ab432f50:T044, ab432f50:P0683 |
| UNIT-0304 | ORIGINAL_TABLE | 水土保持补偿费计算表 | source table with explanation | left_table_right_text | ab432f50:T045, ab432f50:P0684 |
| UNIT-0305 | ORIGINAL_TABLE | 主要材料单价汇总表 | source table with explanation | left_table_right_text | ab432f50:T046, ab432f50:P0685 |
| UNIT-0306 | ORIGINAL_TABLE | 工程单价汇总表 | source table with explanation | left_table_right_text | ab432f50:T047, ab432f50:P0686 |

### SEC-078 6.2效益分析

- Source locator: P0687
- Material density: 15段关键文字、1张表
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `6.2效益分析` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0307 6.2效益分析；UNIT-0308 6.2效益分析；UNIT-0309 6.2效益分析；UNIT-0310 6.2效益分析；UNIT-0311 6.2效益分析
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_table_right_text or top_text_bottom_table
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0307 | ORIGINAL_TEXT | 6.2效益分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0689 |
| UNIT-0308 | ORIGINAL_TEXT | 6.2效益分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0690 |
| UNIT-0309 | ORIGINAL_TEXT | 6.2效益分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0691 |
| UNIT-0310 | ORIGINAL_TEXT | 6.2效益分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0692 |
| UNIT-0311 | ORIGINAL_TEXT | 6.2效益分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0693 |
| UNIT-0312 | ORIGINAL_TEXT | 6.2效益分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0694 |
| UNIT-0313 | ORIGINAL_TEXT | 6.2效益分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0695 |
| UNIT-0314 | ORIGINAL_TEXT | 6.2效益分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0696 |
| UNIT-0315 | ORIGINAL_TEXT | 6.2效益分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0698 |
| UNIT-0316 | ORIGINAL_TEXT | 6.2效益分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0699 |
| UNIT-0317 | ORIGINAL_TABLE | 水土保持防治效果分析表 | source table with explanation | left_table_right_text or top_text_bottom_table | ab432f50:T048, ab432f50:P0700 |
| UNIT-0318 | ORIGINAL_TEXT | 6.2效益分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0703 |
| ... | ... | Additional 4 units in JSON inventory | ... | ... | ... |

### SEC-080 组织管理

- Source locator: P0713
- Material density: 7段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `组织管理` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0323 组织管理；UNIT-0324 组织管理；UNIT-0325 组织管理；UNIT-0326 组织管理；UNIT-0327 组织管理
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0323 | ORIGINAL_TEXT | 组织管理 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0715 |
| UNIT-0324 | ORIGINAL_TEXT | 组织管理 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0716 |
| UNIT-0325 | ORIGINAL_TEXT | 组织管理 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0717 |
| UNIT-0326 | ORIGINAL_TEXT | 组织管理 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0718 |
| UNIT-0327 | ORIGINAL_TEXT | 组织管理 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0721 |
| UNIT-0328 | ORIGINAL_TEXT | 组织管理 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0723 |
| UNIT-0329 | ORIGINAL_TEXT | 组织管理 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0724 |

### SEC-081 后续设计

- Source locator: P0725
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `后续设计` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0330 后续设计
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0330 | ORIGINAL_TEXT | 后续设计 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0729 |

### SEC-082 水土保持监理

- Source locator: P0730
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `水土保持监理` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0331 水土保持监理；UNIT-0332 水土保持监理
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0331 | ORIGINAL_TEXT | 水土保持监理 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0731 |
| UNIT-0332 | ORIGINAL_TEXT | 水土保持监理 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0732 |

### SEC-083 水土保持施工

- Source locator: P0734
- Material density: 5段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `水土保持施工` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0333 水土保持施工；UNIT-0334 水土保持施工；UNIT-0335 水土保持施工；UNIT-0336 水土保持施工；UNIT-0337 水土保持施工
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0333 | ORIGINAL_TEXT | 水土保持施工 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0735 |
| UNIT-0334 | ORIGINAL_TEXT | 水土保持施工 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0737 |
| UNIT-0335 | ORIGINAL_TEXT | 水土保持施工 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0739 |
| UNIT-0336 | ORIGINAL_TEXT | 水土保持施工 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0740 |
| UNIT-0337 | ORIGINAL_TEXT | 水土保持施工 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0741 |

### SEC-084 水土保持设施验收

- Source locator: P0742
- Material density: 7段关键文字、3张表、38张图
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `水土保持设施验收` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0338 水土保持设施验收；UNIT-0339 水土保持设施验收；UNIT-0340 水土保持设施验收；UNIT-0341 水土保持设施验收；UNIT-0342 水土保持设施验收
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_table_right_text or top_text_bottom_table；left_figure_right_text or top_figure_bottom_text
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0338 | ORIGINAL_TEXT | 水土保持设施验收 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0743 |
| UNIT-0339 | ORIGINAL_TEXT | 水土保持设施验收 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0745 |
| UNIT-0340 | ORIGINAL_TEXT | 水土保持设施验收 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0746 |
| UNIT-0341 | ORIGINAL_TEXT | 水土保持设施验收 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0747 |
| UNIT-0342 | ORIGINAL_TEXT | 水土保持设施验收 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0748 |
| UNIT-0343 | ORIGINAL_TEXT | 水土保持设施验收 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0754 |
| UNIT-0344 | ORIGINAL_TEXT | 水土保持设施验收 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | ab432f50:P0757 |
| UNIT-0345 | ORIGINAL_TABLE | 水土保持设施验收 | source table with explanation | left_table_right_text or top_text_bottom_table | ab432f50:T049 |
| UNIT-0346 | ORIGINAL_TABLE | 水土保持设施验收 | source table with explanation | left_table_right_text or top_text_bottom_table | ab432f50:T050 |
| UNIT-0347 | ORIGINAL_TABLE | 水土保持设施验收 | source table with explanation | left_table_right_text or top_text_bottom_table | ab432f50:T051 |
| UNIT-0348 | ORIGINAL_FIGURE | 水土保持设施验收 | source figure/map/diagram with report-language explanation | left_figure_right_text or top_figure_bottom_text | ab432f50:I0001 |
| UNIT-0349 | ORIGINAL_FIGURE | 水土保持设施验收 | source figure/map/diagram with report-language explanation | left_figure_right_text or top_figure_bottom_text | ab432f50:I0002 |
| ... | ... | Additional 36 units in JSON inventory | ... | ... | ... |

## Deck Planning Gate

Before authoring slides, update or review `deck_plan.json` so every substantive page is derived
from selected content units, with report-native headings/captions used for visible small titles.
