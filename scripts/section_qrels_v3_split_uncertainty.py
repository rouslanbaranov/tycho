#!/usr/bin/env python3
"""Per-split paired uncertainty for section rerank on section-qrels v3."""
import argparse
import json
import math
from pathlib import Path
import random

import section_search

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


def summarize(pairs, bootstrap, rng):
    n = len(pairs)
    base = sum(pair[0] for pair in pairs) / n
    rerank = sum(pair[1] for pair in pairs) / n
    b01 = sum(1 for pair in pairs if not pair[0] and pair[1])
    b10 = sum(1 for pair in pairs if pair[0] and not pair[1])
    diffs = []
    for _ in range(bootstrap):
        sample = [pairs[rng.randrange(n)] for _ in range(n)]
        diffs.append(sum(pair[1] for pair in sample) / n
                     - sum(pair[0] for pair in sample) / n)
    return {"n": n, "base": round(base, 4), "rerank": round(rerank, 4),
            "diff": round(rerank - base, 4),
            "ci95": [round(percentile(diffs, 0.025), 4),
                     round(percentile(diffs, 0.975), 4)],
            "b01": b01, "b10": b10,
            "p": round(mcnemar_exact(b01, b10), 6)}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--bootstrap", type=int, default=5000)
    ap.add_argument("--seed", type=int, default=20261029)
    args = ap.parse_args(argv)
    qrels = json.loads((ROOT / "evaluation/section-qrels.v3.json")
                       .read_text(encoding="utf-8"))
    groups = {}
    for item in qrels["items"]:
        accepted = set(item["accepted"])
        base = section_search.search(
            ROOT, item["question"], limit=5, abstain=False,
            section_rerank=False)
        guarded = False
        try:
            rerank = section_search.search(
                ROOT, item["question"], limit=5, abstain=False,
                section_rerank=True)
        except section_search.SearchError:
            rerank = base
            guarded = True
        base_keys = [row["section_key"] for row in base.get("results", [])]
        rerank_keys = [row["section_key"]
                       for row in rerank.get("results", [])]
        pair = (bool(set(base_keys[:1]) & accepted),
                bool(set(rerank_keys[:1]) & accepted))
        groups.setdefault(item["split"], []).append((pair, guarded))
        groups.setdefault("all", []).append((pair, guarded))
    rng = random.Random(args.seed)
    output = {}
    for split, rows in sorted(groups.items()):
        pairs = [row[0] for row in rows]
        output[split] = summarize(pairs, args.bootstrap, rng)
        output[split]["guarded"] = sum(1 for row in rows if row[1])
    print(json.dumps(output, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
