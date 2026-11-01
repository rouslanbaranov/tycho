---
metadata_version: 1
id: tycho.page.38c477e8694b55134ee49d1f8ec255f0
kind: page
parent_id: tycho.chapter.3b9ec227ed58b92c0004eb0d39099142
canonical_path: book/volumes/v11-pattern-atlas/c09-scalability/shuffle-sharding.md
title: Shuffle Sharding
topic_ids:
- scalability-and-load-distribution
perspectives:
- architecture
- operations
- evaluation
summary: Decision card for Shuffle Sharding.
route_hints:
  questions:
  - Should each tenant be assigned a random subset of shards to reduce overlapping
    blast radius?
  prerequisites:
  - tycho.chapter.3b9ec227ed58b92c0004eb0d39099142
  related_ids:
  - tycho.chapter.3b9ec227ed58b92c0004eb0d39099142
  excludes:
  - No owner acceptance is claimed for this card.
  keywords:
  - pattern atlas
  - shuffle sharding
evidence_scope:
  source_ids:
  - src.cortex-shuffle-sharding
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

# Shuffle Sharding

**Identity.** Shuffle Sharding; family Scalability and load distribution; kind
scalability-pattern; priority advanced.

**Decision question.** Should each tenant be assigned a random subset of shards to reduce
overlapping blast radius?

**Good-fit conditions.** Many tenants exist; shard assignment can be consistent; enough
shards exist to reduce overlap.

**Hard contraindications.** Reject when there are too few shards, when assignment cannot
be stable, or when the operational cost of many assignments is high.

**Competing alternative.** Cell-based partitioning or dedicated shards. Reverse the choice
when overlap reduction does not justify assignment complexity.

**Failure and recovery.** Hot tenants and uneven overlap are common; verify assignment in
the owner section.

**Technical owner.**
 [Shuffle
Sharding](../../v08-delivery-deployment-and-recovery/c06-high-availability-and-failure-domain-placement/cells-shuffle-sharding.md#shuffle-sharding)
— shuffle sharding is bounded, not a hashing implementation guide.

**Sources.**
[src.cortex-shuffle-sharding](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch5-cortex-shuffle.2026-10-21: all eighteen served headings
read. The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Cell-Based Architecture; Sharding; Tenant Isolation; Load Balancing.
