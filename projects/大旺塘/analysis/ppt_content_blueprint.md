# PPT Content Blueprint

This blueprint is the mandatory thinking workspace between report extraction and slide planning.
The agent must read it, refine the narrative, and then derive `evidence_ledger.json`,
`chapter_coverage.md`, and `deck_plan.json` from the selected content units.

## Inventory Summary

- Sections: 561
- Important paragraphs: 5099
- Tables: 63
- Figures: 221
- PPT content units: 5383

## Thinking Rules

- Preserve the report's title hierarchy before summarizing.
- Treat table and figure captions as the default small-title source.
- Pair source objects with faithful explanation; do not replace technical process with summary cards.
- Split dense tables, long formulas, and complex maps before reducing font size.
- Every planned slide should point back to one or more content unit IDs or explain why no source object exists.

## Content Units By Report Section

### SEC-000 未分章前置内容

- Source locator: 
- Material density: 1张表
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `未分章前置内容` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0001 未分章前置内容
  - Best source pairing: left_table_right_text
  - Slide split decision: split or crop tables before reducing font size.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0001 | ORIGINAL_TABLE | 未分章前置内容 | source table with explanation | left_table_right_text | 0cc6922b:T001 |

### SEC-003 绪论 > 目的任务 > 项目来源

- Source locator: P0034
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `项目来源` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0002 项目来源；UNIT-0003 项目来源
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0002 | ORIGINAL_TEXT | 项目来源 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0036 |
| UNIT-0003 | ORIGINAL_TEXT | 项目来源 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0037 |

### SEC-004 绪论 > 目的任务 > 目的任务

- Source locator: P0038
- Material density: 10段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `目的任务` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0004 目的任务；UNIT-0005 目的任务；UNIT-0006 目的任务；UNIT-0007 目的任务；UNIT-0008 目的任务
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_text_right_table or top_text_bottom_table
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0004 | ORIGINAL_TEXT | 目的任务 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0039 |
| UNIT-0005 | ORIGINAL_TEXT | 目的任务 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0040 |
| UNIT-0006 | ORIGINAL_TEXT | 目的任务 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0041 |
| UNIT-0007 | ORIGINAL_TEXT | 目的任务 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0042 |
| UNIT-0008 | ORIGINAL_TEXT | 目的任务 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0043 |
| UNIT-0009 | ORIGINAL_TEXT | 目的任务 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0044 |
| UNIT-0010 | ORIGINAL_TEXT | 目的任务 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0045 |
| UNIT-0011 | CALCULATION | 目的任务 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P0046 |
| UNIT-0012 | ORIGINAL_TEXT | 目的任务 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0047 |
| UNIT-0013 | ORIGINAL_TEXT | 目的任务 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0048 |

### SEC-006 绪论 > 目的任务 > 工作依据 > 法律法规

- Source locator: P0050
- Material density: 3段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `法律法规` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0014 法律法规；UNIT-0015 法律法规；UNIT-0016 法律法规
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0014 | ORIGINAL_TEXT | 法律法规 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0055 |
| UNIT-0015 | ORIGINAL_TEXT | 法律法规 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0056 |
| UNIT-0016 | ORIGINAL_TEXT | 法律法规 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0057 |

### SEC-007 绪论 > 目的任务 > 工作依据 > 技术标准

- Source locator: P0058
- Material density: 21段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `技术标准` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0017 技术标准；UNIT-0018 技术标准；UNIT-0019 技术标准；UNIT-0020 技术标准；UNIT-0021 技术标准
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_text_right_table or top_text_bottom_table
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0017 | ORIGINAL_TEXT | 技术标准 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0059 |
| UNIT-0018 | ORIGINAL_TEXT | 技术标准 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0060 |
| UNIT-0019 | ORIGINAL_TEXT | 技术标准 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0061 |
| UNIT-0020 | ORIGINAL_TEXT | 技术标准 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0062 |
| UNIT-0021 | ORIGINAL_TEXT | 技术标准 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0063 |
| UNIT-0022 | ORIGINAL_TEXT | 技术标准 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0064 |
| UNIT-0023 | ORIGINAL_TEXT | 技术标准 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0065 |
| UNIT-0024 | ORIGINAL_TEXT | 技术标准 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0066 |
| UNIT-0025 | ORIGINAL_TEXT | 技术标准 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0067 |
| UNIT-0026 | ORIGINAL_TEXT | 技术标准 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0068 |
| UNIT-0027 | ORIGINAL_TEXT | 技术标准 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0069 |
| UNIT-0028 | ORIGINAL_TEXT | 技术标准 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0070 |
| ... | ... | Additional 9 units in JSON inventory | ... | ... | ... |

### SEC-009 绪论 > 矿业权设置

- Source locator: P0086
- Material density: 1段关键文字、1张表
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `矿业权设置` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0038 矿业权设置；UNIT-0039 华润大旺塘矿现持采矿许可证范围及拐点坐标
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_table_right_text or top_text_bottom_table
  - Slide split decision: split or crop tables before reducing font size.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0038 | ORIGINAL_TEXT | 矿业权设置 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0088 |
| UNIT-0039 | ORIGINAL_TABLE | 华润大旺塘矿现持采矿许可证范围及拐点坐标 | source table with explanation | left_table_right_text or top_text_bottom_table | 0cc6922b:T002, 0cc6922b:P0089 |

### SEC-011 绪论 > 矿业权设置 > 采矿权设置 > 核实报告拟设置采矿权基本情况

- Source locator: P0093
- Material density: 1段关键文字、1张表
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `核实报告拟设置采矿权基本情况` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0040 核实报告拟设置采矿权基本情况；UNIT-0041 资源储量核实报告拟设采矿区范围及拐点坐标
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_table_right_text or top_text_bottom_table
  - Slide split decision: split or crop tables before reducing font size.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0040 | ORIGINAL_TEXT | 核实报告拟设置采矿权基本情况 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0094 |
| UNIT-0041 | ORIGINAL_TABLE | 资源储量核实报告拟设采矿区范围及拐点坐标 | source table with explanation | left_table_right_text or top_text_bottom_table | 0cc6922b:T003, 0cc6922b:P0095 |

### SEC-012 绪论 > 矿业权设置 > 采矿权设置 > 分割保留区（现拟设采矿权）

- Source locator: P0096
- Material density: 1段关键文字、1张表
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `分割保留区（现拟设采矿权）` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0042 分割保留区（现拟设采矿权）；UNIT-0043 分割保留区（现拟设采矿权）范围及拐点坐标
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_table_right_text
  - Slide split decision: split or crop tables before reducing font size.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0042 | ORIGINAL_TEXT | 分割保留区（现拟设采矿权） | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0097 |
| UNIT-0043 | ORIGINAL_TABLE | 分割保留区（现拟设采矿权）范围及拐点坐标 | source table with explanation | left_table_right_text | 0cc6922b:T004, 0cc6922b:P0098 |

### SEC-013 绪论 > 矿业权设置 > 采矿权设置 > 拟设采矿权情况

- Source locator: P0101
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `拟设采矿权情况` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0044 拟设采矿权情况
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0044 | ORIGINAL_TEXT | 拟设采矿权情况 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0102 |

### SEC-014 绪论 > 矿业权设置 > 矿山开发现状

- Source locator: P0103
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `矿山开发现状` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0045 矿山开发现状；UNIT-0046 矿山开发现状
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0045 | ORIGINAL_TEXT | 矿山开发现状 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0104 |
| UNIT-0046 | ORIGINAL_TEXT | 矿山开发现状 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0105 |

### SEC-015 绪论 > 矿业权设置 > 矿山开发规划

- Source locator: P0109
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `矿山开发规划` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0047 矿山开发规划
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0047 | ORIGINAL_TEXT | 矿山开发规划 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0110 |

### SEC-017 绪论 > 以往工作评述 > 以往工作简述

- Source locator: P0112
- Material density: 15段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `以往工作简述` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0048 以往工作简述；UNIT-0049 以往工作简述；UNIT-0050 以往工作简述；UNIT-0051 以往工作简述；UNIT-0052 以往工作简述
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0048 | ORIGINAL_TEXT | 以往工作简述 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0113 |
| UNIT-0049 | ORIGINAL_TEXT | 以往工作简述 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0114 |
| UNIT-0050 | ORIGINAL_TEXT | 以往工作简述 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0115 |
| UNIT-0051 | ORIGINAL_TEXT | 以往工作简述 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0116 |
| UNIT-0052 | ORIGINAL_TEXT | 以往工作简述 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0117 |
| UNIT-0053 | ORIGINAL_TEXT | 以往工作简述 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0118 |
| UNIT-0054 | ORIGINAL_TEXT | 以往工作简述 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0119 |
| UNIT-0055 | ORIGINAL_TEXT | 以往工作简述 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0120 |
| UNIT-0056 | ORIGINAL_TEXT | 以往工作简述 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0121 |
| UNIT-0057 | ORIGINAL_TEXT | 以往工作简述 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0122 |
| UNIT-0058 | ORIGINAL_TEXT | 以往工作简述 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0123 |
| UNIT-0059 | ORIGINAL_TEXT | 以往工作简述 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0124 |
| ... | ... | Additional 3 units in JSON inventory | ... | ... | ... |

### SEC-018 绪论 > 以往工作评述 > 以往工作质量评述

- Source locator: P0129
- Material density: 3段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `以往工作质量评述` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0063 以往工作质量评述；UNIT-0064 以往工作质量评述；UNIT-0065 以往工作质量评述
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0063 | ORIGINAL_TEXT | 以往工作质量评述 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0130 |
| UNIT-0064 | ORIGINAL_TEXT | 以往工作质量评述 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0131 |
| UNIT-0065 | ORIGINAL_TEXT | 以往工作质量评述 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0132 |

### SEC-025 绪论 > 本次工作概况 > 勘查工作部署 > 投入工作量

- Source locator: P0145
- Material density: 1段关键文字、1张表
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `投入工作量` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0066 投入工作量；UNIT-0067 完成主要实物工作量一览表
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_table_right_text or top_text_bottom_table
  - Slide split decision: split or crop tables before reducing font size.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0066 | ORIGINAL_TEXT | 投入工作量 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0146 |
| UNIT-0067 | ORIGINAL_TABLE | 完成主要实物工作量一览表 | source table with explanation | left_table_right_text or top_text_bottom_table | 0cc6922b:T005, 0cc6922b:P0147 |

### SEC-026 绪论 > 本次工作概况 > 勘查工作部署 > 利用以往工作量

- Source locator: P0148
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `利用以往工作量` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0068 利用以往工作量
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0068 | ORIGINAL_TEXT | 利用以往工作量 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0150 |

### SEC-031 绪论 > 本次工作概况 > 勘查完成情况 > 工作评价 > 地下水、地表水动态长期观测

- Source locator: P0157
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `地下水、地表水动态长期观测` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0069 地下水、地表水动态长期观测
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0069 | ORIGINAL_TEXT | 地下水、地表水动态长期观测 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0158 |

### SEC-032 绪论 > 本次工作概况 > 勘查完成情况 > 工作评价 > 物探

- Source locator: P0159
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `物探` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0070 物探
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0070 | ORIGINAL_TEXT | 物探 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0160 |

### SEC-034 绪论 > 本次工作概况 > 勘查完成情况 > 工作评价 > 抽水试验

- Source locator: P0163
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `抽水试验` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0071 抽水试验
  - Best source pairing: left_text_right_table or top_text_bottom_table
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0071 | CALCULATION | 抽水试验 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P0164 |

### SEC-035 绪论 > 本次工作概况 > 勘查完成情况 > 工作评价 > 压水试验

- Source locator: P0165
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `压水试验` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0072 压水试验；UNIT-0073 压水试验
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_text_right_table or top_text_bottom_table
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0072 | ORIGINAL_TEXT | 压水试验 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0166 |
| UNIT-0073 | CALCULATION | 压水试验 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P0167 |

### SEC-036 绪论 > 本次工作概况 > 勘查完成情况 > 工作评价 > 水化学分析样采集及送检

- Source locator: P0168
- Material density: 1段关键文字、1张表
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `水化学分析样采集及送检` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0074 水化学分析样采集及送检；UNIT-0075 水化学分析样采集及送检
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_table_right_text
  - Slide split decision: split or crop tables before reducing font size.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0074 | ORIGINAL_TEXT | 水化学分析样采集及送检 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0170 |
| UNIT-0075 | ORIGINAL_TABLE | 水化学分析样采集及送检 | source table with explanation | left_table_right_text | 0cc6922b:T006 |

### SEC-037 绪论 > 本次工作概况 > 勘查完成情况 > 工作评价 > 孔内成像

- Source locator: P0171
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `孔内成像` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0076 孔内成像
  - Best source pairing: left_text_right_table or top_text_bottom_table
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0076 | CALCULATION | 孔内成像 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P0173 |

### SEC-040 绪论 > 本次工作概况 > 勘查完成情况 > 取得成果

- Source locator: P0179
- Material density: 1段关键文字、1张表
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `取得成果` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0077 取得成果；UNIT-0078 取得成果一览表
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_table_right_text or top_text_bottom_table
  - Slide split decision: split or crop tables before reducing font size.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0077 | ORIGINAL_TEXT | 取得成果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0180 |
| UNIT-0078 | ORIGINAL_TABLE | 取得成果一览表 | source table with explanation | left_table_right_text or top_text_bottom_table | 0cc6922b:T007, 0cc6922b:P0182 |

### SEC-042 区域概况 > 地理位置

- Source locator: P0185
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `地理位置` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0079 地理位置
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0079 | ORIGINAL_TEXT | 地理位置 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0187 |

### SEC-043 区域概况 > 地形地貌

- Source locator: P0191
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `地形地貌` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0080 地形地貌；UNIT-0081 地形地貌
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0080 | ORIGINAL_TEXT | 地形地貌 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0193 |
| UNIT-0081 | ORIGINAL_TEXT | 地形地貌 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0194 |

### SEC-045 区域概况 > 气象水文 > 气象

- Source locator: P0198
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `气象` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0082 气象
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0082 | ORIGINAL_TEXT | 气象 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0199 |

### SEC-046 区域概况 > 气象水文 > 水文

- Source locator: P0203
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `水文` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0083 水文；UNIT-0084 水文
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0083 | ORIGINAL_TEXT | 水文 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0205 |
| UNIT-0084 | ORIGINAL_TEXT | 水文 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0209 |

### SEC-049 区域概况 > 区域地质 > 地层岩性 > 寒武系八村群（∈1bc）

- Source locator: P0215
- Material density: 3段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `寒武系八村群（∈1bc）` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0085 寒武系八村群（∈1bc）；UNIT-0086 寒武系八村群（∈1bc）；UNIT-0087 寒武系八村群（∈1bc）
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0085 | ORIGINAL_TEXT | 寒武系八村群（∈1bc） | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0217 |
| UNIT-0086 | ORIGINAL_TEXT | 寒武系八村群（∈1bc） | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0218 |
| UNIT-0087 | ORIGINAL_TEXT | 寒武系八村群（∈1bc） | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0219 |

### SEC-050 区域概况 > 区域地质 > 地层岩性 > 泥盆系上、中、下统（D1-3）

- Source locator: P0220
- Material density: 5段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `泥盆系上、中、下统（D1-3）` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0088 泥盆系上、中、下统（D1-3）；UNIT-0089 泥盆系上、中、下统（D1-3）；UNIT-0090 泥盆系上、中、下统（D1-3）；UNIT-0091 泥盆系上、中、下统（D1-3）；UNIT-0092 泥盆系上、中、下统（D1-3）
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0088 | ORIGINAL_TEXT | 泥盆系上、中、下统（D1-3） | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0222 |
| UNIT-0089 | ORIGINAL_TEXT | 泥盆系上、中、下统（D1-3） | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0223 |
| UNIT-0090 | ORIGINAL_TEXT | 泥盆系上、中、下统（D1-3） | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0224 |
| UNIT-0091 | ORIGINAL_TEXT | 泥盆系上、中、下统（D1-3） | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0225 |
| UNIT-0092 | ORIGINAL_TEXT | 泥盆系上、中、下统（D1-3） | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0226 |

### SEC-051 区域概况 > 区域地质 > 地层岩性 > 石炭系下统（C1）

- Source locator: P0227
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `石炭系下统（C1）` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0093 石炭系下统（C1）
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0093 | ORIGINAL_TEXT | 石炭系下统（C1） | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0228 |

### SEC-061 区域概况 > 区域水文地质 > 地下水类型及含水岩组划分 > 松散岩类孔隙水

- Source locator: P0253
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `松散岩类孔隙水` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0094 松散岩类孔隙水
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0094 | ORIGINAL_TEXT | 松散岩类孔隙水 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0254 |

### SEC-062 区域概况 > 区域水文地质 > 地下水类型及含水岩组划分 > 碳酸盐岩类裂隙溶洞水

- Source locator: P0255
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `碳酸盐岩类裂隙溶洞水` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0095 碳酸盐岩类裂隙溶洞水
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0095 | ORIGINAL_TEXT | 碳酸盐岩类裂隙溶洞水 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0256 |

### SEC-063 区域概况 > 区域水文地质 > 地下水类型及含水岩组划分 > 基岩裂隙水

- Source locator: P0257
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `基岩裂隙水` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0096 基岩裂隙水
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0096 | ORIGINAL_TEXT | 基岩裂隙水 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0258 |

### SEC-064 区域概况 > 区域水文地质 > 地下水补径排条件

- Source locator: P0259
- Material density: 3段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `地下水补径排条件` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0097 地下水补径排条件；UNIT-0098 地下水补径排条件；UNIT-0099 地下水补径排条件
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0097 | ORIGINAL_TEXT | 地下水补径排条件 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0260 |
| UNIT-0098 | ORIGINAL_TEXT | 地下水补径排条件 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0261 |
| UNIT-0099 | ORIGINAL_TEXT | 地下水补径排条件 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0262 |

### SEC-065 区域概况 > 区域水文地质 > 区域水文地质单元

- Source locator: P0263
- Material density: 5段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `区域水文地质单元` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0100 区域水文地质单元；UNIT-0101 区域水文地质单元；UNIT-0102 区域水文地质单元；UNIT-0103 区域水文地质单元；UNIT-0104 区域水文地质单元
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0100 | ORIGINAL_TEXT | 区域水文地质单元 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0264 |
| UNIT-0101 | ORIGINAL_TEXT | 区域水文地质单元 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0265 |
| UNIT-0102 | ORIGINAL_TEXT | 区域水文地质单元 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0266 |
| UNIT-0103 | ORIGINAL_TEXT | 区域水文地质单元 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0267 |
| UNIT-0104 | ORIGINAL_TEXT | 区域水文地质单元 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0268 |

### SEC-067 水文地质勘探工作 > 水文地质调查

- Source locator: P0275
- Material density: 2段关键文字、1张表
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `水文地质调查` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0105 水文地质调查；UNIT-0106 水文地质调查；UNIT-0107 调查工作量
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_table_right_text
  - Slide split decision: split or crop tables before reducing font size.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0105 | ORIGINAL_TEXT | 水文地质调查 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0276 |
| UNIT-0106 | ORIGINAL_TEXT | 水文地质调查 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0277 |
| UNIT-0107 | ORIGINAL_TABLE | 调查工作量 | source table with explanation | left_table_right_text | 0cc6922b:T008, 0cc6922b:P0278 |

### SEC-068 水文地质勘探工作 > 水文地质调查 > 地层岩性及富水性调查

- Source locator: P0279
- Material density: 2段关键文字、3张表
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `地层岩性及富水性调查` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0108 地层岩性及富水性调查；UNIT-0109 地层岩性及富水性调查；UNIT-0110 地层岩性及富水性调查；UNIT-0111 地层岩性及富水性调查；UNIT-0112 地层岩性及富水性调查
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_table_right_text
  - Slide split decision: split or crop tables before reducing font size.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0108 | ORIGINAL_TEXT | 地层岩性及富水性调查 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0280 |
| UNIT-0109 | ORIGINAL_TABLE | 地层岩性及富水性调查 | source table with explanation | left_table_right_text | 0cc6922b:T009 |
| UNIT-0110 | ORIGINAL_TABLE | 地层岩性及富水性调查 | source table with explanation | left_table_right_text | 0cc6922b:T010 |
| UNIT-0111 | ORIGINAL_TEXT | 地层岩性及富水性调查 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0283 |
| UNIT-0112 | ORIGINAL_TABLE | 地层岩性及富水性调查 | source table with explanation | left_table_right_text | 0cc6922b:T011 |

### SEC-069 水文地质勘探工作 > 水文地质调查 > 井泉点及地表水体调查

- Source locator: P0284
- Material density: 2段关键文字、2张表
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `井泉点及地表水体调查` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0113 井泉点及地表水体调查；UNIT-0114 井泉点及地表水体调查；UNIT-0115 井泉点及地表水体调查；UNIT-0116 井泉点及地表水体调查
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_table_right_text
  - Slide split decision: split or crop tables before reducing font size.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0113 | ORIGINAL_TEXT | 井泉点及地表水体调查 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0287 |
| UNIT-0114 | ORIGINAL_TABLE | 井泉点及地表水体调查 | source table with explanation | left_table_right_text | 0cc6922b:T012 |
| UNIT-0115 | ORIGINAL_TEXT | 井泉点及地表水体调查 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0289 |
| UNIT-0116 | ORIGINAL_TABLE | 井泉点及地表水体调查 | source table with explanation | left_table_right_text | 0cc6922b:T013 |

### SEC-070 水文地质勘探工作 > 水文地质调查 > 小结

- Source locator: P0290
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `小结` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0117 小结；UNIT-0118 小结
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0117 | ORIGINAL_TEXT | 小结 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0291 |
| UNIT-0118 | ORIGINAL_TEXT | 小结 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0292 |

### SEC-073 水文地质勘探工作 > 水文地质物探 > 工作方法 > 测地工作

- Source locator: P0295
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `测地工作` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0119 测地工作；UNIT-0120 测地工作
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0119 | ORIGINAL_TEXT | 测地工作 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0296 |
| UNIT-0120 | ORIGINAL_TEXT | 测地工作 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0297 |

### SEC-074 水文地质勘探工作 > 水文地质物探 > 工作方法 > 高密度电法

- Source locator: P0301
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `高密度电法` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0121 高密度电法；UNIT-0122 高密度电法
  - Best source pairing: left_text_right_table or top_text_bottom_table；left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0121 | CALCULATION | 高密度电法 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P0309 |
| UNIT-0122 | ORIGINAL_TEXT | 高密度电法 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0310 |

### SEC-075 水文地质勘探工作 > 水文地质物探 > 工作方法 > 微动测量

- Source locator: P0314
- Material density: 6段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `微动测量` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0123 微动测量；UNIT-0124 微动测量；UNIT-0125 微动测量；UNIT-0126 微动测量；UNIT-0127 微动测量
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_text_right_table or top_text_bottom_table
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0123 | ORIGINAL_TEXT | 微动测量 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0315 |
| UNIT-0124 | ORIGINAL_TEXT | 微动测量 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0317 |
| UNIT-0125 | CALCULATION | 微动测量 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P0318 |
| UNIT-0126 | ORIGINAL_TEXT | 微动测量 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0319 |
| UNIT-0127 | ORIGINAL_TEXT | 微动测量 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0321 |
| UNIT-0128 | ORIGINAL_TEXT | 微动测量 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0322 |

### SEC-076 水文地质勘探工作 > 水文地质物探 > 工作方法 > 野外工作方法

- Source locator: P0325
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `野外工作方法` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0129 野外工作方法
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0129 | ORIGINAL_TEXT | 野外工作方法 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0329 |

### SEC-077 水文地质勘探工作 > 水文地质物探 > 工作方法 > 数据处理

- Source locator: P0330
- Material density: 18段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `数据处理` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0130 数据处理；UNIT-0131 数据处理；UNIT-0132 数据处理；UNIT-0133 数据处理；UNIT-0134 数据处理
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_text_right_table or top_text_bottom_table
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0130 | ORIGINAL_TEXT | 数据处理 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0331 |
| UNIT-0131 | ORIGINAL_TEXT | 数据处理 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0332 |
| UNIT-0132 | ORIGINAL_TEXT | 数据处理 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0334 |
| UNIT-0133 | CALCULATION | 数据处理 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P0335 |
| UNIT-0134 | CALCULATION | 数据处理 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P0336 |
| UNIT-0135 | ORIGINAL_TEXT | 数据处理 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0337 |
| UNIT-0136 | ORIGINAL_TEXT | 数据处理 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0339 |
| UNIT-0137 | ORIGINAL_TEXT | 数据处理 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0340 |
| UNIT-0138 | ORIGINAL_TEXT | 数据处理 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0343 |
| UNIT-0139 | CALCULATION | 数据处理 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P0344 |
| UNIT-0140 | CALCULATION | 数据处理 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P0345 |
| UNIT-0141 | CALCULATION | 数据处理 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P0346 |
| ... | ... | Additional 6 units in JSON inventory | ... | ... | ... |

### SEC-078 水文地质勘探工作 > 水文地质物探 > 解释依据

- Source locator: P0370
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `解释依据` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0148 解释依据；UNIT-0149 解释依据
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0148 | ORIGINAL_TEXT | 解释依据 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0371 |
| UNIT-0149 | ORIGINAL_TEXT | 解释依据 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0372 |

### SEC-080 水文地质勘探工作 > 水文地质物探 > 成果解释 > P1线高密度成果解释

- Source locator: P0375
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `P1线高密度成果解释` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0150 P1线高密度成果解释
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0150 | ORIGINAL_TEXT | P1线高密度成果解释 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0379 |

### SEC-081 水文地质勘探工作 > 水文地质物探 > 成果解释 > P2线高密度成果解释

- Source locator: P0380
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `P2线高密度成果解释` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0151 P2线高密度成果解释；UNIT-0152 P2线高密度成果解释
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0151 | ORIGINAL_TEXT | P2线高密度成果解释 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0381 |
| UNIT-0152 | ORIGINAL_TEXT | P2线高密度成果解释 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0382 |

### SEC-082 水文地质勘探工作 > 水文地质物探 > 成果解释 > P3线高密度成果解释

- Source locator: P0386
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `P3线高密度成果解释` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0153 P3线高密度成果解释
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0153 | ORIGINAL_TEXT | P3线高密度成果解释 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0387 |

### SEC-083 水文地质勘探工作 > 水文地质物探 > 成果解释 > P4线高密度成果解释

- Source locator: P0391
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `P4线高密度成果解释` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0154 P4线高密度成果解释
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0154 | ORIGINAL_TEXT | P4线高密度成果解释 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0392 |

### SEC-084 水文地质勘探工作 > 水文地质物探 > 成果解释 > P5线高密度成果解释

- Source locator: P0397
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `P5线高密度成果解释` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0155 P5线高密度成果解释
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0155 | ORIGINAL_TEXT | P5线高密度成果解释 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0398 |

### SEC-085 水文地质勘探工作 > 水文地质物探 > 成果解释 > P6线高密度成果解释

- Source locator: P0402
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `P6线高密度成果解释` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0156 P6线高密度成果解释
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0156 | ORIGINAL_TEXT | P6线高密度成果解释 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0403 |

### SEC-086 水文地质勘探工作 > 水文地质物探 > 成果解释 > P7线高密度成果解释

- Source locator: P0407
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `P7线高密度成果解释` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0157 P7线高密度成果解释
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0157 | ORIGINAL_TEXT | P7线高密度成果解释 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0408 |

### SEC-087 水文地质勘探工作 > 水文地质物探 > 成果解释 > P8线高密度成果解释

- Source locator: P0413
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `P8线高密度成果解释` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0158 P8线高密度成果解释
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0158 | ORIGINAL_TEXT | P8线高密度成果解释 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0414 |

### SEC-088 水文地质勘探工作 > 水文地质物探 > 成果解释 > P9线高密度成果解释

- Source locator: P0418
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `P9线高密度成果解释` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0159 P9线高密度成果解释
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0159 | ORIGINAL_TEXT | P9线高密度成果解释 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0419 |

### SEC-089 水文地质勘探工作 > 水文地质物探 > 成果解释 > P10线高密度成果解释

- Source locator: P0425
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `P10线高密度成果解释` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0160 P10线高密度成果解释
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0160 | ORIGINAL_TEXT | P10线高密度成果解释 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0426 |

### SEC-090 水文地质勘探工作 > 水文地质物探 > 成果解释 > P11线高密度成果解释

- Source locator: P0431
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `P11线高密度成果解释` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0161 P11线高密度成果解释
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0161 | ORIGINAL_TEXT | P11线高密度成果解释 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0432 |

### SEC-091 水文地质勘探工作 > 水文地质物探 > 成果解释 > P12线高密度成果解释

- Source locator: P0436
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `P12线高密度成果解释` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0162 P12线高密度成果解释；UNIT-0163 P12线高密度成果解释
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0162 | ORIGINAL_TEXT | P12线高密度成果解释 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0437 |
| UNIT-0163 | ORIGINAL_TEXT | P12线高密度成果解释 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0438 |

### SEC-092 水文地质勘探工作 > 水文地质物探 > 成果解释 > P13线高密度成果解释

- Source locator: P0442
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `P13线高密度成果解释` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0164 P13线高密度成果解释
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0164 | ORIGINAL_TEXT | P13线高密度成果解释 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0443 |

### SEC-093 水文地质勘探工作 > 水文地质物探 > 成果解释 > P14线高密度成果解释

- Source locator: P0447
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `P14线高密度成果解释` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0165 P14线高密度成果解释
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0165 | ORIGINAL_TEXT | P14线高密度成果解释 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0448 |

### SEC-094 水文地质勘探工作 > 水文地质物探 > 成果解释 > P15线高密度成果解释

- Source locator: P0453
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `P15线高密度成果解释` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0166 P15线高密度成果解释
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0166 | ORIGINAL_TEXT | P15线高密度成果解释 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0454 |

### SEC-095 水文地质勘探工作 > 水文地质物探 > 成果解释 > W10线微动成果解释

- Source locator: P0458
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `W10线微动成果解释` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0167 W10线微动成果解释
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0167 | ORIGINAL_TEXT | W10线微动成果解释 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0459 |

### SEC-096 水文地质勘探工作 > 水文地质物探 > 成果解释 > W11线微动成果解释

- Source locator: P0463
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `W11线微动成果解释` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0168 W11线微动成果解释
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0168 | ORIGINAL_TEXT | W11线微动成果解释 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0464 |

### SEC-097 水文地质勘探工作 > 水文地质物探 > 成果解释 > W12线微动成果解释

- Source locator: P0468
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `W12线微动成果解释` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0169 W12线微动成果解释
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0169 | ORIGINAL_TEXT | W12线微动成果解释 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0469 |

### SEC-098 水文地质勘探工作 > 水文地质物探 > 物探成果

- Source locator: P0473
- Material density: 1段关键文字、1张表
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `物探成果` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0170 物探成果；UNIT-0171 物探异常成果统计表
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_table_right_text or top_text_bottom_table
  - Slide split decision: split or crop tables before reducing font size.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0170 | ORIGINAL_TEXT | 物探成果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0474 |
| UNIT-0171 | ORIGINAL_TABLE | 物探异常成果统计表 | source table with explanation | left_table_right_text or top_text_bottom_table | 0cc6922b:T014, 0cc6922b:P0475 |

### SEC-099 水文地质勘探工作 > 水文地质物探 > 成果验证

- Source locator: P0481
- Material density: 4段关键文字、1张表
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `成果验证` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0172 成果验证；UNIT-0173 钻孔验证物探成果表；UNIT-0174 成果验证；UNIT-0175 成果验证；UNIT-0176 成果验证
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_table_right_text or top_text_bottom_table；left_text_right_table or top_text_bottom_table
  - Slide split decision: split or crop tables before reducing font size.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0172 | ORIGINAL_TEXT | 成果验证 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0482 |
| UNIT-0173 | ORIGINAL_TABLE | 钻孔验证物探成果表 | source table with explanation | left_table_right_text or top_text_bottom_table | 0cc6922b:T015, 0cc6922b:P0483 |
| UNIT-0174 | ORIGINAL_TEXT | 成果验证 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0485 |
| UNIT-0175 | ORIGINAL_TEXT | 成果验证 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0486 |
| UNIT-0176 | CALCULATION | 成果验证 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P0487 |

### SEC-101 水文地质勘探工作 > 水文地质钻探 > 水文地质钻孔

- Source locator: P0489
- Material density: 2段关键文字、1张表
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `水文地质钻孔` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0177 水文地质钻孔；UNIT-0178 水文地质钻孔；UNIT-0179 水文地质勘察钻孔信息一览表
  - Best source pairing: left_text_right_table or top_text_bottom_table；left_text_right_figure or text_with_keypoints；left_table_right_text or top_text_bottom_table
  - Slide split decision: split or crop tables before reducing font size.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0177 | CALCULATION | 水文地质钻孔 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P0490 |
| UNIT-0178 | ORIGINAL_TEXT | 水文地质钻孔 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0491 |
| UNIT-0179 | ORIGINAL_TABLE | 水文地质勘察钻孔信息一览表 | source table with explanation | left_table_right_text or top_text_bottom_table | 0cc6922b:T016, 0cc6922b:P0494 |

### SEC-103 水文地质勘探工作 > 水文地质钻探 > 钻孔孔内成像 > 工作概况

- Source locator: P0497
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `工作概况` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0180 工作概况
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0180 | ORIGINAL_TEXT | 工作概况 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0498 |

### SEC-104 水文地质勘探工作 > 水文地质钻探 > 钻孔孔内成像 > 技术要求

- Source locator: P0499
- Material density: 9段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `技术要求` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0181 技术要求；UNIT-0182 技术要求；UNIT-0183 技术要求；UNIT-0184 技术要求；UNIT-0185 技术要求
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_text_right_table or top_text_bottom_table
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0181 | ORIGINAL_TEXT | 技术要求 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0500 |
| UNIT-0182 | ORIGINAL_TEXT | 技术要求 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0501 |
| UNIT-0183 | ORIGINAL_TEXT | 技术要求 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0502 |
| UNIT-0184 | CALCULATION | 技术要求 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P0503 |
| UNIT-0185 | ORIGINAL_TEXT | 技术要求 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0504 |
| UNIT-0186 | CALCULATION | 技术要求 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P0505 |
| UNIT-0187 | ORIGINAL_TEXT | 技术要求 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0506 |
| UNIT-0188 | CALCULATION | 技术要求 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P0507 |
| UNIT-0189 | ORIGINAL_TEXT | 技术要求 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0508 |

