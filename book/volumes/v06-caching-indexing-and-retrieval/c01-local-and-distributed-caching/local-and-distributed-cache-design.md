---
metadata_version: 1
id: "tycho.page.33742c54f667446cbf57cb9f3696a533"
kind: "page"
parent_id: "tycho.chapter.4166e932cbd64ce2a63fe0c6d6eb049a"
canonical_path: "book/volumes/v06-caching-indexing-and-retrieval/c01-local-and-distributed-caching/local-and-distributed-cache-design.md"
title: "Local and distributed caching: authority, freshness and placement"
topic_ids:
  - "scaling-mechanisms"
perspectives:
  - "architecture"
summary: "Integrated question, original scenario and transfer limits for Local and distributed caching. Detailed mechanisms have separate question owners."
route_hints:
  questions:
    - "How do authority, freshness, eviction and invalidation differ?"
  prerequisites: []
  related_ids:
    - "tycho.page.ded52d8d012347b79d70e608488cf6a4"
    - "tycho.page.e0f0d5b68f834acbae94cc6714895dd3"
    - "tycho.landing.1a9054fd18f64dfe911f34a4d17458c0"
    - "tycho.landing.73dff529d70048569efef74bffa88b00"
    - "tycho.page.dc2470904e004a4aa733abcdb25517ed"
    - "tycho.page.c5d20ae7ef6445e5b23dd5fbac625060"
    - "tycho.page.765a54f5d9944577908b40b3fc6cb7ef"
    - "tycho.page.76f6d792c80a448fa1a76001ca6699e1"
    - "tycho.page.f39fa61013ca41abbfba82ef48250f8f"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Local"
    - "and"
    - "distributed"
    - "caching"
    - "authority"
    - "freshness"
    - "placement"
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
<!-- tycho-question-source:tycho.page.33742c54f667446cbf57cb9f3696a533:-1 -->

# Local and distributed caching: authority, freshness and placement

> **Independent Tycho draft V06/C01, 2026-10-19.** Public Redis cache-aside and Caffeine eviction/refresh specifications inform the mechanism. All examples are invented. No application, cache server, performance test or independent reviewer was involved. The former [combined caching research](../../../scaling/local-distributed-caching-and-invalidation.md) is retained for source/claim reconciliation.

<!-- /tycho-question-source -->

