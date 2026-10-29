#!/usr/bin/env python3
"""Page-level evaluation of BM25 and best mode on qrels v3."""
import argparse
import json
from pathlib import Path

import best_search
import section_search

ROOT = Path(__file__).resolve().parents[1]
SPLITS = ("v2", "p3", "v12", "all")


def hit(paths, accepted, k):
    return bool(set(paths[:k]) & accepted)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=ROOT)
    args = ap.parse_args(argv)
    qrels = json.loads((args.root / "evaluation/corpus-qrels.v3.json")
                       .read_text(encoding="utf-8"))
    counts = {split: {"n": 0, "bm25": [0, 0, 0], "best": [0, 0, 0],
                      "direct": [0, 0, 0]} for split in SPLITS}
    for item in qrels["items"]:
        accepted = set(item["accepted"])
        direct = set(item["direct"])
        bm25 = section_search.search(
            args.root, item["question"], limit=5, abstain=False)
        bm25_paths = [row["path"] for row in bm25.get("results", [])]
        best = best_search.best_search(args.root, item["question"], limit=5)
        best_paths = [row["path"] for row in best.get("results", [])]
        for split in (item["split"], "all"):
            bucket = counts[split]
            bucket["n"] += 1
            for k in (1, 3, 5):
                bucket["bm25"][[1, 3, 5].index(k)] += int(
                    hit(bm25_paths, accepted, k))
                bucket["best"][[1, 3, 5].index(k)] += int(
                    hit(best_paths, accepted, k))
                bucket["direct"][[1, 3, 5].index(k)] += int(
                    hit(best_paths, direct, k))
    result = {"qrels": "evaluation/corpus-qrels.v3.json",
              "status": qrels["status"], "splits": {}}
    for split, bucket in counts.items():
        n = bucket["n"]
        result["splits"][split] = {
            "n": n,
            "bm25": [round(v / n, 3) for v in bucket["bm25"]],
            "best": [round(v / n, 3) for v in bucket["best"]],
            "best_direct": [round(v / n, 3) for v in bucket["direct"]],
        }
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
