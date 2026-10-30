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
updated_at: "2026-10-30"
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
> [Write-Behind / Write-Back](../../v11-pattern-atlas/c05-caching-retrieval/README.md#write-behind--write-back) — decision conditions and contraindications.
> [Write-Around](../../v11-pattern-atlas/c05-caching-retrieval/README.md#write-around) — decision conditions and contraindications.
> [Multi-Level Caching](../../v11-pattern-atlas/c05-caching-retrieval/README.md#multi-level-caching) — decision conditions and contraindications.

<!-- tycho-question-source:tycho.page.33742c54f667446cbf57cb9f3696a533:0 -->
## Purpose and mission

Caching trades extra, potentially stale copies for less source work and faster or cheaper common reads. Its architectural value depends on what information is safe to reuse, how long the copy may differ from authoritative state, and whether local or shared placement matches the demand profile.

This chapter owns **cache roles, authoritative ownership, local/shared placement, expiration and refresh policy**. [V06/C02 cache invalidation and stampede](../c02-hot-keys-cache-stampedes-and-read-amplification/cache-invalidation-stampede-and-hot-keys.md) owns concurrency races, hot-key collapse and source protection; they are closely related but not interchangeable questions.

**Distributed-cache mechanism.** A shared cache places copies outside a single process and
serves many instances over a network. It can reduce repeated source reads across replicas,
but adds serialization, network latency, a shared failure domain and cross-instance
freshness problems. Key scope, partitioning, TTL/invalidation, stampede control and
authorization must be explicit.

**Failure and alternative.** A cache outage can turn every miss into origin load; stale
tenant permissions or exclusive availability must not be served as harmless. Bound
concurrent fallback and define an overload response. A local cache, CDN, read replica or
no cache may be preferable when cross-instance freshness and shared-failure cost exceed the
reuse benefit.

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
concurrency, timeouts and error translation. A fill must carry the source version and must not
overwrite a newer committed value, and a read-through cache cannot make per-read application
authorization decisions. Cache-aside with application-owned fill keeps loading policy visible;
prefer read-through when the cache can call the source and the loading contract is uniform.

**Limits.** The cache must implement the source protocol, authentication and backpressure;
a bypass with different client semantics defeats the uniformity claim. A fill that hides source
errors is a correctness defect, not a performance choice.

### Write-Through Cache

A write-through path updates the cache and the authoritative store in one controlled sequence, so a
later read can use the cached copy. A write must not be acknowledged before both sides reach the
declared state, or an explicit reconciliation must repair a partial write. The declared order is
store commit, then cache update; a reader that sees the new cache value can rely on the store,
while a reader that sees the old cache value must be treated as stale. If the cache update fails,
invalidate and repair before serving. A retry carries the same version and must not overwrite a
newer write.

Failure between the two updates leaves cache and store divergent; version the value and retry or
invalidate with an audit trail of the failed write. Write-behind or cache-aside with invalidation
reduces write latency; choose write-through when read-after-write freshness outweighs the extra
write cost.

**Limits.** It doubles write cost and still needs retry/idempotency; a cache and store pair
without a shared transaction cannot promise atomicity. A version check must prevent a late retry
from overwriting a newer write.

### Write-Behind-Write-Back

A write-behind cache acknowledges a write after placing it in a pending buffer and flushes it to
durable storage asynchronously. If that buffer is the cache itself, cache loss can discard
acknowledged writes; that is the card's hard contraindication. If the buffer has its own durable
or replicated record separate from the cache, cache loss is recoverable and the acknowledged write
survives. State which case applies; never include durable acknowledged writes in a permitted loss
window.

Write-through acknowledges only after both sides update; prefer write-behind when write throughput
dominates and a measured loss window is acceptable for at-risk writes, not for durable acknowledged
writes.

**Limits.** Flush ordering, retry and shutdown drain are part of the durability contract; an
unbounded backlog silently breaks the declared loss window. Batch flushes must preserve per-key
order, and a restart must replay the pending buffer before accepting new writes. An owner must reconcile
the backlog after a prolonged outage.

### Write-Around

A write-around policy writes directly to the authoritative store and does not populate the cache,
leaving later reads to fill it. A cached copy must be invalidated or versioned at the update, or a
later read can restore a value older than the committed write.

A stale entry survives the update and is served until it expires; the policy requires reliable
invalidation or versioning at the update and a read test immediately after a write. A bounded
TTL alone does not meet the card's fit condition when invalidation is unreliable. Write-through
keeps the cache current at the cost of write amplification; choose write-around when write volume
is high and later reads can tolerate a refill.

**Limits.** It shifts cost to later reads and increases cold-miss load; latency-critical paths
may need prewarming or a bounded fallback. Invalidation timing is part of the read contract.

### Multi-Level Caching

A multi-level cache keeps a fast local tier in front of a shared tier, trading fewer remote reads
for more places that can hold a stale copy. Hazelcast describes a Near Cache as a copy of
distributed data "in local memory for very fast access" that is "eventually consistent"; it warns
that "Strong consistency is not maintained; you might read stale data." Redis client-side caching
maintains a local cache that "reduces network traffic between a Redis client and the server, which
generally improves performance," but "cache misses, tracking, and invalidation messages always add
a slight performance penalty."

**Invariant (Tycho synthesis).** Every tier must receive the invalidation, or it must detect a
missed invalidation and bound how long a stale copy can be served. The selected sources support
the parts. Hazelcast says invalidation events "can be lost due to the fire-and-forget fashion of
the eventing system" and that "If an event is lost, reads from Near Cache can indefinitely be
stale"; it detects invalidation losses and, after detection, makes stale data unreachable and
directs reads "to the underlying IMap/JCache to fetch the fresh data." Redis sends "an invalidation
message to all clients that have accessed that key previously" when a tracked key is written, and
"If any connection from a client gets disconnected (including one from a connection pool), then
the client will flush all keys from the client-side cache." AWS Well-Architected says to
"Configure a cache invalidation strategy, such as a time-to-live (TTL), for all data that balances
freshness of data and reducing pressure on backend datastore." Tycho guidance: a version check is
one way to enforce the bound; no selected source states it as a per-tier requirement. The
disjunction and per-tier scope are Tycho synthesis; the sources describe one local tier, not every
cache topology. Test the bound for every tier, including after a cold start and a rolling deploy.

**Failure and recovery.** Tier divergence serves different values from different processes;
version keys and measure the propagation delay of each invalidation path. A lost invalidation is
a common cause: Hazelcast detects the loss and directs reads to the underlying structure, Redis
flushes the local cache on disconnect, and a TTL bounds the stale copy. Test the lost-invalidation,
disconnect-flush and TTL paths, including after a cold start and a rolling deploy.

**Alternative (Tycho synthesis).** A remote cache avoids duplicate local copies and gives "more
consistent responses between clients, better efficiency in stored data"; its cost is "higher
latency, as an additional network hop is required to check the remote cache." A local tier stores
data "in the closest location possible (the client itself), resulting in the lowest possible
latency," but duplicate copies create "data inconsistency between those clients." AWS says
client-side caching "can be used alongside remote caching for multi-level caching to improve the
latency." Tycho guidance: add a local tier only when measured remote-read cost exceeds the
staleness and invalidation effort; a local-only cache is the alternative when invalidation paths
cannot be bounded, and it gives up the shared copy. The promotion rule is also Tycho guidance:
promote a value to the local tier only after the shared tier accepts the version.

**Limits.** Each added tier multiplies invalidation paths and failure modes; a tier without an
owner becomes an unbounded stale copy. The selected sources document product behavior and general
guidance, not this book's deployment. No cache cluster was configured, no invalidation was run and
no latency was measured. Test each tier during a rolling deploy and after a cold start.

- Hazelcast, "Near Cache", `read.hazelcast-near-cache.2026-10-30`, version 5.6,
  HTML `3dafe42787ec7b957abf573e69f9ad506eb3a7cec4b1031372b9e7b506e1af7f`,
  article text `7a90d5773194eebdc81c567da7a8eebf7550b0669e156cd9398ab0013486b70e`:
  local-copy, eventual-consistency, invalidation-loss and loss-detection statements.
- Redis, "Client-side caching introduction",
  `read.redis-client-side-caching.2026-10-30`, HTML
  `2fe5199edb619ef4fc3bc17d72312ba5b356ce061c0ca82b2950a10cae15561d`, main text
  `cd9a01d947a7526971b77d903ae2b37845ad2cabf4115a26dd17dc5a26485f20`:
  local-cache, tracking, invalidation and disconnect-flush statements.
- AWS, "PERF03-BP05 Implement data access patterns that utilize caching",
  `read.aws-caching-guidance.2026-10-30`, Markdown
  `2a8596fad95cec9fcea60751e31a9190a76fcb0f773ee83c1c51d8775ff83ceb`:
  client-side, remote and multi-level caching statements and the TTL invalidation step.

### Distributed Cache

A distributed cache places the shared value outside any one application instance so replicas see
one cached representation. API replicas A and B cache the same inventory availability record,
authoritative database revision v17. The cache is a shared dependency with its own failure domain.

Never treat cached tenant permissions or exclusive availability as harmlessly stale without the
actual security/domain owner's approval. The cache's partitioning, replication and replica
ownership are part of its failure domain: define which replica is authoritative for a key and how
a stale replica is detected. Blind bypass can turn a cache incident into an authoritative database
overload. Define bounded concurrent fallback, explicit overload response and whether stale public
descriptions may be served.

Fail the cache strategy if user-visible freshness or pool budgets are breached; a direct
authoritative query with better indexes may be the lower-risk alternative. A distributed cache is a
fit when the shared hit rate and latency justify a network hop and the fallback is bounded.
