#!/usr/bin/env python3
"""Validate qrels v4.1 expansion against frozen v4 labels."""
import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import section_fts_index
from validate_qrels_v4 import check_file, fail


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--page", type=Path, required=True)
    ap.add_argument("--section", type=Path, required=True)
    ap.add_argument("--baseline-page", type=Path, required=True)
    ap.add_argument("--baseline-section", type=Path, required=True)
    ap.add_argument("--root", type=Path, default=ROOT)
    ap.add_argument("--min", type=int, default=10)
    ap.add_argument("--max", type=int, default=15)
    args = ap.parse_args(argv)
    expected = {"book": 90, "atlas": 30, "v12": 30}
    errors = []
    page = check_file(args.page, "page", errors, expected)
    section = check_file(args.section, "section", errors, expected)
    baseline_page = json.loads(args.baseline_page.read_text(encoding="utf-8"))
    baseline_section = json.loads(
        args.baseline_section.read_text(encoding="utf-8"))
    current = section_fts_index.stats(args.root)["snapshot"]
    for name, data in (("page", page), ("section", section)):
        if data.get("snapshot") != current:
            fail(errors, name + ": snapshot is stale")
    page_by_id = {item["id"]: item for item in page["items"]}
    section_by_id = {item["id"]: item for item in section["items"]}
    base_page_by_id = {item["id"]: item for item in baseline_page["items"]}
    base_section_by_id = {
        item["id"]: item for item in baseline_section["items"]}
    if set(page_by_id) != set(base_page_by_id):
        fail(errors, "page query IDs differ from v4")
    if set(section_by_id) != set(base_section_by_id):
        fail(errors, "section query IDs differ from v4")
    for qid, item in page_by_id.items():
        base = base_page_by_id[qid]
        if item["question"] != base["question"]:
            fail(errors, qid + ": question changed")
        if item["split"] != base["split"]:
            fail(errors, qid + ": split changed")
        if not args.min <= len(item["grades"]) <= args.max:
            fail(errors, qid + ": page candidates outside range")
        for key, grade in base["grades"].items():
            if item["grades"].get(key) != grade:
                fail(errors, qid + ": baseline page grade changed")
        if not set(base["accepted"]).issubset(item["accepted"]):
            fail(errors, qid + ": baseline page accepted lost")
        new = set(item["grades"]) - set(base["grades"])
        if sum(1 for key in new if item["grades"][key] == 0) < 2:
            fail(errors, qid + ": fewer than two new page grade-0 labels")
        if len(new) < 1:
            fail(errors, qid + ": no new page candidate")
    for qid, item in section_by_id.items():
        base = base_section_by_id[qid]
        if item["question"] != base["question"]:
            fail(errors, qid + ": section question changed")
        if not args.min <= len(item["grades"]) <= args.max:
            fail(errors, qid + ": section candidates outside range")
        for key, grade in base["grades"].items():
            if item["grades"].get(key) != grade:
                fail(errors, qid + ": baseline section grade changed")
        if not set(base["accepted"]).issubset(item["accepted"]):
            fail(errors, qid + ": baseline section accepted lost")
        new = set(item["grades"]) - set(base["grades"])
        if sum(1 for key in new if item["grades"][key] == 0) < 2:
            fail(errors, qid + ": fewer than two new section grade-0 labels")
        if len(new) < 1:
            fail(errors, qid + ": no new section candidate")
    if errors:
        print("FAIL")
        for error in errors:
            print("-", error)
        return 1
    print("PASS: qrels v4.1 expansion is consistent")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
