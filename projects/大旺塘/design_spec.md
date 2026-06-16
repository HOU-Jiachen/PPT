# 大旺塘 - Design Spec

## I. Project Information

| Item | Value |
| ---- | ----- |
| **Project Name** | 大旺塘矿山地下水治理专项水文地质勘察工程评审汇报 |
| **Canvas Format** | PPT 16:9 (1280x720) |
| **Page Count** | 74 |
| **Design Style** | General Consulting + 政府/工程咨询评审详版 |
| **Target Audience** | 业主单位、矿山安全与水文地质评审专家、设计及治理实施相关方 |
| **Use Case** | 专项勘察工程评审汇报 |
| **Created Date** | 2026-06-16 |

## II. Canvas Specification

| Property | Value |
| -------- | ----- |
| **Format** | PPT 16:9 |
| **Dimensions** | 1280x720 |
| **viewBox** | `0 0 1280 720` |
| **Margins** | left/right 40-60px, top 30px, footer 24px |
| **Content Area** | 1200x600px |

## III. Visual Theme

- **Style**: General Consulting + restrained government engineering review
- **Theme**: Light theme
- **Tone**: evidence-first, source-faithful, technical, restrained

| Role | HEX | Purpose |
| ---- | --- | ------- |
| **Background** | `#F7F9F9` | Page background |
| **Secondary bg** | `#EEF3F3` | Technical bands and table surfaces |
| **Primary** | `#0E5E6F` | Chapter headers and emphasis |
| **Accent** | `#B65A24` | Key engineering warnings and control values |
| **Body text** | `#1B2A2F` | Main body text |
| **Secondary text** | `#5E6B70` | Captions, source notes |
| **Border/divider** | `#C7D3D4` | Table and figure frames |

## IV. Typography System

**Typography direction**: CJK-primary professional sans with serif emphasis for report quotations.

| Role | Chinese | English | Fallback tail |
| ---- | ------- | ------- | ------------- |
| **Title** | `"Microsoft YaHei"` | `Arial` | `sans-serif` |
| **Body** | `"Microsoft YaHei"` | `Arial` | `sans-serif` |
| **Emphasis** | `SimSun` | `Georgia` | `serif` |
| **Code** | — | `Consolas, "Courier New"` | `monospace` |

- Title: `"Microsoft YaHei", Arial, sans-serif`
- Body: `"Microsoft YaHei", Arial, sans-serif`
- Emphasis: `Georgia, SimSun, serif`
- Code: `Consolas, "Courier New", monospace`

**Baseline**: Body font size = 18px.

## V. Layout Principles

- Header area: 90px, title + chapter + page number.
- Content area: 560px, prioritizing original figure/table readability.
- Footer area: 30px, concise source note.
- Layouts: left_text_right_figure, top_figure_bottom_text, left_table_right_text, top_text_bottom_table, evidence_chain, decision_matrix.
- Dense technical pages avoid decorative cards; tables and figures use framed source panels.

## VI. Icon Usage Specification

- Built-in icon library: `tabler-outline`
- Usage is sparse; icons only support agenda, chain and decision pages.

| Purpose | Icon Path | Page |
| ------- | --------- | ---- |
| Objective | `tabler-outline/target` | P02 |
| Evidence | `tabler-outline/chart-bar` | P12 |
| Safety | `tabler-outline/shield` | P72 |

## VII. Visualization Reference List

Catalog read: no chart templates used. The deck uses report-native tables, maps, figures and formulas because source fidelity is more important than restyling source data.

Runners-up considered:
- `bar_chart` | rejected: most numeric pages require precise source tables rather than simplified bars.
- `process_flow` | rejected:防治水措施使用报告原文和证据链矩阵，不替代为流程模板。
- `timeline_horizontal` | rejected:工作经过页保留报告原文时间节点即可。

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Layout pattern | Acquire Via | Status | Reference | text_policy | page_role |
| -------- | ---------- | ----- | ------- | ---- | -------------- | ----------- | ------ | --------- | ----------- | --------- |
| image_003.jpeg | 1255x1038 | 1.21 | Key report source figure | Source figure | source-faithful figure panel | user | Existing | Extracted from DOCX | none | local |
| image_034.png | 881x802 | 1.10 | Key report source figure | Source figure | source-faithful figure panel | user | Existing | Extracted from DOCX | none | local |
| image_060.png | 1002x1060 | 0.95 | Key report source figure | Source figure | source-faithful figure panel | user | Existing | Extracted from DOCX | none | local |
| image_143.jpeg | 1268x1141 | 1.11 | Key report source figure | Source figure | source-faithful figure panel | user | Existing | Extracted from DOCX | none | local |
| image_194.jpeg | 1213x970 | 1.25 | Key report source figure | Source figure | source-faithful figure panel | user | Existing | Extracted from DOCX | none | local |
| image_195.jpeg | 1213x970 | 1.25 | Key report source figure | Source figure | source-faithful figure panel | user | Existing | Extracted from DOCX | none | local |
| image_207.png | 488x464 | 1.05 | Key report source figure | Source figure | source-faithful figure panel | user | Existing | Extracted from DOCX | none | local |
| image_216.png | 709x608 | 1.17 | Key report source figure | Source figure | source-faithful figure panel | user | Existing | Extracted from DOCX | none | local |

