---
metadata_version: 1
id: "tycho.page.0d34dd26886340b89fd4f1499d790a81"
kind: "page"
parent_id: "tycho.chapter.3e2e1da8f99c4a7ba05121baf1ef4d91"
canonical_path: "book/volumes/v05/c05/shard-keys-hotspots-and-resharding.md"
title: "Sharding, partition keys, hotspots and safe resharding"
topic_ids:
  - "scaling-mechanisms"
perspectives:
  - "architecture"
summary: "Integrated question, original scenario and transfer limits for Partitioning, sharding and rebalancing. Detailed mechanisms have separate question owners."
route_hints:
  questions:
    - "How do hot keys, routing, joins and ownership affect scale?"
  prerequisites: []
  related_ids:
    - "tycho.page.3b048fab91c24b9f8121564b9b0e59bb"
    - "tycho.page.94165346d83c4ff79634d4400f4a9ba7"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Sharding"
    - "partition"
    - "keys"
    - "hotspots"
    - "and"
    - "safe"
    - "resharding"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Only exact URL matches to the global source register are normalized here. Page-local case and evidence ledger IDs remain in the body; no claim-level mapping or source inspection is inferred."
content_review:
  status: "draft"
  reviewed_at: null
  reviewer: null
  proof_uri: null
authored_at: "2026-10-18"
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---
<!-- tycho-question-source:tycho.page.0d34dd26886340b89fd4f1499d790a81:-1 -->

# Sharding, partition keys, hotspots and safe resharding

> Tycho bounded technical research for [Issue #84](https://github.com/rouslanbaranov/tycho/issues/84). Public source reading: **2026-10-19**. Selected implementation reference: **Vitess 24.0** Resharding/VSchema documentation. All workload numbers and diagrams are original synthetic models; there is no database shard cluster, measured benchmark or independently approved migration.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.0d34dd26886340b89fd4f1499d790a81:0 -->
## Purpose and mission

Splitting a database into shards is useful only if **resource or operational constraints** justify distributing ownership and the application can tolerate the resulting coordination and migration requirements. More shards cannot automatically spread a single hot tenant or repair a poorly chosen authorization/data consistency boundary.

**Primary question:** How should an architect select a shard key, handle skew and high-cardinality access, preserve co-located transactions and move data to a new shard map without losing correctness?

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.0d34dd26886340b89fd4f1499d790a81:7 -->
## Applied M9 evidence: what transfers and what does not

These examples connect the chapter's conditional mechanism to published experiences or synthetic decision exercises. A historical company report is **first-party, time-scoped evidence**, not a controlled Tycho benchmark; an M9 decision playbook is **original synthetic analysis**, not a company decision.

**Case lens — [Netflix — Cassandra time-series splits](../../../cases/netflix-cassandra-dynamic-time-series-splits.md)**. **Relevant mechanism or architectural contrast:** Wide partitions require adaptive ownership and reader compatibility, with workload-dependent split strategies. **Not established by this report/playbook:** Netflix results do not mean every Cassandra partition should be dynamically split, or that reported gains apply to another dataset.

**Transfer test:** before applying the lesson to another legacy system, identify the exact workload, source date, relevant runtime/protocol versions, state authority, failure/recovery gate and the new observation that would reverse the choice. Follow the case's public evidence ledger rather than treating its link as independent proof.
<!-- /tycho-question-source -->

## Integrated decision and reading route

Choose shard keys and routing with workload skew, cross-shard operations and ownership transfer in view.

Evenly distributing rows can leave one tenant or key overloaded; resharding must preserve correct reads and writes during movement.

The detailed pages separate the mechanisms that make this decision conditional:

- [Partition ownership, keys and skew](shard-strategies.md) — Which key and routing policy distribute useful work rather than row counts?
- [Resharding and alternatives](resharding-transition.md) — How can ownership move without accepting conflicting writes or unnecessary distribution?

[Chapter introduction, ordered pages and full source ledger](README.md). Original source labels retain their historical scope; this editorial decomposition does not turn proposed experiments into executed evidence.
