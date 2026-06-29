# 东坡大道水土保持方案 - Design Spec

## I. Project Information

| Item | Value |
| ---- | ----- |
| **Project Name** | 黄冈市东坡大道片区污水收集管网建设工程水土保持方案汇报 |
| **Canvas Format** | PPT 16:9 (1280x720) |
| **Page Count** | 31 |
| **Design Style** | 克制的市政工程技术评审风格，突出报告原表、关键参数、预测计算和措施闭环 |
| **Target Audience** | 建设单位、行政主管部门、水土保持评审专家及项目实施相关方 |
| **Use Case** | 水土保持方案技术评审与建设管理汇报 |
| **Created Date** | 2026-06-29 |

## II. Canvas Specification

| Property | Value |
| -------- | ----- |
| **Format** | PPT 16:9 |
| **Dimensions** | 1280x720 |
| **viewBox** | `0 0 1280 720` |
| **Margins** | left/right 40-60px, top 30px, footer 24px |
| **Content Area** | 1200x600px |

## III. Visual Theme

- **Style**: source-faithful Chinese engineering review presentation
- **Theme**: light technical pages with deep-blue section rhythm
- **Tone**: evidence-first, technical, restrained
- **Chapter rhythm**: each report chapter starts with a section divider slide carrying the chapter number and name.

| Role | HEX | Purpose |
| ---- | --- | ------- |
| **Background** | `#F7F9FC` | Page background |
| **Secondary bg** | `#F1F6FA` | Technical bands and table surfaces |
| **Primary** | `#01203C` | Chapter headers and emphasis |
| **Accent** | `#4489C8` | Section labels and engineering highlights |
| **Warning** | `#A33A2B` | High-risk values and limitations |
| **Body text** | `#01203C` | Main body text |
| **Secondary text** | `#566B7F` | Captions, source notes |
| **Border/divider** | `#CCD8E2` | Table and figure frames |

## IV. Typography System

**Typography direction**: CJK-primary professional sans with serif fallback for report quotations.

| Role | Chinese | English | Fallback tail |
| ---- | ------- | ------- | ------------- |
| **Title** | `"Microsoft YaHei"` | `Arial` | `sans-serif` |
| **Body** | `"Microsoft YaHei"` | `Arial` | `sans-serif` |
| **Emphasis** | `SimSun` | `Georgia` | `serif` |
| **Code** | — | `Consolas, "Courier New"` | `monospace` |

**Baseline**: Body font size = 18px.

## V. Layout Principles

- Header area: title + chapter + page number.
- Content area prioritizes original figure/table readability.
- Visible slides do not show bottom-left source footers; source notes stay in backend records and speaker notes.
- Dense technical pages avoid decorative cards; tables and figures use framed source panels.
- Visible panel headings must be content-specific, such as `图件重点：矿区强径流带分布` or `表格重点：涌水量预测结果`.
- Generic workflow labels such as `报告对图件的说明`, `报告对表格的说明`, `报告计算口径`, and `报告阐述` are forbidden in visible slides.
- Report section headings, figure captions, table captions and corresponding subsection titles take priority over agent-generated topic labels.
- Visible ellipses are forbidden; long report text must be shortened to complete, source-faithful sentences or split across slides.
- Horizontal report maps/profiles/charts should use top-figure/bottom-text layouts when side-by-side placement would make the figure too small.
- Internal planning metadata, evidence IDs, asset filenames and row/column diagnostics remain only in backend contracts/QA.

## VI. Icon Usage Specification

- Icons are sparse; source figures and tables carry most visual meaning.

## VII. Visualization Reference List

The deck uses report-native tables, maps, figures and formulas because source fidelity is more important than restyling source data.

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Layout pattern | Acquire Via | Status | Reference | text_policy | page_role |
| -------- | ---------- | ----- | ------- | ---- | -------------- | ----------- | ------ | --------- | ----------- | --------- |

