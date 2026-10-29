---
metadata_version: 1
id: "tycho.page.0eb276434c29430e99bb17a65bc0ade9"
kind: "page"
parent_id: "tycho.chapter.87e52392e206a451ea5c79a4194c384b"
canonical_path: "book/volumes/v11-pattern-atlas/c05-caching-retrieval/cache-invalidation.md"
title: "Cache Invalidation"
topic_ids:
  - "performance-engineering"
  - "data-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Decision card for Cache Invalidation with bounded owner evidence."
route_hints:
  questions:
    - "Should cached entries be removed or refreshed when the authoritative value changes?"
  prerequisites:
    - "tycho.chapter.87e52392e206a451ea5c79a4194c384b"
  related_ids:
    - "tycho.chapter.87e52392e206a451ea5c79a4194c384b"
  excludes:
    - "No sufficient coverage, promotion or owner acceptance is claimed for this moved card."
  keywords:
    - "pattern atlas"
    - "cache invalidation"
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
# Cache Invalidation

**Identity.** Cache Invalidation; family Caching and retrieval; kind caching-pattern;
priority core.

**Decision question.** Should cached entries be removed or refreshed when the
authoritative value changes?

**Good-fit conditions.** The authoritative change can emit an invalidation signal; consumers
can tolerate a bounded stale window.

**Hard contraindications.** Reject when no reliable invalidation path exists or stale reads
violate a hard contract.

**Competing alternative.** Expiration after a configured period.

**Failure and recovery.** A reader can miss or briefly see stale data immediately after a
write.

**Technical owner.** [Cache invalidation, stampedes and hot-key failure modes](../../v06-caching-indexing-and-retrieval/c02-hot-keys-cache-stampedes-and-read-amplification/cache-invalidation-stampede-and-hot-keys.md#cache-invalidation) — invalidation is bounded, not a complete invalidation matrix.

**Sources.**
[src.microsoft-caching-guidance](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch3-ms-caching.2026-10-21: sections "Keep the cache consistent on
writes", "Invalidate data in a client-side cache". The source is a public
pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** TTL-Based Expiration; Cache-Aside; Stale-While-Revalidate;
Write-Around.