### SEC-105 水文地质勘探工作 > 水文地质钻探 > 钻孔孔内成像 > 工作方法

- Source locator: P0509
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `工作方法` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0190 工作方法；UNIT-0191 工作方法
  - Best source pairing: left_text_right_table or top_text_bottom_table；left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0190 | CALCULATION | 工作方法 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P0510 |
| UNIT-0191 | ORIGINAL_TEXT | 工作方法 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0515 |

### SEC-106 水文地质勘探工作 > 水文地质钻探 > 钻孔孔内成像 > 测试成果

- Source locator: P0518
- Material density: 2张表
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `测试成果` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0192 孔内成像测试节理裂隙统计表；UNIT-0193 孔内成像测试成果
  - Best source pairing: left_table_right_text or top_text_bottom_table；left_table_right_text
  - Slide split decision: split or crop tables before reducing font size.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0192 | ORIGINAL_TABLE | 孔内成像测试节理裂隙统计表 | source table with explanation | left_table_right_text or top_text_bottom_table | 0cc6922b:T017, 0cc6922b:P0520 |
| UNIT-0193 | ORIGINAL_TABLE | 孔内成像测试成果 | source table with explanation | left_table_right_text | 0cc6922b:T018, 0cc6922b:P0521 |

### SEC-110 水文地质勘探工作 > 水文地质试验 > 抽水试验 > 技术要求

- Source locator: P0528
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `技术要求` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0194 技术要求
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0194 | ORIGINAL_TEXT | 技术要求 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0529 |

### SEC-111 水文地质勘探工作 > 水文地质试验 > 抽水试验 > 水文地质参数计算

- Source locator: P0530
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `水文地质参数计算` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0195 水文地质参数计算
  - Best source pairing: left_text_right_table or top_text_bottom_table
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0195 | CALCULATION | 水文地质参数计算 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P0531 |

### SEC-112 水文地质勘探工作 > 水文地质试验 > 抽水试验 > 抽水试验计算公式

- Source locator: P0532
- Material density: 13段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `抽水试验计算公式` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0196 抽水试验计算公式；UNIT-0197 抽水试验计算公式；UNIT-0198 抽水试验计算公式；UNIT-0199 抽水试验计算公式；UNIT-0200 抽水试验计算公式
  - Best source pairing: left_text_right_table or top_text_bottom_table；left_text_right_figure or text_with_keypoints
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0196 | CALCULATION | 抽水试验计算公式 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P0533 |
| UNIT-0197 | ORIGINAL_TEXT | 抽水试验计算公式 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0534 |
| UNIT-0198 | ORIGINAL_TEXT | 抽水试验计算公式 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0537 |
| UNIT-0199 | CALCULATION | 抽水试验计算公式 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P0540 |
| UNIT-0200 | CALCULATION | 抽水试验计算公式 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P0541 |
| UNIT-0201 | CALCULATION | 抽水试验计算公式 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P0542 |
| UNIT-0202 | CALCULATION | 抽水试验计算公式 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P0543 |
| UNIT-0203 | ORIGINAL_TEXT | 抽水试验计算公式 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0544 |
| UNIT-0204 | ORIGINAL_TEXT | 抽水试验计算公式 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0545 |
| UNIT-0205 | CALCULATION | 抽水试验计算公式 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P0550 |
| UNIT-0206 | CALCULATION | 抽水试验计算公式 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P0551 |
| UNIT-0207 | ORIGINAL_TEXT | 抽水试验计算公式 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0552 |
| ... | ... | Additional 1 units in JSON inventory | ... | ... | ... |

### SEC-113 水文地质勘探工作 > 水文地质试验 > 抽水试验 > 抽水试验计算结果

- Source locator: P0554
- Material density: 5段关键文字、8张表
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `抽水试验计算结果` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0209 抽水试验计算结果；UNIT-0210 抽水试验计算结果；UNIT-0211 抽水试验计算结果；UNIT-0212 抽水试验计算结果；UNIT-0213 钻孔SK4-1计算参数
  - Best source pairing: left_text_right_table or top_text_bottom_table；left_table_right_text；left_table_right_text or top_text_bottom_table
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0209 | CALCULATION | 抽水试验计算结果 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P0555 |
| UNIT-0210 | CALCULATION | 抽水试验计算结果 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P0556 |
| UNIT-0211 | CALCULATION | 抽水试验计算结果 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P0557 |
| UNIT-0212 | CALCULATION | 抽水试验计算结果 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P0558 |
| UNIT-0213 | ORIGINAL_TABLE | 钻孔SK4-1计算参数 | source table with explanation | left_table_right_text | 0cc6922b:T019, 0cc6922b:P0575 |
| UNIT-0214 | ORIGINAL_TABLE | 钻孔SK16-6计算参数 | source table with explanation | left_table_right_text | 0cc6922b:T020, 0cc6922b:P0576 |
| UNIT-0215 | ORIGINAL_TABLE | 钻孔SK9-5计算参数 | source table with explanation | left_table_right_text | 0cc6922b:T021, 0cc6922b:P0577 |
| UNIT-0216 | ORIGINAL_TABLE | 钻孔SK16-8计算参数 | source table with explanation | left_table_right_text | 0cc6922b:T022, 0cc6922b:P0578 |
| UNIT-0217 | ORIGINAL_TABLE | 钻孔SK12-6计算参数 | source table with explanation | left_table_right_text | 0cc6922b:T023, 0cc6922b:P0579 |
| UNIT-0218 | ORIGINAL_TABLE | 钻孔SK9-7计算参数 | source table with explanation | left_table_right_text | 0cc6922b:T024, 0cc6922b:P0580 |
| UNIT-0219 | ORIGINAL_TABLE | 抽水试验计算结果 | source table with explanation | left_table_right_text or top_text_bottom_table | 0cc6922b:T025, 0cc6922b:P0581 |
| UNIT-0220 | ORIGINAL_TABLE | 钻孔单位涌水量计算结果表 | source table with explanation | left_table_right_text or top_text_bottom_table | 0cc6922b:T026, 0cc6922b:P0582 |
| ... | ... | Additional 1 units in JSON inventory | ... | ... | ... |

### SEC-115 水文地质勘探工作 > 水文地质试验 > 压水试验 > 试验概况

- Source locator: P0585
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `试验概况` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0222 试验概况
  - Best source pairing: left_text_right_table or top_text_bottom_table
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0222 | CALCULATION | 试验概况 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P0586 |

### SEC-117 水文地质勘探工作 > 水文地质试验 > 压水试验 > 计算公式

- Source locator: P0591
- Material density: 4段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `计算公式` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0223 计算公式；UNIT-0224 计算公式；UNIT-0225 计算公式；UNIT-0226 计算公式
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0223 | ORIGINAL_TEXT | 计算公式 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0594 |
| UNIT-0224 | ORIGINAL_TEXT | 计算公式 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0599 |
| UNIT-0225 | ORIGINAL_TEXT | 计算公式 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0607 |
| UNIT-0226 | ORIGINAL_TEXT | 计算公式 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0608 |

### SEC-118 水文地质勘探工作 > 水文地质试验 > 压水试验 > 计算结果

- Source locator: P0614
- Material density: 6段关键文字、1张表
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `计算结果` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0227 计算结果；UNIT-0228 计算结果；UNIT-0229 压水试验结果表；UNIT-0230 计算结果；UNIT-0231 计算结果
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_text_right_table or top_text_bottom_table；left_table_right_text or top_text_bottom_table
  - Slide split decision: split or crop tables before reducing font size.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0227 | ORIGINAL_TEXT | 计算结果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0615 |
| UNIT-0228 | CALCULATION | 计算结果 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P0616 |
| UNIT-0229 | ORIGINAL_TABLE | 压水试验结果表 | source table with explanation | left_table_right_text or top_text_bottom_table | 0cc6922b:T027, 0cc6922b:P0617 |
| UNIT-0230 | ORIGINAL_TEXT | 计算结果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0618 |
| UNIT-0231 | ORIGINAL_TEXT | 计算结果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0619 |
| UNIT-0232 | ORIGINAL_TEXT | 计算结果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0620 |
| UNIT-0233 | CALCULATION | 计算结果 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P0621 |

### SEC-121 水文地质勘探工作 > 水文地质试验 > 示踪试验 > 试验原理

- Source locator: P0625
- Material density: 10段关键文字、1张表
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `试验原理` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0234 试验原理；UNIT-0235 试验原理；UNIT-0236 试验原理；UNIT-0237 试验原理；UNIT-0238 试验原理
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_text_right_table or top_text_bottom_table；left_table_right_text
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0234 | ORIGINAL_TEXT | 试验原理 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0626 |
| UNIT-0235 | CALCULATION | 试验原理 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P0627 |
| UNIT-0236 | CALCULATION | 试验原理 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P0628 |
| UNIT-0237 | CALCULATION | 试验原理 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P0629 |
| UNIT-0238 | ORIGINAL_TABLE | 试验原理 | source table with explanation | left_table_right_text | 0cc6922b:T028 |
| UNIT-0239 | ORIGINAL_TEXT | 试验原理 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0630 |
| UNIT-0240 | ORIGINAL_TEXT | 试验原理 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0632 |
| UNIT-0241 | ORIGINAL_TEXT | 试验原理 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0633 |
| UNIT-0242 | ORIGINAL_TEXT | 试验原理 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0634 |
| UNIT-0243 | ORIGINAL_TEXT | 试验原理 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0635 |
| UNIT-0244 | ORIGINAL_TEXT | 试验原理 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0636 |

### SEC-122 水文地质勘探工作 > 水文地质试验 > 示踪试验 > 试验方法

- Source locator: P0637
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `试验方法` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0245 试验方法
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0245 | ORIGINAL_TEXT | 试验方法 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0639 |

### SEC-124 水文地质勘探工作 > 水文地质试验 > 示踪试验 > 试验过程 > 试验部署

- Source locator: P0641
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `试验部署` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0246 试验部署
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0246 | ORIGINAL_TEXT | 试验部署 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0642 |

### SEC-125 水文地质勘探工作 > 水文地质试验 > 示踪试验 > 试验过程 > 第一次示踪试验

- Source locator: P0645
- Material density: 2张表
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `第一次示踪试验` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0247 第一次示踪试验工作部署统计表；UNIT-0248 第一次示踪试验
  - Best source pairing: left_table_right_text or top_text_bottom_table；left_table_right_text
  - Slide split decision: split or crop tables before reducing font size.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0247 | ORIGINAL_TABLE | 第一次示踪试验工作部署统计表 | source table with explanation | left_table_right_text or top_text_bottom_table | 0cc6922b:T029, 0cc6922b:P0650 |
| UNIT-0248 | ORIGINAL_TABLE | 第一次示踪试验 | source table with explanation | left_table_right_text | 0cc6922b:T030 |

### SEC-126 水文地质勘探工作 > 水文地质试验 > 示踪试验 > 试验过程 > 第二次示踪试验

- Source locator: P0652
- Material density: 1段关键文字、2张表
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `第二次示踪试验` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0249 第二次示踪试验；UNIT-0250 第二次示踪试验工作部署统计表；UNIT-0251 第二次示踪试验
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_table_right_text or top_text_bottom_table；left_table_right_text
  - Slide split decision: split or crop tables before reducing font size.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0249 | ORIGINAL_TEXT | 第二次示踪试验 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0653 |
| UNIT-0250 | ORIGINAL_TABLE | 第二次示踪试验工作部署统计表 | source table with explanation | left_table_right_text or top_text_bottom_table | 0cc6922b:T031, 0cc6922b:P0656 |
| UNIT-0251 | ORIGINAL_TABLE | 第二次示踪试验 | source table with explanation | left_table_right_text | 0cc6922b:T032 |

### SEC-127 水文地质勘探工作 > 水文地质试验 > 示踪试验 > 试验结果

- Source locator: P0658
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `试验结果` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0252 试验结果
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0252 | ORIGINAL_TEXT | 试验结果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0659 |

### SEC-129 水文地质勘探工作 > 水文地球化学及同位素分析 > 取样测试与数据整理

- Source locator: P0661
- Material density: 4段关键文字、1张表
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `取样测试与数据整理` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0253 取样测试与数据整理；UNIT-0254 取样测试与数据整理；UNIT-0255 取样测试与数据整理；UNIT-0256 取样测试与数据整理；UNIT-0257 取样点及测试项目表
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_text_right_table or top_text_bottom_table；left_table_right_text or top_text_bottom_table
  - Slide split decision: split or crop tables before reducing font size.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0253 | ORIGINAL_TEXT | 取样测试与数据整理 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0662 |
| UNIT-0254 | ORIGINAL_TEXT | 取样测试与数据整理 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0663 |
| UNIT-0255 | ORIGINAL_TEXT | 取样测试与数据整理 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0667 |
| UNIT-0256 | CALCULATION | 取样测试与数据整理 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P0668 |
| UNIT-0257 | ORIGINAL_TABLE | 取样点及测试项目表 | source table with explanation | left_table_right_text or top_text_bottom_table | 0cc6922b:T033, 0cc6922b:P0669 |

### SEC-131 水文地质勘探工作 > 水文地球化学及同位素分析 > 矿区水化学及同位素特征 > 水化学基本特征

- Source locator: P0671
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `水化学基本特征` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0258 水化学基本特征；UNIT-0259 水化学基本特征
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0258 | ORIGINAL_TEXT | 水化学基本特征 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0672 |
| UNIT-0259 | ORIGINAL_TEXT | 水化学基本特征 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0673 |

### SEC-133 水文地质勘探工作 > 水文地球化学及同位素分析 > 矿区水化学及同位素特征 > 水化学类型特征 > 舒卡列夫分类

- Source locator: P0675
- Material density: 1段关键文字、1张表
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `舒卡列夫分类` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0260 舒卡列夫分类；UNIT-0261 舒卡列夫分类表
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_table_right_text or top_text_bottom_table
  - Slide split decision: split or crop tables before reducing font size.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0260 | ORIGINAL_TEXT | 舒卡列夫分类 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0676 |
| UNIT-0261 | ORIGINAL_TABLE | 舒卡列夫分类表 | source table with explanation | left_table_right_text or top_text_bottom_table | 0cc6922b:T034, 0cc6922b:P0677 |

### SEC-134 水文地质勘探工作 > 水文地球化学及同位素分析 > 矿区水化学及同位素特征 > 水化学类型特征 > Piper三线图

- Source locator: P0678
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `Piper三线图` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0262 Piper三线图；UNIT-0263 Piper三线图
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0262 | ORIGINAL_TEXT | Piper三线图 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0679 |
| UNIT-0263 | ORIGINAL_TEXT | Piper三线图 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0682 |

### SEC-136 水文地质勘探工作 > 水文地球化学及同位素分析 > 矿区水化学及同位素特征 > 水化学形成作用分析 > 水化学成因分析

- Source locator: P0684
- Material density: 3段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `水化学成因分析` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0264 水化学成因分析；UNIT-0265 水化学成因分析；UNIT-0266 水化学成因分析
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_text_right_table or top_text_bottom_table
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0264 | ORIGINAL_TEXT | 水化学成因分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0685 |
| UNIT-0265 | ORIGINAL_TEXT | 水化学成因分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0688 |
| UNIT-0266 | CALCULATION | 水化学成因分析 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P0689 |

### SEC-137 水文地质勘探工作 > 水文地球化学及同位素分析 > 矿区水化学及同位素特征 > 水化学形成作用分析 > 离子比值分析

- Source locator: P0690
- Material density: 6段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `离子比值分析` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0267 离子比值分析；UNIT-0268 离子比值分析；UNIT-0269 离子比值分析；UNIT-0270 离子比值分析；UNIT-0271 离子比值分析
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0267 | ORIGINAL_TEXT | 离子比值分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0691 |
| UNIT-0268 | ORIGINAL_TEXT | 离子比值分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0692 |
| UNIT-0269 | ORIGINAL_TEXT | 离子比值分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0695 |
| UNIT-0270 | ORIGINAL_TEXT | 离子比值分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0697 |
| UNIT-0271 | ORIGINAL_TEXT | 离子比值分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0705 |
| UNIT-0272 | ORIGINAL_TEXT | 离子比值分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0708 |

### SEC-138 水文地质勘探工作 > 水文地球化学及同位素分析 > 矿区水化学及同位素特征 > 氢氧稳定同位素特征分析

- Source locator: P0709
- Material density: 6段关键文字、1张表
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `氢氧稳定同位素特征分析` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0273 氢氧稳定同位素特征分析；UNIT-0274 δD和δ18O含量统计表；UNIT-0275 氢氧稳定同位素特征分析；UNIT-0276 氢氧稳定同位素特征分析；UNIT-0277 氢氧稳定同位素特征分析
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_table_right_text or top_text_bottom_table；left_text_right_table or top_text_bottom_table
  - Slide split decision: split or crop tables before reducing font size.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0273 | ORIGINAL_TEXT | 氢氧稳定同位素特征分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0711 |
| UNIT-0274 | ORIGINAL_TABLE | δD和δ18O含量统计表 | source table with explanation | left_table_right_text or top_text_bottom_table | 0cc6922b:T035, 0cc6922b:P0712 |
| UNIT-0275 | ORIGINAL_TEXT | 氢氧稳定同位素特征分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0713 |
| UNIT-0276 | ORIGINAL_TEXT | 氢氧稳定同位素特征分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0716 |
| UNIT-0277 | ORIGINAL_TEXT | 氢氧稳定同位素特征分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0717 |
| UNIT-0278 | CALCULATION | 氢氧稳定同位素特征分析 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P0718 |
| UNIT-0279 | ORIGINAL_TEXT | 氢氧稳定同位素特征分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0719 |

### SEC-139 水文地质勘探工作 > 水文地球化学及同位素分析 > 矿区水化学及同位素特征 > 小结

- Source locator: P0720
- Material density: 3段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `小结` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0280 小结；UNIT-0281 小结；UNIT-0282 小结
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0280 | ORIGINAL_TEXT | 小结 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0721 |
| UNIT-0281 | ORIGINAL_TEXT | 小结 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0722 |
| UNIT-0282 | ORIGINAL_TEXT | 小结 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0723 |

### SEC-142 矿区水文地质条件 > 矿区地质 > 矿区地层

- Source locator: P0726
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `矿区地层` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0283 矿区地层
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0283 | ORIGINAL_TEXT | 矿区地层 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0729 |

### SEC-143 矿区水文地质条件 > 矿区地质 > 矿区地质构造

- Source locator: P0730
- Material density: 1段关键文字、1张表
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `矿区地质构造` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0284 矿区地质构造；UNIT-0285 基于物探成果的断层构造破碎带汇总表
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_table_right_text
  - Slide split decision: split or crop tables before reducing font size.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0284 | ORIGINAL_TEXT | 矿区地质构造 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0731 |
| UNIT-0285 | ORIGINAL_TABLE | 基于物探成果的断层构造破碎带汇总表 | source table with explanation | left_table_right_text | 0cc6922b:T036, 0cc6922b:P0732 |

### SEC-145 矿区水文地质条件 > 矿区地质 > 矿体地质特征 > 矿体形态、产状

- Source locator: P0736
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `矿体形态、产状` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0286 矿体形态、产状；UNIT-0287 矿体形态、产状
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0286 | ORIGINAL_TEXT | 矿体形态、产状 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0737 |
| UNIT-0287 | ORIGINAL_TEXT | 矿体形态、产状 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0738 |

### SEC-146 矿区水文地质条件 > 矿区地质 > 矿体地质特征 > 规模

- Source locator: P0739
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `规模` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0288 规模
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0288 | ORIGINAL_TEXT | 规模 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0740 |

### SEC-148 矿区水文地质条件 > 矿区地质 > 矿石特征 > 矿石的岩石学特征

- Source locator: P0742
- Material density: 3段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `矿石的岩石学特征` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0289 矿石的岩石学特征；UNIT-0290 矿石的岩石学特征；UNIT-0291 矿石的岩石学特征
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0289 | ORIGINAL_TEXT | 矿石的岩石学特征 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0744 |
| UNIT-0290 | ORIGINAL_TEXT | 矿石的岩石学特征 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0745 |
| UNIT-0291 | ORIGINAL_TEXT | 矿石的岩石学特征 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0746 |

### SEC-149 矿区水文地质条件 > 矿区地质 > 矿石特征 > 矿石化学特征

- Source locator: P0747
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `矿石化学特征` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0292 矿石化学特征
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0292 | ORIGINAL_TEXT | 矿石化学特征 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0748 |

### SEC-150 矿区水文地质条件 > 矿区地质 > 矿石特征 > 矿石放射性

- Source locator: P0749
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `矿石放射性` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0293 矿石放射性；UNIT-0294 矿石放射性
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0293 | ORIGINAL_TEXT | 矿石放射性 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0750 |
| UNIT-0294 | ORIGINAL_TEXT | 矿石放射性 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0751 |

### SEC-153 矿区水文地质条件 > 矿区地质 > 矿石加工技术性能 > 破碎加工工艺流程

- Source locator: P0755
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `破碎加工工艺流程` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0295 破碎加工工艺流程
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0295 | ORIGINAL_TEXT | 破碎加工工艺流程 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0756 |

### SEC-154 矿区水文地质条件 > 矿区地质 > 矿体资源量

- Source locator: P0760
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `矿体资源量` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0296 矿体资源量
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0296 | ORIGINAL_TEXT | 矿体资源量 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0765 |

### SEC-157 矿区水文地质条件 > 矿区水文地质 > 含隔水层 > 松散岩类孔隙水含水层

- Source locator: P0769
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `松散岩类孔隙水含水层` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0297 松散岩类孔隙水含水层
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0297 | ORIGINAL_TEXT | 松散岩类孔隙水含水层 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0770 |

### SEC-158 矿区水文地质条件 > 矿区水文地质 > 含隔水层 > 碳酸盐岩类裂隙溶洞水含水层

- Source locator: P0771
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `碳酸盐岩类裂隙溶洞水含水层` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0298 碳酸盐岩类裂隙溶洞水含水层
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0298 | ORIGINAL_TEXT | 碳酸盐岩类裂隙溶洞水含水层 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0772 |

### SEC-160 矿区水文地质条件 > 矿区水文地质 > 岩溶发育特征 > 可溶岩的分布与埋藏条件

- Source locator: P0774
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `可溶岩的分布与埋藏条件` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0299 可溶岩的分布与埋藏条件；UNIT-0300 可溶岩的分布与埋藏条件
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0299 | ORIGINAL_TEXT | 可溶岩的分布与埋藏条件 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0775 |
| UNIT-0300 | ORIGINAL_TEXT | 可溶岩的分布与埋藏条件 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0776 |

### SEC-161 矿区水文地质条件 > 矿区水文地质 > 岩溶发育特征 > 可溶岩岩溶发育特征

- Source locator: P0777
- Material density: 30段关键文字、5张表
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `可溶岩岩溶发育特征` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0301 可溶岩岩溶发育特征；UNIT-0302 可溶岩岩溶发育特征；UNIT-0303 可溶岩岩溶发育特征；UNIT-0304 可溶岩岩溶发育特征；UNIT-0305 可溶岩岩溶发育特征
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_table_right_text；left_table_right_text or top_text_bottom_table
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0301 | ORIGINAL_TEXT | 可溶岩岩溶发育特征 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0778 |
| UNIT-0302 | ORIGINAL_TABLE | 可溶岩岩溶发育特征 | source table with explanation | left_table_right_text | 0cc6922b:T037 |
| UNIT-0303 | ORIGINAL_TEXT | 可溶岩岩溶发育特征 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0781 |
| UNIT-0304 | ORIGINAL_TABLE | 可溶岩岩溶发育特征 | source table with explanation | left_table_right_text | 0cc6922b:T038 |
| UNIT-0305 | ORIGINAL_TABLE | 可溶岩岩溶发育特征 | source table with explanation | left_table_right_text | 0cc6922b:T039 |
| UNIT-0306 | ORIGINAL_TEXT | 可溶岩岩溶发育特征 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0783 |
| UNIT-0307 | ORIGINAL_TABLE | 可溶岩岩溶发育特征 | source table with explanation | left_table_right_text | 0cc6922b:T040 |
| UNIT-0308 | ORIGINAL_TEXT | 可溶岩岩溶发育特征 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0785 |
| UNIT-0309 | ORIGINAL_TEXT | 可溶岩岩溶发育特征 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0795 |
| UNIT-0310 | ORIGINAL_TABLE | 本次施工钻孔岩溶发育高度统计表 | source table with explanation | left_table_right_text or top_text_bottom_table | 0cc6922b:T041, 0cc6922b:P0796 |
| UNIT-0311 | ORIGINAL_TEXT | 可溶岩岩溶发育特征 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0797 |
| UNIT-0312 | ORIGINAL_TEXT | 可溶岩岩溶发育特征 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0798 |
| ... | ... | Additional 23 units in JSON inventory | ... | ... | ... |

### SEC-162 矿区水文地质条件 > 矿区水文地质 > 岩溶发育特征 > 岩溶发育规律控制因素分析

- Source locator: P0856
- Material density: 21段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `岩溶发育规律控制因素分析` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0336 岩溶发育规律控制因素分析；UNIT-0337 岩溶发育规律控制因素分析；UNIT-0338 岩溶发育规律控制因素分析；UNIT-0339 岩溶发育规律控制因素分析；UNIT-0340 岩溶发育规律控制因素分析
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0336 | ORIGINAL_TEXT | 岩溶发育规律控制因素分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0857 |
| UNIT-0337 | ORIGINAL_TEXT | 岩溶发育规律控制因素分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0858 |
| UNIT-0338 | ORIGINAL_TEXT | 岩溶发育规律控制因素分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0859 |
| UNIT-0339 | ORIGINAL_TEXT | 岩溶发育规律控制因素分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0860 |
| UNIT-0340 | ORIGINAL_TEXT | 岩溶发育规律控制因素分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0861 |
| UNIT-0341 | ORIGINAL_TEXT | 岩溶发育规律控制因素分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0862 |
| UNIT-0342 | ORIGINAL_TEXT | 岩溶发育规律控制因素分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0863 |
| UNIT-0343 | ORIGINAL_TEXT | 岩溶发育规律控制因素分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0864 |
| UNIT-0344 | ORIGINAL_TEXT | 岩溶发育规律控制因素分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0865 |
| UNIT-0345 | ORIGINAL_TEXT | 岩溶发育规律控制因素分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0866 |
| UNIT-0346 | ORIGINAL_TEXT | 岩溶发育规律控制因素分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0867 |
| UNIT-0347 | ORIGINAL_TEXT | 岩溶发育规律控制因素分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0869 |
| ... | ... | Additional 9 units in JSON inventory | ... | ... | ... |

### SEC-163 矿区水文地质条件 > 矿区水文地质 > 矿区强径流带特征

- Source locator: P0879
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `矿区强径流带特征` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0357 矿区强径流带特征；UNIT-0358 矿区强径流带特征
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_text_right_table or top_text_bottom_table
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0357 | ORIGINAL_TEXT | 矿区强径流带特征 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0880 |
| UNIT-0358 | CALCULATION | 矿区强径流带特征 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P0881 |

### SEC-164 矿区水文地质条件 > 矿区水文地质 > 矿区强径流带特征 > 强径流带

- Source locator: P0882
- Material density: 9段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `强径流带` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0359 强径流带；UNIT-0360 强径流带；UNIT-0361 强径流带；UNIT-0362 强径流带；UNIT-0363 强径流带
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0359 | ORIGINAL_TEXT | 强径流带 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0883 |
| UNIT-0360 | ORIGINAL_TEXT | 强径流带 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0886 |
| UNIT-0361 | ORIGINAL_TEXT | 强径流带 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0887 |
| UNIT-0362 | ORIGINAL_TEXT | 强径流带 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0896 |
| UNIT-0363 | ORIGINAL_TEXT | 强径流带 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0897 |
| UNIT-0364 | ORIGINAL_TEXT | 强径流带 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0905 |
| UNIT-0365 | ORIGINAL_TEXT | 强径流带 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0906 |
| UNIT-0366 | ORIGINAL_TEXT | 强径流带 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0910 |
| UNIT-0367 | ORIGINAL_TEXT | 强径流带 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0911 |

### SEC-165 矿区水文地质条件 > 矿区水文地质 > 矿区强径流带特征 > 中等径流带

- Source locator: P0920
- Material density: 8段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `中等径流带` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0368 中等径流带；UNIT-0369 中等径流带；UNIT-0370 中等径流带；UNIT-0371 中等径流带；UNIT-0372 中等径流带
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0368 | ORIGINAL_TEXT | 中等径流带 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0921 |
| UNIT-0369 | ORIGINAL_TEXT | 中等径流带 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0922 |
| UNIT-0370 | ORIGINAL_TEXT | 中等径流带 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0931 |
| UNIT-0371 | ORIGINAL_TEXT | 中等径流带 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0932 |
| UNIT-0372 | ORIGINAL_TEXT | 中等径流带 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0940 |
| UNIT-0373 | ORIGINAL_TEXT | 中等径流带 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0941 |
| UNIT-0374 | ORIGINAL_TEXT | 中等径流带 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0949 |
| UNIT-0375 | ORIGINAL_TEXT | 中等径流带 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0950 |

### SEC-166 矿区水文地质条件 > 矿区水文地质 > 地下水补径排特征

- Source locator: P0957
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `地下水补径排特征` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0376 地下水补径排特征
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0376 | ORIGINAL_TEXT | 地下水补径排特征 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0958 |

### SEC-167 矿区水文地质条件 > 矿区水文地质 > 地下水补径排特征 > 地下水补给特征及边界来水通道

- Source locator: P0959
- Material density: 5段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `地下水补给特征及边界来水通道` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0377 地下水补给特征及边界来水通道；UNIT-0378 地下水补给特征及边界来水通道；UNIT-0379 地下水补给特征及边界来水通道；UNIT-0380 地下水补给特征及边界来水通道；UNIT-0381 地下水补给特征及边界来水通道
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0377 | ORIGINAL_TEXT | 地下水补给特征及边界来水通道 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0960 |
| UNIT-0378 | ORIGINAL_TEXT | 地下水补给特征及边界来水通道 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0961 |
| UNIT-0379 | ORIGINAL_TEXT | 地下水补给特征及边界来水通道 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0962 |
| UNIT-0380 | ORIGINAL_TEXT | 地下水补给特征及边界来水通道 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0963 |
| UNIT-0381 | ORIGINAL_TEXT | 地下水补给特征及边界来水通道 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0964 |

### SEC-168 矿区水文地质条件 > 矿区水文地质 > 地下水补径排特征 > 地下水径流特征

- Source locator: P0965
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `地下水径流特征` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0382 地下水径流特征；UNIT-0383 地下水径流特征
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0382 | ORIGINAL_TEXT | 地下水径流特征 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0967 |
| UNIT-0383 | ORIGINAL_TEXT | 地下水径流特征 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0968 |

### SEC-169 矿区水文地质条件 > 矿区水文地质 > 地下水补径排特征 > 地下水排泄特征及出口通道

- Source locator: P0969
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `地下水排泄特征及出口通道` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0384 地下水排泄特征及出口通道
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0384 | ORIGINAL_TEXT | 地下水排泄特征及出口通道 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0970 |

### SEC-170 矿区水文地质条件 > 矿区水文地质 > 地下水补径排特征 > 地下水补径排关系总结

- Source locator: P0971
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `地下水补径排关系总结` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0385 地下水补径排关系总结
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0385 | ORIGINAL_TEXT | 地下水补径排关系总结 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0972 |

### SEC-172 矿区水文地质条件 > 矿区水文地质 > 地下水动态特征 > 现状地下水水位

- Source locator: P0974
- Material density: 4段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `现状地下水水位` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0386 现状地下水水位；UNIT-0387 现状地下水水位；UNIT-0388 现状地下水水位；UNIT-0389 现状地下水水位
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0386 | ORIGINAL_TEXT | 现状地下水水位 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0975 |
| UNIT-0387 | ORIGINAL_TEXT | 现状地下水水位 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0976 |
| UNIT-0388 | ORIGINAL_TEXT | 现状地下水水位 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0977 |
| UNIT-0389 | ORIGINAL_TEXT | 现状地下水水位 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0978 |

### SEC-173 矿区水文地质条件 > 矿区水文地质 > 地下水动态特征 > 长期地下水位动态观测

- Source locator: P0982
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `长期地下水位动态观测` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0390 长期地下水位动态观测；UNIT-0391 长期地下水位动态观测
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0390 | ORIGINAL_TEXT | 长期地下水位动态观测 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0983 |
| UNIT-0391 | ORIGINAL_TEXT | 长期地下水位动态观测 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0990 |

### SEC-174 矿区水文地质条件 > 矿区水文地质 > 涌水量动态特征

- Source locator: P0991
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `涌水量动态特征` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0392 涌水量动态特征
  - Best source pairing: left_text_right_table or top_text_bottom_table
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0392 | CALCULATION | 涌水量动态特征 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P0992 |

### SEC-176 矿区水文地质条件 > 矿区充水条件分析 > 大气降水

- Source locator: P0996
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `大气降水` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0393 大气降水
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0393 | ORIGINAL_TEXT | 大气降水 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P0998 |

### SEC-177 矿区水文地质条件 > 矿区充水条件分析 > 地表水

- Source locator: P1000
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `地表水` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0394 地表水
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0394 | ORIGINAL_TEXT | 地表水 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1001 |

### SEC-179 矿区水文地质条件 > 矿区充水条件分析 > 地下水 > 第四系残坡积层孔隙水

- Source locator: P1003
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `第四系残坡积层孔隙水` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0395 第四系残坡积层孔隙水
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0395 | ORIGINAL_TEXT | 第四系残坡积层孔隙水 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1004 |

### SEC-180 矿区水文地质条件 > 矿区充水条件分析 > 地下水 > 石炭系碳酸盐岩裂隙溶洞水

- Source locator: P1005
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `石炭系碳酸盐岩裂隙溶洞水` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0396 石炭系碳酸盐岩裂隙溶洞水
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0396 | ORIGINAL_TEXT | 石炭系碳酸盐岩裂隙溶洞水 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1006 |

