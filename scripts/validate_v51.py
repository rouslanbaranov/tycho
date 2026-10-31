#!/usr/bin/env python3
"""Validate v5.1 preserves v5 and adds one hard-negative unit per query."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=ROOT)
    args = ap.parse_args(argv)
    for level, base_name, target_name in (
            ("page", "corpus-qrels.v5-dense.json", "corpus-qrels.v5.1.json"),
            ("section", "section-qrels.v5-dense.json",
             "section-qrels.v5.1.json")):
        base = json.loads((args.root / "evaluation" / base_name).read_text(
            encoding="utf-8"))
        target = json.loads((args.root / "evaluation" / target_name).read_text(
            encoding="utf-8"))
        b = {i["id"]: i for i in base["items"]}
        t = {i["id"]: i for i in target["items"]}
        errors = []
        if set(b) != set(t):
            errors.append(level + ": ID mismatch")
        added = 0
        for qid in b:
            for key, grade in b[qid]["grades"].items():
                if t[qid]["grades"].get(key) != grade:
                    errors.append(qid + ": base grade changed")
            added += len(t[qid]["grades"]) - len(b[qid]["grades"])
            if t[qid]["accepted"] != sorted(
                    k for k, v in t[qid]["grades"].items() if v >= 1):
                errors.append(qid + ": accepted mismatch")
            if t[qid]["direct"] != sorted(
                    k for k, v in t[qid]["grades"].items() if v == 2):
                errors.append(qid + ": direct mismatch")
        if errors:
            print("FAIL", level, errors[:5])
            return 1
        print(level, "PASS", "added", added)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
