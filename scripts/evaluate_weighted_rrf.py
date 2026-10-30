#!/usr/bin/env python3
"""Evaluate weighted RRF between default and 3/2/1 BM25 profiles."""
import argparse
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import section_search

WEIGHTS = {"default": "5,2,0.5", "321": "3,2,1"}
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


def run(root, query, profile):
    os.environ["TYCHO_BM25_WEIGHTS"] = WEIGHTS[profile]
    return section_search.search(root, query, limit=20, abstain=False)


def fuse(default_run, alt_run, weight):
    scores = {}
    for rank, row in enumerate(default_run.get("results", []), 1):
        key = row["section_key"]
        scores[key] = scores.get(key, 0.0) + weight / (60 + rank)
    for rank, row in enumerate(alt_run.get("results", []), 1):
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
        counts = {"default": {"page": [0, 0, 0], "section": [0, 0, 0]}}
        for weight in (2, 3, 4, 6):
            counts["w%d" % weight] = {
                "page": [0, 0, 0], "section": [0, 0, 0]}
        for item in page["items"]:
            default_run = run(args.root, item["question"], "default")
            alt_run = run(args.root, item["question"], "321")
            path_by_key = {row["section_key"]: row["path"]
                           for run in (default_run, alt_run)
                           for row in run.get("results", [])}
            for name, keys in (
                    ("default", [row["section_key"]
                                 for row in default_run.get("results", [])][:5]),
                    *[("w%d" % weight,
                       fuse(default_run, alt_run, weight))
                      for weight in (2, 3, 4, 6)]):
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