## IX. Content Outline

### 项目背景、采矿权与评审目标 (6 pages)
#### Slide 01 - 大旺塘矿山地下水治理专项水文地质勘察工程评审汇报
- **Layout**: cover_with_source_context
- **Core message**: 大旺塘矿山地下水治理专项水文地质勘察工程评审汇报
- **Source mode**: ORIGINAL_TEXT
- **Evidence**: E-0-PROJECT
- **Source note**: 报告封面
#### Slide 02 - 评审重点从治理对象、证据充分性、控制工况和措施边界展开
- **Layout**: structured_agenda
- **Core message**: 评审重点从治理对象、证据充分性、控制工况和措施边界展开
- **Source mode**: INTERPRETATION
- **Evidence**: E-1-OBJECTIVE, E-6-WATER-INFLOW-COMPARE, E-9-WATER-CONTROL
- **Source note**: 目的任务、表6.2-10、第九章
#### Slide 03 - 专项勘察聚焦+50m至+5m凹陷开采阶段地下水治理
- **Layout**: left_text_right_keypoints
- **Core message**: 专项勘察聚焦+50m至+5m凹陷开采阶段地下水治理
- **Source mode**: ORIGINAL_TEXT
- **Evidence**: E-1-OBJECTIVE
- **Source note**: P0039-P0047
#### Slide 04 - 采矿权范围与开采标高变化决定治理边界
- **Layout**: left_table_right_text
- **Core message**: 采矿权范围与开采标高变化决定治理边界
- **Source mode**: ORIGINAL_TABLE
- **Evidence**: E-1-MINING-RIGHT
- **Source note**: 表1.2-1至表1.2-3
#### Slide 05 - 分割保留区叠合图显示现拟设采矿权边界
- **Layout**: top_figure_bottom_text
- **Core message**: 分割保留区叠合图显示现拟设采矿权边界
- **Source mode**: ORIGINAL_FIGURE
- **Evidence**: E-1-MINING-RIGHT
- **Source note**: 图1.2-2
#### Slide 06 - 现状采场与开发规划形成由+50m向+5m推进的治理场景
- **Layout**: left_figure_right_text
- **Core message**: 现状采场与开发规划形成由+50m向+5m推进的治理场景
- **Source mode**: ORIGINAL_FIGURE
- **Evidence**: E-1-MINING-RIGHT
- **Source note**: 图1.2-3、矿山开发规划

### 以往工作、本次工作量与成果基础 (6 pages)
#### Slide 07 - 以往地质、水文地质和资源核实工作构成本次勘察基础
- **Layout**: timeline_with_source_text
- **Core message**: 以往地质、水文地质和资源核实工作构成本次勘察基础
- **Source mode**: ORIGINAL_TEXT
- **Evidence**: E-1-WORKLOAD
- **Source note**: 以往工作评述
#### Slide 08 - 2026年2月9日至3月31日完成51天综合勘察
- **Layout**: left_text_right_sequence
- **Core message**: 2026年2月9日至3月31日完成51天综合勘察
- **Source mode**: ORIGINAL_TEXT
- **Evidence**: E-1-WORKLOAD
- **Source note**: P0136-P0139
#### Slide 09 - 本次工作量覆盖调查、物探、钻探、试验、监测和模拟
- **Layout**: top_text_bottom_table
- **Core message**: 本次工作量覆盖调查、物探、钻探、试验、监测和模拟
- **Source mode**: ORIGINAL_TABLE
- **Evidence**: E-1-WORKLOAD
- **Source note**: 表1.4-1
#### Slide 10 - 成果资料包括报告、附图、附表和附件四类
- **Layout**: left_table_right_text
- **Core message**: 成果资料包括报告、附图、附表和附件四类
- **Source mode**: ORIGINAL_TABLE
- **Evidence**: E-1-WORKLOAD
- **Source note**: 表1.4-2
#### Slide 11 - 现场调查控制50km2并覆盖关键岩溶和水文点
- **Layout**: left_table_right_figure
- **Core message**: 现场调查控制50km2并覆盖关键岩溶和水文点
- **Source mode**: ORIGINAL_TABLE
- **Evidence**: E-3-SURVEY
- **Source note**: 表3.1-1、图3.1-1至图3.1-10
#### Slide 12 - 证据链从地面调查延伸到预测模型和防治水建议
- **Layout**: evidence_chain
- **Core message**: 证据链从地面调查延伸到预测模型和防治水建议
- **Source mode**: INTERPRETATION
- **Evidence**: E-1-WORKLOAD, E-3-GEOPHYSICS-RESULT, E-6-WATER-INFLOW-COMPARE, E-9-WATER-CONTROL
- **Source note**: 表1.4-1、表3.2-1、表6.2-10、第九章

