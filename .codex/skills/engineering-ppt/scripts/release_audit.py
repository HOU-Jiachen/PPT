#!/usr/bin/env python3
"""Audit engineering PPT planning artifacts, SVG output, and the exported PPTX."""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
import zipfile
from collections import defaultdict
from pathlib import Path
from xml.etree import ElementTree as ET

from lxml import etree
from pptx import Presentation


NUMBER_RE = re.compile(r"(?<![\w.])[-+]?\d+(?:\.\d+)?%?(?![\w.])")
SVG_NS = {"svg": "http://www.w3.org/2000/svg"}
STRUCTURAL_DEFAULT = {"cover", "agenda", "section", "closing"}
ORIGINAL_MODES_DEFAULT = {"ORIGINAL_TEXT", "ORIGINAL_TABLE", "ORIGINAL_FIGURE", "CALCULATION"}


def display_path(path: Path, base: Path | None = None) -> str:
    resolved = path.resolve()
    roots = [base.resolve()] if base else []
    roots.append(Path.cwd().resolve())
    for root in roots:
        try:
            return resolved.relative_to(root).as_posix()
        except ValueError:
            continue
    return resolved.name


class Audit:
    def __init__(self) -> None:
        self.items: list[dict] = []

    def add(self, level: str, code: str, message: str, **context: object) -> None:
        self.items.append(
            {"level": level, "code": code, "message": message, "context": context}
        )

    def error(self, code: str, message: str, **context: object) -> None:
        self.add("error", code, message, **context)

    def warning(self, code: str, message: str, **context: object) -> None:
        self.add("warning", code, message, **context)

    def info(self, code: str, message: str, **context: object) -> None:
        self.add("info", code, message, **context)

    def summary(self) -> dict:
        counts = defaultdict(int)
        for item in self.items:
            counts[item["level"]] += 1
        return {
            "errors": counts["error"],
            "warnings": counts["warning"],
            "info": counts["info"],
            "release_ready": counts["error"] == 0,
        }


def load_json(path: Path, audit: Audit, required: bool = True) -> dict:
    if not path.exists():
        if required:
            audit.error("missing-file", f"Required file is missing: {path.name}", path=str(path))
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8-sig"))
    except Exception as exc:
        audit.error("invalid-json", f"Invalid JSON: {path.name}", error=str(exc))
        return {}


def normalize_number(token: str) -> str:
    suffix = "%" if token.endswith("%") else ""
    raw = token[:-1] if suffix else token
    try:
        value = float(raw)
    except ValueError:
        return token
    if math.isclose(value, round(value), abs_tol=1e-10):
        return f"{int(round(value))}{suffix}"
    return f"{value:.10f}".rstrip("0").rstrip(".") + suffix


def collect_numbers(text: str) -> set[str]:
    return {normalize_number(token) for token in NUMBER_RE.findall(text)}


def visible_svg_text(path: Path) -> tuple[str, list[dict], int]:
    tree = ET.parse(path)
    root = tree.getroot()
    texts: list[str] = []
    text_nodes: list[dict] = []
    for node in root.findall(".//svg:text", SVG_NS):
        value = "".join(node.itertext()).strip()
        if not value:
            continue
        texts.append(value)
        text_nodes.append(
            {
                "text": value,
                "x": node.attrib.get("x"),
                "y": node.attrib.get("y"),
                "font_size": node.attrib.get("font-size"),
                "anchor": node.attrib.get("text-anchor", "start"),
            }
        )
    visual_count = len(root.findall(".//svg:image", SVG_NS))
    visual_count += len(root.findall(".//svg:path", SVG_NS))
    visual_count += len(root.findall(".//svg:polyline", SVG_NS))
    return "\n".join(texts), text_nodes, visual_count


def estimated_text_overflow(node: dict, width: float, height: float) -> bool:
    try:
        x = float(node["x"])
        y = float(node["y"])
        size = float(node["font_size"])
    except (TypeError, ValueError):
        return False
    text = node["text"]
    estimated = sum(1.0 if ord(ch) > 127 else 0.56 for ch in text) * size
    anchor = node["anchor"]
    left = x if anchor == "start" else x - estimated if anchor == "end" else x - estimated / 2
    right = left + estimated
    return left < -2 or right > width + 2 or y - size < -2 or y > height + 2