### SEC-181 矿区水文地质条件 > 矿区水文地质勘查类型

- Source locator: P1007
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `矿区水文地质勘查类型` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0397 矿区水文地质勘查类型；UNIT-0398 矿区水文地质勘查类型
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0397 | ORIGINAL_TEXT | 矿区水文地质勘查类型 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1008 |
| UNIT-0398 | ORIGINAL_TEXT | 矿区水文地质勘查类型 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1009 |

### SEC-183 矿段涌突水影响因素评价 > 涌突水影响因素分析

- Source locator: P1012
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `涌突水影响因素分析` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0399 涌突水影响因素分析
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0399 | ORIGINAL_TEXT | 涌突水影响因素分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1013 |

### SEC-184 矿段涌突水影响因素评价 > 涌突水影响因素分析 > 大气降水对矿段涌水量的影响

- Source locator: P1014
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `大气降水对矿段涌水量的影响` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0400 大气降水对矿段涌水量的影响
  - Best source pairing: left_text_right_table or top_text_bottom_table
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0400 | CALCULATION | 大气降水对矿段涌水量的影响 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P1015 |

### SEC-185 矿段涌突水影响因素评价 > 涌突水影响因素分析 > 地表水对矿段涌水的影响

- Source locator: P1016
- Material density: 3段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `地表水对矿段涌水的影响` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0401 地表水对矿段涌水的影响；UNIT-0402 地表水对矿段涌水的影响；UNIT-0403 地表水对矿段涌水的影响
  - Best source pairing: left_text_right_table or top_text_bottom_table；left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0401 | CALCULATION | 地表水对矿段涌水的影响 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P1017 |
| UNIT-0402 | ORIGINAL_TEXT | 地表水对矿段涌水的影响 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1018 |
| UNIT-0403 | ORIGINAL_TEXT | 地表水对矿段涌水的影响 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1019 |

### SEC-186 矿段涌突水影响因素评价 > 涌突水影响因素分析 > 构造对矿段涌突水的影响

- Source locator: P1020
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `构造对矿段涌突水的影响` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0404 构造对矿段涌突水的影响
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0404 | ORIGINAL_TEXT | 构造对矿段涌突水的影响 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1021 |

### SEC-188 矿段涌突水影响因素评价 > 涌突水影响因素分析 > 岩溶发育对矿段涌水的影响 > 平面岩溶非均质性对涌突水的影响

- Source locator: P1024
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `平面岩溶非均质性对涌突水的影响` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0405 平面岩溶非均质性对涌突水的影响
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0405 | ORIGINAL_TEXT | 平面岩溶非均质性对涌突水的影响 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1025 |

### SEC-189 矿段涌突水影响因素评价 > 涌突水影响因素分析 > 岩溶发育对矿段涌水的影响 > 垂向岩溶分带性对涌突水的影响

- Source locator: P1026
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `垂向岩溶分带性对涌突水的影响` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0406 垂向岩溶分带性对涌突水的影响
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0406 | ORIGINAL_TEXT | 垂向岩溶分带性对涌突水的影响 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1027 |

### SEC-190 矿段涌突水影响因素评价 > 涌突水影响因素分析 > 小结

- Source locator: P1028
- Material density: 5段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `小结` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0407 小结；UNIT-0408 小结；UNIT-0409 小结；UNIT-0410 小结；UNIT-0411 小结
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0407 | ORIGINAL_TEXT | 小结 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1029 |
| UNIT-0408 | ORIGINAL_TEXT | 小结 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1030 |
| UNIT-0409 | ORIGINAL_TEXT | 小结 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1031 |
| UNIT-0410 | ORIGINAL_TEXT | 小结 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1032 |
| UNIT-0411 | ORIGINAL_TEXT | 小结 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1033 |

### SEC-191 矿段涌突水影响因素评价 > 含水层富水性评价与分区

- Source locator: P1034
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `含水层富水性评价与分区` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0412 含水层富水性评价与分区
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0412 | ORIGINAL_TEXT | 含水层富水性评价与分区 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1035 |

### SEC-192 矿段涌突水影响因素评价 > 含水层富水性评价与分区 > 主控因素专题图

- Source locator: P1036
- Material density: 8段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `主控因素专题图` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0413 主控因素专题图；UNIT-0414 主控因素专题图；UNIT-0415 主控因素专题图；UNIT-0416 主控因素专题图；UNIT-0417 主控因素专题图
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0413 | ORIGINAL_TEXT | 主控因素专题图 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1045 |
| UNIT-0414 | ORIGINAL_TEXT | 主控因素专题图 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1046 |
| UNIT-0415 | ORIGINAL_TEXT | 主控因素专题图 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1047 |
| UNIT-0416 | ORIGINAL_TEXT | 主控因素专题图 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1048 |
| UNIT-0417 | ORIGINAL_TEXT | 主控因素专题图 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1049 |
| UNIT-0418 | ORIGINAL_TEXT | 主控因素专题图 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1050 |
| UNIT-0419 | ORIGINAL_TEXT | 主控因素专题图 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1051 |
| UNIT-0420 | ORIGINAL_TEXT | 主控因素专题图 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1052 |

### SEC-193 矿段涌突水影响因素评价 > 含水层富水性评价与分区 > 富水性分区

- Source locator: P1053
- Material density: 13段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `富水性分区` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0421 富水性分区；UNIT-0422 富水性分区；UNIT-0423 富水性分区；UNIT-0424 富水性分区；UNIT-0425 富水性分区
  - Best source pairing: left_text_right_table or top_text_bottom_table；left_text_right_figure or text_with_keypoints
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0421 | CALCULATION | 富水性分区 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P1054 |
| UNIT-0422 | ORIGINAL_TEXT | 富水性分区 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1055 |
| UNIT-0423 | CALCULATION | 富水性分区 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P1057 |
| UNIT-0424 | CALCULATION | 富水性分区 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P1058 |
| UNIT-0425 | ORIGINAL_TEXT | 富水性分区 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1059 |
| UNIT-0426 | CALCULATION | 富水性分区 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P1061 |
| UNIT-0427 | ORIGINAL_TEXT | 富水性分区 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1062 |
| UNIT-0428 | ORIGINAL_TEXT | 富水性分区 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1066 |
| UNIT-0429 | ORIGINAL_TEXT | 富水性分区 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1067 |
| UNIT-0430 | ORIGINAL_TEXT | 富水性分区 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1068 |
| UNIT-0431 | ORIGINAL_TEXT | 富水性分区 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1069 |
| UNIT-0432 | ORIGINAL_TEXT | 富水性分区 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1070 |
| ... | ... | Additional 1 units in JSON inventory | ... | ... | ... |

### SEC-196 矿坑涌水量预测 > 水文地质概念模型 > 模型范围

- Source locator: P1077
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `模型范围` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0434 模型范围
  - Best source pairing: left_text_right_table or top_text_bottom_table
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0434 | CALCULATION | 模型范围 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P1078 |

### SEC-197 矿坑涌水量预测 > 水文地质概念模型 > 模型概化

- Source locator: P1081
- Material density: 7段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `模型概化` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0435 模型概化；UNIT-0436 模型概化；UNIT-0437 模型概化；UNIT-0438 模型概化；UNIT-0439 模型概化
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_text_right_table or top_text_bottom_table
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0435 | ORIGINAL_TEXT | 模型概化 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1082 |
| UNIT-0436 | ORIGINAL_TEXT | 模型概化 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1083 |
| UNIT-0437 | ORIGINAL_TEXT | 模型概化 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1084 |
| UNIT-0438 | ORIGINAL_TEXT | 模型概化 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1085 |
| UNIT-0439 | CALCULATION | 模型概化 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P1086 |
| UNIT-0440 | ORIGINAL_TEXT | 模型概化 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1087 |
| UNIT-0441 | ORIGINAL_TEXT | 模型概化 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1088 |

### SEC-198 矿坑涌水量预测 > 水文地质概念模型 > 模型边界概化

- Source locator: P1089
- Material density: 6段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `模型边界概化` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0442 模型边界概化；UNIT-0443 模型边界概化；UNIT-0444 模型边界概化；UNIT-0445 模型边界概化；UNIT-0446 模型边界概化
  - Best source pairing: left_text_right_table or top_text_bottom_table
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0442 | CALCULATION | 模型边界概化 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P1090 |
| UNIT-0443 | CALCULATION | 模型边界概化 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P1091 |
| UNIT-0444 | CALCULATION | 模型边界概化 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P1092 |
| UNIT-0445 | CALCULATION | 模型边界概化 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P1093 |
| UNIT-0446 | CALCULATION | 模型边界概化 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P1094 |
| UNIT-0447 | CALCULATION | 模型边界概化 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P1095 |

### SEC-199 矿坑涌水量预测 > 水文地质比拟法预测矿坑涌水量

- Source locator: P1099
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `水文地质比拟法预测矿坑涌水量` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0448 水文地质比拟法预测矿坑涌水量
  - Best source pairing: left_text_right_table or top_text_bottom_table
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0448 | CALCULATION | 水文地质比拟法预测矿坑涌水量 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P1100 |

### SEC-200 矿坑涌水量预测 > 水文地质比拟法预测矿坑涌水量 > 地表水汇入采坑水量计算

- Source locator: P1101
- Material density: 5段关键文字、2张表
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `地表水汇入采坑水量计算` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0449 地表水汇入采坑水量计算；UNIT-0450 地表水汇入采坑水量计算；UNIT-0451 参数取值表；UNIT-0452 近30年的降水数据统计表；UNIT-0453 地表水汇入采坑水量计算
  - Best source pairing: left_text_right_table or top_text_bottom_table；left_text_right_figure or text_with_keypoints；left_table_right_text
  - Slide split decision: split or crop tables before reducing font size.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0449 | CALCULATION | 地表水汇入采坑水量计算 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P1102 |
| UNIT-0450 | ORIGINAL_TEXT | 地表水汇入采坑水量计算 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1103 |
| UNIT-0451 | ORIGINAL_TABLE | 参数取值表 | source table with explanation | left_table_right_text | 0cc6922b:T042, 0cc6922b:P1109 |
| UNIT-0452 | ORIGINAL_TABLE | 近30年的降水数据统计表 | source table with explanation | left_table_right_text or top_text_bottom_table | 0cc6922b:T043, 0cc6922b:P1110 |
| UNIT-0453 | CALCULATION | 地表水汇入采坑水量计算 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P1111 |
| UNIT-0454 | ORIGINAL_TEXT | 地表水汇入采坑水量计算 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1112 |
| UNIT-0455 | ORIGINAL_TEXT | 地表水汇入采坑水量计算 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1113 |

### SEC-201 矿坑涌水量预测 > 水文地质比拟法预测矿坑涌水量 > 降水渗入采坑水量计算

- Source locator: P1115
- Material density: 20段关键文字、5张表
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `降水渗入采坑水量计算` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0456 降水渗入采坑水量计算；UNIT-0457 降水渗入采坑水量计算；UNIT-0458 降水渗入采坑水量计算；UNIT-0459 参数取值表；UNIT-0460 不同开采标高的露天采坑底面积
  - Best source pairing: left_text_right_table or top_text_bottom_table；left_text_right_figure or text_with_keypoints；left_table_right_text
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0456 | CALCULATION | 降水渗入采坑水量计算 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P1116 |
| UNIT-0457 | CALCULATION | 降水渗入采坑水量计算 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P1117 |
| UNIT-0458 | ORIGINAL_TEXT | 降水渗入采坑水量计算 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1119 |
| UNIT-0459 | ORIGINAL_TABLE | 参数取值表 | source table with explanation | left_table_right_text | 0cc6922b:T044, 0cc6922b:P1124 |
| UNIT-0460 | ORIGINAL_TABLE | 不同开采标高的露天采坑底面积 | source table with explanation | left_table_right_text | 0cc6922b:T045, 0cc6922b:P1125 |
| UNIT-0461 | CALCULATION | 降水渗入采坑水量计算 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P1126 |
| UNIT-0462 | ORIGINAL_TABLE | 计算结果表 | source table with explanation | left_table_right_text | 0cc6922b:T046, 0cc6922b:P1127 |
| UNIT-0463 | ORIGINAL_TEXT | 降水渗入采坑水量计算 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1129 |
| UNIT-0464 | ORIGINAL_TEXT | 降水渗入采坑水量计算 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1131 |
| UNIT-0465 | ORIGINAL_TEXT | 降水渗入采坑水量计算 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1133 |
| UNIT-0466 | CALCULATION | 降水渗入采坑水量计算 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P1134 |
| UNIT-0467 | ORIGINAL_TEXT | 降水渗入采坑水量计算 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1136 |
| ... | ... | Additional 13 units in JSON inventory | ... | ... | ... |

### SEC-202 矿坑涌水量预测 > 水文地质比拟法预测矿坑涌水量 > 露天采坑地下水涌水量的比拟计算

- Source locator: P1162
- Material density: 3段关键文字、2张表
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `露天采坑地下水涌水量的比拟计算` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0481 露天采坑地下水涌水量的比拟计算；UNIT-0482 露天采坑地下水涌水量的比拟计算；UNIT-0483 参数取值表；UNIT-0484 露天采坑地下水涌水量的比拟计算；UNIT-0485 计算结果表
  - Best source pairing: left_text_right_table or top_text_bottom_table；left_text_right_figure or text_with_keypoints；left_table_right_text
  - Slide split decision: split or crop tables before reducing font size.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0481 | CALCULATION | 露天采坑地下水涌水量的比拟计算 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P1163 |
| UNIT-0482 | ORIGINAL_TEXT | 露天采坑地下水涌水量的比拟计算 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1164 |
| UNIT-0483 | ORIGINAL_TABLE | 参数取值表 | source table with explanation | left_table_right_text | 0cc6922b:T049, 0cc6922b:P1172 |
| UNIT-0484 | CALCULATION | 露天采坑地下水涌水量的比拟计算 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P1174 |
| UNIT-0485 | ORIGINAL_TABLE | 计算结果表 | source table with explanation | left_table_right_text | 0cc6922b:T050, 0cc6922b:P1175 |

### SEC-203 矿坑涌水量预测 > 水文地质比拟法预测矿坑涌水量 > 露天矿矿坑总涌水量

- Source locator: P1185
- Material density: 3段关键文字、1张表
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `露天矿矿坑总涌水量` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0486 露天矿矿坑总涌水量计算结果总表；UNIT-0487 露天矿矿坑总涌水量；UNIT-0488 露天矿矿坑总涌水量；UNIT-0489 露天矿矿坑总涌水量
  - Best source pairing: left_table_right_text or top_text_bottom_table；left_text_right_figure or text_with_keypoints
  - Slide split decision: split or crop tables before reducing font size.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0486 | ORIGINAL_TABLE | 露天矿矿坑总涌水量计算结果总表 | source table with explanation | left_table_right_text or top_text_bottom_table | 0cc6922b:T051, 0cc6922b:P1187 |
| UNIT-0487 | ORIGINAL_TEXT | 露天矿矿坑总涌水量 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1188 |
| UNIT-0488 | ORIGINAL_TEXT | 露天矿矿坑总涌水量 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1189 |
| UNIT-0489 | ORIGINAL_TEXT | 露天矿矿坑总涌水量 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1190 |

### SEC-205 矿坑涌水量预测 > 解析法预测矿坑涌水量 > 计算公式的选取

- Source locator: P1192
- Material density: 4段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `计算公式的选取` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0490 计算公式的选取；UNIT-0491 计算公式的选取；UNIT-0492 计算公式的选取；UNIT-0493 计算公式的选取
  - Best source pairing: left_text_right_table or top_text_bottom_table；left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0490 | CALCULATION | 计算公式的选取 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P1193 |
| UNIT-0491 | ORIGINAL_TEXT | 计算公式的选取 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1194 |
| UNIT-0492 | ORIGINAL_TEXT | 计算公式的选取 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1195 |
| UNIT-0493 | CALCULATION | 计算公式的选取 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P1196 |

### SEC-206 矿坑涌水量预测 > 解析法预测矿坑涌水量 > 水文地质参数的选取

- Source locator: P1197
- Material density: 7段关键文字、1张表
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `水文地质参数的选取` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0494 水文地质参数的选取；UNIT-0495 水文地质参数的选取；UNIT-0496 水文地质参数的选取；UNIT-0497 水文地质参数的选取；UNIT-0498 水文地质参数的选取
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_text_right_table or top_text_bottom_table；left_table_right_text
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0494 | ORIGINAL_TEXT | 水文地质参数的选取 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1198 |
| UNIT-0495 | ORIGINAL_TEXT | 水文地质参数的选取 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1200 |
| UNIT-0496 | ORIGINAL_TEXT | 水文地质参数的选取 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1202 |
| UNIT-0497 | ORIGINAL_TEXT | 水文地质参数的选取 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1205 |
| UNIT-0498 | ORIGINAL_TEXT | 水文地质参数的选取 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1207 |
| UNIT-0499 | CALCULATION | 水文地质参数的选取 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P1208 |
| UNIT-0500 | CALCULATION | 水文地质参数的选取 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P1209 |
| UNIT-0501 | ORIGINAL_TABLE | “大井法”计算参数表 | source table with explanation | left_table_right_text | 0cc6922b:T052, 0cc6922b:P1210 |

### SEC-207 矿坑涌水量预测 > 解析法预测矿坑涌水量 > 解析法预测矿坑涌水量结果

- Source locator: P1211
- Material density: 4段关键文字、1张表
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `解析法预测矿坑涌水量结果` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0502 解析法预测矿坑涌水量结果；UNIT-0503 利用解析法预测矿坑涌水量计算结果；UNIT-0504 解析法预测矿坑涌水量结果；UNIT-0505 解析法预测矿坑涌水量结果；UNIT-0506 解析法预测矿坑涌水量结果
  - Best source pairing: left_text_right_table or top_text_bottom_table；left_table_right_text；left_text_right_figure or text_with_keypoints
  - Slide split decision: split or crop tables before reducing font size.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0502 | CALCULATION | 解析法预测矿坑涌水量结果 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P1212 |
| UNIT-0503 | ORIGINAL_TABLE | 利用解析法预测矿坑涌水量计算结果 | source table with explanation | left_table_right_text | 0cc6922b:T053, 0cc6922b:P1213 |
| UNIT-0504 | ORIGINAL_TEXT | 解析法预测矿坑涌水量结果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1214 |
| UNIT-0505 | ORIGINAL_TEXT | 解析法预测矿坑涌水量结果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1215 |
| UNIT-0506 | ORIGINAL_TEXT | 解析法预测矿坑涌水量结果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1216 |

### SEC-208 矿坑涌水量预测 > 数值法预测矿坑涌水量

- Source locator: P1217
- Material density: 4段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `数值法预测矿坑涌水量` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0507 数值法预测矿坑涌水量；UNIT-0508 数值法预测矿坑涌水量；UNIT-0509 数值法预测矿坑涌水量；UNIT-0510 数值法预测矿坑涌水量
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0507 | ORIGINAL_TEXT | 数值法预测矿坑涌水量 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1228 |
| UNIT-0508 | ORIGINAL_TEXT | 数值法预测矿坑涌水量 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1229 |
| UNIT-0509 | ORIGINAL_TEXT | 数值法预测矿坑涌水量 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1230 |
| UNIT-0510 | ORIGINAL_TEXT | 数值法预测矿坑涌水量 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1231 |

### SEC-209 矿坑涌水量预测 > 数值法预测矿坑涌水量 > 初始网格及地质模型

- Source locator: P1235
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `初始网格及地质模型` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0511 初始网格及地质模型；UNIT-0512 初始网格及地质模型
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_text_right_table or top_text_bottom_table
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0511 | ORIGINAL_TEXT | 初始网格及地质模型 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1236 |
| UNIT-0512 | CALCULATION | 初始网格及地质模型 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P1240 |

### SEC-210 矿坑涌水量预测 > 数值法预测矿坑涌水量 > 边界条件及初始参数

- Source locator: P1243
- Material density: 6段关键文字、1张表
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `边界条件及初始参数` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0513 边界条件及初始参数；UNIT-0514 边界条件及初始参数；UNIT-0515 边界条件及初始参数；UNIT-0516 边界条件及初始参数；UNIT-0517 边界条件及初始参数
  - Best source pairing: left_text_right_table or top_text_bottom_table；left_text_right_figure or text_with_keypoints；left_table_right_text
  - Slide split decision: split or crop tables before reducing font size.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0513 | CALCULATION | 边界条件及初始参数 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P1244 |
| UNIT-0514 | CALCULATION | 边界条件及初始参数 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P1246 |
| UNIT-0515 | ORIGINAL_TEXT | 边界条件及初始参数 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1248 |
| UNIT-0516 | ORIGINAL_TEXT | 边界条件及初始参数 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1249 |
| UNIT-0517 | ORIGINAL_TEXT | 边界条件及初始参数 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1250 |
| UNIT-0518 | CALCULATION | 边界条件及初始参数 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P1251 |
| UNIT-0519 | ORIGINAL_TABLE | 模拟区水文地质初始参数取值表 | source table with explanation | left_table_right_text | 0cc6922b:T054, 0cc6922b:P1252 |

### SEC-211 矿坑涌水量预测 > 数值法预测矿坑涌水量 > 识别验证与初始条件

- Source locator: P1253
- Material density: 9段关键文字、1张表
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `识别验证与初始条件` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0520 识别验证与初始条件；UNIT-0521 识别验证与初始条件；UNIT-0522 识别验证与初始条件；UNIT-0523 识别验证与初始条件；UNIT-0524 参数取值表
  - Best source pairing: left_text_right_table or top_text_bottom_table；left_text_right_figure or text_with_keypoints；left_table_right_text
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0520 | CALCULATION | 识别验证与初始条件 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P1254 |
| UNIT-0521 | CALCULATION | 识别验证与初始条件 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P1255 |
| UNIT-0522 | ORIGINAL_TEXT | 识别验证与初始条件 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1258 |
| UNIT-0523 | CALCULATION | 识别验证与初始条件 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P1259 |
| UNIT-0524 | ORIGINAL_TABLE | 参数取值表 | source table with explanation | left_table_right_text | 0cc6922b:T055, 0cc6922b:P1260 |
| UNIT-0525 | ORIGINAL_TEXT | 识别验证与初始条件 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1264 |
| UNIT-0526 | ORIGINAL_TEXT | 识别验证与初始条件 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1266 |
| UNIT-0527 | ORIGINAL_TEXT | 识别验证与初始条件 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1268 |
| UNIT-0528 | CALCULATION | 识别验证与初始条件 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P1269 |
| UNIT-0529 | ORIGINAL_TEXT | 识别验证与初始条件 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1270 |

### SEC-212 矿坑涌水量预测 > 数值法预测矿坑涌水量 > 数值法预测矿坑涌水量结果

- Source locator: P1273
- Material density: 5段关键文字、2张表
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `数值法预测矿坑涌水量结果` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0530 数值法预测矿坑涌水量结果；UNIT-0531 数值法预测矿坑涌水量结果；UNIT-0532 数值法预测矿坑涌水量结果；UNIT-0533 平台坑底面积和水位降深；UNIT-0534 数值法预测矿坑涌水量结果
  - Best source pairing: left_text_right_table or top_text_bottom_table；left_table_right_text
  - Slide split decision: split or crop tables before reducing font size.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0530 | CALCULATION | 数值法预测矿坑涌水量结果 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P1274 |
| UNIT-0531 | CALCULATION | 数值法预测矿坑涌水量结果 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P1275 |
| UNIT-0532 | CALCULATION | 数值法预测矿坑涌水量结果 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P1276 |
| UNIT-0533 | ORIGINAL_TABLE | 平台坑底面积和水位降深 | source table with explanation | left_table_right_text | 0cc6922b:T056, 0cc6922b:P1282 |
| UNIT-0534 | CALCULATION | 数值法预测矿坑涌水量结果 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P1283 |
| UNIT-0535 | ORIGINAL_TABLE | 数值法计算正常涌水量及最大涌水量 | source table with explanation | left_table_right_text | 0cc6922b:T057, 0cc6922b:P1284 |
| UNIT-0536 | CALCULATION | 数值法预测矿坑涌水量结果 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P1285 |

### SEC-213 矿坑涌水量预测 > 预测成果分析

- Source locator: P1286
- Material density: 7段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `预测成果分析` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0537 预测成果分析；UNIT-0538 预测成果分析；UNIT-0539 预测成果分析；UNIT-0540 预测成果分析；UNIT-0541 预测成果分析
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_text_right_table or top_text_bottom_table
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0537 | ORIGINAL_TEXT | 预测成果分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1287 |
| UNIT-0538 | CALCULATION | 预测成果分析 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P1288 |
| UNIT-0539 | ORIGINAL_TEXT | 预测成果分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1289 |
| UNIT-0540 | ORIGINAL_TEXT | 预测成果分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1290 |
| UNIT-0541 | ORIGINAL_TEXT | 预测成果分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1291 |
| UNIT-0542 | ORIGINAL_TEXT | 预测成果分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1292 |
| UNIT-0543 | ORIGINAL_TEXT | 预测成果分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1293 |

### SEC-216 工程地质与地质环境条件 > 工程地质条件 > 工程地质岩组的划分

- Source locator: P1298
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `工程地质岩组的划分` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0544 工程地质岩组的划分
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0544 | ORIGINAL_TEXT | 工程地质岩组的划分 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1299 |

### SEC-218 工程地质与地质环境条件 > 工程地质条件 > 工程地质岩组的划分 > 坚硬岩组

- Source locator: P1302
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `坚硬岩组` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0545 坚硬岩组
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0545 | ORIGINAL_TEXT | 坚硬岩组 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1304 |

### SEC-219 工程地质与地质环境条件 > 工程地质条件 > 岩土分层及其特征

- Source locator: P1305
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `岩土分层及其特征` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0546 岩土分层及其特征
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0546 | ORIGINAL_TEXT | 岩土分层及其特征 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1306 |

### SEC-220 工程地质与地质环境条件 > 工程地质条件 > 岩土分层及其特征 > 第四系残坡积层(Qedl)

- Source locator: P1307
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `第四系残坡积层(Qedl)` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0547 第四系残坡积层(Qedl)
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0547 | ORIGINAL_TEXT | 第四系残坡积层(Qedl) | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1308 |

### SEC-221 工程地质与地质环境条件 > 工程地质条件 > 岩土分层及其特征 > 石炭系下统刘家塘组（C1lj）基岩

- Source locator: P1309
- Material density: 1段关键文字、1张表
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `石炭系下统刘家塘组（C1lj）基岩` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0548 石炭系下统刘家塘组（C1lj）基岩；UNIT-0549 矿区岩石主要物理力学指标一览表
  - Best source pairing: left_text_right_table or top_text_bottom_table；left_table_right_text or top_text_bottom_table
  - Slide split decision: split or crop tables before reducing font size.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0548 | CALCULATION | 石炭系下统刘家塘组（C1lj）基岩 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P1310 |
| UNIT-0549 | ORIGINAL_TABLE | 矿区岩石主要物理力学指标一览表 | source table with explanation | left_table_right_text or top_text_bottom_table | 0cc6922b:T058, 0cc6922b:P1311 |

### SEC-222 工程地质与地质环境条件 > 工程地质条件 > 露采边坡稳定性分析

- Source locator: P1314
- Material density: 6段关键文字、1张表
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `露采边坡稳定性分析` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0550 露采边坡稳定性分析；UNIT-0551 露采边坡稳定性分析；UNIT-0552 露采边坡稳定性分析；UNIT-0553 露采边坡稳定性分析；UNIT-0554 露采边坡稳定性分析
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_text_right_table or top_text_bottom_table；left_table_right_text or top_text_bottom_table
  - Slide split decision: split or crop tables before reducing font size.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0550 | ORIGINAL_TEXT | 露采边坡稳定性分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1315 |
| UNIT-0551 | ORIGINAL_TEXT | 露采边坡稳定性分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1316 |
| UNIT-0552 | ORIGINAL_TEXT | 露采边坡稳定性分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1317 |
| UNIT-0553 | ORIGINAL_TEXT | 露采边坡稳定性分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1318 |
| UNIT-0554 | ORIGINAL_TEXT | 露采边坡稳定性分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1323 |
| UNIT-0555 | CALCULATION | 露采边坡稳定性分析 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P1324 |
| UNIT-0556 | ORIGINAL_TABLE | 边坡分区表 | source table with explanation | left_table_right_text or top_text_bottom_table | 0cc6922b:T059, 0cc6922b:P1325 |

### SEC-223 工程地质与地质环境条件 > 工程地质条件 > 露采边坡稳定性分析 > A-A’剖面

- Source locator: P1328
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `A-A’剖面` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0557 A-A’剖面
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0557 | ORIGINAL_TEXT | A-A’剖面 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1329 |

### SEC-224 工程地质与地质环境条件 > 工程地质条件 > 露采边坡稳定性分析 > B-B’剖面

- Source locator: P1334
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `B-B’剖面` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0558 B-B’剖面
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0558 | ORIGINAL_TEXT | B-B’剖面 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1335 |

### SEC-225 工程地质与地质环境条件 > 工程地质条件 > 露采边坡稳定性分析 > C-C’剖面

- Source locator: P1340
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `C-C’剖面` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0559 C-C’剖面
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0559 | ORIGINAL_TEXT | C-C’剖面 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1341 |

### SEC-226 工程地质与地质环境条件 > 工程地质条件 > 露采边坡稳定性分析 > D-D’剖面

- Source locator: P1346
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `D-D’剖面` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0560 D-D’剖面
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0560 | ORIGINAL_TEXT | D-D’剖面 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1347 |

### SEC-227 工程地质与地质环境条件 > 工程地质条件 > 工程地质问题预测与分析

- Source locator: P1352
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `工程地质问题预测与分析` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0561 工程地质问题预测与分析
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0561 | ORIGINAL_TEXT | 工程地质问题预测与分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1353 |

### SEC-228 工程地质与地质环境条件 > 工程地质条件 > 工程地质问题预测与分析 > 岩溶地面塌陷

- Source locator: P1354
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `岩溶地面塌陷` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0562 岩溶地面塌陷；UNIT-0563 岩溶地面塌陷
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0562 | ORIGINAL_TEXT | 岩溶地面塌陷 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1355 |
| UNIT-0563 | ORIGINAL_TEXT | 岩溶地面塌陷 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1357 |

### SEC-229 工程地质与地质环境条件 > 工程地质条件 > 工程地质问题预测与分析 > 地表变形

- Source locator: P1358
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `地表变形` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0564 地表变形；UNIT-0565 地表变形
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0564 | ORIGINAL_TEXT | 地表变形 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1359 |
| UNIT-0565 | ORIGINAL_TEXT | 地表变形 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1361 |

### SEC-230 工程地质与地质环境条件 > 工程地质条件 > 工程地质问题预测与分析 > 矿坑突水（突泥）

- Source locator: P1362
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `矿坑突水（突泥）` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0566 矿坑突水（突泥）；UNIT-0567 矿坑突水（突泥）
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0566 | ORIGINAL_TEXT | 矿坑突水（突泥） | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1363 |
| UNIT-0567 | ORIGINAL_TEXT | 矿坑突水（突泥） | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1365 |

### SEC-231 工程地质与地质环境条件 > 工程地质条件 > 工程地质问题预测与分析 > 采场边坡崩塌/滑坡

- Source locator: P1366
- Material density: 9段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `采场边坡崩塌/滑坡` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0568 采场边坡崩塌/滑坡；UNIT-0569 采场边坡崩塌/滑坡；UNIT-0570 采场边坡崩塌/滑坡；UNIT-0571 采场边坡崩塌/滑坡；UNIT-0572 采场边坡崩塌/滑坡
  - Best source pairing: left_text_right_table or top_text_bottom_table；left_text_right_figure or text_with_keypoints
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0568 | CALCULATION | 采场边坡崩塌/滑坡 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P1368 |
| UNIT-0569 | ORIGINAL_TEXT | 采场边坡崩塌/滑坡 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1369 |
| UNIT-0570 | ORIGINAL_TEXT | 采场边坡崩塌/滑坡 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1370 |
| UNIT-0571 | ORIGINAL_TEXT | 采场边坡崩塌/滑坡 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1371 |
| UNIT-0572 | ORIGINAL_TEXT | 采场边坡崩塌/滑坡 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1372 |
| UNIT-0573 | ORIGINAL_TEXT | 采场边坡崩塌/滑坡 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1373 |
| UNIT-0574 | ORIGINAL_TEXT | 采场边坡崩塌/滑坡 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1374 |
| UNIT-0575 | CALCULATION | 采场边坡崩塌/滑坡 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P1375 |
| UNIT-0576 | ORIGINAL_TEXT | 采场边坡崩塌/滑坡 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1376 |

### SEC-232 工程地质与地质环境条件 > 工程地质条件 > 矿区工程地质勘查类型

- Source locator: P1377
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `矿区工程地质勘查类型` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0577 矿区工程地质勘查类型
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0577 | ORIGINAL_TEXT | 矿区工程地质勘查类型 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1378 |

### SEC-234 工程地质与地质环境条件 > 地质环境条件 > 勘察区地质环境评价

- Source locator: P1380
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `勘察区地质环境评价` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0578 勘察区地质环境评价
  - Best source pairing: left_text_right_table or top_text_bottom_table
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0578 | CALCULATION | 勘察区地质环境评价 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P1381 |

### SEC-235 工程地质与地质环境条件 > 地质环境条件 > 环境水文地质问题

- Source locator: P1382
- Material density: 2段关键文字、1张表
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `环境水文地质问题` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0579 环境水文地质问题；UNIT-0580 环境水文地质问题；UNIT-0581 环境水文地质问题
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_table_right_text
  - Slide split decision: split or crop tables before reducing font size.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0579 | ORIGINAL_TEXT | 环境水文地质问题 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1383 |
| UNIT-0580 | ORIGINAL_TEXT | 环境水文地质问题 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1385 |
| UNIT-0581 | ORIGINAL_TABLE | 环境水文地质问题 | source table with explanation | left_table_right_text | 0cc6922b:T060 |

### SEC-236 工程地质与地质环境条件 > 地质环境条件 > 地下水开发利用现状

