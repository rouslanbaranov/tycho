#!/usr/bin/env python3
"""Validate authored pattern-card batches and exact owner/backlink bindings."""
import argparse
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from assemble_edition import split
from validate_pattern_registry import EVIDENCE_STATES, heading_slugs, slug_heading

SCHEMA = Path("schemas/pattern-card-batches.v1.schema.json")
BATCHES = Path("edition/patterns/card-batches.v1.json")
REGISTRY = Path("edition/patterns/registry.v1.json")
LEDGER = Path("edition/patterns/reading-ledger.v1.json")
MANIFEST = Path("edition/atlas-manifest.json")
MARKERS = (
    "**Decision question.**",
    "**Good-fit conditions.**",
    "**Hard contraindications.**",
    "**Competing alternative.**",
    "**Failure and recovery.**",
    "**Technical owner.**",
    "**Sources.**",
    "**Decision state.**",
    "**Related entries.**",
)


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


def check_card_text(text, slug):
    for marker in MARKERS:
        require(marker in text, "card-marker-missing: " + slug + ": " + marker)
    require("`sufficient`" not in text, "card-sufficient-claim: " + slug)
    decision_line = next((line for line in text.splitlines()
                          if line.startswith("**Decision state.**")), "")
    require(any(state in decision_line for state in (
        "applicable-under-conditions", "candidate", "contraindicated",
        "insufficient-evidence", "not-required")), "card-decision-state: " + slug)


def check_owner_link(text, chapter_path, owner_path, owner_anchor, root=ROOT):
    line = next((item for item in text.splitlines()
                 if item.startswith("**Technical owner.**")), None)
    require(line is not None, "card-owner-link-missing")
    match = re.search(r"\]\(([^)]+)\)", line)
    require(match is not None, "card-owner-link-missing")
    target = match.group(1)
    path, separator, anchor = target.partition("#")
    require(separator and anchor == owner_anchor, "card-owner-link-anchor")
    resolved = (Path(root) / Path(chapter_path).parent / path).resolve()
    expected = (Path(root) / owner_path).resolve()
    require(resolved == expected, "card-owner-link-path")


def check_backlink(owner_text, chapter_path, slug):
    marker = chapter_path.split("book/volumes/", 1)[-1] + "#" + slug
    # GitHub keeps the extra separator when a heading contains " / ".
    normalized = owner_text.replace("--", "-")
    require(marker in owner_text or marker in normalized,
            "card-backlink-missing: " + slug)


def section_text(body, slug):
    lines = body.splitlines()
    start = None
    for index, line in enumerate(lines):
        if any(line.startswith(prefix) and heading_slugs_text(line[len(prefix):]) == slug
               for prefix in ("### ", "## ", "# ")):
            start = index + 1
            break
    if start is None:
        return None
    end = len(lines)
    for index in range(start, len(lines)):
        if any(lines[index].startswith(prefix) for prefix in ("### ", "## ", "# ")):
            end = index
            break
    return "\n".join(lines[start:end])


def heading_slugs_text(text):
    return slug_heading(text.strip())


