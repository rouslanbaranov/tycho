#!/usr/bin/env python3
"""Validate the sufficient-promotion allowlist and its saved review reports."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = Path("edition/patterns/sufficient-promotions.v1.json")
SCHEMA = Path("schemas/sufficient-promotions.v1.schema.json")
REGISTRY = Path("edition/patterns/registry.v1.json")


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
        raise ValueError("promotions-schema: " + str(len(errors)) +
                         " error(s), first at " + path + ": " + first.message)
    patterns = {item["id"] for item in load(root / REGISTRY)["patterns"]}
    head = subprocess.check_output(
        ["git", "-C", str(root), "rev-parse", "HEAD"], text=True).strip()
    seen = set()
    for item in data["promotions"]:
        pattern_id = item["pattern_id"]
        require(pattern_id in patterns, "promotions-unknown-pattern: " + pattern_id)
        require(pattern_id not in seen, "promotions-duplicate: " + pattern_id)
        seen.add(pattern_id)
        report = (root / item["report_path"]).resolve()
        require(report.is_file() and not report.is_symlink(),
                "promotions-report-missing: " + pattern_id)
        require(hashlib.sha256(report.read_bytes()).hexdigest()
                == item["report_sha256"],
                "promotions-report-hash: " + pattern_id)
        ancestor = subprocess.run(
            ["git", "-C", str(root), "merge-base", "--is-ancestor",
             item["reviewed_head"], head], capture_output=True).returncode == 0
        require(ancestor, "promotions-head-not-ancestor: " + pattern_id)
    return {"promotions": len(data["promotions"])}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    try:
        result = validate(args.root)
    except (ValueError, OSError, KeyError, json.JSONDecodeError) as exc:
        print("FAIL:", exc, file=sys.stderr)
        return 1
    print("PASS: sufficient promotions", result["promotions"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
