#!/usr/bin/env python3
"""Evaluate qrels v3 after excluding prior-accepted pages."""
import argparse
import json
from pathlib import Path

import best_search
import section_search

ROOT = Path(__file__).resolve().parents[1]


def hit(paths, accepted, k):
    return bool(set(paths[:k]) & accepted)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=ROOT)
    args = ap.parse_args(argv)
    pool = json.loads((args.root / "evaluation/corpus-qrels.v3.pool.json")
                      .read_text(encoding="utf-8"))
    priors = {row["id"]: set(row["prior_paths"]) for row in pool["queries"]}
    qrels = json.loads((args.root / "evaluation/corpus-qrels.v3.json")
                       .read_text(encoding="utf-8"))
    counts = {"all": {"n": 0, "bm25": [0, 0, 0], "best": [0, 0, 0]}}
    skipped = 0
    for item in qrels["items"]:
        new = set(item["accepted"]) - priors.get(item["id"], set())
        if not new:
            skipped += 1
            continue
        bm25 = section_search.search(
            args.root, item["question"], limit=5, abstain=False)
        best = best_search.best_search(args.root, item["question"], limit=5)
        bm25_paths = [row["path"] for row in bm25.get("results", [])]
        best_paths = [row["path"] for row in best.get("results", [])]
        bucket = counts.setdefault(item["split"], {
            "n": 0, "bm25": [0, 0, 0], "best": [0, 0, 0]})
        for target in (bucket, counts["all"]):
            target["n"] += 1
            for index, k in enumerate((1, 3, 5)):
                target["bm25"][index] += int(hit(bm25_paths, new, k))
                target["best"][index] += int(hit(best_paths, new, k))
    output = {"qrels": "evaluation/corpus-qrels.v3.json",
              "method": "prior-accepted pages excluded from targets",
              "skipped_queries": skipped, "splits": {}}
    for split, bucket in counts.items():
        n = bucket["n"]
        output["splits"][split] = {
            "n": n,
            "bm25": [round(v / n, 3) for v in bucket["bm25"]],
            "best": [round(v / n, 3) for v in bucket["best"]],
        }
    print(json.dumps(output, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
