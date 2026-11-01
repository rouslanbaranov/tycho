#!/usr/bin/env python3
"""Render observed per-entry promotion time as horizontal bars."""
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "authoring/promotion-entry-timing-2026-10-29.json"
OUT = ROOT / "authoring/promotion-entry-timing-2026-11-01.svg"
LATEST_OUT = ROOT / "authoring/promotion-entry-timing-latest.svg"


def render(entries, out, title, row=22, width=1500):
    left, top, right, bottom = 300, 70, 90, 70
    height = top + len(entries) * row + bottom
    plot_w = width - left - right
    max_v = 10 * ((max(e["minutes"] for e in entries) + 9) // 10)
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="white"/>',
        f'<text x="24" y="28" font-family="Verdana" font-size="17" fill="#141414">'
        f'{html.escape(title)}</text>',
        f'<text x="24" y="48" font-family="Verdana" font-size="11" fill="#606060">'
        f'Newest first; bars are minutes; x-axis is minutes</text>',
    ]
    for tick in range(0, max_v + 1, max(10, max_v // 8)):
        x = left + plot_w * tick / max_v
        parts.append(f'<line x1="{x:.1f}" y1="{top-10}" x2="{x:.1f}" '
                     f'y2="{top + len(entries)*row}" stroke="#e1e1e1"/>')
        parts.append(f'<text x="{x:.1f}" y="{top + len(entries)*row + 22}" '
                     f'text-anchor="middle" font-family="Verdana" font-size="11" '
                     f'fill="#505050">{tick}</text>')
    for i, item in enumerate(entries):
        y = top + i * row
        value = item["minutes"]
        bar_w = plot_w * value / max_v if max_v else 0
        parts.append(f'<rect x="{left}" y="{y}" width="{bar_w:.1f}" height="{row-4}" '
                     f'fill="#1e5ab4" opacity="0.85"/>')
        parts.append(f'<text x="{left-8}" y="{y+row-9}" text-anchor="end" '
                     f'font-family="Verdana" font-size="10" fill="#323232">'
                     f'{html.escape(item["label"])}</text>')
        parts.append(f'<text x="{left+bar_w+6:.1f}" y="{y+row-9}" '
                     f'font-family="Verdana" font-size="10" fill="#323232">{value}</text>')
    parts.append(f'<text x="{left}" y="{height-18}" text-anchor="middle" '
                 f'font-family="Verdana" font-size="11" fill="#505050">minutes</text>')
    parts.append('</svg>')
    out.write_text("\n".join(parts), encoding="utf-8")
    print(out)


def main():
    entries = json.loads(SRC.read_text(encoding="utf-8"))["entries"]
    render(entries[::-1], OUT, f"Promotion time — all {len(entries)} entries")
    render(entries[-15:][::-1], LATEST_OUT, "Promotion time — latest 15 entries")


if __name__ == "__main__":
    main()
