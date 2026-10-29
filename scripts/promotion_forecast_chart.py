#!/usr/bin/env python3
"""Render cumulative single-entry promotion forecast as SVG."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "authoring/promotion-forecast-2026-10-29.json"
OUT = ROOT / "authoring/promotion-forecast-2026-10-29.svg"
COLORS = {"optimistic": "#1e9650", "base": "#1e5ab4", "pessimistic": "#c85a1e"}


def main():
    data = json.loads(SRC.read_text(encoding="utf-8"))
    tiers = data["tiers"]
    total = data["remaining_entries"]
    # order by easiest first; cumulative minutes at each point
    order = ["4/4", "3/4", "2/4", "1/4", "0/4"]
    width, height = 1000, 480
    left, top, right, bottom = 90, 60, 40, 80
    plot_w = width - left - right
    plot_h = height - top - bottom
    max_days = 18
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}">',
             '<rect width="100%" height="100%" fill="white"/>']
    for d in range(0, max_days + 1, 3):
        y = top + plot_h - plot_h * d / max_days
        parts.append(f'<line x1="{left}" y1="{y:.1f}" x2="{left+plot_w}" y2="{y:.1f}" stroke="#e1e1e1"/>')
        parts.append(f'<text x="{left-30}" y="{y+5:.1f}" font-family="Verdana" font-size="12" fill="#505050">{d}</text>')
    for xv in (0, 30, 60, 90, total):
        x = left + plot_w * xv / total
        parts.append(f'<line x1="{x:.1f}" y1="{top}" x2="{x:.1f}" y2="{top+plot_h}" stroke="#f0f0f0"/>')
        parts.append(f'<text x="{x:.1f}" y="{top+plot_h+20}" text-anchor="middle" font-family="Verdana" font-size="11" fill="#505050">{xv}</text>')
    parts.append(f'<line x1="{left}" y1="{top}" x2="{left}" y2="{top+plot_h}" stroke="#3c3c3c"/>')
    parts.append(f'<line x1="{left}" y1="{top+plot_h}" x2="{left+plot_w}" y2="{top+plot_h}" stroke="#3c3c3c"/>')
    for name, per in data["scenarios"].items():
        color = COLORS[name]
        pts = [(0, 0)]
        done = 0
        minutes = 0
        for tier in order:
            for _ in range(tiers[tier]):
                done += 1
                minutes += per[tier]
                pts.append((done, minutes / 60 / 24))
        path = " ".join(f"{left+plot_w*x/total:.1f},{top+plot_h-plot_h*y/max_days:.1f}" for x, y in pts)
        parts.append(f'<polyline points="{path}" fill="none" stroke="{color}" stroke-width="3"/>')
        end_y = pts[-1][1]
        legend_y = 118 + 18 * len([n for n in COLORS if n != name and list(COLORS).index(n) < list(COLORS).index(name)])
        parts.append(f'<line x1="{left+420}" y1="{legend_y}" x2="{left+450}" y2="{legend_y}" stroke="{color}" stroke-width="3"/>')
        parts.append(f'<text x="{left+458}" y="{legend_y+4}" font-family="Verdana" font-size="11" fill="#323232">{name}: {end_y:.1f} days</text>')
    parts.append(f'<text x="{left}" y="25" font-family="Verdana" font-size="16" fill="#141414">Cumulative time to promote the remaining 118 entries</text>')
    parts.append(f'<text x="{left}" y="44" font-family="Verdana" font-size="11" fill="#606060">continuous days; tiers ordered easiest first; base = 90 min for 2/4 gaps</text>')
    parts.append(f'<text x="{left+plot_w/2:.1f}" y="{top+plot_h+48}" text-anchor="middle" font-family="Verdana" font-size="11" fill="#505050">entries promoted from now</text>')
    parts.append('</svg>')
    OUT.write_text("\n".join(parts), encoding="utf-8")
    print(OUT)


if __name__ == "__main__":
    main()
