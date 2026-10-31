---
metadata_version: 1
id: "tycho.chapter.87e52392e206a451ea5c79a4194c384b"
kind: "chapter"
parent_id: "tycho.volume.fe327f72cf81df0237ce47b841e8aef5"
canonical_path: "book/volumes/v11-pattern-atlas/c05-caching-retrieval/README.md"
title: "V11/C05 — Caching and retrieval"
topic_ids:
  - "performance-engineering"
  - "data-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: "All 14 C05 cards with bounded owner links; decision coverage partial."
route_hints:
  questions:
    - "Which cache patterns fit the authority and freshness contract?"
  prerequisites:
    - "tycho.chapter.b20625a099bc4c82b7d547c32c7da28a"
  related_ids:
    - "tycho.volume.fe327f72cf81df0237ce47b841e8aef5"
    - "tycho.chapter.b20625a099bc4c82b7d547c32c7da28a"
    - "tycho.chapter.e9c650012060143639af44b0cfdc4236"
    - "tycho.chapter.22fa23c6c7a6b0c29a52137bc67a00c9"
  excludes:
    - "Bounded owner links; no sufficient coverage or independent review."
  keywords:
    - "pattern atlas"
    - "caching and retrieval"
    - "decision layer"
evidence_scope:
  source_ids:
    - "src.hazelcast"
    - "src.aws-caching-strategies"
    - "src.microsoft-caching-guidance"
    - "src.redis"
    - "src.google-cdn-negative-caching"
    - "src.rfc5861"
    - "src.rfc9111-enrichment"
    - "src.mdn-cache-control"
    - "src.microsoft-cloud-patterns"
    - "src.cloudfront"
    - "src.cloudflare-cache-status"
    - "src.owasp-authorization-decisions"
  claim_ids: []
  status: "source-linked"
  notes: >-
    14 cards cite read units; owner links are bounded. Negative Caching binds
    invariant, failure/recovery and alternative on 2026-10-31 to RFC 9111,
    CloudFront status-code processing, OWASP authorization-decision guidance
    and Cloudflare cache-by-status-code defaults; per-status TTL context is
    retained from Google Cloud CDN.
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-31"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-21"
updated_at: "2026-10-31"
source_inspection_date: "2026-10-31"
content_verified_at: null
---
# V11/C05 — Caching and retrieval

**Owning question:** Which cache patterns fit the authority and freshness contract?

## Purpose and mission

This chapter is the atlas entry point for **Caching and retrieval**. It owns the
conditional decision route for 14 catalog entries, not the deep mechanism explanations.
Read the exact owner section before applying a mechanism claim.

All 14 entries have a self-checked card. Owner sections are bounded: a caching page may
own authority/freshness without owning every cache implementation.

## Pages and reasoning route

Page count is content-dependent. This chapter uses a landing page plus dedicated card
pages for moved entries; a later split is an editorial change, not a plan failure. Start
with the card, check its conditions and contraindications, then read the exact owner
section.

## Entry inventory

Each level-three heading is a stable atlas anchor. Owner links are bounded sections;
none claims sufficient technical or decision coverage.

### Distributed Cache

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

