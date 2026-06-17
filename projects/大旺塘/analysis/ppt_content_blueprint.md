# PPT Content Blueprint

This blueprint is the mandatory thinking workspace between report extraction and slide planning.
The agent must read it, refine the narrative, and then derive `evidence_ledger.json`,
`chapter_coverage.md`, and `deck_plan.json` from the selected content units.

## Inventory Summary

- Sections: 281
- Important paragraphs: 569
- Tables: 63
- Figures: 221
- PPT content units: 853

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
- Material density: 2段关键文字、221张图
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
| ... | ... | Additional 211 units in JSON inventory | ... | ... | ... |

## Deck Planning Gate

Before authoring slides, update or review `deck_plan.json` so every substantive page is derived
from selected content units, with report-native headings/captions used for visible small titles.
