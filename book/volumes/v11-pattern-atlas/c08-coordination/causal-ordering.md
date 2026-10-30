---
metadata_version: 1
id: "tycho.page.4472c6e01fbc41a4af74980b737be3f4"
kind: "page"
parent_id: "tycho.chapter.bee261b76181706235dd8fa7ccde01a9"
canonical_path: "book/volumes/v11-pattern-atlas/c08-coordination/causal-ordering.md"
title: "Causal Ordering"
topic_ids:
  - "distributed-systems"
  - "architecture-decisions"
perspectives:
  - "architecture"
  - "evaluation"
summary: >-
  Decision card for Causal Ordering; failure/recovery and alternative bound;
  coverage remains partial-bounded, no promotion.
route_hints:
  questions:
    - >-
      Should operations that are causally related preserve their order without
      requiring a total order?
  prerequisites:
    - "tycho.chapter.bee261b76181706235dd8fa7ccde01a9"
  related_ids:
    - "tycho.chapter.bee261b76181706235dd8fa7ccde01a9"
  excludes:
    - >-
      No sufficient coverage, promotion or owner acceptance is claimed for this
      moved page.
  keywords:
    - "pattern atlas"
    - "causal ordering"
    - "distributed coordination"
evidence_scope:
  source_ids:
    - "src.jepsen-consistency"
    - "src.lamport-time"
    - "src.mattern-vector-time"
    - "src.kafka"
    - "src.kafka-design"
  claim_ids: []
  status: "source-linked"
  notes: >-
    Card cites read.batch4-causal.2026-10-21, read.lamport-time.2026-10-30,
    read.mattern-vector-time.2026-10-30, read.kafka-introduction.2026-10-30
    and read.kafka-design.2026-10-30; owner section and limits are bounded.
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-30"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-30"
updated_at: "2026-10-30"
source_inspection_date: "2026-10-30"
content_verified_at: null
---
# Causal Ordering

**Identity.** Causal Ordering; family Distributed coordination; kind coordination-pattern;
priority advanced.

**Decision question.** Should operations that are causally related preserve their order
without requiring a total order?

**Good-fit conditions.** Happens-before relationships are meaningful; causal metadata such
as vector clocks can be carried; concurrent operations may diverge but must converge once
the same updates are visible; the delivery path preserves or re-establishes that metadata.

**Hard contraindications.** Reject when a total order is required, when causal metadata
cannot be kept with the operation, when clients switch servers without a session
guarantee, or when concurrent writes have no merge rule.

**Competing alternative.** Sequential consistency as the total-order model, a consensus-backed
replicated log as one implementation, or per-key ordering. Jepsen notes that total order
sacrifices availability and latency; Kafka guarantees order per partition and routes same-key
events to one partition, not a topic-wide order. Reverse the choice when causal metadata
cost exceeds the ordering benefit; the cross-partition reading is Tycho.

**Failure and recovery.** A partition is survivable only while each client stays on one
non-faulty server; switching servers can expose missing dependencies. Reordered delivery,
lost vector metadata and lost session continuity can violate causal order. Keep durable
causal metadata, replay/deduplicate and define a merge; Jepsen requires convergence once
the same operations are visible. The server-switch and metadata-loss inferences are Tycho.

**Technical owner.** [Causal Ordering](../../v04-distributed-coordination-and-events/c01-time-causality-and-ordering/causal-order.md#causal-ordering) — causal ordering is bounded, not a universal clock service.

**Sources.** [Reading ledger](../../../../edition/patterns/reading-ledger.v1.json):
read.batch4-causal.2026-10-21 (`src.jepsen-consistency`), read.lamport-time.2026-10-30
(`src.lamport-time`), read.mattern-vector-time.2026-10-30 (`src.mattern-vector-time`),
read.kafka-introduction.2026-10-30 (`src.kafka`) and read.kafka-design.2026-10-30
(`src.kafka-design`). The units are public papers and documentation, not benchmarks;
no experiment was run.

**Decision state.** applicable-under-conditions.

**Related entries.** Session Consistency; Consensus; Read Replicas; Event Sourcing.
