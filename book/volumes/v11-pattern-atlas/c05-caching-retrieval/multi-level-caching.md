---
metadata_version: 1
id: "tycho.page.9019c073a9804c5c99b236cd7752e78f"
kind: "page"
parent_id: "tycho.chapter.87e52392e206a451ea5c79a4194c384b"
canonical_path: "book/volumes/v11-pattern-atlas/c05-caching-retrieval/multi-level-caching.md"
title: "Multi-Level Caching"
topic_ids:
  - "performance-engineering"
  - "data-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Decision card for Multi-Level Caching with bounded owner evidence."
route_hints:
  questions:
    - "Should data be cached in more than one tier with different latency and freshness?"
  prerequisites:
    - "tycho.chapter.87e52392e206a451ea5c79a4194c384b"
  related_ids:
    - "tycho.chapter.87e52392e206a451ea5c79a4194c384b"
  excludes:
    - "No sufficient coverage, promotion or owner acceptance is claimed for this moved card."
  keywords:
    - "pattern atlas"
    - "multi-level caching"
    - "caching"
evidence_scope:
  source_ids:
    - "src.hazelcast"
    - "src.redis"
    - "src.aws-caching-guidance"
  claim_ids: []
  status: "source-linked"
  notes: >-
    Card cites read.batch3-hazelcast-near.2026-10-21 and the 2026-10-30
    Hazelcast, Redis and AWS records; owner section and limits are bounded.
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
# Multi-Level Caching

**Identity.** Multi-Level Caching; family Caching and retrieval; kind caching-pattern;
priority core.

**Decision question.** Should data be cached in more than one tier with different latency
and freshness?

**Good-fit conditions.** Each tier has a distinct role and a named freshness bound;
promotion and invalidation across tiers are owned; a missed invalidation is detected or
a TTL bounds the stale copy.

**Hard contraindications.** Reject when one tier suffices, when cross-tier invalidation
or a staleness bound cannot be tested, or when duplicate caching only adds inconsistency.

**Competing alternative.** Single shared remote cache or local-only cache. A shared cache
gives more consistent responses at the cost of a network hop; a local tier lowers latency
but duplicates data. Reverse the choice when coordination and invalidation cost exceeds
the latency benefit.

**Failure and recovery.** Cross-tier stale data and invalidation fan-out are common; test
the lost-invalidation, disconnect-flush and TTL bounds in the owner section.

**Technical owner.** [Local and distributed caching: authority, freshness and placement](../../v06-caching-indexing-and-retrieval/c01-local-and-distributed-caching/local-and-distributed-cache-design.md#multi-level-caching) — multi-level authority and coherence are bounded; per-tier eviction is page-specific.

**Sources.** [src.hazelcast](../../../../edition/patterns/reading-ledger.v1.json)
read records read.batch3-hazelcast-near.2026-10-21 and
read.hazelcast-near-cache.2026-10-30: Near Cache local-memory, eventual-consistency and
invalidation-loss statements. [src.redis](../../../../edition/patterns/reading-ledger.v1.json)
read record read.redis-client-side-caching.2026-10-30: local-cache, tracking,
invalidation and disconnect-flush statements.
[src.aws-caching-guidance](../../../../edition/patterns/reading-ledger.v1.json)
read record read.aws-caching-guidance.2026-10-30: client-side, remote and multi-level
caching statements and the TTL invalidation step. The owner section carries the exact
quotes and representation hashes; the 2026-10-30 records and the AWS source are
registered in the reading ledger. These are public documentation units, not benchmarks.

**Decision state.** applicable-under-conditions.

**Related entries.** Distributed Cache; Cache Invalidation; CDN / Edge Caching;
Cache-Aside.
