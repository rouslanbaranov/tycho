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
      "src.sre-frontend-enrichment",
      "src.microsoft-cloud-patterns"
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
  "updated_at": "2026-10-30",
  "source_inspection_date": "2026-10-20",
  "content_verified_at": null
}
---

# Edge caching, private content and origin recovery

**Owning question:** Which representation may an edge reuse, and how is correctness preserved during origin failure?


> **Pattern atlas:**
> [CDN / Edge Caching](../../v11-pattern-atlas/c05-caching-retrieval/README.md#cdn--edge-caching) — decision conditions and contraindications.


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

## Bounded pattern ownership notes

### CDN-Edge Caching

An edge can reduce distance and origin work, but only for responses it may
reuse. Azure CDN describes a content delivery network as a shared cache:
"Dynamic resources that change frequently or are unique to an individual user
can't be cached." CloudFront defines the cache key as "the unique identifier
for an object in the cache" and includes only the distribution domain and URL
path by default. Cacheability is a content and authority contract, not a
network location.

**Invariant.** The cache key, freshness policy and authorization boundary must
agree. RFC 9111 section 4 says a cache "MUST NOT reuse a stored response
unless" the target URI and request method match, request header fields
nominated by Vary match, the response is not `no-cache` without validation,
and the response is fresh, allowed stale, or successfully validated. Section
4.1 makes the Vary fields part of the key test. Section 3.5 says a shared cache
"MUST NOT use a cached response to a request with an Authorization header
field" unless a response directive permits shared storage. Azure CDN states
that "Requests that include authorization header will not be cached."
CloudFront warns that when the Authorization header is not part of the cache
key, CloudFront "can serve the same cached response to both authorized and
unauthorized viewers." CloudFront also warns that a minimum TTL greater than
zero overrides `no-cache`, `no-store` and `private` origin directives. These
are product-specific rules, not interchangeable defaults. Tycho guidance:
treat key, freshness and authorization as one testable contract; do not relax
one dimension because another appears to compensate.

**Failure and recovery.** A misclassified response can serve one user's
private data to another, and a purge can lag the origin. The visible failure
is not only a stale object: the same key can return a representation the
caller was never authorized to receive. Azure CDN says "Azure CDN makes no
guarantees about minimum amount of time that the object will be stored in the
cache" and that cached content can be evicted before expiry. CloudFront can
serve a previously cached object when the origin is unreachable if the
minimum or maximum TTL is greater than zero. Test the authorization matrix,
the stale-on-error path and the purge path together. Tycho guidance: a purge
request without completion evidence is not a proven revocation bound.

**Alternative.** A direct origin or a private cache may be preferable when
every response is user-specific or the purge contract cannot be enforced.
RFC 9111 section 5.2.2.7 says the unqualified `private` directive tells a
shared cache "MUST NOT store the response" while "a private cache MAY store
the response"; section 5.2.2.5 makes `no-store` stricter. CloudFront's stated
choice is to "include the Authorization header in the cache key using a cache
policy" or "disable caching entirely for origins that require origin-side
authorization processing." Azure CDN's "Bypass cache" setting does not cache.
The purge contract is bounded on both products: Azure says downstream caches
"might still hold a cached copy," and CloudFront says a user "might continue
to see the old version" after invalidation. Tycho guidance: "direct origin"
names the uncached route; require completion evidence for the key and
authorization scopes that matter.

**Limits and source boundary.** The selected pages document product
configuration and HTTP requirements, not this book's deployment. No CDN was
configured, no purge was run and no authorization matrix was tested. The Azure
pages describe the retiring classic Standard-from-Microsoft service and an
archived caching-rules page; the HTTP and product statements are bounded to
those revisions, not to every Azure edge product.

- RFC 9111, "HTTP caching", `read.rfc9111-edge-cache.2026-10-30`, served text
  `aeb52adb3279d5f23dae34f68af11bd5cef0a0aff7ffcd014c9ca93c5302cf3e`:
  sections 3.5, 4, 4.1, 4.4, 5.2.2.5 and 5.2.2.7.
- Microsoft, "How caching works", `read.azure-cdn-how-caching.2026-10-30`,
  HTML `5ae280f568de52e593c290d013c61918320815b916ef7bf0c31e468fcbda956a`,
  ms.date 2026-02-28, commit `fe2e4465ddb694284d4bdefca0f41e9499090877`:
  shared-cache, authorization, eviction and freshness statements.
- Microsoft, "Control caching behavior with caching rules",
  `read.azure-cdn-caching-rules.2026-10-30`, archived HTML
  `5e686846ea09abdd926114d382bebb405ad9ece75b606eec5780c81916f9a361`,
  ms.date 2025-03-31, commit `1a312008ffbf4cc43ee13967c16007eda6a11ae9`:
  bypass, zero-duration validation and rule-change purge statements.
- Microsoft, "Purge an Azure CDN endpoint", `read.azure-cdn-purge.2026-10-30`,
  HTML `a2cf2b83b454fa0ce7c1cf8dbbfe6640152bbc630132026ecad3b7c66971f378`,
  ms.date 2026-02-28, commit `fe2e4465ddb694284d4bdefca0f41e9499090877`:
  downstream-cache and query-string purge statements.
- Amazon, "Understand the cache key", `read.cloudfront-cache-key.2026-10-30`,
  Markdown `47c2adb2350549b0f192e0fb3aef953928cb3a8ed43e86c38a74ba695fe80790`:
  key definition, include-when-response-varies and user-specific-cookie
  statements.
- Amazon, "Add custom headers to origin requests",
  `read.cloudfront-auth-header.2026-10-30`, Markdown
  `06076dc410b73bd1bf63c46c01900c8b767b1201c29073c8e440b4b002c3d891`:
  Authorization-header removal, key-mismatch and disable-caching statements.
- Amazon, "Manage how long content stays in the cache (expiration)",
  `read.cloudfront-expiration.2026-10-30`, Markdown
  `cfb1bbad63f66dcf936c4d269ecaa3e2e24871d684e8555eb46ee94ea1eb2a1a`:
  minimum-TTL override and stale-on-origin-error statements.
- Amazon, "Invalidate files to remove content",
  `read.cloudfront-invalidation.2026-10-30`, Markdown
  `62930f87a51b954f89cbe31272057abf219b7224a3d7c058386443ad280b4940`:
  downstream-cache and versioned-file statements.

### Static Content Hosting

See the [dedicated Static Content Hosting owner note](static-content-hosting.md).
