#!/usr/bin/env python3
"""Run strict JSON Schema Draft 2020-12 checks for Tycho metadata v1.

Requires the separately installed public `jsonschema` package with Draft 2020-12
and FormatChecker support. Checks actual date formats and unknown properties;
does not prove claim support, publication rights or real human review.
"""
import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = {
    "document": ROOT / "schemas/document-metadata.v1.schema.json",
    "source": ROOT / "schemas/source-reference.v1.schema.json",
}
EXAMPLES = {
    "document": [
        ROOT / "fixtures/metadata-valid-page.v1.json",
        ROOT / "fixtures/metadata-valid-book.v1.json",
    ],
    "source": [
        ROOT / "fixtures/source-valid-section.v1.json",
        ROOT / "fixtures/source-valid-git-reference.v1.json",
    ],
}


def engine():
    try:
        from jsonschema import Draft202012Validator, FormatChecker
    except ImportError as exc:
        raise RuntimeError(
            "JSON Schema validation dependency missing. Install with: "
            "python3 -m pip install -r requirements-validation.txt"
        ) from exc
    return Draft202012Validator, FormatChecker


def validate_document(kind, source):
    validator, checker = engine()
    schema = json.loads(SCHEMAS[kind].read_text(encoding="utf-8"))
    validator.check_schema(schema)
    data = json.loads(Path(source).read_text(encoding="utf-8"))
    errors = sorted(validator(schema, format_checker=checker()).iter_errors(data),
                    key=lambda e: (list(map(str, e.path)), e.message))
    if errors:
        first = errors[0]
        path = "/".join(map(str, first.path)) or "(document root)"
        raise ValueError(f"{source}: {len(errors)} error(s), first at {path}: {first.message}")
    return data


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("action", choices=("examples", "validate"))
    p.add_argument("--kind", choices=SCHEMAS, help="Required for one-file validation")
    p.add_argument("--file", type=Path, help="JSON instance to validate")
    args = p.parse_args()
    if args.action == "examples":
        count = 0
        for kind, paths in EXAMPLES.items():
            for path in paths:
                validate_document(kind, path)
                count += 1
        print("PASS: schema definitions and valid examples checked:", count)
    else:
        if args.kind is None or args.file is None:
            p.error("validate requires --kind and --file")
        validate_document(args.kind, args.file)
        print("PASS:", args.kind, args.file)


if __name__ == "__main__":
    try:
        main()
    except (ValueError, RuntimeError, OSError, json.JSONDecodeError) as exc:
        print("FAIL:", exc, file=sys.stderr)
        sys.exit(1)
