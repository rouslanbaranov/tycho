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
CID = re.compile(r"^case\.[a-z][a-z0-9-]*\.[a-z][a-z0-9-]*$")
CLAIM_ID = re.compile(r"^claim\.[a-z][a-z0-9-]*\.[a-z][a-z0-9-]*\.[0-9]{3}$")
SOURCE_ID = re.compile(r"^src\.[a-z0-9]+(?:-[a-z0-9]+)*$")
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
    require(isinstance(value, str) and
            re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", value) is not None,
            label + ": expected YYYY-MM-DD calendar date")
    # date.fromisoformat also accepts YYYYMMDD and ISO week dates, unlike
    # JSON Schema's format:date (RFC 3339 full-date). Enforce syntax above.
    try:
        dt.date.fromisoformat(value)
    except ValueError:
        fail(label + ": invalid calendar date " + repr(value))


def json_read(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def parse_source_registry(raw: str) -> dict[str, str]:
    """Map curated M9 source IDs to exactly one literal primary publisher URL.

    No network calls or redirects: this is a local provenance-binding check.
    """
    rows: dict[str, str] = {}
    source_row = re.compile(r"^\| (src\.[^ |]+) \|")
    link_row = re.compile(
        r"^\| (src\.[a-z0-9]+(?:-[a-z0-9]+)*) "
        r"\| [^|]+ \| \[[^\]]+\]\((https://[^)\s]+)\) \|")
    for line in raw.splitlines():
        match = source_row.match(line)
        if not match:
            continue
        source_id = match.group(1)
        require(SOURCE_ID.fullmatch(source_id) is not None, "invalid global source ID: " + source_id)
        full = link_row.match(line)
        require(full is not None, "source registry row missing HTTPS primary link: " + source_id)
        require(source_id not in rows, "duplicate primary source ID: " + source_id)
        rows[source_id] = full.group(2)
    require(len(rows) == 43, "source register must contain 43 unambiguous primary URLs")
    return rows


def validate_record(record: dict, schema: dict, registered_sources: dict[str, str]) -> None:
    require(isinstance(record, dict), "case record must be object")
    required = set(schema["required"])
    require(required <= set(record), "missing case keys " + str(sorted(required - set(record))))
    allowed = set(schema["properties"])
    require(set(record) <= allowed, "unknown case keys " + str(sorted(set(record) - allowed)))
    require(record["collection"] == "tycho-public", "case corpus isolation violation")
    require(record["schema_version"] == "m9-case-1.1-proposal", "invalid schema version")
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
    require(set(record["source_refs"]) <= registered_sources.keys(), "unregistered case source")
    require(isinstance(record["claims"], list) and len(record["claims"]) > 0, "case has no claims")
    iso_date(record["observed_on"], "observed_on", nullable=True)
    review = record["review"]
    require(isinstance(review, dict), "review not object")
    require(set(review) == {"reviewer", "reviewed_on", "limitations"}, "invalid review contract")
    iso_date(review["reviewed_on"], "reviewed_on", nullable=True)
    require(review["reviewer"] is None or isinstance(review["reviewer"], str), "reviewer not string/null")
    if record["status"] == "independent_reviewed":
        # Metadata is necessary, never sufficient, evidence of true peer review.
        require(isinstance(review["reviewer"], str)
                and len(review["reviewer"].strip()) >= 3,
                "independent review requires a named reviewer")
        require(isinstance(review["reviewed_on"], str),
                "independent review requires an actual review date")
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
        require(item["primary_url"] == registered_sources[item["source_ref_id"]],
                "claim primary URL disagrees with curated source_ref_id: " + item["source_ref_id"])
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



def validate_evidence_facet_pilot(
        pilot: dict, questions: list[dict], case_ids: set[str], source_ids: set[str]) -> dict:
    """Check proposed multi-hop labels without treating them as independent gold."""
    require(pilot["status"] == "proposed_for_independent_label_review",
            "facet pilot must not claim independent reviewer acceptance")
    require(pilot["schema_version"] == "m9-facet-coverage-pilot-0.1",
            "unsupported facet pilot format")
    matching = [q for q in questions if q["id"] == pilot["query_id"]]
    require(len(matching) == 1, "facet query missing/ambiguous")
    q = matching[0]
    require(q["query"] == pilot["original_question"],
            "facet question text drifted from frozen baseline")
    require(q["expected_case_ids"] == pilot["frozen_primary_expected_case_ids"],
            "primary baseline labels changed without explicit re-evaluation")
    facets = pilot["required_facets"]
    require(isinstance(facets, list) and len(facets) >= 2,
            "facet coverage requires two or more independently sourced facets")
    names = [f["facet_id"] for f in facets]
    require(len(names) == len(set(names)), "duplicate facet ID")
    direct_cases: set[str] = set()
    for facet in facets:
        require(facet["required_for_complete_synthesis"] is True,
                "pilot facet lacks mandatory-coverage status")
        require(isinstance(facet["case_support"], list) and facet["case_support"],
                "facet has no documented direct evidence")
        for support in facet["case_support"]:
            require(support["role"] == "direct_evidence",
                    "only primary case support may satisfy a required facet")
            require(support["case_id"] in case_ids,
                    "facet points to an unindexed case")
            require(isinstance(support["source_ids"], list) and support["source_ids"],
                    "facet missing source references")
            require(set(support["source_ids"]) <= source_ids,
                    "facet points to unregistered sources")
            require(isinstance(support["claim"], str) and support["claim"],
                    "facet missing bounded claim description")
            direct_cases.add(support["case_id"])
    for support in pilot["contextual_evidence"]:
        require(support["role"] in {"related_but_distinct", "contrast_not_immutable"},
                "contextual analogy must not be promoted to direct proof")
        require(support["case_id"] in case_ids,
                "contextual analogy points to an unindexed case")
        require(set(support["source_ids"]) <= source_ids,
                "contextual analogy points to unregistered sources")
    require(len(direct_cases) >= 2,
            "composite evidence must reference at least two cases")
    require(pilot["review_decision"] == "pending_independent_relevance_adjudication",
            "do not fabricate completed independent relevance review")
    return {"query_id": q["id"], "proposed_facets": len(facets),
            "proposed_direct_cases": len(direct_cases),
            "adjudication": "NOT DONE"}


def read_case_catalog(root: Path = ROOT, source_urls: dict[str, str] | None = None) -> tuple[set[str], list[Path]]:
    case_dir = root / "book/cases"
    root_boundary = root.resolve()
    case_boundary = case_dir.resolve()
    require(case_boundary.is_relative_to(root_boundary),
            "case collection escapes the selected root")
    index_path = case_dir / "README.md"
    require(index_path.resolve().is_relative_to(case_boundary),
            "case README index escapes its collection")
    # Inspect paths before opening any README/index content.
    page_index = index_path.read_text(encoding="utf-8")
    listed = re.findall(r"\]\(([^)#]+\.md(?:#[^)]*)?)\)", page_index)
    local = [case_dir / ref.split("#", 1)[0]
             for ref in listed if not ref.startswith("../")]
    # References to shared root-level source/authoring files are legitimate,
    # but cannot be silently dropped: they too must exist inside this snapshot.
    context = [case_dir / ref.split("#", 1)[0]
               for ref in listed if ref.startswith("../")]
    require(all(ref.resolve().is_relative_to(root_boundary) for ref in context),
            "case index contextual link escapes selected root")
    require(all(ref.is_file() for ref in context),
            "case index contains broken contextual link")
    require(len(local) == len(set(local)), "case index duplicate Markdown paths")
    # resolve() also protects against symlinks that point outside the snapshot.
    require(all(path.resolve().is_relative_to(case_boundary) for path in local),
            "case index escapes the selected case collection")
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
        if source_urls is not None:
            # At least one literal first-party URL from the curated register
            # must accompany its source ID in every case draft. Other mentions
            # may intentionally be contextual, not separately linked.
            cited = set(re.findall(
                r"\bsrc\.[a-z0-9]+(?:-[a-z0-9]+)*\b", text))
            require(any(source_id in cited and url in text
                        for source_id, url in source_urls.items()),
                    path.name + ": no matching curated source ID + primary URL")
    for path in local:
        text = path.read_text(encoding="utf-8")
        for link in re.findall(r"\]\(([^)]+)\)", text):
            if link.startswith(("https://", "http://", "#", "mailto:")):
                continue
            candidate = link.split("#", 1)[0]
            if not candidate:
                continue
            if candidate.endswith(".md"):
                target = (path.parent / candidate).resolve()
                require(target.is_relative_to(root_boundary),
                        path.name + ": relative link escapes selected root: " + link)
                require(target.is_file(), path.name + ": broken relative link " + link)
    return ids, local


def check(root: Path = ROOT) -> dict:
    schema = json_read(root / "authoring/cases/case-record.schema.json")
    require(schema["$schema"].endswith("2020-12/schema"), "unexpected schema dialect")
    require(isinstance(schema.get("$id"), str) and
            schema["$id"].startswith("urn:tycho:m9:"),
            "proposed M9 schema must use scoped Tycho URN")
    raw_sources = (root / "sources/REAL_WORLD_ARCHITECTURE_CASES.md").read_text(encoding="utf-8")
    registered = parse_source_registry(raw_sources)
    global_sources = {s['id']: s['url'] for s in json_read(root / 'sources/register.json')['sources']}
    require(all(global_sources.get(sid) == url for sid, url in registered.items()),
            "M9 source ID/URL disagrees with global source register")
    ids, links = read_case_catalog(root, registered)
    examples = json_read(root / "authoring/cases/examples/case-records.json")
    require(isinstance(examples, list) and len(examples) >= 2, "missing portable examples")
    for item in examples:
        validate_record(item, schema, registered)
        require(item["case_id"] in ids, "sample case missing from book")
    query_data = json_read(root / "tests/fixtures/m9-case-queries.json")
    counts = validate_fixtures(query_data, ids, set(registered))
    facet_pilot = validate_evidence_facet_pilot(
        json_read(root / "tests/fixtures/m9-q042-evidence-facets.proposed.json"),
        query_data["questions"], ids, set(registered))
    validation_engine = "portable strict subset"
    try:
        import jsonschema  # type: ignore
    except ImportError:
        pass
    else:
        jsonschema.Draft202012Validator.check_schema(schema)
        checker = jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker())
        for i, item in enumerate(examples):
            errors = list(checker.iter_errors(item))
            require(not errors, "JSON Schema example " + str(i) + ": " + "; ".join(str(err) for err in errors))
        validation_engine = "jsonschema Draft2020-12+FormatChecker"
    return {"case_pages": len(ids), "indexed_md_paths": len(links), "source_candidates": len(registered),
            "sample_records": len(examples), "question_classes": counts,
            "proposed_facet_pilot": facet_pilot, "schema_check": validation_engine,
            "retrieval_execution": "NOT RUN", "independent_review": "NOT RUN"}


