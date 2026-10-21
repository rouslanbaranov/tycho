#!/usr/bin/env python3
"""Build or check candidate pattern-to-owner coverage for the atlas.

Candidate areas and pages are routing hypotheses, not coverage completion.
No page audit, source reading or technical sufficiency is implied.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
import unicodedata

ROOT = Path(__file__).resolve().parents[1]
COVERAGE = Path("edition/patterns/coverage-map.v1.json")
REVERSE = Path("edition/patterns/reverse-map.v1.json")
TICK = chr(96)
INLINE = re.compile("[" + TICK + "][^" + TICK + r"\n]*[" + TICK + "]")
HEAD = re.compile(r"^\s{0,3}(#{1,6})\s+(.+?)\s*$")
FENCE = re.compile(r"^\s*([" + TICK + r"]{3,}|~{3,})[^\r\n]*$")

FAMILY_DEFAULTS = {
    "application-architecture-and-boundaries": "V02/C01",
    "api-and-service-communication": "V02/C05",
    "messaging-and-event-driven-integration": "V04/C06",
    "data-consistency-transactions-and-event-sourcing": "V04/C05",
    "caching-and-retrieval": "V06/C01",
    "database-and-storage-architecture": "V05/C05",
    "resilience-and-fault-tolerance": "V07/C05",
    "distributed-coordination": "V04/C02",
    "scalability-and-load-distribution": "V07/C06",
    "deployment-and-legacy-modernization": "V08/C04",
    "security-isolation-and-operational-architecture": "V09/C05",
}

FAMILY_ALLOWLIST = {
    "application-architecture-and-boundaries": ["book/volumes/v02-", "book/application/", "book/volumes/v10-"],
    "api-and-service-communication": ["book/volumes/v02-", "book/volumes/v08-", "book/volumes/v09-", "book/security/"],
    "messaging-and-event-driven-integration": ["book/volumes/v04-", "book/volumes/v02-", "book/integration/"],
    "data-consistency-transactions-and-event-sourcing": ["book/volumes/v04-", "book/volumes/v05-", "book/distributed/", "book/data/"],
    "caching-and-retrieval": ["book/volumes/v06-", "book/scaling/"],
    "database-and-storage-architecture": ["book/volumes/v05-", "book/volumes/v04-", "book/data/"],
    "resilience-and-fault-tolerance": ["book/volumes/v07-", "book/volumes/v02-", "book/volumes/v08-", "book/performance/"],
    "distributed-coordination": ["book/volumes/v04-", "book/volumes/v08-", "book/distributed/"],
    "scalability-and-load-distribution": ["book/volumes/v07-", "book/volumes/v08-", "book/volumes/v05-", "book/performance/", "book/scaling/"],
    "deployment-and-legacy-modernization": ["book/volumes/v08-", "book/volumes/v10-", "book/delivery/", "book/deployment/"],
    "security-isolation-and-operational-architecture": ["book/volumes/v09-", "book/volumes/v02-", "book/security/", "book/observability/"],
}

AREA_OVERRIDES = {
    "Modular Monolith": "V02/C03",
    "Microservices Architecture": "V02/C04",
    "Service-Oriented Architecture (SOA)": "V02/C04",
    "Self-Contained Service": "V02/C04",
    "Database per Service": "V02/C02",
    "Domain-Driven Design / Bounded Context": "V02/C02",
    "Anti-Corruption Layer": "V02/C06",
    "Sidecar": "V08/C03",
    "Ambassador": "V08/C03",
    "API Gateway": "V08/C08",
    "Gateway Routing": "V08/C08",
    "Gateway Aggregation": "V08/C08",
    "Gateway Offloading": "V08/C08",
    "Reverse Proxy": "V08/C08",
    "Service Discovery": "V08/C08",
    "Client-Side Discovery": "V08/C08",
    "Server-Side Discovery": "V08/C08",
    "Asynchronous Request-Reply": "V03/C04",
    "Gatekeeper": "V02/C07",
    "Idempotent Receiver": "V04/C04",
    "Process Manager / Routing Slip": "V04/C05",
    "CQRS": "V04/C05",
    "Command Query Responsibility Segregation (CQRS)": "V04/C05",
    "Event Sourcing": "V04/C05",
    "Domain Events": "V04/C05",
    "Saga": "V04/C05",
    "Saga Choreography": "V04/C05",
    "Saga Orchestration": "V04/C05",
    "Compensating Transaction": "V04/C05",
    "Transactional Outbox": "V04/C05",
    "Transactional Inbox": "V04/C05",
    "Idempotency Key": "V04/C04",
    "Change Data Capture (CDC)": "V04/C08",
    "Materialized View": "V04/C05",
    "Command-Side Replica": "V04/C05",
    "Two-Phase Commit (2PC)": "V04/C03",
    "Cache Invalidation": "V06/C02",
    "TTL-Based Expiration": "V06/C02",
    "Negative Caching": "V06/C02",
    "Cache Stampede Protection": "V06/C02",
    "Single Flight / Request Coalescing": "V06/C02",
    "Stale-While-Revalidate": "V06/C02",
    "CDN / Edge Caching": "V08/C08",
    "Sharding": "V05/C05",
    "Partitioning": "V05/C05",
    "Consistent Hashing": "V05/C05",
    "Leader-Follower Replication": "V04/C02",
    "Multi-Leader Replication": "V04/C02",
    "Read Replicas": "V04/C02",
    "Quorum-Based Reads/Writes": "V04/C02",
    "Index Table": "V05/C03",
    "Polyglot Persistence": "V05/C04",
    "CQRS Read Projections": "V04/C05",
    "Expand-and-Contract Schema": "V05/C06",
    "Online Data Migration": "V05/C06",
    "Backup, PITR and Restore": "V05/C07",
    "Retry with Exponential Backoff": "V02/C05",
    "Retry with Jitter": "V02/C05",
    "Timeout": "V02/C05",
    "Deadline Propagation": "V02/C05",
    "Circuit Breaker": "V07/C05",
    "Bulkhead": "V07/C05",
    "Fallback": "V07/C05",
    "Graceful Degradation": "V07/C05",
    "Load Shedding": "V07/C05",
    "Throttling": "V07/C05",
    "Rate Limiting": "V07/C05",
    "Queue-Based Load Leveling": "V07/C05",
    "Priority Queue": "V07/C05",
    "Hedged Requests": "V07/C05",
    "Health Endpoint Monitoring": "V09/C06",
    "Failover / Failback": "V08/C06",
    "Distributed Lock": "V04/C05",
    "Lease-Based Ownership": "V04/C05",
    "Fencing Tokens": "V04/C05",
    "Causal Ordering": "V04/C01",
    "Session Consistency": "V04/C01",
    "Distributed Workflow Orchestration": "V04/C05",
    "Load Balancing": "V08/C08",
    "Cell-Based Architecture": "V08/C06",
    "Shuffle Sharding": "V08/C06",
    "Deployment Stamps": "V08/C07",
    "Geode": "V08/C07",
    "Static Content Hosting": "V08/C08",
    "Tenant-Based Resource Isolation": "V09/C05",
    "Rolling Deployment": "V08/C04",
    "Blue/Green Deployment": "V08/C04",
    "Canary Release": "V08/C04",
    "Feature Flags / Feature Toggles": "V08/C04",
    "GitOps": "V08/C01",
    "Immutable Infrastructure": "V08/C03",
    "Strangler Fig": "V10/C05",
    "Branch by Abstraction": "V10/C05",
    "Parallel Run": "V10/C05",
    "Dark Launching / Shadow Traffic": "V10/C05",
    "Expand-and-Contract": "V08/C05",
    "Controlled Cutover": "V10/C05",
    "SLI/SLO and Error Budgets": "V09/C01",
    "Synthetic Monitoring": "V09/C01",
    "Distributed Tracing": "V09/C03",
    "Structured Logging": "V09/C04",
    "Audit Trail": "V09/C04",
    "Health, Readiness and Liveness Checks": "V09/C06",
}

STOP = {
    "a", "an", "the", "and", "or", "of", "for", "to", "in", "on", "with",
    "by", "from", "as", "at", "is", "are", "be", "pattern", "patterns",
    "architecture", "architectural", "based", "using", "use", "service",
    "services", "system", "design", "data", "distributed",
}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def normalized(value):
    value = unicodedata.normalize("NFKD", value).lower()
    return re.sub(r"[^a-z0-9]+", " ", value).strip()


def tokens(value):
    return {token for token in normalized(value).split()
            if token and token not in STOP and len(token) > 2}


def heading_slugs(path):
    slugs = []
    fenced = None
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        match = FENCE.match(line)
        if match:
            marker = match.group(1)
            if fenced is None:
                fenced = (marker[0], len(marker))
            elif marker[0] == fenced[0] and len(marker) >= fenced[1]:
                fenced = None
            continue
        if fenced is not None:
            continue
        heading = HEAD.match(line)
        if heading:
            slugs.append(slug_heading(heading.group(2)))
    return slugs


def slug_heading(label):
    text = re.sub(r"<[^>]*>", "", label)
    text = INLINE.sub(lambda match: match.group(0).strip(TICK), text)
    text = text.strip().rstrip("#").strip().lower()
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE)
    return re.sub(r"\s+", "-", text)


def chapter_index(outline):
    return {item["code"]: item for item in outline["chapters"]}


def candidate_area(pattern, chapters):
    code = AREA_OVERRIDES.get(pattern["catalog_name"],
                              FAMILY_DEFAULTS[pattern["family"]])
    require(code in chapters, "coverage-area-missing: " + code)
    chapter = chapters[code]
    return {
        "chapter": code,
        "document_id": chapter["id"],
        "path": chapter["path"],
        "title": chapter["title"],
    }


def page_candidates(pattern, area, index, headings):
    family = pattern["family"]
    allow = FAMILY_ALLOWLIST[family]
    area_prefix = area["path"].rsplit("/", 1)[0] + "/"
    names = tokens(pattern["catalog_name"] + " " + " ".join(pattern["aliases"]))
    scored = []
    for doc in index:
        if doc["kind"] != "page":
            continue
        path = doc["path"]
        if "/volumes/v11-" in path:
            continue
        in_area = path.startswith(area_prefix)
        in_family = any(prefix in path for prefix in allow)
        if not (in_area or in_family):
            continue
        title = normalized(doc["title"])
        heading_text = " ".join(headings.get(path, []))
        score = 0
        basis = []
        if normalized(pattern["catalog_name"]) in title:
            score += 10
            basis.append("title-exact")
        elif slug_heading(pattern["catalog_name"]) in headings.get(path, []):
            score += 8
            basis.append("heading-exact")
        for token in names:
            if token in title:
                score += 4
                basis.append("title:" + token)
            elif token in heading_text:
                score += 2
                basis.append("heading:" + token)
        if in_area:
            score += 2
        if score:
            scored.append((score, in_area, doc, basis))
    scored.sort(key=lambda row: (-row[0], not row[1], row[2]["path"]))
    result = []
    weak = None
    for score, in_area, doc, basis in scored:
        if "title-exact" in basis or "heading-exact" in basis:
            confidence = "strong"
        elif len(set(basis)) >= 2 and score >= 6:
            confidence = "medium"
        else:
            if weak is None and in_area and score >= 4:
                weak = (score, in_area, doc, basis)
            continue
        result.append({
            "document_id": doc["id"],
            "path": doc["path"],
            "title": doc["title"],
            "confidence": confidence,
            "basis": sorted(set(basis)),
            "requested_area": in_area,
        })
        if len(result) == 2:
            break
    if not result and weak is not None:
        score, in_area, doc, basis = weak
        result.append({
            "document_id": doc["id"],
            "path": doc["path"],
            "title": doc["title"],
            "confidence": "weak",
            "basis": sorted(set(basis)),
            "requested_area": in_area,
        })
    return result


def build(root=ROOT):
    root = Path(root).resolve()
    registry = load(root / "edition/patterns/registry.v1.json")
    index_doc = load(root / "generated/route-index.v1.json")
    outline = load(root / "edition/outline.json")
    chapters = chapter_index(outline)
    documents = index_doc["documents"]
    headings = {doc["path"]: heading_slugs(root / doc["path"])
                for doc in documents if doc["kind"] == "page"}
    entries = []
    reverse = {}
    for pattern in registry["patterns"]:
        area = candidate_area(pattern, chapters)
        pages = page_candidates(pattern, area, documents, headings)
        entries.append({
            "pattern_id": pattern["id"],
            "catalog_name": pattern["catalog_name"],
            "family": pattern["family"],
            "candidate_area": area,
            "candidate_pages": pages,
            "technical_state": "not-yet-assessed",
            "decision_state": "not-yet-assessed",
            "dimensions_state": "not-yet-assessed",
            "notes": "Phase 1 routing hypothesis only; no page audit or source claim.",
        })
        for page in pages:
            if page["confidence"] == "weak":
                continue
            reverse.setdefault(page["document_id"], {
                "document_id": page["document_id"],
                "path": page["path"],
                "title": page["title"],
                "pattern_ids": [],
            })["pattern_ids"].append(pattern["id"])
    coverage = {
        "schema_version": 1,
        "registry_version": registry["registry_version"],
        "registry_sha256": hashlib.sha256(
            (root / "edition/patterns/registry.v1.json").read_bytes()
        ).hexdigest(),
        "route_index_snapshot": index_doc["snapshot_sha256"],
        "status": "candidate-only",
        "entries": entries,
        "summary": {
            "entries": len(entries),
            "entries_with_any_candidate": sum(bool(item["candidate_pages"]) for item in entries),
            "entries_with_strong_or_medium": sum(
                any(page["confidence"] in ("strong", "medium")
                    for page in item["candidate_pages"])
                for item in entries
            ),
            "entries_without_strong_or_medium": sum(
                not any(page["confidence"] in ("strong", "medium")
                        for page in item["candidate_pages"])
                for item in entries
            ),
            "by_confidence": {
                level: sum(1 for item in entries for page in item["candidate_pages"]
                           if page["confidence"] == level)
                for level in ("strong", "medium", "weak")
            },
            "reverse_documents": len(reverse),
        },
        "scope": "Candidate routing only; not page coverage, source reading or technical acceptance.",
    }
    reverse_map = {
        "schema_version": 1,
        "route_index_snapshot": index_doc["snapshot_sha256"],
        "documents": [reverse[key] for key in sorted(reverse)],
        "scope": "Reverse view of candidate coverage-map links only.",
    }
    return coverage, reverse_map


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    try:
        coverage, reverse = build(root)
        if args.write:
            (root / COVERAGE).write_text(json.dumps(coverage, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
            (root / REVERSE).write_text(json.dumps(reverse, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        if args.check:
            require((root / COVERAGE).is_file() and (root / REVERSE).is_file(),
                    "coverage-files-missing")
            require(load(root / COVERAGE) == coverage, "coverage-map-stale")
            require(load(root / REVERSE) == reverse, "reverse-map-stale")
        if args.json:
            print(json.dumps(coverage["summary"], indent=2))
        else:
            print("Pattern coverage:", coverage["summary"])
    except (ValueError, OSError, KeyError) as exc:
        print("FAIL:", exc, file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
