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
            "content_richness": {
                "minimum_original_source_ratio": 0.55,
                "max_consecutive_interpretation_slides": 2,
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
                "source_mode",
                "evidence_ids",
                "visual_proof",
                "layout_pattern",
                "source_note",
                "Source mode",
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
                "minimum_visible_characters_without_visual": 70,
                "minimum_visual_objects": 1,
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
