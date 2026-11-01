#!/usr/bin/env python3
"""Evaluate a bounded hashed-vector reranker against BM25 candidates.

This is a hybrid lexical probe, not a neural embedding benchmark. It uses the
same stdio MCP search surface and records whether reranking improves retrieval
on the frozen agentic set. It does not change the default server.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path
import re
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import evaluate_agentic  # noqa: E402

DATASET = ROOT / "evaluation/agentic-qrels.v1.json"
TOKEN = re.compile(r"[a-z0-9]+")


def vector(text, dimensions=512):
    values = [0.0] * dimensions
    for token in TOKEN.findall(text.casefold()):
        index = int(hashlib.sha256(token.encode()).hexdigest()[:8], 16)
        values[index % dimensions] += 1.0
    norm = math.sqrt(sum(value * value for value in values))
    return [value / norm for value in values] if norm else values


def cosine(left, right):
    return sum(a * b for a, b in zip(left, right))


def normalise_scores(items):
    values = [item["score"] for item in items]
    if not values:
        return {}
    low, high = min(values), max(values)
    if high == low:
        return {item["section_key"]: 0.0 for item in items}
    return {
        item["section_key"]: (item["score"] - low) / (high - low)
        for item in items
    }


def rank(items, question, accepted, alpha):
    if alpha == 0:
        return [item["path"] for item in items]
    query = vector(question)
    ranked = []
    for item in items:
        text = " ".join(str(item.get(key, "")) for key in (
            "title", "heading", "excerpt"))
        score = (1 - alpha) * item["_bm25_norm"] + alpha * cosine(
            query, vector(text))
        ranked.append((score, item["path"]))
    ranked.sort(key=lambda pair: (-pair[0], pair[1]))
    return [path for _, path in ranked]


def metrics(paths, accepted):
    rank_value = evaluate_agentic.first_relevant_rank(paths, accepted)
    return {
        "recall@10": 1.0 if rank_value else 0.0,
        "mrr": round(1.0 / rank_value, 6) if rank_value else 0.0,
        "ndcg@10": evaluate_agentic.ndcg_at(paths, accepted),
        "top1": rank_value == 1,
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dataset", type=Path, default=DATASET)
    parser.add_argument("--limit", type=int, default=20)
    parser.add_argument("--max-tasks", type=int)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    dataset = json.loads(args.dataset.read_text(encoding="utf-8"))
    items = dataset["items"]
    if args.max_tasks is not None:
        items = items[:args.max_tasks]
    process = subprocess.Popen(
        [sys.executable, "mcp/mcp_server.py", "--root", str(ROOT)],
        cwd=str(ROOT), stdin=subprocess.PIPE, stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL, text=True,
    )
    records = []
    try:
        request_id = 1
        described = evaluate_agentic.call_tool(
            process, request_id, "tycho_describe", {})
        snapshot = described.get("snapshot")
        for task in items:
            if task["category"] == "unanswerable":
                continue
            request_id += 1
            start = time.perf_counter()
            payload = evaluate_agentic.call_tool(
                process, request_id, "tycho_search", {
                    "query": task["question"], "limit": args.limit,
                    "abstain": False,
                })
            elapsed = (time.perf_counter() - start) * 1000.0
            results = payload.get("results") or []
            norms = normalise_scores(results)
            for item in results:
                item["_bm25_norm"] = norms.get(item["section_key"], 0.0)
            accepted = [entry["path"] for entry in task["accepted"]]
            records.append({
                "id": task["id"],
                "category": task["category"],
                "question": task["question"],
                "accepted": accepted,
                "items": results,
                "latency_ms": round(elapsed, 3),
            })
    finally:
        process.terminate()
        try:
            process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            process.kill()
    alphas = [0.0, 0.25, 0.5, 0.75, 1.0]
    summary = {}
    for alpha in alphas:
        rows = []
        for record in records:
            rows.append(metrics(
                rank(record["items"], record["question"],
                     record["accepted"], alpha),
                record["accepted"]))
        def mean(key):
            return round(sum(row[key] for row in rows) / len(rows), 6)
        summary[str(alpha)] = {
            "count": len(rows),
            "recall@10": mean("recall@10"),
            "mrr": mean("mrr"),
            "ndcg@10": mean("ndcg@10"),
            "top1": round(sum(row["top1"] for row in rows) / len(rows), 6),
        }
    report = {
        "dataset": dataset["dataset"],
        "snapshot": snapshot,
        "head": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=str(ROOT), text=True).strip(),
        "limit": args.limit,
        "candidate_tasks": len(records),
        "mean_latency_ms": round(
            sum(record["latency_ms"] for record in records) / len(records), 3),
        "alphas": summary,
        "decision": "no-default-change",
        "notice": (
            "Hashed bag-of-words vectors, not neural embeddings. This probe "
            "does not justify changing the default ranker."),
    }
    text = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(text, encoding="utf-8")
        print(text)
    else:
        print(text)


if __name__ == "__main__":
    main()
