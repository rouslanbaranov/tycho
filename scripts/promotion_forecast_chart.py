#!/usr/bin/env python3
"""Render cumulative promotion forecast as horizontal scenario bars."""
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "authoring/promotion-forecast-2026-10-30.json"
OUT = ROOT / "authoring/promotion-forecast-2026-11-01.svg"
COLORS = {"optimistic": "#1e9650", "base": "#1e5ab4", "pessimistic": "#c85a1e"}
ORDER = ["4/4", "3/4", "2/4", "1/4", "0/4"]


def main():
    data = json.loads(SRC.read_text(encoding="utf-8"))
    tiers = data["tiers"]
    remaining = data["remaining_entries"]
    days = {}
    for name, per in data["scenarios"].items():
        minutes = sum(tiers[tier] * per[tier] for tier in ORDER)
        days[name] = minutes / 60 / 8
    width, height = 1000, 420
    left, top, right, bottom = 220, 70, 100, 80
    plot_w = width - left - right
    row = 70
    max_days = 8
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="white"/>',
        f'<text x="24" y="30" font-family="Verdana" font-size="17" fill="#141414">'
        f'Promotion forecast — {remaining} remaining entries</text>',
        f'<text x="24" y="50" font-family="Verdana" font-size="11" fill="#606060">'
        f'Cumulative continuous 8-hour days; x-axis is days</text>',
    ]
    for tick in range(0, max_days + 1, 1):
        x = left + plot_w * tick / max_days
        parts.append(f'<line x1="{x:.1f}" y1="{top-10}" x2="{x:.1f}" '
                     f'y2="{top + 3*row}" stroke="#e1e1e1"/>')
        parts.append(f'<text x="{x:.1f}" y="{top + 3*row + 22}" text-anchor="middle" '
                     f'font-family="Verdana" font-size="11" fill="#505050">{tick}</text>')
    for i, name in enumerate(("optimistic", "base", "pessimistic")):
        y = top + i * row
        value = days[name]
        bar_w = plot_w * value / max_days
        parts.append(f'<rect x="{left}" y="{y}" width="{bar_w:.1f}" height="{row-14}" '
                     f'fill="{COLORS[name]}" opacity="0.85"/>')
        parts.append(f'<text x="{left-10}" y="{y+row-22}" text-anchor="end" '
                     f'font-family="Verdana" font-size="13" fill="#323232">{name}</text>')
        parts.append(f'<text x="{left+bar_w+8:.1f}" y="{y+row-22}" '
                     f'font-family="Verdana" font-size="12" fill="#323232">{value:.1f} days</text>')
    parts.append(f'<text x="{left}" y="{height-18}" text-anchor="middle" '
                 f'font-family="Verdana" font-size="11" fill="#505050">days</text>')
    parts.append('</svg>')
    OUT.write_text("\n".join(parts), encoding="utf-8")
    print(OUT)


if __name__ == "__main__":
    main()
