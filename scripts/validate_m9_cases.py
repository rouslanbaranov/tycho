#!/usr/bin/env python3
"""Deterministic offline validation of M9 draft case collection and portable contracts.

No external requests, no private repositories, no hosted index, no production
MCP/semantic-evaluation claims. Run at repository root:
    python3 scripts/validate_m9_cases.py
    python3 scripts/validate_m9_cases.py --self-test

jsonschema (Draft 2020-12 with format checker) is used when already available;
otherwise the built-in strict-shape validator checks the known portable subset
and reports that a full JSON-Schema-engine check was NOT executed.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASE_DIR = ROOT / "book/cases"
SOURCE_REGISTER = ROOT / "sources/REAL_WORLD_ARCHITECTURE_CASES.md"
PROPOSED_SCHEMA = ROOT / "authoring/cases/case-record.schema.json"
SAMPLES = ROOT / "authoring/cases/examples/case-records.json"
QUERIES = ROOT / "tests/fixtures/m9-case-queries.json"
CID = re.compile(r"^case\.[a-z][a-z0-9-]*\.[a-z][a-z0-9-]*$")
CLAIM_ID = re.compile(r"^claim\.[a-z][a-z0-9-]*\.[a-z][a-z0-9-]*\.[0-9]{3}$")
SOURCE_ID = re.compile(r"^(N|U|A|SH|SP|ST|DI|ME|LI|CF)[0-9]{2}$")
EXPECTED_BEHAVIORS = {"answerable", "reject_false_claim", "insufficient_evidence"}
DATE_FIELDS = ("event_date", "publication_date", "accessed_on")


def fail(msg: str) -> None:
    raise ValueError(msg)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def iso_date(value: object, label: str, nullable: bool = False) -> None:
    if value is None and nullable:
        return
    require(isinstance(value, str), label + ": expected YYYY-MM-DD")
    try:
        dt.date.fromisoformat(value)
    except ValueError:
        fail(label + ": invalid ISO date " + repr(value))


def json_read(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_record(record: dict, schema: dict, registered_sources: set[str]) -> None:
    require(isinstance(record, dict), "case record must be object")
    required = set(schema["required"])
    require(required <= set(record), "missing case keys " + str(sorted(required - set(record))))
    allowed = set(schema["properties"])
    require(set(record) <= allowed, "unknown case keys " + str(sorted(set(record) - allowed)))
    require(record["collection"] == "tycho-public", "case corpus isolation violation")
    require(record["schema_version"] == "m9-case-1.0-proposal", "invalid schema version")
    # Keep the no-dependency fallback faithful to declared JSON Schema types.
    for key, minimum in (("title", 12), ("company", 2), ("legacy_state", 12), ("target_state", 12)):
        require(isinstance(record[key], str) and len(record[key]) >= minimum,
                key + ": expected string of minimum length " + str(minimum))
    require(isinstance(record["case_id"], str) and CID.fullmatch(record["case_id"]) is not None, "invalid case_id")
    require(record["status"] in schema["properties"]["status"]["enum"], "invalid review status")
    require(isinstance(record["source_refs"], list) and len(record["source_refs"]) > 0, "source_refs absent")
    require(all(isinstance(ref, str) and SOURCE_ID.fullmatch(ref) is not None
                for ref in record["source_refs"]), "source ref not a valid string ID")
    require(len(record["source_refs"]) == len(set(record["source_refs"])), "duplicate source ref")
    require(set(record["source_refs"]) <= registered_sources, "unregistered case source")
    require(isinstance(record["claims"], list) and len(record["claims"]) > 0, "case has no claims")
    iso_date(record["observed_on"], "observed_on", nullable=True)
    review = record["review"]
    require(isinstance(review, dict), "review not object")
    require(set(review) == {"reviewer", "reviewed_on", "limitations"}, "invalid review contract")
    iso_date(review["reviewed_on"], "reviewed_on", nullable=True)
    require(review["reviewer"] is None or isinstance(review["reviewer"], str), "reviewer not string/null")
    require(isinstance(review["limitations"], list)
            and all(isinstance(x, str) for x in review["limitations"]), "review limitations not string list")
    pattern = record["patterns"]
    require(isinstance(pattern, dict) and set(pattern) == {"selected", "avoided"}, "invalid patterns")
    require(all(isinstance(pattern[k], list) and all(isinstance(x, str) for x in pattern[k])
                for k in ("selected", "avoided")), "pattern tokens not string arrays")
    for key in ("constraints", "failure_modes"):
        require(isinstance(record[key], list) and all(isinstance(x, str) for x in record[key]),
                key + " must be string list")
    claim_keys = set(schema["$defs"]["claim"]["required"])
    claim_allowed = set(schema["$defs"]["claim"]["properties"])
    seen = set()
    for item in record["claims"]:
        require(isinstance(item, dict), "claim not object")
        require(claim_keys <= set(item), "missing claim keys " + str(sorted(claim_keys - set(item))))
        require(set(item) <= claim_allowed, "unknown claim keys")
        cid = item["claim_id"]
        require(isinstance(cid, str) and CLAIM_ID.fullmatch(cid) is not None, "invalid claim_id")
        require(cid not in seen, "duplicate claim_id")
        seen.add(cid)
        require(cid.startswith(record["case_id"].replace("case.", "claim.") + "."), "claim_id does not belong to case")
        require(isinstance(item["statement"], str) and len(item["statement"]) >= 12,
                "claim statement too short or not string")
        require(isinstance(item["source_ref_id"], str)
                and SOURCE_ID.fullmatch(item["source_ref_id"]) is not None,
                "claim source ID not a valid string")
        require(item["source_ref_id"] in record["source_refs"], "claim source absent from case source_refs")
        require(isinstance(item["primary_url"], str) and item["primary_url"].startswith("https://"), "primary URL not HTTPS")
        require(isinstance(item["source_section"], str) and len(item["source_section"]) > 2, "empty source section")
        require(item["evidence_type"] in schema["$defs"]["claim"]["properties"]["evidence_type"]["enum"], "unknown evidence type")
        require(isinstance(item["qualification"], str) and len(item["qualification"]) >= 10, "no qualification")
        for name in DATE_FIELDS:
            iso_date(item[name], name, nullable=name != "accessed_on")
        window = item["validity_window"]
        require(isinstance(window, dict) and set(window) == {"valid_from", "valid_until"}, "invalid window")
        for k in window:
            iso_date(window[k], k, nullable=True)
        if window["valid_from"] and window["valid_until"]:
            require(window["valid_from"] <= window["valid_until"], "inverted validity window")
        if "metric" in item:
            metric = item["metric"]
            require(isinstance(metric, dict) and set(metric) == {"value", "unit", "comparison", "workload"}, "invalid metric")
            require(isinstance(metric["value"], (int, float)) and not isinstance(metric["value"], bool), "metric not numeric")
            require(all(isinstance(metric[k], str) and metric[k] for k in ("unit", "comparison", "workload")), "unbounded metric")


def validate_fixtures(fixtures: dict, case_ids: set[str], source_ids: set[str]) -> dict:
    require(fixtures["collection"] == "tycho-public", "fixture public-corpus violation")
    qs = fixtures["questions"]
    require(isinstance(qs, list) and len(qs) >= 30, "fewer than 30 retrieval queries")
    seen = set()
    counts = {k: 0 for k in EXPECTED_BEHAVIORS}
    for q in qs:
        ident = q["id"]
        require(re.fullmatch(r"m9-q[0-9]{3}", ident) is not None and ident not in seen, "duplicate/invalid query ID")
        seen.add(ident)
        require(isinstance(q["query"], str) and len(q["query"]) >= 15, "empty query text")
        require(q["expected_behavior"] in counts, "unsupported expected behavior")
        counts[q["expected_behavior"]] += 1
        require(isinstance(q["guard"], str) and q["guard"], "missing negative/temporal guard")
        require(set(q["expected_case_ids"]) <= case_ids, ident + " refers to unknown case")
        require(set(q["required_source_ids"]) <= source_ids, ident + " refers to unknown source")
    require(all(value > 0 for value in counts.values()), "missing answer/refusal/false-claim fixture class")
    return counts


def read_case_catalog() -> tuple[set[str], list[Path]]:
    page_index = (CASE_DIR / "README.md").read_text(encoding="utf-8")
    local = [
        CASE_DIR / path.split("#", 1)[0]
        for path in re.findall(r"\]\(([^)#]+\.md(?:#[^)]*)?)\)", page_index)
        if not path.startswith("../")
    ]
    require(len(local) == len(set(local)), "case index duplicate Markdown paths")
    case_pages = [p for p in local if "decisions" not in p.parts]
    require(len(case_pages) >= 20, "case index lost required cases")
    require(all(p.is_file() for p in local), "missing local case index path")
    ids = set()
    for path in case_pages:
        text = path.read_text(encoding="utf-8")
        m = re.search(r"case\.[a-z][a-z0-9-]*\.[a-z][a-z0-9-]*", text)
        require(m is not None, str(path) + ": missing stable case ID")
        cid = m.group(0)
        require(cid not in ids, "duplicate case_id: " + cid)
        ids.add(cid)
        require("mermaid" in text.lower(), path.name + ": no architectural graph")
        require(text.count("```") % 2 == 0, path.name + ": unclosed Markdown fence")
        require("http" in text, path.name + ": no primary-source link")
    for path in local:
        text = path.read_text(encoding="utf-8")
        for link in re.findall(r"\]\(([^)]+)\)", text):
            if link.startswith(("https://", "http://", "#", "mailto:")):
                continue
            candidate = link.split("#", 1)[0]
            if not candidate:
                continue
            if candidate.endswith(".md"):
                require((path.parent / candidate).resolve().is_file(), path.name + ": broken relative link " + link)
    return ids, local


def check(root: Path = ROOT) -> dict:
    schema = json_read(PROPOSED_SCHEMA)
    require(schema["$schema"].endswith("2020-12/schema"), "unexpected schema dialect")
    assert schema["$id"].startswith("urn:tycho:m9:")
    raw_sources = SOURCE_REGISTER.read_text(encoding="utf-8")
    registered = set(re.findall(r"^\| ((?:N|U|A|SH|SP|ST|DI|ME|LI|CF)[0-9]{2}) \|", raw_sources, flags=re.M))
    require(len(registered) == 43, "source register not 43 candidates")
    ids, links = read_case_catalog()
    examples = json_read(SAMPLES)
    require(isinstance(examples, list) and len(examples) >= 2, "missing portable examples")
    for item in examples:
        validate_record(item, schema, registered)
        require(item["case_id"] in ids, "sample case missing from book")
    counts = validate_fixtures(json_read(QUERIES), ids, registered)
    validation_engine = "portable strict subset"
    try:
        import jsonschema  # type: ignore
    except ImportError:
        pass
    else:
        checker = jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker())
        for i, item in enumerate(examples):
            errors = list(checker.iter_errors(item))
            require(not errors, "JSON Schema example " + str(i) + ": " + "; ".join(str(err) for err in errors))
        validation_engine = "jsonschema Draft2020-12+FormatChecker"
    return {"case_pages": len(ids), "indexed_md_paths": len(links), "source_candidates": len(registered),
            "sample_records": len(examples), "question_classes": counts, "schema_check": validation_engine,
            "retrieval_execution": "NOT RUN", "independent_review": "NOT RUN"}


def self_test() -> None:
    schema = json_read(PROPOSED_SCHEMA)
    refs = set(re.findall(r"^\| ((?:N|U|A|SH|SP|ST|DI|ME|LI|CF)[0-9]{2}) \|",
                          SOURCE_REGISTER.read_text(encoding="utf-8"), flags=re.M))
    good = json_read(SAMPLES)[0]
    validate_record(good, schema, refs)
    failures = 0
    malformed_records = []
    mutations = ("wrong_collection", "orphan_source", "bad_claim", "missing_review", "future_window",
                 "integer_title", "short_statement", "non_string_source_ref", "non_string_pattern",
                 "non_string_review_limitation")
    for mutation in mutations:
        candidate = json.loads(json.dumps(good))
        if mutation == "wrong_collection":
            candidate["collection"] = "other-private-corpus"
        if mutation == "orphan_source":
            candidate["claims"][0]["source_ref_id"] = "XX99"
        if mutation == "bad_claim":
            candidate["claims"][0]["claim_id"] = "claim.invalid"
        if mutation == "missing_review":
            del candidate["review"]
        if mutation == "future_window":
            candidate["claims"][0]["validity_window"] = {
                "valid_from": "2026-10-20", "valid_until": "2026-10-19"
            }
        if mutation == "integer_title":
            candidate["title"] = 42
        if mutation == "short_statement":
            candidate["claims"][0]["statement"] = "too short"
        if mutation == "non_string_source_ref":
            candidate["source_refs"][0] = ["N11"]
        if mutation == "non_string_pattern":
            candidate["patterns"]["selected"] = [123]
        if mutation == "non_string_review_limitation":
            candidate["review"]["limitations"] = [False]
        malformed_records.append(candidate)
        try:
            validate_record(candidate, schema, refs)
        except ValueError:
            failures += 1
    require(failures == 10, "one or more negative contract tests incorrectly accepted")
    print("PASS: 10 malformed records rejected by built-in strict subset; valid example accepted")
    try:
        import jsonschema  # type: ignore
    except ImportError:
        print("NOT RUN: Draft2020-12 JSON Schema negative suite (jsonschema package absent)")
    else:
        jsonschema.Draft202012Validator.check_schema(schema)
        validator = jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker())
        require(not list(validator.iter_errors(good)), "jsonschema unexpectedly rejected valid sample")
        # JSON Schema 2020-12 "format: date" checks individual dates; it
        # cannot compare values of two sibling fields. Our extra semantic
        # invariant valid_from <= valid_until must run in validate_record.
        schema_mutations = [
            (name, candidate) for name, candidate in zip(mutations, malformed_records)
            if name != "future_window"
        ]
        for name, candidate in schema_mutations:
            require(bool(list(validator.iter_errors(candidate))),
                    "jsonschema accepted schema-invalid sample: " + name)
        reversed_window = malformed_records[mutations.index("future_window")]
        require(not list(validator.iter_errors(reversed_window)),
                "expected both inverted-window date strings to satisfy the base schema")
        # The semantic validator above already rejected the inverted window.
        print("PASS: Draft2020-12 engine rejects 9 schema violations; "
              "semantic validator rejects 1 inverted validity window")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_test:
            self_test()
        else:
            print(json.dumps(check(), indent=2))
    except (ValueError, KeyError, TypeError, json.JSONDecodeError) as error:
        print("M9 validation FAILED: " + str(error), file=sys.stderr)
        raise SystemExit(1)