- Source locator: P1387
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `地下水开发利用现状` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0582 地下水开发利用现状
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0582 | ORIGINAL_TEXT | 地下水开发利用现状 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1388 |

### SEC-239 工程地质与地质环境条件 > 地质环境条件 > 未来矿山开采过程中可能引起的环境地质问题预测评价 > 矿山建设和开采引发地面地质灾害的预测评价

- Source locator: P1393
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `矿山建设和开采引发地面地质灾害的预测评价` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0583 矿山建设和开采引发地面地质灾害的预测评价
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0583 | ORIGINAL_TEXT | 矿山建设和开采引发地面地质灾害的预测评价 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1394 |

### SEC-241 工程地质与地质环境条件 > 地质环境条件 > 未来矿山开采过程中可能引起的环境地质问题预测评价 > 矿山开采对水源的影响

- Source locator: P1397
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `矿山开采对水源的影响` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0584 矿山开采对水源的影响
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0584 | ORIGINAL_TEXT | 矿山开采对水源的影响 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1398 |

### SEC-242 工程地质与地质环境条件 > 地质环境条件 > 矿区地质环境类型

- Source locator: P1399
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `矿区地质环境类型` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0585 矿区地质环境类型
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0585 | ORIGINAL_TEXT | 矿区地质环境类型 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1400 |

### SEC-244 矿区防治水建议 > 矿山防治水原则

- Source locator: P1403
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `矿山防治水原则` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0586 矿山防治水原则
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0586 | ORIGINAL_TEXT | 矿山防治水原则 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1404 |

### SEC-245 矿区防治水建议 > 矿山防治水原则 > 以查明矿坑充水条件为基础，加强采掘过程中水文地质条件研究

- Source locator: P1405
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `以查明矿坑充水条件为基础，加强采掘过程中水文地质条件研究` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0587 以查明矿坑充水条件为基础，加强采掘过程中水文地质条件研究
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0587 | ORIGINAL_TEXT | 以查明矿坑充水条件为基础，加强采掘过程中水文地质条件研究 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1406 |

### SEC-246 矿区防治水建议 > 矿山防治水原则 > 遵循先简单、后复杂，层层设防的原则

- Source locator: P1407
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `遵循先简单、后复杂，层层设防的原则` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0588 遵循先简单、后复杂，层层设防的原则
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0588 | ORIGINAL_TEXT | 遵循先简单、后复杂，层层设防的原则 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1408 |

### SEC-247 矿区防治水建议 > 矿山防治水原则 > 精心组织合理规划，最大限度节约投资的原则

- Source locator: P1409
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `精心组织合理规划，最大限度节约投资的原则` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0589 精心组织合理规划，最大限度节约投资的原则
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0589 | ORIGINAL_TEXT | 精心组织合理规划，最大限度节约投资的原则 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1411 |

### SEC-248 矿区防治水建议 > 矿山防治水措施

- Source locator: P1412
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `矿山防治水措施` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0590 矿山防治水措施
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0590 | ORIGINAL_TEXT | 矿山防治水措施 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1413 |

### SEC-249 矿区防治水建议 > 矿山防治水措施 > 地表堵水措施

- Source locator: P1414
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `地表堵水措施` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0591 地表堵水措施
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0591 | ORIGINAL_TEXT | 地表堵水措施 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1415 |

### SEC-250 矿区防治水建议 > 矿山防治水措施 > 帷幕截水措施

- Source locator: P1416
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `帷幕截水措施` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0592 帷幕截水措施
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0592 | ORIGINAL_TEXT | 帷幕截水措施 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1417 |

### SEC-251 矿区防治水建议 > 矿山防治水措施 > 采坑截渗系统

- Source locator: P1418
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `采坑截渗系统` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0593 采坑截渗系统
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0593 | ORIGINAL_TEXT | 采坑截渗系统 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1419 |

### SEC-253 矿区防治水建议 > 矿山防治水措施 > 超前探水工程

- Source locator: P1422
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `超前探水工程` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0594 超前探水工程
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0594 | ORIGINAL_TEXT | 超前探水工程 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1423 |

### SEC-254 矿区防治水建议 > 矿山防治水措施 > 地下水长期监测工程

- Source locator: P1424
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `地下水长期监测工程` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0595 地下水长期监测工程
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0595 | ORIGINAL_TEXT | 地下水长期监测工程 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1425 |

### SEC-257 矿区水资源综合利用及供水建议 > 水资源综合利用 > 生态用水

- Source locator: P1429
- Material density: 3段关键文字、2张表
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `生态用水` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0596 生态用水；UNIT-0597 GB 3838-2002生态环境水质评价表（常规项目）；UNIT-0598 GB 3838-2002生态环境水质评价表（微量元素）；UNIT-0599 生态用水；UNIT-0600 生态用水
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_table_right_text or top_text_bottom_table
  - Slide split decision: split or crop tables before reducing font size.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0596 | ORIGINAL_TEXT | 生态用水 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1430 |
| UNIT-0597 | ORIGINAL_TABLE | GB 3838-2002生态环境水质评价表（常规项目） | source table with explanation | left_table_right_text or top_text_bottom_table | 0cc6922b:T061, 0cc6922b:P1431 |
| UNIT-0598 | ORIGINAL_TABLE | GB 3838-2002生态环境水质评价表（微量元素） | source table with explanation | left_table_right_text or top_text_bottom_table | 0cc6922b:T062, 0cc6922b:P1432 |
| UNIT-0599 | ORIGINAL_TEXT | 生态用水 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1433 |
| UNIT-0600 | ORIGINAL_TEXT | 生态用水 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1434 |

### SEC-259 矿区水资源综合利用及供水建议 > 水资源综合利用 > 矿坑水排放 > 水质评价

- Source locator: P1436
- Material density: 1段关键文字、1张表
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `水质评价` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0601 水质评价；UNIT-0602 矿区矿坑水排放水质评价表
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_table_right_text
  - Slide split decision: split or crop tables before reducing font size.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0601 | ORIGINAL_TEXT | 水质评价 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1437 |
| UNIT-0602 | ORIGINAL_TABLE | 矿区矿坑水排放水质评价表 | source table with explanation | left_table_right_text | 0cc6922b:T063, 0cc6922b:P1438 |

### SEC-260 矿区水资源综合利用及供水建议 > 水资源综合利用 > 矿坑水排放 > 排放途径与污染防控

- Source locator: P1440
- Material density: 6段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `排放途径与污染防控` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0603 排放途径与污染防控；UNIT-0604 排放途径与污染防控；UNIT-0605 排放途径与污染防控；UNIT-0606 排放途径与污染防控；UNIT-0607 排放途径与污染防控
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0603 | ORIGINAL_TEXT | 排放途径与污染防控 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1441 |
| UNIT-0604 | ORIGINAL_TEXT | 排放途径与污染防控 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1442 |
| UNIT-0605 | ORIGINAL_TEXT | 排放途径与污染防控 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1443 |
| UNIT-0606 | ORIGINAL_TEXT | 排放途径与污染防控 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1444 |
| UNIT-0607 | ORIGINAL_TEXT | 排放途径与污染防控 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1445 |
| UNIT-0608 | ORIGINAL_TEXT | 排放途径与污染防控 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1446 |

### SEC-262 矿区水资源综合利用及供水建议 > 供水建议 > 生产供水

- Source locator: P1449
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `生产供水` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0609 生产供水
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0609 | ORIGINAL_TEXT | 生产供水 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1450 |

### SEC-263 矿区水资源综合利用及供水建议 > 供水建议 > 生活供水

- Source locator: P1451
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `生活供水` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0610 生活供水
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0610 | ORIGINAL_TEXT | 生活供水 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1452 |

### SEC-265 矿区水资源综合利用及供水建议 > 供水建议 > 生活供水 > 备选方案

- Source locator: P1455
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `备选方案` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0611 备选方案
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0611 | ORIGINAL_TEXT | 备选方案 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1456 |

### SEC-266 结论与建议

- Source locator: P1458
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `结论与建议` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0612 结论与建议
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0612 | ORIGINAL_TEXT | 结论与建议 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1459 |

### SEC-268 结论与建议 > 勘查类型 > 水文地质勘查类型

- Source locator: P1461
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `水文地质勘查类型` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0613 水文地质勘查类型；UNIT-0614 水文地质勘查类型
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0613 | ORIGINAL_TEXT | 水文地质勘查类型 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1462 |
| UNIT-0614 | ORIGINAL_TEXT | 水文地质勘查类型 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1463 |

### SEC-269 结论与建议 > 勘查类型 > 工程地质勘查类型

- Source locator: P1465
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `工程地质勘查类型` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0615 工程地质勘查类型
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0615 | ORIGINAL_TEXT | 工程地质勘查类型 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1466 |

### SEC-270 结论与建议 > 勘查类型 > 地质环境类型

- Source locator: P1467
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `地质环境类型` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0616 地质环境类型
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0616 | ORIGINAL_TEXT | 地质环境类型 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1468 |

### SEC-272 结论与建议 > 主要成果 > 查明了矿区岩溶水文地质条件

- Source locator: P1470
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `查明了矿区岩溶水文地质条件` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0617 查明了矿区岩溶水文地质条件；UNIT-0618 查明了矿区岩溶水文地质条件
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0617 | ORIGINAL_TEXT | 查明了矿区岩溶水文地质条件 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1471 |
| UNIT-0618 | ORIGINAL_TEXT | 查明了矿区岩溶水文地质条件 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1472 |

### SEC-273 结论与建议 > 主要成果 > 揭示了矿区地层岩溶发育特征

- Source locator: P1473
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `揭示了矿区地层岩溶发育特征` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0619 揭示了矿区地层岩溶发育特征
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0619 | ORIGINAL_TEXT | 揭示了矿区地层岩溶发育特征 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1474 |

### SEC-274 结论与建议 > 主要成果 > 圈定了矿区边界处岩溶水强径流带

- Source locator: P1475
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `圈定了矿区边界处岩溶水强径流带` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0620 圈定了矿区边界处岩溶水强径流带
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0620 | ORIGINAL_TEXT | 圈定了矿区边界处岩溶水强径流带 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1476 |

### SEC-275 结论与建议 > 主要成果 > 预测了矿区不同开采水平的涌水量

- Source locator: P1477
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `预测了矿区不同开采水平的涌水量` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0621 预测了矿区不同开采水平的涌水量
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0621 | ORIGINAL_TEXT | 预测了矿区不同开采水平的涌水量 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1478 |

### SEC-276 结论与建议 > 主要成果 > 提出了矿区凹陷开采阶段防治水措施

- Source locator: P1479
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `提出了矿区凹陷开采阶段防治水措施` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0622 提出了矿区凹陷开采阶段防治水措施
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0622 | ORIGINAL_TEXT | 提出了矿区凹陷开采阶段防治水措施 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1480 |

### SEC-278 结论与建议 > 存在问题 > 勘察工作中存在的主要问题

- Source locator: P1482
- Material density: 4段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `勘察工作中存在的主要问题` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0623 勘察工作中存在的主要问题；UNIT-0624 勘察工作中存在的主要问题；UNIT-0625 勘察工作中存在的主要问题；UNIT-0626 勘察工作中存在的主要问题
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0623 | ORIGINAL_TEXT | 勘察工作中存在的主要问题 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1483 |
| UNIT-0624 | ORIGINAL_TEXT | 勘察工作中存在的主要问题 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1484 |
| UNIT-0625 | ORIGINAL_TEXT | 勘察工作中存在的主要问题 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1485 |
| UNIT-0626 | ORIGINAL_TEXT | 勘察工作中存在的主要问题 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1486 |

### SEC-279 结论与建议 > 存在问题 > 开采过程中可能出现的问题

- Source locator: P1487
- Material density: 4段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `开采过程中可能出现的问题` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0627 开采过程中可能出现的问题；UNIT-0628 开采过程中可能出现的问题；UNIT-0629 开采过程中可能出现的问题；UNIT-0630 开采过程中可能出现的问题
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0627 | ORIGINAL_TEXT | 开采过程中可能出现的问题 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1488 |
| UNIT-0628 | ORIGINAL_TEXT | 开采过程中可能出现的问题 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1489 |
| UNIT-0629 | ORIGINAL_TEXT | 开采过程中可能出现的问题 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1490 |
| UNIT-0630 | ORIGINAL_TEXT | 开采过程中可能出现的问题 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1491 |

### SEC-280 结论与建议 > 下步建议

- Source locator: P1492
- Material density: 49段关键文字、221张图
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `下步建议` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0631 下步建议；UNIT-0632 下步建议；UNIT-0633 下步建议；UNIT-0634 下步建议；UNIT-0635 下步建议
  - Best source pairing: left_text_right_table or top_text_bottom_table；left_text_right_figure or text_with_keypoints；left_figure_right_text or top_figure_bottom_text
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0631 | CALCULATION | 下步建议 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 0cc6922b:P1493 |
| UNIT-0632 | ORIGINAL_TEXT | 下步建议 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 0cc6922b:P1494 |
| UNIT-0633 | ORIGINAL_FIGURE | 下步建议 | source figure/map/diagram with report-language explanation | left_figure_right_text or top_figure_bottom_text | 0cc6922b:I0001 |
| UNIT-0634 | ORIGINAL_FIGURE | 下步建议 | source figure/map/diagram with report-language explanation | left_figure_right_text or top_figure_bottom_text | 0cc6922b:I0002 |
| UNIT-0635 | ORIGINAL_FIGURE | 下步建议 | source figure/map/diagram with report-language explanation | left_figure_right_text or top_figure_bottom_text | 0cc6922b:I0003 |
| UNIT-0636 | ORIGINAL_FIGURE | 下步建议 | source figure/map/diagram with report-language explanation | left_figure_right_text or top_figure_bottom_text | 0cc6922b:I0004 |
| UNIT-0637 | ORIGINAL_FIGURE | 下步建议 | source figure/map/diagram with report-language explanation | left_figure_right_text or top_figure_bottom_text | 0cc6922b:I0005 |
| UNIT-0638 | ORIGINAL_FIGURE | 下步建议 | source figure/map/diagram with report-language explanation | left_figure_right_text or top_figure_bottom_text | 0cc6922b:I0006 |
| UNIT-0639 | ORIGINAL_FIGURE | 下步建议 | source figure/map/diagram with report-language explanation | left_figure_right_text or top_figure_bottom_text | 0cc6922b:I0007 |
| UNIT-0640 | ORIGINAL_FIGURE | 下步建议 | source figure/map/diagram with report-language explanation | left_figure_right_text or top_figure_bottom_text | 0cc6922b:I0008 |
| UNIT-0641 | ORIGINAL_FIGURE | 下步建议 | source figure/map/diagram with report-language explanation | left_figure_right_text or top_figure_bottom_text | 0cc6922b:I0009 |
| UNIT-0642 | ORIGINAL_FIGURE | 下步建议 | source figure/map/diagram with report-language explanation | left_figure_right_text or top_figure_bottom_text | 0cc6922b:I0010 |
| ... | ... | Additional 258 units in JSON inventory | ... | ... | ... |

### SEC-283 结论与建议 > 下步建议 > ### 项目来源

- Source locator: L00151
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### 项目来源` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0901 ### 项目来源；UNIT-0902 ### 项目来源
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0901 | ORIGINAL_TEXT | ### 项目来源 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00155 |
| UNIT-0902 | ORIGINAL_TEXT | ### 项目来源 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00157 |

### SEC-284 结论与建议 > 下步建议 > ### 目的任务

- Source locator: L00159
- Material density: 10段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### 目的任务` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0903 ### 目的任务；UNIT-0904 ### 目的任务；UNIT-0905 ### 目的任务；UNIT-0906 ### 目的任务；UNIT-0907 ### 目的任务
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_text_right_table or top_text_bottom_table
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0903 | ORIGINAL_TEXT | ### 目的任务 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00161 |
| UNIT-0904 | ORIGINAL_TEXT | ### 目的任务 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00163 |
| UNIT-0905 | ORIGINAL_TEXT | ### 目的任务 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00165 |
| UNIT-0906 | ORIGINAL_TEXT | ### 目的任务 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00167 |
| UNIT-0907 | ORIGINAL_TEXT | ### 目的任务 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00169 |
| UNIT-0908 | ORIGINAL_TEXT | ### 目的任务 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00171 |
| UNIT-0909 | ORIGINAL_TEXT | ### 目的任务 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00173 |
| UNIT-0910 | CALCULATION | ### 目的任务 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L00175 |
| UNIT-0911 | ORIGINAL_TEXT | ### 目的任务 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00177 |
| UNIT-0912 | ORIGINAL_TEXT | ### 目的任务 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00179 |

### SEC-286 结论与建议 > 下步建议 > #### <a id="OLE_LINK40"></a><a id="OLE_LINK39"></a>法律法规

- Source locator: L00183
- Material density: 3段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### <a id="OLE_LINK40"></a><a id="OLE_LINK39"></a>法律法规` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0913 #### <a id="OLE_LINK40"></a><a id="OLE_LI…；UNIT-0914 #### <a id="OLE_LINK40"></a><a id="OLE_LI…；UNIT-0915 #### <a id="OLE_LINK40"></a><a id="OLE_LI…
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0913 | ORIGINAL_TEXT | #### <a id="OLE_LINK40"></a><a id="OLE_LI… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00189 |
| UNIT-0914 | ORIGINAL_TEXT | #### <a id="OLE_LINK40"></a><a id="OLE_LI… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00190 |
| UNIT-0915 | ORIGINAL_TEXT | #### <a id="OLE_LINK40"></a><a id="OLE_LI… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00191 |

### SEC-287 结论与建议 > 下步建议 > #### 技术标准

- Source locator: L00193
- Material density: 21段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### 技术标准` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0916 #### 技术标准；UNIT-0917 #### 技术标准；UNIT-0918 #### 技术标准；UNIT-0919 #### 技术标准；UNIT-0920 #### 技术标准
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_text_right_table or top_text_bottom_table
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0916 | ORIGINAL_TEXT | #### 技术标准 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00195 |
| UNIT-0917 | ORIGINAL_TEXT | #### 技术标准 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00196 |
| UNIT-0918 | ORIGINAL_TEXT | #### 技术标准 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00197 |
| UNIT-0919 | ORIGINAL_TEXT | #### 技术标准 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00198 |
| UNIT-0920 | ORIGINAL_TEXT | #### 技术标准 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00199 |
| UNIT-0921 | ORIGINAL_TEXT | #### 技术标准 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00200 |
| UNIT-0922 | ORIGINAL_TEXT | #### 技术标准 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00201 |
| UNIT-0923 | ORIGINAL_TEXT | #### 技术标准 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00202 |
| UNIT-0924 | ORIGINAL_TEXT | #### 技术标准 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00203 |
| UNIT-0925 | ORIGINAL_TEXT | #### 技术标准 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00204 |
| UNIT-0926 | ORIGINAL_TEXT | #### 技术标准 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00205 |
| UNIT-0927 | ORIGINAL_TEXT | #### 技术标准 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00206 |
| ... | ... | Additional 9 units in JSON inventory | ... | ... | ... |

### SEC-289 结论与建议 > 下步建议 > ## <a id="_Toc22701"></a><a id="_Toc16298"></a><a id="_Toc17082"></a><a id="_Toc4225"></a><a id="_Toc18265"></a><a id="_Toc14811"></a><a id="_Toc28147"></a><a id="_Toc27338"></a><a id="_Toc29071"></a>矿业权设置

- Source locator: L00225
- Material density: 78段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `## <a id="_Toc22701"></a><a id="_Toc16298"></a><a id="_Toc17082"></a><a id="_Toc4225"></a><a id="_Toc18265"></a><a id="_Toc14811"></a><a id="_Toc28147"></a><a id="_Toc27338"></a><a id="_Toc29071"></a>矿业权设置` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-0937 ## <a id="_Toc22701"></a><a id="_Toc16298…；UNIT-0938 ## <a id="_Toc22701"></a><a id="_Toc16298…；UNIT-0939 ## <a id="_Toc22701"></a><a id="_Toc16298…；UNIT-0940 ## <a id="_Toc22701"></a><a id="_Toc16298…；UNIT-0941 ## <a id="_Toc22701"></a><a id="_Toc16298…
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-0937 | ORIGINAL_TEXT | ## <a id="_Toc22701"></a><a id="_Toc16298… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00229 |
| UNIT-0938 | ORIGINAL_TEXT | ## <a id="_Toc22701"></a><a id="_Toc16298… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00249 |
| UNIT-0939 | ORIGINAL_TEXT | ## <a id="_Toc22701"></a><a id="_Toc16298… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00251 |
| UNIT-0940 | ORIGINAL_TEXT | ## <a id="_Toc22701"></a><a id="_Toc16298… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00253 |
| UNIT-0941 | ORIGINAL_TEXT | ## <a id="_Toc22701"></a><a id="_Toc16298… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00255 |
| UNIT-0942 | ORIGINAL_TEXT | ## <a id="_Toc22701"></a><a id="_Toc16298… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00257 |
| UNIT-0943 | ORIGINAL_TEXT | ## <a id="_Toc22701"></a><a id="_Toc16298… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00259 |
| UNIT-0944 | ORIGINAL_TEXT | ## <a id="_Toc22701"></a><a id="_Toc16298… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00261 |
| UNIT-0945 | ORIGINAL_TEXT | ## <a id="_Toc22701"></a><a id="_Toc16298… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00263 |
| UNIT-0946 | ORIGINAL_TEXT | ## <a id="_Toc22701"></a><a id="_Toc16298… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00265 |
| UNIT-0947 | ORIGINAL_TEXT | ## <a id="_Toc22701"></a><a id="_Toc16298… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00267 |
| UNIT-0948 | ORIGINAL_TEXT | ## <a id="_Toc22701"></a><a id="_Toc16298… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00269 |
| ... | ... | Additional 66 units in JSON inventory | ... | ... | ... |

### SEC-291 结论与建议 > 下步建议 > #### 核实报告拟设置采矿权基本情况

- Source locator: L00407
- Material density: 95段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### 核实报告拟设置采矿权基本情况` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-1015 #### 核实报告拟设置采矿权基本情况；UNIT-1016 #### 核实报告拟设置采矿权基本情况；UNIT-1017 #### 核实报告拟设置采矿权基本情况；UNIT-1018 #### 核实报告拟设置采矿权基本情况；UNIT-1019 #### 核实报告拟设置采矿权基本情况
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-1015 | ORIGINAL_TEXT | #### 核实报告拟设置采矿权基本情况 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00409 |
| UNIT-1016 | ORIGINAL_TEXT | #### 核实报告拟设置采矿权基本情况 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00429 |
| UNIT-1017 | ORIGINAL_TEXT | #### 核实报告拟设置采矿权基本情况 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00431 |
| UNIT-1018 | ORIGINAL_TEXT | #### 核实报告拟设置采矿权基本情况 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00433 |
| UNIT-1019 | ORIGINAL_TEXT | #### 核实报告拟设置采矿权基本情况 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00435 |
| UNIT-1020 | ORIGINAL_TEXT | #### 核实报告拟设置采矿权基本情况 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00437 |
| UNIT-1021 | ORIGINAL_TEXT | #### 核实报告拟设置采矿权基本情况 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00439 |
| UNIT-1022 | ORIGINAL_TEXT | #### 核实报告拟设置采矿权基本情况 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00441 |
| UNIT-1023 | ORIGINAL_TEXT | #### 核实报告拟设置采矿权基本情况 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00443 |
| UNIT-1024 | ORIGINAL_TEXT | #### 核实报告拟设置采矿权基本情况 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00445 |
| UNIT-1025 | ORIGINAL_TEXT | #### 核实报告拟设置采矿权基本情况 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00447 |
| UNIT-1026 | ORIGINAL_TEXT | #### 核实报告拟设置采矿权基本情况 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00449 |
| ... | ... | Additional 83 units in JSON inventory | ... | ... | ... |

### SEC-292 结论与建议 > 下步建议 > #### 分割保留区（现拟设采矿权）

- Source locator: L00617
- Material density: 57段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### 分割保留区（现拟设采矿权）` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-1110 #### 分割保留区（现拟设采矿权）；UNIT-1111 #### 分割保留区（现拟设采矿权）；UNIT-1112 #### 分割保留区（现拟设采矿权）；UNIT-1113 #### 分割保留区（现拟设采矿权）；UNIT-1114 #### 分割保留区（现拟设采矿权）
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-1110 | ORIGINAL_TEXT | #### 分割保留区（现拟设采矿权） | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00619 |
| UNIT-1111 | ORIGINAL_TEXT | #### 分割保留区（现拟设采矿权） | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00639 |
| UNIT-1112 | ORIGINAL_TEXT | #### 分割保留区（现拟设采矿权） | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00641 |
| UNIT-1113 | ORIGINAL_TEXT | #### 分割保留区（现拟设采矿权） | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00643 |
| UNIT-1114 | ORIGINAL_TEXT | #### 分割保留区（现拟设采矿权） | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00645 |
| UNIT-1115 | ORIGINAL_TEXT | #### 分割保留区（现拟设采矿权） | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00647 |
| UNIT-1116 | ORIGINAL_TEXT | #### 分割保留区（现拟设采矿权） | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00649 |
| UNIT-1117 | ORIGINAL_TEXT | #### 分割保留区（现拟设采矿权） | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00651 |
| UNIT-1118 | ORIGINAL_TEXT | #### 分割保留区（现拟设采矿权） | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00653 |
| UNIT-1119 | ORIGINAL_TEXT | #### 分割保留区（现拟设采矿权） | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00655 |
| UNIT-1120 | ORIGINAL_TEXT | #### 分割保留区（现拟设采矿权） | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00657 |
| UNIT-1121 | ORIGINAL_TEXT | #### 分割保留区（现拟设采矿权） | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00659 |
| ... | ... | Additional 45 units in JSON inventory | ... | ... | ... |

### SEC-293 结论与建议 > 下步建议 > #### 拟设采矿权情况

- Source locator: L00753
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### 拟设采矿权情况` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-1167 #### 拟设采矿权情况
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-1167 | ORIGINAL_TEXT | #### 拟设采矿权情况 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00755 |

### SEC-294 结论与建议 > 下步建议 > ### 矿山开发现状

- Source locator: L00757
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### 矿山开发现状` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-1168 ### 矿山开发现状；UNIT-1169 ### 矿山开发现状
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-1168 | ORIGINAL_TEXT | ### 矿山开发现状 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00759 |
| UNIT-1169 | ORIGINAL_TEXT | ### 矿山开发现状 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00761 |

### SEC-295 结论与建议 > 下步建议 > ### 矿山开发规划

- Source locator: L00769
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### 矿山开发规划` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-1170 ### 矿山开发规划
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-1170 | ORIGINAL_TEXT | ### 矿山开发规划 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00771 |

### SEC-297 结论与建议 > 下步建议 > ### 以往工作简述

- Source locator: L00775
- Material density: 15段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### 以往工作简述` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-1171 ### 以往工作简述；UNIT-1172 ### 以往工作简述；UNIT-1173 ### 以往工作简述；UNIT-1174 ### 以往工作简述；UNIT-1175 ### 以往工作简述
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-1171 | ORIGINAL_TEXT | ### 以往工作简述 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00777 |
| UNIT-1172 | ORIGINAL_TEXT | ### 以往工作简述 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00779 |
| UNIT-1173 | ORIGINAL_TEXT | ### 以往工作简述 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00781 |
| UNIT-1174 | ORIGINAL_TEXT | ### 以往工作简述 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00783 |
| UNIT-1175 | ORIGINAL_TEXT | ### 以往工作简述 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00785 |
| UNIT-1176 | ORIGINAL_TEXT | ### 以往工作简述 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00787 |
| UNIT-1177 | ORIGINAL_TEXT | ### 以往工作简述 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00789 |
| UNIT-1178 | ORIGINAL_TEXT | ### 以往工作简述 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00791 |
| UNIT-1179 | ORIGINAL_TEXT | ### 以往工作简述 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00793 |
| UNIT-1180 | ORIGINAL_TEXT | ### 以往工作简述 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00795 |
| UNIT-1181 | ORIGINAL_TEXT | ### 以往工作简述 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00797 |
| UNIT-1182 | ORIGINAL_TEXT | ### 以往工作简述 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00799 |
| ... | ... | Additional 3 units in JSON inventory | ... | ... | ... |

### SEC-298 结论与建议 > 下步建议 > ### 以往工作质量评述

- Source locator: L00809
- Material density: 3段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### 以往工作质量评述` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-1186 ### 以往工作质量评述；UNIT-1187 ### 以往工作质量评述；UNIT-1188 ### 以往工作质量评述
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-1186 | ORIGINAL_TEXT | ### 以往工作质量评述 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00811 |
| UNIT-1187 | ORIGINAL_TEXT | ### 以往工作质量评述 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00813 |
| UNIT-1188 | ORIGINAL_TEXT | ### 以往工作质量评述 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00815 |

### SEC-303 结论与建议 > 下步建议 > #### 简要经过

- Source locator: L00829
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### 简要经过` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-1189 #### 简要经过；UNIT-1190 #### 简要经过
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-1189 | ORIGINAL_TEXT | #### 简要经过 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00834 |
| UNIT-1190 | ORIGINAL_TEXT | #### 简要经过 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00835 |

### SEC-305 结论与建议 > 下步建议 > #### 投入工作量

- Source locator: L00839
- Material density: 63段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### 投入工作量` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-1191 #### 投入工作量；UNIT-1192 #### 投入工作量；UNIT-1193 #### 投入工作量；UNIT-1194 #### 投入工作量；UNIT-1195 #### 投入工作量
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-1191 | ORIGINAL_TEXT | #### 投入工作量 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00841 |
| UNIT-1192 | ORIGINAL_TEXT | #### 投入工作量 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00853 |
| UNIT-1193 | ORIGINAL_TEXT | #### 投入工作量 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00855 |
| UNIT-1194 | ORIGINAL_TEXT | #### 投入工作量 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00859 |
| UNIT-1195 | ORIGINAL_TEXT | #### 投入工作量 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00865 |
| UNIT-1196 | ORIGINAL_TEXT | #### 投入工作量 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00871 |
| UNIT-1197 | ORIGINAL_TEXT | #### 投入工作量 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00873 |
| UNIT-1198 | ORIGINAL_TEXT | #### 投入工作量 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00875 |
| UNIT-1199 | ORIGINAL_TEXT | #### 投入工作量 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00879 |
| UNIT-1200 | ORIGINAL_TEXT | #### 投入工作量 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00881 |
| UNIT-1201 | ORIGINAL_TEXT | #### 投入工作量 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00885 |
| UNIT-1202 | ORIGINAL_TEXT | #### 投入工作量 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L00887 |
| ... | ... | Additional 51 units in JSON inventory | ... | ... | ... |

### SEC-306 结论与建议 > 下步建议 > #### 利用以往工作量

- Source locator: L01181
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### 利用以往工作量` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-1254 #### 利用以往工作量
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-1254 | ORIGINAL_TEXT | #### 利用以往工作量 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01185 |

### SEC-311 结论与建议 > 下步建议 > ##### 地下水、地表水动态长期观测

- Source locator: L01199
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `##### 地下水、地表水动态长期观测` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-1255 ##### 地下水、地表水动态长期观测
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-1255 | ORIGINAL_TEXT | ##### 地下水、地表水动态长期观测 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01201 |

### SEC-312 结论与建议 > 下步建议 > ##### 物探

- Source locator: L01203
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `##### 物探` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-1256 ##### 物探
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-1256 | ORIGINAL_TEXT | ##### 物探 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01205 |

### SEC-314 结论与建议 > 下步建议 > ##### 抽水试验

- Source locator: L01211
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `##### 抽水试验` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-1257 ##### 抽水试验
  - Best source pairing: left_text_right_table or top_text_bottom_table
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-1257 | CALCULATION | ##### 抽水试验 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L01213 |

### SEC-315 结论与建议 > 下步建议 > ##### 压水试验

- Source locator: L01215
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `##### 压水试验` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-1258 ##### 压水试验；UNIT-1259 ##### 压水试验
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_text_right_table or top_text_bottom_table
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-1258 | ORIGINAL_TEXT | ##### 压水试验 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01217 |
| UNIT-1259 | CALCULATION | ##### 压水试验 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L01219 |

### SEC-316 结论与建议 > 下步建议 > ##### 水化学分析样采集及送检

- Source locator: L01221
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `##### 水化学分析样采集及送检` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-1260 ##### 水化学分析样采集及送检
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-1260 | ORIGINAL_TEXT | ##### 水化学分析样采集及送检 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01225 |

### SEC-317 结论与建议 > 下步建议 > ##### 孔内成像

- Source locator: L01235
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `##### 孔内成像` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-1261 ##### 孔内成像；UNIT-1262 ##### 孔内成像
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_text_right_table or top_text_bottom_table
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-1261 | ORIGINAL_TEXT | ##### 孔内成像 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01237 |
| UNIT-1262 | CALCULATION | ##### 孔内成像 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L01239 |

### SEC-320 结论与建议 > 下步建议 > #### 取得成果

- Source locator: L01251
- Material density: 24段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### 取得成果` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-1263 #### 取得成果；UNIT-1264 #### 取得成果；UNIT-1265 #### 取得成果；UNIT-1266 #### 取得成果；UNIT-1267 #### 取得成果
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-1263 | ORIGINAL_TEXT | #### 取得成果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01253 |
| UNIT-1264 | ORIGINAL_TEXT | #### 取得成果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01271 |
| UNIT-1265 | ORIGINAL_TEXT | #### 取得成果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01279 |
| UNIT-1266 | ORIGINAL_TEXT | #### 取得成果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01285 |
| UNIT-1267 | ORIGINAL_TEXT | #### 取得成果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01291 |
| UNIT-1268 | ORIGINAL_TEXT | #### 取得成果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01297 |
| UNIT-1269 | ORIGINAL_TEXT | #### 取得成果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01303 |
| UNIT-1270 | ORIGINAL_TEXT | #### 取得成果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01311 |
| UNIT-1271 | ORIGINAL_TEXT | #### 取得成果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01317 |
| UNIT-1272 | ORIGINAL_TEXT | #### 取得成果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01323 |
| UNIT-1273 | ORIGINAL_TEXT | #### 取得成果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01329 |
| UNIT-1274 | ORIGINAL_TEXT | #### 取得成果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01335 |
| ... | ... | Additional 12 units in JSON inventory | ... | ... | ... |

