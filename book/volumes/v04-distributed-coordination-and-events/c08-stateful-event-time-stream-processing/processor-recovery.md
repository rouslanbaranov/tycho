---
metadata_version: 1
id: "tycho.page.57478c7e1ff6443fb3f41a2f143caa9b"
kind: "page"
parent_id: "tycho.chapter.566e576a945b44628386d520214d6c4a"
canonical_path: "book/volumes/v04-distributed-coordination-and-events/c08-stateful-event-time-stream-processing/processor-recovery.md"
title: "Processor selection and recovery experiments"
topic_ids:
  - "integration-architecture"
perspectives:
  - "architecture"
summary: "Which topology and external effect must a recovery test actually cover?"
route_hints:
  questions:
    - "Which topology and external effect must a recovery test actually cover?"
  prerequisites:
    - "tycho.page.205058a4a2da4523842395cc7864c8f0"
  related_ids:
    - "tycho.chapter.566e576a945b44628386d520214d6c4a"
    - "tycho.page.a2c47a0850154eaa95e1eb97e23f9c71"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "processor"
    - "recovery"
evidence_scope:
  source_ids:
    - "src.kafka-streams"
  claim_ids: []
  status: "source-linked"
  notes: "Bounded question from tycho.page.a2c47a0850154eaa95e1eb97e23f9c71; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-20"
  reviewer: "Codex editorial decomposition"
  proof_uri: null
authored_at: "2026-10-20"
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---
# Processor selection and recovery experiments

**Owning question:** Which topology and external effect must a recovery test actually cover?

This page belongs to [V04/C08 — Stateful/event-time stream processing](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.a2c47a0850154eaa95e1eb97e23f9c71:5 -->
## 5. Choose the processor for the real topology

| Criterion | Kafka Streams 4.1 documentation | Flink 2.1 documentation |
|---|---|---|
| Deployment integration | Embedded library in application instances interacting with Kafka | Distributed stream job/runtime and checkpoint-managed operator state |
| State ownership | Local task stores with changelog topics | Stateful operators and configured checkpoint/state backends |
| Fault recovery | Task migration/rebalance plus changelog restore | Restore consistent source positions/operator snapshots from checkpoint |
| Scaling boundary | Partition/task assignment and state redistribution | Parallel operators, keyed partitions, checkpoint/rescale compatibility |
| Operational burden | Application instances, task/changelog/offset/standby management | Dedicated job runtime, checkpoint storage, restart/upgrade state governance |
| Exactly-once nuance | Kafka transaction/Streams `exactly_once_v2` scope | Checkpoint + connector/sink-specific guarantee scope |
| Evidence gap | Whether observed consumer/producer modes and topic policies meet needs | Whether actual source/sink/upgrade topology supports desired semantics |

This is a comparison of **documented architectural mechanisms**, not measured product speed/price/feature superiority. Kafka Streams is not automatically better for small jobs, and Flink is not automatically necessary for complex ones.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.a2c47a0850154eaa95e1eb97e23f9c71:6 -->
## 6. Failure/recovery experiments

1. Build an **original synthetic** input fixture with unique event IDs, duplicate deliveries, out-of-order arrivals, and a known expected materialized result.
2. Inject a crash immediately after state update but before output/offset checkpoint; repeat near checkpoint completion.
3. Reassign a partition/operator and verify restored state, emitted output and input position, not just that the process starts.
4. Force input lag and hot-key skew; measure resource/IO impact and time to regain the advertised output freshness.
5. Upgrade schema/state serialization, rollback and restore from a controlled savepoint/changelog position.
6. Add a real external effect and test idempotency/compensation separately; **do not infer** correctness from Kafka/Flink's internal guarantees.

Without a concrete source/sink topology and the above evidence, the correct decision is **measure first**, not to promise exact once, zero loss or fixed checkpoint recovery time.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](checkpoints-time.md) |
| Next | [Continue the reasoning](README.md) |
| Integrated question | [Original scenario and limits](stateful-stream-processing-and-cdc.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.
