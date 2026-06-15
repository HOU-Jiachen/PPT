#!/usr/bin/env python3
"""Create a reviewable deck_plan/evidence ledger from a legacy slide manifest."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


STRUCTURAL = {"cover", "agenda", "section", "closing"}
MODE_BY_TYPE = {
    "source_text": "ORIGINAL_TEXT",
    "figure": "ORIGINAL_FIGURE",
    "table": "ORIGINAL_TABLE",
    "analysis": "INTERPRETATION",
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("project", type=Path)
    parser.add_argument("manifest", type=Path)
    args = parser.parse_args()
    project = args.project.resolve()
    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    slides = []
    evidence = []
    current_chapter = "项目总览"
    for item in manifest:
        page = int(item["page"])
        slide_type = str(item.get("type", ""))
        if slide_type == "section":
            current_chapter = str(item.get("title", "")).strip()
        evidence_ids = []
        source = str(item.get("source", "")).replace("来源：", "").strip()
        if slide_type not in STRUCTURAL:
            evidence_id = f"LEGACY-P{page:03d}"
            evidence_ids = [evidence_id]
            evidence.append(
                {
                    "id": evidence_id,
                    "kind": MODE_BY_TYPE.get(slide_type, "INTERPRETATION"),
                    "summary": item.get("title", ""),
                    "source_file": "",
                    "source_locator": source,
                    "catalog_ids": [],
                    "verification_status": "needs-verification",
                    "visible_numbers": [],
                    "notes": "Migrated from legacy manifest; verify against original source.",
                }
            )
        slides.append(
            {
                "page": page,
                "type": slide_type,
                "chapter": current_chapter,
                "title": item.get("title", ""),
                "source_mode": MODE_BY_TYPE.get(slide_type, ""),
                "evidence_ids": evidence_ids,
                "visual_proof": slide_type if slide_type not in STRUCTURAL else "",
                "source_note": source,
            }
        )
    plan = {
        "schema_version": "1.0",
        "project": project.name,
        "deck": {"title": "", "audience": "", "objective": "", "chapter_order": []},
        "slides": slides,
    }
    ledger = {
        "schema_version": "1.0",
        "project": project.name,
        "rules": {},
        "evidence": evidence,
    }
    (project / "deck_plan.json").write_text(
        json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    (project / "evidence_ledger.json").write_text(
        json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps({"slides": len(slides), "evidence": len(evidence)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
