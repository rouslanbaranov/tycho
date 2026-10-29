#!/usr/bin/env python3
"""Measure search latency and index size on a frozen snapshot.

This is an operational baseline, not a relevance, quality or sufficiency claim.
"""
import argparse
import json
import math
from pathlib import Path
import statistics
import sys
import time

import route_index
import search_reindex
import section_fts_index
import section_search

ROOT = Path(__file__).resolve().parents[1]


def percentile(values, fraction):
    if not values:
        return None
    ordered = sorted(values)
    index = max(0, min(len(ordered) - 1, math.ceil(fraction * len(ordered)) - 1))
    return ordered[index]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--queries", type=Path,
                    default=ROOT / "evaluation/corpus-qrels.v2.json")
    ap.add_argument("--limit", type=int, default=5)
    ap.add_argument("--repeats", type=int, default=2)
    ap.add_argument("--warmup", type=int, default=3)
    ap.add_argument("--root", type=Path, default=ROOT)
    args = ap.parse_args(argv)
    data = json.loads(args.queries.read_text(encoding="utf-8"))
    questions = [item["question"] for item in data["items"]
                 if item.get("category") != "unanswerable"]
    for question in questions[:args.warmup]:
        section_search.search(args.root, question, limit=args.limit, abstain=False)
    samples = []
    for _ in range(args.repeats):
        for question in questions:
            started = time.perf_counter()
            section_search.search(args.root, question, limit=args.limit,
                                  abstain=False)
            samples.append((time.perf_counter() - started) * 1000)
    stats = section_fts_index.stats(args.root)
    payload = {
        "schema_version": 1,
        "status": "ok",
        "snapshot": stats["snapshot"],
        "queries": len(questions),
        "repeats": args.repeats,
        "latency_ms": {
            "mean": round(statistics.mean(samples), 3),
            "p50": round(percentile(samples, 0.50), 3),
            "p95": round(percentile(samples, 0.95), 3),
            "p99": round(percentile(samples, 0.99), 3),
            "max": round(max(samples), 3),
        },
        "index": {
            "bytes": stats["bytes"],
            "sections": stats["sections"],
            "passages": stats["passages"],
        },
        "ranker": section_search.RANKER_VERSION,
        "notice": "Operational baseline only; no quality, sufficiency or CI claim.",
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, ValueError, RuntimeError) as exc:
        print(json.dumps({"status": "error", "error": str(exc)}))
        sys.exit(1)
