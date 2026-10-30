#!/usr/bin/env python3
"""Evaluate BM25 field weights on qrels v4 page/section metrics."""
import argparse
import json
import os
from pathlib import Path

import section_search

ROOT = Path(__file__).resolve().parents[1]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=ROOT)
    args = ap.parse_args(argv)
    page_qrels = json.loads(
        (args.root / "evaluation/corpus-qrels.v4.json").read_text(
            encoding="utf-8"))
    section_qrels = json.loads(
        (args.root / "evaluation/section-qrels.v4.json").read_text(
            encoding="utf-8"))
    sections = {item["id"]: item for item in section_qrels["items"]}
    grid = [
        (5.0, 2.0, 0.25),
        (8.0, 3.0, 0.25),
        (5.0, 3.0, 0.5),
        (3.0, 1.0, 0.25),
        (5.0, 2.0, 1.0),
        (2.0, 1.0, 0.25),
        (5.0, 4.0, 0.5),
    ]
    output = {}
    for weights in grid:
        os.environ["TYCHO_BM25_WEIGHTS"] = ",".join(
            f"{value:g}" for value in weights)
        counts = {split: {"page": [0, 0, 0], "section": [0, 0, 0]}
                  for split in ("book", "atlas", "v12", "all")}
        totals = {split: 0 for split in counts}
        for item in page_qrels["items"]:
            with section_search._QUERY_CACHE_LOCK:
                section_search._QUERY_CACHE.clear()
            result = section_search.search(
                args.root, item["question"], limit=5, abstain=False,
                section_rerank=False)
            page_keys = [row["path"] for row in result.get("results", [])]
            section_keys = [row["section_key"]
                            for row in result.get("results", [])]
            page_accept = set(item["accepted"])
            section_accept = set(sections[item["id"]]["accepted"])
            for split in (item["split"], "all"):
                totals[split] += 1
                for index, k in enumerate((1, 3, 5)):
                    counts[split]["page"][index] += int(
                        bool(set(page_keys[:k]) & page_accept))
                    counts[split]["section"][index] += int(
                        bool(set(section_keys[:k]) & section_accept))
        entry = {}
        for split, count in counts.items():
            n = totals[split]
            entry[split] = {
                "n": n,
                "page": [round(value / n, 3)
                         for value in count["page"]],
                "section": [round(value / n, 3)
                            for value in count["section"]],
            }
        output[str(weights)] = entry
    print(json.dumps(output, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
