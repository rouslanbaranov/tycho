---
metadata_version: 1
id: "tycho.chapter.4166e932cbd64ce2a63fe0c6d6eb049a"
kind: "chapter"
parent_id: "tycho.volume.69e6229b222f4535bc0b3941cee1b1cc"
canonical_path: "book/volumes/v06-caching-indexing-and-retrieval/c01-local-and-distributed-caching/README.md"
title: "V06/C01 — Local and distributed caching"
topic_ids:
  - "scaling-mechanisms"
perspectives:
  - "architecture"
  - "evaluation"
summary: "How do authority, freshness, eviction and invalidation differ? The reading route separates 3 detailed questions from the integrated decision."
route_hints:
  questions:
    - "How do authority, freshness, eviction and invalidation differ?"
  prerequisites:
    - "tycho.chapter.7031445877fb4f8d831d962d170521c8"
    - "tycho.chapter.e451bfe1e0cb4c588f0576e0b2b7d3d0"
    - "tycho.chapter.3e2e1da8f99c4a7ba05121baf1ef4d91"
    - "tycho.chapter.3d0f6dd1e8e94cd397326e129b5c287f"
  related_ids:
    - "tycho.page.33742c54f667446cbf57cb9f3696a533"
    - "tycho.page.765a54f5d9944577908b40b3fc6cb7ef"
    - "tycho.page.76f6d792c80a448fa1a76001ca6699e1"
    - "tycho.page.f39fa61013ca41abbfba82ef48250f8f"
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

# V06/C01 — Local and distributed caching

## Purpose and mission

How do authority, freshness, eviction and invalidation differ? This chapter owns that question within caching, indexing and information retrieval. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Distinguish authoritative state from cached copies and define freshness, eviction and invalidation behavior.

A successful cache hit can return an inadmissibly stale value; cache availability is not authoritative correctness. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

Begin with the integrated decision, then open the independent question that matches the missing mechanism or observed failure. Read source limits before applying the conclusion.

| Page | Independent question and role |
|---|---|
| [Integrated decision and original walkthrough](local-and-distributed-cache-design.md) | How do authority, freshness, eviction and invalidation differ? |
| [Authority, freshness and cache placement](cache-authority.md) | Which state remains authoritative when a local or distributed cache is used? |
| [Eviction, refresh and cache-aside races](refresh-semantics.md) | Which read/write interleaving invalidates a naive freshness promise? |
| [Cache cost, failure and acceptance](cache-acceptance.md) | When should stale service, origin protection or no cache be preferred? |

## Boundaries and further reading

The preceding and following chapters supply context; this landing does not replace their canonical mechanisms. Follow the exact source ledger on the child page when a claim depends on a product version or historical period.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V06 — Caching, indexing and information retrieval](../README.md) |
| Previous | [V05/C08 — Object storage, large transfers and publication](../../v05-data-models-engines-and-lifecycle/c08-object-storage-large-transfers-and-publication/README.md) |
| Next | [V06/C02 — Hot keys, cache stampedes and read amplification](../c02-hot-keys-cache-stampedes-and-read-amplification/README.md) |
| Prerequisite | [V02/C02 — Domain boundaries, data ownership and contracts](../../v02-application-boundaries-and-contracts/c02-domain-boundaries-data-ownership-and-contracts/README.md) |
| Prerequisite | [V05/C03 — Query planning, indexes and access paths](../../v05-data-models-engines-and-lifecycle/c03-query-planning-indexes-and-access-paths/README.md) |
| Prerequisite | [V05/C05 — Partitioning, sharding and rebalancing](../../v05-data-models-engines-and-lifecycle/c05-partitioning-sharding-and-rebalancing/README.md) |
| Prerequisite | [V05/C06 — Schema evolution, data migration and retention](../../v05-data-models-engines-and-lifecycle/c06-schema-evolution-data-migration-and-retention/README.md) |
| Source reading | [Page-local evidence and versions](local-and-distributed-cache-design.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.

## Chapter source ledger

The following original citation rows, review limits and earlier topical routes are retained once for this chapter. Each question page points here and retains its inline citations. Evidence coverage must be judged at the actual claim and version, not inferred from source-list length.

<!-- tycho-question-source:tycho.page.33742c54f667446cbf57cb9f3696a533:9 -->
## 8. Public source ledger and nonclaims

| Public source | Narrow support | Does not establish |
|---|---|---|
| [Caffeine Eviction](https://github.com/ben-manes/caffeine/wiki/Eviction) | Size, weight and expiration choices | Strong coherence across replicas |
| [Caffeine Refresh](https://github.com/ben-manes/caffeine/wiki/Refresh) | Refresh eligibility and previous-value serving model | Actual app cache freshness bound |
| [Redis cache-aside](https://redis.io/docs/latest/develop/use-cases/cache-aside/) | Read-through-on-miss / TTL / invalidate-on-write pattern | Atomic cross-resource consistency or measured performance |
| [Combined earlier cache research](../../../scaling/local-distributed-caching-and-invalidation.md) | Previously bounded original explanations | Independently accepted final source claim mapping |

- [SRE, *Cascading Failures*](https://sre.google/sre-book/addressing-cascading-failures/),
  inspected 2026-10-21: latency-versus-capacity cache dependence, cold-start scenarios and
  the recovery test. The source's examples are contextual, not universal thresholds.

All application names, diagrams, decisions, numerical examples and tests are original fictional teaching material. No cache implementation or benchmark was exercised.

**Navigation:** proposed owner **V06/C01** in [outline](../../../PROPOSED-STRUCTURE.md), via [scaling landing](../../../scaling/README.md). Read [cache invalidation/stampedes](../c02-hot-keys-cache-stampedes-and-read-amplification/cache-invalidation-stampede-and-hot-keys.md), [source connection pools](../../v03-execution-concurrency-and-flow-control/c05-thread-connection-and-buffer-pools/connection-pools-hikaricp-pgbouncer.md), [overload controls](../../v07-performance-scale-and-resilience/c05-overload-protection-and-graceful-degradation/overload-admission-control-and-graceful-degradation.md).
<!-- /tycho-question-source -->
