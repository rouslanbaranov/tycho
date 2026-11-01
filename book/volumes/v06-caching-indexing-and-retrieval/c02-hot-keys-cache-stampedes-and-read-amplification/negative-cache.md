---
metadata_version: 1
id: "tycho.page.f077c7f124b54e2a8137cec267d9170a"
kind: "page"
parent_id: "tycho.chapter.1035327a459242b78329b41b8fddfee6"
canonical_path: "book/volumes/v06-caching-indexing-and-retrieval/c02-hot-keys-cache-stampedes-and-read-amplification/negative-cache.md"
title: "Negative caching and discriminating experiments"
topic_ids:
  - "scaling-mechanisms"
perspectives:
  - "architecture"
summary: "Which revoked permission or absent value makes cached absence unsafe?"
route_hints:
  questions:
    - "Which revoked permission or absent value makes cached absence unsafe?"
  prerequisites:
    - "tycho.page.edc267f2fa954e66891e006ddfbfb15f"
  related_ids:
    - "tycho.chapter.1035327a459242b78329b41b8fddfee6"
    - "tycho.page.e0f0d5b68f834acbae94cc6714895dd3"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "negative"
    - "cache"
evidence_scope:
  source_ids:
    - "src.google-cdn-negative-caching"
    - "src.rfc9111-enrichment"
    - "src.cloudfront"
    - "src.owasp-authorization-decisions"
    - "src.cloudflare-cache-status"
  claim_ids: []
  status: "source-linked"
  notes: >-
    Bounded question from tycho.page.e0f0d5b68f834acbae94cc6714895dd3; four
    public sources were inspected on 2026-10-31 and bound to the invariant,
    failure/recovery and alternative dimensions. The Google Cloud CDN unit is
    retained for per-status TTL context. Coverage is self-checked; no
    independent review is claimed.
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-31"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-20"
updated_at: "2026-10-31"
source_inspection_date: null
content_verified_at: null
---
# Negative caching and discriminating experiments

**Owning question:** Which revoked permission or absent value makes cached absence unsafe?

This page belongs to [V06/C02 — Hot keys, cache stampedes and read amplification](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.e0f0d5b68f834acbae94cc6714895dd3:4 -->
## 4. Negative caching and evicted authorization

Caching an absent result can protect against repeated misses for nonexistent IDs. It also
creates a freshness question: if a new object is created, a cached not-found may hide it.
A stale *allow* or *deny* decision can have more serious authorization consequences than
an old description.

Define:
- no-entry versus cached-negative versus actual deletion/tombstone;
- whether unknown data-source errors may be cached at all;
- TTL/backoff with a bounded denial or stale-visibility contract;
- consistency with create/delete and access-revocation paths;
- tenant/key namespaces, malformed IDs and probe-driven resource attacks.

**Protocol baseline.** RFC 9111 allows a cache to store "negative results (e.g., 404
(Not Found))", but only inside its storage rules: the response must be final, cacheable,
and stored under a cache key. A status code that is "heuristically cacheable" may receive
a heuristic freshness lifetime; an explicit expiration time forbids heuristics. A shared
cache must not reuse a response to a request carrying `Authorization` unless a response
directive "allows it to be stored by a shared cache". The specification warns that
mistakes "might lead to the caching of sensitive information (e.g., authentication
credentials)". Those rules bound storage and reuse; they do not define an application's
authorization semantics.

**Not a universal absence.** A cached negative must never become a universal statement
that an object does not exist for all authorized principals if visibility varies by
principal or tenant. OWASP's authorization-decision guidance says to "Bind each decision
to the authenticated subject, action, resource, tenant, and relevant context" and to
"Cache only for the same subject, action, resource scope, tenant, and relevant
policy/input state, within the approved freshness limit". **Tycho rule:** a negative key
for an authorization-sensitive lookup includes the tenant, principal or scope, the checked
operation and the policy revision; a key that omits one of these is not shared. CloudFront
shows the deployment side: it caches a 403 only when the origin sends `Cache-Control
max-age` or `Cache-Control s-maxage`, so a denial becomes edge-cacheable only when the
origin explicitly makes it so.