### 区域与矿区水文地质背景 (6 pages)
#### Slide 13 - 地理位置和交通条件限定调查与治理组织边界
- **Layout**: left_figure_right_text
- **Core message**: 地理位置和交通条件限定调查与治理组织边界
- **Source mode**: ORIGINAL_FIGURE
- **Evidence**: E-2-REGIONAL
- **Source note**: 图2.1-1
#### Slide 14 - 地形地貌与降雨条件共同塑造汇水和补给格局
- **Layout**: top_figure_bottom_text
- **Core message**: 地形地貌与降雨条件共同塑造汇水和补给格局
- **Source mode**: ORIGINAL_FIGURE
- **Evidence**: E-2-REGIONAL, E-6-RAINFALL-RUNOFF
- **Source note**: 图2.2-1、图2.3-1
#### Slide 15 - 项目区水系和矿区周边水系支撑地表水关系判断
- **Layout**: top_figure_bottom_text
- **Core message**: 项目区水系和矿区周边水系支撑地表水关系判断
- **Source mode**: ORIGINAL_FIGURE
- **Evidence**: E-2-REGIONAL
- **Source note**: 图2.3-2、图2.3-3
#### Slide 16 - 区域地质图说明矿区所处构造和地层背景
- **Layout**: left_figure_right_text
- **Core message**: 区域地质图说明矿区所处构造和地层背景
- **Source mode**: ORIGINAL_FIGURE
- **Evidence**: E-2-REGIONAL
- **Source note**: 图2.4-1
#### Slide 17 - 区域水文地质单元决定地下水边界概化基础
- **Layout**: left_figure_right_text
- **Core message**: 区域水文地质单元决定地下水边界概化基础
- **Source mode**: ORIGINAL_FIGURE
- **Evidence**: E-2-REGIONAL
- **Source note**: 图2.5-1
#### Slide 18 - 地下水类型与补径排条件为岩溶直接充水判断铺垫
- **Layout**: left_text_right_table
- **Core message**: 地下水类型与补径排条件为岩溶直接充水判断铺垫
- **Source mode**: ORIGINAL_TEXT
- **Evidence**: E-2-REGIONAL
- **Source note**: 区域水文地质章节

