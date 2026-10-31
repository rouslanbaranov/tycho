---
metadata_version: 1
id: "tycho.page.c0fca8b9b51a3b1080e177f58741e9f9"
kind: "page"
parent_id: "tycho.chapter.87e52392e206a451ea5c79a4194c384b"
canonical_path: "book/volumes/v11-pattern-atlas/c05-caching-retrieval/cache-stampede.md"
title: "Cache Stampede Protection"
topic_ids:
  - "performance-engineering"
  - "data-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: >-
  Decision card for Cache Stampede Protection; all four dimensions
  source-bound; coverage remains partial-bounded, no promotion.
route_hints:
  questions:
    - >-
      Should concurrent misses be coordinated so they do not all hit the
      source at once?
  prerequisites:
    - "tycho.chapter.87e52392e206a451ea5c79a4194c384b"
  related_ids:
    - "tycho.chapter.87e52392e206a451ea5c79a4194c384b"
  excludes:
    - >-
      No sufficient coverage, promotion or owner acceptance is claimed for this
      moved page.
  keywords:
    - "pattern atlas"
    - "cache stampede"
    - "caching and retrieval"
evidence_scope:
  source_ids:
    - "src.cloudflare-cache-stampede"
    - "src.aws-caching-challenges"
    - "src.redis"
    - "src.go-singleflight"
    - "src.aws-ttl-jitter"
    - "src.aws-per-cache-stampede"
    - "src.microsoft-caching-guidance"
  claim_ids: []
  status: "source-linked"
  notes: >-
    Card cites read.cloudflare-sometimes-i-cache.2026-10-31,
    read.aws-caching-challenges.2026-10-31,
    read.redis-distributed-locks.2026-10-31,
    read.go-singleflight.2026-10-31,
    read.aws-valkey-ttl-jitter.2026-10-31,
    read.aws-community-per.2026-10-31 and retained
    read.batch3-ms-caching.2026-10-21; owner section and limits are bounded.
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-31"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-31"
updated_at: "2026-10-31"
source_inspection_date: "2026-10-31"
content_verified_at: null
---
# Cache Stampede Protection

**Identity.** Cache Stampede Protection; family Caching and retrieval; kind
caching-pattern; priority core.

**Decision question.** Should concurrent misses be coordinated so they do not all hit the
source at once?

**Good-fit conditions.** A hot key can expire under load; source capacity is limited; a
wait/reject/declared-stale contract is available; coordination failure has a fallback;
duplicate fills are acceptable.

**Hard contraindications.** Reject when the source can absorb the miss burst, when one
coordination point would block all callers, when waiters need independent cancellation or
differing authorization, or when single-flight state and lease fencing have no owner.

**Competing alternative.** TTL jitter, probabilistic early expiration, prewarming, or
request coalescing. Reverse the choice when coordination latency and failure outweigh source
protection.

**Failure and recovery.** Lease loss, lock-service unavailability, retry storms and
expired-lease double refresh are common; a leader error is shared by every waiter; measure
origin QPS, coalesce refreshes and cap source admission.

**Technical owner.** [Cache Stampede Protection](../../v06-caching-indexing-and-retrieval/c02-hot-keys-cache-stampedes-and-read-amplification/stampede-protection.md#cache-stampede-protection) — stampede protection is bounded, not a single-flight implementation.

**Sources.**

- Cloudflare, *Sometimes I cache: implementing lock-free probabilistic caching*:
  "When the image server sees these 10 requests all happening at the same time, it gets
  overloaded." Record `read.cloudflare-sometimes-i-cache.2026-10-31`; canonical text
  SHA-256 `1095c942825ca57d17f82796398957e8dfa6fac01eb7fe2c0a47b52752220a19`.
- AWS Builders' Library, *Caching challenges and strategies*: "To remedy this issue we use
  request coalescing, where the servers or external cache ensure that only one pending
  request is out for uncached resources." Record `read.aws-caching-challenges.2026-10-31`;
  canonical text SHA-256
  `55f310713a99dd8282b6e4e569538462793e6387a3c1ca6251a6aa1c42e739a1`.
- Redis, *Distributed Locks with Redis*: "Safety property: Mutual exclusion. At any given
  moment, only one client can hold a lock"; "You should implement fencing tokens." Record
  `read.redis-distributed-locks.2026-10-31`; canonical text SHA-256
  `628a3026cdbad3121deb6f604d43f9e01317db9d0f7bb74f9ea4e1524291bb17`.
- Go, *singleflight package*: "Do executes and returns the results of the given function,
  making sure that only one execution is in-flight for a given key at a time." Record
  `read.go-singleflight.2026-10-31`; canonical text SHA-256
  `a3810adc75c789bbe3c59a2aa1ca627bcdedfc9962703c444234a99f225762c4`.
- AWS Builder Center, *Database Caching on AWS with Valkey*: "If a bunch of cache entries
  share the same TTL (and are written at the same time), they all expire at the same time.
  Suddenly every request is a cache miss and your database gets hammered. The fix is dead
  simple: ✨Jitter✨." Record `read.aws-valkey-ttl-jitter.2026-10-31`; canonical text
  SHA-256 `75b455cb1f36e9b17d840a5e20cacf68d56bd6a2d65e334098f3196d3451df07`.
- AWS Builder Center community article (Portuguese), *Resiliência Extrema em Camadas de
  Acesso a Dados*: describes an XFetch-style ElastiCache adapter; community content, not
  AWS documentation. Record `read.aws-community-per.2026-10-31`; canonical text SHA-256
  `631905b81459a0deb70c8c675b4ae76b68a9f41cd23fb0e6bb6472e77e7a0c0f`.
- Retained context:
  [src.microsoft-caching-guidance](../../../../edition/patterns/reading-ledger.v1.json)
  record `read.batch3-ms-caching.2026-10-21` covers cache concurrency and cold-cache/source
  overload, not stampede leases or coalescing. The sources are public documentation and
  articles, not benchmarks.

**Decision state.** applicable-under-conditions.

**Related entries.** Single Flight; TTL-Based Expiration; Cache Invalidation;
Stale-While-Revalidate.
