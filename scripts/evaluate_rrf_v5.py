#!/usr/bin/env python3
"""Evaluate RRF fusion of multiple BM25 weight profiles on v5-dense."""
import argparse
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import section_search

PROFILES = {
    "default": "5,2,0.5",
    "title": "10,1,0.2",
    "heading": "2,10,0.2",
    "body": "1,1,5",
}


def run(root, query, profile):
    os.environ["TYCHO_BM25_WEIGHTS"] = PROFILES[profile]
    return section_search.search(root, query, limit=20, abstain=False)


def fuse(rankings, names, k=60):
    scores = {}
    for name in names:
        for rank, row in enumerate(rankings[name].get("results", []), 1):
            key = row["section_key"]
            scores[key] = scores.get(key, 0.0) + 1.0 / (k + rank)
    return sorted(scores, key=lambda key: (-scores[key], key))[:5]


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
    combos = {
        "default": ("default",),
        "title+body": ("title", "body"),
        "default+title+body": ("default", "title", "body"),
        "all": ("default", "title", "heading", "body"),
        "title+heading+body": ("title", "heading", "body"),
    }
    counts = {name: {"page": [0, 0, 0], "section": [0, 0, 0]}
              for name in combos}
    paths = {}
    for item in page["items"]:
        rankings = {name: run(args.root, item["question"], name)
                    for name in PROFILES}
        path_by_key = {row["section_key"]: row["path"]
                       for name in rankings
                       for row in rankings[name].get("results", [])}
        for name, names in combos.items():
            keys = fuse(rankings, names)
            page_keys = [path_by_key[key] for key in keys]
            for index, k in enumerate((1, 3, 5)):
                counts[name]["page"][index] += int(
                    bool(set(page_keys[:k]) & set(item["accepted"])))
                counts[name]["section"][index] += int(
                    bool(set(keys[:k]) & set(sections[item["id"]]["accepted"])))
    n = len(page["items"])
    output = {name: {level: [round(value / n, 3) for value in values]
                     for level, values in levels.items()}
              for name, levels in counts.items()}
    print(json.dumps(output, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
