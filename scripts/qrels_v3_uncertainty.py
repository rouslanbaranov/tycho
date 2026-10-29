#!/usr/bin/env python3
"""Paired uncertainty analysis for BM25 versus best on qrels v3."""
import argparse
import json
import math
from pathlib import Path
import random

import best_search
import section_search

ROOT = Path(__file__).resolve().parents[1]


def hit(paths, accepted):
    return bool(set(paths[:1]) & accepted)


def mcnemar_exact(b01, b10):
    n = b01 + b10
    if n == 0:
        return 1.0
    tail = sum(math.comb(n, k) for k in range(0, min(b01, b10) + 1))
    return min(1.0, 2.0 * tail / (2 ** n))


def percentile(values, fraction):
    ordered = sorted(values)
    index = int(round((len(ordered) - 1) * fraction))
    return ordered[index]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=ROOT)
    ap.add_argument("--bootstrap", type=int, default=5000)
    ap.add_argument("--seed", type=int, default=20261029)
    args = ap.parse_args(argv)
    qrels = json.loads((args.root / "evaluation/corpus-qrels.v3.json")
                       .read_text(encoding="utf-8"))
    rows = []
    for item in qrels["items"]:
        accepted = set(item["accepted"])
        bm25 = section_search.search(
            args.root, item["question"], limit=5, abstain=False)
        best = best_search.best_search(
            args.root, item["question"], limit=5)
        bm25_paths = [row["path"] for row in bm25.get("results", [])]
        best_paths = [row["path"] for row in best.get("results", [])]
        rows.append((hit(bm25_paths, accepted), hit(best_paths, accepted)))
    n = len(rows)
    bm25_hits = sum(row[0] for row in rows)
    best_hits = sum(row[1] for row in rows)
    b01 = sum(1 for row in rows if not row[0] and row[1])
    b10 = sum(1 for row in rows if row[0] and not row[1])
    rng = random.Random(args.seed)
    diffs = []
    for _ in range(args.bootstrap):
        sample = [rows[rng.randrange(n)] for _ in range(n)]
        diffs.append(sum(row[1] for row in sample) / n
                     - sum(row[0] for row in sample) / n)
    result = {
        "qrels": "evaluation/corpus-qrels.v3.json",
        "status": qrels["status"],
        "n": n,
        "bm25_top1": round(bm25_hits / n, 4),
        "best_top1": round(best_hits / n, 4),
        "diff": round((best_hits - bm25_hits) / n, 4),
        "ci95": [round(percentile(diffs, 0.025), 4),
                 round(percentile(diffs, 0.975), 4)],
        "discordant": {"bm25_only": b10, "best_only": b01},
        "mcnemar_exact_p": round(mcnemar_exact(b01, b10), 6),
        "bootstrap": args.bootstrap,
        "seed": args.seed,
        "limits": "AI-adjudicated page-level qrels; not human or independent review.",
    }
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
