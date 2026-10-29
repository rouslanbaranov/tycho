#!/usr/bin/env python3
"""Benchmark section_rerank overhead on phase2 queries."""
import argparse
import json
from pathlib import Path
import statistics
import time

import section_search

ROOT = Path(__file__).resolve().parents[1]


def measure(root, queries, rerank, repeats):
    samples = []
    for _ in range(repeats):
        for query in queries:
            with section_search._QUERY_CACHE_LOCK:
                section_search._QUERY_CACHE.clear()
            start = time.perf_counter()
            try:
                section_search.search(
                    root, query, limit=5, abstain=False,
                    section_rerank=rerank)
            except section_search.SearchError:
                continue
            samples.append((time.perf_counter() - start) * 1000)
    return samples


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
    args = ap.parse_args(argv)
    data = json.loads((args.root / "evaluation/agent-qrels.phase2.json")
                      .read_text(encoding="utf-8"))
    queries = [item["question"] for item in data["items"]
               if item.get("final_label") == "answerable"
               and "v12" not in item["question"].casefold()]
    base = measure(args.root, queries, False, args.repeats)
    rerank = measure(args.root, queries, True, args.repeats)
    print(json.dumps({"queries": len(queries), "repeats": args.repeats,
                      "default": summary(base),
                      "section_rerank": summary(rerank)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
