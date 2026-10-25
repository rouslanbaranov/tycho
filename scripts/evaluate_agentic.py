#!/usr/bin/env python3
"""Run the frozen agentic benchmark over the MCP stdio transport.

The runner measures retrieval and agent cost, not answer quality or a
server-generated verdict. It starts one stdio server, issues bounded tool
calls and records citations, abstention, tool calls, context bytes and
latency. No query log or secret is used.
"""
import argparse
import json
import math
from pathlib import Path
import statistics
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
DATASET = ROOT / "evaluation/agentic-qrels.v1.json"
META = {
    "io.modelcontextprotocol/protocolVersion": "2026-07-28",
    "io.modelcontextprotocol/clientCapabilities": {},
}


def percentile(values, fraction):
    if not values:
        return None
    ordered = sorted(values)
    index = min(len(ordered) - 1, max(0, int(round(fraction * (len(ordered) - 1)))))
    return round(ordered[index], 6)


def ndcg_at(paths, accepted, k=10):
    accepted = set(accepted)
    if not accepted:
        return None
    dcg = 0.0
    for rank, path in enumerate(paths[:k], start=1):
        if path in accepted:
            dcg += 1.0 / math.log2(rank + 1)
    ideal = sum(1.0 / math.log2(rank + 1)
                for rank in range(1, min(len(accepted), k) + 1))
    return round(dcg / ideal, 6) if ideal else None


def first_relevant_rank(paths, accepted):
    accepted = set(accepted)
    for rank, path in enumerate(paths, start=1):
        if path in accepted:
            return rank
    return None


def summarize(records):
    answerable = [row for row in records if row["expected_abstention"] is False]
    unanswerable = [row for row in records if row["expected_abstention"] is True]
    def mean(key, rows):
        values = [row[key] for row in rows if row.get(key) is not None]
        return round(statistics.fmean(values), 6) if values else None
    latencies = [row["latency_ms"] for row in records]
    return {
        "answerable": {
            "count": len(answerable),
            "recall@10": mean("doc_hit", answerable),
            "ndcg@10": mean("ndcg@10", answerable),
            "mrr": mean("mrr", answerable),
            "top1": mean("top1", answerable),
            "path_precision": mean("path_precision", answerable),
            "policy_abstain_rate": mean("default_would_abstain", answerable),
            "policy_confident_rate": mean("policy_confident", answerable),
            "mean_tool_calls": mean("tool_calls", answerable),
            "mean_context_bytes": mean("context_bytes", answerable),
            "mean_latency_ms": mean("latency_ms", answerable),
        },
        "unanswerable": {
            "count": len(unanswerable),
            "abstention_rate": mean("abstained", unanswerable),
            "false_confident_count": sum(
                1 for row in unanswerable if row["confident_wrong"]),
        },
        "overall": {
            "count": len(records),
            "mean_tool_calls": mean("tool_calls", records),
            "mean_context_bytes": mean("context_bytes", records),
            "p50_latency_ms": percentile(latencies, 0.50),
            "p95_latency_ms": percentile(latencies, 0.95),
        },
    }


def request(process, request_id, method, params):
    payload = {
        "jsonrpc": "2.0",
        "id": request_id,
        "method": method,
        "params": params,
    }
    process.stdin.write(json.dumps(payload, ensure_ascii=False) + "\n")
    process.stdin.flush()
    while True:
        line = process.stdout.readline()
        if not line:
            raise RuntimeError(
                "MCP server exited while waiting for " + method)
        response = json.loads(line)
        if response.get("id") == request_id:
            if "error" in response:
                raise RuntimeError(
                    method + " failed: " + json.dumps(response["error"]))
            return response["result"]


def call_tool(process, request_id, name, arguments):
    result = request(process, request_id, "tools/call", {
        "_meta": META,
        "name": name,
        "arguments": arguments,
    })
    if result.get("isError"):
        raise RuntimeError(name + " returned isError")
    return result.get("structuredContent") or {}


