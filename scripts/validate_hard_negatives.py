#!/usr/bin/env python3
"""Validate one hard-negative label file."""
import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--batch", required=True)
    ap.add_argument("--labeler", required=True)
    ap.add_argument("--labels", type=Path, required=True)
    ap.add_argument("--root", type=Path, default=ROOT)
    args = ap.parse_args(argv)
    candidates = json.loads(
        (args.root / "evaluation/hard-negatives-v5/batches" /
         (args.batch + ".candidates.json")).read_text(encoding="utf-8"))
    labels = json.loads(args.labels.read_text(encoding="utf-8"))
    errors = []
    if labels.get("batch") != args.batch:
        errors.append("batch mismatch")
    if labels.get("labeler") != args.labeler:
        errors.append("labeler mismatch")
    if labels.get("status") != "ai-adjudicated-not-human":
        errors.append("status mismatch")
    expected = {item["id"]: item for item in candidates["items"]}
    actual = {item["id"]: item for item in labels.get("items", [])}
    if set(expected) != set(actual):
        errors.append("query set mismatch")
    for qid, item in expected.items():
        page = {x["path"] for x in item["page_new"]}
        section = {x["section_key"] for x in item["section_new"]}
        got = actual[qid]
        if set(got.get("page_grades", {})) != page:
            errors.append(qid + ": page keys mismatch")
        if set(got.get("section_grades", {})) != section:
            errors.append(qid + ": section keys mismatch")
        for value in list(got.get("page_grades", {}).values()) + list(
                got.get("section_grades", {}).values()):
            if value not in (0, 1, 2):
                errors.append(qid + ": invalid grade")
    if errors:
        print("FAIL")
        for error in errors:
            print("-", error)
        return 1
    print("PASS: hard-negative labels are complete")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
