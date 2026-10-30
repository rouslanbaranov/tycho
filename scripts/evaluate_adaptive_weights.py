#!/usr/bin/env python3
"""Evaluate an unsupervised default-vs-321 weight selector."""
import argparse
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import section_search

PROFILES = {"default": "5,2,0.5", "321": "3,2,1"}
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
    os.environ["TYCHO_BM25_WEIGHTS"] = PROFILES[profile]
    return section_search.search(root, query, limit=5, abstain=False)


def score_stats(payload):
    rows = payload.get("results", [])
    scores = [float(row.get("score", 0.0)) for row in rows]
    if not scores:
        return 0.0, 0.0
    top = scores[0]
    second = scores[1] if len(scores) > 1 else top
    margin = (abs(top - second) / abs(top) if top else 0.0)
    return top, margin


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
                  for name in ("default", "321", "max_score", "min_margin")}
        for item in page["items"]:
            runs = {profile: run(args.root, item["question"], profile)
                    for profile in PROFILES}
            stats = {profile: score_stats(payload)
                     for profile, payload in runs.items()}
            choices = {
                "default": runs["default"],
                "321": runs["321"],
                "max_score": runs[max(stats, key=lambda p: stats[p][0])],
                "min_margin": runs[min(stats, key=lambda p: stats[p][1])],
            }
            for name, payload in choices.items():
                rows = payload.get("results", [])
                paths = [row["path"] for row in rows]
                keys = [row["section_key"] for row in rows]
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
