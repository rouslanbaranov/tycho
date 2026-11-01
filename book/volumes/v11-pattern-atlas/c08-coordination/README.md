---
metadata_version: 1
id: "tycho.chapter.bee261b76181706235dd8fa7ccde01a9"
kind: "chapter"
parent_id: "tycho.volume.fe327f72cf81df0237ce47b841e8aef5"
canonical_path: "book/volumes/v11-pattern-atlas/c08-coordination/README.md"
title: "V11/C08 — Distributed coordination"
topic_ids:
  - "distributed-systems"
  - "architecture-decisions"
perspectives:
  - "architecture"
  - "evaluation"
summary: "All 9 C08 cards with bounded owner links; decision coverage partial."
route_hints:
  questions:
    - "Which coordination mechanisms preserve safety and progress?"
  prerequisites:
    - "tycho.chapter.b20625a099bc4c82b7d547c32c7da28a"
  related_ids:
    - "tycho.volume.fe327f72cf81df0237ce47b841e8aef5"
    - "tycho.chapter.b20625a099bc4c82b7d547c32c7da28a"
    - "tycho.chapter.69085752a11c69305aa2a369b8ec9d29"
    - "tycho.chapter.3b9ec227ed58b92c0004eb0d39099142"
  excludes:
    - "Bounded owner links; no sufficient coverage or independent review."
  keywords:
    - "pattern atlas"
    - "distributed coordination"
    - "decision layer"
evidence_scope:
  source_ids:
    - "src.raft"
    - "src.kubernetes"
    - "src.kleppmann-distributed-locking"
    - "src.jepsen-consistency"
    - "src.lamport-time"
    - "src.mattern-vector-time"
    - "src.kafka"
    - "src.kafka-design"
    - "src.temporal"
  claim_ids: []
  status: "source-linked"
  notes: >-
    9 cards cite read units; owner links are bounded. Distributed Workflow
    Orchestration moved to a dedicated page on 2026-11-01 with Temporal, AWS
    Step Functions and Cadence sources; no sufficient coverage.
content_review:
  status: "self-checked"
  reviewed_at: "2026-11-01"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-21"
updated_at: "2026-11-01"
source_inspection_date: "2026-11-01"
content_verified_at: null
---
# V11/C08 — Distributed coordination

**Owning question:** Which coordination mechanisms preserve safety and progress?

## Purpose and mission

This chapter is the atlas entry point for **Distributed coordination**. It owns the
conditional decision route for 9 catalog entries, not the deep mechanism explanations.
Read the exact owner section before applying a mechanism claim.

All 9 entries have a self-checked card. Owner sections are bounded: a leader-recovery
or quorum page may own the safety contract without owning every coordination mechanism.

## Pages and reasoning route

Page count is content-dependent. This chapter currently uses one landing page for all
entries; a later split is an editorial change, not a plan failure. Start with the card,
check its conditions and contraindications, then read the exact owner section.

## Entry inventory

Each level-three heading is a stable atlas anchor. Owner links are bounded sections;
none claims sufficient technical or decision coverage.

### Leader Election

See the [Leader Election](leader-election.md) card.

### Consensus

See the [Consensus](consensus.md) card.

### Distributed Lock

See the [Distributed Lock](distributed-lock.md) card.

### Lease-Based Ownership

See the [Lease-Based Ownership](lease-based-ownership.md) card.

### Fencing Tokens

See the [dedicated Fencing Tokens card](fencing-tokens.md).

### Quorum Coordination

See the [Quorum Coordination](quorum-coordination.md) card.

### Causal Ordering

See the [dedicated Causal Ordering card](causal-ordering.md).

### Session Consistency

See the [dedicated Session Consistency card](session-consistency.md).

### Distributed Workflow Orchestration

See the [dedicated Distributed Workflow Orchestration card](distributed-workflow-orchestration.md).

## Chapter result and counterexample

Nine cards establish a conditional decision route. Owner sections are bounded; none
establishes technical sufficiency.

Counterexample: a lease without destination fencing is not evidence for the fencing
card's safety conditions.

## Navigation and prerequisites

- Parent: [V11](../README.md).
- Previous: [V11/C07](../c07-resilience/README.md).
- Next: [V11/C09](../c09-scalability/README.md).
- Prerequisite: V10/C03 — pattern applicability and contraindications.
- Registry: [pattern registry](../../../../edition/patterns/registry.v1.json).
- Card batch: [card batches](../../../../edition/patterns/card-batches.v1.json).
- Coverage map: [candidate coverage](../../../../edition/patterns/coverage-map.v1.json).

## Evidence and known limits

- All 9 cards cite read ledger units; owner links and backlinks are self-checked.
- Owner links are bounded sections, not dedicated pattern pages.
- No entry claims sufficient technical or decision coverage.
- No independent editorial review, benchmark, production observation or runtime test
  is asserted.
