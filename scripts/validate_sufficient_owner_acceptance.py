#!/usr/bin/env python3
"""Validate the owner-acceptance record for sufficient promotions."""
import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = Path("edition/patterns/sufficient-owner-acceptance.v1.json")
SCHEMA = Path("schemas/sufficient-owner-acceptance.v1.schema.json")
REGISTRY = Path("edition/patterns/registry.v1.json")
PROMOTIONS = Path("edition/patterns/sufficient-promotions.v1.json")


def require(ok, message):
    if not ok:
        raise ValueError(message)


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def engine():
    try:
        from jsonschema import Draft202012Validator, FormatChecker
    except ImportError as exc:
        raise RuntimeError(
            "Install validation dependencies from requirements-validation.txt") from exc
    return Draft202012Validator, FormatChecker


def validate(root=ROOT):
    root = Path(root).resolve()
    Draft, Format = engine()
    schema = load(root / SCHEMA)
    Draft.check_schema(schema)
    data = load(root / ARTIFACT)
    errors = sorted(Draft(schema, format_checker=Format()).iter_errors(data),
                    key=lambda error: (list(map(str, error.path)), error.message))
    if errors:
        first = errors[0]
        path = "/".join(map(str, first.path)) or "(root)"
        raise ValueError("owner-acceptance-schema: " + str(len(errors)) +
                         " error(s), first at " + path + ": " + first.message)
    patterns = {item["id"] for item in load(root / REGISTRY)["patterns"]}
    promoted = {item["pattern_id"]
                for item in load(root / PROMOTIONS)["promotions"]}
    entries = data["accepted_entries"]
    for pattern_id in entries:
        require(pattern_id in patterns,
                "owner-acceptance-unknown-pattern: " + pattern_id)
        require(pattern_id in promoted,
                "owner-acceptance-without-promotion: " + pattern_id)
    for report in data["review_reports"]:
        path = (root / report).resolve()
        require(path.is_relative_to((root / "authoring/ai-reviews").resolve()),
                "owner-acceptance-report-location: " + report)
        require(path.is_file(), "owner-acceptance-report-missing: " + report)
    status = data["status"]
    if status == "pending":
        require(data["owner"] is None and data["accepted_at"] is None,
                "owner-acceptance-pending-fields")
        require(not entries, "owner-acceptance-pending-entries")
    else:
        require(data["owner"].strip(), "owner-acceptance-owner")
        require(data["accepted_at"], "owner-acceptance-date")
        require(bool(entries) == (status == "accepted"),
                "owner-acceptance-entry-state")
    return {"status": status, "entries": len(entries)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    try:
        result = validate(args.root)
    except (ValueError, OSError, KeyError, json.JSONDecodeError) as exc:
        print("FAIL:", exc, file=sys.stderr)
        return 1
    print("PASS: sufficient owner acceptance", result["status"],
          result["entries"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
