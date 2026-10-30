#!/usr/bin/env python3
"""Evaluate RRF BM25 fusion across qrels versions."""
import argparse
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import section_search

PROFILES = {"default": "5,2,0.5", "title": "10,1,0.2",
            "body": "1,1,5", "321": "3,2,1"}
DATASETS = {
    "v4": ("evaluation/corpus-qrels.v4.json",
           "evaluation/section-qrels.v4.json"),
    "v4.1": ("evaluation/corpus-qrels.v4.1.json",
             "evaluation/section-qrels.v4.1.json"),
    "v5": ("evaluation/corpus-qrels.v5-dense.json",
           "evaluation/section-qrels.v5-dense.json"),
    "v3": ("evaluation/corpus-qrels.v3.json",
           "evaluation/section-qrels.v3.json"),
}
COMBOS = {"default": ("default",), "default+title+body":
          ("default", "title", "body"), "title+body": ("title", "body"),
          "default+321": ("default", "321")}


def search(root, query, profile):
    os.environ["TYCHO_BM25_WEIGHTS"] = PROFILES[profile]
    return section_search.search(root, query, limit=20, abstain=False)


def fuse(rankings, names):
    scores = {}
    for name in names:
        for rank, row in enumerate(rankings[name].get("results", []), 1):
            key = row["section_key"]
            scores[key] = scores.get(key, 0.0) + 1.0 / (60 + rank)
    return sorted(scores, key=lambda key: (-scores[key], key))[:5]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=ROOT)
    args = ap.parse_args(argv)
    output = {}
    for dataset, (page_name, section_name) in DATASETS.items():
        page_path = args.root / page_name
        section_path = args.root / section_name
        if not page_path.is_file() or not section_path.is_file():
            continue
        page = json.loads(page_path.read_text(encoding="utf-8"))
        section = json.loads(section_path.read_text(encoding="utf-8"))
        sections = {item["id"]: item for item in section["items"]}
        counts = {name: {"page": [0, 0, 0], "section": [0, 0, 0]}
                  for name in COMBOS}
        for item in page["items"]:
            rankings = {profile: search(args.root, item["question"], profile)
                        for profile in PROFILES}
            path_by_key = {row["section_key"]: row["path"]
                           for profile in rankings
                           for row in rankings[profile].get("results", [])}
            for name, names in COMBOS.items():
                keys = fuse(rankings, names)
                paths = [path_by_key[key] for key in keys]
                for index, k in enumerate((1, 3, 5)):
                    counts[name]["page"][index] += int(
                        bool(set(paths[:k]) & set(item["accepted"])))
                    counts[name]["section"][index] += int(
                        bool(set(keys[:k]) &
                             set(sections[item["id"]]["accepted"])))
        n = len(page["items"])
        output[dataset] = {name: {level: [round(value / n, 3)
                                          for value in values]
                                  for level, values in levels.items()}
                           for name, levels in counts.items()}
    print(json.dumps(output, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
