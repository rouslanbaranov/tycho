#!/usr/bin/env python3
"""Evaluate query-conditioned best/semantic routing on v5-dense."""
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import best_search
import section_search


def metrics(rows, page_item, section_item):
    paths = [row["path"] for row in rows]
    keys = [row["section_key"] for row in rows]
    return [[int(bool(set(paths[:k]) & set(page_item["accepted"])))
             for k in (1, 3, 5)],
            [int(bool(set(keys[:k]) & set(section_item["accepted"])))
             for k in (1, 3, 5)]]


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
    thresholds = (0.02, 0.05, 0.10, 0.20, 0.35)
    counts = {"base": {"page": [0, 0, 0], "section": [0, 0, 0]}}
    for threshold in thresholds:
        counts["gate%.2f" % threshold] = {
            "page": [0, 0, 0], "section": [0, 0, 0]}
    for item in page["items"]:
        base = section_search.search(
            args.root, item["question"], limit=5, abstain=False)
        base_rows = base.get("results", [])
        best = best_search.best_search(
            args.root, item["question"], limit=5)
        best_rows = best.get("results", [])
        section_item = sections[item["id"]]
        for name, rows in (("base", base_rows),):
            page_hits, section_hits = metrics(rows, item, section_item)
            for index in range(3):
                counts[name]["page"][index] += page_hits[index]
                counts[name]["section"][index] += section_hits[index]
        scores = [float(row.get("score", 0.0)) for row in base_rows]
        margin = ((scores[0] - scores[1]) / scores[0]
                  if len(scores) > 1 and scores[0] else 1.0)
        for threshold in thresholds:
            rows = best_rows if margin < threshold else base_rows
            page_hits, section_hits = metrics(rows, item, section_item)
            name = "gate%.2f" % threshold
            for index in range(3):
                counts[name]["page"][index] += page_hits[index]
                counts[name]["section"][index] += section_hits[index]
    n = len(page["items"])
    output = {name: {level: [round(value / n, 3) for value in values]
                     for level, values in levels.items()}
              for name, levels in counts.items()}
    print(json.dumps(output, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
