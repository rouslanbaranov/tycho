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
summary: "How do hot keys, routing, joins and ownership affect scale? The reading route separates 2 detailed questions from the integrated decision."
route_hints:
  questions:
    - "How do hot keys, routing, joins and ownership affect scale?"
  prerequisites:
    - "tycho.chapter.4a127ad6ab514ede9ff74394e5174f9c"
  related_ids:
    - "tycho.page.0d34dd26886340b89fd4f1499d790a81"
    - "tycho.page.3b048fab91c24b9f8121564b9b0e59bb"
    - "tycho.page.94165346d83c4ff79634d4400f4a9ba7"
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

Begin with the integrated decision, then open the independent question that matches the missing mechanism or observed failure. Read source limits before applying the conclusion.

| Page | Independent question and role |
|---|---|
| [Integrated decision and original walkthrough](shard-keys-hotspots-and-resharding.md) | How do hot keys, routing, joins and ownership affect scale? |
| [Partition ownership, keys and skew](shard-strategies.md) | Which key and routing policy distribute useful work rather than row counts? |
| [Resharding and alternatives](resharding-transition.md) | How can ownership move without accepting conflicting writes or unnecessary distribution? |

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

## Chapter source ledger

The following original citation rows, review limits and earlier topical routes are retained once for this chapter. Each question page points here and retains its inline citations. Evidence coverage must be judged at the actual claim and version, not inferred from source-list length.

<!-- tycho-question-source:tycho.page.0d34dd26886340b89fd4f1499d790a81:6 -->
## Bounded public evidence and status

| ID | Public primary reference and inspected scope | Supports, not an empirical deployment |
|---|---|---|
| E01 | [Vitess 24.0 Resharding guide](https://vitess.io/docs/24.0/user-guides/configuration-advanced/resharding/), **Preparation, Vindexes, Apply VSchema, Create New Shards, Start the Reshard** | Versioned real example of keys/co-location, copy/cutover; not universal online migration guarantee |
| E02 | [Vitess VSchema reference](https://vitess.io/docs/reference/vschema/), **Vindexes and Primary Vindex**; rolling documentation observed 2026-10-19 | Keyspace ID and lookup indirection, not a tested migration for this hypothetical service |
| E03 | [PostgreSQL 17 table partitioning](https://www.postgresql.org/docs/17/ddl-partitioning.html), **Declarative Partitioning and Partition Pruning** | Physical table partitioning and planner behavior; not an application-wide distributed transaction protocol |

All diagrams are original; no Vitess cluster, data move, load generator, index benchmark or independent technical review ran. **Shard count, key and traffic thresholds are not prescribed** by this chapter.

<!-- /tycho-question-source -->
