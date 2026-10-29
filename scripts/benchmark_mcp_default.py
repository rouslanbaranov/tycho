#!/usr/bin/env python3
"""Benchmark pure BM25 versus margin-gated section rerank on qrels v3."""
import argparse
import json
from pathlib import Path
import statistics
import time

import section_search

ROOT = Path(__file__).resolve().parents[1]


def measure(root, queries, margin, repeats):
    samples = []
    skipped = 0
    for _ in range(repeats):
        for query in queries:
            with section_search._QUERY_CACHE_LOCK:
                section_search._QUERY_CACHE.clear()
            start = time.perf_counter()
            try:
                section_search.search(
                    root, query, limit=5, abstain=False,
                    section_rerank=margin is not None,
                    section_rerank_margin=margin)
            except section_search.SearchError:
                skipped += 1
                continue
            samples.append((time.perf_counter() - start) * 1000)
    return samples, skipped


def summary(samples):
    ordered = sorted(samples)
    def pct(fraction):
        return round(ordered[int(round((len(ordered) - 1) * fraction))], 1)
    return {"n": len(samples), "p50_ms": pct(0.5), "p95_ms": pct(0.95),
            "p99_ms": pct(0.99),
            "mean_ms": round(statistics.mean(samples), 1)}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=ROOT)
    ap.add_argument("--repeats", type=int, default=3)
    ap.add_argument("--limit", type=int, default=None)
    args = ap.parse_args(argv)
    data = json.loads((args.root / "evaluation/corpus-qrels.v3.json")
                      .read_text(encoding="utf-8"))
    queries = [item["question"] for item in data["items"]]
    if args.limit is not None:
        queries = queries[:args.limit]
    base, base_skipped = measure(args.root, queries, None, args.repeats)
    default, default_skipped = measure(args.root, queries, 0.15, args.repeats)
    print(json.dumps({"queries": len(queries), "repeats": args.repeats,
                      "base": summary(base), "base_skipped": base_skipped,
                      "default": summary(default),
                      "default_skipped": default_skipped}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