### 水文地质勘探方法与物探成果 (12 pages)
#### Slide 19 - 物探采用高密度电法与微动组合识别岩溶和破碎带
- **Layout**: left_text_right_figure
- **Core message**: 物探采用高密度电法与微动组合识别岩溶和破碎带
- **Source mode**: ORIGINAL_TEXT
- **Evidence**: E-3-GEOPHYSICS-DEPLOY
- **Source note**: 图3.2-1至图3.2-4
#### Slide 20 - 15条高密度剖面和3条微动剖面覆盖关键地段
- **Layout**: top_figure_bottom_text
- **Core message**: 15条高密度剖面和3条微动剖面覆盖关键地段
- **Source mode**: ORIGINAL_FIGURE
- **Evidence**: E-3-GEOPHYSICS-DEPLOY
- **Source note**: 图3.2-5、P0160
#### Slide 21 - P1-P2剖面揭示构造破碎带和孤立低阻异常
- **Layout**: top_figure_bottom_text
- **Core message**: P1-P2剖面揭示构造破碎带和孤立低阻异常
- **Source mode**: ORIGINAL_FIGURE
- **Evidence**: E-3-GEOPHYSICS-RESULT
- **Source note**: 图3.2-11、图3.2-12
#### Slide 22 - P8-P10剖面集中显示采场内多处岩溶发育区
- **Layout**: top_figure_bottom_text
- **Core message**: P8-P10剖面集中显示采场内多处岩溶发育区
- **Source mode**: ORIGINAL_FIGURE
- **Evidence**: E-3-GEOPHYSICS-RESULT
- **Source note**: 图3.2-18、图3.2-19、图3.2-21
#### Slide 23 - P11-P15剖面补足中西部、南部和边界异常识别
- **Layout**: top_figure_bottom_text
- **Core message**: P11-P15剖面补足中西部、南部和边界异常识别
- **Source mode**: ORIGINAL_FIGURE
- **Evidence**: E-3-GEOPHYSICS-RESULT
- **Source note**: 图3.2-22至图3.2-26
#### Slide 24 - W10-W12微动剖面识别低速异常和深部结构
- **Layout**: top_figure_bottom_text
- **Core message**: W10-W12微动剖面识别低速异常和深部结构
- **Source mode**: ORIGINAL_FIGURE
- **Evidence**: E-3-GEOPHYSICS-RESULT
- **Source note**: 图3.2-27至图3.2-29
#### Slide 25 - 物探异常成果表需按断层和岩溶异常分组展示
- **Layout**: left_table_right_text
- **Core message**: 物探异常成果表需按断层和岩溶异常分组展示
- **Source mode**: ORIGINAL_TABLE
- **Evidence**: E-3-GEOPHYSICS-RESULT
- **Source note**: 表3.2-1
#### Slide 26 - 平面异常推断图汇总10处断层与81处岩溶发育区
- **Layout**: left_figure_right_text
- **Core message**: 平面异常推断图汇总10处断层与81处岩溶发育区
- **Source mode**: ORIGINAL_FIGURE
- **Evidence**: E-3-GEOPHYSICS-RESULT
- **Source note**: 图3.2-30、P0474
#### Slide 27 - 28组钻孔验证物探成果，整体准确率82.1%
- **Layout**: top_text_bottom_table
- **Core message**: 28组钻孔验证物探成果，整体准确率82.1%
- **Source mode**: ORIGINAL_TABLE
- **Evidence**: E-3-GEOPHYSICS-VALIDATION
- **Source note**: 表3.2-2、P0484
#### Slide 28 - 吻合与不吻合样本共同限定物探解释可靠边界
- **Layout**: left_table_right_text
- **Core message**: 吻合与不吻合样本共同限定物探解释可靠边界
- **Source mode**: ORIGINAL_TABLE
- **Evidence**: E-3-GEOPHYSICS-VALIDATION
- **Source note**: 表3.2-2
#### Slide 29 - 物探成果为后续钻探布置、岩溶评价和防治水靶区提供依据
- **Layout**: left_text_right_figure
- **Core message**: 物探成果为后续钻探布置、岩溶评价和防治水靶区提供依据
- **Source mode**: ORIGINAL_TEXT
- **Evidence**: E-3-GEOPHYSICS-RESULT, E-3-GEOPHYSICS-VALIDATION
- **Source note**: 物探成果、成果验证小节
#### Slide 30 - 物探章节小结：异常识别需与钻孔、试验和分区成果联动解释
- **Layout**: evidence_chain
- **Core message**: 物探章节小结：异常识别需与钻孔、试验和分区成果联动解释
- **Source mode**: INTERPRETATION
- **Evidence**: E-3-GEOPHYSICS-RESULT, E-3-GEOPHYSICS-VALIDATION, E-3-DRILLING
- **Source note**: 图3.2-30、表3.2-2、T016