### SEC-322 结论与建议 > 下步建议 > ## <a id="_Toc28962"></a><a id="_Toc23323"></a><a id="_Toc18470"></a>地理位置

- Source locator: L01407
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `## <a id="_Toc28962"></a><a id="_Toc23323"></a><a id="_Toc18470"></a>地理位置` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-1287 ## <a id="_Toc28962"></a><a id="_Toc23323…；UNIT-1288 ## <a id="_Toc28962"></a><a id="_Toc23323…
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-1287 | ORIGINAL_TEXT | ## <a id="_Toc28962"></a><a id="_Toc23323… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01411 |
| UNIT-1288 | ORIGINAL_TEXT | ## <a id="_Toc28962"></a><a id="_Toc23323… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01415 |

### SEC-323 结论与建议 > 下步建议 > ## <a id="_Toc11276"></a><a id="_Toc16028"></a><a id="_Toc30636"></a>地形地貌

- Source locator: L01419
- Material density: 3段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `## <a id="_Toc11276"></a><a id="_Toc16028"></a><a id="_Toc30636"></a>地形地貌` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-1289 ## <a id="_Toc11276"></a><a id="_Toc16028…；UNIT-1290 ## <a id="_Toc11276"></a><a id="_Toc16028…；UNIT-1291 ## <a id="_Toc11276"></a><a id="_Toc16028…
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-1289 | ORIGINAL_TEXT | ## <a id="_Toc11276"></a><a id="_Toc16028… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01423 |
| UNIT-1290 | ORIGINAL_TEXT | ## <a id="_Toc11276"></a><a id="_Toc16028… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01425 |
| UNIT-1291 | ORIGINAL_TEXT | ## <a id="_Toc11276"></a><a id="_Toc16028… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01427 |

### SEC-325 结论与建议 > 下步建议 > ### 气象

- Source locator: L01433
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### 气象` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-1292 ### 气象
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-1292 | ORIGINAL_TEXT | ### 气象 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01435 |

### SEC-326 结论与建议 > 下步建议 > ### 水文

- Source locator: L01443
- Material density: 5段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### 水文` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-1293 ### 水文；UNIT-1294 ### 水文；UNIT-1295 ### 水文；UNIT-1296 ### 水文；UNIT-1297 ### 水文
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-1293 | ORIGINAL_TEXT | ### 水文 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01445 |
| UNIT-1294 | ORIGINAL_TEXT | ### 水文 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01447 |
| UNIT-1295 | ORIGINAL_TEXT | ### 水文 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01451 |
| UNIT-1296 | ORIGINAL_TEXT | ### 水文 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01455 |
| UNIT-1297 | ORIGINAL_TEXT | ### 水文 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01457 |

### SEC-329 结论与建议 > 下步建议 > #### 寒武系八村群（∈1bc）

- Source locator: L01467
- Material density: 3段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### 寒武系八村群（∈1bc）` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-1298 #### 寒武系八村群（∈1bc）；UNIT-1299 #### 寒武系八村群（∈1bc）；UNIT-1300 #### 寒武系八村群（∈1bc）
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-1298 | ORIGINAL_TEXT | #### 寒武系八村群（∈1bc） | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01471 |
| UNIT-1299 | ORIGINAL_TEXT | #### 寒武系八村群（∈1bc） | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01473 |
| UNIT-1300 | ORIGINAL_TEXT | #### 寒武系八村群（∈1bc） | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01475 |

### SEC-330 结论与建议 > 下步建议 > #### 泥盆系上、中、下统（D1\-3）

- Source locator: L01477
- Material density: 5段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### 泥盆系上、中、下统（D1\-3）` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-1301 #### 泥盆系上、中、下统（D1\-3）；UNIT-1302 #### 泥盆系上、中、下统（D1\-3）；UNIT-1303 #### 泥盆系上、中、下统（D1\-3）；UNIT-1304 #### 泥盆系上、中、下统（D1\-3）；UNIT-1305 #### 泥盆系上、中、下统（D1\-3）
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-1301 | ORIGINAL_TEXT | #### 泥盆系上、中、下统（D1\-3） | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01481 |
| UNIT-1302 | ORIGINAL_TEXT | #### 泥盆系上、中、下统（D1\-3） | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01483 |
| UNIT-1303 | ORIGINAL_TEXT | #### 泥盆系上、中、下统（D1\-3） | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01485 |
| UNIT-1304 | ORIGINAL_TEXT | #### 泥盆系上、中、下统（D1\-3） | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01487 |
| UNIT-1305 | ORIGINAL_TEXT | #### 泥盆系上、中、下统（D1\-3） | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01489 |

### SEC-331 结论与建议 > 下步建议 > #### 石炭系下统（C1）

- Source locator: L01491
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### 石炭系下统（C1）` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-1306 #### 石炭系下统（C1）
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-1306 | ORIGINAL_TEXT | #### 石炭系下统（C1） | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01493 |

### SEC-338 结论与建议 > 下步建议 > #### 地壳稳定性

- Source locator: L01525
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### 地壳稳定性` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-1307 #### 地壳稳定性
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-1307 | ORIGINAL_TEXT | #### 地壳稳定性 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01529 |

### SEC-341 结论与建议 > 下步建议 > #### 松散岩类孔隙水

- Source locator: L01539
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### 松散岩类孔隙水` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-1308 #### 松散岩类孔隙水
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-1308 | ORIGINAL_TEXT | #### 松散岩类孔隙水 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01541 |

### SEC-342 结论与建议 > 下步建议 > #### 碳酸盐岩类裂隙溶洞水

- Source locator: L01543
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### 碳酸盐岩类裂隙溶洞水` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-1309 #### 碳酸盐岩类裂隙溶洞水
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-1309 | ORIGINAL_TEXT | #### 碳酸盐岩类裂隙溶洞水 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01545 |

### SEC-343 结论与建议 > 下步建议 > #### 基岩裂隙水

- Source locator: L01547
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### 基岩裂隙水` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-1310 #### 基岩裂隙水
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-1310 | ORIGINAL_TEXT | #### 基岩裂隙水 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01549 |

### SEC-344 结论与建议 > 下步建议 > ### <a id="_Toc22775"></a><a id="_Toc31228"></a>地下水补径排条件

- Source locator: L01551
- Material density: 3段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### <a id="_Toc22775"></a><a id="_Toc31228"></a>地下水补径排条件` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-1311 ### <a id="_Toc22775"></a><a id="_Toc3122…；UNIT-1312 ### <a id="_Toc22775"></a><a id="_Toc3122…；UNIT-1313 ### <a id="_Toc22775"></a><a id="_Toc3122…
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-1311 | ORIGINAL_TEXT | ### <a id="_Toc22775"></a><a id="_Toc3122… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01553 |
| UNIT-1312 | ORIGINAL_TEXT | ### <a id="_Toc22775"></a><a id="_Toc3122… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01555 |
| UNIT-1313 | ORIGINAL_TEXT | ### <a id="_Toc22775"></a><a id="_Toc3122… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01557 |

### SEC-345 结论与建议 > 下步建议 > ### 区域水文地质单元

- Source locator: L01559
- Material density: 5段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### 区域水文地质单元` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-1314 ### 区域水文地质单元；UNIT-1315 ### 区域水文地质单元；UNIT-1316 ### 区域水文地质单元；UNIT-1317 ### 区域水文地质单元；UNIT-1318 ### 区域水文地质单元
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-1314 | ORIGINAL_TEXT | ### 区域水文地质单元 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01561 |
| UNIT-1315 | ORIGINAL_TEXT | ### 区域水文地质单元 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01563 |
| UNIT-1316 | ORIGINAL_TEXT | ### 区域水文地质单元 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01565 |
| UNIT-1317 | ORIGINAL_TEXT | ### 区域水文地质单元 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01567 |
| UNIT-1318 | ORIGINAL_TEXT | ### 区域水文地质单元 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01569 |

### SEC-347 结论与建议 > 下步建议 > ## <a id="_Toc13220"></a><a id="_Toc6572"></a><a id="_Toc12562"></a><a id="_Toc9282"></a><a id="_Toc2089"></a><a id="_Toc31221"></a><a id="_Toc28353"></a><a id="_Toc19653"></a><a id="_Toc11204"></a><a id="_Toc30473"></a>水文地质调查

- Source locator: L01577
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `## <a id="_Toc13220"></a><a id="_Toc6572"></a><a id="_Toc12562"></a><a id="_Toc9282"></a><a id="_Toc2089"></a><a id="_Toc31221"></a><a id="_Toc28353"></a><a id="_Toc19653"></a><a id="_Toc11204"></a><a id="_Toc30473"></a>水文地质调查` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-1319 ## <a id="_Toc13220"></a><a id="_Toc6572"…；UNIT-1320 ## <a id="_Toc13220"></a><a id="_Toc6572"…
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-1319 | ORIGINAL_TEXT | ## <a id="_Toc13220"></a><a id="_Toc6572"… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01579 |
| UNIT-1320 | ORIGINAL_TEXT | ## <a id="_Toc13220"></a><a id="_Toc6572"… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01581 |

### SEC-348 结论与建议 > 下步建议 > ### 地层岩性及富水性调查

- Source locator: L01639
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### 地层岩性及富水性调查` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-1321 ### 地层岩性及富水性调查；UNIT-1322 ### 地层岩性及富水性调查
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-1321 | ORIGINAL_TEXT | ### 地层岩性及富水性调查 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01641 |
| UNIT-1322 | ORIGINAL_TEXT | ### 地层岩性及富水性调查 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01661 |

### SEC-349 结论与建议 > 下步建议 > ### 井泉点及地表水体调查

- Source locator: L01671
- Material density: 4段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### 井泉点及地表水体调查` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-1323 ### 井泉点及地表水体调查；UNIT-1324 ### 井泉点及地表水体调查；UNIT-1325 ### 井泉点及地表水体调查；UNIT-1326 ### 井泉点及地表水体调查
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-1323 | ORIGINAL_TEXT | ### 井泉点及地表水体调查 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01673 |
| UNIT-1324 | ORIGINAL_TEXT | ### 井泉点及地表水体调查 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01677 |
| UNIT-1325 | ORIGINAL_TEXT | ### 井泉点及地表水体调查 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01687 |
| UNIT-1326 | ORIGINAL_TEXT | ### 井泉点及地表水体调查 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01689 |

### SEC-350 结论与建议 > 下步建议 > ### 小结

- Source locator: L01699
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### 小结` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-1327 ### 小结；UNIT-1328 ### 小结
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-1327 | ORIGINAL_TEXT | ### 小结 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01701 |
| UNIT-1328 | ORIGINAL_TEXT | ### 小结 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01703 |

### SEC-353 结论与建议 > 下步建议 > #### <a id="_Toc224174405"></a>测地工作

- Source locator: L01709
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### <a id="_Toc224174405"></a>测地工作` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-1329 #### <a id="_Toc224174405"></a>测地工作；UNIT-1330 #### <a id="_Toc224174405"></a>测地工作
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-1329 | ORIGINAL_TEXT | #### <a id="_Toc224174405"></a>测地工作 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01711 |
| UNIT-1330 | ORIGINAL_TEXT | #### <a id="_Toc224174405"></a>测地工作 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01713 |

### SEC-354 结论与建议 > 下步建议 > #### <a id="_Toc224174406"></a>高密度电法

- Source locator: L01721
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### <a id="_Toc224174406"></a>高密度电法` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-1331 #### <a id="_Toc224174406"></a>高密度电法；UNIT-1332 #### <a id="_Toc224174406"></a>高密度电法
  - Best source pairing: left_text_right_table or top_text_bottom_table；left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-1331 | CALCULATION | #### <a id="_Toc224174406"></a>高密度电法 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L01737 |
| UNIT-1332 | ORIGINAL_TEXT | #### <a id="_Toc224174406"></a>高密度电法 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01739 |

### SEC-355 结论与建议 > 下步建议 > #### <a id="_Toc224174407"></a><a id="_Toc16719"></a><a id="_Toc4223"></a>微动测量

- Source locator: L01747
- Material density: 6段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### <a id="_Toc224174407"></a><a id="_Toc16719"></a><a id="_Toc4223"></a>微动测量` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-1333 #### <a id="_Toc224174407"></a><a id="_To…；UNIT-1334 #### <a id="_Toc224174407"></a><a id="_To…；UNIT-1335 #### <a id="_Toc224174407"></a><a id="_To…；UNIT-1336 #### <a id="_Toc224174407"></a><a id="_To…；UNIT-1337 #### <a id="_Toc224174407"></a><a id="_To…
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_text_right_table or top_text_bottom_table
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-1333 | ORIGINAL_TEXT | #### <a id="_Toc224174407"></a><a id="_To… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01749 |
| UNIT-1334 | ORIGINAL_TEXT | #### <a id="_Toc224174407"></a><a id="_To… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01753 |
| UNIT-1335 | CALCULATION | #### <a id="_Toc224174407"></a><a id="_To… | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L01755 |
| UNIT-1336 | ORIGINAL_TEXT | #### <a id="_Toc224174407"></a><a id="_To… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01757 |
| UNIT-1337 | ORIGINAL_TEXT | #### <a id="_Toc224174407"></a><a id="_To… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01761 |
| UNIT-1338 | ORIGINAL_TEXT | #### <a id="_Toc224174407"></a><a id="_To… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01763 |

### SEC-356 结论与建议 > 下步建议 > #### <a id="_Toc224174408"></a>野外工作方法

- Source locator: L01769
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### <a id="_Toc224174408"></a>野外工作方法` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-1339 #### <a id="_Toc224174408"></a>野外工作方法；UNIT-1340 #### <a id="_Toc224174408"></a>野外工作方法
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-1339 | ORIGINAL_TEXT | #### <a id="_Toc224174408"></a>野外工作方法 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01775 |
| UNIT-1340 | ORIGINAL_TEXT | #### <a id="_Toc224174408"></a>野外工作方法 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01777 |

### SEC-357 结论与建议 > 下步建议 > #### <a id="_Toc224174409"></a>数据处理

- Source locator: L01779
- Material density: 18段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### <a id="_Toc224174409"></a>数据处理` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-1341 #### <a id="_Toc224174409"></a>数据处理；UNIT-1342 #### <a id="_Toc224174409"></a>数据处理；UNIT-1343 #### <a id="_Toc224174409"></a>数据处理；UNIT-1344 #### <a id="_Toc224174409"></a>数据处理；UNIT-1345 #### <a id="_Toc224174409"></a>数据处理
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_text_right_table or top_text_bottom_table
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-1341 | ORIGINAL_TEXT | #### <a id="_Toc224174409"></a>数据处理 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01781 |
| UNIT-1342 | ORIGINAL_TEXT | #### <a id="_Toc224174409"></a>数据处理 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01783 |
| UNIT-1343 | ORIGINAL_TEXT | #### <a id="_Toc224174409"></a>数据处理 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01787 |
| UNIT-1344 | CALCULATION | #### <a id="_Toc224174409"></a>数据处理 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L01789 |
| UNIT-1345 | CALCULATION | #### <a id="_Toc224174409"></a>数据处理 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L01791 |
| UNIT-1346 | ORIGINAL_TEXT | #### <a id="_Toc224174409"></a>数据处理 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01793 |
| UNIT-1347 | ORIGINAL_TEXT | #### <a id="_Toc224174409"></a>数据处理 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01797 |
| UNIT-1348 | ORIGINAL_TEXT | #### <a id="_Toc224174409"></a>数据处理 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01799 |
| UNIT-1349 | ORIGINAL_TEXT | #### <a id="_Toc224174409"></a>数据处理 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01805 |
| UNIT-1350 | CALCULATION | #### <a id="_Toc224174409"></a>数据处理 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L01807 |
| UNIT-1351 | CALCULATION | #### <a id="_Toc224174409"></a>数据处理 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L01809 |
| UNIT-1352 | CALCULATION | #### <a id="_Toc224174409"></a>数据处理 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L01811 |
| ... | ... | Additional 6 units in JSON inventory | ... | ... | ... |

### SEC-358 结论与建议 > 下步建议 > ### <a id="_Toc224174415"></a>解释依据

- Source locator: L01859
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### <a id="_Toc224174415"></a>解释依据` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-1359 ### <a id="_Toc224174415"></a>解释依据；UNIT-1360 ### <a id="_Toc224174415"></a>解释依据
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-1359 | ORIGINAL_TEXT | ### <a id="_Toc224174415"></a>解释依据 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01861 |
| UNIT-1360 | ORIGINAL_TEXT | ### <a id="_Toc224174415"></a>解释依据 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01863 |

### SEC-360 结论与建议 > 下步建议 > #### <a id="_Toc224174417"></a>P1线高密度成果解释

- Source locator: L01869
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### <a id="_Toc224174417"></a>P1线高密度成果解释` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-1361 #### <a id="_Toc224174417"></a>P1线高密度成果解释；UNIT-1362 #### <a id="_Toc224174417"></a>P1线高密度成果解释
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-1361 | ORIGINAL_TEXT | #### <a id="_Toc224174417"></a>P1线高密度成果解释 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01875 |
| UNIT-1362 | ORIGINAL_TEXT | #### <a id="_Toc224174417"></a>P1线高密度成果解释 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01877 |

### SEC-361 结论与建议 > 下步建议 > #### <a id="_Toc224174418"></a>P2线高密度成果解释

- Source locator: L01879
- Material density: 3段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### <a id="_Toc224174418"></a>P2线高密度成果解释` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-1363 #### <a id="_Toc224174418"></a>P2线高密度成果解释；UNIT-1364 #### <a id="_Toc224174418"></a>P2线高密度成果解释；UNIT-1365 #### <a id="_Toc224174418"></a>P2线高密度成果解释
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-1363 | ORIGINAL_TEXT | #### <a id="_Toc224174418"></a>P2线高密度成果解释 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01881 |
| UNIT-1364 | ORIGINAL_TEXT | #### <a id="_Toc224174418"></a>P2线高密度成果解释 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01883 |
| UNIT-1365 | ORIGINAL_TEXT | #### <a id="_Toc224174418"></a>P2线高密度成果解释 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01889 |

### SEC-362 结论与建议 > 下步建议 > #### <a id="_Toc224174419"></a>P3线高密度成果解释

- Source locator: L01891
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### <a id="_Toc224174419"></a>P3线高密度成果解释` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-1366 #### <a id="_Toc224174419"></a>P3线高密度成果解释；UNIT-1367 #### <a id="_Toc224174419"></a>P3线高密度成果解释
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-1366 | ORIGINAL_TEXT | #### <a id="_Toc224174419"></a>P3线高密度成果解释 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01893 |
| UNIT-1367 | ORIGINAL_TEXT | #### <a id="_Toc224174419"></a>P3线高密度成果解释 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01899 |

### SEC-363 结论与建议 > 下步建议 > #### P4线高密度成果解释

- Source locator: L01901
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### P4线高密度成果解释` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-1368 #### P4线高密度成果解释；UNIT-1369 #### P4线高密度成果解释
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-1368 | ORIGINAL_TEXT | #### P4线高密度成果解释 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01903 |
| UNIT-1369 | ORIGINAL_TEXT | #### P4线高密度成果解释 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01911 |

### SEC-364 结论与建议 > 下步建议 > #### P5线高密度成果解释

- Source locator: L01913
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### P5线高密度成果解释` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-1370 #### P5线高密度成果解释；UNIT-1371 #### P5线高密度成果解释
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-1370 | ORIGINAL_TEXT | #### P5线高密度成果解释 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01915 |
| UNIT-1371 | ORIGINAL_TEXT | #### P5线高密度成果解释 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01921 |

### SEC-365 结论与建议 > 下步建议 > #### P6线高密度成果解释

- Source locator: L01923
- Material density: 3段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### P6线高密度成果解释` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-1372 #### P6线高密度成果解释；UNIT-1373 #### P6线高密度成果解释；UNIT-1374 #### P6线高密度成果解释
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-1372 | ORIGINAL_TEXT | #### P6线高密度成果解释 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01925 |
| UNIT-1373 | ORIGINAL_TEXT | #### P6线高密度成果解释 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01929 |
| UNIT-1374 | ORIGINAL_TEXT | #### P6线高密度成果解释 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01931 |

### SEC-366 结论与建议 > 下步建议 > #### P7线高密度成果解释

- Source locator: L01933
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### P7线高密度成果解释` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-1375 #### P7线高密度成果解释；UNIT-1376 #### P7线高密度成果解释
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-1375 | ORIGINAL_TEXT | #### P7线高密度成果解释 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01935 |
| UNIT-1376 | ORIGINAL_TEXT | #### P7线高密度成果解释 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01943 |

### SEC-367 结论与建议 > 下步建议 > #### P8线高密度成果解释

- Source locator: L01945
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### P8线高密度成果解释` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-1377 #### P8线高密度成果解释；UNIT-1378 #### P8线高密度成果解释
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-1377 | ORIGINAL_TEXT | #### P8线高密度成果解释 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01947 |
| UNIT-1378 | ORIGINAL_TEXT | #### P8线高密度成果解释 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01953 |

### SEC-368 结论与建议 > 下步建议 > #### P9线高密度成果解释

- Source locator: L01955
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### P9线高密度成果解释` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-1379 #### P9线高密度成果解释；UNIT-1380 #### P9线高密度成果解释
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-1379 | ORIGINAL_TEXT | #### P9线高密度成果解释 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01957 |
| UNIT-1380 | ORIGINAL_TEXT | #### P9线高密度成果解释 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01963 |

### SEC-369 结论与建议 > 下步建议 > #### <a id="_Toc224174426"></a><a id="OLE_LINK14"></a>P10线高密度成果解释

- Source locator: L01969
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### <a id="_Toc224174426"></a><a id="OLE_LINK14"></a>P10线高密度成果解释` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-1381 #### <a id="_Toc224174426"></a><a id="OLE…；UNIT-1382 #### <a id="_Toc224174426"></a><a id="OLE…
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-1381 | ORIGINAL_TEXT | #### <a id="_Toc224174426"></a><a id="OLE… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01971 |
| UNIT-1382 | ORIGINAL_TEXT | #### <a id="_Toc224174426"></a><a id="OLE… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01979 |

### SEC-370 结论与建议 > 下步建议 > #### P11线高密度成果解释

- Source locator: L01981
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### P11线高密度成果解释` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-1383 #### P11线高密度成果解释；UNIT-1384 #### P11线高密度成果解释
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-1383 | ORIGINAL_TEXT | #### P11线高密度成果解释 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01983 |
| UNIT-1384 | ORIGINAL_TEXT | #### P11线高密度成果解释 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01989 |

### SEC-371 结论与建议 > 下步建议 > #### P12线高密度成果解释

- Source locator: L01991
- Material density: 3段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### P12线高密度成果解释` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-1385 #### P12线高密度成果解释；UNIT-1386 #### P12线高密度成果解释；UNIT-1387 #### P12线高密度成果解释
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-1385 | ORIGINAL_TEXT | #### P12线高密度成果解释 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01993 |
| UNIT-1386 | ORIGINAL_TEXT | #### P12线高密度成果解释 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L01995 |
| UNIT-1387 | ORIGINAL_TEXT | #### P12线高密度成果解释 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L02001 |

### SEC-372 结论与建议 > 下步建议 > #### P13线高密度成果解释

- Source locator: L02003
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### P13线高密度成果解释` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-1388 #### P13线高密度成果解释；UNIT-1389 #### P13线高密度成果解释
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-1388 | ORIGINAL_TEXT | #### P13线高密度成果解释 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L02005 |
| UNIT-1389 | ORIGINAL_TEXT | #### P13线高密度成果解释 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L02011 |

### SEC-373 结论与建议 > 下步建议 > #### P14线高密度成果解释

- Source locator: L02013
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### P14线高密度成果解释` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-1390 #### P14线高密度成果解释；UNIT-1391 #### P14线高密度成果解释
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-1390 | ORIGINAL_TEXT | #### P14线高密度成果解释 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L02015 |
| UNIT-1391 | ORIGINAL_TEXT | #### P14线高密度成果解释 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L02023 |

### SEC-374 结论与建议 > 下步建议 > #### P15线高密度成果解释

- Source locator: L02025
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### P15线高密度成果解释` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-1392 #### P15线高密度成果解释；UNIT-1393 #### P15线高密度成果解释
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-1392 | ORIGINAL_TEXT | #### P15线高密度成果解释 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L02027 |
| UNIT-1393 | ORIGINAL_TEXT | #### P15线高密度成果解释 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L02033 |

### SEC-375 结论与建议 > 下步建议 > #### W10线微动成果解释

- Source locator: L02035
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### W10线微动成果解释` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-1394 #### W10线微动成果解释；UNIT-1395 #### W10线微动成果解释
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-1394 | ORIGINAL_TEXT | #### W10线微动成果解释 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L02037 |
| UNIT-1395 | ORIGINAL_TEXT | #### W10线微动成果解释 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L02043 |

### SEC-376 结论与建议 > 下步建议 > #### W11线微动成果解释

- Source locator: L02045
- Material density: 3段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### W11线微动成果解释` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-1396 #### W11线微动成果解释；UNIT-1397 #### W11线微动成果解释；UNIT-1398 #### W11线微动成果解释
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-1396 | ORIGINAL_TEXT | #### W11线微动成果解释 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L02047 |
| UNIT-1397 | ORIGINAL_TEXT | #### W11线微动成果解释 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L02051 |
| UNIT-1398 | ORIGINAL_TEXT | #### W11线微动成果解释 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L02053 |

### SEC-377 结论与建议 > 下步建议 > #### W12线微动成果解释

- Source locator: L02055
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### W12线微动成果解释` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-1399 #### W12线微动成果解释；UNIT-1400 #### W12线微动成果解释
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-1399 | ORIGINAL_TEXT | #### W12线微动成果解释 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L02057 |
| UNIT-1400 | ORIGINAL_TEXT | #### W12线微动成果解释 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L02063 |

### SEC-378 结论与建议 > 下步建议 > ### <a id="_Toc224174435"></a><a id="_Toc19880"></a><a id="_Toc1766"></a>物探成果

- Source locator: L02065
- Material density: 340段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### <a id="_Toc224174435"></a><a id="_Toc19880"></a><a id="_Toc1766"></a>物探成果` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-1401 ### <a id="_Toc224174435"></a><a id="_Toc…；UNIT-1402 ### <a id="_Toc224174435"></a><a id="_Toc…；UNIT-1403 ### <a id="_Toc224174435"></a><a id="_Toc…；UNIT-1404 ### <a id="_Toc224174435"></a><a id="_Toc…；UNIT-1405 ### <a id="_Toc224174435"></a><a id="_Toc…
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-1401 | ORIGINAL_TEXT | ### <a id="_Toc224174435"></a><a id="_Toc… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L02067 |
| UNIT-1402 | ORIGINAL_TEXT | ### <a id="_Toc224174435"></a><a id="_Toc… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L02091 |
| UNIT-1403 | ORIGINAL_TEXT | ### <a id="_Toc224174435"></a><a id="_Toc… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L02103 |
| UNIT-1404 | ORIGINAL_TEXT | ### <a id="_Toc224174435"></a><a id="_Toc… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L02113 |
| UNIT-1405 | ORIGINAL_TEXT | ### <a id="_Toc224174435"></a><a id="_Toc… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L02123 |
| UNIT-1406 | ORIGINAL_TEXT | ### <a id="_Toc224174435"></a><a id="_Toc… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L02135 |
| UNIT-1407 | ORIGINAL_TEXT | ### <a id="_Toc224174435"></a><a id="_Toc… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L02147 |
| UNIT-1408 | ORIGINAL_TEXT | ### <a id="_Toc224174435"></a><a id="_Toc… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L02159 |
| UNIT-1409 | ORIGINAL_TEXT | ### <a id="_Toc224174435"></a><a id="_Toc… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L02171 |
| UNIT-1410 | ORIGINAL_TEXT | ### <a id="_Toc224174435"></a><a id="_Toc… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L02181 |
| UNIT-1411 | ORIGINAL_TEXT | ### <a id="_Toc224174435"></a><a id="_Toc… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L02193 |
| UNIT-1412 | ORIGINAL_TEXT | ### <a id="_Toc224174435"></a><a id="_Toc… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L02205 |
| ... | ... | Additional 328 units in JSON inventory | ... | ... | ... |

### SEC-379 结论与建议 > 下步建议 > ### 成果验证

- Source locator: L03217
- Material density: 82段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### 成果验证` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-1741 ### 成果验证；UNIT-1742 ### 成果验证；UNIT-1743 ### 成果验证；UNIT-1744 ### 成果验证；UNIT-1745 ### 成果验证
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_text_right_table or top_text_bottom_table
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-1741 | ORIGINAL_TEXT | ### 成果验证 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L03219 |
| UNIT-1742 | ORIGINAL_TEXT | ### 成果验证 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L03243 |
| UNIT-1743 | ORIGINAL_TEXT | ### 成果验证 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L03245 |
| UNIT-1744 | ORIGINAL_TEXT | ### 成果验证 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L03247 |
| UNIT-1745 | ORIGINAL_TEXT | ### 成果验证 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L03249 |
| UNIT-1746 | ORIGINAL_TEXT | ### 成果验证 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L03257 |
| UNIT-1747 | ORIGINAL_TEXT | ### 成果验证 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L03259 |
| UNIT-1748 | ORIGINAL_TEXT | ### 成果验证 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L03263 |
| UNIT-1749 | ORIGINAL_TEXT | ### 成果验证 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L03271 |
| UNIT-1750 | ORIGINAL_TEXT | ### 成果验证 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L03273 |
| UNIT-1751 | ORIGINAL_TEXT | ### 成果验证 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L03277 |
| UNIT-1752 | ORIGINAL_TEXT | ### 成果验证 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L03285 |
| ... | ... | Additional 70 units in JSON inventory | ... | ... | ... |

### SEC-381 结论与建议 > 下步建议 > ### 水文地质钻孔

- Source locator: L03645
- Material density: 529段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### 水文地质钻孔` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-1823 ### 水文地质钻孔；UNIT-1824 ### 水文地质钻孔；UNIT-1825 ### 水文地质钻孔；UNIT-1826 ### 水文地质钻孔；UNIT-1827 ### 水文地质钻孔
  - Best source pairing: left_text_right_table or top_text_bottom_table；left_text_right_figure or text_with_keypoints
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-1823 | CALCULATION | ### 水文地质钻孔 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L03647 |
| UNIT-1824 | ORIGINAL_TEXT | ### 水文地质钻孔 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L03649 |
| UNIT-1825 | ORIGINAL_TEXT | ### 水文地质钻孔 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L03681 |
| UNIT-1826 | ORIGINAL_TEXT | ### 水文地质钻孔 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L03683 |
| UNIT-1827 | ORIGINAL_TEXT | ### 水文地质钻孔 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L03685 |
| UNIT-1828 | ORIGINAL_TEXT | ### 水文地质钻孔 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L03687 |
| UNIT-1829 | ORIGINAL_TEXT | ### 水文地质钻孔 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L03689 |
| UNIT-1830 | ORIGINAL_TEXT | ### 水文地质钻孔 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L03691 |
| UNIT-1831 | ORIGINAL_TEXT | ### 水文地质钻孔 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L03693 |
| UNIT-1832 | ORIGINAL_TEXT | ### 水文地质钻孔 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L03695 |
| UNIT-1833 | ORIGINAL_TEXT | ### 水文地质钻孔 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L03699 |
| UNIT-1834 | ORIGINAL_TEXT | ### 水文地质钻孔 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L03701 |
| ... | ... | Additional 517 units in JSON inventory | ... | ... | ... |

### SEC-383 结论与建议 > 下步建议 > #### 工作概况

- Source locator: L04871
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### 工作概况` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-2352 #### 工作概况
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-2352 | ORIGINAL_TEXT | #### 工作概况 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L04873 |

### SEC-384 结论与建议 > 下步建议 > #### 技术要求

- Source locator: L04875
- Material density: 9段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### 技术要求` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-2353 #### 技术要求；UNIT-2354 #### 技术要求；UNIT-2355 #### 技术要求；UNIT-2356 #### 技术要求；UNIT-2357 #### 技术要求
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_text_right_table or top_text_bottom_table
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-2353 | ORIGINAL_TEXT | #### 技术要求 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L04877 |
| UNIT-2354 | ORIGINAL_TEXT | #### 技术要求 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L04879 |
| UNIT-2355 | ORIGINAL_TEXT | #### 技术要求 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L04881 |
| UNIT-2356 | CALCULATION | #### 技术要求 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L04883 |
| UNIT-2357 | ORIGINAL_TEXT | #### 技术要求 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L04885 |
| UNIT-2358 | CALCULATION | #### 技术要求 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L04887 |
| UNIT-2359 | ORIGINAL_TEXT | #### 技术要求 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L04889 |
| UNIT-2360 | CALCULATION | #### 技术要求 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L04891 |
| UNIT-2361 | ORIGINAL_TEXT | #### 技术要求 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L04893 |

### SEC-385 结论与建议 > 下步建议 > #### <a id="_Toc28988"></a>工作方法

- Source locator: L04895
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### <a id="_Toc28988"></a>工作方法` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-2362 #### <a id="_Toc28988"></a>工作方法；UNIT-2363 #### <a id="_Toc28988"></a>工作方法
  - Best source pairing: left_text_right_table or top_text_bottom_table；left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-2362 | CALCULATION | #### <a id="_Toc28988"></a>工作方法 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L04897 |
| UNIT-2363 | ORIGINAL_TEXT | #### <a id="_Toc28988"></a>工作方法 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L04907 |

### SEC-386 结论与建议 > 下步建议 > #### 测试成果