## IX. Content Outline

### 综合说明与审批依据 (2 pages)
#### Slide 03 - 综合报告表给出项目全局控制指标
- **Layout**: left_table_right_text
- **Core message**: 综合报告表给出项目全局控制指标
- **Source mode**: ORIGINAL_TABLE
- **Evidence**: E-001
- **Source note**: T004
#### Slide 04 - 前期批复和编制依据明确方案边界
- **Layout**: text_with_keypoints
- **Core message**: 前期批复和编制依据明确方案边界
- **Source mode**: ORIGINAL_TEXT
- **Evidence**: E-002
- **Source note**: P0036、P0037、P0079、P0080、P0082

### 项目概况与工程布置 (3 pages)
#### Slide 05 - 建设项目工程特性表锁定规模、投资与工期
- **Layout**: left_table_right_text
- **Core message**: 建设项目工程特性表锁定规模、投资与工期
- **Source mode**: ORIGINAL_TABLE
- **Evidence**: E-003
- **Source note**: T008、P0207
#### Slide 06 - 项目位于黄州区城北片区并沿多条道路布设
- **Layout**: top_figure_bottom_text
- **Core message**: 项目位于黄州区城北片区并沿多条道路布设
- **Source mode**: ORIGINAL_FIGURE
- **Evidence**: E-004
- **Source note**: P0065、P0066、P0071、T009
#### Slide 07 - 施工组织与顶管工艺决定扰动范围和防护时序
- **Layout**: top_figure_bottom_text
- **Core message**: 施工组织与顶管工艺决定扰动范围和防护时序
- **Source mode**: ORIGINAL_FIGURE
- **Evidence**: E-005
- **Source note**: T010、T011

### 防治责任范围与标准目标 (2 pages)
#### Slide 08 - 防治责任范围全部为临时占地 34416.00m²
- **Layout**: left_table_right_text
- **Core message**: 防治责任范围全部为临时占地 34416.00m²
- **Source mode**: ORIGINAL_TABLE
- **Evidence**: E-006
- **Source note**: T006、P0125、T013、P0252
#### Slide 09 - 六项防治指标采用南方红壤区一级标准
- **Layout**: left_table_right_text
- **Core message**: 六项防治指标采用南方红壤区一级标准
- **Source mode**: ORIGINAL_TABLE
- **Evidence**: E-007
- **Source note**: T007、P0134

### 水土保持评价与土石方 (3 pages)
#### Slide 10 - 法制约因素与技术标准评价结论均为符合
- **Layout**: top_table_bottom_text
- **Core message**: 法制约因素与技术标准评价结论均为符合
- **Source mode**: ORIGINAL_TABLE
- **Evidence**: E-008
- **Source note**: T018、P0319、T019、P0322、T020、P0325
#### Slide 11 - 土石方平衡显示弃方委托处置、借方外购
- **Layout**: left_table_right_text
- **Core message**: 土石方平衡显示弃方委托处置、借方外购
- **Source mode**: ORIGINAL_TABLE
- **Evidence**: E-009
- **Source note**: T015、P0264、T016
#### Slide 12 - 主体工程已列水保措施以土地整治和铺种草皮为主
- **Layout**: left_table_right_text
- **Core message**: 主体工程已列水保措施以土地整治和铺种草皮为主
- **Source mode**: ORIGINAL_TABLE
- **Evidence**: E-010
- **Source note**: T021、P0369

