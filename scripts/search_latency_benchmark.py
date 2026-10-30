#!/usr/bin/env python3
"""Warm latency benchmark for qrels v4 queries."""
import argparse
import json
import statistics
import time
from pathlib import Path

import best_search
import section_search

ROOT = Path(__file__).resolve().parents[1]


def stats(values):
    ordered = sorted(values)
    return {
        "n": len(values),
        "mean_ms": round(statistics.mean(values) * 1000, 2),
        "p50_ms": round(statistics.median(values) * 1000, 2),
        "p95_ms": round(ordered[max(0, int(round(.95 * (len(ordered) - 1))))]
                         * 1000, 2),
        "max_ms": round(max(values) * 1000, 2),
    }


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=ROOT)
    args = ap.parse_args(argv)
    qrels = json.loads((args.root / "evaluation/corpus-qrels.v4.json")
                       .read_text(encoding="utf-8"))
    queries = [item["question"] for item in qrels["items"]]
    output = {"queries": len(queries), "index_bytes":
              (args.root / "generated/sections-fts-v5.sqlite").stat().st_size}
    cold = []
    for query in queries:
        with section_search._QUERY_CACHE_LOCK:
            section_search._QUERY_CACHE.clear()
        start = time.perf_counter()
        section_search.search(args.root, query, limit=5, abstain=False,
                              section_rerank=False)
        cold.append(time.perf_counter() - start)
    output["bm25_cold"] = stats(cold)
    warm = []
    for query in queries:
        start = time.perf_counter()
        section_search.search(args.root, query, limit=5, abstain=False,
                              section_rerank=False)
        warm.append(time.perf_counter() - start)
    output["bm25_warm"] = stats(warm)
    margin = []
    for query in queries:
        start = time.perf_counter()
        try:
            section_search.search(
                args.root, query, limit=5, abstain=False,
                section_rerank=True, section_rerank_margin=0.05)
        except section_search.SearchError:
            pass
        margin.append(time.perf_counter() - start)
    output["margin_005_warm"] = stats(margin)
    best_times = []
    for query in queries[:20]:
        start = time.perf_counter()
        best_search.best_search(args.root, query, limit=5)
        best_times.append(time.perf_counter() - start)
    output["best_warm_20"] = stats(best_times)
    print(json.dumps(output, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
