---
metadata_version: 1
id: "tycho.page.cf5d48a4f68b40f8890649805a798bf4"
kind: "page"
parent_id: "tycho.chapter.87e52392e206a451ea5c79a4194c384b"
canonical_path: "book/volumes/v11-pattern-atlas/c05-caching-retrieval/ttl-based-expiration.md"
title: "TTL-Based Expiration"
topic_ids:
  - "performance-engineering"
  - "data-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Decision card for TTL-Based Expiration with bounded owner evidence."
route_hints:
  questions:
    - "Should entries expire after a bounded time even without an explicit invalidation?"
  prerequisites:
    - "tycho.chapter.87e52392e206a451ea5c79a4194c384b"
  related_ids:
    - "tycho.chapter.87e52392e206a451ea5c79a4194c384b"
  excludes:
    - "No sufficient coverage, promotion or owner acceptance is claimed for this moved card."
  keywords:
    - "pattern atlas"
    - "ttl-based expiration"
    - "caching"
evidence_scope:
  source_ids:
    - "src.microsoft-caching-guidance"
  claim_ids: []
  status: "source-linked"
  notes: "Card cites read.batch3-ms-caching.2026-10-21; owner section and limits are bounded."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-29"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-29"
updated_at: "2026-10-29"
source_inspection_date: "2026-10-21"
content_verified_at: null
---
# TTL-Based Expiration

**Identity.** TTL-Based Expiration; family Caching and retrieval; kind caching-pattern;
priority core.

**Decision question.** Should entries expire after a bounded time even without an explicit
invalidation?

**Good-fit conditions.** The maximum acceptable stale window is at least the TTL; a reload
after expiry is acceptable; staleness is bounded by time.

**Hard contraindications.** Reject when data must be current and no shorter TTL or bypass
can meet the freshness contract, or when the TTL would exceed the acceptable stale window.

**Competing alternative.** A shorter TTL or a full bypass to the source data store.
Reverse the choice when data must be current and bounded staleness is unacceptable.

**Failure and recovery.** A long-lived cache can fill; adding items can then force
eviction of existing entries. The source states no recovery action. Tycho guidance:
monitor eviction and reload traffic, and size or partition the cache.

**Technical owner.** [TTL-Based Expiration](../../v06-caching-indexing-and-retrieval/c01-local-and-distributed-caching/refresh-semantics.md#ttl-based-expiration) — a bounded owner section, not a universal TTL policy.

**Sources.**
[src.microsoft-caching-guidance](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch3-ms-caching.2026-10-21: sections "Considerations for using caching",
"Caching and eventual consistency". The source is a public pattern/documentation unit, not
a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Cache Invalidation; Cache Stampede Protection; Negative Caching;
Stale-While-Revalidate.
