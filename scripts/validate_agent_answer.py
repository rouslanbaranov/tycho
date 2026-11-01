#!/usr/bin/env python3
"""Validate an agent answer against the v2 evidence contract.

Mechanical checks only. Semantic support is deliberately reported as
"not-checked"; a judge or human must still read the evidence.
"""
import argparse
import json
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DB = ROOT / "generated/sections-fts-v5.sqlite"


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def section_keys(db):
    con = sqlite3.connect(db)
    try:
        return {row[0] for row in con.execute("select section_key from sections")}
    finally:
        con.close()


def validate_answer(answer, question, sections):
    errors = []
    warnings = []
    claims = answer.get("claims") or []
    if not answer.get("task_id"):
        errors.append("missing task_id")
    if not answer.get("answer"):
        errors.append("missing answer text")
    if answer.get("abstain") is False and not claims:
        errors.append("non-abstaining answer has no claims")

    seen_claim_ids = set()
    evidence_keys = []
    for claim in claims:
        claim_id = claim.get("claim_id")
        if not claim_id:
            errors.append("claim without claim_id")
            continue
        if claim_id in seen_claim_ids:
            errors.append("duplicate claim_id: " + claim_id)
        seen_claim_ids.add(claim_id)
        if not claim.get("text"):
            errors.append("empty claim text: " + claim_id)
        evidence = claim.get("evidence") or []
        if not evidence:
            errors.append("claim has no evidence: " + claim_id)
        for item in evidence:
            key = item.get("section_key", "")
            if key not in sections:
                errors.append("unresolved section key: " + key)
            if item.get("supports") != claim_id:
                errors.append("supports mismatch: " + key + " -> " + str(item.get("supports")))
            if not item.get("quote"):
                errors.append("empty quote: " + key)
            if item.get("status") not in ("observed", "inference"):
                errors.append("bad evidence status: " + key)
            evidence_keys.append(key)

    citations = answer.get("citations") or []
    if len(citations) != len(set(citations)):
        errors.append("duplicate citations")
    if set(citations) != set(evidence_keys):
        errors.append("citations must equal unique evidence section keys")
    for key in citations:
        if key not in sections:
            errors.append("unresolved citation: " + key)

    required = set(question.get("required_evidence") or [])
    computed_missing = sorted(required - set(citations))
    declared_missing = sorted(set(answer.get("missing_required_anchors") or []))
    if declared_missing != computed_missing:
        errors.append("missing_required_anchors does not match computed coverage")
    coverage = 1.0 if not required else (len(required) - len(computed_missing)) / len(required)
    extra = set(citations) - set(evidence_keys)
    if extra:
        errors.append("orphan citations: " + ", ".join(sorted(extra)))
    if required and computed_missing:
        warnings.append("required_anchor_coverage=" + format(coverage, ".3f"))
    return {
        "ok": not errors,
        "task_id": answer.get("task_id"),
        "citations_resolved": not any(e.startswith("unresolved") for e in errors),
        "required_anchor_coverage": round(coverage, 3),
        "missing_required_anchors": computed_missing,
        "semantic_support": "not-checked",
        "errors": errors,
        "warnings": warnings,
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("answer", type=Path)
    parser.add_argument("--corpus", type=Path,
                        default=ROOT / "evaluation/agent-benchmark/corpus-v7.json")
    parser.add_argument("--db", type=Path, default=DEFAULT_DB)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    answer = load(args.answer)
    corpus = load(args.corpus)
    question = next((q for q in corpus["questions"]
                     if q["id"] == answer.get("task_id")), None)
    if question is None:
        print("FAIL: task_id absent from corpus", file=sys.stderr)
        return 1
    result = validate_answer(answer, question, section_keys(args.db))
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(("PASS" if result["ok"] else "FAIL") + ": " + str(result["task_id"]))
        for error in result["errors"]:
            print("  " + error)
        for warning in result["warnings"]:
            print("  warning: " + warning)
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
