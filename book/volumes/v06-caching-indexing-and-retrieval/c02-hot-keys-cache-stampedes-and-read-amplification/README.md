---
metadata_version: 1
id: "tycho.chapter.1035327a459242b78329b41b8fddfee6"
kind: "chapter"
parent_id: "tycho.volume.69e6229b222f4535bc0b3941cee1b1cc"
canonical_path: "book/volumes/v06-caching-indexing-and-retrieval/c02-hot-keys-cache-stampedes-and-read-amplification/README.md"
title: "V06/C02 — Hot keys, cache stampedes and read amplification"
topic_ids:
  - "scaling-mechanisms"
perspectives:
  - "architecture"
  - "evaluation"
summary: "When does adding a cache worsen recovery or contention? The reading route separates 3 detailed questions from the integrated decision."
route_hints:
  questions:
    - "When does adding a cache worsen recovery or contention?"
  prerequisites:
    - "tycho.chapter.4166e932cbd64ce2a63fe0c6d6eb049a"
  related_ids:
    - "tycho.page.e0f0d5b68f834acbae94cc6714895dd3"
    - "tycho.page.028aab692b414bcdba7713500ab6f735"
    - "tycho.page.edc267f2fa954e66891e006ddfbfb15f"
    - "tycho.page.f077c7f124b54e2a8137cec267d9170a"
  excludes:
    - "No new benchmark, source inspection or independent edition review is asserted."
  keywords:
    - "system-design"
    - "edition-navigation"
evidence_scope:
  source_ids:
    - "src.sre-cascading"
  claim_ids: []
  status: "unknown"
  notes: "Editorial synthesis of the linked accepted manuscript; exact source versions and nonclaims remain in its page-local evidence ledger."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-20"
  reviewer: "Codex editorial assembly"
  proof_uri: null
authored_at: "2026-10-20"
updated_at: "2026-10-21"
source_inspection_date: null
content_verified_at: null
---

# V06/C02 — Hot keys, cache stampedes and read amplification

## Purpose and mission

When does adding a cache worsen recovery or contention? This chapter owns that question within caching, indexing and information retrieval. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Bound regeneration, hot-key fan-out and cold-start demand as part of cache recovery.

A cache outage or simultaneous expiry can concentrate traffic on the protected origin and amplify the original failure. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

Begin with the integrated decision, then open the independent question that matches the missing mechanism or observed failure. Read source limits before applying the conclusion.

| Page | Independent question and role |
|---|---|
| [Integrated decision and original walkthrough](cache-invalidation-stampede-and-hot-keys.md) | When does adding a cache worsen recovery or contention? |
| [Stale fills and regeneration ownership](stale-fill.md) | Which version or fencing rule prevents a refresh from publishing obsolete state? |
| [Stampedes and source protection](stampede-protection.md) | How do expiry and cache loss concentrate demand on the origin? |
| [Negative caching and discriminating experiments](negative-cache.md) | Which revoked permission or absent value makes cached absence unsafe? |

## Boundaries and further reading

The preceding and following chapters supply context; this landing does not replace their canonical mechanisms. Follow the exact source ledger on the child page when a claim depends on a product version or historical period.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V06 — Caching, indexing and information retrieval](../README.md) |
| Previous | [V06/C01 — Local and distributed caching](../c01-local-and-distributed-caching/README.md) |
| Next | [V06/C03 — Lexical full-text indexing and ranking](../c03-lexical-full-text-indexing-and-ranking/README.md) |
| Prerequisite | [V06/C01 — Local and distributed caching](../c01-local-and-distributed-caching/README.md) |
| Source reading | [Page-local evidence and versions](cache-invalidation-stampede-and-hot-keys.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.

## Chapter source ledger

The following original citation rows, review limits and earlier topical routes are retained once for this chapter. Each question page points here and retains its inline citations. Evidence coverage must be judged at the actual claim and version, not inferred from source-list length.

<!-- tycho-question-source:tycho.page.e0f0d5b68f834acbae94cc6714895dd3:7 -->
## 7. Public references and limitations

| Independently inspected material | Supports | Not established |
|---|---|---|
| [Redis cache-aside](https://redis.io/docs/latest/develop/use-cases/cache-aside/) | Cache-aside, TTL, invalidation and stampede concerns | Strong consistency for concurrent cache writes |
| [Redis EXPIRE](https://redis.io/docs/latest/commands/expire/) | Key expiry policies and clock/lifetime behavior | Automatic transactional coordination with source DB |
| [Caffeine Refresh](https://github.com/ben-manes/caffeine/wiki/Refresh) | Refresh eligibility, async reload and old-value serving | Cross-node refresh serialization |
| [Earlier Tycho combined cache study](../../../scaling/local-distributed-caching-and-invalidation.md) | Original version-scoped source research | Executed race/lock proof |

- [SRE, *Cascading Failures*](https://sre.google/sre-book/addressing-cascading-failures/),
  inspected 2026-10-21: cold-cache and source-overload interaction, including a full
  restart of replicas. The source's examples are contextual, not universal thresholds.

All race participants, diagrams, metrics and design results are synthetic. No cache service, load generator, source DB or reviewer was involved.

**Navigation:** proposed **V06/C02** in [the 69-question outline](../../../PROPOSED-STRUCTURE.md), [scaling entry](../../../scaling/README.md), [cache placement/freshness](../c01-local-and-distributed-caching/local-and-distributed-cache-design.md), [pool budget](../../v03-execution-concurrency-and-flow-control/c05-thread-connection-and-buffer-pools/connection-pools-hikaricp-pgbouncer.md), [overload](../../v07-performance-scale-and-resilience/c05-overload-protection-and-graceful-degradation/overload-admission-control-and-graceful-degradation.md).
<!-- /tycho-question-source -->
