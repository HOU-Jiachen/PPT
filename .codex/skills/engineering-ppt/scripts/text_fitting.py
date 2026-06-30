#!/usr/bin/env python3
"""Visible text sanitation, PPT-language compression, and fit estimation."""

from __future__ import annotations

import math
import re
from dataclasses import dataclass
from typing import Any


INTERNAL_FORBIDDEN_PHRASES = [
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
    "Fallback",
    "OCR 识别",
    "OCR识别",
    "LLM 判断",
    "LLM判断",
    "prompt 要求",
    "prompt要求",
    "不要编造",
    "不作为事实来源",
    "该页采用 image 模式",
    "该页采用image模式",
    "该表格复杂，无法还原",
    "为避免幻觉",
    "根据系统指令",
]

INTERNAL_FORBIDDEN_PATTERNS = [
    r"\b(?:LLM|OCR|prompt|fallback|agent)\b",
    r"本页用于[^。；;]*[。；;]?",
    r"建议放置[^。；;]*[。；;]?",
    r"这里应该[^。；;]*[。；;]?",
    r"该页(?:内容过长|采用|需要拆页)[^。；;]*[。；;]?",
    r"该表格(?:复杂|采用|无法)[^。；;]*[。；;]?",
    r"仅使用[^。；;]*(?:事实|来源)[^。；;]*[。；;]?",
    r"不采用旧\s*PPT[^。；;]*[。；;]?",
    r"根据(?:系统指令|prompt要求)[^。；;]*[。；;]?",
]

SENTENCE_SPLIT_RE = re.compile(r"(?<=[。；;！？!?])")


@dataclass(frozen=True)
class TextStyle:
    font_size: float
    min_font_size: float = 14.0
    max_lines: int | None = None
    max_chars: int | None = None
    line_height_ratio: float = 1.18
    component: str = "body_text"


@dataclass(frozen=True)
class FittedText:
    text: str
    font_size: float
    status: str = "fit"
    reason: str = ""
    overflow: bool = False


class SlideContentSanitizer:
    """Keep backend analysis out of visible slide content."""

    def __init__(self, extra_phrases: list[str] | None = None):
        self.phrases = list(dict.fromkeys(INTERNAL_FORBIDDEN_PHRASES + (extra_phrases or [])))

    def sanitize(self, text: str, *, component: str = "body_text") -> str:
        value = normalize_text(text)
        if not value:
            return ""
        for phrase in self.phrases:
            if phrase:
                value = value.replace(phrase, "")
        for pattern in INTERNAL_FORBIDDEN_PATTERNS:
            value = re.sub(pattern, "", value, flags=re.I)
        value = re.sub(r"\b(?:source_mode|evidence_ids|visual_proof|layout_pattern|render_mode|table_id)\b[:：]?\s*\S*", "", value, flags=re.I)
        value = re.sub(r"(?<![A-Za-z])PPT(?![A-Za-z])\s*[，,。；;]?", "", value)
        value = normalize_text(value)
        value = re.sub(r"^[：:，,；;。]+", "", value).strip(" ，,；;。:：")
        if component in {"body_text", "bullet", "conclusion", "hybrid_conclusion"}:
            value = compress_for_ppt(value, max_chars=component_char_limit(component))
        return value

    def sanitize_slide_record(self, slide: dict[str, Any]) -> dict[str, Any]:
        """Return a slide record whose visible text only comes from slide_content."""

        content = dict(slide.get("slide_content") or {})
        if not content:
            content = {
                "title": slide.get("title", ""),
                "bullets": slide.get("bullets", []),
                "caption": slide.get("caption", ""),
            }
        clean = {
            "title": self.sanitize(str(content.get("title", "")), component="title"),
            "bullets": [
                self.sanitize(str(item), component="bullet")
                for item in content.get("bullets", [])[:5]
                if self.sanitize(str(item), component="bullet")
            ],
            "caption": self.sanitize(str(content.get("caption", "")), component="caption"),
        }
        result = dict(slide)
        result["slide_content"] = clean
        result.setdefault("internal_notes", [])
        result.setdefault("speaker_notes", [])
        return result

    def visible_text_violations(self, text: str) -> list[str]:
        value = normalize_text(text)
        hits = [phrase for phrase in self.phrases if phrase and phrase in value]
        for pattern in INTERNAL_FORBIDDEN_PATTERNS:
            if re.search(pattern, value, flags=re.I):
                hits.append(pattern)
        return list(dict.fromkeys(hits))


class TextFittingEngine:
    """Estimate text fit without violating hard minimum font sizes."""

    def fit_text_to_box(self, text: str, width_in: float, height_in: float, style: TextStyle) -> FittedText:
        sanitizer = SlideContentSanitizer()
        clean = sanitizer.sanitize(text, component=style.component)
        size = float(style.font_size)
        min_size = float(style.min_font_size)
        while size > min_size:
            if not self.overflows(clean, width_in, height_in, size, style):
                return FittedText(clean, size)
            size -= 1
        if not self.overflows(clean, width_in, height_in, min_size, style):
            return FittedText(clean, min_size)

        compressed = compress_for_ppt(clean, max_chars=style.max_chars or component_char_limit(style.component))
        if not self.overflows(compressed, width_in, height_in, min_size, style):
            return FittedText(compressed, min_size, status="compressed", reason="compressed at min_font_size")

        reduced = reduce_bullets_or_sentences(compressed, max_items=5, max_chars=style.max_chars or component_char_limit(style.component))
        if not self.overflows(reduced, width_in, height_in, min_size, style):
            return FittedText(reduced, min_size, status="reduced", reason="reduced content at min_font_size")

        return FittedText(
            reduced,
            min_size,
            status="needs_relayout_or_split",
            reason="Text still overflows at min_font_size",
            overflow=True,
        )

    def overflows(self, text: str, width_in: float, height_in: float, font_size: float, style: TextStyle) -> bool:
        lines = estimate_text_lines(text, width_in, font_size)
        if style.max_lines is not None and lines > style.max_lines:
            return True
        line_height = font_size * style.line_height_ratio
        available_lines = max(1.0, height_in * 72.0 / max(1.0, line_height))
        return lines > available_lines + 0.2


