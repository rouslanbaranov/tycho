#!/usr/bin/env python3
"""Validate the self-checked semantic audit of all 419 canonical pages."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_pattern_registry import slug_heading

ARTIFACT = Path("edition/patterns/semantic-audit.v1.json")
SCHEMA = Path("schemas/pattern-semantic-audit.v1.schema.json")
ROUTE = Path("generated/route-index.v1.json")
PHASE4 = Path("edition/patterns/phase4.v1.json")
REQUIRED_CHECKS = {
    "technical": ["identity", "question", "content", "evidence", "limits", "navigation"],
    "decision": ["identity", "question", "content", "evidence", "limits", "navigation"],
    "navigation": ["identity", "inventory", "links", "status", "limits"],
    "atlas": ["identity", "cards", "owner_links", "nonclaims", "links"],
}
REQUIRED_GATES = [
    "independent-technical-review",
    "independent-editorial-review",
    "owner-acceptance",
]


def require(ok, message):
    if not ok:
        raise ValueError(message)


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def tier_for(path, kind):
    if path.startswith("book/volumes/v11-pattern-atlas/"):
        return "atlas"
    if kind in ("book", "volume", "chapter", "landing"):
        return "navigation"
    if kind == "decision":
        return "decision"
    return "technical"


def headings(text):
    found = []
    fenced = False
    for line in text.splitlines():
        if line.strip().startswith("```"):
            fenced = not fenced
            continue
        if fenced:
            continue
        if line.startswith("#"):
            label = line.lstrip("#").strip()
            if label:
                found.append(label)
    return found


def anchor_ok(anchor, text):
    if anchor == "page":
        return True
    label = anchor.lstrip("# ").strip()
    if not label:
        return False
    slug = slug_heading(label)
    for heading in headings(text):
        if heading.strip().lower() == label.lower() or slug_heading(heading) == slug:
            return True
    return False


def engine():
    try:
        from jsonschema import Draft202012Validator, FormatChecker
    except ImportError as exc:
        raise RuntimeError("Install validation dependencies from requirements-validation.txt") from exc
    return Draft202012Validator, FormatChecker


def compute_summary(pages, gates, review_events):
    tiers = {"technical": 0, "decision": 0, "navigation": 0, "atlas": 0}
    dispositions = {"sound": 0, "sound-with-findings": 0,
                    "needs-remediation": 0, "blocked": 0}
    severity = {"total": 0, "low": 0, "medium": 0, "high": 0}
    with_findings = 0
    for page in pages:
        review = page["review"]
        tiers[page["tier"]] += 1
        dispositions[review["disposition"]] += 1
        if review["findings"]:
            with_findings += 1
        for finding in review["findings"]:
            severity["total"] += 1
            severity[finding["severity"]] += 1
    return {
        "pages": len(pages),
        "by_tier": tiers,
        "by_disposition": dispositions,
        "findings": severity,
        "pages_with_findings": with_findings,
        "independent_reviews": sum(1 for event in review_events
                                  if event["kind"] == "human"),
        "human_reviews": sum(1 for event in review_events
                             if event["kind"] == "human"),
        "agent_reviews": sum(1 for event in review_events
                             if event["kind"] == "independent-agent"),
        "owner_acceptance": "not-recorded",
        "open_gates": sum(1 for gate in gates if gate["status"] != "closed"),
    }


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
        raise ValueError("semantic-audit-schema: " + str(len(errors)) +
                         " error(s), first at " + path + ": " + first.message)

    route = load(root / ROUTE)
    documents = {item["path"]: item for item in route["documents"]}
    phase4 = load(root / PHASE4)
    dispositions = {item["path"]: item["disposition"]
                    for item in phase4["page_dispositions"]}
    require(len(documents) == 419, "semantic-audit-route-count")
    require(len(data["pages"]) == 419, "semantic-audit-page-count")

    seen_paths = set()
    seen_ids = set()
    for page in data["pages"]:
        path = page["path"]
        require(path not in seen_paths, "semantic-audit-duplicate-path")
        require(page["document_id"] not in seen_ids, "semantic-audit-duplicate-id")
        seen_paths.add(path)
        seen_ids.add(page["document_id"])
        document = documents.get(path)
        require(document is not None, "semantic-audit-unknown-page: " + path)
        require(page["document_id"] == document["id"], "semantic-audit-id: " + path)
        require(page["kind"] == document["kind"], "semantic-audit-kind: " + path)
        require(page["phase4_disposition"] == dispositions.get(path),
                "semantic-audit-phase4: " + path)
        require(page["tier"] == tier_for(path, document["kind"]),
                "semantic-audit-tier: " + path)
        require(sha(root / path) == page["sha256"], "semantic-audit-sha: " + path)

        review = page["review"]
        required = REQUIRED_CHECKS[page["tier"]]
        for check in required:
            require(check in review["checks"], "semantic-audit-check-missing: " + path)
        failed_checks = [check for check in required
                         if review["checks"][check] != "pass"]
        findings = review["findings"]
        if review["disposition"] == "sound":
            require(not findings, "semantic-audit-sound-with-findings: " + path)
            require(not failed_checks, "semantic-audit-sound-with-partial: " + path)
        if review["disposition"] == "sound-with-findings":
            require(findings, "semantic-audit-findings-missing: " + path)
            require(all(item["severity"] == "low" for item in findings),
                    "semantic-audit-medium-in-bounded: " + path)
        if review["disposition"] == "needs-remediation":
            require(any(item["severity"] in ("medium", "high") for item in findings),
                    "semantic-audit-remediation-severity: " + path)
            require(any(item["severity"] in ("medium", "high") and item["remediation"]
                        for item in findings),
                    "semantic-audit-remediation-missing: " + path)
        if review["disposition"] == "blocked":
            require(any(item["gate"] for item in findings),
                    "semantic-audit-gate-missing: " + path)
        for finding in findings:
            require(finding["remediation"] or finding["gate"],
                    "semantic-audit-finding-resolution-missing: " + path)
            require(anchor_ok(finding["anchor"], (root / path).read_text(encoding="utf-8")),
                    "semantic-audit-finding-anchor: " + path + ": " + finding["anchor"])
            if finding["severity"] == "high":
                require(review["disposition"] in ("needs-remediation", "blocked"),
                        "semantic-audit-high-disposition: " + path)

    require(seen_paths == set(documents), "semantic-audit-coverage-mismatch")
    summary = compute_summary(data["pages"], data["open_gates"], data["review_events"])
    require(summary == data["summary"], "semantic-audit-summary-mismatch")
    gate_ids = {gate["id"] for gate in data["open_gates"]}
    for gate in REQUIRED_GATES:
        require(gate in gate_ids, "semantic-audit-gate-missing: " + gate)
    for event in data["review_events"]:
        require(event["reviewer"].strip(), "semantic-audit-reviewer-empty")
        require((root / event["report_path"]).is_file(),
                "semantic-audit-review-report: " + event["report_path"])
    require(any(event["kind"] == "human" for event in data["review_events"]),
            "semantic-audit-human-review-missing")
    require(data["summary"]["agent_reviews"] == sum(
        1 for event in data["review_events"] if event["kind"] == "independent-agent"),
        "semantic-audit-agent-review-count")
    require(data["summary"]["human_reviews"] == sum(
        1 for event in data["review_events"] if event["kind"] == "human"),
        "semantic-audit-human-review-count")
    require(data["summary"]["independent_reviews"] == data["summary"]["human_reviews"],
            "semantic-audit-independent-review-count")
    require(data["summary"]["owner_acceptance"] == "not-recorded",
            "semantic-audit-owner-acceptance-claim")
    require(data["status"] != "reviewed", "semantic-audit-reviewed-claim")
    require(len(data["source_commit_note"]) >= 40, "semantic-audit-source-commit-note")

    head = subprocess.check_output(["git", "-C", str(root), "rev-parse", "HEAD"],
                                   text=True).strip()
    ancestor = subprocess.run(
        ["git", "-C", str(root), "merge-base", "--is-ancestor",
         data["source_commit"], head], capture_output=True).returncode == 0
    require(ancestor, "semantic-audit-source-commit-not-ancestor")
    return summary


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
        print("PASS: semantic audit", result["pages"], "pages,",
              result["findings"]["total"], "findings,", result["open_gates"], "gates")
    return 0


if __name__ == "__main__":
    sys.exit(main())
