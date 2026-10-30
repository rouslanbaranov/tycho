#!/usr/bin/env python3
"""Evaluate title/heading weights at body 0.5 on qrels v4/v3."""
import argparse
import json
import os
from pathlib import Path

import section_search

ROOT = Path(__file__).resolve().parents[1]
GRID = [
    (5.0, 2.0, 0.5),
    (8.0, 3.0, 0.5),
    (5.0, 3.0, 0.5),
    (4.0, 2.0, 0.5),
    (6.0, 3.0, 0.5),
    (5.0, 4.0, 0.5),
    (3.0, 2.0, 0.5),
]


def evaluate(root, page_qrels, section_qrels, weights):
    os.environ["TYCHO_BM25_WEIGHTS"] = ",".join(
        f"{value:g}" for value in weights)
    sections = {item["id"]: item for item in section_qrels["items"]}
    counts = {"all": {"page": [0, 0, 0], "section": [0, 0, 0]}}
    totals = {"all": 0}
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
        for split in (item["split"], "all"):
            counts.setdefault(split, {"page": [0, 0, 0],
                                      "section": [0, 0, 0]})
            totals.setdefault(split, 0)
            totals[split] += 1
            for index, k in enumerate((1, 3, 5)):
                counts[split]["page"][index] += int(
                    bool(set(page_keys[:k]) & page_accept))
                counts[split]["section"][index] += int(
                    bool(set(section_keys[:k]) & section_accept))
    return {split: {level: [round(value / totals[split], 3)
                            for value in values]
                    for level, values in count.items()}
            for split, count in counts.items() if totals[split]}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=ROOT)
    args = ap.parse_args(argv)
    datasets = {}
    for name in ("v4", "v3"):
        page = json.loads((args.root / "evaluation" / (
            f"corpus-qrels.{name}.json")).read_text(encoding="utf-8"))
        section = json.loads((args.root / "evaluation" / (
            f"section-qrels.{name}.json")).read_text(encoding="utf-8"))
        datasets[name] = (page, section)
    output = {}
    for name, (page, section) in datasets.items():
        output[name] = {}
        for weights in GRID:
            output[name][str(weights)] = evaluate(
                args.root, page, section, weights)
    print(json.dumps(output, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