- Source locator: L04913
- Material density: 83段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### 测试成果` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-2364 #### 测试成果；UNIT-2365 #### 测试成果；UNIT-2366 #### 测试成果；UNIT-2367 #### 测试成果；UNIT-2368 #### 测试成果
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-2364 | ORIGINAL_TEXT | #### 测试成果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L04933 |
| UNIT-2365 | ORIGINAL_TEXT | #### 测试成果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L04937 |
| UNIT-2366 | ORIGINAL_TEXT | #### 测试成果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L04941 |
| UNIT-2367 | ORIGINAL_TEXT | #### 测试成果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L04945 |
| UNIT-2368 | ORIGINAL_TEXT | #### 测试成果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L04947 |
| UNIT-2369 | ORIGINAL_TEXT | #### 测试成果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L04949 |
| UNIT-2370 | ORIGINAL_TEXT | #### 测试成果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L04951 |
| UNIT-2371 | ORIGINAL_TEXT | #### 测试成果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L04953 |
| UNIT-2372 | ORIGINAL_TEXT | #### 测试成果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L04955 |
| UNIT-2373 | ORIGINAL_TEXT | #### 测试成果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L04957 |
| UNIT-2374 | ORIGINAL_TEXT | #### 测试成果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L04959 |
| UNIT-2375 | ORIGINAL_TEXT | #### 测试成果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L04961 |
| ... | ... | Additional 71 units in JSON inventory | ... | ... | ... |

### SEC-390 结论与建议 > 下步建议 > #### 技术要求

- Source locator: L05155
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### 技术要求` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-2447 #### 技术要求
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-2447 | ORIGINAL_TEXT | #### 技术要求 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L05157 |

### SEC-391 结论与建议 > 下步建议 > #### 水文地质参数计算

- Source locator: L05159
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### 水文地质参数计算` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-2448 #### 水文地质参数计算
  - Best source pairing: left_text_right_table or top_text_bottom_table
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-2448 | CALCULATION | #### 水文地质参数计算 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L05161 |

### SEC-392 结论与建议 > 下步建议 > #### 抽水试验计算公式

- Source locator: L05163
- Material density: 17段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### 抽水试验计算公式` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-2449 #### 抽水试验计算公式；UNIT-2450 #### 抽水试验计算公式；UNIT-2451 #### 抽水试验计算公式；UNIT-2452 #### 抽水试验计算公式；UNIT-2453 #### 抽水试验计算公式
  - Best source pairing: left_text_right_table or top_text_bottom_table；left_text_right_figure or text_with_keypoints
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-2449 | CALCULATION | #### 抽水试验计算公式 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L05165 |
| UNIT-2450 | ORIGINAL_TEXT | #### 抽水试验计算公式 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L05167 |
| UNIT-2451 | ORIGINAL_TEXT | #### 抽水试验计算公式 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L05173 |
| UNIT-2452 | CALCULATION | #### 抽水试验计算公式 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L05179 |
| UNIT-2453 | CALCULATION | #### 抽水试验计算公式 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L05181 |
| UNIT-2454 | CALCULATION | #### 抽水试验计算公式 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L05183 |
| UNIT-2455 | CALCULATION | #### 抽水试验计算公式 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L05185 |
| UNIT-2456 | ORIGINAL_TEXT | #### 抽水试验计算公式 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L05187 |
| UNIT-2457 | ORIGINAL_TEXT | #### 抽水试验计算公式 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L05189 |
| UNIT-2458 | ORIGINAL_TEXT | #### 抽水试验计算公式 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L05191 |
| UNIT-2459 | ORIGINAL_TEXT | #### 抽水试验计算公式 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L05193 |
| UNIT-2460 | ORIGINAL_TEXT | #### 抽水试验计算公式 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L05195 |
| ... | ... | Additional 5 units in JSON inventory | ... | ... | ... |

### SEC-393 结论与建议 > 下步建议 > #### 抽水试验计算结果

- Source locator: L05207
- Material density: 216段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### 抽水试验计算结果` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-2466 #### 抽水试验计算结果；UNIT-2467 #### 抽水试验计算结果；UNIT-2468 #### 抽水试验计算结果；UNIT-2469 #### 抽水试验计算结果；UNIT-2470 #### 抽水试验计算结果
  - Best source pairing: left_text_right_table or top_text_bottom_table；left_text_right_figure or text_with_keypoints
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-2466 | CALCULATION | #### 抽水试验计算结果 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L05209 |
| UNIT-2467 | CALCULATION | #### 抽水试验计算结果 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L05211 |
| UNIT-2468 | CALCULATION | #### 抽水试验计算结果 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L05213 |
| UNIT-2469 | CALCULATION | #### 抽水试验计算结果 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L05215 |
| UNIT-2470 | ORIGINAL_TEXT | #### 抽水试验计算结果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L05227 |
| UNIT-2471 | ORIGINAL_TEXT | #### 抽水试验计算结果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L05231 |
| UNIT-2472 | ORIGINAL_TEXT | #### 抽水试验计算结果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L05235 |
| UNIT-2473 | ORIGINAL_TEXT | #### 抽水试验计算结果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L05239 |
| UNIT-2474 | ORIGINAL_TEXT | #### 抽水试验计算结果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L05243 |
| UNIT-2475 | CALCULATION | #### 抽水试验计算结果 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L05247 |
| UNIT-2476 | ORIGINAL_TEXT | #### 抽水试验计算结果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L05257 |
| UNIT-2477 | ORIGINAL_TEXT | #### 抽水试验计算结果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L05261 |
| ... | ... | Additional 204 units in JSON inventory | ... | ... | ... |

### SEC-395 结论与建议 > 下步建议 > #### 试验概况

- Source locator: L05885
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### 试验概况` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-2682 #### 试验概况
  - Best source pairing: left_text_right_table or top_text_bottom_table
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-2682 | CALCULATION | #### 试验概况 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L05887 |

### SEC-397 结论与建议 > 下步建议 > #### 计算公式

- Source locator: L05897
- Material density: 5段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### 计算公式` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-2683 #### 计算公式；UNIT-2684 #### 计算公式；UNIT-2685 #### 计算公式；UNIT-2686 #### 计算公式；UNIT-2687 #### 计算公式
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-2683 | ORIGINAL_TEXT | #### 计算公式 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L05903 |
| UNIT-2684 | ORIGINAL_TEXT | #### 计算公式 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L05913 |
| UNIT-2685 | ORIGINAL_TEXT | #### 计算公式 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L05929 |
| UNIT-2686 | ORIGINAL_TEXT | #### 计算公式 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L05931 |
| UNIT-2687 | ORIGINAL_TEXT | #### 计算公式 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L05939 |

### SEC-398 结论与建议 > 下步建议 > #### 计算结果

- Source locator: L05943
- Material density: 1219段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### 计算结果` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-2688 #### 计算结果；UNIT-2689 #### 计算结果；UNIT-2690 #### 计算结果；UNIT-2691 #### 计算结果；UNIT-2692 #### 计算结果
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_text_right_table or top_text_bottom_table
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-2688 | ORIGINAL_TEXT | #### 计算结果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L05945 |
| UNIT-2689 | CALCULATION | #### 计算结果 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L05947 |
| UNIT-2690 | ORIGINAL_TEXT | #### 计算结果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L05949 |
| UNIT-2691 | ORIGINAL_TEXT | #### 计算结果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L05975 |
| UNIT-2692 | ORIGINAL_TEXT | #### 计算结果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L05977 |
| UNIT-2693 | ORIGINAL_TEXT | #### 计算结果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L05979 |
| UNIT-2694 | ORIGINAL_TEXT | #### 计算结果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L05981 |
| UNIT-2695 | ORIGINAL_TEXT | #### 计算结果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L05983 |
| UNIT-2696 | ORIGINAL_TEXT | #### 计算结果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L05985 |
| UNIT-2697 | ORIGINAL_TEXT | #### 计算结果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L05989 |
| UNIT-2698 | ORIGINAL_TEXT | #### 计算结果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L05991 |
| UNIT-2699 | ORIGINAL_TEXT | #### 计算结果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L05993 |
| ... | ... | Additional 1207 units in JSON inventory | ... | ... | ... |

### SEC-401 结论与建议 > 下步建议 > #### 试验原理

- Source locator: L08817
- Material density: 10段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### 试验原理` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-3907 #### 试验原理；UNIT-3908 #### 试验原理；UNIT-3909 #### 试验原理；UNIT-3910 #### 试验原理；UNIT-3911 #### 试验原理
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_text_right_table or top_text_bottom_table
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-3907 | ORIGINAL_TEXT | #### 试验原理 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L08819 |
| UNIT-3908 | CALCULATION | #### 试验原理 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L08821 |
| UNIT-3909 | CALCULATION | #### 试验原理 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L08823 |
| UNIT-3910 | CALCULATION | #### 试验原理 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L08825 |
| UNIT-3911 | ORIGINAL_TEXT | #### 试验原理 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L08835 |
| UNIT-3912 | ORIGINAL_TEXT | #### 试验原理 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L08839 |
| UNIT-3913 | ORIGINAL_TEXT | #### 试验原理 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L08841 |
| UNIT-3914 | ORIGINAL_TEXT | #### 试验原理 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L08843 |
| UNIT-3915 | ORIGINAL_TEXT | #### 试验原理 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L08845 |
| UNIT-3916 | ORIGINAL_TEXT | #### 试验原理 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L08847 |

### SEC-402 结论与建议 > 下步建议 > #### <a id="bookmark16"></a><a id="_Toc1256"></a>试验方法

- Source locator: L08849
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### <a id="bookmark16"></a><a id="_Toc1256"></a>试验方法` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-3917 #### <a id="bookmark16"></a><a id="_Toc12…
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-3917 | ORIGINAL_TEXT | #### <a id="bookmark16"></a><a id="_Toc12… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L08853 |

### SEC-404 结论与建议 > 下步建议 > ##### 试验部署

- Source locator: L08857
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `##### 试验部署` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-3918 ##### 试验部署
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-3918 | ORIGINAL_TEXT | ##### 试验部署 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L08859 |

### SEC-405 结论与建议 > 下步建议 > ##### <a id="bookmark43"></a>第一次示踪试验

- Source locator: L08865
- Material density: 19段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `##### <a id="bookmark43"></a>第一次示踪试验` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-3919 ##### <a id="bookmark43"></a>第一次示踪试验；UNIT-3920 ##### <a id="bookmark43"></a>第一次示踪试验；UNIT-3921 ##### <a id="bookmark43"></a>第一次示踪试验；UNIT-3922 ##### <a id="bookmark43"></a>第一次示踪试验；UNIT-3923 ##### <a id="bookmark43"></a>第一次示踪试验
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-3919 | ORIGINAL_TEXT | ##### <a id="bookmark43"></a>第一次示踪试验 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L08897 |
| UNIT-3920 | ORIGINAL_TEXT | ##### <a id="bookmark43"></a>第一次示踪试验 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L08899 |
| UNIT-3921 | ORIGINAL_TEXT | ##### <a id="bookmark43"></a>第一次示踪试验 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L08903 |
| UNIT-3922 | ORIGINAL_TEXT | ##### <a id="bookmark43"></a>第一次示踪试验 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L08905 |
| UNIT-3923 | ORIGINAL_TEXT | ##### <a id="bookmark43"></a>第一次示踪试验 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L08907 |
| UNIT-3924 | ORIGINAL_TEXT | ##### <a id="bookmark43"></a>第一次示踪试验 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L08915 |
| UNIT-3925 | ORIGINAL_TEXT | ##### <a id="bookmark43"></a>第一次示踪试验 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L08917 |
| UNIT-3926 | ORIGINAL_TEXT | ##### <a id="bookmark43"></a>第一次示踪试验 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L08921 |
| UNIT-3927 | ORIGINAL_TEXT | ##### <a id="bookmark43"></a>第一次示踪试验 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L08923 |
| UNIT-3928 | ORIGINAL_TEXT | ##### <a id="bookmark43"></a>第一次示踪试验 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L08925 |
| UNIT-3929 | ORIGINAL_TEXT | ##### <a id="bookmark43"></a>第一次示踪试验 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L08933 |
| UNIT-3930 | ORIGINAL_TEXT | ##### <a id="bookmark43"></a>第一次示踪试验 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L08935 |
| ... | ... | Additional 7 units in JSON inventory | ... | ... | ... |

### SEC-406 结论与建议 > 下步建议 > ##### 第二次示踪试验

- Source locator: L08985
- Material density: 23段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `##### 第二次示踪试验` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-3938 ##### 第二次示踪试验；UNIT-3939 ##### 第二次示踪试验；UNIT-3940 ##### 第二次示踪试验；UNIT-3941 ##### 第二次示踪试验；UNIT-3942 ##### 第二次示踪试验
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-3938 | ORIGINAL_TEXT | ##### 第二次示踪试验 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L08987 |
| UNIT-3939 | ORIGINAL_TEXT | ##### 第二次示踪试验 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09015 |
| UNIT-3940 | ORIGINAL_TEXT | ##### 第二次示踪试验 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09017 |
| UNIT-3941 | ORIGINAL_TEXT | ##### 第二次示踪试验 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09021 |
| UNIT-3942 | ORIGINAL_TEXT | ##### 第二次示踪试验 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09023 |
| UNIT-3943 | ORIGINAL_TEXT | ##### 第二次示踪试验 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09025 |
| UNIT-3944 | ORIGINAL_TEXT | ##### 第二次示踪试验 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09031 |
| UNIT-3945 | ORIGINAL_TEXT | ##### 第二次示踪试验 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09033 |
| UNIT-3946 | ORIGINAL_TEXT | ##### 第二次示踪试验 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09035 |
| UNIT-3947 | ORIGINAL_TEXT | ##### 第二次示踪试验 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09039 |
| UNIT-3948 | ORIGINAL_TEXT | ##### 第二次示踪试验 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09041 |
| UNIT-3949 | ORIGINAL_TEXT | ##### 第二次示踪试验 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09043 |
| ... | ... | Additional 11 units in JSON inventory | ... | ... | ... |

### SEC-407 结论与建议 > 下步建议 > #### 试验结果

- Source locator: L09101
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### 试验结果` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-3961 #### 试验结果
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-3961 | ORIGINAL_TEXT | #### 试验结果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09103 |

### SEC-409 结论与建议 > 下步建议 > ### <a id="_Toc13113"></a><a id="_Toc4861"></a>取样测试与数据整理

- Source locator: L09107
- Material density: 45段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### <a id="_Toc13113"></a><a id="_Toc4861"></a>取样测试与数据整理` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-3962 ### <a id="_Toc13113"></a><a id="_Toc4861…；UNIT-3963 ### <a id="_Toc13113"></a><a id="_Toc4861…；UNIT-3964 ### <a id="_Toc13113"></a><a id="_Toc4861…；UNIT-3965 ### <a id="_Toc13113"></a><a id="_Toc4861…；UNIT-3966 ### <a id="_Toc13113"></a><a id="_Toc4861…
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_text_right_table or top_text_bottom_table
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-3962 | ORIGINAL_TEXT | ### <a id="_Toc13113"></a><a id="_Toc4861… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09109 |
| UNIT-3963 | ORIGINAL_TEXT | ### <a id="_Toc13113"></a><a id="_Toc4861… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09111 |
| UNIT-3964 | ORIGINAL_TEXT | ### <a id="_Toc13113"></a><a id="_Toc4861… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09119 |
| UNIT-3965 | CALCULATION | ### <a id="_Toc13113"></a><a id="_Toc4861… | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L09121 |
| UNIT-3966 | ORIGINAL_TEXT | ### <a id="_Toc13113"></a><a id="_Toc4861… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09123 |
| UNIT-3967 | ORIGINAL_TEXT | ### <a id="_Toc13113"></a><a id="_Toc4861… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09137 |
| UNIT-3968 | ORIGINAL_TEXT | ### <a id="_Toc13113"></a><a id="_Toc4861… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09149 |
| UNIT-3969 | ORIGINAL_TEXT | ### <a id="_Toc13113"></a><a id="_Toc4861… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09161 |
| UNIT-3970 | ORIGINAL_TEXT | ### <a id="_Toc13113"></a><a id="_Toc4861… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09173 |
| UNIT-3971 | ORIGINAL_TEXT | ### <a id="_Toc13113"></a><a id="_Toc4861… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09185 |
| UNIT-3972 | ORIGINAL_TEXT | ### <a id="_Toc13113"></a><a id="_Toc4861… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09197 |
| UNIT-3973 | ORIGINAL_TEXT | ### <a id="_Toc13113"></a><a id="_Toc4861… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09209 |
| ... | ... | Additional 33 units in JSON inventory | ... | ... | ... |

### SEC-411 结论与建议 > 下步建议 > #### <a id="_Toc175574494"></a>水化学基本特征

- Source locator: L09381
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### <a id="_Toc175574494"></a>水化学基本特征` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-4007 #### <a id="_Toc175574494"></a>水化学基本特征；UNIT-4008 #### <a id="_Toc175574494"></a>水化学基本特征
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-4007 | ORIGINAL_TEXT | #### <a id="_Toc175574494"></a>水化学基本特征 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09383 |
| UNIT-4008 | ORIGINAL_TEXT | #### <a id="_Toc175574494"></a>水化学基本特征 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09385 |

### SEC-413 结论与建议 > 下步建议 > ##### 舒卡列夫分类

- Source locator: L09389
- Material density: 24段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `##### 舒卡列夫分类` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-4009 ##### 舒卡列夫分类；UNIT-4010 ##### 舒卡列夫分类；UNIT-4011 ##### 舒卡列夫分类；UNIT-4012 ##### 舒卡列夫分类；UNIT-4013 ##### 舒卡列夫分类
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-4009 | ORIGINAL_TEXT | ##### 舒卡列夫分类 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09391 |
| UNIT-4010 | ORIGINAL_TEXT | ##### 舒卡列夫分类 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09393 |
| UNIT-4011 | ORIGINAL_TEXT | ##### 舒卡列夫分类 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09403 |
| UNIT-4012 | ORIGINAL_TEXT | ##### 舒卡列夫分类 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09411 |
| UNIT-4013 | ORIGINAL_TEXT | ##### 舒卡列夫分类 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09419 |
| UNIT-4014 | ORIGINAL_TEXT | ##### 舒卡列夫分类 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09427 |
| UNIT-4015 | ORIGINAL_TEXT | ##### 舒卡列夫分类 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09435 |
| UNIT-4016 | ORIGINAL_TEXT | ##### 舒卡列夫分类 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09443 |
| UNIT-4017 | ORIGINAL_TEXT | ##### 舒卡列夫分类 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09451 |
| UNIT-4018 | ORIGINAL_TEXT | ##### 舒卡列夫分类 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09459 |
| UNIT-4019 | ORIGINAL_TEXT | ##### 舒卡列夫分类 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09467 |
| UNIT-4020 | ORIGINAL_TEXT | ##### 舒卡列夫分类 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09475 |
| ... | ... | Additional 12 units in JSON inventory | ... | ... | ... |

### SEC-414 结论与建议 > 下步建议 > ##### Piper三线图

- Source locator: L09515
- Material density: 3段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `##### Piper三线图` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-4033 ##### Piper三线图；UNIT-4034 ##### Piper三线图；UNIT-4035 ##### Piper三线图
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-4033 | ORIGINAL_TEXT | ##### Piper三线图 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09517 |
| UNIT-4034 | ORIGINAL_TEXT | ##### Piper三线图 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09521 |
| UNIT-4035 | ORIGINAL_TEXT | ##### Piper三线图 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09523 |

### SEC-416 结论与建议 > 下步建议 > ##### 水化学成因分析

- Source locator: L09527
- Material density: 4段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `##### 水化学成因分析` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-4036 ##### 水化学成因分析；UNIT-4037 ##### 水化学成因分析；UNIT-4038 ##### 水化学成因分析；UNIT-4039 ##### 水化学成因分析
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_text_right_table or top_text_bottom_table
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-4036 | ORIGINAL_TEXT | ##### 水化学成因分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09529 |
| UNIT-4037 | ORIGINAL_TEXT | ##### 水化学成因分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09531 |
| UNIT-4038 | ORIGINAL_TEXT | ##### 水化学成因分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09533 |
| UNIT-4039 | CALCULATION | ##### 水化学成因分析 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L09535 |

### SEC-417 结论与建议 > 下步建议 > ##### 离子比值分析

- Source locator: L09537
- Material density: 10段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `##### 离子比值分析` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-4040 ##### 离子比值分析；UNIT-4041 ##### 离子比值分析；UNIT-4042 ##### 离子比值分析；UNIT-4043 ##### 离子比值分析；UNIT-4044 ##### 离子比值分析
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-4040 | ORIGINAL_TEXT | ##### 离子比值分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09539 |
| UNIT-4041 | ORIGINAL_TEXT | ##### 离子比值分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09541 |
| UNIT-4042 | ORIGINAL_TEXT | ##### 离子比值分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09545 |
| UNIT-4043 | ORIGINAL_TEXT | ##### 离子比值分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09547 |
| UNIT-4044 | ORIGINAL_TEXT | ##### 离子比值分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09551 |
| UNIT-4045 | ORIGINAL_TEXT | ##### 离子比值分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09555 |
| UNIT-4046 | ORIGINAL_TEXT | ##### 离子比值分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09557 |
| UNIT-4047 | ORIGINAL_TEXT | ##### 离子比值分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09567 |
| UNIT-4048 | ORIGINAL_TEXT | ##### 离子比值分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09571 |
| UNIT-4049 | ORIGINAL_TEXT | ##### 离子比值分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09573 |

### SEC-418 结论与建议 > 下步建议 > #### 氢氧稳定同位素特征分析

- Source locator: L09575
- Material density: 58段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### 氢氧稳定同位素特征分析` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-4050 #### 氢氧稳定同位素特征分析；UNIT-4051 #### 氢氧稳定同位素特征分析；UNIT-4052 #### 氢氧稳定同位素特征分析；UNIT-4053 #### 氢氧稳定同位素特征分析；UNIT-4054 #### 氢氧稳定同位素特征分析
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_text_right_table or top_text_bottom_table
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-4050 | ORIGINAL_TEXT | #### 氢氧稳定同位素特征分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09579 |
| UNIT-4051 | ORIGINAL_TEXT | #### 氢氧稳定同位素特征分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09581 |
| UNIT-4052 | ORIGINAL_TEXT | #### 氢氧稳定同位素特征分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09601 |
| UNIT-4053 | ORIGINAL_TEXT | #### 氢氧稳定同位素特征分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09603 |
| UNIT-4054 | ORIGINAL_TEXT | #### 氢氧稳定同位素特征分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09605 |
| UNIT-4055 | ORIGINAL_TEXT | #### 氢氧稳定同位素特征分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09611 |
| UNIT-4056 | ORIGINAL_TEXT | #### 氢氧稳定同位素特征分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09613 |
| UNIT-4057 | ORIGINAL_TEXT | #### 氢氧稳定同位素特征分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09615 |
| UNIT-4058 | ORIGINAL_TEXT | #### 氢氧稳定同位素特征分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09621 |
| UNIT-4059 | ORIGINAL_TEXT | #### 氢氧稳定同位素特征分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09623 |
| UNIT-4060 | ORIGINAL_TEXT | #### 氢氧稳定同位素特征分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09625 |
| UNIT-4061 | ORIGINAL_TEXT | #### 氢氧稳定同位素特征分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09631 |
| ... | ... | Additional 46 units in JSON inventory | ... | ... | ... |

### SEC-419 结论与建议 > 下步建议 > #### 小结

- Source locator: L09755
- Material density: 3段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### 小结` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-4108 #### 小结；UNIT-4109 #### 小结；UNIT-4110 #### 小结
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-4108 | ORIGINAL_TEXT | #### 小结 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09757 |
| UNIT-4109 | ORIGINAL_TEXT | #### 小结 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09758 |
| UNIT-4110 | ORIGINAL_TEXT | #### 小结 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09759 |

### SEC-422 结论与建议 > 下步建议 > ### 矿区地层

- Source locator: L09765
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### 矿区地层` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-4111 ### 矿区地层
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-4111 | ORIGINAL_TEXT | ### 矿区地层 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09771 |

### SEC-423 结论与建议 > 下步建议 > ### 矿区地质构造

- Source locator: L09773
- Material density: 27段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### 矿区地质构造` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-4112 ### 矿区地质构造；UNIT-4113 ### 矿区地质构造；UNIT-4114 ### 矿区地质构造；UNIT-4115 ### 矿区地质构造；UNIT-4116 ### 矿区地质构造
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-4112 | ORIGINAL_TEXT | ### 矿区地质构造 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09775 |
| UNIT-4113 | ORIGINAL_TEXT | ### 矿区地质构造 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09789 |
| UNIT-4114 | ORIGINAL_TEXT | ### 矿区地质构造 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09795 |
| UNIT-4115 | ORIGINAL_TEXT | ### 矿区地质构造 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09797 |
| UNIT-4116 | ORIGINAL_TEXT | ### 矿区地质构造 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09799 |
| UNIT-4117 | ORIGINAL_TEXT | ### 矿区地质构造 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09805 |
| UNIT-4118 | ORIGINAL_TEXT | ### 矿区地质构造 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09807 |
| UNIT-4119 | ORIGINAL_TEXT | ### 矿区地质构造 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09809 |
| UNIT-4120 | ORIGINAL_TEXT | ### 矿区地质构造 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09815 |
| UNIT-4121 | ORIGINAL_TEXT | ### 矿区地质构造 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09817 |
| UNIT-4122 | ORIGINAL_TEXT | ### 矿区地质构造 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09819 |
| UNIT-4123 | ORIGINAL_TEXT | ### 矿区地质构造 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09825 |
| ... | ... | Additional 15 units in JSON inventory | ... | ... | ... |

### SEC-425 结论与建议 > 下步建议 > #### 矿体形态、产状

- Source locator: L09891
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### 矿体形态、产状` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-4139 #### 矿体形态、产状；UNIT-4140 #### 矿体形态、产状
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-4139 | ORIGINAL_TEXT | #### 矿体形态、产状 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09893 |
| UNIT-4140 | ORIGINAL_TEXT | #### 矿体形态、产状 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09895 |

### SEC-426 结论与建议 > 下步建议 > #### 规模

- Source locator: L09897
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### 规模` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-4141 #### 规模
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-4141 | ORIGINAL_TEXT | #### 规模 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09899 |

### SEC-428 结论与建议 > 下步建议 > #### 矿石的岩石学特征

- Source locator: L09903
- Material density: 3段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### 矿石的岩石学特征` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-4142 #### 矿石的岩石学特征；UNIT-4143 #### 矿石的岩石学特征；UNIT-4144 #### 矿石的岩石学特征
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-4142 | ORIGINAL_TEXT | #### 矿石的岩石学特征 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09907 |
| UNIT-4143 | ORIGINAL_TEXT | #### 矿石的岩石学特征 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09909 |
| UNIT-4144 | ORIGINAL_TEXT | #### 矿石的岩石学特征 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09911 |

### SEC-429 结论与建议 > 下步建议 > #### 矿石化学特征

- Source locator: L09913
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### 矿石化学特征` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-4145 #### 矿石化学特征
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-4145 | ORIGINAL_TEXT | #### 矿石化学特征 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09915 |

### SEC-430 结论与建议 > 下步建议 > #### 矿石放射性

- Source locator: L09917
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### 矿石放射性` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-4146 #### 矿石放射性；UNIT-4147 #### 矿石放射性
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-4146 | ORIGINAL_TEXT | #### 矿石放射性 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09919 |
| UNIT-4147 | ORIGINAL_TEXT | #### 矿石放射性 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09921 |

### SEC-433 结论与建议 > 下步建议 > #### 破碎加工工艺流程

- Source locator: L09929
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### 破碎加工工艺流程` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-4148 #### 破碎加工工艺流程
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-4148 | ORIGINAL_TEXT | #### 破碎加工工艺流程 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09931 |

### SEC-434 结论与建议 > 下步建议 > ### 矿体资源量

- Source locator: L09939
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### 矿体资源量` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-4149 ### 矿体资源量
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-4149 | ORIGINAL_TEXT | ### 矿体资源量 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09949 |

### SEC-437 结论与建议 > 下步建议 > #### 松散岩类孔隙水含水层

- Source locator: L09957
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### 松散岩类孔隙水含水层` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-4150 #### 松散岩类孔隙水含水层
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-4150 | ORIGINAL_TEXT | #### 松散岩类孔隙水含水层 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09959 |

### SEC-438 结论与建议 > 下步建议 > #### 碳酸盐岩类裂隙溶洞水含水层

- Source locator: L09961
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### 碳酸盐岩类裂隙溶洞水含水层` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-4151 #### 碳酸盐岩类裂隙溶洞水含水层
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-4151 | ORIGINAL_TEXT | #### 碳酸盐岩类裂隙溶洞水含水层 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09963 |

### SEC-440 结论与建议 > 下步建议 > #### 可溶岩的分布与埋藏条件

- Source locator: L09967
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### 可溶岩的分布与埋藏条件` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-4152 #### 可溶岩的分布与埋藏条件；UNIT-4153 #### 可溶岩的分布与埋藏条件
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-4152 | ORIGINAL_TEXT | #### 可溶岩的分布与埋藏条件 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09969 |
| UNIT-4153 | ORIGINAL_TEXT | #### 可溶岩的分布与埋藏条件 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09971 |

### SEC-441 结论与建议 > 下步建议 > #### 可溶岩岩溶发育特征

- Source locator: L09973
- Material density: 449段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### 可溶岩岩溶发育特征` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-4154 #### 可溶岩岩溶发育特征；UNIT-4155 #### 可溶岩岩溶发育特征；UNIT-4156 #### 可溶岩岩溶发育特征；UNIT-4157 #### 可溶岩岩溶发育特征；UNIT-4158 #### 可溶岩岩溶发育特征
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-4154 | ORIGINAL_TEXT | #### 可溶岩岩溶发育特征 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09975 |
| UNIT-4155 | ORIGINAL_TEXT | #### 可溶岩岩溶发育特征 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L09997 |
| UNIT-4156 | ORIGINAL_TEXT | #### 可溶岩岩溶发育特征 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L10017 |
| UNIT-4157 | ORIGINAL_TEXT | #### 可溶岩岩溶发育特征 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L10019 |
| UNIT-4158 | ORIGINAL_TEXT | #### 可溶岩岩溶发育特征 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L10027 |
| UNIT-4159 | ORIGINAL_TEXT | #### 可溶岩岩溶发育特征 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L10029 |
| UNIT-4160 | ORIGINAL_TEXT | #### 可溶岩岩溶发育特征 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L10031 |
| UNIT-4161 | ORIGINAL_TEXT | #### 可溶岩岩溶发育特征 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L10033 |
| UNIT-4162 | ORIGINAL_TEXT | #### 可溶岩岩溶发育特征 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L10035 |
| UNIT-4163 | ORIGINAL_TEXT | #### 可溶岩岩溶发育特征 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L10037 |
| UNIT-4164 | ORIGINAL_TEXT | #### 可溶岩岩溶发育特征 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L10039 |
| UNIT-4165 | ORIGINAL_TEXT | #### 可溶岩岩溶发育特征 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L10041 |
| ... | ... | Additional 437 units in JSON inventory | ... | ... | ... |

### SEC-442 结论与建议 > 下步建议 > #### 岩溶发育规律控制因素分析

- Source locator: L10977
- Material density: 21段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### 岩溶发育规律控制因素分析` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-4603 #### 岩溶发育规律控制因素分析；UNIT-4604 #### 岩溶发育规律控制因素分析；UNIT-4605 #### 岩溶发育规律控制因素分析；UNIT-4606 #### 岩溶发育规律控制因素分析；UNIT-4607 #### 岩溶发育规律控制因素分析
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-4603 | ORIGINAL_TEXT | #### 岩溶发育规律控制因素分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L10979 |
| UNIT-4604 | ORIGINAL_TEXT | #### 岩溶发育规律控制因素分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L10981 |
| UNIT-4605 | ORIGINAL_TEXT | #### 岩溶发育规律控制因素分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L10983 |
| UNIT-4606 | ORIGINAL_TEXT | #### 岩溶发育规律控制因素分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L10985 |
| UNIT-4607 | ORIGINAL_TEXT | #### 岩溶发育规律控制因素分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L10987 |
| UNIT-4608 | ORIGINAL_TEXT | #### 岩溶发育规律控制因素分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L10989 |
| UNIT-4609 | ORIGINAL_TEXT | #### 岩溶发育规律控制因素分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L10991 |
| UNIT-4610 | ORIGINAL_TEXT | #### 岩溶发育规律控制因素分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L10993 |
| UNIT-4611 | ORIGINAL_TEXT | #### 岩溶发育规律控制因素分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L10995 |
| UNIT-4612 | ORIGINAL_TEXT | #### 岩溶发育规律控制因素分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L10997 |
| UNIT-4613 | ORIGINAL_TEXT | #### 岩溶发育规律控制因素分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L10999 |
| UNIT-4614 | ORIGINAL_TEXT | #### 岩溶发育规律控制因素分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11003 |
| ... | ... | Additional 9 units in JSON inventory | ... | ... | ... |

### SEC-443 结论与建议 > 下步建议 > ### 矿区强径流带特征

- Source locator: L11023
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### 矿区强径流带特征` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-4624 ### 矿区强径流带特征；UNIT-4625 ### 矿区强径流带特征
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_text_right_table or top_text_bottom_table
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-4624 | ORIGINAL_TEXT | ### 矿区强径流带特征 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11025 |
| UNIT-4625 | CALCULATION | ### 矿区强径流带特征 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L11027 |

### SEC-444 结论与建议 > 下步建议 > #### 强径流带

- Source locator: L11029
- Material density: 29段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### 强径流带` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-4626 #### 强径流带；UNIT-4627 #### 强径流带；UNIT-4628 #### 强径流带；UNIT-4629 #### 强径流带；UNIT-4630 #### 强径流带
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-4626 | ORIGINAL_TEXT | #### 强径流带 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11031 |
| UNIT-4627 | ORIGINAL_TEXT | #### 强径流带 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11035 |
| UNIT-4628 | ORIGINAL_TEXT | #### 强径流带 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11037 |
| UNIT-4629 | ORIGINAL_TEXT | #### 强径流带 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11039 |
| UNIT-4630 | ORIGINAL_TEXT | #### 强径流带 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11041 |
| UNIT-4631 | ORIGINAL_TEXT | #### 强径流带 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11045 |
| UNIT-4632 | ORIGINAL_TEXT | #### 强径流带 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11049 |
| UNIT-4633 | ORIGINAL_TEXT | #### 强径流带 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11051 |
| UNIT-4634 | ORIGINAL_TEXT | #### 强径流带 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11053 |
| UNIT-4635 | ORIGINAL_TEXT | #### 强径流带 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11055 |
| UNIT-4636 | ORIGINAL_TEXT | #### 强径流带 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11057 |
| UNIT-4637 | ORIGINAL_TEXT | #### 强径流带 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11059 |
| ... | ... | Additional 17 units in JSON inventory | ... | ... | ... |