### 钻探、孔内成像与水文地质试验 (10 pages)
#### Slide 31 - 66个钻孔针对岩溶发育区、断层影响带和边界径流通道布置
- **Layout**: left_text_right_table
- **Core message**: 66个钻孔针对岩溶发育区、断层影响带和边界径流通道布置
- **Source mode**: ORIGINAL_TEXT
- **Evidence**: E-3-DRILLING, E-3-BOREHOLE-INFO
- **Source note**: 水文地质钻孔章节、T016
#### Slide 32 - 钻孔信息表应拆分展示坐标、孔深、水位和试验类型
- **Layout**: top_text_bottom_table
- **Core message**: 钻孔信息表应拆分展示坐标、孔深、水位和试验类型
- **Source mode**: ORIGINAL_TABLE
- **Evidence**: E-3-BOREHOLE-INFO
- **Source note**: T016
#### Slide 33 - 孔内成像记录节理走向和倾角，补充岩体结构判断
- **Layout**: left_table_right_figure
- **Core message**: 孔内成像记录节理走向和倾角，补充岩体结构判断
- **Source mode**: ORIGINAL_TABLE
- **Evidence**: E-3-BOREHOLE-IMAGING
- **Source note**: 表3.6-1、表3.6-2、图3.6-1至图3.6-2
#### Slide 34 - 抽水试验以潜水非完整井公式计算含水层参数
- **Layout**: left_text_right_table
- **Core message**: 抽水试验以潜水非完整井公式计算含水层参数
- **Source mode**: CALCULATION
- **Evidence**: E-3-PUMPING-TEST
- **Source note**: 表3.4-1至表3.4-6
#### Slide 35 - 6个抽水孔参数结果支撑强富水与极强富水判定
- **Layout**: top_text_bottom_table
- **Core message**: 6个抽水孔参数结果支撑强富水与极强富水判定
- **Source mode**: ORIGINAL_TABLE
- **Evidence**: E-3-PUMPING-TEST, E-3-AQUIFER-RICHNESS
- **Source note**: 表3.4-7、T026、P0583
#### Slide 36 - SK16-6单位涌水量5.3164L/(s·m)，局部达到极强富水
- **Layout**: left_text_right_table
- **Core message**: SK16-6单位涌水量5.3164L/(s·m)，局部达到极强富水
- **Source mode**: ORIGINAL_TEXT
- **Evidence**: E-3-AQUIFER-RICHNESS
- **Source note**: P0583
#### Slide 37 - 13个钻孔202段次压水试验评价岩体透水性
- **Layout**: top_text_bottom_table
- **Core message**: 13个钻孔202段次压水试验评价岩体透水性
- **Source mode**: ORIGINAL_TABLE
- **Evidence**: E-3-PRESSURE-TEST
- **Source note**: T027
#### Slide 38 - 示踪试验部署结果需如实披露未接收到示踪剂信号
- **Layout**: left_table_right_text
- **Core message**: 示踪试验部署结果需如实披露未接收到示踪剂信号
- **Source mode**: ORIGINAL_TABLE
- **Evidence**: E-3-TRACER, E-10-LIMITATIONS
- **Source note**: 表3.4-10、表3.4-11、存在问题
#### Slide 39 - 水化学与同位素样品覆盖地表水、井泉和钻孔点
- **Layout**: left_table_right_figure
- **Core message**: 水化学与同位素样品覆盖地表水、井泉和钻孔点
- **Source mode**: ORIGINAL_TABLE
- **Evidence**: E-3-HYDROCHEM-ISOTOPE
- **Source note**: T033、图3.5-1
#### Slide 40 - 水化学类型与氢氧同位素结果用于识别补给来源
- **Layout**: top_text_bottom_table
- **Core message**: 水化学类型与氢氧同位素结果用于识别补给来源
- **Source mode**: ORIGINAL_TABLE
- **Evidence**: E-3-HYDROCHEM-ISOTOPE
- **Source note**: T034、T035

