#!/usr/bin/env python3
"""Validate the merged qrels v5-dense page/section files."""
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
    ap.add_argument("--page", type=Path, required=True)
    ap.add_argument("--section", type=Path, required=True)
    ap.add_argument("--root", type=Path, default=ROOT)
    args = ap.parse_args(argv)
    page = json.loads(args.page.read_text(encoding="utf-8"))
    section = json.loads(args.section.read_text(encoding="utf-8"))
    base_page = json.loads(
        (args.root / "evaluation/corpus-qrels.v4.1.json").read_text(
            encoding="utf-8"))
    base_section = json.loads(
        (args.root / "evaluation/section-qrels.v4.1.json").read_text(
            encoding="utf-8"))
    candidates = json.loads(
        (args.root / "evaluation/qrels-v5-dense/candidates.json").read_text(
            encoding="utf-8"))
    page_base = {item["id"]: item for item in base_page["items"]}
    section_base = {item["id"]: item for item in base_section["items"]}
    candidate_by_id = {item["id"]: item for item in candidates["items"]}
    errors = []
    for name, data, level in (("page", page, "page"),
                              ("section", section, "section")):
        if data.get("status") != "ai-adjudicated-not-human":
            fail(errors, name + ": bad status")
        if len(data.get("items", [])) != 150:
            fail(errors, name + ": expected 150 queries")
        if data.get("snapshot") != base_page["snapshot"]:
            fail(errors, name + ": stale snapshot")
    page_by_id = {item["id"]: item for item in page["items"]}
    section_by_id = {item["id"]: item for item in section["items"]}
    if set(page_by_id) != set(page_base):
        fail(errors, "page IDs differ from v4.1")
    if set(section_by_id) != set(section_base):
        fail(errors, "section IDs differ from v4.1")
    con = sqlite3.connect(args.root / "generated/sections-fts-v5.sqlite")
    paths = {row[0] for row in con.execute("select distinct path from sections")}
    section_keys = {row[0] for row in con.execute(
        "select section_key from sections")}
    for qid, page_item in page_by_id.items():
        candidate = candidate_by_id[qid]
        expected_pages = (set(candidate["page_existing"]) |
                          {entry["path"] for entry in candidate["page_new"]})
        if set(page_item["grades"]) != expected_pages:
            fail(errors, qid + ": page candidate set mismatch")
        if len(page_item["grades"]) != candidates["target_candidates"]:
            fail(errors, qid + ": wrong page candidate count")
        for key, grade in page_item["grades"].items():
            if key not in paths:
                fail(errors, qid + ": unknown page path")
            if grade not in (0, 1, 2):
                fail(errors, qid + ": invalid page grade")
        base = page_base[qid]
        for key, grade in base["grades"].items():
            if page_item["grades"].get(key) != grade:
                fail(errors, qid + ": page baseline grade changed")
        if not set(base["accepted"]).issubset(page_item["accepted"]):
            fail(errors, qid + ": page accepted lost")
        section_item = section_by_id[qid]
        expected_sections = (set(candidate["section_existing"]) |
                             {entry["section_key"]
                              for entry in candidate["section_new"]})
        if set(section_item["grades"]) != expected_sections:
            fail(errors, qid + ": section candidate set mismatch")
        if len(section_item["grades"]) != candidates["target_candidates"]:
            fail(errors, qid + ": wrong section candidate count")
        for key, grade in section_item["grades"].items():
            if key not in section_keys:
                fail(errors, qid + ": unknown section key")
            if grade not in (0, 1, 2):
                fail(errors, qid + ": invalid section grade")
        base = section_base[qid]
        for key, grade in base["grades"].items():
            if section_item["grades"].get(key) != grade:
                fail(errors, qid + ": section baseline grade changed")
        if not set(base["accepted"]).issubset(section_item["accepted"]):
            fail(errors, qid + ": section accepted lost")
        for name, item in (("page", page_item), ("section", section_item)):
            accepted = sorted(k for k, v in item["grades"].items() if v >= 1)
            direct = sorted(k for k, v in item["grades"].items() if v == 2)
            if item["accepted"] != accepted:
                fail(errors, qid + ": " + name + " accepted mismatch")
            if item["direct"] != direct:
                fail(errors, qid + ": " + name + " direct mismatch")
            if not direct:
                fail(errors, qid + ": no direct " + name)
    if errors:
        print("FAIL")
        for error in errors:
            print("-", error)
        return 1
    print("PASS: qrels v5-dense is dense and preserves v4.1")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