### SEC-445 结论与建议 > 下步建议 > #### 中等径流带

- Source locator: L11099
- Material density: 31段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### 中等径流带` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-4655 #### 中等径流带；UNIT-4656 #### 中等径流带；UNIT-4657 #### 中等径流带；UNIT-4658 #### 中等径流带；UNIT-4659 #### 中等径流带
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-4655 | ORIGINAL_TEXT | #### 中等径流带 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11101 |
| UNIT-4656 | ORIGINAL_TEXT | #### 中等径流带 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11103 |
| UNIT-4657 | ORIGINAL_TEXT | #### 中等径流带 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11105 |
| UNIT-4658 | ORIGINAL_TEXT | #### 中等径流带 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11107 |
| UNIT-4659 | ORIGINAL_TEXT | #### 中等径流带 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11109 |
| UNIT-4660 | ORIGINAL_TEXT | #### 中等径流带 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11113 |
| UNIT-4661 | ORIGINAL_TEXT | #### 中等径流带 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11115 |
| UNIT-4662 | ORIGINAL_TEXT | #### 中等径流带 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11117 |
| UNIT-4663 | ORIGINAL_TEXT | #### 中等径流带 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11119 |
| UNIT-4664 | ORIGINAL_TEXT | #### 中等径流带 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11121 |
| UNIT-4665 | ORIGINAL_TEXT | #### 中等径流带 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11123 |
| UNIT-4666 | ORIGINAL_TEXT | #### 中等径流带 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11125 |
| ... | ... | Additional 19 units in JSON inventory | ... | ... | ... |

### SEC-446 结论与建议 > 下步建议 > ### 地下水补径排特征

- Source locator: L11171
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### 地下水补径排特征` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-4686 ### 地下水补径排特征
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-4686 | ORIGINAL_TEXT | ### 地下水补径排特征 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11173 |

### SEC-447 结论与建议 > 下步建议 > #### 地下水补给特征及边界来水通道

- Source locator: L11175
- Material density: 5段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### 地下水补给特征及边界来水通道` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-4687 #### 地下水补给特征及边界来水通道；UNIT-4688 #### 地下水补给特征及边界来水通道；UNIT-4689 #### 地下水补给特征及边界来水通道；UNIT-4690 #### 地下水补给特征及边界来水通道；UNIT-4691 #### 地下水补给特征及边界来水通道
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-4687 | ORIGINAL_TEXT | #### 地下水补给特征及边界来水通道 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11177 |
| UNIT-4688 | ORIGINAL_TEXT | #### 地下水补给特征及边界来水通道 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11179 |
| UNIT-4689 | ORIGINAL_TEXT | #### 地下水补给特征及边界来水通道 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11181 |
| UNIT-4690 | ORIGINAL_TEXT | #### 地下水补给特征及边界来水通道 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11183 |
| UNIT-4691 | ORIGINAL_TEXT | #### 地下水补给特征及边界来水通道 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11185 |

### SEC-448 结论与建议 > 下步建议 > #### 地下水径流特征

- Source locator: L11187
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### 地下水径流特征` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-4692 #### 地下水径流特征；UNIT-4693 #### 地下水径流特征
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-4692 | ORIGINAL_TEXT | #### 地下水径流特征 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11191 |
| UNIT-4693 | ORIGINAL_TEXT | #### 地下水径流特征 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11193 |

### SEC-449 结论与建议 > 下步建议 > #### 地下水排泄特征及出口通道

- Source locator: L11195
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### 地下水排泄特征及出口通道` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-4694 #### 地下水排泄特征及出口通道
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-4694 | ORIGINAL_TEXT | #### 地下水排泄特征及出口通道 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11197 |

### SEC-450 结论与建议 > 下步建议 > #### 地下水补径排关系总结

- Source locator: L11199
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### 地下水补径排关系总结` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-4695 #### 地下水补径排关系总结
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-4695 | ORIGINAL_TEXT | #### 地下水补径排关系总结 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11201 |

### SEC-452 结论与建议 > 下步建议 > #### 现状地下水水位

- Source locator: L11205
- Material density: 4段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### 现状地下水水位` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-4696 #### 现状地下水水位；UNIT-4697 #### 现状地下水水位；UNIT-4698 #### 现状地下水水位；UNIT-4699 #### 现状地下水水位
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-4696 | ORIGINAL_TEXT | #### 现状地下水水位 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11207 |
| UNIT-4697 | ORIGINAL_TEXT | #### 现状地下水水位 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11209 |
| UNIT-4698 | ORIGINAL_TEXT | #### 现状地下水水位 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11211 |
| UNIT-4699 | ORIGINAL_TEXT | #### 现状地下水水位 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11213 |

### SEC-453 结论与建议 > 下步建议 > #### 长期地下水位动态观测

- Source locator: L11221
- Material density: 4段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### 长期地下水位动态观测` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-4700 #### 长期地下水位动态观测；UNIT-4701 #### 长期地下水位动态观测；UNIT-4702 #### 长期地下水位动态观测；UNIT-4703 #### 长期地下水位动态观测
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-4700 | ORIGINAL_TEXT | #### 长期地下水位动态观测 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11223 |
| UNIT-4701 | ORIGINAL_TEXT | #### 长期地下水位动态观测 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11229 |
| UNIT-4702 | ORIGINAL_TEXT | #### 长期地下水位动态观测 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11233 |
| UNIT-4703 | ORIGINAL_TEXT | #### 长期地下水位动态观测 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11237 |

### SEC-454 结论与建议 > 下步建议 > ### 涌水量动态特征

- Source locator: L11239
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### 涌水量动态特征` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-4704 ### 涌水量动态特征
  - Best source pairing: left_text_right_table or top_text_bottom_table
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-4704 | CALCULATION | ### 涌水量动态特征 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L11241 |

### SEC-456 结论与建议 > 下步建议 > #### 大气降水

- Source locator: L11249
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### 大气降水` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-4705 #### 大气降水
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-4705 | ORIGINAL_TEXT | #### 大气降水 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11253 |

### SEC-457 结论与建议 > 下步建议 > #### 地表水

- Source locator: L11257
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### 地表水` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-4706 #### 地表水
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-4706 | ORIGINAL_TEXT | #### 地表水 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11259 |

### SEC-459 结论与建议 > 下步建议 > ##### 第四系残坡积层孔隙水

- Source locator: L11263
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `##### 第四系残坡积层孔隙水` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-4707 ##### 第四系残坡积层孔隙水
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-4707 | ORIGINAL_TEXT | ##### 第四系残坡积层孔隙水 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11265 |

### SEC-460 结论与建议 > 下步建议 > ##### 石炭系碳酸盐岩裂隙溶洞水

- Source locator: L11267
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `##### 石炭系碳酸盐岩裂隙溶洞水` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-4708 ##### 石炭系碳酸盐岩裂隙溶洞水
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-4708 | ORIGINAL_TEXT | ##### 石炭系碳酸盐岩裂隙溶洞水 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11269 |

### SEC-461 结论与建议 > 下步建议 > ## <a id="_Toc11822"></a>矿区水文地质勘查类型

- Source locator: L11271
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `## <a id="_Toc11822"></a>矿区水文地质勘查类型` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-4709 ## <a id="_Toc11822"></a>矿区水文地质勘查类型；UNIT-4710 ## <a id="_Toc11822"></a>矿区水文地质勘查类型
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-4709 | ORIGINAL_TEXT | ## <a id="_Toc11822"></a>矿区水文地质勘查类型 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11273 |
| UNIT-4710 | ORIGINAL_TEXT | ## <a id="_Toc11822"></a>矿区水文地质勘查类型 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11275 |

### SEC-463 结论与建议 > 下步建议 > ## <a id="_Toc10241"></a><a id="_Toc14925"></a><a id="_Toc31712"></a><a id="_Toc10016"></a><a id="_Toc17214"></a><a id="_Toc23946"></a><a id="_Toc10097"></a><a id="_Toc7757"></a>涌突水影响因素分析

- Source locator: L11281
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `## <a id="_Toc10241"></a><a id="_Toc14925"></a><a id="_Toc31712"></a><a id="_Toc10016"></a><a id="_Toc17214"></a><a id="_Toc23946"></a><a id="_Toc10097"></a><a id="_Toc7757"></a>涌突水影响因素分析` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-4711 ## <a id="_Toc10241"></a><a id="_Toc14925…
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-4711 | ORIGINAL_TEXT | ## <a id="_Toc10241"></a><a id="_Toc14925… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11283 |

### SEC-464 结论与建议 > 下步建议 > ### 大气降水对矿段涌水量的影响

- Source locator: L11285
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### 大气降水对矿段涌水量的影响` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-4712 ### 大气降水对矿段涌水量的影响
  - Best source pairing: left_text_right_table or top_text_bottom_table
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-4712 | CALCULATION | ### 大气降水对矿段涌水量的影响 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L11287 |

### SEC-465 结论与建议 > 下步建议 > ### 地表水对矿段涌水的影响

- Source locator: L11289
- Material density: 3段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### 地表水对矿段涌水的影响` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-4713 ### 地表水对矿段涌水的影响；UNIT-4714 ### 地表水对矿段涌水的影响；UNIT-4715 ### 地表水对矿段涌水的影响
  - Best source pairing: left_text_right_table or top_text_bottom_table；left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-4713 | CALCULATION | ### 地表水对矿段涌水的影响 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L11291 |
| UNIT-4714 | ORIGINAL_TEXT | ### 地表水对矿段涌水的影响 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11293 |
| UNIT-4715 | ORIGINAL_TEXT | ### 地表水对矿段涌水的影响 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11295 |

### SEC-466 结论与建议 > 下步建议 > ### 构造对矿段涌突水的影响

- Source locator: L11297
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### 构造对矿段涌突水的影响` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-4716 ### 构造对矿段涌突水的影响
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-4716 | ORIGINAL_TEXT | ### 构造对矿段涌突水的影响 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11299 |

### SEC-468 结论与建议 > 下步建议 > #### 平面岩溶非均质性对涌突水的影响

- Source locator: L11305
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### 平面岩溶非均质性对涌突水的影响` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-4717 #### 平面岩溶非均质性对涌突水的影响
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-4717 | ORIGINAL_TEXT | #### 平面岩溶非均质性对涌突水的影响 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11307 |

### SEC-469 结论与建议 > 下步建议 > #### 垂向岩溶分带性对涌突水的影响

- Source locator: L11309
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### 垂向岩溶分带性对涌突水的影响` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-4718 #### 垂向岩溶分带性对涌突水的影响
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-4718 | ORIGINAL_TEXT | #### 垂向岩溶分带性对涌突水的影响 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11311 |

### SEC-470 结论与建议 > 下步建议 > ### 小结

- Source locator: L11313
- Material density: 5段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### 小结` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-4719 ### 小结；UNIT-4720 ### 小结；UNIT-4721 ### 小结；UNIT-4722 ### 小结；UNIT-4723 ### 小结
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-4719 | ORIGINAL_TEXT | ### 小结 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11315 |
| UNIT-4720 | ORIGINAL_TEXT | ### 小结 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11317 |
| UNIT-4721 | ORIGINAL_TEXT | ### 小结 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11319 |
| UNIT-4722 | ORIGINAL_TEXT | ### 小结 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11321 |
| UNIT-4723 | ORIGINAL_TEXT | ### 小结 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11323 |

### SEC-471 结论与建议 > 下步建议 > ## <a id="_Toc17417"></a><a id="_Toc32730"></a><a id="_Toc9447"></a><a id="_Toc17299"></a><a id="_Toc1121"></a><a id="_Toc31658"></a><a id="_Toc5050"></a><a id="_Toc1963"></a>含水层富水性评价与分区

- Source locator: L11325
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `## <a id="_Toc17417"></a><a id="_Toc32730"></a><a id="_Toc9447"></a><a id="_Toc17299"></a><a id="_Toc1121"></a><a id="_Toc31658"></a><a id="_Toc5050"></a><a id="_Toc1963"></a>含水层富水性评价与分区` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-4724 ## <a id="_Toc17417"></a><a id="_Toc32730…
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-4724 | ORIGINAL_TEXT | ## <a id="_Toc17417"></a><a id="_Toc32730… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11327 |

### SEC-472 结论与建议 > 下步建议 > ### 主控因素专题图

- Source locator: L11329
- Material density: 9段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### 主控因素专题图` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-4725 ### 主控因素专题图；UNIT-4726 ### 主控因素专题图；UNIT-4727 ### 主控因素专题图；UNIT-4728 ### 主控因素专题图；UNIT-4729 ### 主控因素专题图
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-4725 | ORIGINAL_TEXT | ### 主控因素专题图 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11345 |
| UNIT-4726 | ORIGINAL_TEXT | ### 主控因素专题图 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11347 |
| UNIT-4727 | ORIGINAL_TEXT | ### 主控因素专题图 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11349 |
| UNIT-4728 | ORIGINAL_TEXT | ### 主控因素专题图 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11351 |
| UNIT-4729 | ORIGINAL_TEXT | ### 主控因素专题图 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11353 |
| UNIT-4730 | ORIGINAL_TEXT | ### 主控因素专题图 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11355 |
| UNIT-4731 | ORIGINAL_TEXT | ### 主控因素专题图 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11357 |
| UNIT-4732 | ORIGINAL_TEXT | ### 主控因素专题图 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11359 |
| UNIT-4733 | ORIGINAL_TEXT | ### 主控因素专题图 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11361 |

### SEC-473 结论与建议 > 下步建议 > ### 富水性分区

- Source locator: L11363
- Material density: 16段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### 富水性分区` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-4734 ### 富水性分区；UNIT-4735 ### 富水性分区；UNIT-4736 ### 富水性分区；UNIT-4737 ### 富水性分区；UNIT-4738 ### 富水性分区
  - Best source pairing: left_text_right_table or top_text_bottom_table；left_text_right_figure or text_with_keypoints
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-4734 | CALCULATION | ### 富水性分区 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L11365 |
| UNIT-4735 | ORIGINAL_TEXT | ### 富水性分区 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11367 |
| UNIT-4736 | ORIGINAL_TEXT | ### 富水性分区 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11369 |
| UNIT-4737 | CALCULATION | ### 富水性分区 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L11371 |
| UNIT-4738 | CALCULATION | ### 富水性分区 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L11373 |
| UNIT-4739 | ORIGINAL_TEXT | ### 富水性分区 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11375 |
| UNIT-4740 | CALCULATION | ### 富水性分区 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L11379 |
| UNIT-4741 | ORIGINAL_TEXT | ### 富水性分区 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11381 |
| UNIT-4742 | ORIGINAL_TEXT | ### 富水性分区 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11387 |
| UNIT-4743 | ORIGINAL_TEXT | ### 富水性分区 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11389 |
| UNIT-4744 | ORIGINAL_TEXT | ### 富水性分区 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11391 |
| UNIT-4745 | ORIGINAL_TEXT | ### 富水性分区 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11393 |
| ... | ... | Additional 4 units in JSON inventory | ... | ... | ... |

### SEC-476 结论与建议 > 下步建议 > ### 模型范围

- Source locator: L11409
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### 模型范围` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-4750 ### 模型范围
  - Best source pairing: left_text_right_table or top_text_bottom_table
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-4750 | CALCULATION | ### 模型范围 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L11411 |

### SEC-477 结论与建议 > 下步建议 > ### 模型概化

- Source locator: L11417
- Material density: 7段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### 模型概化` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-4751 ### 模型概化；UNIT-4752 ### 模型概化；UNIT-4753 ### 模型概化；UNIT-4754 ### 模型概化；UNIT-4755 ### 模型概化
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_text_right_table or top_text_bottom_table
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-4751 | ORIGINAL_TEXT | ### 模型概化 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11419 |
| UNIT-4752 | ORIGINAL_TEXT | ### 模型概化 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11421 |
| UNIT-4753 | ORIGINAL_TEXT | ### 模型概化 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11423 |
| UNIT-4754 | ORIGINAL_TEXT | ### 模型概化 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11425 |
| UNIT-4755 | CALCULATION | ### 模型概化 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L11427 |
| UNIT-4756 | ORIGINAL_TEXT | ### 模型概化 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11429 |
| UNIT-4757 | ORIGINAL_TEXT | ### 模型概化 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11431 |

### SEC-478 结论与建议 > 下步建议 > ### 模型边界概化

- Source locator: L11433
- Material density: 6段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### 模型边界概化` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-4758 ### 模型边界概化；UNIT-4759 ### 模型边界概化；UNIT-4760 ### 模型边界概化；UNIT-4761 ### 模型边界概化；UNIT-4762 ### 模型边界概化
  - Best source pairing: left_text_right_table or top_text_bottom_table
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-4758 | CALCULATION | ### 模型边界概化 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L11435 |
| UNIT-4759 | CALCULATION | ### 模型边界概化 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L11437 |
| UNIT-4760 | CALCULATION | ### 模型边界概化 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L11439 |
| UNIT-4761 | CALCULATION | ### 模型边界概化 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L11441 |
| UNIT-4762 | CALCULATION | ### 模型边界概化 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L11443 |
| UNIT-4763 | CALCULATION | ### 模型边界概化 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L11445 |

### SEC-479 结论与建议 > 下步建议 > ## <a id="_Toc3917"></a><a id="_Toc15300"></a><a id="_Toc13879"></a><a id="_Toc10378"></a><a id="_Toc29285"></a>水文地质比拟法预测矿坑涌水量

- Source locator: L11451
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `## <a id="_Toc3917"></a><a id="_Toc15300"></a><a id="_Toc13879"></a><a id="_Toc10378"></a><a id="_Toc29285"></a>水文地质比拟法预测矿坑涌水量` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-4764 ## <a id="_Toc3917"></a><a id="_Toc15300"…
  - Best source pairing: left_text_right_table or top_text_bottom_table
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-4764 | CALCULATION | ## <a id="_Toc3917"></a><a id="_Toc15300"… | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L11453 |

### SEC-480 结论与建议 > 下步建议 > ### 地表水汇入采坑水量计算

- Source locator: L11455
- Material density: 132段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### 地表水汇入采坑水量计算` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-4765 ### 地表水汇入采坑水量计算；UNIT-4766 ### 地表水汇入采坑水量计算；UNIT-4767 ### 地表水汇入采坑水量计算；UNIT-4768 ### 地表水汇入采坑水量计算；UNIT-4769 ### 地表水汇入采坑水量计算
  - Best source pairing: left_text_right_table or top_text_bottom_table；left_text_right_figure or text_with_keypoints
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-4765 | CALCULATION | ### 地表水汇入采坑水量计算 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L11457 |
| UNIT-4766 | ORIGINAL_TEXT | ### 地表水汇入采坑水量计算 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11459 |
| UNIT-4767 | ORIGINAL_TEXT | ### 地表水汇入采坑水量计算 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11481 |
| UNIT-4768 | ORIGINAL_TEXT | ### 地表水汇入采坑水量计算 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11483 |
| UNIT-4769 | ORIGINAL_TEXT | ### 地表水汇入采坑水量计算 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11491 |
| UNIT-4770 | ORIGINAL_TEXT | ### 地表水汇入采坑水量计算 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11493 |
| UNIT-4771 | ORIGINAL_TEXT | ### 地表水汇入采坑水量计算 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11495 |
| UNIT-4772 | ORIGINAL_TEXT | ### 地表水汇入采坑水量计算 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11501 |
| UNIT-4773 | ORIGINAL_TEXT | ### 地表水汇入采坑水量计算 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11505 |
| UNIT-4774 | ORIGINAL_TEXT | ### 地表水汇入采坑水量计算 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11513 |
| UNIT-4775 | ORIGINAL_TEXT | ### 地表水汇入采坑水量计算 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11515 |
| UNIT-4776 | ORIGINAL_TEXT | ### 地表水汇入采坑水量计算 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11517 |
| ... | ... | Additional 120 units in JSON inventory | ... | ... | ... |

### SEC-481 结论与建议 > 下步建议 > ### 降水渗入采坑水量计算

- Source locator: L11801
- Material density: 62段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### 降水渗入采坑水量计算` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-4897 ### 降水渗入采坑水量计算；UNIT-4898 ### 降水渗入采坑水量计算；UNIT-4899 ### 降水渗入采坑水量计算；UNIT-4900 ### 降水渗入采坑水量计算；UNIT-4901 ### 降水渗入采坑水量计算
  - Best source pairing: left_text_right_table or top_text_bottom_table；left_text_right_figure or text_with_keypoints
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-4897 | CALCULATION | ### 降水渗入采坑水量计算 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L11803 |
| UNIT-4898 | CALCULATION | ### 降水渗入采坑水量计算 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L11805 |
| UNIT-4899 | ORIGINAL_TEXT | ### 降水渗入采坑水量计算 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11809 |
| UNIT-4900 | ORIGINAL_TEXT | ### 降水渗入采坑水量计算 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11829 |
| UNIT-4901 | ORIGINAL_TEXT | ### 降水渗入采坑水量计算 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11831 |
| UNIT-4902 | ORIGINAL_TEXT | ### 降水渗入采坑水量计算 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11835 |
| UNIT-4903 | ORIGINAL_TEXT | ### 降水渗入采坑水量计算 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11837 |
| UNIT-4904 | ORIGINAL_TEXT | ### 降水渗入采坑水量计算 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11841 |
| UNIT-4905 | ORIGINAL_TEXT | ### 降水渗入采坑水量计算 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11843 |
| UNIT-4906 | ORIGINAL_TEXT | ### 降水渗入采坑水量计算 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11849 |
| UNIT-4907 | ORIGINAL_TEXT | ### 降水渗入采坑水量计算 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11851 |
| UNIT-4908 | ORIGINAL_TEXT | ### 降水渗入采坑水量计算 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L11853 |
| ... | ... | Additional 50 units in JSON inventory | ... | ... | ... |

### SEC-482 结论与建议 > 下步建议 > ### 露天采坑地下水涌水量的比拟计算

- Source locator: L12057
- Material density: 25段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### 露天采坑地下水涌水量的比拟计算` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-4959 ### 露天采坑地下水涌水量的比拟计算；UNIT-4960 ### 露天采坑地下水涌水量的比拟计算；UNIT-4961 ### 露天采坑地下水涌水量的比拟计算；UNIT-4962 ### 露天采坑地下水涌水量的比拟计算；UNIT-4963 ### 露天采坑地下水涌水量的比拟计算
  - Best source pairing: left_text_right_table or top_text_bottom_table；left_text_right_figure or text_with_keypoints
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-4959 | CALCULATION | ### 露天采坑地下水涌水量的比拟计算 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L12059 |
| UNIT-4960 | ORIGINAL_TEXT | ### 露天采坑地下水涌水量的比拟计算 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12061 |
| UNIT-4961 | ORIGINAL_TEXT | ### 露天采坑地下水涌水量的比拟计算 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12087 |
| UNIT-4962 | ORIGINAL_TEXT | ### 露天采坑地下水涌水量的比拟计算 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12097 |
| UNIT-4963 | ORIGINAL_TEXT | ### 露天采坑地下水涌水量的比拟计算 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12101 |
| UNIT-4964 | ORIGINAL_TEXT | ### 露天采坑地下水涌水量的比拟计算 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12105 |
| UNIT-4965 | ORIGINAL_TEXT | ### 露天采坑地下水涌水量的比拟计算 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12109 |
| UNIT-4966 | ORIGINAL_TEXT | ### 露天采坑地下水涌水量的比拟计算 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12115 |
| UNIT-4967 | ORIGINAL_TEXT | ### 露天采坑地下水涌水量的比拟计算 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12119 |
| UNIT-4968 | ORIGINAL_TEXT | ### 露天采坑地下水涌水量的比拟计算 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12123 |
| UNIT-4969 | ORIGINAL_TEXT | ### 露天采坑地下水涌水量的比拟计算 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12127 |
| UNIT-4970 | ORIGINAL_TEXT | ### 露天采坑地下水涌水量的比拟计算 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12131 |
| ... | ... | Additional 13 units in JSON inventory | ... | ... | ... |

### SEC-483 结论与建议 > 下步建议 > ### 露天矿矿坑总涌水量

- Source locator: L12181
- Material density: 35段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### 露天矿矿坑总涌水量` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-4984 ### 露天矿矿坑总涌水量；UNIT-4985 ### 露天矿矿坑总涌水量；UNIT-4986 ### 露天矿矿坑总涌水量；UNIT-4987 ### 露天矿矿坑总涌水量；UNIT-4988 ### 露天矿矿坑总涌水量
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-4984 | ORIGINAL_TEXT | ### 露天矿矿坑总涌水量 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12199 |
| UNIT-4985 | ORIGINAL_TEXT | ### 露天矿矿坑总涌水量 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12203 |
| UNIT-4986 | ORIGINAL_TEXT | ### 露天矿矿坑总涌水量 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12209 |
| UNIT-4987 | ORIGINAL_TEXT | ### 露天矿矿坑总涌水量 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12211 |
| UNIT-4988 | ORIGINAL_TEXT | ### 露天矿矿坑总涌水量 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12213 |
| UNIT-4989 | ORIGINAL_TEXT | ### 露天矿矿坑总涌水量 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12217 |
| UNIT-4990 | ORIGINAL_TEXT | ### 露天矿矿坑总涌水量 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12219 |
| UNIT-4991 | ORIGINAL_TEXT | ### 露天矿矿坑总涌水量 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12221 |
| UNIT-4992 | ORIGINAL_TEXT | ### 露天矿矿坑总涌水量 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12225 |
| UNIT-4993 | ORIGINAL_TEXT | ### 露天矿矿坑总涌水量 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12227 |
| UNIT-4994 | ORIGINAL_TEXT | ### 露天矿矿坑总涌水量 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12229 |
| UNIT-4995 | ORIGINAL_TEXT | ### 露天矿矿坑总涌水量 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12233 |
| ... | ... | Additional 23 units in JSON inventory | ... | ... | ... |

### SEC-485 结论与建议 > 下步建议 > ### 计算公式的选取

- Source locator: L12309
- Material density: 4段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### 计算公式的选取` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-5019 ### 计算公式的选取；UNIT-5020 ### 计算公式的选取；UNIT-5021 ### 计算公式的选取；UNIT-5022 ### 计算公式的选取
  - Best source pairing: left_text_right_table or top_text_bottom_table；left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-5019 | CALCULATION | ### 计算公式的选取 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L12311 |
| UNIT-5020 | ORIGINAL_TEXT | ### 计算公式的选取 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12313 |
| UNIT-5021 | ORIGINAL_TEXT | ### 计算公式的选取 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12315 |
| UNIT-5022 | CALCULATION | ### 计算公式的选取 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L12317 |

### SEC-486 结论与建议 > 下步建议 > ### 水文地质参数的选取

- Source locator: L12319
- Material density: 29段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### 水文地质参数的选取` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-5023 ### 水文地质参数的选取；UNIT-5024 ### 水文地质参数的选取；UNIT-5025 ### 水文地质参数的选取；UNIT-5026 ### 水文地质参数的选取；UNIT-5027 ### 水文地质参数的选取
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_text_right_table or top_text_bottom_table
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-5023 | ORIGINAL_TEXT | ### 水文地质参数的选取 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12321 |
| UNIT-5024 | ORIGINAL_TEXT | ### 水文地质参数的选取 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12325 |
| UNIT-5025 | ORIGINAL_TEXT | ### 水文地质参数的选取 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12329 |
| UNIT-5026 | ORIGINAL_TEXT | ### 水文地质参数的选取 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12335 |
| UNIT-5027 | ORIGINAL_TEXT | ### 水文地质参数的选取 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12339 |
| UNIT-5028 | CALCULATION | ### 水文地质参数的选取 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L12341 |
| UNIT-5029 | CALCULATION | ### 水文地质参数的选取 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L12343 |
| UNIT-5030 | CALCULATION | ### 水文地质参数的选取 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L12345 |
| UNIT-5031 | ORIGINAL_TEXT | ### 水文地质参数的选取 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12357 |
| UNIT-5032 | ORIGINAL_TEXT | ### 水文地质参数的选取 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12359 |
| UNIT-5033 | ORIGINAL_TEXT | ### 水文地质参数的选取 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12361 |
| UNIT-5034 | ORIGINAL_TEXT | ### 水文地质参数的选取 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12365 |
| ... | ... | Additional 17 units in JSON inventory | ... | ... | ... |

### SEC-487 结论与建议 > 下步建议 > ### <a id="_Toc2145"></a><a id="_Toc27611"></a><a id="_Toc15945"></a><a id="_Toc18405"></a>解析法预测矿坑涌水量结果

- Source locator: L12411
- Material density: 17段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### <a id="_Toc2145"></a><a id="_Toc27611"></a><a id="_Toc15945"></a><a id="_Toc18405"></a>解析法预测矿坑涌水量结果` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-5052 ### <a id="_Toc2145"></a><a id="_Toc27611…；UNIT-5053 ### <a id="_Toc2145"></a><a id="_Toc27611…；UNIT-5054 ### <a id="_Toc2145"></a><a id="_Toc27611…；UNIT-5055 ### <a id="_Toc2145"></a><a id="_Toc27611…；UNIT-5056 ### <a id="_Toc2145"></a><a id="_Toc27611…
  - Best source pairing: left_text_right_table or top_text_bottom_table；left_text_right_figure or text_with_keypoints
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-5052 | CALCULATION | ### <a id="_Toc2145"></a><a id="_Toc27611… | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L12413 |
| UNIT-5053 | CALCULATION | ### <a id="_Toc2145"></a><a id="_Toc27611… | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L12415 |
| UNIT-5054 | ORIGINAL_TEXT | ### <a id="_Toc2145"></a><a id="_Toc27611… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12425 |
| UNIT-5055 | ORIGINAL_TEXT | ### <a id="_Toc2145"></a><a id="_Toc27611… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12427 |
| UNIT-5056 | ORIGINAL_TEXT | ### <a id="_Toc2145"></a><a id="_Toc27611… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12429 |
| UNIT-5057 | ORIGINAL_TEXT | ### <a id="_Toc2145"></a><a id="_Toc27611… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12435 |
| UNIT-5058 | ORIGINAL_TEXT | ### <a id="_Toc2145"></a><a id="_Toc27611… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12437 |
| UNIT-5059 | ORIGINAL_TEXT | ### <a id="_Toc2145"></a><a id="_Toc27611… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12439 |
| UNIT-5060 | ORIGINAL_TEXT | ### <a id="_Toc2145"></a><a id="_Toc27611… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12443 |
| UNIT-5061 | ORIGINAL_TEXT | ### <a id="_Toc2145"></a><a id="_Toc27611… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12445 |
| UNIT-5062 | ORIGINAL_TEXT | ### <a id="_Toc2145"></a><a id="_Toc27611… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12447 |
| UNIT-5063 | ORIGINAL_TEXT | ### <a id="_Toc2145"></a><a id="_Toc27611… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12451 |
| ... | ... | Additional 5 units in JSON inventory | ... | ... | ... |

### SEC-488 结论与建议 > 下步建议 > ## <a id="_Toc29317"></a>数值法预测矿坑涌水量

- Source locator: L12463
- Material density: 4段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `## <a id="_Toc29317"></a>数值法预测矿坑涌水量` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-5069 ## <a id="_Toc29317"></a>数值法预测矿坑涌水量；UNIT-5070 ## <a id="_Toc29317"></a>数值法预测矿坑涌水量；UNIT-5071 ## <a id="_Toc29317"></a>数值法预测矿坑涌水量；UNIT-5072 ## <a id="_Toc29317"></a>数值法预测矿坑涌水量
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-5069 | ORIGINAL_TEXT | ## <a id="_Toc29317"></a>数值法预测矿坑涌水量 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12485 |
| UNIT-5070 | ORIGINAL_TEXT | ## <a id="_Toc29317"></a>数值法预测矿坑涌水量 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12487 |
| UNIT-5071 | ORIGINAL_TEXT | ## <a id="_Toc29317"></a>数值法预测矿坑涌水量 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12489 |
| UNIT-5072 | ORIGINAL_TEXT | ## <a id="_Toc29317"></a>数值法预测矿坑涌水量 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12491 |

### SEC-489 结论与建议 > 下步建议 > ### 初始网格及地质模型

- Source locator: L12499
- Material density: 4段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### 初始网格及地质模型` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-5073 ### 初始网格及地质模型；UNIT-5074 ### 初始网格及地质模型；UNIT-5075 ### 初始网格及地质模型；UNIT-5076 ### 初始网格及地质模型
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_text_right_table or top_text_bottom_table
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-5073 | ORIGINAL_TEXT | ### 初始网格及地质模型 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12501 |
| UNIT-5074 | ORIGINAL_TEXT | ### 初始网格及地质模型 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12507 |
| UNIT-5075 | CALCULATION | ### 初始网格及地质模型 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L12509 |
| UNIT-5076 | CALCULATION | ### 初始网格及地质模型 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L12513 |

### SEC-490 结论与建议 > 下步建议 > ### 边界条件及初始参数

- Source locator: L12515
- Material density: 16段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### 边界条件及初始参数` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-5077 ### 边界条件及初始参数；UNIT-5078 ### 边界条件及初始参数；UNIT-5079 ### 边界条件及初始参数；UNIT-5080 ### 边界条件及初始参数；UNIT-5081 ### 边界条件及初始参数
  - Best source pairing: left_text_right_table or top_text_bottom_table；left_text_right_figure or text_with_keypoints
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-5077 | CALCULATION | ### 边界条件及初始参数 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L12517 |
| UNIT-5078 | CALCULATION | ### 边界条件及初始参数 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L12521 |
| UNIT-5079 | ORIGINAL_TEXT | ### 边界条件及初始参数 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12525 |
| UNIT-5080 | ORIGINAL_TEXT | ### 边界条件及初始参数 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12527 |
| UNIT-5081 | ORIGINAL_TEXT | ### 边界条件及初始参数 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12529 |
| UNIT-5082 | CALCULATION | ### 边界条件及初始参数 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L12531 |
| UNIT-5083 | CALCULATION | ### 边界条件及初始参数 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L12533 |
| UNIT-5084 | ORIGINAL_TEXT | ### 边界条件及初始参数 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12547 |
| UNIT-5085 | ORIGINAL_TEXT | ### 边界条件及初始参数 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12549 |
| UNIT-5086 | ORIGINAL_TEXT | ### 边界条件及初始参数 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12553 |
| UNIT-5087 | ORIGINAL_TEXT | ### 边界条件及初始参数 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12555 |
| UNIT-5088 | ORIGINAL_TEXT | ### 边界条件及初始参数 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12559 |
| ... | ... | Additional 4 units in JSON inventory | ... | ... | ... |

