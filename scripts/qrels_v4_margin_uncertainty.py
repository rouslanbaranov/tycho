#!/usr/bin/env python3
"""Paired uncertainty for margin vs BM25 on qrels v4 page metrics."""
import argparse
import json
import math
from pathlib import Path
import random

import section_search

ROOT = Path(__file__).resolve().parents[1]


def mcnemar(b01, b10):
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
    ap.add_argument("--seed", type=int, default=20261030)
    ap.add_argument("--margin", type=float, default=0.05)
    args = ap.parse_args(argv)
    qrels = json.loads((args.root / "evaluation/corpus-qrels.v4.json")
                       .read_text(encoding="utf-8"))
    groups = {}
    for item in qrels["items"]:
        accepted = set(item["accepted"])
        base = section_search.search(
            args.root, item["question"], limit=5, abstain=False,
            section_rerank=False)
        try:
            margin = section_search.search(
                args.root, item["question"], limit=5, abstain=False,
                section_rerank=True, section_rerank_margin=args.margin)
        except section_search.SearchError:
            margin = base
        base_paths = [row["path"] for row in base.get("results", [])]
        margin_paths = [row["path"] for row in margin.get("results", [])]
        pair = {
            "top1": (bool(set(base_paths[:1]) & accepted),
                     bool(set(margin_paths[:1]) & accepted)),
            "top5": (bool(set(base_paths[:5]) & accepted),
                     bool(set(margin_paths[:5]) & accepted)),
        }
        groups.setdefault(item["split"], []).append(pair)
        groups.setdefault("all", []).append(pair)
    rng = random.Random(args.seed)
    output = {}
    for split, pairs in sorted(groups.items()):
        section = {}
        for metric in ("top1", "top5"):
            values = [pair[metric] for pair in pairs]
            n = len(values)
            base = sum(pair[0] for pair in values) / n
            margin = sum(pair[1] for pair in values) / n
            b01 = sum(1 for pair in values if not pair[0] and pair[1])
            b10 = sum(1 for pair in values if pair[0] and not pair[1])
            diffs = []
            for _ in range(args.bootstrap):
                sample = [values[rng.randrange(n)] for _ in range(n)]
                diffs.append(sum(pair[1] for pair in sample) / n
                              - sum(pair[0] for pair in sample) / n)
            section[metric] = {
                "base": round(base, 4), "margin": round(margin, 4),
                "diff": round(margin - base, 4),
                "ci95": [round(percentile(diffs, 0.025), 4),
                         round(percentile(diffs, 0.975), 4)],
                "b01": b01, "b10": b10,
                "p": round(mcnemar(b01, b10), 6),
            }
        output[split] = {"n": len(pairs), **section}
    print(json.dumps(output, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
