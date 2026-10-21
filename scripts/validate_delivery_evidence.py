#!/usr/bin/env python3
"""Validate Phase 5 delivery evidence against current counts and nonclaims."""
import argparse
from collections import Counter
import json
from pathlib import Path
import subprocess
import sys

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
    schema = load(root / "schemas/pattern-delivery-evidence.v1.schema.json")
    Draft.check_schema(schema)
    errors = sorted(Draft(schema, format_checker=Format()).iter_errors(data),
                    key=lambda error: (list(map(str, error.path)), error.message))
    if errors:
        first = errors[0]
        path = "/".join(map(str, first.path)) or "(root)"
        raise ValueError("delivery-schema: " + str(len(errors)) + " error(s), first at " + path + ": " + first.message)
    registry = load(root / "edition/patterns/registry.v1.json")
    owner_units = load(root / "edition/patterns/owner-units.v1.json")
    phase4 = load(root / "edition/patterns/phase4.v1.json")
    semantic = load(root / "edition/patterns/semantic-audit.v1.json")
    ledger = load(root / "edition/patterns/reading-ledger.v1.json")
    sources = load(root / "sources/register.json")
    cards = load(root / "edition/patterns/card-batches.v1.json")
    card_count = sum(len(batch["entries"]) for batch in cards["batches"])
    require(data["summary"]["entries"] == len(registry["patterns"]), "delivery-entry-count")
    require(data["summary"]["cards"] == card_count, "delivery-card-count")
    require(data["summary"]["pages"] == phase4["summary"]["pages"], "delivery-page-count")
    require(data["summary"]["routes"] == phase4["summary"]["routes"], "delivery-route-count")
    require(data["summary"]["unresolved_related"] == phase4["summary"]["unresolved_related"], "delivery-unresolved-count")
    require(data["summary"]["related_labels"] == phase4["summary"]["related_labels"], "delivery-related-count")
    require(data["summary"]["non_routes"] == phase4["summary"]["non_routes"], "delivery-non-route-count")
    require(data["summary"]["retrieval_questions"] == phase4["summary"]["retrieval_questions"], "delivery-question-count")
    require(data["summary"]["semantic_pages"] == semantic["summary"]["pages"], "delivery-semantic-page-count")
    require(data["summary"]["semantic_findings"] == semantic["summary"]["findings"]["total"], "delivery-semantic-finding-count")
    require(data["summary"]["semantic_pages_with_findings"] == semantic["summary"]["pages_with_findings"], "delivery-semantic-finding-pages")
    require(data["summary"]["semantic_open_gates"] == semantic["summary"]["open_gates"], "delivery-semantic-gate-count")
    require(data["summary"]["human_reviews"] == semantic["summary"]["human_reviews"], "delivery-human-review-count")
    require(data["summary"]["independent_reviews"] == semantic["summary"]["independent_reviews"], "delivery-independent-review-count")
    require(data["summary"]["ledger_records"] == len(ledger["records"]), "delivery-ledger-count")
    require(data["summary"]["sources"] == len(sources["sources"]), "delivery-source-count")
    technical = Counter(item["coverage"]["technical"]
                        for item in registry["patterns"])
    decision = Counter(item["coverage"]["decision"]
                       for item in registry["patterns"])
    require(data["summary"]["partial_technical"] == technical["partial"],
            "delivery-technical-partial-count")
    require(data["summary"]["partial_bounded_technical"]
            == technical["partial-bounded"], "delivery-technical-bounded-count")
    require(data["summary"]["partial_reviewed_technical"]
            == technical["partial-reviewed"], "delivery-technical-reviewed-count")
    require(data["summary"]["name_only_technical"] == technical["name-only"],
            "delivery-technical-name-only-count")
    require(data["summary"]["partial_decision"] == decision["partial"],
            "delivery-decision-partial-count")
    require(data["summary"]["partial_bounded_decision"]
            == decision["partial-bounded"], "delivery-decision-bounded-count")
    require(data["summary"]["partial_reviewed_decision"]
            == decision["partial-reviewed"], "delivery-decision-reviewed-count")
    require(data["summary"]["owner_units"]
            == owner_units["summary"]["owner_units"], "delivery-owner-unit-count")
    require(data["summary"]["shared_pages"]
            == len(owner_units["shared_pages"]), "delivery-shared-page-count")
    require(data["summary"]["sufficient_technical"] == 0, "delivery-sufficient-technical")
    require(data["summary"]["sufficient_decision"] == 0, "delivery-sufficient-decision")
    dod = {item["id"]: item for item in data["dod"]}
    require(dod.get("independent-editorial-review", {}).get("status") == "met",
            "delivery-human-review-missing")
    require(dod.get("owner-acceptance", {}).get("status") != "met",
            "delivery-owner-acceptance-claim")
    require(dod.get("technical-sufficiency", {}).get("status") != "met",
            "delivery-technical-sufficiency-claim")
    require(dod.get("decision-sufficiency", {}).get("status") != "met",
            "delivery-decision-sufficiency-claim")
    require(data["status"] != "reviewed", "delivery-reviewed-claim")
    require(len(data["source_commit_note"]) >= 40, "delivery-source-commit-note")
    head = subprocess.check_output(["git", "-C", str(root), "rev-parse", "HEAD"], text=True).strip()
    ancestor = subprocess.run(["git", "-C", str(root), "merge-base", "--is-ancestor",
                               data["source_commit"], head], capture_output=True).returncode == 0
    require(ancestor, "delivery-source-commit-not-ancestor")
    return {"entries": data["summary"]["entries"], "cards": data["summary"]["cards"],
            "gaps": len(data["open_gaps"]), "checks": len(data["checks"])}


def validate(root=ROOT):
    return validate_data(load(Path(root) / "edition/patterns/delivery-evidence.v1.json"), root)


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
        print("PASS: delivery evidence", result["entries"], "entries,", result["cards"], "cards,",
              result["gaps"], "open gaps")
    return 0


if __name__ == "__main__":
    sys.exit(main())
