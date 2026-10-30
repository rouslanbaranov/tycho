#!/usr/bin/env python3
"""Validate independent qrels v4 page and section files."""
import argparse
import json
from pathlib import Path
import sqlite3
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "generated/sections-fts-v5.sqlite"


def fail(errors, message):
    errors.append(message)


def check_file(path, level, errors):
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("schema_version") != 4:
        fail(errors, f"{path}: schema_version must be 4")
    if data.get("status") != "ai-adjudicated-not-human":
        fail(errors, f"{path}: status must be ai-adjudicated-not-human")
    if data.get("level") != level:
        fail(errors, f"{path}: level must be {level}")
    items = data.get("items", [])
    if data.get("query_count") != len(items):
        fail(errors, f"{path}: query_count mismatch")
    ids = [item.get("id") for item in items]
    if len(ids) != len(set(ids)):
        fail(errors, f"{path}: duplicate query ids")
    counts = {}
    for item in items:
        qid = item.get("id", "")
        if not qid.startswith("V4-"):
            fail(errors, f"{path}: id does not start V4-: {qid}")
        counts[item.get("split")] = counts.get(item.get("split"), 0) + 1
        grades = item.get("grades", {})
        if not grades:
            fail(errors, f"{path}: no grades for {qid}")
        if any(value not in (0, 1, 2) for value in grades.values()):
            fail(errors, f"{path}: invalid grade for {qid}")
        accepted = set(item.get("accepted", []))
        direct = set(item.get("direct", []))
        if accepted != {key for key, value in grades.items() if value >= 1}:
            fail(errors, f"{path}: accepted mismatch for {qid}")
        if direct != {key for key, value in grades.items() if value == 2}:
            fail(errors, f"{path}: direct mismatch for {qid}")
        if not direct:
            fail(errors, f"{path}: no direct answer for {qid}")
    expected = {"book": 90, "atlas": 30, "v12": 30}
    if counts != expected:
        fail(errors, f"{path}: split counts {counts} != {expected}")
    return data


def section_map(errors):
    if not DB.is_file():
        fail(errors, f"missing section DB: {DB}")
        return {}
    db = sqlite3.connect("file:" + DB.as_posix() + "?mode=ro", uri=True)
    try:
        rows = db.execute(
            "SELECT section_key,path FROM sections").fetchall()
    finally:
        db.close()
    return {key: path for key, path in rows}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--page", type=Path, required=True)
    ap.add_argument("--section", type=Path, required=True)
    ap.add_argument("--root", type=Path, default=ROOT)
    args = ap.parse_args(argv)
    errors = []
    page = check_file(args.page, "page", errors)
    section = check_file(args.section, "section", errors)
    if page.get("snapshot") != section.get("snapshot"):
        fail(errors, "page/section snapshot mismatch")
    if page.get("content_commit") != section.get("content_commit"):
        fail(errors, "page/section content_commit mismatch")
    import section_fts_index
    current = section_fts_index.stats(args.root)["snapshot"]
    if page.get("snapshot") != current:
        fail(errors, "qrels snapshot is stale against current index")
    try:
        head = subprocess.check_output(
            ["git", "-C", str(args.root), "rev-parse", "HEAD"],
            text=True).strip()
    except (OSError, subprocess.CalledProcessError):
        head = None
    if head and page.get("content_commit") != head:
        fail(errors, "content_commit is not current HEAD")
    page_by_id = {item["id"]: item for item in page.get("items", [])}
    sections = section_map(errors)
    for item in section.get("items", []):
        page_item = page_by_id.get(item["id"])
        if page_item is None:
            fail(errors, "missing page query: " + item["id"])
            continue
        if page_item.get("question") != item.get("question"):
            fail(errors, "question mismatch: " + item["id"])
        for key, grade in item.get("grades", {}).items():
            path = sections.get(key)
            if path is None:
                fail(errors, f"unknown section key: {key}")
                continue
            if not (args.root / path).is_file():
                fail(errors, f"missing section path: {path}")
            page_grade = page_item.get("grades", {}).get(path)
            if page_grade is None:
                fail(errors, f"page missing section path: {item['id']} {path}")
            elif page_grade == 0 and grade >= 1:
                fail(errors, f"page/section grade conflict: {item['id']} {path}")
            elif page_grade == 1 and grade == 2:
                fail(errors, f"page partial but section direct: {item['id']}")
    for item in page.get("items", []):
        for path in item.get("grades", {}):
            if not (args.root / path).is_file():
                fail(errors, f"missing page path: {path}")
    if not errors:
        print("PASS: qrels v4 page/section files are internally consistent")
        return 0
    print("FAIL")
    for error in errors:
        print("-", error)
    return 1


if __name__ == "__main__":
    sys.exit(main())
