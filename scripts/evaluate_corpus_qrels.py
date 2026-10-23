#!/usr/bin/env python3
"""Evaluate corpus-level relevance judgments against a section search function.

The metric functions are pure and testable without the search layer. The CLI
imports section_search lazily, so this script can be reviewed before #50 lands.
Results are a diagnostic for the pinned snapshot, not a claim of answer quality.
"""
import argparse
import json
import math
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_QRELS = ROOT / "evaluation/corpus-qrels.v2.json"
DEFAULT_ROUTE = ROOT / "generated/route-index.v1.json"
K_VALUES = (1, 3, 5)
SCOPES = ("page", "chapter", "section")


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def first_rank(results, predicate):
    for index, result in enumerate(results, start=1):
        if predicate(result):
            return index
    return None


def page_predicate(accepted):
    paths = {answer["path"] for answer in accepted}
    return lambda result: result.get("path") in paths


def chapter_predicate(accepted, parent_of):
    parents = {parent_of.get(answer["path"]) for answer in accepted}
    return lambda result: parent_of.get(result.get("path")) in parents


def section_predicate(accepted):
    def predicate(result):
        for answer in accepted:
            if result.get("path") != answer["path"]:
                continue
            if answer["section_id"] is None or answer["section_id"] == result.get("section_id"):
                return True
        return False
    return predicate


def ndcg_at(results, accepted, k=10):
    grades = {}
    for answer in accepted:
        grades[answer["path"]] = max(grades.get(answer["path"], 0), answer["grade"])
    dcg = 0.0
    for index, result in enumerate(results[:k], start=1):
        gain = grades.get(result.get("path"), 0)
        if gain:
            dcg += gain / math.log2(index + 1)
    ideal = sorted(grades.values(), reverse=True)[:k]
    idcg = sum(gain / math.log2(index + 1)
               for index, gain in enumerate(ideal, start=1))
    return dcg / idcg if idcg else None


def summarize(rows, k_values=K_VALUES):
    answerable = [row for row in rows if not row["unanswerable"]]
    count = len(answerable)
    summary = {
        "items": len(rows),
        "answerable": count,
        "unanswerable": len(rows) - count,
    }
    for scope in SCOPES:
        ranks = [row[scope + "_rank"] for row in answerable]
        block = {}
        for k in k_values:
            block["hit@" + str(k)] = (
                sum(1 for rank in ranks if rank and rank <= k) / count
                if count else None)
        block["mrr"] = (
            sum(1.0 / rank for rank in ranks if rank) / count
            if count else None)
        summary[scope] = block
    ndcgs = [row["ndcg@10"] for row in answerable if row["ndcg@10"] is not None]
    summary["ndcg@10"] = sum(ndcgs) / len(ndcgs) if ndcgs else None
    unanswered = [row for row in rows if row["unanswerable"]]
    summary["unanswerable_no_result_rate"] = (
        sum(1 for row in unanswered if row["no_result"]) / len(unanswered)
        if unanswered else None)
    return summary


def evaluate(items, search_fn, parent_of, k_values=K_VALUES):
    rows = []
    snapshots = set()
    for item in items:
        response = search_fn(item["question"])
        results = response.get("results", [])
        if response.get("snapshot"):
            snapshots.add(response["snapshot"])
        if item["category"] == "unanswerable":
            rows.append({
                "id": item["id"],
                "split": item["split"],
                "category": item["category"],
                "unanswerable": True,
                "no_result": response.get("status") == "no-results" or not results,
                "page_rank": None,
                "chapter_rank": None,
                "section_rank": None,
                "ndcg@10": None,
            })
            continue
        accepted = item["accepted"]
        rows.append({
            "id": item["id"],
            "split": item["split"],
            "category": item["category"],
            "unanswerable": False,
            "no_result": False,
            "page_rank": first_rank(results, page_predicate(accepted)),
            "chapter_rank": first_rank(results, chapter_predicate(accepted, parent_of)),
            "section_rank": first_rank(results, section_predicate(accepted)),
            "ndcg@10": ndcg_at(results, accepted),
        })

    def grouped(key):
        values = sorted({row[key] for row in rows})
        return {value: summarize([row for row in rows if row[key] == value], k_values)
                for value in values}

    return {
        "overall": summarize(rows, k_values),
        "by_split": grouped("split"),
        "by_category": grouped("category"),
        "search_snapshots": sorted(snapshots),
        "items": rows,
    }


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--qrels", type=Path, default=DEFAULT_QRELS)
    ap.add_argument("--route-index", type=Path, default=DEFAULT_ROUTE)
    ap.add_argument("--split", choices=("all", "dev", "heldout"), default="all")
    ap.add_argument("--limit", type=int, default=10)
    ap.add_argument("--root", type=Path, default=ROOT)
    ap.add_argument("--index", type=Path)
    args = ap.parse_args(argv)

    if not 1 <= args.limit <= 20:
        print(json.dumps({"status": "invalid-request",
                          "error": "limit must be in 1..20"}))
        return 1
    qrels = load(args.qrels)
    route = load(args.route_index)
    items = qrels["items"]
    if args.split != "all":
        items = [item for item in items if item["split"] == args.split]
    if not items:
        print(json.dumps({"status": "invalid-request",
                          "error": "no items for the selected split"}))
        return 1
    parent_of = {doc["path"]: doc["parent_id"] for doc in route["documents"]}
    try:
        import section_search
    except ImportError:
        print(json.dumps({
            "status": "not-available",
            "error": "section search layer is not present on this branch; merge #50 first",
        }))
        return 2

    def search_fn(question):
        return section_search.search(args.root, question, limit=args.limit,
                                     index_path=args.index, abstain=False)

    result = evaluate(items, search_fn, parent_of)
    if len(result["search_snapshots"]) > 1:
        print(json.dumps({"status": "snapshot-mismatch",
                          "error": "search snapshot changed during evaluation"}))
        return 1
    result.update({
        "status": "ok",
        "split": args.split,
        "limit": args.limit,
        "qrels_snapshot": qrels["snapshot"]["route_index_snapshot"],
        "search_snapshot": (result["search_snapshots"][0]
                            if result["search_snapshots"] else None),
        "label_status": qrels["status"],
        "independent_review": qrels["provenance"]["independent_review"],
    })
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