def normalize_text(text: str) -> str:
    value = re.sub(r"\s+", " ", text or "").strip()
    value = re.sub(r"\s*\|\s*", "；", value)
    value = value.replace("……", "").replace("...", "").replace("…", "")
    value = re.sub(r"[，,]{2,}", "，", value)
    value = re.sub(r"[；;]{2,}", "；", value)
    value = re.sub(r"[：:]\s*[。；;，,]+", "：", value)
    return value


def component_char_limit(component: str) -> int:
    return {
        "title": 42,
        "subtitle": 34,
        "body_text": 68,
        "bullet": 42,
        "conclusion": 52,
        "caption": 40,
        "table_note": 36,
        "table_cell": 28,
        "hybrid_conclusion": 38,
    }.get(component, 60)


def visible_units(text: str) -> float:
    total = 0.0
    for char in text or "":
        if char.isspace():
            continue
        total += 0.55 if ord(char) < 128 else 1.0
    return total


def estimate_text_lines(text: str, width_in: float, font_size: float) -> int:
    paragraphs = [part.strip() for part in re.split(r"[\r\n]+", text or "") if part.strip()]
    if not paragraphs:
        return 1
    max_units = max(4.0, width_in * 72.0 / max(font_size * 0.92, 1))
    lines = 0
    for paragraph in paragraphs:
        lines += max(1, math.ceil(visible_units(paragraph) / max_units))
    return lines


def split_sentences(text: str) -> list[str]:
    parts = [item.strip(" ，,；;。") for item in SENTENCE_SPLIT_RE.split(text or "") if item.strip(" ，,；;。")]
    if len(parts) <= 1:
        parts = [item.strip(" ，,；;。") for item in re.split(r"[；;]", text or "") if item.strip(" ，,；;。")]
    return parts


def compress_for_ppt(text: str, max_chars: int = 68) -> str:
    value = normalize_text(text)
    if len(value) <= max_chars:
        return ensure_sentence(value)
    sentences = split_sentences(value)
    if sentences:
        value = sentences[0]
    replacements = [
        (r"根据(?:本次|此次)?(?:调查|评价|分析|勘察|核查)结果[，,]?", ""),
        (r"因此(?:本项目|该项目)?", ""),
        (r"且", "，"),
        (r"具有", "有"),
        (r"无明显", "无"),
        (r"范围内", "内"),
        (r"影响较小", "影响小"),
        (r"能够得到有效控制", "可控"),
        (r"符合.*?要求", "符合要求"),
    ]
    for pattern, repl in replacements:
        value = re.sub(pattern, repl, value)
    value = normalize_text(value)
    if len(value) > max_chars:
        boundary = max(value[:max_chars].rfind(mark) for mark in ("，", "、", "；", ";", " "))
        if boundary >= max_chars * 0.5:
            value = value[:boundary]
        else:
            value = value[:max_chars]
    return ensure_sentence(value.strip(" ，,；;。"))


def reduce_bullets_or_sentences(text: str, max_items: int = 5, max_chars: int = 68) -> str:
    parts = [part for part in re.split(r"(?:\n|(?<=。)|(?<=；)|(?<=;))", text or "") if part.strip()]
    if len(parts) > 1:
        kept = [compress_for_ppt(part, max_chars=max_chars) for part in parts[:max_items]]
        return "\n".join(item for item in kept if item)
    return compress_for_ppt(text, max_chars=max_chars)


def ensure_sentence(text: str) -> str:
    value = (text or "").strip(" ，,；;。")
    if value and value[-1] not in "。；;！!？?：:）】》”’0123456789%":
        value += "。"
    return value


def final_text_review_payload(slides: list[dict[str, Any]]) -> dict[str, Any]:
    sanitizer = SlideContentSanitizer()
    findings = []
    for index, slide in enumerate(slides, start=1):
        visible_parts = []
        content = slide.get("slide_content") or {}
        if isinstance(content, dict):
            visible_parts.append(str(content.get("title", "")))
            visible_parts.extend(str(item) for item in content.get("bullets", []) or [])
            visible_parts.append(str(content.get("caption", "")))
        text = "\n".join(visible_parts)
        violations = sanitizer.visible_text_violations(text)
        if violations:
            findings.append({"page": index, "code": "internal-visible-text", "matches": violations})
        long_items = [item for item in visible_parts if len(normalize_text(item)) > 90]
        if long_items:
            findings.append({"page": index, "code": "long-report-style-text", "items": long_items[:3]})
    return {"findings": findings, "passed": not findings}
