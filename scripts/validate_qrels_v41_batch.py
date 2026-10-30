#!/usr/bin/env python3
"""Validate one qrels v4.1 expansion batch."""
import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import section_fts_index
from validate_qrels_v4 import check_file, fail

BATCHES = {
    f"B{index:02d}": [f"V4-A{start + offset:03d}" for offset in range(10)]
    for index, start in enumerate(range(1, 151, 10), 1)
}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--page", type=Path, required=True)
    ap.add_argument("--section", type=Path, required=True)
    ap.add_argument("--batch", required=True, choices=sorted(BATCHES))
    ap.add_argument("--root", type=Path, default=ROOT)
    ap.add_argument("--min", type=int, default=10)
    ap.add_argument("--max", type=int, default=15)
    args = ap.parse_args(argv)
    ids = set(BATCHES[args.batch])
    baseline_page = json.loads(
        (args.root / "evaluation/corpus-qrels.v4.json").read_text(
            encoding="utf-8"))
    baseline_section = json.loads(
        (args.root / "evaluation/section-qrels.v4.json").read_text(
            encoding="utf-8"))
    base_page = [item for item in baseline_page["items"]
                 if item["id"] in ids]
    base_section = [item for item in baseline_section["items"]
                    if item["id"] in ids]
    if len(base_page) != 10 or len(base_section) != 10:
        raise SystemExit("baseline batch is incomplete")
    expected = {}
    for item in base_page:
        expected[item["split"]] = expected.get(item["split"], 0) + 1
    errors = []
    page = check_file(args.page, "page", errors, expected)
    section = check_file(args.section, "section", errors, expected)
    current = section_fts_index.stats(args.root)["snapshot"]
    for name, data in (("page", page), ("section", section)):
        if data.get("snapshot") != current:
            fail(errors, name + ": snapshot is stale")
    page_by_id = {item["id"]: item for item in page["items"]}
    section_by_id = {item["id"]: item for item in section["items"]}
    if set(page_by_id) != ids:
        fail(errors, "batch page IDs mismatch")
    if set(section_by_id) != ids:
        fail(errors, "batch section IDs mismatch")
    base_page_by_id = {item["id"]: item for item in base_page}
    base_section_by_id = {item["id"]: item for item in base_section}
    for qid in ids:
        item = page_by_id[qid]
        base = base_page_by_id[qid]
        if item["question"] != base["question"] or item["split"] != base["split"]:
            fail(errors, qid + ": question/split changed")
        if not args.min <= len(item["grades"]) <= args.max:
            fail(errors, qid + ": page candidates outside range")
        for key, grade in base["grades"].items():
            if item["grades"].get(key) != grade:
                fail(errors, qid + ": baseline page grade changed")
        new = set(item["grades"]) - set(base["grades"])
        if len(new) < 1:
            fail(errors, qid + ": no new page candidate")
        if sum(1 for key in new if item["grades"][key] == 0) < 2:
            fail(errors, qid + ": fewer than two new page grade-0 labels")
        item = section_by_id[qid]
        base = base_section_by_id[qid]
        if item["question"] != base["question"]:
            fail(errors, qid + ": section question changed")
        if not args.min <= len(item["grades"]) <= args.max:
            fail(errors, qid + ": section candidates outside range")
        for key, grade in base["grades"].items():
            if item["grades"].get(key) != grade:
                fail(errors, qid + ": baseline section grade changed")
        new = set(item["grades"]) - set(base["grades"])
        if len(new) < 1:
            fail(errors, qid + ": no new section candidate")
        if sum(1 for key in new if item["grades"][key] == 0) < 2:
            fail(errors, qid + ": fewer than two new section grade-0 labels")
    if errors:
        print("FAIL")
        for error in errors:
            print("-", error)
        return 1
    print("PASS: qrels v4.1 batch is consistent")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
