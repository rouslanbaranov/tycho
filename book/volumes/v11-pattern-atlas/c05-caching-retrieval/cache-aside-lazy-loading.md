---
metadata_version: 1
id: "tycho.page.f1aadca8dc3848c1a0aafa83f0e13f83"
kind: "page"
parent_id: "tycho.chapter.87e52392e206a451ea5c79a4194c384b"
canonical_path: "book/volumes/v11-pattern-atlas/c05-caching-retrieval/cache-aside-lazy-loading.md"
title: "Cache-Aside / Lazy Loading"
topic_ids:
  - "performance-engineering"
  - "data-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: >-
  Decision card for Cache-Aside / Lazy Loading; source-anchored on the Azure
  Cache-Aside pattern, AWS ElastiCache best practices and caching strategies,
  and Redis cache-aside; coverage remains partial-bounded, no promotion.
route_hints:
  questions:
    - >-
      Should the application populate the cache after a miss instead of routing
      every read through the cache layer?
  prerequisites:
    - "tycho.chapter.87e52392e206a451ea5c79a4194c384b"
  related_ids:
    - "tycho.chapter.87e52392e206a451ea5c79a4194c384b"
    - "tycho.page.76f6d792c80a448fa1a76001ca6699e1"
  excludes:
    - >-
      No sufficient coverage, promotion or owner acceptance is claimed for this
      moved page.
  keywords:
    - "pattern atlas"
    - "cache-aside"
    - "lazy loading"
    - "caching and retrieval"
evidence_scope:
  source_ids:
    - "src.aws-caching-strategies"
    - "src.microsoft-cloud-patterns"
    - "src.redis-cache-aside"
  claim_ids: []
  status: "source-linked"
  notes: >-
    Card cites read.azure-cache-aside-pattern.2026-11-01,
    read.aws-elasticache-best-practices.2026-11-01,
    read.aws-caching-strategies.2026-11-01 and
    read.redis-cache-aside.2026-11-01; read.batch3-aws-caching.2026-10-21
    is retained as historical citation; owner section and limits are bounded.
content_review:
  status: "self-checked"
  reviewed_at: "2026-11-01"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-11-01"
updated_at: "2026-11-01"
source_inspection_date: "2026-11-01"
content_verified_at: null
---
# Cache-Aside / Lazy Loading

**Identity.** Cache-Aside / Lazy Loading; family Caching and retrieval; kind
caching-pattern; priority core.

**Decision question.** Should the application populate the cache after a miss instead of
routing every read through the cache layer?

**Good-fit conditions.** The application can own fill and invalidation; misses are
acceptable; duplicate fills are controlled; the source remains authoritative; a brief
stale window after a write is tolerable; the origin can absorb a fallback read.

**Hard contraindications.** Reject when every read must be served from cache, when fill
races cannot be controlled, when invalidation has no owner, or when the data is "sensitive
or security related" and must be retrieved "from the primary source".

**Competing alternative.** A shorter TTL with retried invalidation, or serving the read from
the source when its latency budget allows. Reverse when fill and invalidation logic becomes
duplicated and inconsistent.

**Failure and recovery.** A miss-only fill leaves "no updates to the cache when data is
changed in the database", so "data in the cache can become stale"; between a write and the
next read a reader can "briefly see stale data". Azure states that a malfunctioning cache
"can fall back to the origin data store", and AWS calls node failure survivable because a
replacement empty node continues to serve "though with increased latency"; Redis recommends
an atomic mutex or probabilistic early refresh against a key-expiry stampede. Tycho
guidance: gate fills by cached revision, distinguish a cold fill from a post-delete
tombstone, retry failed invalidation and use single-flight for concurrent misses.

**Technical owner.** [Cache-aside is a sequence, not a consistency theorem](../../v06-caching-indexing-and-retrieval/c01-local-and-distributed-caching/refresh-semantics.md#4-cache-aside-is-a-sequence-not-a-consistency-theorem) — the sequence is bounded, not a complete cache-aside library guide.

**Sources.** Four public units across three sources were inspected on 2026-11-01: the Microsoft
Azure Cache-Aside pattern, the AWS ElastiCache best-practices hub and its
caching-strategies child, and the Redis cache-aside page. Read records:
`read.azure-cache-aside-pattern.2026-11-01`,
`read.aws-elasticache-best-practices.2026-11-01`,
`read.aws-caching-strategies.2026-11-01` and
`read.redis-cache-aside.2026-11-01`. The retained
`read.batch3-aws-caching.2026-10-21` record supplies the historical
cache-aside citation. Source ids: `src.microsoft-cloud-patterns`,
`src.aws-caching-strategies` and `src.redis-cache-aside`. Public
documentation, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Read-Through Cache; Cache Invalidation; Cache Stampede Protection;
Distributed Cache.

**Limits.** The Azure page is living pattern documentation, the AWS page is
titled for Memcached and carries general strategy statements, and the Redis
page is a vendor use case. The stale-fill race, version gate, tombstone
distinction and durable invalidation are Tycho synthesis. No cache, origin,
node failure, stampede or revocation path was exercised. Coverage is
self-checked, not independently reviewed or promoted.
