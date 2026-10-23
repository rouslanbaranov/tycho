#!/usr/bin/env python3
"""Evaluate the calibrated refusal policy against qrels v2.

This reports refusal/retention counts, not answer correctness. The qrels are
author-labelled; independent adjudication remains a separate gate.
"""
import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_QRELS = ROOT / "evaluation/corpus-qrels.v2.json"


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def rate(numerator, denominator):
    return numerator / denominator if denominator else None


def summarize(rows):
    answerable = [row for row in rows if not row["unanswerable"]]
    unanswerable = [row for row in rows if row["unanswerable"]]
    abstained_ans = [row for row in answerable if row["abstained"]]
    abstained_unans = [row for row in unanswerable if row["abstained"]]
    return {
        "items": len(rows),
        "answerable": len(answerable),
        "unanswerable": len(unanswerable),
        "answerable_retained": len(answerable) - len(abstained_ans),
        "answerable_false_abstain": len(abstained_ans),
        "answerable_retention": rate(
            len(answerable) - len(abstained_ans), len(answerable)),
        "unanswerable_abstained": len(abstained_unans),
        "unanswerable_false_answer": len(unanswerable) - len(abstained_unans),
        "unanswerable_abstention": rate(
            len(abstained_unans), len(unanswerable)),
        "abstention_precision": rate(
            len(abstained_unans),
            len(abstained_unans) + len(abstained_ans)),
        "false_answer_rate": rate(
            len(unanswerable) - len(abstained_unans), len(unanswerable)),
        "reasons": {
            reason: sum(1 for row in rows if row["basis"] == reason)
            for reason in sorted({row["basis"] for row in rows})
        },
    }


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--qrels", type=Path, default=DEFAULT_QRELS)
    ap.add_argument("--split", choices=("all", "dev", "heldout"), default="all")
    ap.add_argument("--limit", type=int, default=5)
    ap.add_argument("--root", type=Path, default=ROOT)
    ap.add_argument("--index", type=Path)
    args = ap.parse_args(argv)
    import section_search
    qrels = load(args.qrels)
    rows = []
    for item in qrels["items"]:
        if args.split != "all" and item["split"] != args.split:
            continue
        payload = section_search.search(
            args.root, item["question"], limit=args.limit,
            index_path=args.index, abstain=True)
        answer = payload.get("answerability", {})
        rows.append({
            "id": item["id"],
            "split": item["split"],
            "unanswerable": item["category"] == "unanswerable",
            "status": payload.get("status"),
            "abstained": payload.get("status") in (
                "no-confident-answer", "no-results"),
            "basis": answer.get("basis"),
            "returned": payload.get("returned", 0),
        })
    result = {
        "status": "ok",
        "split": args.split,
        "limit": args.limit,
        "qrels": str(args.qrels),
        "overall": summarize(rows),
        "by_split": {
            split: summarize([row for row in rows if row["split"] == split])
            for split in sorted({row["split"] for row in rows})
        },
        "label_status": qrels["status"],
        "independent_review": qrels["provenance"]["independent_review"],
        "limits": [
            "Author-labelled qrels; no independent adjudication.",
            "Refusal is not answer correctness.",
            "No CI, human review, owner acceptance or sufficiency claim.",
        ],
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
