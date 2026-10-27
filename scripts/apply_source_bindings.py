#!/usr/bin/env python3
"""Merge extracted per-dimension source bindings into owner units."""
import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
OWNER = Path("edition/patterns/owner-units.v1.json")
PLAN = Path("edition/patterns/source-plan.v1.json")
LEDGER = Path("edition/patterns/reading-ledger.v1.json")
DIMENSIONS = ("mechanism", "invariant", "failure_recovery", "alternative")
FIELDS = ("pattern_id", "dimension", "source_id", "ledger_record",
          "section", "quote", "revision")


def require(ok, message):
    if not ok:
        raise ValueError(message)


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("bindings", nargs="+", type=Path)
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    root = args.root.resolve()
    owner = load(root / OWNER)
    plan = {item["pattern_id"]: item
            for item in load(root / PLAN)["entries"]}
    ledger = {item["id"]: item
              for item in load(root / LEDGER)["records"]}
    entries = {item["pattern_id"]: item for item in owner["entries"]}
    count = 0
    for path in args.bindings:
        for binding in load(path):
            for field in FIELDS:
                require(field in binding, "binding-field: " + field)
            pid = binding["pattern_id"]
            dim = binding["dimension"]
            require(pid in entries, "binding-pattern: " + pid)
            require(dim in DIMENSIONS, "binding-dimension: " + pid)
            require(binding["quote"] and len(binding["quote"].strip()) >= 30,
                    "binding-quote: " + pid + ": " + dim)
            units = plan[pid]["required_units"]
            unit = next((item for item in units
                         if item["source_id"] == binding["source_id"]
                         and item.get("read_record_id") == binding["ledger_record"]),
                        None)
            if unit is None:
                unit = next((item for item in units
                             if item["source_id"] == binding["source_id"]), None)
            require(unit is not None, "binding-source: " + pid + ": " + dim)
            require(unit.get("read_record_id") == binding["ledger_record"],
                    "binding-record: " + pid + ": " + dim)
            record = ledger.get(binding["ledger_record"])
            require(record is not None, "binding-record-missing: " + pid)
            require(record["status"] == "read", "binding-record-status: " + pid)
            require(record["source_id"] == binding["source_id"],
                    "binding-record-source: " + pid)
            require(binding["section"] in record.get("sections_read", []),
                    "binding-section: " + pid + ": " + dim)
            require(binding["revision"] == record.get("content_sha256"),
                    "binding-revision: " + pid + ": " + dim)
            evidence = entries[pid]["technical_evidence"][dim]
            require(evidence["state"] == "supported",
                    "binding-not-supported: " + pid + ": " + dim)
            existing = evidence.get("binding")
            if existing is not None:
                require(existing == binding, "binding-conflict: " + pid + ": " + dim)
            else:
                evidence["binding"] = {key: binding[key] for key in
                                       ("source_id", "ledger_record", "section",
                                        "quote", "revision")}
                count += 1
    (root / OWNER).write_text(json.dumps(owner, indent=2, ensure_ascii=False) + "\n")
    print("PASS: bindings applied", count)
    return 0


if __name__ == "__main__":
    sys.exit(main())
