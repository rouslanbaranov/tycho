#!/usr/bin/env python3
"""Evaluate atlas-layer routing by BM25 score ratio."""
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import section_search


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=ROOT)
    args = ap.parse_args(argv)
    page = json.loads(
        (args.root / "evaluation/corpus-qrels.v5-dense.json").read_text(
            encoding="utf-8"))
    section = json.loads(
        (args.root / "evaluation/section-qrels.v5-dense.json").read_text(
            encoding="utf-8"))
    sections = {item["id"]: item for item in section["items"]}
    ratios = (0.2, 0.3, 0.4, 0.5, 0.6)
    counts = {"global": {"page": [0, 0, 0], "section": [0, 0, 0]}}
    for ratio in ratios:
        counts["r%.1f" % ratio] = {
            "page": [0, 0, 0], "section": [0, 0, 0]}
    routed = 0
    for item in page["items"]:
        global_run = section_search.search(
            args.root, item["question"], limit=5, abstain=False)
        atlas_run = section_search.search(
            args.root, item["question"], limit=5, abstain=False,
            volume="v11")
        global_rows = global_run.get("results", [])
        atlas_rows = atlas_run.get("results", [])
        gscore = float(global_rows[0]["score"]) if global_rows else 0.0
        ascore = float(atlas_rows[0]["score"]) if atlas_rows else 0.0
        ratio_value = ascore / gscore if gscore else 0.0
        for name, rows in (("global", global_rows),):
            paths = [row["path"] for row in rows]
            keys = [row["section_key"] for row in rows]
            for index, k in enumerate((1, 3, 5)):
                counts[name]["page"][index] += int(
                    bool(set(paths[:k]) & set(item["accepted"])))
                counts[name]["section"][index] += int(
                    bool(set(keys[:k]) &
                         set(sections[item["id"]]["accepted"])))
        for threshold in ratios:
            rows = atlas_rows if ratio_value >= threshold else global_rows
            if ratio_value >= threshold:
                routed += 1
            paths = [row["path"] for row in rows]
            keys = [row["section_key"] for row in rows]
            name = "r%.1f" % threshold
            for index, k in enumerate((1, 3, 5)):
                counts[name]["page"][index] += int(
                    bool(set(paths[:k]) & set(item["accepted"])))
                counts[name]["section"][index] += int(
                    bool(set(keys[:k]) &
                         set(sections[item["id"]]["accepted"])))
    n = len(page["items"])
    output = {name: {level: [round(value / n, 3) for value in values]
                     for level, values in levels.items()}
              for name, levels in counts.items()}
    output["_routed"] = routed
    print(json.dumps(output, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