### SEC-491 结论与建议 > 下步建议 > ### 识别验证与初始条件

- Source locator: L12575
- Material density: 21段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### 识别验证与初始条件` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-5093 ### 识别验证与初始条件；UNIT-5094 ### 识别验证与初始条件；UNIT-5095 ### 识别验证与初始条件；UNIT-5096 ### 识别验证与初始条件；UNIT-5097 ### 识别验证与初始条件
  - Best source pairing: left_text_right_table or top_text_bottom_table；left_text_right_figure or text_with_keypoints
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-5093 | CALCULATION | ### 识别验证与初始条件 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L12577 |
| UNIT-5094 | CALCULATION | ### 识别验证与初始条件 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L12579 |
| UNIT-5095 | ORIGINAL_TEXT | ### 识别验证与初始条件 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12585 |
| UNIT-5096 | CALCULATION | ### 识别验证与初始条件 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L12587 |
| UNIT-5097 | CALCULATION | ### 识别验证与初始条件 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L12589 |
| UNIT-5098 | ORIGINAL_TEXT | ### 识别验证与初始条件 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12603 |
| UNIT-5099 | ORIGINAL_TEXT | ### 识别验证与初始条件 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12605 |
| UNIT-5100 | ORIGINAL_TEXT | ### 识别验证与初始条件 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12609 |
| UNIT-5101 | ORIGINAL_TEXT | ### 识别验证与初始条件 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12611 |
| UNIT-5102 | ORIGINAL_TEXT | ### 识别验证与初始条件 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12615 |
| UNIT-5103 | ORIGINAL_TEXT | ### 识别验证与初始条件 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12617 |
| UNIT-5104 | ORIGINAL_TEXT | ### 识别验证与初始条件 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12621 |
| ... | ... | Additional 9 units in JSON inventory | ... | ... | ... |

### SEC-492 结论与建议 > 下步建议 > ### 数值法预测矿坑涌水量结果

- Source locator: L12651
- Material density: 22段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### 数值法预测矿坑涌水量结果` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-5114 ### 数值法预测矿坑涌水量结果；UNIT-5115 ### 数值法预测矿坑涌水量结果；UNIT-5116 ### 数值法预测矿坑涌水量结果；UNIT-5117 ### 数值法预测矿坑涌水量结果；UNIT-5118 ### 数值法预测矿坑涌水量结果
  - Best source pairing: left_text_right_table or top_text_bottom_table；left_text_right_figure or text_with_keypoints
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-5114 | CALCULATION | ### 数值法预测矿坑涌水量结果 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L12653 |
| UNIT-5115 | CALCULATION | ### 数值法预测矿坑涌水量结果 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L12655 |
| UNIT-5116 | CALCULATION | ### 数值法预测矿坑涌水量结果 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L12657 |
| UNIT-5117 | ORIGINAL_TEXT | ### 数值法预测矿坑涌水量结果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12678 |
| UNIT-5118 | ORIGINAL_TEXT | ### 数值法预测矿坑涌水量结果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12688 |
| UNIT-5119 | ORIGINAL_TEXT | ### 数值法预测矿坑涌水量结果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12692 |
| UNIT-5120 | ORIGINAL_TEXT | ### 数值法预测矿坑涌水量结果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12696 |
| UNIT-5121 | ORIGINAL_TEXT | ### 数值法预测矿坑涌水量结果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12700 |
| UNIT-5122 | ORIGINAL_TEXT | ### 数值法预测矿坑涌水量结果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12706 |
| UNIT-5123 | ORIGINAL_TEXT | ### 数值法预测矿坑涌水量结果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12710 |
| UNIT-5124 | ORIGINAL_TEXT | ### 数值法预测矿坑涌水量结果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12714 |
| UNIT-5125 | ORIGINAL_TEXT | ### 数值法预测矿坑涌水量结果 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12718 |
| ... | ... | Additional 10 units in JSON inventory | ... | ... | ... |

### SEC-493 结论与建议 > 下步建议 > ## <a id="_Toc32443"></a>预测成果分析

- Source locator: L12752
- Material density: 7段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `## <a id="_Toc32443"></a>预测成果分析` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-5136 ## <a id="_Toc32443"></a>预测成果分析；UNIT-5137 ## <a id="_Toc32443"></a>预测成果分析；UNIT-5138 ## <a id="_Toc32443"></a>预测成果分析；UNIT-5139 ## <a id="_Toc32443"></a>预测成果分析；UNIT-5140 ## <a id="_Toc32443"></a>预测成果分析
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_text_right_table or top_text_bottom_table
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-5136 | ORIGINAL_TEXT | ## <a id="_Toc32443"></a>预测成果分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12754 |
| UNIT-5137 | CALCULATION | ## <a id="_Toc32443"></a>预测成果分析 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L12756 |
| UNIT-5138 | ORIGINAL_TEXT | ## <a id="_Toc32443"></a>预测成果分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12758 |
| UNIT-5139 | ORIGINAL_TEXT | ## <a id="_Toc32443"></a>预测成果分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12760 |
| UNIT-5140 | ORIGINAL_TEXT | ## <a id="_Toc32443"></a>预测成果分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12762 |
| UNIT-5141 | ORIGINAL_TEXT | ## <a id="_Toc32443"></a>预测成果分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12764 |
| UNIT-5142 | ORIGINAL_TEXT | ## <a id="_Toc32443"></a>预测成果分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12766 |

### SEC-496 结论与建议 > 下步建议 > ### 工程地质岩组的划分

- Source locator: L12772
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### 工程地质岩组的划分` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-5143 ### 工程地质岩组的划分
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-5143 | ORIGINAL_TEXT | ### 工程地质岩组的划分 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12774 |

### SEC-498 结论与建议 > 下步建议 > #### 坚硬岩组

- Source locator: L12780
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### 坚硬岩组` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-5144 #### 坚硬岩组
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-5144 | ORIGINAL_TEXT | #### 坚硬岩组 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12784 |

### SEC-499 结论与建议 > 下步建议 > ### 岩土分层及其特征

- Source locator: L12786
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### 岩土分层及其特征` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-5145 ### 岩土分层及其特征
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-5145 | ORIGINAL_TEXT | ### 岩土分层及其特征 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12788 |

### SEC-500 结论与建议 > 下步建议 > #### 第四系残坡积层\(Qedl\)

- Source locator: L12790
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### 第四系残坡积层\(Qedl\)` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-5146 #### 第四系残坡积层\(Qedl\)
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-5146 | ORIGINAL_TEXT | #### 第四系残坡积层\(Qedl\) | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12792 |

### SEC-501 结论与建议 > 下步建议 > #### 石炭系下统刘家塘组（C1*lj*）基岩

- Source locator: L12794
- Material density: 97段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### 石炭系下统刘家塘组（C1*lj*）基岩` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-5147 #### 石炭系下统刘家塘组（C1*lj*）基岩；UNIT-5148 #### 石炭系下统刘家塘组（C1*lj*）基岩；UNIT-5149 #### 石炭系下统刘家塘组（C1*lj*）基岩；UNIT-5150 #### 石炭系下统刘家塘组（C1*lj*）基岩；UNIT-5151 #### 石炭系下统刘家塘组（C1*lj*）基岩
  - Best source pairing: left_text_right_table or top_text_bottom_table；left_text_right_figure or text_with_keypoints
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-5147 | CALCULATION | #### 石炭系下统刘家塘组（C1*lj*）基岩 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L12796 |
| UNIT-5148 | ORIGINAL_TEXT | #### 石炭系下统刘家塘组（C1*lj*）基岩 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12852 |
| UNIT-5149 | ORIGINAL_TEXT | #### 石炭系下统刘家塘组（C1*lj*）基岩 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12858 |
| UNIT-5150 | ORIGINAL_TEXT | #### 石炭系下统刘家塘组（C1*lj*）基岩 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12860 |
| UNIT-5151 | ORIGINAL_TEXT | #### 石炭系下统刘家塘组（C1*lj*）基岩 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12862 |
| UNIT-5152 | ORIGINAL_TEXT | #### 石炭系下统刘家塘组（C1*lj*）基岩 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12864 |
| UNIT-5153 | ORIGINAL_TEXT | #### 石炭系下统刘家塘组（C1*lj*）基岩 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12866 |
| UNIT-5154 | ORIGINAL_TEXT | #### 石炭系下统刘家塘组（C1*lj*）基岩 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12868 |
| UNIT-5155 | ORIGINAL_TEXT | #### 石炭系下统刘家塘组（C1*lj*）基岩 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12870 |
| UNIT-5156 | ORIGINAL_TEXT | #### 石炭系下统刘家塘组（C1*lj*）基岩 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12872 |
| UNIT-5157 | ORIGINAL_TEXT | #### 石炭系下统刘家塘组（C1*lj*）基岩 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12874 |
| UNIT-5158 | ORIGINAL_TEXT | #### 石炭系下统刘家塘组（C1*lj*）基岩 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L12876 |
| ... | ... | Additional 85 units in JSON inventory | ... | ... | ... |

### SEC-502 结论与建议 > 下步建议 > ### 露采边坡稳定性分析

- Source locator: L13076
- Material density: 22段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### 露采边坡稳定性分析` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-5244 ### 露采边坡稳定性分析；UNIT-5245 ### 露采边坡稳定性分析；UNIT-5246 ### 露采边坡稳定性分析；UNIT-5247 ### 露采边坡稳定性分析；UNIT-5248 ### 露采边坡稳定性分析
  - Best source pairing: left_text_right_figure or text_with_keypoints；left_text_right_table or top_text_bottom_table
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-5244 | ORIGINAL_TEXT | ### 露采边坡稳定性分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13078 |
| UNIT-5245 | ORIGINAL_TEXT | ### 露采边坡稳定性分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13080 |
| UNIT-5246 | ORIGINAL_TEXT | ### 露采边坡稳定性分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13082 |
| UNIT-5247 | ORIGINAL_TEXT | ### 露采边坡稳定性分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13084 |
| UNIT-5248 | ORIGINAL_TEXT | ### 露采边坡稳定性分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13094 |
| UNIT-5249 | CALCULATION | ### 露采边坡稳定性分析 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L13096 |
| UNIT-5250 | ORIGINAL_TEXT | ### 露采边坡稳定性分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13126 |
| UNIT-5251 | ORIGINAL_TEXT | ### 露采边坡稳定性分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13128 |
| UNIT-5252 | ORIGINAL_TEXT | ### 露采边坡稳定性分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13130 |
| UNIT-5253 | ORIGINAL_TEXT | ### 露采边坡稳定性分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13132 |
| UNIT-5254 | ORIGINAL_TEXT | ### 露采边坡稳定性分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13142 |
| UNIT-5255 | ORIGINAL_TEXT | ### 露采边坡稳定性分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13144 |
| ... | ... | Additional 10 units in JSON inventory | ... | ... | ... |

### SEC-503 结论与建议 > 下步建议 > #### A\-A’剖面

- Source locator: L13194
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### A\-A’剖面` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-5266 #### A\-A’剖面
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-5266 | ORIGINAL_TEXT | #### A\-A’剖面 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13196 |

### SEC-504 结论与建议 > 下步建议 > #### B\-B’剖面

- Source locator: L13206
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### B\-B’剖面` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-5267 #### B\-B’剖面
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-5267 | ORIGINAL_TEXT | #### B\-B’剖面 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13208 |

### SEC-505 结论与建议 > 下步建议 > #### C\-C’剖面

- Source locator: L13218
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### C\-C’剖面` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-5268 #### C\-C’剖面
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-5268 | ORIGINAL_TEXT | #### C\-C’剖面 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13220 |

### SEC-506 结论与建议 > 下步建议 > #### D\-D’剖面

- Source locator: L13230
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### D\-D’剖面` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-5269 #### D\-D’剖面
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-5269 | ORIGINAL_TEXT | #### D\-D’剖面 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13232 |

### SEC-507 结论与建议 > 下步建议 > ### 工程地质问题预测与分析

- Source locator: L13242
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### 工程地质问题预测与分析` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-5270 ### 工程地质问题预测与分析
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-5270 | ORIGINAL_TEXT | ### 工程地质问题预测与分析 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13244 |

### SEC-508 结论与建议 > 下步建议 > #### 岩溶地面塌陷

- Source locator: L13246
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### 岩溶地面塌陷` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-5271 #### 岩溶地面塌陷；UNIT-5272 #### 岩溶地面塌陷
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-5271 | ORIGINAL_TEXT | #### 岩溶地面塌陷 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13248 |
| UNIT-5272 | ORIGINAL_TEXT | #### 岩溶地面塌陷 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13252 |

### SEC-509 结论与建议 > 下步建议 > #### 地表变形

- Source locator: L13254
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### 地表变形` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-5273 #### 地表变形；UNIT-5274 #### 地表变形
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-5273 | ORIGINAL_TEXT | #### 地表变形 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13256 |
| UNIT-5274 | ORIGINAL_TEXT | #### 地表变形 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13260 |

### SEC-510 结论与建议 > 下步建议 > #### 矿坑突水（突泥）

- Source locator: L13262
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### 矿坑突水（突泥）` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-5275 #### 矿坑突水（突泥）；UNIT-5276 #### 矿坑突水（突泥）
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-5275 | ORIGINAL_TEXT | #### 矿坑突水（突泥） | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13264 |
| UNIT-5276 | ORIGINAL_TEXT | #### 矿坑突水（突泥） | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13268 |

### SEC-511 结论与建议 > 下步建议 > #### 采场边坡崩塌/滑坡

- Source locator: L13270
- Material density: 9段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### 采场边坡崩塌/滑坡` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-5277 #### 采场边坡崩塌/滑坡；UNIT-5278 #### 采场边坡崩塌/滑坡；UNIT-5279 #### 采场边坡崩塌/滑坡；UNIT-5280 #### 采场边坡崩塌/滑坡；UNIT-5281 #### 采场边坡崩塌/滑坡
  - Best source pairing: left_text_right_table or top_text_bottom_table；left_text_right_figure or text_with_keypoints
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-5277 | CALCULATION | #### 采场边坡崩塌/滑坡 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L13274 |
| UNIT-5278 | ORIGINAL_TEXT | #### 采场边坡崩塌/滑坡 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13276 |
| UNIT-5279 | ORIGINAL_TEXT | #### 采场边坡崩塌/滑坡 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13278 |
| UNIT-5280 | ORIGINAL_TEXT | #### 采场边坡崩塌/滑坡 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13280 |
| UNIT-5281 | ORIGINAL_TEXT | #### 采场边坡崩塌/滑坡 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13282 |
| UNIT-5282 | ORIGINAL_TEXT | #### 采场边坡崩塌/滑坡 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13284 |
| UNIT-5283 | ORIGINAL_TEXT | #### 采场边坡崩塌/滑坡 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13286 |
| UNIT-5284 | CALCULATION | #### 采场边坡崩塌/滑坡 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L13288 |
| UNIT-5285 | ORIGINAL_TEXT | #### 采场边坡崩塌/滑坡 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13290 |

### SEC-512 结论与建议 > 下步建议 > ### 矿区工程地质勘查类型

- Source locator: L13292
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### 矿区工程地质勘查类型` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-5286 ### 矿区工程地质勘查类型
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-5286 | ORIGINAL_TEXT | ### 矿区工程地质勘查类型 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13294 |

### SEC-514 结论与建议 > 下步建议 > ### 勘察区地质环境评价

- Source locator: L13298
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### 勘察区地质环境评价` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-5287 ### 勘察区地质环境评价
  - Best source pairing: left_text_right_table or top_text_bottom_table
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-5287 | CALCULATION | ### 勘察区地质环境评价 | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L13300 |

### SEC-515 结论与建议 > 下步建议 > ### 环境水文地质问题

- Source locator: L13302
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### 环境水文地质问题` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-5288 ### 环境水文地质问题；UNIT-5289 ### 环境水文地质问题
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-5288 | ORIGINAL_TEXT | ### 环境水文地质问题 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13304 |
| UNIT-5289 | ORIGINAL_TEXT | ### 环境水文地质问题 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13308 |

### SEC-516 结论与建议 > 下步建议 > ### 地下水开发利用现状

- Source locator: L13320
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### 地下水开发利用现状` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-5290 ### 地下水开发利用现状
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-5290 | ORIGINAL_TEXT | ### 地下水开发利用现状 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13322 |

### SEC-519 结论与建议 > 下步建议 > #### 矿山建设和开采引发地面地质灾害的预测评价

- Source locator: L13332
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### 矿山建设和开采引发地面地质灾害的预测评价` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-5291 #### 矿山建设和开采引发地面地质灾害的预测评价
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-5291 | ORIGINAL_TEXT | #### 矿山建设和开采引发地面地质灾害的预测评价 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13334 |

### SEC-521 结论与建议 > 下步建议 > #### 矿山开采对水源的影响

- Source locator: L13340
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### 矿山开采对水源的影响` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-5292 #### 矿山开采对水源的影响
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-5292 | ORIGINAL_TEXT | #### 矿山开采对水源的影响 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13342 |

### SEC-522 结论与建议 > 下步建议 > ### 矿区地质环境类型

- Source locator: L13344
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### 矿区地质环境类型` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-5293 ### 矿区地质环境类型
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-5293 | ORIGINAL_TEXT | ### 矿区地质环境类型 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13346 |

### SEC-524 结论与建议 > 下步建议 > ## <a id="_Toc19499"></a><a id="_Toc7652"></a><a id="_Toc6468"></a><a id="_Toc16808"></a><a id="_Toc23899"></a><a id="_Toc8256"></a><a id="_Toc27567"></a><a id="_Toc20631"></a><a id="_Toc18716"></a><a id="_Toc9034"></a>矿山防治水原则

- Source locator: L13350
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `## <a id="_Toc19499"></a><a id="_Toc7652"></a><a id="_Toc6468"></a><a id="_Toc16808"></a><a id="_Toc23899"></a><a id="_Toc8256"></a><a id="_Toc27567"></a><a id="_Toc20631"></a><a id="_Toc18716"></a><a id="_Toc9034"></a>矿山防治水原则` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-5294 ## <a id="_Toc19499"></a><a id="_Toc7652"…
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-5294 | ORIGINAL_TEXT | ## <a id="_Toc19499"></a><a id="_Toc7652"… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13352 |

### SEC-525 结论与建议 > 下步建议 > ### 以查明矿坑充水条件为基础，加强采掘过程中水文地质条件研究

- Source locator: L13354
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### 以查明矿坑充水条件为基础，加强采掘过程中水文地质条件研究` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-5295 ### 以查明矿坑充水条件为基础，加强采掘过程中水文地质条件研究
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-5295 | ORIGINAL_TEXT | ### 以查明矿坑充水条件为基础，加强采掘过程中水文地质条件研究 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13356 |

### SEC-526 结论与建议 > 下步建议 > ### 遵循先简单、后复杂，层层设防的原则

- Source locator: L13358
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### 遵循先简单、后复杂，层层设防的原则` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-5296 ### 遵循先简单、后复杂，层层设防的原则
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-5296 | ORIGINAL_TEXT | ### 遵循先简单、后复杂，层层设防的原则 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13360 |

### SEC-527 结论与建议 > 下步建议 > ### 精心组织合理规划，最大限度节约投资的原则

- Source locator: L13362
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### 精心组织合理规划，最大限度节约投资的原则` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-5297 ### 精心组织合理规划，最大限度节约投资的原则
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-5297 | ORIGINAL_TEXT | ### 精心组织合理规划，最大限度节约投资的原则 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13366 |

### SEC-528 结论与建议 > 下步建议 > ## <a id="_Toc24228"></a><a id="_Toc15562"></a><a id="_Toc16479"></a><a id="_Toc32158"></a><a id="_Toc14267"></a><a id="_Toc24123"></a><a id="_Toc31344"></a><a id="_Toc12980"></a><a id="_Toc22946"></a><a id="_Toc27290"></a>矿山防治水措施

- Source locator: L13368
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `## <a id="_Toc24228"></a><a id="_Toc15562"></a><a id="_Toc16479"></a><a id="_Toc32158"></a><a id="_Toc14267"></a><a id="_Toc24123"></a><a id="_Toc31344"></a><a id="_Toc12980"></a><a id="_Toc22946"></a><a id="_Toc27290"></a>矿山防治水措施` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-5298 ## <a id="_Toc24228"></a><a id="_Toc15562…
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-5298 | ORIGINAL_TEXT | ## <a id="_Toc24228"></a><a id="_Toc15562… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13370 |

### SEC-529 结论与建议 > 下步建议 > ### 地表堵水措施

- Source locator: L13372
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### 地表堵水措施` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-5299 ### 地表堵水措施
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-5299 | ORIGINAL_TEXT | ### 地表堵水措施 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13374 |

### SEC-530 结论与建议 > 下步建议 > ### 帷幕截水措施

- Source locator: L13376
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### 帷幕截水措施` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-5300 ### 帷幕截水措施
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-5300 | ORIGINAL_TEXT | ### 帷幕截水措施 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13378 |

### SEC-531 结论与建议 > 下步建议 > ### 采坑截渗系统

- Source locator: L13380
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### 采坑截渗系统` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-5301 ### 采坑截渗系统
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-5301 | ORIGINAL_TEXT | ### 采坑截渗系统 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13382 |

### SEC-533 结论与建议 > 下步建议 > ### 超前探水工程

- Source locator: L13388
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### 超前探水工程` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-5302 ### 超前探水工程
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-5302 | ORIGINAL_TEXT | ### 超前探水工程 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13390 |

### SEC-534 结论与建议 > 下步建议 > ### 地下水长期监测工程

- Source locator: L13392
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### 地下水长期监测工程` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-5303 ### 地下水长期监测工程
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-5303 | ORIGINAL_TEXT | ### 地下水长期监测工程 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13394 |

### SEC-537 结论与建议 > 下步建议 > ### 生态用水

- Source locator: L13400
- Material density: 37段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### 生态用水` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-5304 ### 生态用水；UNIT-5305 ### 生态用水；UNIT-5306 ### 生态用水；UNIT-5307 ### 生态用水；UNIT-5308 ### 生态用水
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-5304 | ORIGINAL_TEXT | ### 生态用水 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13402 |
| UNIT-5305 | ORIGINAL_TEXT | ### 生态用水 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13422 |
| UNIT-5306 | ORIGINAL_TEXT | ### 生态用水 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13424 |
| UNIT-5307 | ORIGINAL_TEXT | ### 生态用水 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13426 |
| UNIT-5308 | ORIGINAL_TEXT | ### 生态用水 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13428 |
| UNIT-5309 | ORIGINAL_TEXT | ### 生态用水 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13430 |
| UNIT-5310 | ORIGINAL_TEXT | ### 生态用水 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13432 |
| UNIT-5311 | ORIGINAL_TEXT | ### 生态用水 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13436 |
| UNIT-5312 | ORIGINAL_TEXT | ### 生态用水 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13438 |
| UNIT-5313 | ORIGINAL_TEXT | ### 生态用水 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13440 |
| UNIT-5314 | ORIGINAL_TEXT | ### 生态用水 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13442 |
| UNIT-5315 | ORIGINAL_TEXT | ### 生态用水 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13444 |
| ... | ... | Additional 25 units in JSON inventory | ... | ... | ... |

### SEC-539 结论与建议 > 下步建议 > #### 水质评价

- Source locator: L13534
- Material density: 13段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### 水质评价` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-5341 #### 水质评价；UNIT-5342 #### 水质评价；UNIT-5343 #### 水质评价；UNIT-5344 #### 水质评价；UNIT-5345 #### 水质评价
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: material is dense; split into source context, original object pages, and chapter conclusion.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-5341 | ORIGINAL_TEXT | #### 水质评价 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13536 |
| UNIT-5342 | ORIGINAL_TEXT | #### 水质评价 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13556 |
| UNIT-5343 | ORIGINAL_TEXT | #### 水质评价 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13558 |
| UNIT-5344 | ORIGINAL_TEXT | #### 水质评价 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13560 |
| UNIT-5345 | ORIGINAL_TEXT | #### 水质评价 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13562 |
| UNIT-5346 | ORIGINAL_TEXT | #### 水质评价 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13566 |
| UNIT-5347 | ORIGINAL_TEXT | #### 水质评价 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13568 |
| UNIT-5348 | ORIGINAL_TEXT | #### 水质评价 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13570 |
| UNIT-5349 | ORIGINAL_TEXT | #### 水质评价 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13572 |
| UNIT-5350 | ORIGINAL_TEXT | #### 水质评价 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13576 |
| UNIT-5351 | ORIGINAL_TEXT | #### 水质评价 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13578 |
| UNIT-5352 | ORIGINAL_TEXT | #### 水质评价 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13580 |
| ... | ... | Additional 1 units in JSON inventory | ... | ... | ... |

### SEC-540 结论与建议 > 下步建议 > #### 排放途径与污染防控

- Source locator: L13586
- Material density: 6段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### 排放途径与污染防控` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-5354 #### 排放途径与污染防控；UNIT-5355 #### 排放途径与污染防控；UNIT-5356 #### 排放途径与污染防控；UNIT-5357 #### 排放途径与污染防控；UNIT-5358 #### 排放途径与污染防控
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-5354 | ORIGINAL_TEXT | #### 排放途径与污染防控 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13588 |
| UNIT-5355 | ORIGINAL_TEXT | #### 排放途径与污染防控 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13590 |
| UNIT-5356 | ORIGINAL_TEXT | #### 排放途径与污染防控 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13592 |
| UNIT-5357 | ORIGINAL_TEXT | #### 排放途径与污染防控 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13594 |
| UNIT-5358 | ORIGINAL_TEXT | #### 排放途径与污染防控 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13596 |
| UNIT-5359 | ORIGINAL_TEXT | #### 排放途径与污染防控 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13598 |

### SEC-542 结论与建议 > 下步建议 > ### 生产供水

- Source locator: L13604
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### 生产供水` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-5360 ### 生产供水
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-5360 | ORIGINAL_TEXT | ### 生产供水 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13606 |

### SEC-543 结论与建议 > 下步建议 > ### 生活供水

- Source locator: L13608
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### 生活供水` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-5361 ### 生活供水
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-5361 | ORIGINAL_TEXT | ### 生活供水 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13610 |

### SEC-545 结论与建议 > 下步建议 > #### 备选方案

- Source locator: L13616
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `#### 备选方案` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-5362 #### 备选方案
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-5362 | ORIGINAL_TEXT | #### 备选方案 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13618 |

### SEC-546 结论与建议 > 下步建议 > # <a id="_Toc6639"></a><a id="_Toc31266"></a><a id="_Toc18699"></a><a id="_Toc17332"></a>结论与建议

- Source locator: L13620
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `# <a id="_Toc6639"></a><a id="_Toc31266"></a><a id="_Toc18699"></a><a id="_Toc17332"></a>结论与建议` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-5363 # <a id="_Toc6639"></a><a id="_Toc31266">…
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-5363 | ORIGINAL_TEXT | # <a id="_Toc6639"></a><a id="_Toc31266">… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13622 |

### SEC-548 结论与建议 > 下步建议 > ### 水文地质勘查类型

- Source locator: L13626
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### 水文地质勘查类型` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-5364 ### 水文地质勘查类型；UNIT-5365 ### 水文地质勘查类型
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-5364 | ORIGINAL_TEXT | ### 水文地质勘查类型 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13628 |
| UNIT-5365 | ORIGINAL_TEXT | ### 水文地质勘查类型 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13630 |

### SEC-549 结论与建议 > 下步建议 > ### 工程地质勘查类型

- Source locator: L13634
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### 工程地质勘查类型` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-5366 ### 工程地质勘查类型
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-5366 | ORIGINAL_TEXT | ### 工程地质勘查类型 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13636 |

### SEC-550 结论与建议 > 下步建议 > ### 地质环境类型

- Source locator: L13638
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### 地质环境类型` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-5367 ### 地质环境类型
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-5367 | ORIGINAL_TEXT | ### 地质环境类型 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13640 |

### SEC-552 结论与建议 > 下步建议 > ### 查明了矿区岩溶水文地质条件

- Source locator: L13644
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### 查明了矿区岩溶水文地质条件` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-5368 ### 查明了矿区岩溶水文地质条件；UNIT-5369 ### 查明了矿区岩溶水文地质条件
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-5368 | ORIGINAL_TEXT | ### 查明了矿区岩溶水文地质条件 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13646 |
| UNIT-5369 | ORIGINAL_TEXT | ### 查明了矿区岩溶水文地质条件 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13648 |

### SEC-553 结论与建议 > 下步建议 > ### 揭示了矿区地层岩溶发育特征

- Source locator: L13650
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### 揭示了矿区地层岩溶发育特征` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-5370 ### 揭示了矿区地层岩溶发育特征
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-5370 | ORIGINAL_TEXT | ### 揭示了矿区地层岩溶发育特征 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13652 |

### SEC-554 结论与建议 > 下步建议 > ### 圈定了矿区边界处岩溶水强径流带

- Source locator: L13654
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### 圈定了矿区边界处岩溶水强径流带` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-5371 ### 圈定了矿区边界处岩溶水强径流带
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-5371 | ORIGINAL_TEXT | ### 圈定了矿区边界处岩溶水强径流带 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13656 |

### SEC-555 结论与建议 > 下步建议 > ### 预测了矿区不同开采水平的涌水量

- Source locator: L13658
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### 预测了矿区不同开采水平的涌水量` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-5372 ### 预测了矿区不同开采水平的涌水量
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-5372 | ORIGINAL_TEXT | ### 预测了矿区不同开采水平的涌水量 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13660 |

### SEC-556 结论与建议 > 下步建议 > ### 提出了矿区凹陷开采阶段防治水措施

- Source locator: L13662
- Material density: 1段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### 提出了矿区凹陷开采阶段防治水措施` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-5373 ### 提出了矿区凹陷开采阶段防治水措施
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-5373 | ORIGINAL_TEXT | ### 提出了矿区凹陷开采阶段防治水措施 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13664 |

### SEC-558 结论与建议 > 下步建议 > ### 勘察工作中存在的主要问题

- Source locator: L13668
- Material density: 4段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### 勘察工作中存在的主要问题` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-5374 ### 勘察工作中存在的主要问题；UNIT-5375 ### 勘察工作中存在的主要问题；UNIT-5376 ### 勘察工作中存在的主要问题；UNIT-5377 ### 勘察工作中存在的主要问题
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-5374 | ORIGINAL_TEXT | ### 勘察工作中存在的主要问题 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13670 |
| UNIT-5375 | ORIGINAL_TEXT | ### 勘察工作中存在的主要问题 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13672 |
| UNIT-5376 | ORIGINAL_TEXT | ### 勘察工作中存在的主要问题 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13674 |
| UNIT-5377 | ORIGINAL_TEXT | ### 勘察工作中存在的主要问题 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13676 |

### SEC-559 结论与建议 > 下步建议 > ### 开采过程中可能出现的问题

- Source locator: L13678
- Material density: 4段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `### 开采过程中可能出现的问题` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-5378 ### 开采过程中可能出现的问题；UNIT-5379 ### 开采过程中可能出现的问题；UNIT-5380 ### 开采过程中可能出现的问题；UNIT-5381 ### 开采过程中可能出现的问题
  - Best source pairing: left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-5378 | ORIGINAL_TEXT | ### 开采过程中可能出现的问题 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13680 |
| UNIT-5379 | ORIGINAL_TEXT | ### 开采过程中可能出现的问题 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13682 |
| UNIT-5380 | ORIGINAL_TEXT | ### 开采过程中可能出现的问题 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13684 |
| UNIT-5381 | ORIGINAL_TEXT | ### 开采过程中可能出现的问题 | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13686 |

### SEC-560 结论与建议 > 下步建议 > ## <a id="_Toc615"></a><a id="_Toc2917"></a><a id="_Toc31234"></a><a id="_Toc32384"></a><a id="_Toc17723"></a><a id="_Toc22067"></a><a id="_Toc8825"></a><a id="_Toc9048"></a><a id="_Toc19751"></a><a id="_Toc4274"></a><a id="_Toc13382"></a>下步建议

- Source locator: L13688
- Material density: 2段关键文字
- Agent synthesis draft before slide planning:
  - Audience-facing point: explain `## <a id="_Toc615"></a><a id="_Toc2917"></a><a id="_Toc31234"></a><a id="_Toc32384"></a><a id="_Toc17723"></a><a id="_Toc22067"></a><a id="_Toc8825"></a><a id="_Toc9048"></a><a id="_Toc19751"></a><a id="_Toc4274"></a><a id="_Toc13382"></a>下步建议` through source evidence, not a generic summary.
  - Must-keep original wording/data: UNIT-5382 ## <a id="_Toc615"></a><a id="_Toc2917"><…；UNIT-5383 ## <a id="_Toc615"></a><a id="_Toc2917"><…
  - Best source pairing: left_text_right_table or top_text_bottom_table；left_text_right_figure or text_with_keypoints
  - Slide split decision: one source-text page may be sufficient if evidence remains readable.

| Unit | Source Mode | Candidate Title | Role | Layout Hint | Catalog IDs |
| --- | --- | --- | --- | --- | --- |
| UNIT-5382 | CALCULATION | ## <a id="_Toc615"></a><a id="_Toc2917"><… | calculation logic or parameter explanation | left_text_right_table or top_text_bottom_table | 4e2d4c72:L13690 |
| UNIT-5383 | ORIGINAL_TEXT | ## <a id="_Toc615"></a><a id="_Toc2917"><… | source text / section context / faithful explanation | left_text_right_figure or text_with_keypoints | 4e2d4c72:L13692 |

## Deck Planning Gate

Before authoring slides, update or review `deck_plan.json` so every substantive page is derived
from selected content units, with report-native headings/captions used for visible small titles.
