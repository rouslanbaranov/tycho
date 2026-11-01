---
metadata_version: 1
id: tycho.page.66b1abd75ba098b1c4eca281b5fcc3a8
kind: page
parent_id: tycho.chapter.87e52392e206a451ea5c79a4194c384b
canonical_path: book/volumes/v11-pattern-atlas/c05-caching-retrieval/read-through-cache.md
title: Read-Through Cache
topic_ids:
- caching
perspectives:
- architecture
- operations
- evaluation
summary: Decision card for Read-Through Cache.
route_hints:
  questions:
  - Should the cache layer load missing data on behalf of the application?
  prerequisites:
  - tycho.chapter.87e52392e206a451ea5c79a4194c384b
  related_ids:
  - tycho.chapter.87e52392e206a451ea5c79a4194c384b
  excludes:
  - No owner acceptance is claimed for this card.
  keywords:
  - pattern atlas
  - read through cache
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

# Read-Through Cache

**Identity.** Read-Through Cache; family Caching and retrieval; kind caching-pattern;
priority core.

**Decision question.** Should the cache layer load missing data on behalf of the
application?

**Good-fit conditions.** The cache can own loading and error mapping; the source contract
is stable; fill stampedes and stale data are handled.

**Hard contraindications.** Reject when the cache cannot safely call the source, when
application-specific authorization is needed for each read, or when fill failures are
hidden.

**Competing alternative.** Cache-aside with application-owned fill. Reverse the choice
when cache-layer coupling or opaque failures outweigh simpler fill logic.

**Failure and recovery.** Fill latency and error masking are common; verify loading
semantics in the owner section.

**Technical owner.**
 [Local and distributed caching: authority, freshness and
placement](../../v06-caching-indexing-and-retrieval/c01-local-and-distributed-caching/local-and-distributed-cache-design.md#read-through-cache)
— read-through freshness and authority are bounded; loader failure semantics are page-specific.

**Sources.**
[src.microsoft-caching-guidance](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch3-ms-caching.2026-10-21: sections "Caching in distributed
applications", "Implement caching patterns". The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Cache-Aside; Write-Through; Distributed Cache; Negative Caching.
