#!/usr/bin/env python3
"""Validate V12 artifact-level qrels."""
import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import section_search
import section_fts_index


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--file", type=Path, required=True)
    ap.add_argument("--root", type=Path, default=ROOT)
    ap.add_argument("--expected", type=int, default=30)
    args = ap.parse_args(argv)
    errors = []
    try:
        data = json.loads(args.file.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print("FAIL")
        print("- cannot read:", exc)
        return 1
    if data.get("schema_version") != 1:
        errors.append("schema_version must be 1")
    if data.get("status") != "ai-adjudicated-not-human":
        errors.append("status must be ai-adjudicated-not-human")
    items = data.get("items", [])
    if data.get("query_count") != len(items):
        errors.append("query_count mismatch")
    if len(items) != args.expected:
        errors.append(f"expected {args.expected} queries, got {len(items)}")
    current = section_fts_index.stats(args.root)["snapshot"]
    if data.get("snapshot") != current:
        errors.append("snapshot is stale against current index")
    artifacts = {item["id"]: item for item in
                 section_search.load_v12_artifacts(args.root)}
    ids = [item.get("id") for item in items]
    if len(ids) != len(set(ids)):
        errors.append("duplicate query ids")
    for item in items:
        qid = item.get("id", "")
        if not qid.startswith("V12A-"):
            errors.append(f"id does not start V12A-: {qid}")
        grades = item.get("grades", {})
        if not 4 <= len(grades) <= 10:
            errors.append(f"{qid}: need 4-10 candidates, got {len(grades)}")
        if any(value not in (0, 1, 2) for value in grades.values()):
            errors.append(f"{qid}: invalid grade")
        if any(key not in artifacts for key in grades):
            errors.append(f"{qid}: unknown artifact id")
        accepted = set(item.get("accepted", []))
        direct = set(item.get("direct", []))
        if accepted != {key for key, value in grades.items() if value >= 1}:
            errors.append(f"{qid}: accepted mismatch")
        if direct != {key for key, value in grades.items() if value == 2}:
            errors.append(f"{qid}: direct mismatch")
        if not direct:
            errors.append(f"{qid}: no direct answer")
    if errors:
        print("FAIL")
        for error in errors:
            print("-", error)
        return 1
    print("PASS: V12 artifact qrels are internally consistent")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