def parse_font_size(value: object) -> float | None:
    if value is None:
        return None
    match = re.search(r"[-+]?\d+(?:\.\d+)?", str(value))
    if not match:
        return None
    return float(match.group(0))


def is_template_or_meta_text(node: dict, width: float, height: float, policy: dict) -> bool:
    exemptions = policy.get("font_exemptions", {})
    text = str(node.get("text", "")).strip()
    try:
        x = float(node.get("x") or 0)
        y = float(node.get("y") or 0)
    except (TypeError, ValueError):
        return False

    footer_y_min = float(exemptions.get("footer_y_min_ratio", 0.90)) * height
    header_y_max = float(exemptions.get("header_y_max_ratio", 0.12)) * height
    if y >= footer_y_min or y <= header_y_max:
        return True

    for phrase in exemptions.get("phrases", ["来源：", "Source:"]):
        if phrase and text.startswith(str(phrase)):
            return True

    page_number_regex = exemptions.get("page_number_regex")
    if page_number_regex and re.fullmatch(str(page_number_regex), text):
        return x <= width * 0.08 or x >= width * 0.92 or y >= footer_y_min

    return False


def audit_plan(
    project: Path,
    plan: dict,
    ledger: dict,
    policy: dict,
    strict: bool,
    audit: Audit,
) -> dict[int, dict]:
    slides = plan.get("slides", [])
    evidence = {item.get("id"): item for item in ledger.get("evidence", []) if item.get("id")}
    structural = set(policy.get("structural_slide_types", STRUCTURAL_DEFAULT))
    original_modes = set(policy.get("original_source_modes", ORIGINAL_MODES_DEFAULT))
    chapter_exemptions = set(
        policy.get("chapter_original_evidence_exemptions", ["项目总览"])
    )
    pages: dict[int, dict] = {}
    chapter_modes: dict[str, set[str]] = defaultdict(set)

    if strict and not slides:
        audit.error("empty-deck-plan", "deck_plan.json has no slides.")
        return pages

    for slide in slides:
        page = slide.get("page")
        if not isinstance(page, int):
            audit.error("invalid-page", "Every slide must have an integer page number.", slide=slide)
            continue
        pages[page] = slide
        slide_type = str(slide.get("type", "")).lower()
        title = str(slide.get("title", "")).strip()
        chapter = str(slide.get("chapter", "")).strip()
        source_mode = str(slide.get("source_mode", "")).upper()
        evidence_ids = slide.get("evidence_ids", [])

        if not title:
            audit.error("missing-title", "Slide title is empty.", page=page)
        if slide_type not in structural:
            if not chapter:
                audit.error("missing-chapter", "Content slide has no chapter.", page=page)
            if not source_mode:
                audit.error("missing-source-mode", "Content slide has no source_mode.", page=page)
            if not evidence_ids:
                audit.error("missing-evidence", "Content slide has no evidence_ids.", page=page)
        for evidence_id in evidence_ids:
            item = evidence.get(evidence_id)
            if item is None:
                audit.error(
                    "unknown-evidence",
                    "Slide references an unknown evidence ID.",
                    page=page,
                    evidence_id=evidence_id,
                )
            elif item.get("verification_status") != "verified":
                level = audit.error if strict else audit.warning
                level(
                    "unverified-evidence",
                    "Evidence must be verified against the original source.",
                    page=page,
                    evidence_id=evidence_id,
                )
            else:
                evidence_text = " ".join(
                    str(item.get(key, ""))
                    for key in ("summary", "exact_text", "values", "notes")
                )
                slide.setdefault("_allowed_numbers", [])
                slide["_allowed_numbers"].extend(sorted(collect_numbers(evidence_text)))
        if chapter and source_mode:
            chapter_modes[chapter].add(source_mode)

    for chapter, modes in chapter_modes.items():
        if chapter not in chapter_exemptions and not modes.intersection(original_modes):
            audit.error(
                "chapter-without-original-evidence",
                "Chapter has no original text, table, figure, or calculation slide.",
                chapter=chapter,
                modes=sorted(modes),
            )

    richness = policy.get("content_richness", {})
    substantive = [
        slide for slide in slides if str(slide.get("type", "")).lower() not in structural
    ]
    if substantive:
        original_count = sum(
            1
            for slide in substantive
            if str(slide.get("source_mode", "")).upper() in original_modes
        )
        ratio = original_count / len(substantive)
        minimum_ratio = float(richness.get("minimum_original_source_ratio", 0))
        if strict and minimum_ratio and ratio < minimum_ratio:
            audit.error(
                "insufficient-original-source-coverage",
                "Substantive slides do not preserve enough original text, tables, figures, or calculations.",
                original_slides=original_count,
                substantive_slides=len(substantive),
                ratio=round(ratio, 3),
                minimum_ratio=minimum_ratio,
            )

        max_consecutive = int(richness.get("max_consecutive_interpretation_slides", 0))
        if strict and max_consecutive:
            run: list[int] = []
            for slide in slides:
                slide_type = str(slide.get("type", "")).lower()
                source_mode = str(slide.get("source_mode", "")).upper()
                if slide_type in structural or source_mode in original_modes:
                    run = []
                    continue
                if source_mode:
                    run.append(slide.get("page"))
                    if len(run) > max_consecutive:
                        audit.error(
                            "too-many-consecutive-summary-slides",
                            "Too many consecutive non-original-evidence slides.",
                            pages=run,
                            max_consecutive=max_consecutive,
                        )
                        run = run[-max_consecutive:]
    return pages


