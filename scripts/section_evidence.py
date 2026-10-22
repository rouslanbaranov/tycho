#!/usr/bin/env python3
"""Bounded, read-only evidence and decision-reference resolution.

Resolves registered claim, source, book-document and decision IDs against the
canonical claim ledger, source register and route index. It returns only
registered metadata and citations; it never fetches a source, copies source
text, invents inspection, traverses a graph or mutates the book.

Every lookup carries a deterministic evidence snapshot derived from the route
snapshot and the exact ledger/register/lock bytes. A caller may pass an expected
snapshot and receive an explicit mismatch instead of newer evidence.
"""
import argparse
import hashlib
import json
from pathlib import Path
import sys

import validate_claim_references as claims_validator

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CLAIMS = ROOT / "sources/claim-references.json"
DEFAULT_REGISTER = ROOT / "sources/register.json"
DEFAULT_LOCK = ROOT / "sources/public-repositories.lock.json"
DEFAULT_ROUTE = ROOT / "generated/route-index.v1.json"


class EvidenceError(ValueError):
    def __init__(self, message, status="invalid-request"):
        super().__init__(message)
        self.status = status


def require(value, message, status="invalid-request"):
    if not value:
        raise EvidenceError(message, status)


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def canonical_json(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=False,
                      separators=(",", ":"))


def file_digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def doc_summary(doc):
    if doc is None:
        return None
    return {
        "document_id": doc["id"],
        "title": doc["title"],
        "kind": doc["kind"],
        "path": doc["path"],
        "parent_id": doc["parent_id"],
        "evidence_status": doc["evidence_status"],
        "claim_ids": doc["claim_ids"],
        "source_ids": doc["source_ids"],
        "summary": doc["summary"],
    }


def source_summary(source):
    return {
        "source_id": source["id"],
        "title": source["title"],
        "publisher": source["publisher"],
        "kind": source["kind"],
        "url": source["url"],
        "resolved_url": source.get("resolved_url"),
        "version": source.get("version"),
        "topics": source.get("topics", []),
        "admission": source.get("admission"),
        "access": source.get("access"),
        "reading_status": source.get("reading_status"),
        "access_checked": source.get("access_checked"),
        "content_verified": source.get("content_verified"),
        "verification_scope": source.get("verification_scope"),
        "license_notes": source.get("license_notes"),
        "inspection_claim_allowed": source.get("admission") == "admitted-for-research",
    }


def build_store(claims_path=DEFAULT_CLAIMS, register_path=DEFAULT_REGISTER,
                lock_path=DEFAULT_LOCK, route_path=DEFAULT_ROUTE):
    claims_data = load(claims_path)
    register = load(register_path)
    lock = load(lock_path)
    route = load(route_path)
    try:
        counts = claims_validator.validate(claims_data, register, lock)
    except ValueError as exc:
        raise EvidenceError("Claim ledger failed local validation: " + str(exc),
                            "not-available") from exc
    sources = {source["id"]: source for source in register["sources"]}
    claims = {claim["id"]: claim for claim in claims_data["claims"]}
    docs_by_id = {doc["id"]: doc for doc in route["documents"]}
    docs_by_path = {doc["path"]: doc for doc in route["documents"]}
    snapshot = hashlib.sha256(canonical_json({
        "route_snapshot": route["snapshot_sha256"],
        "claims_sha256": file_digest(claims_path),
        "register_sha256": file_digest(register_path),
        "lock_sha256": file_digest(lock_path),
    }).encode("utf-8")).hexdigest()
    return {
        "claims": claims,
        "sources": sources,
        "docs_by_id": docs_by_id,
        "docs_by_path": docs_by_path,
        "route_snapshot": route["snapshot_sha256"],
        "snapshot": snapshot,
        "counts": counts,
    }


def check_expected(store, expected_snapshot):
    if expected_snapshot is not None:
        require(expected_snapshot == store["snapshot"],
                "Evidence snapshot does not match the current ledger/register/route",
                "snapshot-mismatch")


def resolve_claim(store, claim_id, expected_snapshot=None):
    require(isinstance(claim_id, str) and claim_id,
            "claim id must be a non-empty string")
    check_expected(store, expected_snapshot)
    claim = store["claims"].get(claim_id)
    require(claim is not None, "Unknown claim: " + claim_id, "not-found")
    owner = store["docs_by_path"].get(claim["owner_page"])
    evidence = []
    relations = set()
    contradictions = []
    unavailable = []
    warnings = []
    for item in claim["evidence"]:
        source = store["sources"][item["source_id"]]
        relations.add(item["relation"])
        allowed = (item["relation"] != "unavailable"
                   and source["admission"] == "admitted-for-research"
                   and item["verification"] in ("section-inspected", "code-inspected"))
        entry = {
            "source": source_summary(source),
            "relation": item["relation"],
            "verification": item["verification"],
            "observed_at": item["observed_at"],
            "location": item["location"],
            "reasoning": item["reasoning"],
            "allowed_as_inspected_evidence": allowed,
        }
        evidence.append(entry)
        if item["relation"] == "contradicts":
            contradictions.append({"source_id": item["source_id"],
                                   "reasoning": item["reasoning"]})
        if item["relation"] == "unavailable":
            unavailable.append({"source_id": item["source_id"],
                                "reasoning": item["reasoning"]})
    if owner is None:
        warnings.append("Owner page is outside the book route index")
    elif claim["id"] not in owner.get("claim_ids", []):
        warnings.append("Owner page frontmatter does not declare this claim ID")
    if claim["status"] == "contested":
        warnings.append("Claim is contested; contradictions are part of the record")
    if claim["status"] == "insufficient-evidence":
        warnings.append("Claim is insufficient-evidence; do not present it as a finding")
    if any(not entry["allowed_as_inspected_evidence"]
           and entry["relation"] != "unavailable" for entry in evidence):
        warnings.append("At least one evidence entry is not admitted-and-inspected")
    return {
        "status": "ok",
        "snapshot": store["snapshot"],
        "route_snapshot": store["route_snapshot"],
        "claim": {
            "id": claim["id"],
            "statement": claim["statement"],
            "status": claim["status"],
            "owner_page": claim["owner_page"],
            "applicability": claim["applicability"],
            "evidence": evidence,
            "relations": sorted(relations),
            "contradictions": contradictions,
            "unavailable": unavailable,
        },
        "owner_document": doc_summary(owner),
        "warnings": warnings,
    }


