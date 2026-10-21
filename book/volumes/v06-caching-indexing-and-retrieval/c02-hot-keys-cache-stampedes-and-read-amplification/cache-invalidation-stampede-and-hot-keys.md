---
metadata_version: 1
id: "tycho.page.e0f0d5b68f834acbae94cc6714895dd3"
kind: "page"
parent_id: "tycho.chapter.1035327a459242b78329b41b8fddfee6"
canonical_path: "book/volumes/v06-caching-indexing-and-retrieval/c02-hot-keys-cache-stampedes-and-read-amplification/cache-invalidation-stampede-and-hot-keys.md"
title: "Cache invalidation, stampedes and hot-key failure modes"
topic_ids:
  - "scaling-mechanisms"
perspectives:
  - "architecture"
summary: "Integrated decision and bounded source limits for Hot keys, cache stampedes and read amplification. Detailed mechanisms have separate question owners."
route_hints:
  questions:
    - "When does adding a cache worsen recovery or contention?"
  prerequisites: []
  related_ids:
    - "tycho.page.ded52d8d012347b79d70e608488cf6a4"
    - "tycho.page.33742c54f667446cbf57cb9f3696a533"
    - "tycho.page.c5d20ae7ef6445e5b23dd5fbac625060"
    - "tycho.landing.1a9054fd18f64dfe911f34a4d17458c0"
    - "tycho.landing.73dff529d70048569efef74bffa88b00"
    - "tycho.page.dc2470904e004a4aa733abcdb25517ed"
    - "tycho.page.028aab692b414bcdba7713500ab6f735"
    - "tycho.page.edc267f2fa954e66891e006ddfbfb15f"
    - "tycho.page.f077c7f124b54e2a8137cec267d9170a"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Cache"
    - "invalidation"
    - "stampedes"
    - "and"
    - "hot-key"
    - "failure"
    - "modes"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Only exact URL matches to the global source register are normalized here. Page-local case and evidence ledger IDs remain in the body; no claim-level mapping or source inspection is inferred."
content_review:
  status: "draft"
  reviewed_at: null
  reviewer: null
  proof_uri: null
authored_at: "2026-10-19"
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---
<!-- tycho-question-source:tycho.page.e0f0d5b68f834acbae94cc6714895dd3:-1 -->

# Cache invalidation, stampedes and hot-key failure modes

> **Original Tycho V06/C02 chapter draft**, 2026-10-19. Public Caffeine refresh, Redis cache-aside and EXPIRE sources describe mechanisms. All races and load examples here are educational inventions; no cache, Redis lock, version guard, database or benchmark was run or reviewed. The earlier [combined cache research](../../../scaling/local-distributed-caching-and-invalidation.md) remains intact until claims are reconciled.

<!-- /tycho-question-source -->

> **Pattern atlas:**
> [Cache Invalidation](../../v11-pattern-atlas/c05-caching-retrieval/README.md#cache-invalidation) — decision conditions and contraindications.

<!-- tycho-question-source:tycho.page.e0f0d5b68f834acbae94cc6714895dd3:0 -->
## Purpose and mission

A cache may perform well under ordinary traffic and become a **load amplifier** precisely during a key expiration, a write burst or an outage. Expiring an entry and asking all waiting clients to refetch it can overload a healthy authoritative store. Invalidating after a write can also be undone by a slower in-flight read filling an obsolete value.

This chapter owns concurrent cache correctness and overload boundaries. [V06/C01 cache placement and freshness](../c01-local-and-distributed-caching/local-and-distributed-cache-design.md) owns local/shared/no-cache choice and base TTL/refresh semantics. [V07/C05 overload protection](../../v07-performance-scale-and-resilience/c05-overload-protection-and-graceful-degradation/overload-admission-control-and-graceful-degradation.md) owns general system admission policies.

<!-- /tycho-question-source -->

## Integrated decision and reading route

Bound regeneration, hot-key fan-out and cold-start demand as part of cache recovery.

A cache outage or simultaneous expiry can concentrate traffic on the protected origin and amplify the original failure.

The detailed pages separate the mechanisms that make this decision conditional:

- [Stale fills and regeneration ownership](stale-fill.md) — Which version or fencing rule prevents a refresh from publishing obsolete state?
- [Stampedes and source protection](stampede-protection.md) — How do expiry and cache loss concentrate demand on the origin?
- [Negative caching and discriminating experiments](negative-cache.md) — Which revoked permission or absent value makes cached absence unsafe?

[Chapter introduction, ordered pages and full source ledger](README.md). Original source labels retain their historical scope; this editorial decomposition does not turn proposed experiments into executed evidence.

## Bounded pattern ownership notes

These notes define the decision boundary for atlas cards whose mechanism is not the main subject of
this page. They are synthetic design guidance, not measured evidence, and they do not create a new
source claim.

### Cache Invalidation

Cache invalidation removes or versions a cached entry when the authoritative value changes, so a
later read cannot reuse the superseded copy. The invalidation must be ordered with the write or
guarded by a version, and a failed invalidation must remain visible rather than silently skipped.

A lost invalidation or an in-flight fill resurrects stale data; bound the TTL, compare versions on
fill and record invalidations that failed. A short TTL accepts bounded staleness without a purge
path; use explicit invalidation when the allowed staleness is shorter than the TTL that is
affordable.