**Technical owner.** [Distributed Cache](../../v06-caching-indexing-and-retrieval/c01-local-and-distributed-caching/local-and-distributed-cache-design.md#distributed-cache) — invalidation authority and freshness are bounded; topology and replication are owner-specific.

**Sources.** [src.hazelcast](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch3-hazelcast-cache.2026-10-21: all twelve served headings read. The source is
a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Multi-Level Caching; Cache-Aside; Cache Invalidation; CDN / Edge
Caching.

### Cache-Aside / Lazy Loading

**Identity.** Cache-Aside / Lazy Loading; family Caching and retrieval; kind
caching-pattern; priority core.

**Decision question.** Should the application populate the cache after a miss instead of
routing every read through the cache layer?

**Good-fit conditions.** The application can own fill and invalidation; misses are
acceptable; duplicate fills are controlled; the source remains authoritative.

**Hard contraindications.** Reject when every read must be served from cache, when fill
races cannot be controlled, or when invalidation has no owner.

**Competing alternative.** A shorter TTL with retried invalidation, or serving the read from
the source when its latency budget allows. Reverse when fill and invalidation logic becomes
duplicated and inconsistent.

**Failure and recovery.** Stale fills and concurrent misses are common; gate fills by cached
revision, distinguish a cold fill from a post-delete tombstone, retry failed invalidation and
use single-flight for concurrent misses.

**Technical owner.** [Cache-aside is a sequence, not a consistency theorem](../../v06-caching-indexing-and-retrieval/c01-local-and-distributed-caching/refresh-semantics.md#4-cache-aside-is-a-sequence-not-a-consistency-theorem) — the sequence is bounded, not a complete cache-aside library guide.

**Sources.**
[src.aws-caching-strategies](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch3-aws-caching.2026-10-21: sections "Caching patterns", "Cache-Aside
(Lazy Loading)", "Write-Through". The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Read-Through Cache; Cache Invalidation; Cache Stampede Protection;
Distributed Cache.

### Read-Through Cache

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

**Technical owner.** [Local and distributed caching: authority, freshness and placement](../../v06-caching-indexing-and-retrieval/c01-local-and-distributed-caching/local-and-distributed-cache-design.md#read-through-cache) — read-through freshness and authority are bounded; loader failure semantics are page-specific.

**Sources.**
[src.microsoft-caching-guidance](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch3-ms-caching.2026-10-21: sections "Caching in distributed
applications", "Implement caching patterns". The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Cache-Aside; Write-Through; Distributed Cache; Negative Caching.

### Write-Through Cache

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

**Technical owner.** [Local and distributed caching: authority, freshness and placement](../../v06-caching-indexing-and-retrieval/c01-local-and-distributed-caching/local-and-distributed-cache-design.md#write-through-cache) — write-through ordering and acknowledgement are bounded; backend durability is page-specific.

**Sources.**
[src.aws-caching-strategies](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch3-aws-caching.2026-10-21: sections "Caching patterns",
"Write-Through". The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Write-Behind; Cache-Aside; Cache Invalidation; Distributed Cache.

### Write-Behind / Write-Back

**Identity.** Write-Behind / Write-Back; family Caching and retrieval; kind
caching-pattern; priority advanced.

**Decision question.** Should writes land in the cache first and reach the store
asynchronously?

**Good-fit conditions.** The cache can durably buffer writes; loss tolerance is explicit;
ordering and retry are owned; the store can catch up.

**Hard contraindications.** Reject when a cache loss would lose accepted writes, when
ordering is mandatory, or when no reconciliation path exists.

**Competing alternative.** Write-through or direct store writes. Reverse the choice when
durability and replay complexity exceed latency benefit.

**Failure and recovery.** Cache loss and reordering are common; verify durability in the
owner section.

**Technical owner.** [Local and distributed caching: authority, freshness and placement](../../v06-caching-indexing-and-retrieval/c01-local-and-distributed-caching/local-and-distributed-cache-design.md#write-behind-write-back) — write-behind durability and ordering are bounded; flush retry policy is page-specific.

**Sources.**
[src.microsoft-caching-guidance](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch3-ms-caching.2026-10-21: sections "Caching in distributed
applications", "Manage concurrency in a cache". The record covers caching write consistency
generally, not write-behind buffering or durability; that mechanism is synthetic owner guidance.
The source is a public pattern/documentation unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Write-Through; Write-Around; Distributed Cache; Transactional Outbox.

### Write-Around

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

**Technical owner.** [Local and distributed caching: authority, freshness and placement](../../v06-caching-indexing-and-retrieval/c01-local-and-distributed-caching/local-and-distributed-cache-design.md#write-around) — write-around freshness and miss path are bounded; prefetch policy is page-specific.

**Sources.**
[src.microsoft-caching-guidance](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch3-ms-caching.2026-10-21: sections "Keep the cache consistent on
writes", "Manage data expiration in a cache". The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Write-Through; Cache Invalidation; TTL-Based Expiration; Cache-Aside.

### Cache Invalidation

See the [dedicated Cache Invalidation card](cache-invalidation.md).

### TTL-Based Expiration

See the [dedicated TTL-Based Expiration card](ttl-based-expiration.md).

### Negative Caching

**Identity.** Negative Caching; family Caching and retrieval; kind caching-pattern;
priority core.

**Decision question.** Should failures or empty results be cached like successful
responses?

**Good-fit conditions.** The failure is stable enough to cache; TTL is short; negative
entries cannot hide a later valid result; status-specific policy exists. RFC 9111 allows
"negative results (e.g., 404 (Not Found))" only inside its storage rules, and a shared
cache must not reuse an authorization-bearing response unless a directive "allows it to
be stored by a shared cache".

**Hard contraindications.** Reject when failures are transient, when caching an error
would hide recovery, or when negative entries leak existence or authorization. CloudFront
caches a 403 only when the origin sends `Cache-Control max-age` or `Cache-Control
s-maxage`, so a denial the origin does not explicitly mark cacheable is not a safe
default.

**Competing alternative.** A per-principal key, a short TTL, or bypass. OWASP says to
"Cache only for the same subject, action, resource scope, tenant, and relevant
policy/input state, within the approved freshness limit"; Cloudflare gives 404 and 410 a
3-minute default Edge TTL and says "All other status codes are not cached by default."
Reverse when repeated misses amplify origin load and the denial is global for the key.

**Failure and recovery.** A cached denial can outlive a create/grant or leak across
principals; scope keys by tenant/principal, delete or version on change, bound TTL and
test revocation. OWASP states that "a cached permit must not outlive a required
revocation deadline"; CloudFront's error-caching minimum TTL defaults to 10 seconds (the
window is the larger of that minimum and any origin cache directive) and it "continues
to retry at intervals".

**Technical owner.** [Negative caching and discriminating experiments](../../v06-caching-indexing-and-retrieval/c02-hot-keys-cache-stampedes-and-read-amplification/negative-cache.md#4-negative-caching-and-evicted-authorization) — negative-cache policy is bounded, not a universal error-cache rule.

**Sources.** Four public units were inspected on 2026-10-31:
`src.rfc9111-enrichment`, `src.cloudfront`,
`src.owasp-authorization-decisions` and `src.cloudflare-cache-status`
([reading ledger](../../../../edition/patterns/reading-ledger.v1.json)).
Records: `read.rfc9111-negative-caching.2026-10-31`,
`read.cloudfront-status-codes.2026-10-31`,
`read.owasp-authorization-decisions.2026-10-31` and
`read.cloudflare-cache-status.2026-10-31`. The retained
`src.google-cdn-negative-caching` record `read.batch3-google-negative.2026-10-21`
supplies the per-status TTL example. These are protocol, documentation and
guidance units, not benchmarks.

**Decision state.** applicable-under-conditions.

**Related entries.** TTL-Based Expiration; CDN / Edge Caching; Cache Invalidation; Cache
Stampede Protection.

### Cache Stampede Protection

See the [dedicated Cache Stampede Protection card](cache-stampede.md).

### Single Flight / Request Coalescing

**Identity.** Single Flight / Request Coalescing; family Caching and retrieval; kind
caching-pattern; priority core.

**Decision question.** Should duplicate in-flight requests for the same key share one
source call?

**Good-fit conditions.** Requests are read-mostly; the key is stable; waiters can tolerate
shared failure; the coalescing scope is bounded.

**Hard contraindications.** Reject when requests carry different authorization or
parameters, when one slow call would block unrelated callers, or when cancellation must be
independent.

**Competing alternative.** Independent calls with stampede protection at the source.
Reverse the choice when shared latency/failure outweighs duplicate-call reduction.

**Failure and recovery.** One failure fans out to all waiters; verify scope and
cancellation in the owner section.

**Technical owner.** [Single Flight / Request Coalescing](../../v06-caching-indexing-and-retrieval/c02-hot-keys-cache-stampedes-and-read-amplification/stampede-protection.md#single-flight-request-coalescing) — coalescing window and leader election are bounded; library semantics are implementation-specific.

**Sources.**
[src.microsoft-caching-guidance](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch3-ms-caching.2026-10-21: section "Manage concurrency in a cache". The
record covers cache concurrency, not request coalescing; coalescing and leader election are
synthetic owner guidance. The source is a public pattern/documentation unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Cache Stampede Protection; Cache-Aside; Distributed Cache; Timeout.

### Stale-While-Revalidate

See the [dedicated Stale-While-Revalidate card](stale-while-revalidate.md).

### Multi-Level Caching

See the [dedicated Multi-Level Caching card](multi-level-caching.md).

### CDN / Edge Caching

See the [dedicated CDN / Edge Caching card](cdn-edge-caching.md).

## Chapter result and counterexample

Fourteen cards establish a conditional decision route. Owner sections are bounded; none
establishes technical sufficiency.

Counterexample: a CDN configured to cache a personalized response is not evidence for
the edge-caching card's cacheability conditions.

## Navigation and prerequisites

- Parent: [V11](../README.md).
- Previous: [V11/C04](../c04-consistency-events/README.md).
- Next: [V11/C06](../c06-database-storage/README.md).
- Prerequisite: V10/C03 — pattern applicability and contraindications.
- Registry: [pattern registry](../../../../edition/patterns/registry.v1.json).
- Card batch: [card batches](../../../../edition/patterns/card-batches.v1.json).
- Coverage map: [candidate coverage](../../../../edition/patterns/coverage-map.v1.json).

## Evidence and known limits

- All 14 cards cite read ledger units; owner links and backlinks are self-checked.
- Owner links are bounded sections, not dedicated pattern pages.
- No entry claims sufficient technical or decision coverage.
- No independent editorial review, benchmark, production observation or runtime test
  is asserted.
