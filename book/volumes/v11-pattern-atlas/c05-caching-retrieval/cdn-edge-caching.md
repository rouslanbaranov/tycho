---
metadata_version: 1
id: "tycho.page.2ec1eb872ed5f04ba10d4821f7645980"
kind: "page"
parent_id: "tycho.chapter.87e52392e206a451ea5c79a4194c384b"
canonical_path: "book/volumes/v11-pattern-atlas/c05-caching-retrieval/cdn-edge-caching.md"
title: "CDN / Edge Caching"
topic_ids:
  - "performance-engineering"
  - "data-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Decision card for CDN / Edge Caching with bounded owner evidence."
route_hints:
  questions:
    - "Should content be cached at the edge close to clients rather than only at the origin?"
  prerequisites:
    - "tycho.chapter.87e52392e206a451ea5c79a4194c384b"
  related_ids:
    - "tycho.chapter.87e52392e206a451ea5c79a4194c384b"
  excludes:
    - "No sufficient coverage, promotion or owner acceptance is claimed for this moved card."
  keywords:
    - "pattern atlas"
    - "cdn / edge caching"
    - "caching"
evidence_scope:
  source_ids:
    - "src.microsoft-cloud-patterns"
    - "src.rfc9111-enrichment"
  claim_ids: []
  status: "source-linked"
  notes: >-
    Card cites read.batch3-ms-static.2026-10-21, RFC 9111 and the Azure CDN and
    CloudFront records; owner section and limits are bounded.
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-30"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-30"
updated_at: "2026-10-30"
source_inspection_date: "2026-10-30"
content_verified_at: null
---
# CDN / Edge Caching

**Identity.** CDN / Edge Caching; family Caching and retrieval; kind caching-pattern;
priority core.

**Decision question.** Should content be cached at the edge close to clients rather than
only at the origin?

**Good-fit conditions.** Content is shareable and versioned; every request value
that changes the response is in the cache key; authorization is enforced outside
the reusable representation or bound to that key; origin protection and purge
are owned; edge failure is handled.

**Hard contraindications.** Reject when every response is user-specific, when
origin authorization depends on a header absent from the key, when purge cannot
meet the freshness or revocation contract, or when edge configuration is
unowned.

**Competing alternative.** A private cache, origin cache or direct origin.
Reverse the choice when responses are user-specific or the purge contract
cannot be enforced.

**Failure and recovery.** Stale private content, purge lag and downstream
copies are common; test the authorization matrix, stale-on-error path and purge
path in the owner section.

**Technical owner.** [CDN / Edge Caching](../../v08-delivery-deployment-and-recovery/c08-network-request-paths-routing-and-edge-delivery/edge-cache-origin.md#cdn-edge-caching) — edge caching is bounded, not a CDN product manual.

**Sources.**
[src.microsoft-cloud-patterns](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch3-ms-static.2026-10-21: all nine served headings read.
The source is a public pattern/documentation
unit, not a benchmark. Additional bindings read 2026-10-30: RFC 9111
(`src.rfc9111-enrichment`) sections 3.5, 4, 4.1, 4.4, 5.2.2.5 and 5.2.2.7;
Azure CDN caching and purge pages; CloudFront cache-key, Authorization,
expiration and
invalidation pages. The owner section carries record hashes; their metadata is
registered in the reading ledger.

**Decision state.** applicable-under-conditions.

**Related entries.** Cache Invalidation; TTL-Based Expiration; Negative Caching;
Multi-Level Caching.