def scan_forbidden(text: str, phrases: list[str], audit: Audit, artifact: str) -> None:
    for phrase in phrases:
        if phrase and phrase in text:
            audit.error(
                "forbidden-visible-phrase",
                "Internal workflow wording is visible in the deck.",
                phrase=phrase,
                artifact=artifact,
            )


def audit_ledger(ledger: dict, catalog: dict, strict: bool, audit: Audit) -> None:
    catalog_ids = {item.get("id") for item in catalog.get("entries", []) if item.get("id")}
    seen = set()
    allowed_kinds = {
        "FACT",
        "ORIGINAL_TEXT",
        "ORIGINAL_TABLE",
        "ORIGINAL_FIGURE",
        "CALCULATION",
        "INTERPRETATION",
        "RECOMMENDATION",
    }
    for item in ledger.get("evidence", []):
        evidence_id = item.get("id")
        if not evidence_id:
            audit.error("evidence-without-id", "Evidence record has no ID.")
            continue
        if evidence_id in seen:
            audit.error("duplicate-evidence-id", "Evidence ID is duplicated.", evidence_id=evidence_id)
        seen.add(evidence_id)
        kind = str(item.get("kind", "")).upper()
        if kind not in allowed_kinds:
            audit.error("invalid-evidence-kind", "Evidence kind is invalid.", evidence_id=evidence_id)
        if item.get("verification_status") == "verified":
            required = ("source_file", "source_locator", "catalog_ids")
            for field in required:
                if not item.get(field):
                    audit.error(
                        "incomplete-verified-evidence",
                        "Verified evidence lacks source traceability.",
                        evidence_id=evidence_id,
                        field=field,
                    )
            for catalog_id in item.get("catalog_ids", []):
                if catalog_id not in catalog_ids:
                    audit.error(
                        "unknown-catalog-id",
                        "Verified evidence references an unknown source-catalog ID.",
                        evidence_id=evidence_id,
                        catalog_id=catalog_id,
                    )
            if kind == "CALCULATION":
                if not item.get("formula") or not item.get("inputs"):
                    audit.error(
                        "incomplete-calculation",
                        "Verified calculation must include formula and verified inputs.",
                        evidence_id=evidence_id,
                    )
        elif strict:
            # Slide-level checks identify use of unverified evidence. This catches unused
            # records too, preventing a misleading all-clear ledger.
            audit.warning(
                "ledger-record-not-verified",
                "Evidence ledger contains a record that is not verified.",
                evidence_id=evidence_id,
            )


