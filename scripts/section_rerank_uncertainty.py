#!/usr/bin/env python3
"""Paired uncertainty for section rerank top-1 on phase2+phase3."""
import argparse
import json
import math
from pathlib import Path
import random

ROOT = Path(__file__).resolve().parents[1]


def mcnemar_exact(b01, b10):
    n = b01 + b10
    if n == 0:
        return 1.0
    tail = sum(math.comb(n, k) for k in range(0, min(b01, b10) + 1))
    return min(1.0, 2.0 * tail / (2 ** n))


def percentile(values, fraction):
    ordered = sorted(values)
    return ordered[int(round((len(ordered) - 1) * fraction))]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=ROOT)
    ap.add_argument("--bootstrap", type=int, default=5000)
    ap.add_argument("--seed", type=int, default=20261029)
    args = ap.parse_args(argv)
    data = json.loads((args.root / "evaluation/section-rerank-validation.json")
                      .read_text(encoding="utf-8"))
    rows = data["phase2"]["rows"] + data["phase3"]["rows"]
    pairs = [(row["base"][0], row["reranked"][0]) for row in rows]
    n = len(pairs)
    base = sum(pair[0] for pair in pairs) / n
    rerank = sum(pair[1] for pair in pairs) / n
    b01 = sum(1 for pair in pairs if not pair[0] and pair[1])
    b10 = sum(1 for pair in pairs if pair[0] and not pair[1])
    rng = random.Random(args.seed)
    diffs = []
    for _ in range(args.bootstrap):
        sample = [pairs[rng.randrange(n)] for _ in range(n)]
        diffs.append(sum(pair[1] for pair in sample) / n
                     - sum(pair[0] for pair in sample) / n)
    result = {
        "n": n,
        "base_top1": round(base, 4),
        "rerank_top1": round(rerank, 4),
        "diff": round(rerank - base, 4),
        "ci95": [round(percentile(diffs, 0.025), 4),
                 round(percentile(diffs, 0.975), 4)],
        "discordant": {"base_only": b10, "rerank_only": b01},
        "mcnemar_exact_p": round(mcnemar_exact(b01, b10), 6),
        "bootstrap": args.bootstrap,
        "seed": args.seed,
        "labels": "agent-adjudicated; not human review",
    }
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