def row_for(task, payload, reads, latency_ms, tool_calls):
    accepted = [entry["path"] for entry in task["accepted"]]
    confident_results = payload.get("results") or []
    results = confident_results or payload.get("weak_results") or []
    paths = [item.get("path") for item in results]
    rank = first_relevant_rank(paths, accepted)
    accepted_sections = {
        entry["path"] + "#" + entry["section_id"]
        for entry in task["accepted"] if entry.get("section_id")
    }
    returned_sections = {item.get("citation") for item in results}
    section_hit = None
    if accepted_sections:
        section_hit = bool(accepted_sections & returned_sections)
    precision = None
    if paths:
        precision = round(
            sum(1 for path in paths if path in accepted) / len(paths), 6)
    unanswerable = task["category"] == "unanswerable"
    status = payload.get("status")
    assessment = payload.get("answerability") or {}
    policy_abstained = assessment.get("no_confident_answer") is True
    abstained = policy_abstained or not paths
    return {
        "id": task["id"],
        "source_id": task["source_id"],
        "category": task["category"],
        "expected_abstention": unanswerable,
        "status": status,
        "policy_confident": assessment.get("confident"),
        "policy_state": assessment.get("state"),
        "default_would_abstain": policy_abstained,
        "returned": payload.get("returned"),
        "weak_returned": payload.get("weak_returned", 0),
        "visible_returned": len(results),
        "doc_hit": bool(rank),
        "section_hit": section_hit,
        "top1": rank == 1,
        "mrr": round(1.0 / rank, 6) if rank else 0.0,
        "ndcg@10": ndcg_at(paths, accepted),
        "path_precision": precision,
        "abstained": abstained,
        "confident_wrong": (
            unanswerable and assessment.get("confident") is True
            and bool(confident_results)),

        "tool_calls": tool_calls,
        "context_bytes": len(json.dumps(payload, ensure_ascii=False)) + sum(
            len(json.dumps(item, ensure_ascii=False)) for item in reads),
        "latency_ms": round(latency_ms, 3),
        "top_citations": [item.get("citation") for item in results[:3]],
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dataset", type=Path, default=DATASET)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--strategy", choices=("search-once", "search-read"),
                        default="search-once")
    parser.add_argument(
        "--mode", choices=("diagnostic", "strict", "exploratory"),
        default="diagnostic",
        help="diagnostic uses abstain=False; strict/exploratory use the policy")
    parser.add_argument("--max-tasks", type=int)
    parser.add_argument("--max-chars", type=int)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    dataset = json.loads(args.dataset.read_text(encoding="utf-8"))
    items = dataset["items"]
    if args.max_tasks is not None:
        items = items[:args.max_tasks]
    process = subprocess.Popen(
        [sys.executable, "scripts/mcp_server.py", "--root", str(args.root)],
        cwd=str(ROOT), stdin=subprocess.PIPE, stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL, text=True,
    )
    request_id = 0
    records = []
    try:
        request_id += 1
        describe = call_tool(process, request_id, "tycho_describe", {})
        records_meta = {
            "dataset": dataset["dataset"],
            "source": dataset["source"],
            "selection": dataset["selection"],
            "snapshot": describe.get("snapshot"),
            "strategy": args.strategy,
            "mode": args.mode,
            "max_chars": args.max_chars,
            "limit": args.limit,
            "head": subprocess.check_output(
                ["git", "rev-parse", "HEAD"], cwd=str(ROOT), text=True).strip(),
        }
        for task in items:
            start = time.perf_counter()
            request_id += 1
            search_args = {"query": task["question"], "limit": args.limit}
            if args.max_chars is not None:
                search_args["max_chars"] = args.max_chars
            if args.mode == "diagnostic":
                search_args["abstain"] = False
            elif args.mode == "strict":
                search_args["mode"] = "strict"
                search_args["abstain"] = True
            else:
                search_args["mode"] = "exploratory"
                search_args["abstain"] = True
            payload = call_tool(process, request_id, "tycho_search", search_args)
            reads = []
            calls = 1
            if args.strategy == "search-read" and payload.get("results"):
                request_id += 1
                reads.append(call_tool(process, request_id, "tycho_read", {
                    "section_key": payload["results"][0]["section_key"],
                    "budget_chars": 4000,
                }))
                calls += 1
            elapsed = (time.perf_counter() - start) * 1000.0
            records.append(row_for(task, payload, reads, elapsed, calls))
    finally:
        process.terminate()
        try:
            process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            process.kill()
    report = dict(records_meta)
    report["metrics"] = summarize(records)
    report["tasks"] = records
    text = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(text, encoding="utf-8")
        print(json.dumps({
            "json": str(args.json),
            "dataset": report["dataset"],
            "snapshot": report["snapshot"],
            "strategy": report["strategy"],
            "metrics": report["metrics"],
        }, indent=2, sort_keys=True))
    else:
        print(text)


if __name__ == "__main__":
    main()
