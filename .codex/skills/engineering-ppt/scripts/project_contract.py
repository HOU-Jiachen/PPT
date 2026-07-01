#!/usr/bin/env python3
"""Create the reusable planning and QA contracts for an engineering PPT project."""

from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path


DIRECTORIES = (
    "sources",
    "analysis",
    "images",
    "tables",
    "notes",
    "qa",
    "svg_output",
    "svg_final",
    "exports",
)


def write_json_if_missing(path: Path, payload: dict) -> bool:
    if path.exists():
        return False
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return True


def init_project(
    project: Path, project_name: str | None = None, canvas_format: str = "ppt169"
) -> list[Path]:
    project.mkdir(parents=True, exist_ok=True)
    for directory in DIRECTORIES:
        (project / directory).mkdir(parents=True, exist_ok=True)

    name = project_name or project.name
    created: list[Path] = []
    contracts = {
        project / "project_config.json": {
            "schema_version": "1.0",
            "project": name,
            "canvas_format": canvas_format,
            "created_at": datetime.now().isoformat(timespec="seconds"),
        },
        project / "evidence_ledger.json": {
            "schema_version": "1.0",
            "project": name,
            "updated_at": datetime.now().isoformat(timespec="seconds"),
            "rules": {
                "source_truth": "Only verified source evidence may support FACT or CALCULATION.",
                "conflict_handling": "Keep conflicting source values separate and disclose the conflict.",
            },
            "evidence": [],
        },
        project / "deck_plan.json": {
            "schema_version": "1.0",
            "project": name,
            "deck": {
                "title": "",
                "audience": "",
                "objective": "",
                "chapter_order": [],
            },
            "slides": [],
        },
        project / "qa" / "release_policy.json": {
            "schema_version": "1.0",
            "minimum_font_px": {
                "title": 30,
                "body": 18,
                "body_absolute": 14,
                "table_absolute": 12,
                "chart_label": 14,
                "source": 10,
            },
            "font_exemptions": {
                "footer_y_min_ratio": 0.90,
                "header_y_max_ratio": 0.12,
                "phrases": ["来源：", "Source:"],
                "page_number_regex": "^\\d{1,3}$",
            },
            "layout_collision": {
                "enabled": True,
                "canvas_margin_px": 2,
                "text_overlap_min_ratio": 0.35,
                "text_image_overlap_min_ratio": 0.15,
                "image_min_area_ratio": 0.03,
            },
            "aesthetic_layout": {
                "enabled": True,
                "minimum_box_area_ratio": 0.004,
                "minimum_occupied_area_ratio": 0.18,
                "minimum_structural_occupied_area_ratio": 0.10,
                "maximum_occupied_area_ratio": 0.92,
                "maximum_balance_offset_ratio": 0.22,
                "severe_balance_offset_ratio": 0.32,
                "element_overlap_min_ratio": 0.55,
                "severe_element_overlap_ratio": 0.75,
            },
            "section_dividers": {
                "required": True,
                "before_first_content_chapter": True,
                "label": "chapter_number_and_name",
            },
            "content_richness": {
                "minimum_original_source_ratio": 0.55,
                "max_consecutive_interpretation_slides": 2,
                "max_summary_or_overall_pages": 3,
                "summary_page_types": [
                    "overview",
                    "summary",
                    "chapter_summary",
                    "conclusion",
                    "closing",
                    "management_action",
                ],
                "preferred_mixed_layouts": [
                    "left_text_right_figure",
                    "left_figure_right_text",
                    "top_text_bottom_figure",
                    "top_figure_bottom_text",
                    "left_text_right_table",
                    "left_table_right_text",
                    "top_text_bottom_table",
                    "top_table_bottom_text",
                ],
            },
            "forbidden_visible_phrases": [
                "报告原文摘录",
                "工程原文摘录",
                "表中缺失项沿用报告提取状态",
                "不做补造",
                "不作补造",
                "审查提示",
                "数据提示",
                "口径A",
                "口径B",
                "本次审查",
                "静态余量",
                "来源模式",
                "证据编号",
                "本页用于",
                "证据解读",
                "原表定位",
                "行列规模",
                "密集表按重点行重排",
                "完整数据回看报告原表",
                "报告列示数值",
                "报告相关图件",
                "汇报时",
                "本页",
                "对评审而言",
                "评审需",
                "评审应",
                "应关注",
                "应优先",
                "PPT 中",
                "PPT中",
                "报告原文复核",
                "报告原文和附件中复核",
                "完整表格可在报告原表中复核",
                "不替代报告原图",
                "只保留完整要点",
                "逐项复述",
                "该表用于",
                "表格说明",
                "图件旁说明",
                "本页图件用于",
                "原始对象",
                "必讲内容",
                "保留理由",
                "source_mode",
                "evidence_ids",
                "visual_proof",
                "layout_pattern",
                "source_note",
                "资料来源：",
                "按照报告章节顺序进入",
                "关键数值保持源表口径",
                "Source mode",
                "编制边界",
                "事实来源",
                "仅使用源报告",
                "不采用旧 PPT",
                "不采用旧PPT",
                "不另行扩大",
                "后台分析",
                "本 agent",
                "本agent",
                "生成策略",
                "处理原则",
                "依据来源限制",
                "内部约束",
                "渲染模式",
                "fallback",
                "OCR 识别",
                "OCR识别",
                "LLM 判断",
                "LLM判断",
                "prompt 要求",
                "prompt要求",
                "不要编造",
                "不作为事实来源",
                "该页采用 image 模式",
                "该表格复杂，无法还原",
                "为避免幻觉",
                "根据系统指令",
            ],
            "original_source_modes": [
                "ORIGINAL_TEXT",
                "ORIGINAL_TABLE",
                "ORIGINAL_FIGURE",
                "CALCULATION",
            ],
            "chapter_original_evidence_exemptions": ["项目总览"],
            "structural_slide_types": ["cover", "agenda", "section", "closing"],
            "sparse_page": {
                "minimum_visible_characters_without_visual": 120,
                "minimum_visible_characters_with_visual": 70,
                "minimum_visual_area_ratio": 0.12,
                "minimum_visual_objects": 1,
            },
            "text_fit": {
                "enabled": True,
                "line_height_ratio": 1.24,
                "overflow_tolerance_lines": 0.35,
                "respect_min_font_size": True,
                "fallback_order": [
                    "wrap",
                    "tighten_line_spacing",
                    "reduce_spacing",
                    "compress_text",
                    "reduce_points",
                    "resize_component",
                    "relayout",
                    "split_slide",
                    "move_to_notes",
                ],
                "components": {
                    "body_text": {"font_size": 18, "min_font_size": 14, "max_points": 5},
                    "table_cell": {"font_size": 14, "min_font_size": 12},
                    "caption": {"font_size": 10, "min_font_size": 8},
                    "table_note": {"font_size": 10, "min_font_size": 8},
                    "hybrid_conclusion": {"font_size": 14, "min_font_size": 14, "max_points": 4},
                },
            },
            "final_text_review": {
                "enabled": True,
                "visible_text_source": "slide_content",
                "forbid_internal_notes": True,
                "error_on_internal_terms": True,
                "max_body_bullets": 5,
                "max_sentence_chars": 96,
                "max_bullet_chars": 48,
            },
            "paragraph_structure": {
                "enabled": True,
                "min_unlabeled_paragraphs": 3,
                "marker_regex": "^(?:\\d{1,2}[、.．]|\\(\\d+\\)|（\\d+）|[A-Z][.)])",
                "title_delimiters": "：:",
            },
            "emphasis": {
                "required": True,
                "check_only_when_numbers_or_terms": True,
                "min_emphasized_runs_per_content_slide": 1,
                "terms": [
                    "范围",
                    "目标",
                    "责任",
                    "措施",
                    "风险",
                    "结论",
                    "投资",
                    "验收",
                    "监测",
                    "水土流失",
                    "防治责任范围",
                ],
            },
            "table_fidelity": {
                "enabled": True,
                "require_table_ir": True,
                "allowed_render_modes": ["native", "image", "hybrid", "auto"],
                "complex_tables_default_to_image": True,
                "image_modes_require_crop_asset": True,
                "llm_must_not_reconstruct_complex_tables": True,
                "require_docx_table_models_for_docx_sources": True,
                "small_medium_max_rows": 10,
                "small_medium_max_cols": 7,
                "header_missing_error_ratio": 0.4,
                "native_merge_required_for_merged_small_tables": True,
                "unsupported_table_number_is_error": True,
                "image_table_min_effective_pt": 10,
                "table_image_source_dpi": 220,
                "skip_tables_requiring_cross_page": True,
            },
            "post_generation_review": {
                "enabled": True,
                "max_repair_rounds": 3,
                "issue_list_schema": "structured",
                "blocking_severities": ["critical", "high"],
                "review_stages": [
                    "ContentReview",
                    "FormatReview",
                    "FactConsistencyReview",
                    "VisualReview",
                    "AutoRepair",
                ],
                "report": "qa/review_report.json",
            },
            "duplicate_content": {
                "enabled": True,
                "max_consecutive_body_similarity": 0.9,
                "minimum_body_characters": 80,
            },
        },
    }
    for path, payload in contracts.items():
        if write_json_if_missing(path, payload):
            created.append(path)
    return created


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("project", type=Path)
    parser.add_argument("--name")
    parser.add_argument("--format", default="ppt169")
    args = parser.parse_args()
    created = init_project(args.project.resolve(), args.name, args.format)
    print(
        json.dumps(
            {
                "project": str(args.project.resolve()),
                "created": [str(path) for path in created],
                "contracts_ready": True,
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
