#!/usr/bin/env python3
"""Validate one empty-context DeepSeek label batch for qrels v5-dense."""
import argparse
import json
from pathlib import Path
import sqlite3
import sys

ROOT = Path(__file__).resolve().parents[1]


def fail(errors, message):
    errors.append(message)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--batch", required=True)
    ap.add_argument("--labels", type=Path, required=True)
    ap.add_argument("--root", type=Path, default=ROOT)
    args = ap.parse_args(argv)
    candidates = json.loads(
        (args.root / "evaluation/qrels-v5-dense/batches" /
         (args.batch + ".candidates.json")).read_text(encoding="utf-8"))
    labels = json.loads(args.labels.read_text(encoding="utf-8"))
    errors = []
    if labels.get("batch") != args.batch:
        fail(errors, "batch id mismatch")
    if labels.get("status") != "ai-adjudicated-not-human":
        fail(errors, "status is not ai-adjudicated-not-human")
    expected = {item["id"]: item for item in candidates["items"]}
    actual = {item["id"]: item for item in labels.get("items", [])}
    if set(expected) != set(actual):
        fail(errors, "query set mismatch")
    con = sqlite3.connect(args.root / "generated/sections-fts-v5.sqlite")
    paths = {row[0] for row in con.execute("select distinct path from sections")}
    section_keys = {row[0] for row in con.execute(
        "select section_key from sections")}
    for qid, item in expected.items():
        seen = actual[qid]
        page_new = {entry["path"] for entry in item["page_new"]}
        section_new = {entry["section_key"] for entry in item["section_new"]}
        page_grades = seen.get("page_grades", {})
        section_grades = seen.get("section_grades", {})
        if set(page_grades) != page_new:
            fail(errors, qid + ": page grade keys mismatch")
        if set(section_grades) != section_new:
            fail(errors, qid + ": section grade keys mismatch")
        for key, grade in page_grades.items():
            if grade not in (0, 1, 2):
                fail(errors, qid + ": invalid page grade")
            if key not in paths:
                fail(errors, qid + ": unknown page path")
        for key, grade in section_grades.items():
            if grade not in (0, 1, 2):
                fail(errors, qid + ": invalid section grade")
            if key not in section_keys:
                fail(errors, qid + ": unknown section key")
    if errors:
        print("FAIL")
        for error in errors:
            print("-", error)
        return 1
    print("PASS: v5-dense batch labels are complete")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
