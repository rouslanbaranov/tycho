#!/usr/bin/env python3
"""Build a section-level qrels v3 candidate pool and unreviewed packets."""
import argparse
import json
from pathlib import Path
import subprocess

import section_search

ROOT = Path(__file__).resolve().parents[1]
POOL = ROOT / "evaluation/section-qrels.v3.pool.json"
PACKETS = ROOT / "evaluation/section-qrels-v3"


def add(candidates, results, source):
    for rank, result in enumerate(results, 1):
        key = result["section_key"]
        entry = candidates.setdefault(key, {
            "section_key": key, "section_id": result.get("section_id"),
            "path": result["path"], "heading": result.get("heading", ""),
            "excerpt": result.get("excerpt", "")[:600],
            "sources": {},
        })
        entry["sources"].setdefault(source, rank)


def build(root):
    qrels = json.loads((root / "evaluation/corpus-qrels.v3.json")
                       .read_text(encoding="utf-8"))
    commit = subprocess.check_output(
        ["git", "-C", str(root), "rev-parse", "HEAD"], text=True).strip()
    queries = []
    for item in qrels["items"]:
        candidates = {}
        base = section_search.search(
            root, item["question"], limit=5, abstain=False,
            section_rerank=False)
        reranked = section_search.search(
            root, item["question"], limit=5, abstain=False,
            section_rerank=True)
        add(candidates, base.get("results", []), "bm25")
        add(candidates, reranked.get("results", []), "section-rerank")
        queries.append({
            "id": item["id"], "split": item["split"],
            "question": item["question"],
            "candidates": sorted(candidates.values(),
                                 key=lambda entry: entry["section_key"]),
        })
    return {
        "schema_version": 1, "status": "pooled-unreviewed",
        "snapshot": qrels["snapshot"], "content_commit": commit,
        "level": "section", "query_count": len(queries),
        "candidate_count": sum(len(query["candidates"]) for query in queries),
        "sources": ["bm25", "section-rerank"], "queries": queries,
        "limits": "AI section adjudication required; not human review.",
    }


def write_packets(pool, size=20):
    PACKETS.mkdir(parents=True, exist_ok=True)
    rows = pool["queries"]
    batches = [rows[i:i + size] for i in range(0, len(rows), size)]
    for number, batch in enumerate(batches, 1):
        payload = {"schema_version": 1, "packet": number,
                   "packets": len(batches), "status": "unreviewed",
                   "snapshot": pool["snapshot"], "level": "section",
                   "queries": batch,
                   "instructions": ("Grade every section 0/1/2; page-level "
                                    "prior labels are not answers.")}
        (PACKETS / ("packet-%02d.json" % number)).write_text(
            json.dumps(payload, indent=2, sort_keys=True) + "\n",
            encoding="utf-8")
    return len(batches)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=ROOT)
    args = ap.parse_args(argv)
    pool = build(args.root)
    POOL.write_text(json.dumps(pool, indent=2, sort_keys=True) + "\n",
                    encoding="utf-8")
    count = write_packets(pool)
    print(json.dumps({"queries": pool["query_count"],
                      "candidates": pool["candidate_count"],
                      "packets": count}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