def validate_data(data, root=ROOT):
    root = Path(root).resolve()
    Draft, Format = engine()
    schema = load(root / SCHEMA)
    Draft.check_schema(schema)
    validator = Draft(schema, format_checker=Format())
    errors = sorted(validator.iter_errors(data), key=lambda error: (list(map(str, error.path)), error.message))
    if errors:
        first = errors[0]
        path = "/".join(map(str, first.path)) or "(root)"
        raise ValueError("card-batches-schema: " + str(len(errors)) + " error(s), first at " + path + ": " + first.message)

    registry = load(root / REGISTRY)
    manifest = load(root / MANIFEST)
    ledger = load(root / LEDGER)
    by_pattern = {item["id"]: item for item in registry["patterns"]}
    families = {item["id"]: item for item in registry["families"]}
    chapters = {item["code"]: item for item in manifest["chapters"]}
    records = {item["id"]: item for item in ledger["records"]}
    seen = set()
    count = 0
    for batch in data["batches"]:
        require(batch["chapter"] in chapters, "card-batch-chapter-missing: " + batch["chapter"])
        chapter = chapters[batch["chapter"]]
        family = families[chapter["family"]]
        chapter_path = root / chapter["path"]
        require(chapter_path.is_file(), "card-batch-chapter-file: " + chapter["path"])
        _, body = split(chapter_path.read_text(encoding="utf-8"))
        chapter_anchors = heading_slugs(chapter_path)
        for entry in batch["entries"]:
            pattern_id = entry["pattern_id"]
            require(pattern_id in by_pattern, "card-pattern-unknown: " + pattern_id)
            pattern = by_pattern[pattern_id]
            require(pattern_id not in seen, "card-pattern-duplicate: " + pattern_id)
            seen.add(pattern_id)
            require(pattern_id in family["pattern_ids"], "card-pattern-family: " + pattern_id)
            require(pattern["atlas_section"] == entry["atlas_section"], "card-anchor-mismatch: " + pattern_id)
            card_path = entry.get("card_path", chapter["path"])
            card_file = root / card_path
            require(card_file.is_file(), "card-file-missing: " + card_path)
            card_anchors = heading_slugs(card_file)
            require(entry["atlas_section"] in card_anchors,
                    "card-anchor-missing: " + entry["atlas_section"])
            _, body = split(card_file.read_text(encoding="utf-8"))
            text = section_text(body, entry["atlas_section"])
            require(text is not None, "card-section-missing: " + entry["atlas_section"])
            check_card_text(text, entry["atlas_section"])
            record = records.get(entry["ledger_record"])
            require(record is not None, "card-ledger-missing: " + entry["ledger_record"])
            require(record["status"] == "read", "card-ledger-not-read: " + entry["ledger_record"])
            require(entry["ledger_record"] in text, "card-ledger-not-cited: " + entry["atlas_section"])
            require(record["source_id"] in text, "card-source-not-cited: " + entry["atlas_section"])
            if entry["owner_state"] == "linked":
                owner = root / entry["owner_path"]
                require(owner.is_file() and not owner.is_symlink(), "card-owner-file: " + entry["owner_path"])
                require(entry["owner_anchor"] in heading_slugs(owner), "card-owner-anchor: " + entry["owner_anchor"])
                owner_text = owner.read_text(encoding="utf-8")
                check_backlink(owner_text, card_path, entry["atlas_section"])
                require(pattern["technical_owner"]["path"] == entry["owner_path"], "card-registry-owner-path: " + pattern_id)
                require(pattern["technical_owner"]["anchor"] == entry["owner_anchor"], "card-registry-owner-anchor: " + pattern_id)
                require(pattern["technical_owner"]["state"] in EVIDENCE_STATES,
                        "card-registry-owner-state: " + pattern_id)
                check_owner_link(text, card_path, entry["owner_path"], entry["owner_anchor"], root)
                require(pattern["coverage"]["technical"] in EVIDENCE_STATES,
                        "card-registry-technical: " + pattern_id)
                require(pattern["coverage"]["overall"] in EVIDENCE_STATES,
                        "card-registry-coverage: " + pattern_id)
            else:
                issue = str(entry["remediation_issue"])
                require("technical-owner-missing" in text, "card-missing-owner-marker: " + entry["atlas_section"])
                require("#" + issue in text, "card-remediation-not-cited: " + entry["atlas_section"])
                require(pattern["technical_owner"]["state"] == "missing", "card-registry-owner-state: " + pattern_id)
                require(pattern["technical_owner"]["path"] is None, "card-registry-owner-path: " + pattern_id)
                require(pattern["technical_owner"]["anchor"] is None, "card-registry-owner-anchor: " + pattern_id)
                require(pattern["coverage"]["technical"] == "missing", "card-registry-technical: " + pattern_id)
                require(pattern["coverage"]["overall"] == "missing", "card-registry-coverage: " + pattern_id)
            require(pattern["coverage"]["decision"] in EVIDENCE_STATES,
                    "card-registry-decision: " + pattern_id)
            require(pattern["review_status"] == "self-checked", "card-registry-review: " + pattern_id)
            count += 1
    return {
        "batches": len(data["batches"]),
        "entries": count,
        "scope": "card structure, exact anchors, ledger citations and registry state; not independent review",
    }


def validate(root=ROOT):
    root = Path(root).resolve()
    return validate_data(load(root / BATCHES), root)


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
        print("PASS: pattern cards", result["batches"], "batch(es),", result["entries"], "entries")
    return 0


if __name__ == "__main__":
    sys.exit(main())
