#!/usr/bin/env python3
"""Evaluate BM25 weight profiles across v5 5-fold holdouts."""
import argparse
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import section_search

PROFILES = {"5,2,.5": "5,2,0.5", "3,2,1": "3,2,1"}
FOLDS = 5


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
    output = {label: {} for label in PROFILES}
    for label, raw in PROFILES.items():
        os.environ["TYCHO_BM25_WEIGHTS"] = raw
        counts = {fold: {"page": [0, 0, 0], "section": [0, 0, 0]}
                  for fold in range(FOLDS)}
        totals = [0] * FOLDS
        for index, item in enumerate(page["items"]):
            fold = index % FOLDS
            totals[fold] += 1
            result = section_search.search(
                args.root, item["question"], limit=5, abstain=False)
            rows = result.get("results", [])
            paths = [row["path"] for row in rows]
            keys = [row["section_key"] for row in rows]
            for hit_index, k in enumerate((1, 3, 5)):
                counts[fold]["page"][hit_index] += int(
                    bool(set(paths[:k]) & set(item["accepted"])))
                counts[fold]["section"][hit_index] += int(
                    bool(set(keys[:k]) &
                         set(sections[item["id"]]["accepted"])))
        output[label] = {
            "folds": {str(fold): {
                level: [round(value / totals[fold], 3) for value in values]
                for level, values in levels.items()}
                for fold, levels in counts.items()},
            "overall": {
                level: [round(sum(counts[fold][level][i]
                                  for fold in range(FOLDS)) / len(page["items"]), 3)
                        for i in range(3)]
                for level in ("page", "section")}}
    print(json.dumps(output, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