### 矿区水文地质条件、岩溶发育与强径流带 (12 pages)
#### Slide 41 - 基于物探成果汇总10条断层构造破碎带
- **Layout**: left_table_right_figure
- **Core message**: 基于物探成果汇总10条断层构造破碎带
- **Source mode**: ORIGINAL_TABLE
- **Evidence**: E-4-FAULTS
- **Source note**: 表4.1-1、图4.1-1
#### Slide 42 - 矿区地层、矿体和资源量背景限定含水层空间关系
- **Layout**: top_figure_bottom_text
- **Core message**: 矿区地层、矿体和资源量背景限定含水层空间关系
- **Source mode**: ORIGINAL_FIGURE
- **Evidence**: E-2-REGIONAL
- **Source note**: 图4.1-2、图4.1-3
#### Slide 43 - 68行钻孔岩溶发育统计表需分标高段呈现
- **Layout**: top_text_bottom_table
- **Core message**: 68行钻孔岩溶发育统计表需分标高段呈现
- **Source mode**: ORIGINAL_TABLE
- **Evidence**: E-4-KARST-RATE
- **Source note**: 表4.2-1
#### Slide 44 - 总岩溶率与+35m、+20m、+5m、-10m分区图展示垂向差异
- **Layout**: top_figure_bottom_text
- **Core message**: 总岩溶率与+35m、+20m、+5m、-10m分区图展示垂向差异
- **Source mode**: ORIGINAL_FIGURE
- **Evidence**: E-4-KARST-RATE
- **Source note**: 图4.2-2至图4.2-6
#### Slide 45 - 7条边界水文地质剖面用于刻画垂向岩溶发育
- **Layout**: left_figure_right_text
- **Core message**: 7条边界水文地质剖面用于刻画垂向岩溶发育
- **Source mode**: ORIGINAL_FIGURE
- **Evidence**: E-4-KARST-RATE
- **Source note**: 图4.2-7
#### Slide 46 - 18-2与2-4边界剖面显示东北、东南侧岩溶裂隙带
- **Layout**: top_figure_bottom_text
- **Core message**: 18-2与2-4边界剖面显示东北、东南侧岩溶裂隙带
- **Source mode**: ORIGINAL_FIGURE
- **Evidence**: E-4-KARST-RATE
- **Source note**: 图4.2-8、图4.2-9
#### Slide 47 - 南侧和西北侧剖面显示强发育段与补给区特征
- **Layout**: top_figure_bottom_text
- **Core message**: 南侧和西北侧剖面显示强发育段与补给区特征
- **Source mode**: ORIGINAL_FIGURE
- **Evidence**: E-4-KARST-RATE
- **Source note**: 图4.2-10、图4.2-12、图4.2-13
#### Slide 48 - JL1-JL4四条强径流带是帷幕截水的核心控制对象
- **Layout**: left_figure_right_text
- **Core message**: JL1-JL4四条强径流带是帷幕截水的核心控制对象
- **Source mode**: ORIGINAL_FIGURE
- **Evidence**: E-4-RUNOFF-BELTS
- **Source note**: 图4.2-15、P1475
#### Slide 49 - 强径流带局部证据由物探低速/低阻区、裂隙照片和岩芯照片共同支撑
- **Layout**: mixed_evidence_grid
- **Core message**: 强径流带局部证据由物探低速/低阻区、裂隙照片和岩芯照片共同支撑
- **Source mode**: ORIGINAL_FIGURE
- **Evidence**: E-4-RUNOFF-BELTS, E-3-GEOPHYSICS-RESULT
- **Source note**: 图4.2-16至图4.2-37
#### Slide 50 - 地下水位等值线和动态曲线揭示水位变化格局
- **Layout**: top_figure_bottom_text
- **Core message**: 地下水位等值线和动态曲线揭示水位变化格局
- **Source mode**: ORIGINAL_FIGURE
- **Evidence**: E-4-DYNAMIC
- **Source note**: 图4.2-38至图4.2-41
#### Slide 51 - 排水量动态曲线说明涌水量受降水直接补给影响明显
- **Layout**: left_text_right_figure
- **Core message**: 排水量动态曲线说明涌水量受降水直接补给影响明显
- **Source mode**: ORIGINAL_FIGURE
- **Evidence**: E-4-DYNAMIC
- **Source note**: 图4.2-42、P0992
#### Slide 52 - 富水性分区与突涌水危险性分区锁定重点治理空间
- **Layout**: top_figure_bottom_text
- **Core message**: 富水性分区与突涌水危险性分区锁定重点治理空间
- **Source mode**: ORIGINAL_FIGURE
- **Evidence**: E-5-RICHNESS-ZONING, E-5-RISK-ZONING
- **Source note**: 图5.2-2、图5.2-3