### 水土流失分析与预测 (4 pages)
#### Slide 13 - 扰动地表面积与预测单元集中在管网工程区
- **Layout**: top_table_bottom_text
- **Core message**: 扰动地表面积与预测单元集中在管网工程区
- **Source mode**: ORIGINAL_TABLE
- **Evidence**: E-011
- **Source note**: T023、P0392、T025、P0401、T026、P0407
#### Slide 14 - 背景土壤侵蚀模数取 261.46t/km²·a
- **Layout**: left_table_right_text
- **Core message**: 背景土壤侵蚀模数取 261.46t/km²·a
- **Source mode**: CALCULATION
- **Evidence**: E-012
- **Source note**: T027、P0412、T028、P0420
#### Slide 15 - 施工期扰动后侵蚀模数显著高于背景值
- **Layout**: left_table_right_text
- **Core message**: 施工期扰动后侵蚀模数显著高于背景值
- **Source mode**: CALCULATION
- **Evidence**: E-013
- **Source note**: T030、P0463、T031、P0471、T032、P0474、T033、P0476
#### Slide 16 - 预测土壤流失总量 104.05t，新增量 94.92t
- **Layout**: left_table_right_text
- **Core message**: 预测土壤流失总量 104.05t，新增量 94.92t
- **Source mode**: ORIGINAL_TABLE
- **Evidence**: E-014
- **Source note**: T034、P0496

### 水土保持措施与施工安排 (3 pages)
#### Slide 17 - 防治分区为管网工程区，防治面积 34416.00m²
- **Layout**: left_table_right_text
- **Core message**: 防治分区为管网工程区，防治面积 34416.00m²
- **Source mode**: ORIGINAL_TABLE
- **Evidence**: E-015
- **Source note**: T035、P0523
#### Slide 18 - 措施体系覆盖工程、植物和临时三类措施
- **Layout**: left_table_right_text
- **Core message**: 措施体系覆盖工程、植物和临时三类措施
- **Source mode**: ORIGINAL_TABLE
- **Evidence**: E-016
- **Source note**: T036、P0549、T037、P0573
#### Slide 19 - 措施实施进度需嵌入 2025—2026 年施工窗口
- **Layout**: top_table_bottom_text
- **Core message**: 措施实施进度需嵌入 2025—2026 年施工窗口
- **Source mode**: ORIGINAL_TABLE
- **Evidence**: E-017
- **Source note**: T038、P0601

### 投资概算、效益与管理验收 (5 pages)
#### Slide 20 - 水土保持估算总投资为 26.9211 万元
- **Layout**: left_table_right_text
- **Core message**: 水土保持估算总投资为 26.9211 万元
- **Source mode**: ORIGINAL_TABLE
- **Evidence**: E-018
- **Source note**: T040、P0679
#### Slide 21 - 工程、植物、临时和独立费用共同构成新增投资
- **Layout**: top_table_bottom_text
- **Core message**: 工程、植物、临时和独立费用共同构成新增投资
- **Source mode**: ORIGINAL_TABLE
- **Evidence**: E-019
- **Source note**: T041、P0680、T042、P0681、T043、P0682、T044、P0683
#### Slide 22 - 水土保持补偿费 51624 元符合免征情形
- **Layout**: left_table_right_text
- **Core message**: 水土保持补偿费 51624 元符合免征情形
- **Source mode**: ORIGINAL_TABLE
- **Evidence**: E-020
- **Source note**: T045、P0684
#### Slide 23 - 六项防治效果达到或高于目标值
- **Layout**: left_table_right_text
- **Core message**: 六项防治效果达到或高于目标值
- **Source mode**: ORIGINAL_TABLE
- **Evidence**: E-021
- **Source note**: T048、P0700
#### Slide 24 - 后续管理需落实组织管理、监理施工和设施验收
- **Layout**: text_with_keypoints
- **Core message**: 后续管理需落实组织管理、监理施工和设施验收
- **Source mode**: MANAGEMENT_ACTION
- **Evidence**: E-022
- **Source note**: T049、T050、T051

## X. Speaker Notes Requirements

- One notes file per slide under `notes/`.
- Notes use formal engineering review language and cite source notes.

## XI. Technical Constraints Reminder

- Final PPTX must remain natively editable.
- Keep body text readable; do not shrink source tables below readable floor.
- Source conflicts and limitations remain visible when relevant.