def audit_svgs(
    project: Path,
    pages: dict[int, dict],
    policy: dict,
    source_numbers: set[str],
    strict: bool,
    audit: Audit,
) -> int:
    candidates = [project / "svg_final", project / "svg_output"]
    candidates.extend(project.glob("*/svg_final"))
    candidates.extend(project.glob("*/svg_output"))
    candidate_files = [
        (directory, sorted(directory.glob("*.svg")))
        for directory in candidates
        if directory.exists()
    ]
    svg_dir, files = max(candidate_files, key=lambda item: len(item[1]), default=(project, []))
    if not files:
        audit.warning("no-svg", "No SVG output found; visual-content checks were skipped.")
        return 0
    audit.info("svg-directory", "Auditing SVG directory.", path=display_path(svg_dir), slides=len(files))

    phrases = policy.get("forbidden_visible_phrases", [])
    sparse = policy.get("sparse_page", {})
    min_chars = int(sparse.get("minimum_visible_characters_without_visual", 70))
    for path in files:
        match = re.match(r"(\d+)", path.stem)
        page_number = int(match.group(1)) if match else 0
        slide = pages.get(page_number, {})
        slide_type = str(slide.get("type", path.stem.split("_", 1)[-1])).lower()
        text, nodes, visual_count = visible_svg_text(path)
        scan_forbidden(text, phrases, audit, path.name)

        tree = ET.parse(path)
        root = tree.getroot()
        viewbox = [float(value) for value in root.attrib.get("viewBox", "0 0 1280 720").split()]
        width, height = viewbox[2], viewbox[3]
        for node in nodes:
            if estimated_text_overflow(node, width, height):
                audit.error(
                    "probable-text-overflow",
                    "A single SVG text line probably crosses the canvas boundary.",
                    page=page_number,
                    text=node["text"],
                )
            min_font = (
                policy.get("minimum_font_px", {}).get("body_absolute")
                or policy.get("minimum_font_px", {}).get("body_minimum")
                or 14
            )
            size = parse_font_size(node.get("font_size"))
            if (
                strict
                and size is not None
                and size < float(min_font)
                and not is_template_or_meta_text(node, width, height, policy)
            ):
                audit.error(
                    "body-font-too-small",
                    "Visible PPT body text is below the absolute minimum font size.",
                    page=page_number,
                    text=node["text"],
                    font_size=size,
                    minimum=float(min_font),
                )

        if slide_type not in STRUCTURAL_DEFAULT and not slide.get("density_exempt_reason"):
            visible_chars = len(re.sub(r"\s+", "", text))
            if visible_chars < min_chars and visual_count == 0:
                audit.warning(
                    "sparse-page",
                    "Page has little visible text and no figure/path-based visual proof.",
                    page=page_number,
                    visible_characters=visible_chars,
                )

        allowed_numbers = set(source_numbers)
        allowed_numbers.update(slide.get("_allowed_numbers", []))
        ignored = {str(page_number)}
        ignored.update(collect_numbers(str(slide.get("source_note", ""))))
        chapter_match = re.search(r"第\s*(\d+)\s*章", str(slide.get("chapter", "")))
        if chapter_match:
            ignored.add(chapter_match.group(1))
        unsupported = sorted(collect_numbers(text) - allowed_numbers - ignored)
        if unsupported:
            level = audit.error if strict else audit.warning
            level(
                "unsupported-number",
                "Visible number was not found in the normalized source corpus.",
                page=page_number,
                numbers=unsupported,
            )
    return len(files)


def pptx_text(archive: zipfile.ZipFile) -> str:
    values = []
    for name in archive.namelist():
        if not name.startswith("ppt/slides/slide") or not name.endswith(".xml"):
            continue
        root = etree.fromstring(archive.read(name))
        values.extend(root.xpath("//a:t/text()", namespaces={"a": "http://schemas.openxmlformats.org/drawingml/2006/main"}))
    return "\n".join(values)


