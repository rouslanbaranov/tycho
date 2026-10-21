---
{
  "metadata_version": 1,
  "id": "tycho.page.3349b84b088ebcca496bb52fbdbbc565",
  "kind": "page",
  "parent_id": "tycho.chapter.8a86707018773def410689efbc79cf94",
  "canonical_path": "book/volumes/v08-delivery-deployment-and-recovery/c08-network-request-paths-routing-and-edge-delivery/edge-cache-origin.md",
  "title": "Edge caching, private content and origin recovery",
  "topic_ids": [
    "network-architecture"
  ],
  "perspectives": [
    "architecture",
    "operations",
    "evaluation"
  ],
  "summary": "Which representation may an edge reuse, and how is correctness preserved during origin failure?",
  "route_hints": {
    "questions": [
      "Which representation may an edge reuse, and how is correctness preserved during origin failure?"
    ],
    "prerequisites": [],
    "related_ids": [
      "tycho.chapter.8a86707018773def410689efbc79cf94"
    ],
    "excludes": [
      "No executed product experiment or independent acceptance is claimed."
    ],
    "keywords": [
      "which",
      "representation",
      "edge",
      "reuse",
      "correctness",
      "preserved",
      "during",
      "origin",
      "failure"
    ]
  },
  "evidence_scope": {
    "source_ids": [
      "src.rfc9111-enrichment",
      "src.sre-frontend-enrichment"
    ],
    "claim_ids": [],
    "status": "source-linked",
    "notes": "Exact selected passages and source limitations are recorded in the page ledger and dated enrichment inspection record. Synthetic protocols are original design reasoning."
  },
  "content_review": {
    "status": "self-checked",
    "reviewed_at": "2026-10-20",
    "reviewer": "Codex enrichment author; execution gates pending",
    "proof_uri": null
  },
  "authored_at": "2026-10-20",
  "updated_at": "2026-10-20",
  "source_inspection_date": "2026-10-20",
  "content_verified_at": null
}
---

# Edge caching, private content and origin recovery

**Owning question:** Which representation may an edge reuse, and how is correctness preserved during origin failure?


> **Pattern atlas:**
> [CDN / Edge Caching](../../v11-pattern-atlas/c05-caching-retrieval/README.md#cdn-edge-caching) — decision conditions and contraindications.


> **Pattern atlas:**
> [Static Content Hosting](../../v11-pattern-atlas/c09-scalability/README.md#static-content-hosting) — decision conditions and contraindications.

## Cacheability is a content and authority contract

An edge can reduce distance and origin work, but only for responses it may reuse. Classify immutable public assets, mutable public representations and private caller-dependent content separately. The cache key, freshness policy and authorization boundary must agree.

RFC 9111 sections 3.5 and 4 constrain reuse of authenticated responses by shared caches and describe cache selection/validation. An authorization header is not a complete design for private edge caching; explicit cache directives can alter reuse rules. Test the actual CDN/proxy configuration.

**Static-content mechanism.** Immutable, versioned assets are published to an object store
or CDN origin and served by URL without per-request application compute. A publication
pipeline uploads and verifies the version; the edge caches by that URL; mutable or private
content needs a separate key and authorization contract.

**Failure and recovery.** Origin outage, incomplete purge, stale deletion and a cold-cache
miss storm are common. Prewarm critical assets, verify propagation, keep an origin failover
and use versioned rollback rather than mutating a cached object. A dynamic origin,
self-hosted files or edge compute may be preferable when content changes per request or the
publication pipeline cannot be governed.

## Original worked example

A fictional catalogue exposes versioned public thumbnails and restricted source images. Public thumbnail URLs include immutable content versions. Restricted originals are fetched through an access decision and must not accidentally share a public-cache route. Changing visibility from public to private is a revocation problem: removing the database's public flag does not erase every distributed copy already served.

Define the observable contract. A public immutable asset may tolerate an old URL until retirement. A restricted object may require authorization on every access, a capability with bounded lifetime, or an edge policy whose propagation bound is acceptable. A purge request without completion evidence is not a proven revocation bound.

~~~mermaid
flowchart TD
    R["Request with representation and access context"] --> P{"Reuse explicitly permitted?"}
    P -->|No| A["Authorize and reach origin"]
    P -->|Yes| F{"Matching entry is usable?"}
    F -->|Yes| H["Return within freshness contract"]
    F -->|No| V["Validate or fetch with origin budget"]
    V --> E{"Origin unavailable"}
    E --> S["Serve stale only if contract permits"]
    E --> U["Otherwise report unavailable"]
~~~

Text alternative: permission to reuse precedes the freshness decision. Origin failure does not grant permission to expose a response that the caller could not otherwise receive. This is a synthetic reasoning flow; exact directives remain normative in the RFC.

## Origin protection and rewarming

After widespread expiry, many edge locations may refill together. The origin needs bounded concurrent fills, retry budgets and a deliberate stale-response policy. A cache hit-rate average conceals one expensive class of misses. Estimate origin demand by class: in an invented workload of 2,000 requests/s with a 2% miss rate, 40 origin fetches/s is only a mean; correlated expiry can temporarily approach the full offered rate.

Versioned URLs simplify invalidation for immutable bytes but increase retained objects and make garbage collection a separate task. Mutable names allow in-place updates but require a freshness and validation policy. Neither option replaces access enforcement.

## Acceptance and evidence boundary

Proposed tests: same URL under two access identities; changed response variants; stale edge content after revocation; dropped purge requests; origin loss during expiry; and restoration under retries. Observe origin concurrency, response age, unauthorized exposure, egress and user outcomes. No hit-rate or latency improvement is measured here.

Sources: [RFC 9111](https://www.rfc-editor.org/rfc/rfc9111.html#section-3.5) for shared-cache restrictions and validation; the linked [cache stampede owner](../../v06-caching-indexing-and-retrieval/c02-hot-keys-cache-stampedes-and-read-amplification/stampede-protection.md) for source protection. The workload arithmetic and failure scenarios are original synthetic analysis. A specific CDN requires its own versioned documentation and verification.

## Navigation

Parent: [network chapter](README.md). Previous: [trust boundaries](tls-gateway-boundaries.md). Continue to [object access and lifecycle](../../v05-data-models-engines-and-lifecycle/c08-object-storage-large-transfers-and-publication/access-lifecycle.md) and [overload recovery](../../v07-performance-scale-and-resilience/c05-overload-protection-and-graceful-degradation/README.md).
