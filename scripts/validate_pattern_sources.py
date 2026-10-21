#!/usr/bin/env python3
"""Validate the pattern source plan, reading ledger and registry bindings.

Structural checks only: this does not prove that a source supports a technical
claim, that a page was read independently or that the plan is complete.
"""
import argparse
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
PLAN = Path("edition/patterns/source-plan.v1.json")
LEDGER = Path("edition/patterns/reading-ledger.v1.json")
PLAN_SCHEMA = Path("schemas/pattern-source-plan.v1.schema.json")
LEDGER_SCHEMA = Path("schemas/pattern-reading-ledger.v1.schema.json")
REGISTRY = Path("edition/patterns/registry.v1.json")
ROUTE = Path("generated/route-index.v1.json")
REGISTER = Path("sources/register.json")
STATUS = {"read": "read", "planned": "not-read", "blocked": "blocked"}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def engine():
    try:
        from jsonschema import Draft202012Validator, FormatChecker
    except ImportError as exc:
        raise RuntimeError("Install validation dependencies from requirements-validation.txt") from exc
    return Draft202012Validator, FormatChecker


def check_schema(data, schema, label, root):
    Draft, Format = engine()
    schema = load(root / schema)
    Draft.check_schema(schema)
    errors = sorted(Draft(schema, format_checker=Format()).iter_errors(data),
                    key=lambda error: (list(map(str, error.path)), error.message))
    if errors:
        first = errors[0]
        path = "/".join(map(str, first.path)) or "(root)"
        raise ValueError(label + ": " + str(len(errors)) + " error(s), first at "
                         + path + ": " + first.message)


def validate_data(plan, ledger, registry, route, sources, root=ROOT):
    root = Path(root).resolve()
    check_schema(plan, PLAN_SCHEMA, "source-schema", root)
    check_schema(ledger, LEDGER_SCHEMA, "ledger-schema", root)

    require(plan["registry_sha256"] == hashlib.sha256(
        (root / REGISTRY).read_bytes()).hexdigest(), "source-registry-hash")
    require(plan["route_index_snapshot"] == route["snapshot_sha256"],
            "source-route-snapshot")
    patterns = {item["id"]: item for item in registry["patterns"]}
    require(len(plan["entries"]) == 145, "source-plan-entry-count")
    seen = set()
    read_ids = []
    planned = 0
    blocked = 0
    source_ids = {item["id"] for item in sources["sources"]}
    for entry in plan["entries"]:
        pattern_id = entry["pattern_id"]
        require(pattern_id in patterns, "source-plan-pattern: " + pattern_id)
        require(pattern_id not in seen, "source-plan-duplicate-pattern: " + pattern_id)
        seen.add(pattern_id)
        pattern = patterns[pattern_id]
        require(entry["catalog_name"] == pattern["catalog_name"], "source-plan-catalog-name")
        require(entry["priority"] == pattern["priority"], "source-plan-priority")
        expected_units = []
        for unit in entry["required_units"]:
            require(unit["source_id"] in source_ids,
                    "source-plan-unknown-source: " + unit["source_id"])
            if unit["status"] == "read":
                read_ids.append(unit["read_record_id"])
            elif unit["status"] == "planned":
                planned += 1
            elif unit["status"] == "blocked":
                blocked += 1
            expected_units.append({
                "source_id": unit["source_id"],
                "unit": unit["unit"],
                "status": STATUS[unit["status"]],
            })
        actual_units = pattern.get("source_units", [])
        require(actual_units == expected_units, "source-registry-mismatch: " + pattern_id)

    records = ledger["records"]
    require(len(records) == len({item["id"] for item in records}), "ledger-duplicate-id")
    by_record = {}
    for record in records:
        require(record["source_id"] in source_ids,
                "ledger-unknown-source: " + record["source_id"])
        require(record["access_date"] <= ledger["updated"], "ledger-access-date")
        by_record[record["id"]] = record
    referenced = list(plan["foundation_records"]) + read_ids
    require(set(referenced) == set(by_record), "ledger-unreferenced-record")
    for unit in [unit for entry in plan["entries"] for unit in entry["required_units"]
                 if unit["status"] == "read"]:
        require(unit["read_record_id"] in by_record, "source-plan-read-record")
        record = by_record[unit["read_record_id"]]
        require(record["source_id"] == unit["source_id"], "source-read-source")
        require(record["unit_url"] == unit["url"], "source-read-url")
        require(record["unit_label"] == unit["unit"], "source-read-label")
        require(record["unit_type"] == unit["unit_type"], "source-read-type")
        require(record["sections_read"] == unit["sections"], "source-read-sections")

    summary = plan["summary"]
    require(summary["entries"] == len(plan["entries"]), "source-summary-entries")
    require(summary["required_units"] == sum(len(e["required_units"]) for e in plan["entries"]),
            "source-summary-units")
    require(summary["read_units"] == len(read_ids), "source-summary-read")
    require(summary["planned_units"] == planned, "source-summary-planned")
    require(summary["blocked_units"] == blocked, "source-summary-blocked")
    require(summary["ledger_records"] == len(records), "source-summary-ledger")
    require(seen == set(patterns), "source-pattern-partition")

    return {
        "entries": len(plan["entries"]),
        "required_units": sum(len(e["required_units"]) for e in plan["entries"]),
        "read_units": len(read_ids),
        "planned_units": planned,
        "blocked_units": blocked,
        "ledger_records": len(records),
        "foundation_records": len(plan["foundation_records"]),
        "scope": "plan and ledger structure; not complete reading or technical truth",
    }


def validate(root=ROOT):
    root = Path(root).resolve()
    return validate_data(load(root / PLAN), load(root / LEDGER), load(root / REGISTRY),
                         load(root / ROUTE), load(root / REGISTER), root)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    try:
        result = validate(args.root)
    except (ValueError, OSError, KeyError, json.JSONDecodeError) as exc:
        print("FAIL:", exc, file=sys.stderr)
        sys.exit(1)
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print("PASS: source plan", result["entries"], "entries;",
              result["read_units"], "read;", result["ledger_records"], "ledger records")
    return 0


if __name__ == "__main__":
    sys.exit(main())
