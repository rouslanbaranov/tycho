#!/usr/bin/env python3
"""Benchmark 1/2/4 real MCP stdio processes on qrels v4 queries."""
import argparse
import json
import multiprocessing
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]


def worker(payload):
    root, queries = payload
    requests = [
        {"jsonrpc": "2.0", "id": 1, "method": "initialize",
         "params": {"protocolVersion": "2025-11-25", "capabilities": {},
                    "clientInfo": {"name": "throughput", "version": "1"}}},
        {"jsonrpc": "2.0", "method": "notifications/initialized"},
    ]
    for index, query in enumerate(queries, 2):
        requests.append({
            "jsonrpc": "2.0", "id": index, "method": "tools/call",
            "params": {"name": "tycho_search",
                       "arguments": {"query": query}},
        })
    payload_text = "".join(json.dumps(request) + "\n"
                           for request in requests)
    proc = subprocess.run(
        [sys.executable, "scripts/mcp_server.py"], cwd=root,
        input=payload_text, text=True, capture_output=True, timeout=300)
    responses = [json.loads(line) for line in proc.stdout.splitlines()
                 if line.strip()]
    errors = sum(1 for message in responses
                 if message.get("error") or
                 message.get("result", {}).get("isError"))
    return {"queries": len(queries), "responses": len(responses),
            "errors": errors}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=ROOT)
    ap.add_argument("--processes", type=int, nargs="+", default=[1, 2, 4])
    args = ap.parse_args(argv)
    qrels = json.loads((args.root / "evaluation/corpus-qrels.v4.json")
                       .read_text(encoding="utf-8"))
    queries = [item["question"] for item in qrels["items"]]
    output = {"queries": len(queries), "runs": []}
    for count in args.processes:
        chunks = [queries[index::count] for index in range(count)]
        start = time.perf_counter()
        with multiprocessing.Pool(processes=count) as pool:
            values = pool.map(worker, [(str(args.root), chunk)
                                       for chunk in chunks])
        elapsed = time.perf_counter() - start
        output["runs"].append({
            "processes": count,
            "elapsed_ms": round(elapsed * 1000, 1),
            "responses": sum(value["responses"] for value in values),
            "errors": sum(value["errors"] for value in values),
        })
    print(json.dumps(output, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