def audit_pptx(path: Path, expected_slides: int, policy: dict, audit: Audit) -> None:
    if not path.exists():
        audit.error("missing-pptx", "Requested PPTX does not exist.", path=display_path(path))
        return
    try:
        with zipfile.ZipFile(path) as archive:
            bad = archive.testzip()
            if bad:
                audit.error("corrupt-pptx", "PPTX contains a corrupt ZIP entry.", entry=bad)
            xml_parts = [
                name for name in archive.namelist() if name.endswith(".xml") or name.endswith(".rels")
            ]
            for name in xml_parts:
                etree.fromstring(archive.read(name))
            for name in archive.namelist():
                if name.startswith("ppt/media/") and not name.endswith("/") and not archive.read(name):
                    audit.error("empty-media", "PPTX contains an empty media file.", entry=name)
            scan_forbidden(
                pptx_text(archive),
                policy.get("forbidden_visible_phrases", []),
                audit,
                path.name,
            )
        presentation = Presentation(path)
        actual = len(presentation.slides)
        if expected_slides and actual != expected_slides:
            audit.error(
                "slide-count-mismatch",
                "PPTX slide count does not match deck plan.",
                expected=expected_slides,
                actual=actual,
            )
        ratio = presentation.slide_width / presentation.slide_height
        if not math.isclose(ratio, 16 / 9, rel_tol=0.01):
            audit.warning("unexpected-aspect-ratio", "PPTX is not 16:9.", ratio=ratio)
        audit.info("pptx-valid", "PPTX package, XML, media, and parser checks passed.", slides=actual)
    except Exception as exc:
        audit.error("pptx-parse-failed", "PPTX validation failed.", error=str(exc))


def write_reports(project: Path, audit: Audit, metadata: dict) -> None:
    qa = project / "qa"
    qa.mkdir(parents=True, exist_ok=True)
    payload = {"summary": audit.summary(), "metadata": metadata, "findings": audit.items}
    (qa / "release_audit.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    lines = [
        "# Release Audit",
        "",
        f"- Errors: {payload['summary']['errors']}",
        f"- Warnings: {payload['summary']['warnings']}",
        f"- Release ready: {payload['summary']['release_ready']}",
        "",
    ]
    for item in audit.items:
        context = json.dumps(item["context"], ensure_ascii=False)
        lines.append(f"- **{item['level'].upper()} {item['code']}**: {item['message']} `{context}`")
    lines.append("")
    (qa / "release_audit.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("project", type=Path)
    parser.add_argument("--pptx", type=Path)
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()
    project = args.project.resolve()
    audit = Audit()
    policy = load_json(project / "qa" / "release_policy.json", audit, required=args.strict)
    plan = load_json(project / "deck_plan.json", audit, required=args.strict)
    ledger = load_json(project / "evidence_ledger.json", audit, required=args.strict)
    catalog = load_json(project / "analysis" / "source_catalog.json", audit, required=args.strict)
    audit_ledger(ledger, catalog, args.strict, audit)
    source_text = "\n".join(item.get("text", "") for item in catalog.get("entries", []))
    source_numbers = collect_numbers(source_text)
    pages = audit_plan(project, plan, ledger, policy, args.strict, audit)
    svg_count = audit_svgs(project, pages, policy, source_numbers, args.strict, audit)
    if args.pptx:
        audit_pptx(args.pptx.resolve(), len(pages) or svg_count, policy, audit)
    metadata = {
        "project": display_path(project),
        "strict": args.strict,
        "planned_slides": len(pages),
        "svg_slides": svg_count,
        "pptx": display_path(args.pptx) if args.pptx else None,
    }
    write_reports(project, audit, metadata)
    print(json.dumps({"summary": audit.summary(), **metadata}, ensure_ascii=False))
    sys.exit(1 if audit.summary()["errors"] else 0)


if __name__ == "__main__":
    main()
