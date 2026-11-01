#!/usr/bin/env python3
"""Validate claim-level judge output against its input tasks."""
import argparse
import json
import sys
from pathlib import Path


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def validate(judge, tasks):
    errors = []
    by_task = {t["task_id"]: t for t in tasks}
    seen = set()
    for item in judge.get("items", []):
        tid = item.get("task_id")
        if tid not in by_task:
            errors.append("unknown task: " + str(tid))
            continue
        if tid in seen:
            errors.append("duplicate task: " + tid)
        seen.add(tid)
        core_ids = {c["claim_id"] for c in by_task[tid]["claims"]}
        verdicts = item.get("claim_verdicts", [])
        vids = [v.get("claim_id") for v in verdicts]
        if len(vids) != len(set(vids)):
            errors.append(tid + ": duplicate claim verdicts")
        missing = core_ids - set(vids)
        if missing and item.get("core_coverage") == 2:
            errors.append(tid + ": coverage 2 with missing claims " + str(sorted(missing)))
        for v in verdicts:
            if v.get("claim_id") not in core_ids:
                errors.append(tid + ": unknown claim " + str(v.get("claim_id")))
            if not v.get("quote_id") or not v.get("reason"):
                errors.append(tid + ": incomplete verdict " + str(v.get("claim_id")))
        values = [v.get("verdict") for v in verdicts if v.get("core")]
        expected_support = 2 if values and all(v == "supported" for v in values) else (
            0 if "unsupported" in values else 1)
        if item.get("semantic_support") != expected_support:
            errors.append(tid + ": semantic_support inconsistent with claim verdicts")
        expected_pass = expected_support == 2 and item.get("core_coverage") == 2
        if bool(item.get("pass")) != expected_pass:
            errors.append(tid + ": pass inconsistent with support/coverage")
    return {"ok": not errors, "tasks": len(seen), "errors": errors}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("judge")
    parser.add_argument("--input", required=True)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    result = validate(load(args.judge), load(args.input)["tasks"])
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(("PASS" if result["ok"] else "FAIL") + ": " + str(result["tasks"]) + " tasks")
        for error in result["errors"]:
            print("  " + error)
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
