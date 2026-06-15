# Design Specification

## I. Purpose

- Audience: 水行政审批机构、评审专家、项目管理单位。
- Objective: 判断 750 万 m³农业灌溉取水方案是否合理、可靠、可监管。
- Narrative: 先给结论，再依次验证边界、总量、需水、水源、退水、影响和落实条件。

## II. Canvas

- Format: PPT 16:9
- ViewBox: 1280 × 720
- Safe margin: 56 px

## III. Visual System

- Style: 克制、专业、工程审查导向。
- Background: 温和浅灰白；关键结论页使用深蓝底。
- Primary: 深水利蓝 `#0B3558`
- Accent: 清水青 `#0E9F9A`
- Secondary: 农业绿 `#63A35C`
- Warning: 土橙 `#D97745`

## IV. Typography

- Font stack: `"Microsoft YaHei", Arial, sans-serif`
- Cover title: 58 px
- Claim title: 34–40 px
- Body: 18–22 px
- Annotation/source: 11–13 px

## V. Layout Rhythm

- Anchor: P01, P02, P10
- Dense: P04, P05, P06, P07, P08
- Breathing: P03, P09
- Macro layouts include cover, verdict rail, range map, bullet chart, bar chart, supply equation, flow balance, risk matrix, roadmap, approval checklist.

## VI. Source Discipline

- No invented values.
- Conflicting extracted values are disclosed rather than silently selected.
- Footer source: `玉泉水库水资源论证报告（送审稿，2026 年 5 月）`.

## VII. Visualization Reference List

| Page | Type | Data |
|---|---|---|
| P04 | horizontal bar / bullet | 控制 3.5 亿 m³，实际 3.4437 亿 m³，静态余量 563 万 m³ |
| P05 | horizontal bar | 作物定额：水稻 584、油菜 87、小麦 66、玉米 134 m³/亩·年 |
| P06 | stacked supply bar | 水库 94.57、东风三干渠 655.43、合计 750 万 m³ |
| P07 | flow balance | 取水 750、耗水 600、回归水 150 万 m³ |

## VIII. Content Outline

See `claim_spine.md`.

