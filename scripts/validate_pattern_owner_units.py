#!/usr/bin/env python3
"""Validate section-level pattern owner units and per-entry coverage evidence.

Checks exactly one owner unit per carded catalog entry, verbatim evidence,
decision-card fields, source records and coverage-state consistency against the
registry. Structural and textual checks only: this is not independent review,
sufficient coverage or technical truth.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from assemble_edition import split
from validate_pattern_registry import (
    EVIDENCE_STATES, SEVERITY, heading_slugs, normalize_alias, slug_heading,
)

ARTIFACT = Path("edition/patterns/owner-units.v1.json")
SCHEMA = Path("schemas/pattern-owner-units.v1.schema.json")
REGISTRY = Path("edition/patterns/registry.v1.json")
BATCHES = Path("edition/patterns/card-batches.v1.json")
LEDGER = Path("edition/patterns/reading-ledger.v1.json")
SOURCE_PLAN = Path("edition/patterns/source-plan.v1.json")
MANIFEST = Path("edition/atlas-manifest.json")
PROMOTIONS = Path("edition/patterns/sufficient-promotions.v1.json")
TICK = chr(96)
HEAD = re.compile(r"^\s{0,3}(#{1,6})\s+(.+?)\s*$")
FENCE = re.compile(r"^\s*(?:" + TICK + r"{3,}|~{3,})[^\r\n]*$")
CARD_MARKERS = (
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
STATES = ("supported", "partial", "absent")
COVERAGE_STATES = EVIDENCE_STATES + ("sufficient",)
DIMENSIONS = ("mechanism", "invariant", "failure_recovery", "alternative")


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
            "Install validation dependencies: python3 -m pip install "
            "-r requirements-validation.txt") from exc
    return Draft202012Validator, FormatChecker


def squash(value):
    return " ".join(value.split())


def sections(text):
    """Return (level, heading, anchor, line, body) for each Markdown section."""
    lines = text.splitlines()
    start = 0
    if lines and lines[0].strip() == "---":
        for index in range(1, len(lines)):
            if lines[index].strip() == "---":
                start = index + 1
                break
    result = []
    current = None
    buffer = []
    fenced = False
    for number, line in enumerate(lines[start:], start + 1):
        if FENCE.match(line):
            fenced = not fenced
            buffer.append(line)
            continue
        match = HEAD.match(line) if not fenced else None
        if match:
            if current is not None:
                result.append((current[0], current[1],
                               slug_heading(current[1]), current[2],
                               "\n".join(buffer)))
            current = (len(match.group(1)), match.group(2).strip(), number)
            buffer = []
        else:
            buffer.append(line)
    if current is not None:
        result.append((current[0], current[1], slug_heading(current[1]),
                       current[2], "\n".join(buffer)))
    return result


def section_body(page_text, heading, level, line):
    """Body of a section, including nested subsections, up to the next peer."""
    found = [item for item in sections(page_text)
             if item[1] == heading and item[0] == level and item[3] == line]
    require(len(found) == 1, "owner-units-unit-ambiguous: " + heading)
    lines = page_text.splitlines()
    start = line
    end = len(lines)
    fenced = False
    for number in range(start, len(lines)):
        entry = lines[number]
        if FENCE.match(entry):
            fenced = not fenced
            continue
        match = HEAD.match(entry) if not fenced else None
        if match and len(match.group(1)) <= level:
            end = number
            break
    return "\n".join(lines[start:end])


def card_section_text(chapter_text, slug):
    _, body = split(chapter_text)
    lines = body.splitlines()
    start = None
    for index, line in enumerate(lines):
        if line.startswith("### ") and slug_heading(line[4:].strip()) == slug:
            start = index + 1
            break
    require(start is not None, "owner-units-card-section: " + slug)
    end = len(lines)
    for index in range(start, len(lines)):
        if lines[index].startswith("### ") or lines[index].startswith("## "):
            end = index
            break
    return "\n".join(lines[start:end])


def card_field(text, label):
    match = re.search(r"\*\*" + label + r"\.\*\*\s*(.+?)(?:\n\n|\Z)", text, re.S)
    require(match is not None, "owner-units-card-field: " + label)
    return squash(match.group(1))


def card_state(text):
    line = next((item for item in text.splitlines()
                 if item.startswith("**Decision state.**")), None)
    require(line is not None, "owner-units-card-state")
    value = line[len("**Decision state.**"):].strip().rstrip(".").strip()
    value = value.replace(TICK, "").strip()
    require(value, "owner-units-card-state-empty")
    return value


def expected_coverage(evidence, pattern_id, promotion=None):
    for name in DIMENSIONS:
        require(evidence[name]["state"] in STATES,
                "owner-units-dimension-state: " + pattern_id + ": " + name)
    require(evidence["mechanism"]["state"] != "absent",
            "owner-units-name-only: " + pattern_id)
    if promotion and all(evidence[name]["state"] == "supported"
                         for name in DIMENSIONS):
        return "sufficient"
    return ("partial-bounded"
            if (evidence["mechanism"]["state"] == "supported"
                and evidence["invariant"]["state"] == "supported")
            else "partial")


def check_binding(entry, name, binding, plan_units, records):
    pattern_id = entry["pattern_id"]
    unit = plan_units.get(binding["source_id"])
    require(unit is not None,
            "owner-units-binding-source: " + pattern_id + ": " + name)
    require(unit.get("read_record_id") == binding["ledger_record"],
            "owner-units-binding-record: " + pattern_id + ": " + name)
    record = records.get(binding["ledger_record"])
    require(record is not None,
            "owner-units-binding-record-missing: " + pattern_id + ": " + name)
    require(record["status"] == "read",
            "owner-units-binding-record-status: " + pattern_id + ": " + name)
    require(record["source_id"] == binding["source_id"],
            "owner-units-binding-record-source: " + pattern_id + ": " + name)
    require(binding["section"] in record.get("sections_read", []),
            "owner-units-binding-section: " + pattern_id + ": " + name)
    require(binding["revision"] == record.get("content_sha256"),
            "owner-units-binding-revision: " + pattern_id + ": " + name)


def expected_overall(technical, decision):
    if technical == "not-applicable" and decision == "not-applicable":
        return "not-applicable"
    if technical == "not-applicable":
        return decision
    if decision == "not-applicable":
        return technical
    return technical if SEVERITY[technical] >= SEVERITY[decision] else decision


def validate_data(data, root=ROOT):
    root = Path(root).resolve()
    Draft, Format = engine()
    schema = load(root / SCHEMA)
    Draft.check_schema(schema)
    errors = sorted(Draft(schema, format_checker=Format()).iter_errors(data),
                    key=lambda error: (list(map(str, error.path)), error.message))
    if errors:
        first = errors[0]
        path = "/".join(map(str, first.path)) or "(root)"
        raise ValueError("owner-units-schema: " + str(len(errors)) +
                         " error(s), first at " + path + ": " + first.message)

    registry = load(root / REGISTRY)
    batches = load(root / BATCHES)
    ledger = load(root / LEDGER)
    source_plan = load(root / SOURCE_PLAN)
    plan_units = {item["pattern_id"]: {
        unit["source_id"]: unit for unit in item["required_units"]}
        for item in source_plan["entries"]}
    manifest = load(root / MANIFEST)
    promotion_data = load(root / PROMOTIONS)
    promotions = {item["pattern_id"]: item
                  for item in promotion_data["promotions"]}
    patterns = {item["id"]: item for item in registry["patterns"]}
    records = {item["id"]: item for item in ledger["records"]}
    chapters = {item["code"]: item for item in manifest["chapters"]}
    cards = {}
    for batch in batches["batches"]:
        chapter = chapters[batch["chapter"]]
        chapter_text = (root / chapter["path"]).read_text(encoding="utf-8")
        for entry in batch["entries"]:
            cards[entry["pattern_id"]] = (chapter, entry, chapter_text)

    entries = data["entries"]
    require(len(entries) == 145, "owner-units-entry-count")
    seen = set()
    page_cache = {}
    by_page = {}
    units = {}
    for item in entries:
        pattern_id = item["pattern_id"]
        require(pattern_id in patterns, "owner-units-unknown-pattern: " + pattern_id)
        require(pattern_id in cards, "owner-units-uncarded: " + pattern_id)
        require(pattern_id not in seen, "owner-units-duplicate-pattern: " + pattern_id)
        seen.add(pattern_id)
        pattern = patterns[pattern_id]
        chapter, card, chapter_text = cards[pattern_id]
        owner = item["owner"]
        technical = pattern["technical_owner"]
        require(owner["path"] == technical["path"],
                "owner-units-owner-path: " + pattern_id)
        require(owner["document_id"] == technical["document_id"],
                "owner-units-owner-document: " + pattern_id)
        require(owner["anchor"] == technical["anchor"],
                "owner-units-owner-anchor: " + pattern_id)
        require(item["technical_coverage"] in COVERAGE_STATES,
                "owner-units-coverage-state: " + pattern_id)
        require(item["decision_coverage"] in COVERAGE_STATES,
                "owner-units-decision-state: " + pattern_id)
        require(item["review_state"] in ("self-checked", "independent-reviewed"),
                "owner-units-review-state: " + pattern_id)
        if item["review_state"] == "independent-reviewed":
            require(registry["review"]["independent_review"] is True,
                    "owner-units-reviewed-without-record: " + pattern_id)

        page = root / owner["path"]
        require(page.is_file() and not page.is_symlink(),
                "owner-units-owner-file: " + pattern_id)
        if owner["path"] not in page_cache:
            page_cache[owner["path"]] = page.read_text(encoding="utf-8")
        page_text = page_cache[owner["path"]]
        body = section_body(page_text, owner["heading"], owner["level"],
                            owner["line"])
        require(owner["anchor"] == slug_heading(owner["heading"])
                or owner["anchor"] in heading_slugs(page),
                "owner-units-anchor-slug: " + pattern_id)
        require(owner["anchor"] in heading_slugs(page),
                "owner-units-anchor-missing: " + pattern_id)
        require(len(body.split()) >= 20, "owner-units-unit-too-short: " + pattern_id)
        require(1 <= len(owner["unit_terms"]) <= 4,
                "owner-units-term-count: " + pattern_id)
        haystack = squash(owner["heading"] + " " + body).lower()
        for term in owner["unit_terms"]:
            require(squash(term).lower() in haystack,
                    "owner-units-term-missing: " + pattern_id + ": " + term)
        heading_key = normalize_alias(owner["heading"])
        named = any(normalize_alias(label) in heading_key
                    for label in [pattern["catalog_name"], *pattern["aliases"]])
        if owner["unit_kind"] == "dedicated":
            require(named, "owner-units-dedicated-heading: " + pattern_id)

        evidence = item["technical_evidence"]
        flat = squash(body).lower()
        for name in DIMENSIONS:
            record = evidence[name]
            require(record["state"] in STATES,
                    "owner-units-dimension-state: " + pattern_id + ": " + name)
            quote = squash(record.get("quote", ""))
            if record["state"] == "supported":
                require(len(quote) >= 30,
                        "owner-units-quote-missing: " + pattern_id + ": " + name)
                require(quote.lower() in flat,
                        "owner-units-quote-not-verbatim: " + pattern_id + ": " + name)
                require(record.get("reason", "").strip(),
                        "owner-units-reason-missing-supported: " + pattern_id + ": " + name)
            else:
                if record["state"] == "absent":
                    require(record.get("reason", "").strip(),
                            "owner-units-reason-missing: " + pattern_id + ": " + name)
                if quote:
                    require(quote.lower() in flat,
                            "owner-units-quote-not-verbatim: " + pattern_id + ": " + name)
        promotion = promotions.get(pattern_id)
        if promotion:
            require(promotion["technical"] == "pass"
                    and promotion["decision"] == "pass",
                    "owner-units-promotion-not-pass: " + pattern_id)
            require(promotion["owner_page_sha256"]
                    == hashlib.sha256(page.read_bytes()).hexdigest(),
                    "owner-units-promotion-owner-hash: " + pattern_id)
            require(promotion["card_sha256"]
                    == hashlib.sha256((root / chapter["path"]).read_bytes()).hexdigest(),
                    "owner-units-promotion-card-hash: " + pattern_id)
        for name in DIMENSIONS:
            record = evidence[name]
            binding = record.get("binding")
            if binding:
                check_binding(item, name, binding,
                              plan_units.get(pattern_id, {}), records)
            if (item["technical_coverage"] == "sufficient" or promotion):
                require(record["state"] != "supported" or binding,
                        "owner-units-binding-missing: " + pattern_id + ": " + name)
        computed = expected_coverage(evidence, pattern_id, promotion)
        require(item["technical_coverage"] == computed,
                "owner-units-technical-derivation: " + pattern_id)
        if item["technical_coverage"] == "sufficient" and not promotion:
            raise ValueError("owner-units-sufficient-without-promotion: " + pattern_id)

        decision = item["decision_evidence"]
        require(decision["atlas_section"] == pattern["atlas_section"],
                "owner-units-atlas-section: " + pattern_id)
        require(decision["atlas_section"] == card["atlas_section"],
                "owner-units-card-section-id: " + pattern_id)
        card_text = card_section_text(chapter_text, card["atlas_section"])
        require(decision["question"] == card_field(card_text, "Decision question"),
                "owner-units-question: " + pattern_id)
        require(decision["competing_alternative"]
                == card_field(card_text, "Competing alternative"),
                "owner-units-alternative: " + pattern_id)
        require(decision["decision_state"] == card_state(card_text),
                "owner-units-decision-state-value: " + pattern_id)
        present = sum(1 for marker in CARD_MARKERS if marker in card_text)
        present += 1 if "**Identity.**" in card_text else 0
        require(decision["card_components"] == present == 10,
                "owner-units-card-components: " + pattern_id)
        require(TICK + "sufficient" + TICK not in card_text,
                "owner-units-card-sufficient-claim: " + pattern_id)

        support = item["source_support"]
        require(support["ledger_record"] == card["ledger_record"],
                "owner-units-ledger-record: " + pattern_id)
        record = records.get(support["ledger_record"])
        require(record is not None, "owner-units-ledger-missing: " + pattern_id)
        require(record["status"] == "read", "owner-units-ledger-status: " + pattern_id)
        require(record["source_id"] == support["source_id"],
                "owner-units-ledger-source: " + pattern_id)
        require(record["unit_type"] == support["unit_type"],
                "owner-units-ledger-unit-type: " + pattern_id)
        require(card["ledger_record"] in card_text,
                "owner-units-ledger-not-cited: " + pattern_id)
        require(record["source_id"] in card_text,
                "owner-units-source-not-cited: " + pattern_id)
        require(support["status"] == "read", "owner-units-source-status: " + pattern_id)
        require(support["card_citation"] is True,
                "owner-units-card-citation: " + pattern_id)

        computed_decision = "sufficient" if promotion else "partial-bounded"
        require(item["decision_coverage"] == computed_decision,
                "owner-units-decision-derivation: " + pattern_id)
        if item["decision_coverage"] == "sufficient" and not promotion:
            raise ValueError("owner-units-sufficient-without-promotion: " + pattern_id)

        coverage = pattern["coverage"]
        require(coverage["technical"] == item["technical_coverage"],
                "owner-units-registry-technical: " + pattern_id)
        require(coverage["decision"] == item["decision_coverage"],
                "owner-units-registry-decision: " + pattern_id)
        require(coverage["overall"]
                == expected_overall(coverage["technical"], coverage["decision"]),
                "owner-units-registry-overall: " + pattern_id)
        require(technical["state"] == coverage["technical"],
                "owner-units-registry-owner-state: " + pattern_id)
        require(pattern["atlas_owner"]["state"] == coverage["decision"],
                "owner-units-registry-atlas-state: " + pattern_id)
        require(item["catalog_name"] == pattern["catalog_name"],
                "owner-units-catalog-name: " + pattern_id)
        require(item["family"] == pattern["family"],
                "owner-units-family: " + pattern_id)

        unit_key = (owner["path"], owner["anchor"])
        unit = units.setdefault(unit_key, {"kinds": set(), "patterns": []})
        unit["kinds"].add(owner["unit_kind"])
        unit["patterns"].append(pattern_id)
        by_page.setdefault(owner["path"], []).append(item)

    require(seen == set(cards), "owner-units-card-partition")

    expected_shared = {path: sorted(item["pattern_id"] for item in items)
                       for path, items in by_page.items() if len(items) > 1}
    require(len(expected_shared) == 33, "owner-units-shared-page-count")
    shared = data["shared_pages"]
    require(len(shared) == 33, "owner-units-shared-list")
    seen_pages = set()
    decisions = {"keep": 0, "deepen": 0, "split": 0}
    for page in shared:
        path = page["path"]
        require(path in expected_shared, "owner-units-shared-unknown: " + path)
        require(path not in seen_pages, "owner-units-shared-duplicate: " + path)
        seen_pages.add(path)
        require(sorted(page["pattern_ids"]) == expected_shared[path],
                "owner-units-shared-patterns: " + path)
        require(page["pattern_count"] == len(expected_shared[path]),
                "owner-units-shared-count: " + path)
        items = by_page[path]
        require(page["document_id"] == items[0]["owner"]["document_id"],
                "owner-units-shared-document: " + path)
        page_units = {item["owner"]["anchor"] for item in items}
        require(page["unit_count"] == len(page_units),
                "owner-units-shared-units: " + path)
        dedicated = {item["owner"]["anchor"] for item in items
                     if item["owner"]["unit_kind"] == "dedicated"}
        require(page["dedicated_units"] == len(dedicated),
                "owner-units-shared-dedicated: " + path)
        bounded = sum(1 for item in items
                      if item["technical_coverage"] == "partial-bounded")
        require(page["bounded_entries"] == bounded,
                "owner-units-shared-bounded: " + path)
        require(page["decision"] in decisions,
                "owner-units-shared-decision: " + path)
        decisions[page["decision"]] += 1
    require(seen_pages == set(expected_shared), "owner-units-shared-partition")

    deferrals = data["split_deferrals"]
    split_pages = {page["path"]: page for page in shared if page["decision"] == "split"}
    require(len(deferrals) == len(split_pages) == 0, "owner-units-split-deferral-count")
    seen_deferrals = set()
    for item in deferrals:
        path = item["path"]
        require(path in split_pages, "owner-units-split-deferral-page: " + path)
        require(path not in seen_deferrals, "owner-units-split-deferral-duplicate: " + path)
        seen_deferrals.add(path)
        require(item["document_id"] == split_pages[path]["document_id"],
                "owner-units-split-deferral-document: " + path)
        require(item["pattern_ids"] == split_pages[path]["pattern_ids"],
                "owner-units-split-deferral-patterns: " + path)
        require(item["decision"] == "deferred",
                "owner-units-split-deferral-decision: " + path)
        require(len(item["gate"]) >= 40,
                "owner-units-split-deferral-gate: " + path)
    require(seen_deferrals == set(split_pages), "owner-units-split-deferral-partition")

    summary = data["summary"]
    counts = {
        "entries": len(entries),
        "owner_pages": len(by_page),
        "shared_pages": len(shared),
        "owner_units": len(units),
        "dedicated_units": sum(1 for value in units.values()
                               if "dedicated" in value["kinds"]),
        "embedded_units": sum(1 for value in units.values()
                              if "dedicated" not in value["kinds"]),
        "mechanism_supported": sum(1 for item in entries
                                   if item["technical_evidence"]["mechanism"]["state"] == "supported"),
        "invariant_supported": sum(1 for item in entries
                                   if item["technical_evidence"]["invariant"]["state"] == "supported"),
        "failure_recovery_supported": sum(1 for item in entries
                                          if item["technical_evidence"]["failure_recovery"]["state"] == "supported"),
        "alternative_supported": sum(1 for item in entries
                                     if item["technical_evidence"]["alternative"]["state"] == "supported"),
        "technical_partial_bounded": sum(1 for item in entries
                                         if item["technical_coverage"] == "partial-bounded"),
        "technical_partial": sum(1 for item in entries
                                 if item["technical_coverage"] == "partial"),
        "technical_name_only": sum(1 for item in entries
                                   if item["technical_coverage"] == "name-only"),
        "technical_sufficient": sum(1 for item in entries
                                    if item["technical_coverage"] == "sufficient"),
        "decision_partial_bounded": sum(1 for item in entries
                                        if item["decision_coverage"] == "partial-bounded"),
        "decision_partial": sum(1 for item in entries
                                if item["decision_coverage"] == "partial"),
        "decision_name_only": sum(1 for item in entries
                                  if item["decision_coverage"] == "name-only"),
        "decision_sufficient": sum(1 for item in entries
                                   if item["decision_coverage"] == "sufficient"),
        "partial_reviewed": sum(1 for item in entries
                                if "partial-reviewed" in (item["technical_coverage"],
                                                          item["decision_coverage"])),
        "independent_reviews": sum(1 for item in entries
                                   if item["review_state"] == "independent-reviewed"),
        "shared_page_decisions": decisions,
        "split_deferred": len(deferrals),
    }
    require(summary == counts, "owner-units-summary-mismatch")
    require(counts["technical_name_only"] == 0, "owner-units-name-only-remaining")
    require(counts["technical_sufficient"] == len(promotions),
            "owner-units-sufficient-technical")
    require(counts["decision_sufficient"] == len(promotions),
            "owner-units-sufficient-decision")
    require(counts["partial_reviewed"] == 0, "owner-units-reviewed-claim")
    require(counts["independent_reviews"] == 0, "owner-units-independent-review-claim")

    return {"entries": counts["entries"], "owner_pages": counts["owner_pages"],
            "units": counts["owner_units"], "shared_pages": counts["shared_pages"],
            "bounded": counts["technical_partial_bounded"],
            "partial": counts["technical_partial"],
            "decisions": decisions,
            "scope": "section-level ownership evidence; not independent review"}


def validate(root=ROOT):
    root = Path(root).resolve()
    return validate_data(load(root / ARTIFACT), root)


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
        print("PASS: owner units", result["entries"], "entries,",
              result["units"], "units,", result["shared_pages"], "shared pages")
    return 0


if __name__ == "__main__":
    sys.exit(main())