### 矿坑涌水量预测与模型验证 (10 pages)
#### Slide 53 - 水文地质概念模型明确模型范围、边界和充水来源
- **Layout**: top_figure_bottom_text
- **Core message**: 水文地质概念模型明确模型范围、边界和充水来源
- **Source mode**: ORIGINAL_FIGURE
- **Evidence**: E-6-NUMERICAL-MODEL
- **Source note**: 图6.1-1、图6.1-2
#### Slide 54 - 地表水汇入计算使用上游汇水面积、降水量和径流系数
- **Layout**: left_text_right_table
- **Core message**: 地表水汇入计算使用上游汇水面积、降水量和径流系数
- **Source mode**: CALCULATION
- **Evidence**: E-6-RAINFALL-RUNOFF
- **Source note**: 表6.2-1
#### Slide 55 - 降水渗入计算保留近30年降水数据和P-III型拟合曲线
- **Layout**: top_figure_bottom_table
- **Core message**: 降水渗入计算保留近30年降水数据和P-III型拟合曲线
- **Source mode**: CALCULATION
- **Evidence**: E-6-RAINFALL-RUNOFF
- **Source note**: 表6.2-2、图6.2-1、表6.2-7
#### Slide 56 - 比拟法以+50m实测排水量和平台面积/降深推算地下水涌水量
- **Layout**: left_table_right_text
- **Core message**: 比拟法以+50m实测排水量和平台面积/降深推算地下水涌水量
- **Source mode**: CALCULATION
- **Evidence**: E-6-WATER-INFLOW-COMPARE
- **Source note**: 表6.2-8、表6.2-9
#### Slide 57 - 总涌水量表是防治水系统规模和安全冗余的核心依据
- **Layout**: top_text_bottom_table
- **Core message**: 总涌水量表是防治水系统规模和安全冗余的核心依据
- **Source mode**: ORIGINAL_TABLE
- **Evidence**: E-6-WATER-INFLOW-COMPARE
- **Source note**: 表6.2-10
#### Slide 58 - 解析法保留公式选取、渗透系数、含水层厚度和影响半径
- **Layout**: left_text_right_table
- **Core message**: 解析法保留公式选取、渗透系数、含水层厚度和影响半径
- **Source mode**: CALCULATION
- **Evidence**: E-6-WATER-INFLOW-COMPARE
- **Source note**: 表6.3参数与结果
#### Slide 59 - 解析法结果用于校核比拟法，不直接替代控制工况
- **Layout**: top_text_bottom_table
- **Core message**: 解析法结果用于校核比拟法，不直接替代控制工况
- **Source mode**: ORIGINAL_TABLE
- **Evidence**: E-6-WATER-INFLOW-COMPARE, E-6-METHOD-COMPARISON
- **Source note**: 解析法预测结果、预测成果分析
#### Slide 60 - 数值模型用二维剖分和三维地质结构承接预测场景
- **Layout**: top_figure_bottom_text
- **Core message**: 数值模型用二维剖分和三维地质结构承接预测场景
- **Source mode**: ORIGINAL_FIGURE
- **Evidence**: E-6-NUMERICAL-MODEL
- **Source note**: 图6.4-1、图6.4-2
#### Slide 61 - 观测点拟合和天然流场验证模型可用于后续预测
- **Layout**: top_figure_bottom_text
- **Core message**: 观测点拟合和天然流场验证模型可用于后续预测
- **Source mode**: ORIGINAL_FIGURE
- **Evidence**: E-6-NUMERICAL-MODEL
- **Source note**: 图6.4-3至图6.4-5
#### Slide 62 - +35m、+20m、+5m终了线地质结构对应分台阶预测结果
- **Layout**: top_figure_bottom_table
- **Core message**: +35m、+20m、+5m终了线地质结构对应分台阶预测结果
- **Source mode**: ORIGINAL_FIGURE
- **Evidence**: E-6-NUMERICAL-MODEL
- **Source note**: 图6.4-6至图6.4-8、表6.4-4

### 工程地质、地质环境与水资源利用 (6 pages)
#### Slide 63 - 工程地质岩组和岩土分层决定边坡与塌陷风险背景
- **Layout**: left_text_right_table
- **Core message**: 工程地质岩组和岩土分层决定边坡与塌陷风险背景
- **Source mode**: ORIGINAL_TEXT
- **Evidence**: E-7-ENGINEERING-GEOLOGY
- **Source note**: 工程地质条件章节
#### Slide 64 - 岩石物理力学指标支撑边坡稳定性和工程地质类型判断
- **Layout**: top_text_bottom_table
- **Core message**: 岩石物理力学指标支撑边坡稳定性和工程地质类型判断
- **Source mode**: ORIGINAL_TABLE
- **Evidence**: E-7-ENGINEERING-GEOLOGY
- **Source note**: 表7.1-1
#### Slide 65 - 采场边坡划分为3个区，并用四条典型剖面分析
- **Layout**: top_figure_bottom_table
- **Core message**: 采场边坡划分为3个区，并用四条典型剖面分析
- **Source mode**: ORIGINAL_FIGURE
- **Evidence**: E-7-ENGINEERING-GEOLOGY
- **Source note**: 图7.1-1至图7.1-9、表7.1-2
#### Slide 66 - 主要工程地质问题包括塌陷、变形、突水突泥和边坡失稳
- **Layout**: left_text_right_risk_matrix
- **Core message**: 主要工程地质问题包括塌陷、变形、突水突泥和边坡失稳
- **Source mode**: ORIGINAL_TEXT
- **Evidence**: E-7-ENGINEERING-GEOLOGY
- **Source note**: 工程地质问题预测与分析
#### Slide 67 - 矿坑排水水质对照标准未出现超标，为回用与排放提供依据
- **Layout**: top_text_bottom_table
- **Core message**: 矿坑排水水质对照标准未出现超标，为回用与排放提供依据
- **Source mode**: ORIGINAL_TABLE
- **Evidence**: E-8-WATER-QUALITY
- **Source note**: T061-T063、表9.1-3
#### Slide 68 - 矿坑水优先回用于生产，余水排放需配置沉淀与缓冲能力
- **Layout**: left_text_right_flow
- **Core message**: 矿坑水优先回用于生产，余水排放需配置沉淀与缓冲能力
- **Source mode**: ORIGINAL_TEXT
- **Evidence**: E-9-WATER-RESOURCE, E-8-WATER-QUALITY
- **Source note**: 第九章水资源综合利用及供水建议

