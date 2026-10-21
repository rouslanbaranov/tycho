#!/usr/bin/env python3
"""Validate the candidate coverage and reverse maps.

Candidate areas and pages are routing hypotheses. This validates references and
counts only; it does not establish page coverage, source support or technical truth.
"""
import argparse
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
COVERAGE = Path("edition/patterns/coverage-map.v1.json")
REVERSE = Path("edition/patterns/reverse-map.v1.json")
REGISTRY = Path("edition/patterns/registry.v1.json")
ROUTE = Path("generated/route-index.v1.json")
OUTLINE = Path("edition/outline.json")
CONFIDENCE = {"strong", "medium", "weak"}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def validate_data(coverage, reverse, root=ROOT):
    root = Path(root).resolve()
    registry = load(root / REGISTRY)
    route = load(root / ROUTE)
    outline = load(root / OUTLINE)
    patterns = {item["id"]: item for item in registry["patterns"]}
    documents = {item["id"]: item for item in route["documents"]}
    chapters = {item["code"]: item for item in outline["chapters"]}

    require(coverage["schema_version"] == 1, "coverage-schema-version")
    require(coverage["status"] == "candidate-only", "coverage-status")
    require(coverage["registry_version"] == registry["registry_version"],
            "coverage-registry-version")
    require(coverage["registry_sha256"] == hashlib.sha256(
        (root / REGISTRY).read_bytes()).hexdigest(), "coverage-registry-hash")
    require(coverage["route_index_snapshot"] == route["snapshot_sha256"],
            "coverage-route-snapshot")
    entries = coverage["entries"]
    require(len(entries) == 145, "coverage-entry-count")
    seen = set()
    reverse_expected = {}
    for entry in entries:
        pattern_id = entry["pattern_id"]
        require(pattern_id in patterns, "coverage-unknown-pattern: " + pattern_id)
        require(pattern_id not in seen, "coverage-duplicate-pattern: " + pattern_id)
        seen.add(pattern_id)
        area = entry["candidate_area"]
        require(area["chapter"] in chapters, "coverage-area-chapter")
        chapter = chapters[area["chapter"]]
        require(area["document_id"] == chapter["id"], "coverage-area-id")
        require(area["path"] == chapter["path"], "coverage-area-path")
        require(documents.get(area["document_id"], {}).get("kind") == "chapter",
                "coverage-area-document")
        require(entry["technical_state"] == "not-yet-assessed", "coverage-technical-state")
        require(entry["decision_state"] == "not-yet-assessed", "coverage-decision-state")
        require(entry["dimensions_state"] == "not-yet-assessed", "coverage-dimension-state")
        pages = entry["candidate_pages"]
        require(len(pages) <= 2, "coverage-page-count")
        page_paths = set()
        for page in pages:
            require(page["confidence"] in CONFIDENCE, "coverage-confidence")
            require(page["document_id"] in documents, "coverage-unknown-page")
            doc = documents[page["document_id"]]
            require(doc["kind"] == "page", "coverage-page-kind")
            require(page["path"] == doc["path"], "coverage-page-path")
            require(page["path"] not in page_paths, "coverage-duplicate-page")
            page_paths.add(page["path"])
            require("v11-pattern-atlas" not in page["path"], "coverage-atlas-self-owner")
            if page["confidence"] in ("strong", "medium"):
                reverse_expected.setdefault(page["document_id"], {
                    "document_id": page["document_id"],
                    "path": doc["path"],
                    "title": doc["title"],
                    "pattern_ids": [],
                })["pattern_ids"].append(pattern_id)
    require(seen == set(patterns), "coverage-pattern-partition")

    summary = coverage["summary"]
    require(summary["entries"] == 145, "coverage-summary-entries")
    require(summary["entries_with_any_candidate"] == sum(bool(e["candidate_pages"]) for e in entries),
            "coverage-summary-any")
    require(summary["entries_with_strong_or_medium"] == sum(
        any(p["confidence"] in ("strong", "medium") for p in e["candidate_pages"])
        for e in entries), "coverage-summary-strong-medium")
    require(summary["entries_without_strong_or_medium"] == sum(
        not any(p["confidence"] in ("strong", "medium") for p in e["candidate_pages"])
        for e in entries), "coverage-summary-without")
    require(summary["by_confidence"] == {
        level: sum(1 for e in entries for p in e["candidate_pages"] if p["confidence"] == level)
        for level in ("strong", "medium", "weak")}, "coverage-summary-confidence")
    require(summary["reverse_documents"] == len(reverse_expected), "coverage-summary-reverse")

    require(reverse["schema_version"] == 1, "reverse-schema-version")
    require(reverse["route_index_snapshot"] == route["snapshot_sha256"], "reverse-route-snapshot")
    actual = {}
    for item in reverse["documents"]:
        require(item["document_id"] in documents, "reverse-unknown-document")
        require(documents[item["document_id"]]["path"] == item["path"], "reverse-path")
        require(item["pattern_ids"] and len(item["pattern_ids"]) == len(set(item["pattern_ids"])),
                "reverse-pattern-list")
        require(set(item["pattern_ids"]) <= set(patterns), "reverse-unknown-pattern")
        actual[item["document_id"]] = {
            "document_id": item["document_id"],
            "path": item["path"],
            "title": item["title"],
            "pattern_ids": sorted(item["pattern_ids"]),
        }
    expected = {key: {**value, "pattern_ids": sorted(value["pattern_ids"])}
                for key, value in reverse_expected.items()}
    require(actual == expected, "reverse-map-mismatch")

    return {
        "entries": len(entries),
        "candidate_pages": sum(len(e["candidate_pages"]) for e in entries),
        "strong_or_medium": summary["entries_with_strong_or_medium"],
        "reverse_documents": len(actual),
        "scope": "candidate routing references; not page audit or source review",
    }


def validate(root=ROOT):
    root = Path(root).resolve()
    return validate_data(load(root / COVERAGE), load(root / REVERSE), root)


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
        print("PASS: coverage", result["entries"], "entries,",
              result["reverse_documents"], "reverse documents")
    return 0


if __name__ == "__main__":
    sys.exit(main())
