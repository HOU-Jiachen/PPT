#!/usr/bin/env python3
"""Choose cleaner figure panel layouts from image dimensions."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from PIL import Image


def image_ratio(path: Path) -> float:
    with Image.open(path) as image:
        width, height = image.size
    return width / max(1, height)


def choose_figure_layout(paths: list[Path], available_w: float, available_h: float) -> dict[str, Any]:
    """Return an unframed grid plan that preserves image proportions."""

    count = len(paths)
    if count <= 0:
        raise ValueError("No figure paths supplied")
    ratios = []
    for path in paths:
        try:
            ratios.append(image_ratio(path))
        except Exception:
            ratios.append(1.0)

    average = sum(ratios) / len(ratios)
    if count == 1:
        return {"cols": 1, "rows": 1, "gap": 0.0, "mode": "single"}
    if count == 2:
        if average > 1.9:
            return {"cols": 1, "rows": 2, "gap": 0.12, "mode": "stacked-wide"}
        return {"cols": 2, "rows": 1, "gap": 0.14, "mode": "paired"}
    if count == 3:
        if average > 2.1 or available_w / max(available_h, 0.1) < 2.0:
            return {"cols": 1, "rows": 3, "gap": 0.10, "mode": "stacked-three"}
        return {"cols": 3, "rows": 1, "gap": 0.12, "mode": "triptych"}
    return {"cols": 2, "rows": 2, "gap": 0.12, "mode": "quad"}
