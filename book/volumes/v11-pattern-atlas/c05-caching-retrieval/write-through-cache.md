---
metadata_version: 1
id: tycho.page.5fb7eaf260a79203576f73f9a9dad5c3
kind: page
parent_id: tycho.chapter.87e52392e206a451ea5c79a4194c384b
canonical_path: book/volumes/v11-pattern-atlas/c05-caching-retrieval/write-through-cache.md
title: Write-Through Cache
topic_ids:
- caching
perspectives:
- architecture
- operations
- evaluation
summary: Decision card for Write-Through Cache.
route_hints:
  questions:
  - Should every write update the cache and the authoritative store together?
  prerequisites:
  - tycho.chapter.87e52392e206a451ea5c79a4194c384b
  related_ids:
  - tycho.chapter.87e52392e206a451ea5c79a4194c384b
  excludes:
  - No owner acceptance is claimed for this card.
  keywords:
  - pattern atlas
  - write through cache
evidence_scope:
  source_ids:
  - src.aws-caching-strategies
  claim_ids: []
  status: source-linked
  notes: Source-level bindings remain in the owner unit.
content_review:
  status: self-checked
  reviewed_at: '2026-11-01'
  reviewer: Automated authoring agent
  proof_uri: null
authored_at: '2026-11-01'
updated_at: '2026-11-01'
source_inspection_date: '2026-10-21'
content_verified_at: null
---

# Write-Through Cache

**Identity.** Write-Through Cache; family Caching and retrieval; kind caching-pattern;
priority core.

**Decision question.** Should every write update the cache and the authoritative store
together?

**Good-fit conditions.** Writes are not dominated by high volume; consistency between
cache and store matters; failure of either side is handled.

**Hard contraindications.** Reject when write latency is critical, when the store cannot
participate in a reliable sequence, or when partial failure has no reconciliation.

**Competing alternative.** Write-behind or cache-aside with invalidation. Reverse the
choice when write amplification or dual-write failure dominates.

**Failure and recovery.** Partial writes and stale cache entries are common; verify
ordering in the owner section.

**Technical owner.**
 [Local and distributed caching: authority, freshness and
placement](../../v06-caching-indexing-and-retrieval/c01-local-and-distributed-caching/local-and-distributed-cache-design.md#write-through-cache)
— write-through ordering and acknowledgement are bounded; backend durability is page-specific.

**Sources.**
[src.aws-caching-strategies](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch3-aws-caching.2026-10-21: sections "Caching patterns",
"Write-Through". The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Write-Behind; Cache-Aside; Cache Invalidation; Distributed Cache.
