---
metadata_version: 1
id: tycho.page.5e99f672b9cae686c28d5a6d161c1fdf
kind: page
parent_id: tycho.chapter.87e52392e206a451ea5c79a4194c384b
canonical_path: book/volumes/v11-pattern-atlas/c05-caching-retrieval/write-around.md
title: Write-Around
topic_ids:
- caching
perspectives:
- architecture
- operations
- evaluation
summary: Decision card for Write-Around.
route_hints:
  questions:
  - Should writes bypass the cache and invalidate or refresh it later?
  prerequisites:
  - tycho.chapter.87e52392e206a451ea5c79a4194c384b
  related_ids:
  - tycho.chapter.87e52392e206a451ea5c79a4194c384b
  excludes:
  - No owner acceptance is claimed for this card.
  keywords:
  - pattern atlas
  - write around
evidence_scope:
  source_ids:
  - src.microsoft-caching-guidance
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

# Write-Around

**Identity.** Write-Around; family Caching and retrieval; kind caching-pattern; priority
advanced.

**Decision question.** Should writes bypass the cache and invalidate or refresh it later?

**Good-fit conditions.** Writes are large or infrequent; cached reads can tolerate a miss
after write; invalidation is reliable.

**Hard contraindications.** Reject when read-after-write freshness is required, when
invalidation is unreliable, or when the miss penalty is unacceptable.

**Competing alternative.** Write-through or write-behind. Reverse the choice when
post-write misses dominate the read path.

**Failure and recovery.** Stale entries after invalidation failure are common; verify
invalidation in the owner section.

**Technical owner.**
 [Local and distributed caching: authority, freshness and
placement](../../v06-caching-indexing-and-retrieval/c01-local-and-distributed-caching/local-and-distributed-cache-design.md#write-around)
— write-around freshness and miss path are bounded; prefetch policy is page-specific.

**Sources.**
[src.microsoft-caching-guidance](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch3-ms-caching.2026-10-21: sections "Keep the cache consistent on
writes", "Manage data expiration in a cache". The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Write-Through; Cache Invalidation; TTL-Based Expiration; Cache-Aside.
