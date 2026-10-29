#!/usr/bin/env python3
"""Build the pooled qrels v3 candidate set and unreviewed packets.

The pool is page-level. Prior qrels are preserved as seed evidence, never as
final v3 labels. Independent adjudication is external and not performed here.
"""
import argparse
import json
from pathlib import Path
import subprocess
import sys

import best_search
import section_fts_index

ROOT = Path(__file__).resolve().parents[1]
POOL = ROOT / "evaluation/corpus-qrels.v3.pool.json"
PACKETS = ROOT / "evaluation/qrels-v3"
SOURCES = (
    ("v2", "evaluation/corpus-qrels.v2.json"),
    ("p3", "evaluation/agent-qrels.phase3.json"),
    ("v12", "evaluation/v12-simulation-qrels.v1.json"),
)


def load_queries(root):
    rows = []
    for split, relative in SOURCES:
        data = json.loads((Path(root) / relative).read_text(encoding="utf-8"))
        for item in data.get("items", []):
            if split == "p3" and item.get("final_label") != "answerable":
                continue
            if item.get("category") == "unanswerable":
                continue
            rows.append((split, item))
    return rows


def prior_paths(item):
    return {entry["path"] for entry in item.get("accepted", [])}


def add_candidates(candidates, results, source):
    for rank, result in enumerate(results, 1):
        path = result["path"]
        entry = candidates.setdefault(path, {
            "path": path,
            "sections": [],
            "sources": {},
            "prior": False,
            "title": "",
            "heading": "",
            "excerpt": "",
        })
        entry["title"] = entry["title"] or str(result.get("title", ""))
        entry["heading"] = entry["heading"] or str(result.get("heading", ""))
        entry["excerpt"] = entry["excerpt"] or str(result.get("excerpt", ""))[:600]
        section = result.get("section_id")
        if section and section not in entry["sections"]:
            entry["sections"].append(section)
        entry["sources"].setdefault(source, rank)


def build(root):
    queries = load_queries(root)
    snapshot = section_fts_index.stats(root)["snapshot"]
    commit = subprocess.check_output(
        ["git", "-C", str(root), "rev-parse", "HEAD"],
        text=True).strip()
    pool_queries = []
    for split, item in queries:
        candidates = {}
        import section_search
        bm25 = section_search.search(
            root, item["question"], limit=10, abstain=False).get("results", [])
        best = best_search.best_search(
            root, item["question"], limit=10)
        add_candidates(candidates, bm25, "bm25")
        add_candidates(candidates, best["results"], "best")
        prior = prior_paths(item)
        for path in prior:
            if path not in candidates and (Path(root) / path).is_file():
                candidates[path] = {"path": path, "sections": [],
                                    "sources": {"prior": 0}, "prior": True}
        for path, entry in candidates.items():
            entry["prior"] = path in prior
        pool_queries.append({
            "id": item["id"],
            "split": split,
            "question": item["question"],
            "prior_paths": sorted(prior),
            "candidates": sorted(candidates.values(),
                                 key=lambda entry: entry["path"]),
        })
    return {
        "schema_version": 1,
        "status": "pooled-unreviewed",
        "snapshot": snapshot,
        "content_commit": commit,
        "query_count": len(pool_queries),
        "candidate_count": sum(len(row["candidates"]) for row in pool_queries),
        "level": "page",
        "sources": ["bm25", "best"],
        "queries": pool_queries,
        "limits": (
            "Candidate pool only. Prior qrels are seed evidence; no final v3 "
            "grades. Independent adjudication is required."
        ),
    }


def write_packets(pool, size=20):
    PACKETS.mkdir(parents=True, exist_ok=True)
    rows = pool["queries"]
    packets = [rows[i:i + size] for i in range(0, len(rows), size)]
    for number, batch in enumerate(packets, 1):
        payload = {
            "schema_version": 1,
            "packet": number,
            "packets": len(packets),
            "status": "unreviewed",
            "snapshot": pool["snapshot"],
            "level": "page",
            "queries": batch,
            "instructions": (
                "Grade each candidate page 0 (not relevant), 1 (partially "
                "relevant) or 2 (directly relevant). Do not infer from prior "
                "labels. This is a read-only independent adjudication packet."
            ),
        }
        (PACKETS / ("packet-%02d.json" % number)).write_text(
            json.dumps(payload, indent=2, sort_keys=True) + "\n",
            encoding="utf-8")
    return len(packets)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=ROOT)
    args = ap.parse_args(argv)
    pool = build(args.root)
    POOL.write_text(json.dumps(pool, indent=2, sort_keys=True) + "\n",
                    encoding="utf-8")
    count = write_packets(pool)
    print(json.dumps({"pool": str(POOL), "queries": pool["query_count"],
                      "candidates": pool["candidate_count"],
                      "packets": count}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