**Bounded denial and recovery.** A cached denial can outlive a grant or a revocation.
OWASP states that "a cached permit must not outlive a required revocation deadline",
says to "Account for changes between evaluation and use", and tells integrations to
"Recheck authorization for subsequent operations or when the relevant state changes" and
to "Fail closed." CloudFront's error-caching minimum TTL is 10 seconds by default; the
effective window is the larger of that minimum and any origin cache directive, and after
it CloudFront "tries again" and "continues to retry at intervals", so a cached error is
a bounded retry window rather than a permanent verdict. On a 5xx, CloudFront may also
serve an expired object, which is a stale-availability choice, not evidence that the
object exists for the caller. **Tycho rule:** bound a denial by the shorter of its TTL and the
revocation deadline; delete or version the key on create, grant, revoke and delete; never
cache an unknown backend error as "absent".

**Alternatives.** Per-principal keying, a short TTL and bypass are the three bounded
alternatives. RFC 9111 notes that "double keying" adds information such as the referring
site to the cache key; for authorization, the analogous material is the principal, tenant
and policy revision. Cloudflare gives 404 and 410 a 3-minute default Edge TTL when no
cache directive or expiry is present and says "All other status codes are not cached by
default"; a status-code rule can set a TTL or `no-store`/`no-cache`. Bypass means the
authorization path never reads a negative entry; a short TTL makes the stale window
explicit; a per-principal key prevents reuse by another principal. **Tycho choice rule:**
prefer per-principal keying for authorization decisions, a short TTL for public existence
checks, and bypass when the revocation deadline is shorter than any useful TTL. Reverse
when repeated misses dominate origin load and the denial is global for the key.

**Bound source limits.** Four public sources were inspected on 2026-10-31: RFC 9111,
*HTTP Caching* (2022); Amazon CloudFront, *How CloudFront processes HTTP 4xx and 5xx
status codes from your origin*; OWASP, *Authorization Decisions and Output Handling Cheat
Sheet*, section "Security Considerations" ("Bound reuse"); and Cloudflare, *Cache by
status code*. The Google Cloud CDN *Use negative caching* page remains the retained
per-status TTL example. These units describe protocol rules, documented product behavior
and application guidance; none measures this page's keying, revocation or failure
behavior. Read records: `read.rfc9111-negative-caching.2026-10-31`,
`read.cloudfront-status-codes.2026-10-31`, `read.owasp-authorization-decisions.2026-10-31`
and `read.cloudflare-cache-status.2026-10-31`. Coverage is self-checked, not
independently reviewed.

<!-- /tycho-question-source -->

> **Pattern atlas:**
> [Negative Caching](../../v11-pattern-atlas/c05-caching-retrieval/README.md#negative-caching) — decision conditions and contraindications.

<!-- tycho-question-source:tycho.page.e0f0d5b68f834acbae94cc6714895dd3:6 -->
## 6. A discriminating failure experiment

Reproducible candidate tests (not performed):
1. Concurrent source v1 read and v2 write/delete, with delayed fill; detect regression.
2. 300 simultaneous misses across multiple replicas to one hot key; observe source requests and admission.
3. Refresh lock expiry followed by stale worker resumption; verify fence.
4. Cache cold start and complete loss at peak offered arrivals.
5. Mutation of an authorization-sensitive value during a permitted TTL.
6. Backend read error returning no result; ensure it is not negatively cached as “absent”.
7. Cache TTL jitter with many keys; compare with one-key hotspot.
8. Mixed application/cache versions and replay of invalidation events.

Report correctness and valid outcomes first, then hit ratio, p95/p99, DB utilization, queue age and added memory/network costs. A performance win based on unreported errors or stale authorization is not valid.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](stampede-protection.md) |
| Next | [Continue the reasoning](README.md) |
| Integrated question | [Original scenario and limits](cache-invalidation-stampede-and-hot-keys.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.
