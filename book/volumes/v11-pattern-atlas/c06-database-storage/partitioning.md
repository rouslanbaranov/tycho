---
metadata_version: 1
id: tycho.page.d5845f0958de98990f19d54abc92fe0b
kind: page
parent_id: tycho.chapter.22fa23c6c7a6b0c29a52137bc67a00c9
canonical_path: book/volumes/v11-pattern-atlas/c06-database-storage/partitioning.md
title: Partitioning
topic_ids:
- database-and-storage-architecture
perspectives:
- architecture
- operations
- evaluation
summary: Decision card for Partitioning.
route_hints:
  questions:
  - Should a large table or stream be divided into partitions for pruning, retention
    or parallelism?
  prerequisites:
  - tycho.chapter.22fa23c6c7a6b0c29a52137bc67a00c9
  related_ids:
  - tycho.chapter.22fa23c6c7a6b0c29a52137bc67a00c9
  excludes:
  - No owner acceptance is claimed for this card.
  keywords:
  - pattern atlas
  - partitioning
evidence_scope:
  source_ids:
  - src.postgresql
  claim_ids: []
  status: source-linked
  notes: Source-level bindings remain in the owner unit.
content_review:
  status: self-checked
  reviewed_at: '2026-11-01'
  reviewer: Automated authoring agent
  proof_uri: null
authored_at: '2026-11-01'
updated_at: '2026-11-01'
source_inspection_date: '2026-10-21'
content_verified_at: null
---

# Partitioning

**Identity.** Partitioning; family Database and storage architecture; kind
data-distribution-pattern; priority core.

**Decision question.** Should a large table or stream be divided into partitions for
pruning, retention or parallelism?

**Good-fit conditions.** Partition key aligns with query/retention; partition count is
manageable; pruning is observable; maintenance is owned.

**Hard contraindications.** Reject when queries cross all partitions, when partition count
grows unbounded, or when partition keys create skew.

**Competing alternative.** Single table/index or sharding across nodes. Reverse the choice
when partition maintenance and pruning no longer justify the split.

**Failure and recovery.** Partition skew and maintenance are common; verify
pruning/lifecycle in the owner section.

**Technical owner.**
 [Sharding, partition keys, hotspots and safe
resharding](../../v05-data-models-engines-and-lifecycle/c05-partitioning-sharding-and-rebalancing/shard-keys-hotspots-and-resharding.md#partitioning)
— partition key and pruning are bounded; per-engine partition mechanics are implementation-specific.

**Sources.** [src.postgresql](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch3-pg-partition.2026-10-21: all thirteen headings read.
The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Sharding; Consistent Hashing; Index Table; Online Data Migration.
