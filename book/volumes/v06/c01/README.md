---
metadata_version: 1
id: "tycho.chapter.4166e932cbd64ce2a63fe0c6d6eb049a"
kind: "chapter"
parent_id: "tycho.volume.69e6229b222f4535bc0b3941cee1b1cc"
canonical_path: "book/volumes/v06/c01/README.md"
title: "V06/C01 — Local and distributed caching"
topic_ids:
  - "scaling-mechanisms"
perspectives:
  - "architecture"
  - "evaluation"
summary: "How do authority, freshness, eviction and invalidation differ?"
route_hints:
  questions:
    - "How do authority, freshness, eviction and invalidation differ?"
  prerequisites:
    - "tycho.chapter.7031445877fb4f8d831d962d170521c8"
    - "tycho.chapter.e451bfe1e0cb4c588f0576e0b2b7d3d0"
    - "tycho.chapter.3e2e1da8f99c4a7ba05121baf1ef4d91"
    - "tycho.chapter.3d0f6dd1e8e94cd397326e129b5c287f"
  related_ids: []
  excludes:
    - "No new benchmark, source inspection or independent edition review is asserted."
  keywords:
    - "system-design"
    - "edition-navigation"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Editorial synthesis of the linked accepted manuscript; exact source versions and nonclaims remain in its page-local evidence ledger."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-20"
  reviewer: "Codex editorial assembly"
  proof_uri: null
authored_at: "2026-10-20"
updated_at: "2026-10-20"
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

| Page | Owning question |
|---|---|
| [Local and distributed caching: authority, freshness and placement](local-and-distributed-cache-design.md) | How do authority, freshness, eviction and invalidation differ? |

The page is one bounded explanation. Its mechanism, failure analysis and evidence are kept together rather than split to meet a numerical page quota. Use these section entry points:

- [1. Begin with the authority and the data contract](local-and-distributed-cache-design.md#1-begin-with-the-authority-and-the-data-contract).
- [2. Three basic placements](local-and-distributed-cache-design.md#2-three-basic-placements).
- [Engineering walkthrough — Local cache update versus cross-instance freshness](local-and-distributed-cache-design.md#engineering-walkthrough-local-cache-update-versus-cross-instance-freshness).
- [8. Public source ledger and nonclaims](local-and-distributed-cache-design.md#8-public-source-ledger-and-nonclaims).

## Boundaries and further reading

The preceding and following chapters supply context; this landing does not replace their canonical mechanisms. Follow the exact source ledger on the child page when a claim depends on a product version or historical period.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V06 — Caching, indexing and information retrieval](../README.md) |
| Previous | [V05/C07 — Replication, backups and restore drills](../../v05/c07/README.md) |
| Next | [V06/C02 — Hot keys, cache stampedes and read amplification](../c02/README.md) |
| Prerequisite | [V02/C02 — Domain boundaries, data ownership and contracts](../../v02/c02/README.md) |
| Prerequisite | [V05/C03 — Query planning, indexes and access paths](../../v05/c03/README.md) |
| Prerequisite | [V05/C05 — Partitioning, sharding and rebalancing](../../v05/c05/README.md) |
| Prerequisite | [V05/C06 — Schema evolution, data migration and retention](../../v05/c06/README.md) |
| Source reading | [Page-local evidence and versions](local-and-distributed-cache-design.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.
