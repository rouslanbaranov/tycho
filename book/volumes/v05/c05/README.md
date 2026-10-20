---
metadata_version: 1
id: "tycho.chapter.3e2e1da8f99c4a7ba05121baf1ef4d91"
kind: "chapter"
parent_id: "tycho.volume.01d303aaa7984edaac4127884592dd75"
canonical_path: "book/volumes/v05/c05/README.md"
title: "V05/C05 — Partitioning, sharding and rebalancing"
topic_ids:
  - "scaling-mechanisms"
perspectives:
  - "architecture"
  - "evaluation"
summary: "How do hot keys, routing, joins and ownership affect scale?"
route_hints:
  questions:
    - "How do hot keys, routing, joins and ownership affect scale?"
  prerequisites:
    - "tycho.chapter.4a127ad6ab514ede9ff74394e5174f9c"
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

# V05/C05 — Partitioning, sharding and rebalancing

## Purpose and mission

How do hot keys, routing, joins and ownership affect scale? This chapter owns that question within data models, engines and lifecycle. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Choose shard keys and routing with workload skew, cross-shard operations and ownership transfer in view.

Evenly distributing rows can leave one tenant or key overloaded; resharding must preserve correct reads and writes during movement. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

| Page | Owning question |
|---|---|
| [Sharding, partition keys, hotspots and safe resharding](shard-keys-hotspots-and-resharding.md) | How do hot keys, routing, joins and ownership affect scale? |

The page is one bounded explanation. Its mechanism, failure analysis and evidence are kept together rather than split to meet a numerical page quota. Use these section entry points:

- [1. Distinguish physical partitions, logical ownership and replicas](shard-keys-hotspots-and-resharding.md#1-distinguish-physical-partitions-logical-ownership-and-replicas).
- [2. Why shard-key selection cannot be made from average RPS](shard-keys-hotspots-and-resharding.md#2-why-shard-key-selection-cannot-be-made-from-average-rps).
- [Bounded public evidence and status](shard-keys-hotspots-and-resharding.md#bounded-public-evidence-and-status).
- [Applied M9 evidence: what transfers and what does not](shard-keys-hotspots-and-resharding.md#applied-m9-evidence-what-transfers-and-what-does-not).

## Boundaries and further reading

The preceding and following chapters supply context; this landing does not replace their canonical mechanisms. Follow the exact source ledger on the child page when a claim depends on a product version or historical period.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V05 — Data models, engines and lifecycle](../README.md) |
| Previous | [V05/C04 — Alternative data models and stores](../c04/README.md) |
| Next | [V05/C06 — Schema evolution, data migration and retention](../c06/README.md) |
| Prerequisite | [V05/C04 — Alternative data models and stores](../c04/README.md) |
| Source reading | [Page-local evidence and versions](shard-keys-hotspots-and-resharding.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.
