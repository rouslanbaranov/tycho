#!/usr/bin/env python3
"""Render the promotion timing trend chart from the timing JSON."""
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "authoring/promotion-timing.v1.json"
SVG = ROOT / "authoring/promotion-timing-2026-10-29.svg"
COLORS = {
    "single_entry_cycle": "#1e5ab4",
    "clean_cycle": "#1e9650",
    "remediation_cycle": "#c85a1e",
}


def main():
    data = json.loads(SRC.read_text(encoding="utf-8"))
    labels = data["labels"]
    series = data["series"]
    width, height = 900, 480
    left, top, right, bottom = 90, 60, 40, 80
    plot_w = width - left - right
    plot_h = height - top - bottom
    max_v = 60
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}">',
             '<rect width="100%" height="100%" fill="white"/>']
    for v in range(0, max_v + 1, 10):
        y = top + plot_h - plot_h * v / max_v
        parts.append(f'<line x1="{left}" y1="{y:.1f}" x2="{left+plot_w}" y2="{y:.1f}" stroke="#e1e1e1"/>')
        parts.append(f'<text x="{left-30}" y="{y+5:.1f}" font-family="Verdana" font-size="12" fill="#505050">{v}</text>')
    parts.append(f'<line x1="{left}" y1="{top}" x2="{left}" y2="{top+plot_h}" stroke="#3c3c3c"/>')
    parts.append(f'<line x1="{left}" y1="{top+plot_h}" x2="{left+plot_w}" y2="{top+plot_h}" stroke="#3c3c3c"/>')
    n = len(labels)
    for key, values in series.items():
        color = COLORS.get(key, "#646464")
        pts = []
        for i, value in enumerate(values):
            x = left + plot_w * i / max(1, n - 1)
            y = top + plot_h - plot_h * value / max_v
            pts.append((x, y))
        path = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
        parts.append(f'<polyline points="{path}" fill="none" stroke="{color}" stroke-width="3"/>')
        for x, y in pts:
            parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="{color}"/>')
    for i, label in enumerate(labels):
        x = left + plot_w * i / max(1, n - 1)
        x = min(x, left + plot_w - 40)
        parts.append(f'<text x="{x:.1f}" text-anchor="middle" y="{top+plot_h+24}" font-family="Verdana" font-size="13" fill="#323232">{label}</text>')
    parts.append(f'<text x="{left}" y="25" font-family="Verdana" font-size="16" fill="#141414">Promotion timing trend (minutes, rolling estimate)</text>')
    legend_y = 45
    for key, color in COLORS.items():
        parts.append(f'<line x1="{left+420}" y1="{legend_y}" x2="{left+450}" y2="{legend_y}" stroke="{color}" stroke-width="3"/>')
        parts.append(f'<text x="{left+458}" y="{legend_y+4}" font-family="Verdana" font-size="12" fill="#323232">{key.replace("_", " ")}</text>')
        legend_y += 18
    parts.append('</svg>')
    SVG.write_text("\n".join(parts), encoding="utf-8")
    print(SVG)


if __name__ == "__main__":
    main()
