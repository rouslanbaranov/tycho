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
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Bounded question from tycho.page.e0f0d5b68f834acbae94cc6714895dd3; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-20"
  reviewer: "Codex editorial decomposition"
  proof_uri: null
authored_at: "2026-10-20"
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---
# Negative caching and discriminating experiments

**Owning question:** Which revoked permission or absent value makes cached absence unsafe?

This page belongs to [V06/C02 — Hot keys, cache stampedes and read amplification](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.e0f0d5b68f834acbae94cc6714895dd3:4 -->
## 4. Negative caching and evicted authorization

Caching an absent result can protect against repeated misses for nonexistent IDs. But it creates a freshness question: if a new object is created, a cached not-found may hide it. A stale *allow* or *deny* decision can have more serious authorization consequences than an old description.

Define:
- no-entry versus cached-negative versus actual deletion/tombstone;
- whether unknown data-source errors may be cached at all;
- TTL/backoff with a bounded denial or stale-visibility contract;
- consistency with create/delete and access-revocation paths;
- tenant/key namespaces, malformed IDs and probe-driven resource attacks.

A cached negative must never become a universal statement that an object does not exist for all authorized principals if visibility varies by principal or tenant.

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
