#!/usr/bin/env python3
"""Sweep section-rerank margin thresholds on qrels v4 at body 0.5."""
import argparse
import json
from pathlib import Path

import section_search

ROOT = Path(__file__).resolve().parents[1]
THRESHOLDS = (0.05, 0.1, 0.15, 0.2, 0.3, 0.4, 0.5, None)


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
    counts = {}
    totals = {}
    for threshold in (False,) + THRESHOLDS:
        label = ("base" if threshold is False else
                 "global" if threshold is None else str(threshold))
        counts[label] = {split: {"page": [0, 0, 0],
                                  "section": [0, 0, 0]}
                         for split in ("book", "atlas", "v12", "all")}
        totals[label] = {split: 0 for split in counts[label]}
    for item in page_qrels["items"]:
        for threshold in (False,) + THRESHOLDS:
            label = ("base" if threshold is False else
                     "global" if threshold is None else str(threshold))
            if threshold is False:
                result = section_search.search(
                    args.root, item["question"], limit=5, abstain=False,
                    section_rerank=False)
            else:
                try:
                    result = section_search.search(
                        args.root, item["question"], limit=5, abstain=False,
                        section_rerank=True, section_rerank_margin=threshold)
                except section_search.SearchError:
                    result = section_search.search(
                        args.root, item["question"], limit=5, abstain=False,
                        section_rerank=False)
            page_keys = [row["path"] for row in result.get("results", [])]
            section_keys = [row["section_key"]
                            for row in result.get("results", [])]
            page_accept = set(item["accepted"])
            section_accept = set(sections[item["id"]]["accepted"])
            for split in (item["split"], "all"):
                totals[label][split] += 1
                for index, k in enumerate((1, 3, 5)):
                    counts[label][split]["page"][index] += int(
                        bool(set(page_keys[:k]) & page_accept))
                    counts[label][split]["section"][index] += int(
                        bool(set(section_keys[:k]) & section_accept))
    output = {}
    for label, splits in counts.items():
        output[label] = {}
        for split, count in splits.items():
            n = totals[label][split]
            output[label][split] = {
                "n": n,
                "page": [round(value / n, 3)
                         for value in count["page"]],
                "section": [round(value / n, 3)
                            for value in count["section"]],
            }
    print(json.dumps(output, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
