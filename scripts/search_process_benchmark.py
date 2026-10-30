#!/usr/bin/env python3
"""Benchmark process isolation for qrels v4 search."""
import argparse
import json
import multiprocessing
from pathlib import Path
import time

ROOT = Path(__file__).resolve().parents[1]


def worker(payload):
    root, query = payload
    import section_search
    result = section_search.search(
        root, query, limit=5, abstain=False, section_rerank=False)
    return [(row["section_key"], row["path"])
            for row in result.get("results", [])]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=ROOT)
    ap.add_argument("--processes", type=int, nargs="+", default=[2, 4, 8])
    args = ap.parse_args(argv)
    qrels = json.loads((args.root / "evaluation/corpus-qrels.v4.json")
                       .read_text(encoding="utf-8"))
    queries = [item["question"] for item in qrels["items"]]
    baseline = [worker((str(args.root), query)) for query in queries]
    output = {"queries": len(queries), "runs": []}
    for count in args.processes:
        start = time.perf_counter()
        with multiprocessing.Pool(processes=count) as pool:
            values = pool.map(
                worker, [(str(args.root), query) for query in queries],
                chunksize=5)
        elapsed = time.perf_counter() - start
        output["runs"].append({
            "processes": count,
            "elapsed_ms": round(elapsed * 1000, 1),
            "mismatches": sum(1 for value, expected in zip(values, baseline)
                              if value != expected),
        })
    print(json.dumps(output, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