### 防治水建议、问题披露与评审决策 (6 pages)
#### Slide 69 - 防治水原则强调查明充水条件、层层设防和合理投资
- **Layout**: left_text_right_keypoints
- **Core message**: 防治水原则强调查明充水条件、层层设防和合理投资
- **Source mode**: ORIGINAL_TEXT
- **Evidence**: E-9-WATER-CONTROL
- **Source note**: 矿山防治水原则
#### Slide 70 - 地表堵水、帷幕截水和采坑截渗构成前端控水体系
- **Layout**: left_text_right_figure
- **Core message**: 地表堵水、帷幕截水和采坑截渗构成前端控水体系
- **Source mode**: ORIGINAL_TEXT
- **Evidence**: E-9-WATER-CONTROL, E-4-RUNOFF-BELTS
- **Source note**: 第九章防治水措施、图4.2-15
#### Slide 71 - 预先疏干、超前探水和长期监测控制开采过程不确定性
- **Layout**: left_text_right_sequence
- **Core message**: 预先疏干、超前探水和长期监测控制开采过程不确定性
- **Source mode**: ORIGINAL_TEXT
- **Evidence**: E-9-WATER-CONTROL, E-10-LIMITATIONS
- **Source note**: 第九章防治水措施、存在问题
#### Slide 72 - 实施优先级应围绕强径流带、风险分区和+5m控制工况排序
- **Layout**: decision_matrix
- **Core message**: 实施优先级应围绕强径流带、风险分区和+5m控制工况排序
- **Source mode**: MANAGEMENT_ACTION
- **Evidence**: E-4-RUNOFF-BELTS, E-5-RISK-ZONING, E-6-WATER-INFLOW-COMPARE, E-9-WATER-CONTROL
- **Source note**: 图4.2-15、图5.2-3、表6.2-10、第九章
#### Slide 73 - 问题披露：示踪试验条件不足和开采加深后的动态变化需持续跟踪
- **Layout**: left_text_right_actions
- **Core message**: 问题披露：示踪试验条件不足和开采加深后的动态变化需持续跟踪
- **Source mode**: ORIGINAL_TEXT
- **Evidence**: E-10-LIMITATIONS, E-3-TRACER
- **Source note**: 第十章存在问题、下步建议
#### Slide 74 - 评审确认事项：控制工况、治理边界、监测闭环和设计输入
- **Layout**: decision_summary
- **Core message**: 评审确认事项：控制工况、治理边界、监测闭环和设计输入
- **Source mode**: CONCLUSION
- **Evidence**: E-1-OBJECTIVE, E-4-RUNOFF-BELTS, E-5-RISK-ZONING, E-6-WATER-INFLOW-COMPARE, E-9-WATER-CONTROL, E-10-LIMITATIONS
- **Source note**: 报告目的任务、图4.2-15、图5.2-3、表6.2-10、第九章、第十章

## X. Speaker Notes Requirements

- One notes file per slide under `notes/`.
- Notes use formal engineering review language and cite source notes.
- Target duration: 55-70 minutes for 74 slides.

## XI. Technical Constraints Reminder

- Final PPTX must remain natively editable.
- Keep body text readable; do not shrink source tables below readable floor.
- Source conflicts and limitations remain visible when relevant.
