#!/usr/bin/env python3
"""Render observed per-entry promotion time and a single-entry forecast band."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "authoring/promotion-entry-timing-2026-10-29.json"
OUT = ROOT / "authoring/promotion-entry-timing-2026-10-29.svg"
LATEST_OUT = ROOT / "authoring/promotion-entry-timing-latest.svg"


def main():
    data = json.loads(SRC.read_text(encoding="utf-8"))
    entries = data["entries"]
    observed = [e["minutes"] for e in entries]
    post = observed
    mean = sum(post) / len(post)
    lo, hi = min(post), max(post)
    forecast_slots = 4
    total_slots = len(entries) + forecast_slots
    width = 1900
    height = 820
    left, top, right, bottom = 80, 90, 60, 250
    plot_w = width - left - right
    plot_h = height - top - bottom
    max_v = 10 * ((max(observed + [hi]) + 9) // 10)
    slot = plot_w / total_slots
    bar_w = slot * 0.55
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
             '<rect width="100%" height="100%" fill="white"/>']
    for v in range(0, max_v + 1, max(10, max_v // 6)):
        y = top + plot_h - plot_h * v / max_v
        parts.append(f'<line x1="{left}" y1="{y:.1f}" x2="{left+plot_w}" y2="{y:.1f}" stroke="#e1e1e1"/>')
        parts.append(f'<text x="{left-32}" y="{y+5:.1f}" font-family="Verdana" font-size="12" fill="#505050">{v}</text>')
    parts.append(f'<line x1="{left}" y1="{top}" x2="{left}" y2="{top+plot_h}" stroke="#3c3c3c"/>')
    parts.append(f'<line x1="{left}" y1="{top+plot_h}" x2="{left+plot_w}" y2="{top+plot_h}" stroke="#3c3c3c"/>')
    # forecast band and mean line over the next slots
    fx0 = left + slot * len(entries)
    fx1 = left + plot_w
    fy_hi = top + plot_h - plot_h * hi / max_v
    fy_lo = top + plot_h - plot_h * lo / max_v
    fy_mean = top + plot_h - plot_h * mean / max_v
    parts.append(f'<rect x="{fx0:.1f}" y="{fy_hi:.1f}" width="{fx1-fx0:.1f}" height="{fy_lo-fy_hi:.1f}" fill="#1e5ab4" opacity="0.10"/>')
    parts.append(f'<line x1="{fx0:.1f}" y1="{fy_mean:.1f}" x2="{fx1:.1f}" y2="{fy_mean:.1f}" stroke="#1e5ab4" stroke-width="2" stroke-dasharray="6 4"/>')
    parts.append(f'<text x="{fx0+8:.1f}" y="{fy_mean-8:.1f}" font-family="Verdana" font-size="10" fill="#1e5ab4">forecast {mean:.0f} min; range {lo}-{hi} (n={len(observed)})</text>')
    for i, item in enumerate(entries):
        value = item["minutes"]
        x = left + slot * i + (slot - bar_w) / 2
        y = top + plot_h - plot_h * value / max_v
        color = "#c85a1e" if i == 0 else "#1e5ab4"
        parts.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{bar_w:.1f}" height="{top+plot_h-y:.1f}" fill="{color}" opacity="0.85"/>')
        parts.append(f'<text x="{x+bar_w/2:.1f}" y="{y-6:.1f}" text-anchor="middle" font-family="Verdana" font-size="11" fill="#323232">{value}</text>')
        lx = x + bar_w / 2
        ly = top + plot_h + 16
        parts.append(f'<text x="{lx:.1f}" y="{ly:.1f}" text-anchor="end" transform="rotate(-45 {lx:.1f} {ly:.1f})" font-family="Verdana" font-size="10" fill="#323232">{item["label"]}</text>')
    latest = entries[-5:]
    lx0 = width - 430
    parts.append(f'<text x="{lx0}" y="24" font-family="Verdana" font-size="13" fill="#141414">Latest promotions</text>')
    for j, item in enumerate(reversed(latest)):
        parts.append(f'<text x="{lx0}" y="{44 + j*17}" font-family="Verdana" font-size="11" fill="#323232">{item["label"]}: {item["minutes"]} min</text>')
    parts.append(f'<text x="{left}" y="25" font-family="Verdana" font-size="16" fill="#141414">Single-entry promotion time and forecast</text>')
    parts.append(f'<text x="{left}" y="44" font-family="Verdana" font-size="11" fill="#606060">orange: pre-optimization; blue bars: observed; dashed band: next-entry range</text>')
    parts.append('</svg>')
    OUT.write_text("\n".join(parts), encoding="utf-8")
    print(OUT)




def render_latest(entries):
    subset = entries[-15:]
    width, height = 1500, 620
    left, top, right, bottom = 80, 70, 40, 230
    plot_w = width - left - right
    plot_h = height - top - bottom
    max_v = 10 * ((max(e["minutes"] for e in subset) + 9) // 10)
    slot = plot_w / len(subset)
    bar_w = slot * 0.55
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
             '<rect width="100%" height="100%" fill="white"/>']
    for v in range(0, max_v + 1, max(10, max_v // 6)):
        y = top + plot_h - plot_h * v / max_v
        parts.append(f'<line x1="{left}" y1="{y:.1f}" x2="{left+plot_w}" y2="{y:.1f}" stroke="#e1e1e1"/>')
        parts.append(f'<text x="{left-32}" y="{y+5:.1f}" font-family="Verdana" font-size="12" fill="#505050">{v}</text>')
    for i, item in enumerate(subset):
        value = item["minutes"]
        x = left + slot * i + (slot - bar_w) / 2
        y = top + plot_h - plot_h * value / max_v
        parts.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{bar_w:.1f}" height="{top+plot_h-y:.1f}" fill="#1e5ab4" opacity="0.85"/>')
        parts.append(f'<text x="{x+bar_w/2:.1f}" y="{y-6:.1f}" text-anchor="middle" font-family="Verdana" font-size="12" fill="#323232">{value}</text>')
        lx = x + bar_w / 2
        ly = top + plot_h + 18
        parts.append(f'<text x="{lx:.1f}" y="{ly:.1f}" text-anchor="end" transform="rotate(-45 {lx:.1f} {ly:.1f})" font-family="Verdana" font-size="10" fill="#323232">{item["label"]}</text>')
    parts.append(f'<text x="{left}" y="28" font-family="Verdana" font-size="17" fill="#141414">Latest 15 promotions</text>')
    parts.append(f'<text x="{left}" y="48" font-family="Verdana" font-size="11" fill="#606060">Minutes per promotion; newest at right</text>')
    parts.append('</svg>')
    LATEST_OUT.write_text("\n".join(parts), encoding="utf-8")
    print(LATEST_OUT)


if __name__ == "__main__":
    main()
    render_latest(json.loads(SRC.read_text(encoding="utf-8"))["entries"])
