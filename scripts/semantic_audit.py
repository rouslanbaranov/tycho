#!/usr/bin/env python3
"""Build the semantic-audit review queue or combine per-volume reviews."""
import argparse
from datetime import date
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_pattern_semantic_audit import (  # noqa: E402
    ARTIFACT, PHASE4, REQUIRED_CHECKS, ROUTE, compute_summary, load,
    tier_for, validate_data,
)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def headings(path):
    found = []
    fenced = False
    fence = chr(96) * 3
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if line.strip().startswith(fence):
            fenced = not fenced
            continue
        if fenced:
            continue
        if line.startswith("## ") or line.startswith("### "):
            label = line.lstrip("#").strip()
            if label:
                found.append(label)
    return found[:40]


def page_records(root):
    route = load(root / ROUTE)
    phase4 = load(root / PHASE4)
    dispositions = {item["path"]: item["disposition"]
                    for item in phase4["page_dispositions"]}
    records = []
    for document in route["documents"]:
        path = document["path"]
        tier = tier_for(path, document["kind"])
        records.append({
            "path": path,
            "document_id": document["id"],
            "kind": document["kind"],
            "tier": tier,
            "phase4_disposition": dispositions[path],
            "required_checks": REQUIRED_CHECKS[tier],
            "sha256": sha(root / path),
        })
    return sorted(records, key=lambda item: item["path"])


def batch_name(path):
    parts = path.split("/")
    if len(parts) > 2 and parts[0] == "book" and parts[1] == "volumes":
        return parts[2].split("-")[0]
    return "book"


def write_queue(root, outdir):
    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    batches = {}
    for record in page_records(root):
        batches.setdefault(batch_name(record["path"]), []).append({
            "path": record["path"],
            "document_id": record["document_id"],
            "kind": record["kind"],
            "tier": record["tier"],
            "phase4_disposition": record["phase4_disposition"],
            "required_checks": record["required_checks"],
            "headings": headings(root / record["path"]),
        })
    for batch, pages in sorted(batches.items()):
        target = outdir / (batch + ".json")
        target.write_text(json.dumps({"batch": batch, "pages": pages},
                                     indent=2, ensure_ascii=False) + "\n",
                          encoding="utf-8")
        print("queue", batch, len(pages), target)


def load_reviews(directory):
    directory = Path(directory)
    reviews = {}
    for path in sorted(directory.glob("*.json")):
        data = load(path)
        items = data["reviews"] if isinstance(data, dict) else data
        for item in items:
            page_path = item["path"]
            if page_path in reviews:
                raise ValueError("semantic-audit-duplicate-review: " + page_path)
            reviews[page_path] = item
    return reviews


def source_commit(root):
    try:
        return subprocess.check_output(
            ["git", "-C", str(root), "merge-base", "HEAD", "main"],
            text=True).strip()
    except subprocess.CalledProcessError:
        return subprocess.check_output(
            ["git", "-C", str(root), "rev-parse", "HEAD"], text=True).strip()