def resolve_source(store, source_id, expected_snapshot=None):
    require(isinstance(source_id, str) and source_id,
            "source id must be a non-empty string")
    check_expected(store, expected_snapshot)
    source = store["sources"].get(source_id)
    require(source is not None, "Unknown source: " + source_id, "not-found")
    references = []
    for claim in store["claims"].values():
        for item in claim["evidence"]:
            if item["source_id"] == source_id:
                references.append({
                    "claim_id": claim["id"],
                    "claim_status": claim["status"],
                    "owner_page": claim["owner_page"],
                    "relation": item["relation"],
                    "verification": item["verification"],
                })
    warnings = []
    if source["admission"] != "admitted-for-research":
        warnings.append("Source is not admitted for research evidence")
    if not references:
        warnings.append("No registered claim references this source")
    return {
        "status": "ok",
        "snapshot": store["snapshot"],
        "route_snapshot": store["route_snapshot"],
        "source": source_summary(source),
        "claims": references,
        "warnings": warnings,
    }


def resolve_document(store, document_id, expected_snapshot=None):
    require(isinstance(document_id, str) and document_id,
            "document id must be a non-empty string")
    check_expected(store, expected_snapshot)
    document = store["docs_by_id"].get(document_id)
    require(document is not None, "Unknown document: " + document_id, "not-found")
    ledger_claims = [claim for claim in store["claims"].values()
                     if claim["owner_page"] == document["path"]]
    front_claims = []
    warnings = []
    for claim_id in document.get("claim_ids", []):
        claim = store["claims"].get(claim_id)
        if claim is None:
            warnings.append("Declared claim ID has no ledger record: " + claim_id)
            front_claims.append({"claim_id": claim_id, "found": False})
        else:
            front_claims.append({"claim_id": claim_id, "found": True,
                                 "status": claim["status"]})
    if ledger_claims and not document.get("claim_ids"):
        warnings.append("Ledger claims for this page are absent from frontmatter claim_ids")
    source_ids = set(document.get("source_ids", []))
    for claim in ledger_claims:
        for item in claim["evidence"]:
            source_ids.add(item["source_id"])
    for sid in sorted(source_ids):
        if sid not in store["sources"]:
            warnings.append("Declared source ID has no register record: " + sid)
    sources = [source_summary(store["sources"][sid])
               for sid in sorted(source_ids) if sid in store["sources"]]
    return {
        "status": "ok",
        "snapshot": store["snapshot"],
        "route_snapshot": store["route_snapshot"],
        "document": doc_summary(document),
        "frontmatter_claims": front_claims,
        "ledger_claims": [{
            "claim_id": claim["id"],
            "status": claim["status"],
            "relations": sorted({item["relation"] for item in claim["evidence"]}),
            "source_ids": [item["source_id"] for item in claim["evidence"]],
        } for claim in ledger_claims],
        "sources": sources,
        "warnings": warnings,
    }


def resolve_decision(store, decision_id, expected_snapshot=None):
    require(isinstance(decision_id, str) and decision_id,
            "decision id must be a non-empty string")
    check_expected(store, expected_snapshot)
    document = store["docs_by_id"].get(decision_id)
    require(document is not None, "Unknown document: " + decision_id, "not-found")
    require(document["kind"] == "decision",
            "Document is not a decision: " + decision_id)
    references = []
    for relation in ("related", "prerequisites"):
        for target_id in document.get(relation, []):
            target = store["docs_by_id"].get(target_id)
            references.append({
                "relation": relation,
                "document_id": target_id,
                "found": target is not None,
                "title": target["title"] if target else None,
                "kind": target["kind"] if target else None,
                "path": target["path"] if target else None,
            })
    return {
        "status": "ok",
        "snapshot": store["snapshot"],
        "route_snapshot": store["route_snapshot"],
        "decision": doc_summary(document),
        "direct_references": references,
        "warnings": ["Direct references only; no graph traversal is performed"],
    }


RESOLVERS = {
    "claim": resolve_claim,
    "source": resolve_source,
    "document": resolve_document,
    "decision": resolve_decision,
}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("action", choices=sorted(RESOLVERS))
    ap.add_argument("--id", required=True)
    ap.add_argument("--expected-snapshot")
    ap.add_argument("--claims", type=Path, default=DEFAULT_CLAIMS)
    ap.add_argument("--register", type=Path, default=DEFAULT_REGISTER)
    ap.add_argument("--lock", type=Path, default=DEFAULT_LOCK)
    ap.add_argument("--route-index", type=Path, default=DEFAULT_ROUTE)
    args = ap.parse_args(argv)
    try:
        store = build_store(args.claims, args.register, args.lock, args.route_index)
        result = RESOLVERS[args.action](store, args.id, args.expected_snapshot)
    except EvidenceError as exc:
        print(json.dumps({"status": exc.status, "error": str(exc)}, sort_keys=True))
        return 1
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
