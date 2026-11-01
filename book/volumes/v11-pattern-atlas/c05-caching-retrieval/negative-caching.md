---
metadata_version: 1
id: "tycho.page.b6f0e0ea50474e29901d5b7b7f471bac"
kind: "page"
parent_id: "tycho.chapter.87e52392e206a451ea5c79a4194c384b"
canonical_path: "book/volumes/v11-pattern-atlas/c05-caching-retrieval/negative-caching.md"
title: "Negative Caching"
topic_ids:
  - "performance-engineering"
  - "data-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: >-
  Decision card for Negative Caching; source-anchored on RFC 9111, CloudFront,
  OWASP authorization-decision reuse and Cloudflare status-code caching;
  coverage remains partial-bounded, no promotion.
route_hints:
  questions:
    - >-
      Should failures or empty results be cached like successful responses?
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
    - "negative caching"
    - "caching and retrieval"
evidence_scope:
  source_ids:
    - "src.cloudflare-cache-status"
    - "src.cloudfront"
    - "src.google-cdn-negative-caching"
    - "src.owasp-authorization-decisions"
    - "src.rfc9111-enrichment"
  claim_ids: []
  status: "source-linked"
  notes: >-
    Card cites read.rfc9111-negative-caching.2026-10-31,
    read.cloudfront-status-codes.2026-10-31,
    read.owasp-authorization-decisions.2026-10-31 and
    read.cloudflare-cache-status.2026-10-31; read.batch3-google-negative.2026-10-21
    is retained per-status TTL context; owner section and limits are bounded.
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
# Negative Caching

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
default. OWASP's "Bound reuse" rule also requires the same subject, action, resource
scope, tenant and policy/input state within the approved freshness limit.

**Competing alternative.** A per-principal key, a short TTL, or bypass. OWASP says to
"Cache only for the same subject, action, resource scope, tenant, and relevant
policy/input state, within the approved freshness limit"; Cloudflare gives 404 and 410 a
3-minute default Edge TTL and says "All other status codes are not cached by default."
Reverse when repeated misses amplify origin load and the denial is global for the key.

**Failure and recovery.** A cached denial can outlive a create/grant or leak across
principals; scope keys by tenant/principal, delete or version on change, bound TTL and
test revocation. OWASP states that "a cached permit must not outlive a required
revocation deadline" and says to fail closed and recheck when the relevant state changes;
CloudFront's error-caching minimum TTL defaults to 10 seconds (the window is the larger
of that minimum and any origin cache directive) and it "continues to retry at intervals".
CloudFront may also serve an expired object on a 5xx, which is an availability choice,
not evidence that the object exists for the caller. RFC 9111 likewise prohibits a stale
response unless the cache is disconnected or the client or origin server explicitly
permits it.

**Technical owner.** [Negative caching and discriminating experiments](../../v06-caching-indexing-and-retrieval/c02-hot-keys-cache-stampedes-and-read-amplification/negative-cache.md#4-negative-caching-and-evicted-authorization) — negative-cache policy is bounded, not a universal error-cache rule.

**Sources.** Four public units were inspected on 2026-10-31: RFC 9111, *HTTP Caching*
(2022); Amazon CloudFront, *How CloudFront processes HTTP 4xx and 5xx status codes from
your origin*; OWASP, *Authorization Decisions and Output Handling Cheat Sheet*, section
"Security Considerations" ("Bound reuse"); and Cloudflare, *Cache by status code*. Read
records: `read.rfc9111-negative-caching.2026-10-31`,
`read.cloudfront-status-codes.2026-10-31`,
`read.owasp-authorization-decisions.2026-10-31` and
`read.cloudflare-cache-status.2026-10-31`. The retained
`src.google-cdn-negative-caching` record `read.batch3-google-negative.2026-10-21`
supplies the per-status TTL example. These units describe protocol rules, documented
product behavior and application guidance, not benchmarks or local reproduction. Source
ids: `src.rfc9111-enrichment`, `src.cloudfront`,
`src.owasp-authorization-decisions`, `src.cloudflare-cache-status` and the retained
`src.google-cdn-negative-caching`.

**Decision state.** applicable-under-conditions.

**Related entries.** TTL-Based Expiration; CDN / Edge Caching; Cache Invalidation; Cache
Stampede Protection.

**Limits.** Negative caching is a Tycho reading of storable non-success results, not a
term used by RFC 9111. CloudFront's 403 rule is conditional and does not establish a
per-principal cache key; OWASP addresses authorization-decision reuse, not HTTP cache
mechanics; Cloudflare documents status-code defaults, not principals. Coverage is
self-checked, not independently reviewed.