def build(root, reviews_dir, out):
    records = {item["path"]: item for item in page_records(root)}
    reviews = load_reviews(reviews_dir)
    if set(reviews) != set(records):
        missing = sorted(set(records) - set(reviews))
        extra = sorted(set(reviews) - set(records))
        raise ValueError("semantic-audit-coverage: missing=" + str(len(missing)) +
                         " extra=" + str(len(extra)))
    pages = []
    for path, record in sorted(records.items()):
        review = reviews[path]
        findings = []
        for finding in review.get("findings", []):
            findings.append({
                "severity": finding["severity"],
                "kind": finding["kind"],
                "summary": finding["summary"],
                "anchor": finding["anchor"],
                "remediation": finding.get("remediation"),
                "gate": finding.get("gate"),
            })
        page = {
            "document_id": record["document_id"],
            "path": path,
            "kind": record["kind"],
            "tier": record["tier"],
            "phase4_disposition": record["phase4_disposition"],
            "sha256": record["sha256"],
            "review": {
                "reviewed_at": date.today().isoformat(),
                "reviewer_role": "automated-authoring-agent",
                "method": "bounded-page-read",
                "disposition": review["disposition"],
                "checks": review["checks"],
                "findings": findings,
                "notes": review.get("notes") or "Bounded self-checked page review.",
            },
        }
        pages.append(page)
    gates = [
        {
            "id": "independent-technical-review",
            "status": "open",
            "description": "No named independent technical reviewer has examined the atlas cards or the audited pages.",
            "action": "Assign a named reviewer and record the exact checked evidence before any sufficient promotion.",
        },
        {
            "id": "independent-editorial-review",
            "status": "open",
            "description": "No named independent editorial reviewer has examined the decision cards or the page findings.",
            "action": "Assign a named editor, review the packet and record accepted or rejected findings.",
        },
        {
            "id": "owner-acceptance",
            "status": "open",
            "description": "The owner has not accepted the Pattern Atlas or the semantic-audit record.",
            "action": "Record owner acceptance only after the independent review gates are closed.",
        },
        {
            "id": "polyglot-persistence-owner",
            "status": "blocked",
            "description": "Polyglot Persistence remains uncarded because no technical owner exists.",
            "action": "Keep the entry blocked and uncited, or assign an owner through a separate task.",
        },
        {
            "id": "split-discovery-balancing",
            "status": "open",
            "description": "The discovery and balancing page has a recorded split decision that is deferred.",
            "action": "Perform the split only through a documented page migration with stable identities.",
        },
        {
            "id": "split-tls-gateway",
            "status": "open",
            "description": "The TLS and gateway page has a recorded split decision that is deferred.",
            "action": "Perform the split only through a documented page migration with stable identities.",
        },
        {
            "id": "split-identity-authorization",
            "status": "open",
            "description": "The identity and authorization page has a recorded split decision that is deferred.",
            "action": "Perform the split only through a documented page migration with stable identities.",
        },
    ]
    data = {
        "schema_version": 1,
        "status": "semantic-audit-recorded",
        "audit_date": date.today().isoformat(),
        "source_commit": source_commit(root),
        "scope": "One self-checked semantic disposition for each of the 419 canonical pages, "
                 "including technical, decision, navigation and atlas pages; not independent review.",
        "method": "Every page was read as a bounded page, its identity and links were checked, "
                  "and findings were recorded against section headings. The review does not "
                  "re-verify every sentence against external sources.",
        "review_rules": {
            "technical": "Check the reader question, mechanism content, source references, "
                         "limits, internal navigation and page identity.",
            "decision": "Check the decision question, decision content, evidence, limits, "
                        "internal navigation and page identity.",
            "navigation": "Check inventory claims, child links, status wording, limits and "
                          "page identity.",
            "atlas": "Check card completeness, exact owner links, nonclaims, links and page identity.",
            "dispositions": {
                "sound": "No finding and all required checks pass.",
                "sound-with-findings": "Only bounded low or medium findings, each with a remediation or gate.",
                "needs-remediation": "At least one finding has a concrete remediation.",
                "blocked": "At least one finding has an explicit unresolved gate.",
            },
        },
        "pages": pages,
        "open_gates": gates,
        "limits": [
            "This is self-checked agent editorial evidence, not independent technical or editorial review.",
            "The audit records a bounded page reading and does not source-verify every sentence.",
            "The 69 owner-accepted manuscripts retain their acceptance; findings are bounded remediation items.",
            "No release, deployment, hosted retrieval, benchmark or CI result is claimed.",
            "No page split, document ID change or ownership migration was performed.",
        ],
    }
    data["summary"] = compute_summary(pages, gates)
    validate_data(data, root)
    Path(out).write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n",
                         encoding="utf-8")
    print("wrote", out, "pages", len(pages))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--queue", type=Path, help="write per-volume review queues here")
    parser.add_argument("--reviews", type=Path, help="combine review JSON files from here")
    parser.add_argument("--out", type=Path, default=ARTIFACT)
    parser.add_argument("--check", action="store_true", help="validate the committed artifact")
    args = parser.parse_args()
    try:
        if args.queue:
            write_queue(ROOT, args.queue)
        if args.reviews:
            build(ROOT, args.reviews, ROOT / args.out)
        if args.check:
            result = validate_data(load(ROOT / ARTIFACT), ROOT)
            print("PASS: semantic audit", result["pages"], "pages,",
                  result["findings"]["total"], "findings,", result["open_gates"], "gates")
    except (ValueError, OSError, KeyError, json.JSONDecodeError) as exc:
        print("FAIL:", exc, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
