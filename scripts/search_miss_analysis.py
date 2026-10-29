#!/usr/bin/env python3
"""Diagnose BM25 retrieval misses on the frozen qrels.

Diagnostic only: no ranking changes and no quality claims.
"""
import argparse
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SOURCES = (("v2", "evaluation/corpus-qrels.v2.json"),
           ("p3", "evaluation/agent-qrels.phase3.json"))
TOKEN = re.compile(r"[a-z0-9]{3,}")


def tokens(value):
    return set(TOKEN.findall(value.lower()))


def load_queries(root):
    rows = []
    for split, relative in SOURCES:
        data = json.loads((Path(root) / relative).read_text(encoding="utf-8"))
        for item in data.get("items", []):
            if split == "p3" and item.get("final_label") != "answerable":
                continue
            if item.get("category") == "unanswerable":
                continue
            rows.append({"split": split, "id": item["id"],
                         "question": item["question"],
                         "accepted": item.get("accepted", [])})
    return rows


def accepted_set(item):
    return {(a["path"], a.get("section_id")) for a in item["accepted"]}


def exact_rank(results, wanted):
    for rank, result in enumerate(results, 1):
        if (result["path"], result["section_id"]) in wanted:
            return rank
        if (result["path"], None) in wanted:
            return rank
    return None


def page_rank(results, wanted):
    pages = {path for path, _ in wanted}
    for rank, result in enumerate(results, 1):
        if result["path"] in pages:
            return rank
    return None


def classify(exact, page):
    if exact is not None and exact <= 5:
        return "hit"
    if page is not None and page <= 5:
        return "section-granularity"
    if exact is not None and exact <= 20:
        return "exact-rank-6-20"
    if page is not None and page <= 20:
        return "page-rank-6-20"
    return "not-top-20"


def run(root, limit=20):
    import section_search
    rows = load_queries(root)
    misses = []
    counts = {}
    for item in rows:
        results = section_search.search(
            root, item["question"], limit=limit, abstain=False).get(
                "results", [])
        wanted = accepted_set(item)
        exact = exact_rank(results, wanted)
        page = page_rank(results, wanted)
        status = classify(exact, page)
        counts[status] = counts.get(status, 0) + 1
        if status == "hit":
            continue
        top = results[0] if results else {}
        misses.append({
            "split": item["split"], "id": item["id"],
            "question": item["question"], "status": status,
            "exact_rank": exact, "page_rank": page,
            "accepted": sorted("%s#%s" % (p, s) for p, s in wanted),
            "top": {"path": top.get("path"),
                    "section_id": top.get("section_id"),
                    "heading": top.get("heading")},
            "query_tokens": len(tokens(item["question"])),
            "top_token_overlap": len(tokens(item["question"])
                                     & tokens(str(top.get("heading", "")))),
        })
    return {
        "schema_version": 1,
        "status": "diagnostic",
        "queries": len(rows),
        "misses": len(misses),
        "counts": counts,
        "by_split": {
            split: sum(1 for m in misses if m["split"] == split)
            for split, _ in SOURCES},
        "items": misses,
        "notice": "No ranking change; no quality or sufficiency claim.",
    }


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=ROOT)
    ap.add_argument("--limit", type=int, default=20)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args(argv)
    report = run(args.root, args.limit)
    if args.output:
        args.output.write_text(json.dumps(report, indent=2, sort_keys=True)
                               + "\n", encoding="utf-8")
    print(json.dumps({k: report[k] for k in
                      ("queries", "misses", "counts", "by_split")},
                     indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
