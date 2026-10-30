#!/usr/bin/env python3
"""Concurrency audit for cached section search."""
import argparse
import json
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import section_search

ROOT = Path(__file__).resolve().parents[1]


def fingerprint(result):
    return [(row["section_key"], row["path"])
            for row in result.get("results", [])]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=ROOT)
    ap.add_argument("--workers", type=int, default=16)
    ap.add_argument("--rounds", type=int, default=3)
    args = ap.parse_args(argv)
    qrels = json.loads((args.root / "evaluation/corpus-qrels.v4.json")
                       .read_text(encoding="utf-8"))
    queries = [item["question"] for item in qrels["items"]]
    sequential = {}
    for query in queries:
        sequential[query] = fingerprint(section_search.search(
            args.root, query, limit=5, abstain=False, section_rerank=False))
    output = {"queries": len(queries), "workers": args.workers, "rounds": []}
    for round_number in range(args.rounds):
        with section_search._QUERY_CACHE_LOCK:
            section_search._QUERY_CACHE.clear()
        start = time.perf_counter()
        with ThreadPoolExecutor(max_workers=args.workers) as pool:
            concurrent = list(pool.map(
                lambda query: (query, fingerprint(section_search.search(
                    args.root, query, limit=5, abstain=False,
                    section_rerank=False))), queries))
        elapsed = time.perf_counter() - start
        mismatches = [query for query, value in concurrent
                      if value != sequential[query]]
        output["rounds"].append({
            "round": round_number + 1,
            "elapsed_ms": round(elapsed * 1000, 1),
            "mismatches": len(mismatches),
        })
    print(json.dumps(output, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
