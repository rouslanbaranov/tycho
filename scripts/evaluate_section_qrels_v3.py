#!/usr/bin/env python3
"""Evaluate BM25 and section_rerank on section-qrels v3."""
import argparse
import json
from pathlib import Path

import section_search

ROOT = Path(__file__).resolve().parents[1]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=ROOT)
    args = ap.parse_args(argv)
    qrels = json.loads((args.root / "evaluation/section-qrels.v3.json")
                       .read_text(encoding="utf-8"))
    counts = {"all": {"n": 0, "base": [0, 0, 0],
                       "rerank": [0, 0, 0], "guarded": 0}}
    for item in qrels["items"]:
        accepted = set(item["accepted"])
        base = section_search.search(
            args.root, item["question"], limit=5, abstain=False,
            section_rerank=False)
        guarded = False
        try:
            rerank = section_search.search(
                args.root, item["question"], limit=5, abstain=False,
                section_rerank=True)
        except section_search.SearchError:
            rerank = base
            guarded = True
        base_keys = [row["section_key"] for row in base.get("results", [])]
        rerank_keys = [row["section_key"]
                       for row in rerank.get("results", [])]
        for split in (item["split"], "all"):
            bucket = counts.setdefault(split, {"n": 0, "base": [0, 0, 0],
                                               "rerank": [0, 0, 0],
                                               "guarded": 0})
            bucket["n"] += 1
            bucket["guarded"] += int(guarded)
            for index, k in enumerate((1, 3, 5)):
                bucket["base"][index] += int(
                    bool(set(base_keys[:k]) & accepted))
                bucket["rerank"][index] += int(
                    bool(set(rerank_keys[:k]) & accepted))
    output = {"qrels": "evaluation/section-qrels.v3.json",
              "status": qrels["status"], "splits": {}}
    for split, bucket in counts.items():
        n = bucket["n"]
        output["splits"][split] = {
            "n": n, "guarded": bucket["guarded"],
            "base": [round(v / n, 3) for v in bucket["base"]],
            "rerank": [round(v / n, 3) for v in bucket["rerank"]],
        }
    print(json.dumps(output, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