def self_test(root: Path = ROOT) -> None:
    schema = json_read(root / "authoring/cases/case-record.schema.json")
    refs = parse_source_registry(
        (root / "sources/REAL_WORLD_ARCHITECTURE_CASES.md").read_text(encoding="utf-8"))
    good = json_read(root / "authoring/cases/examples/case-records.json")[0]
    validate_record(good, schema, refs)
    failures = 0
    malformed_records = []
    mutations = ("wrong_collection", "orphan_source", "bad_claim", "missing_review", "future_window",
                 "integer_title", "short_statement", "non_string_source_ref", "non_string_pattern",
                 "non_string_review_limitation", "basic_date", "week_date", "invalid_calendar_date",
                 "independent_review_null_reviewer", "independent_review_null_date",
                 "independent_review_blank_reviewer", "wrong_source_url", "foreign_url_same_host")
    for mutation in mutations:
        candidate = json.loads(json.dumps(good))
        if mutation == "wrong_collection":
            candidate["collection"] = "other-private-corpus"
        if mutation == "orphan_source":
            candidate["claims"][0]["source_ref_id"] = "src.m9-missing"
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
            candidate["source_refs"][0] = ["src.m9-n11"]
        if mutation == "non_string_pattern":
            candidate["patterns"]["selected"] = [123]
        if mutation == "non_string_review_limitation":
            candidate["review"]["limitations"] = [False]
        if mutation == "basic_date":
            candidate["observed_on"] = "20261019"
        if mutation == "week_date":
            candidate["claims"][0]["accessed_on"] = "2026-W43-1"
        if mutation == "invalid_calendar_date":
            candidate["claims"][0]["accessed_on"] = "2026-02-30"
        if mutation == "independent_review_null_reviewer":
            candidate["status"] = "independent_reviewed"
            candidate["review"]["reviewed_on"] = "2026-10-19"
        if mutation == "independent_review_null_date":
            candidate["status"] = "independent_reviewed"
            candidate["review"]["reviewer"] = "Independent Reviewer"
        if mutation == "independent_review_blank_reviewer":
            candidate["status"] = "independent_reviewed"
            candidate["review"]["reviewer"] = "   "
            candidate["review"]["reviewed_on"] = "2026-10-19"
        if mutation == "wrong_source_url":
            candidate["claims"][0]["primary_url"] = refs["src.m9-st01"]
        if mutation == "foreign_url_same_host":
            candidate["claims"][0]["primary_url"] = refs["src.m9-n11"] + "-another-article"
        malformed_records.append(candidate)
        try:
            validate_record(candidate, schema, refs)
        except ValueError:
            failures += 1
    require(failures == len(mutations), "one or more negative contract tests incorrectly accepted")
    print("PASS: " + str(len(mutations)) +
          " malformed records rejected by built-in strict subset; valid example accepted")
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
        semantic_only = {"orphan_source", "future_window", "wrong_source_url", "foreign_url_same_host"}
        schema_mutations = [
            (name, candidate) for name, candidate in zip(mutations, malformed_records)
            if name not in semantic_only
        ]
        for name, candidate in schema_mutations:
            require(bool(list(validator.iter_errors(candidate))),
                    "jsonschema accepted schema-invalid sample: " + name)
        reversed_window = malformed_records[mutations.index("future_window")]
        require(not list(validator.iter_errors(reversed_window)),
                "expected both inverted-window date strings to satisfy the base schema")
        for name in ("orphan_source", "wrong_source_url", "foreign_url_same_host"):
            candidate = malformed_records[mutations.index(name)]
            require(not list(validator.iter_errors(candidate)),
                    "base schema unexpectedly constrains registered source identity or URL: " + name)
        # The semantic validator already rejected both mismatched source URLs.
        print("PASS: Draft2020-12 engine rejects " +
              str(len(schema_mutations)) + " schema violations; "
              "semantic validator rejects unknown source, inverted window and 2 source URL mismatches")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--root", type=Path, default=ROOT,
                        help="Pinned checkout/snapshot root (default: repository containing this script)")
    args = parser.parse_args()
    try:
        root = args.root.resolve()
        require(root.is_dir(), "--root must reference a directory")
        if args.self_test:
            self_test(root)
        else:
            print(json.dumps(check(root), indent=2))
    except (ValueError, KeyError, TypeError, json.JSONDecodeError) as error:
        print("M9 validation FAILED: " + str(error), file=sys.stderr)
        raise SystemExit(1)
