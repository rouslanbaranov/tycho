#!/usr/bin/env python3
"""Validate the Phase 4 page/entry audit artifact."""
import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from phase4_audit import ARTIFACT, REGISTRY

ROOT = Path(__file__).resolve().parents[1]


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


def validate_data(data, root=ROOT):
    root = Path(root).resolve()
    Draft, Format = engine()
    schema = load(root / "schemas/pattern-phase4.v1.schema.json")
    Draft.check_schema(schema)
    errors = sorted(Draft(schema, format_checker=Format()).iter_errors(data),
                    key=lambda error: (list(map(str, error.path)), error.message))
    if errors:
        first = errors[0]
        path = "/".join(map(str, first.path)) or "(root)"
        raise ValueError("phase4-schema: " + str(len(errors)) + " error(s), first at " + path + ": " + first.message)
    registry = load(root / REGISTRY)
    ids = {item["id"] for item in registry["patterns"]}
    pages = data["page_dispositions"]
    require(len(pages) == 421, "phase4-page-count")
    require(len({p["path"] for p in pages}) == 421, "phase4-page-duplicate")
    require(len({p["document_id"] for p in pages}) == 421, "phase4-page-id-duplicate")
    audit = data["entry_audit"]
    require(len(audit) == 145, "phase4-entry-count")
    require(len({item["pattern_id"] for item in audit}) == 145, "phase4-entry-duplicate")
    require({item["pattern_id"] for item in audit} == ids, "phase4-entry-membership")
    for item in audit:
        require(len(item["dimensions"]) == 14, "phase4-dimension-count")
        require(set(item["dimensions"]) == set(data["dimensions"]), "phase4-dimension-names")
    matrix = data["gap_matrix"]
    require(len(matrix) == 145, "phase4-gap-count")
    require({item["pattern_id"] for item in matrix} == ids, "phase4-gap-membership")
    routes = data["routes"]
    for route in routes:
        require(route["from"] in ids and route["to"] in ids, "phase4-route-endpoint")
        require(route["from"] != route["to"], "phase4-route-self")
    related = data["related_dispositions"]
    for item in related:
        if item["disposition"] == "mapped":
            require(item["target"] in ids, "phase4-related-target")
        else:
            require(item["target"] is None, "phase4-related-non-route-target")
        require(len(item["reason"]) >= 10, "phase4-related-reason")
    questions = data["retrieval_questions"]
    require(len(questions) == 145, "phase4-question-count")
    require(len({item["pattern_id"] for item in questions}) == 145, "phase4-question-duplicate")
    summary = data["summary"]
    require(summary["pages"] == len(pages), "phase4-summary-pages")
    require(summary["entries"] == len(audit), "phase4-summary-entries")
    require(summary["routes"] == len(routes), "phase4-summary-routes")
    require(summary["retrieval_questions"] == len(questions), "phase4-summary-questions")
    require(summary["blocked_entries"] == 0, "phase4-blocked-count")
    require(summary["related_labels"] == len(related), "phase4-related-count")
    require(summary["non_routes"] == sum(
        1 for item in related if item["disposition"] == "non-route"),
        "phase4-non-route-count")
    require(summary["unresolved_related"] == 0, "phase4-unresolved-count")
    return {"pages": len(pages), "entries": len(audit), "cards": len(questions),
            "routes": len(routes), "non_routes": len(related)}


def validate(root=ROOT):
    return validate_data(load(Path(root) / ARTIFACT), root)


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
        print("PASS: phase4", result["pages"], "pages,", result["entries"], "entries,",
              result["routes"], "routes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