> **Pattern atlas:**
> [Distributed Cache](../../v11-pattern-atlas/c05-caching-retrieval/README.md#distributed-cache) — decision conditions and contraindications.
> [Read-Through Cache](../../v11-pattern-atlas/c05-caching-retrieval/README.md#read-through-cache) — decision conditions and contraindications.
> [Write-Through Cache](../../v11-pattern-atlas/c05-caching-retrieval/README.md#write-through-cache) — decision conditions and contraindications.
> [Write-Behind / Write-Back](../../v11-pattern-atlas/c05-caching-retrieval/README.md#write-behind-write-back) — decision conditions and contraindications.
> [Write-Around](../../v11-pattern-atlas/c05-caching-retrieval/README.md#write-around) — decision conditions and contraindications.
> [Multi-Level Caching](../../v11-pattern-atlas/c05-caching-retrieval/README.md#multi-level-caching) — decision conditions and contraindications.

<!-- tycho-question-source:tycho.page.33742c54f667446cbf57cb9f3696a533:0 -->
## Purpose and mission

Caching trades extra, potentially stale copies for less source work and faster or cheaper common reads. Its architectural value depends on what information is safe to reuse, how long the copy may differ from authoritative state, and whether local or shared placement matches the demand profile.

This chapter owns **cache roles, authoritative ownership, local/shared placement, expiration and refresh policy**. [V06/C02 cache invalidation and stampede](../c02-hot-keys-cache-stampedes-and-read-amplification/cache-invalidation-stampede-and-hot-keys.md) owns concurrency races, hot-key collapse and source protection; they are closely related but not interchangeable questions.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.33742c54f667446cbf57cb9f3696a533:8 -->
## Engineering walkthrough — Local cache update versus cross-instance freshness

**Original synthetic topology:** API replicas A and B cache the same inventory availability record, authoritative database revision v17. A writes v18 and invalidates *its own* local cache. B continues serving v17 until TTL expiry. A successful local invalidation has not provided globally strong freshness.

| User requirement | Possible choice | Required failure proof |
|---|---|---|
| Public catalogue description may lag up to 30 s | Bounded TTL/local cache acceptable if measured | Worst-case age under clock skew, write burst and restart |
| Exclusive booking result must be current | Authoritative transaction or version-checked read | Stale value never authorizes duplicate confirmed allocation |
| Fast shared read model under load | Shared cache or invalidation bus | Redis/network loss, stale fill, authorization and fallback admission |

**Outage:** distributed cache becomes unavailable while 1,000 callers request one hot item. Blind bypass can turn a cache incident into an authoritative database overload. Define bounded concurrent fallback, explicit overload response and whether stale public descriptions may be served. Never treat cached tenant permissions or exclusive availability as harmlessly stale without the actual security/domain owner's approval.

The cache-aside and Caffeine eviction/refresh sources support mechanics but do not promise cross-replica coherence. **Proposed, not run:** perform a write on A while B is isolated from invalidation, then restore connectivity and measure staleness/incorrect decisions. Fail the cache strategy if user-visible freshness or pool budgets are breached; a direct authoritative query with better indexes may be the lower-risk alternative.

<!-- /tycho-question-source -->

## Integrated decision and reading route

Distinguish authoritative state from cached copies and define freshness, eviction and invalidation behavior.

A successful cache hit can return an inadmissibly stale value; cache availability is not authoritative correctness.

The detailed pages separate the mechanisms that make this decision conditional:

- [Authority, freshness and cache placement](cache-authority.md) — Which state remains authoritative when a local or distributed cache is used?
- [Eviction, refresh and cache-aside races](refresh-semantics.md) — Which read/write interleaving invalidates a naive freshness promise?
- [Cache cost, failure and acceptance](cache-acceptance.md) — When should stale service, origin protection or no cache be preferred?

[Chapter introduction, ordered pages and full source ledger](README.md). Original source labels retain their historical scope; this editorial decomposition does not turn proposed experiments into executed evidence.

## Bounded pattern ownership notes

These notes define the decision boundary for atlas cards whose mechanism is not the main subject of
this page. They are synthetic design guidance, not measured evidence, and they do not create a new
source claim.

### Read-Through Cache

A read-through cache loads a miss from the source on behalf of the caller and stores the result, so
the application never performs the fill itself. A fill failure must be returned or mapped
explicitly, never hidden as an ordinary cache miss, and concurrent fills must not stampede the
source.

Slow fills and error masking make the cache appear healthy while the source degrades; bound fill
concurrency, timeouts and error translation. Cache-aside with application-owned fill keeps loading
policy visible; prefer read-through when the cache can call the source and the loading contract is
uniform.

### Write-Through Cache

A write-through path updates the cache and the authoritative store in one controlled sequence, so a
later read can use the cached copy. A write must not be acknowledged before both sides reach the
declared state, or an explicit reconciliation must repair a partial write.

Failure between the two updates leaves cache and store divergent; version the value and retry or
invalidate with an audit trail of the failed write. Write-behind or cache-aside with invalidation
reduces write latency; choose write-through when read-after-write freshness outweighs the extra
write cost.

### Write-Behind / Write-Back

A write-behind cache acknowledges the cached write and flushes it to durable storage asynchronously.
An acknowledged write must survive the declared durability window, so the pending buffer needs its
own durable or replicated record.

Cache loss before flush discards acknowledged writes; track the flush backlog and make the
durability window explicit to callers. Write-through acknowledges only after both sides update;
prefer write-behind when write throughput dominates and a measured loss window is acceptable.

### Write-Around

A write-around policy writes directly to the authoritative store and does not populate the cache,
leaving later reads to fill it. A cached copy must be invalidated or versioned at the update, or a
later read can restore a value older than the committed write.

A stale entry survives the update and is served until it expires; pair the policy with invalidation
or a bounded TTL and test a read immediately after a write. Write-through keeps the cache current at
the cost of write amplification; choose write-around when write volume is high and later reads can
tolerate a refill.

### Multi-Level Caching

A multi-level cache keeps a fast local tier in front of a shared tier, trading fewer remote reads
for more places that can hold a stale copy. Every tier must receive the invalidation, or each tier
must carry a bounded staleness contract and a version check.

Tier divergence serves different values from different processes; version keys and measure the
propagation delay of each invalidation path. One shared cache keeps a single copy but pays remote
latency; add a local tier when the measured remote-read cost exceeds the staleness and invalidation
effort.
