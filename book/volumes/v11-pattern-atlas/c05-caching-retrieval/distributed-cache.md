---
metadata_version: 1
id: tycho.page.02deb764ea6860b10b47d7404ac57e86
kind: page
parent_id: tycho.chapter.87e52392e206a451ea5c79a4194c384b
canonical_path: book/volumes/v11-pattern-atlas/c05-caching-retrieval/distributed-cache.md
title: Distributed Cache
topic_ids:
- caching
perspectives:
- architecture
- operations
- evaluation
summary: Decision card for Distributed Cache.
route_hints:
  questions:
  - Should cached data live in a shared distributed tier rather than only inside each
    process?
  prerequisites:
  - tycho.chapter.87e52392e206a451ea5c79a4194c384b
  related_ids:
  - tycho.chapter.87e52392e206a451ea5c79a4194c384b
  excludes:
  - No owner acceptance is claimed for this card.
  keywords:
  - pattern atlas
  - distributed cache
evidence_scope:
  source_ids:
  - src.hazelcast
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

# Distributed Cache

**Identity.** Distributed Cache; family Caching and retrieval; kind
infrastructure-pattern; priority core.

**Decision question.** Should cached data live in a shared distributed tier rather than
only inside each process?

**Good-fit conditions.** Multiple instances need shared freshness; the network hop is
acceptable; partitioning/replication and failure are owned.

**Hard contraindications.** Reject when local cache suffices, when the shared tier becomes
an unowned single point, or when network latency dominates the hit benefit.

**Competing alternative.** Local in-process cache or no cache. Reverse the choice when
distributed coordination cost exceeds cross-instance reuse.

**Failure and recovery.** Network partitions, stale replicas and a shared failure domain are
common; bound fallback so a cache outage does not overload the source.

**Technical owner.**
 [Distributed
Cache](../../v06-caching-indexing-and-retrieval/c01-local-and-distributed-caching/local-and-distributed-cache-design.md#distributed-cache)
— invalidation authority and freshness are bounded; topology and replication are owner-specific.

**Sources.** [src.hazelcast](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch3-hazelcast-cache.2026-10-21: all twelve served headings read. The source is
a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Multi-Level Caching; Cache-Aside; Cache Invalidation; CDN / Edge
Caching.
