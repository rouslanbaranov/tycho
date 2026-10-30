#!/usr/bin/env python3
"""Evaluate finer BM25 body weights on qrels v4 and v3."""
import argparse
import json
import os
from pathlib import Path

import section_search

ROOT = Path(__file__).resolve().parents[1]


def evaluate(root, page_qrels, section_qrels, weights):
    os.environ["TYCHO_BM25_WEIGHTS"] = ",".join(
        f"{value:g}" for value in weights)
    sections = {item["id"]: item for item in section_qrels["items"]}
    counts = {"page": [0, 0, 0], "section": [0, 0, 0]}
    for item in page_qrels["items"]:
        with section_search._QUERY_CACHE_LOCK:
            section_search._QUERY_CACHE.clear()
        result = section_search.search(
            root, item["question"], limit=5, abstain=False,
            section_rerank=False)
        page_keys = [row["path"] for row in result.get("results", [])]
        section_keys = [row["section_key"]
                        for row in result.get("results", [])]
        page_accept = set(item["accepted"])
        section_accept = set(sections[item["id"]]["accepted"])
        for index, k in enumerate((1, 3, 5)):
            counts["page"][index] += int(
                bool(set(page_keys[:k]) & page_accept))
            counts["section"][index] += int(
                bool(set(section_keys[:k]) & section_accept))
    n = len(page_qrels["items"])
    return {level: [round(value / n, 3) for value in values]
            for level, values in counts.items()}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=ROOT)
    args = ap.parse_args(argv)
    datasets = {}
    for name in ("v4", "v3"):
        page_path = args.root / (
            "evaluation/corpus-qrels.v4.json" if name == "v4"
            else "evaluation/corpus-qrels.v3.json")
        section_path = args.root / (
            "evaluation/section-qrels.v4.json" if name == "v4"
            else "evaluation/section-qrels.v3.json")
        datasets[name] = (
            json.loads(page_path.read_text(encoding="utf-8")),
            json.loads(section_path.read_text(encoding="utf-8")))
    grid = [
        (5.0, 2.0, 0.25),
        (5.0, 2.0, 0.5),
        (5.0, 2.0, 0.75),
        (5.0, 2.0, 1.0),
        (5.0, 2.0, 1.25),
        (5.0, 2.0, 1.5),
        (5.0, 2.0, 2.0),
    ]
    output = {}
    for name, (page_qrels, section_qrels) in datasets.items():
        output[name] = {}
        for weights in grid:
            output[name][str(weights)] = evaluate(
                args.root, page_qrels, section_qrels, weights)
    print(json.dumps(output, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
