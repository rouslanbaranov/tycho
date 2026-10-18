"""Render the public-source catalogue from its canonical JSON inventory."""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]

def render():
    data = json.loads((ROOT / "sources/register.json").read_text())
    rows = data["sources"]
    out = ["# Curated public sources", "", "Generated from `register.json`; do not edit this catalogue manually.", "", f"Inventory date: {data['updated']}. Entries: {len(rows)}.", "", "Entry-page/abstract inspection is not full reading. Commercial books are bibliography-only. Pending records are not content evidence. Core/supporting is an editorial priority, not a world ranking.", ""]
    for category in dict.fromkeys(s["category"] for s in rows):
        out += ["## " + category.replace("-", " ").title(), "", "| ID / priority | Source | Planned use | Admission / access |", "|---|---|---|---|"]
        for s in rows:
            if s["category"] != category:
                continue
            values = [s["id"] + " / " + s["priority"], f"[{s['title']}]({s['url']}) — {s['publisher']}", s["planned_use"], s["admission"] + " / " + s["access"]]
            out.append("| " + " | ".join(v.replace("|", "\\|").replace("\n", " ") for v in values) + " |")
        out += [""]
    return "\n".join(out)

if __name__ == "__main__":
    target = ROOT / "sources/CATALOG.md"
    content = render()
    if "--check" in sys.argv:
        if not target.exists() or target.read_text() != content:
            raise SystemExit("Source catalogue is stale; run python3 scripts/source_catalog.py")
        print("Source catalogue matches the canonical register")
    else:
        target.write_text(content)
