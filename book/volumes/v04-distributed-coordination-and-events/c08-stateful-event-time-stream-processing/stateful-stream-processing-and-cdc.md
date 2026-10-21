---
metadata_version: 1
id: "tycho.page.a2c47a0850154eaa95e1eb97e23f9c71"
kind: "page"
parent_id: "tycho.chapter.566e576a945b44628386d520214d6c4a"
canonical_path: "book/volumes/v04-distributed-coordination-and-events/c08-stateful-event-time-stream-processing/stateful-stream-processing-and-cdc.md"
title: "Stateful stream processing, Kafka Streams, Flink and CDC"
topic_ids:
  - "integration-architecture"
perspectives:
  - "architecture"
summary: "Integrated question, original scenario and transfer limits for Stateful/event-time stream processing. Detailed mechanisms have separate question owners."
route_hints:
  questions:
    - "How do replay, watermarks, state stores and recovery shape correctness?"
  prerequisites: []
  related_ids:
    - "tycho.page.54c4335d1dd142e8b794daf4768fc3d2"
    - "tycho.page.205058a4a2da4523842395cc7864c8f0"
    - "tycho.page.57478c7e1ff6443fb3f41a2f143caa9b"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Stateful"
    - "stream"
    - "processing"
    - "Kafka"
    - "Streams"
    - "Flink"
    - "and"
    - "CDC"
evidence_scope:
  source_ids:
    - "src.kafka-streams"
  claim_ids: []
  status: "source-linked"
  notes: "Only exact URL matches to the global source register are normalized here. Page-local case and evidence ledger IDs remain in the body; no claim-level mapping or source inspection is inferred."
content_review:
  status: "draft"
  reviewed_at: null
  reviewer: null
  proof_uri: null
authored_at: "2026-10-18"
updated_at: "2026-10-21"
source_inspection_date: null
content_verified_at: null
---
<!-- tycho-question-source:tycho.page.a2c47a0850154eaa95e1eb97e23f9c71:-1 -->

# Stateful stream processing, Kafka Streams, Flink and CDC

> Tycho Issue [#81](https://github.com/rouslanbaranov/tycho/issues/81), proposed V04/C08. Source reading 2026-10-18. **Pinned examples:** Apache Kafka Streams documentation 4.1, Apache Flink documentation release **2.1** (explicitly archived/outdated), PostgreSQL documentation 17 and Debezium 3.6. Original synthetic diagrams and arithmetic; not an executed stream processor, validated exactly-once guarantee or current-version benchmark.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.a2c47a0850154eaa95e1eb97e23f9c71:0 -->
## Purpose and mission

Processing records in order is not the same as calculating correct, recoverable *state* while inputs arrive late, operators restart, partitions rebalance and external systems change. This page owns the recovery, event-time and CDC boundary. The Kafka Streams/Flink **state/position comparison** is on [processor-recovery.md](processor-recovery.md); this page does not repeat that table.

**Primary question:** Which durable positions, state snapshots, event-time policies and sink semantics must align for a stream processor to recover without silently dropping or repeating material business effects?

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.a2c47a0850154eaa95e1eb97e23f9c71:7 -->
## Engineering walkthrough — Late correction after checkpoint and restore

**Original synthetic event-time scenario:** an aggregate computes total reservations per business day from a CDC log. Event E5 reports a booking at event time 10:01 but arrives after the operator has advanced its watermark beyond that window. Another event cancels the booking later. A checkpoint captures operator state and source positions, but a checkpoint alone does not decide whether a late business correction should be discarded, sent as an update or routed to a reconciliation stream.

| Boundary | Owner and question | Failure to detect |
|---|---|---|
| Source CDC | Database transaction position and stable change identity | Snapshot followed by replay duplicates a change without dedup |
| Event time/watermark | Operator's chosen lateness policy | Window silently closes before valid late correction arrives |
| Checkpoint | Consistent recoverable operator state/offset as specified by runtime | External sink side effect committed outside checkpoint protocol |
| Savepoint/deployment | Versioned state schema and migration compatibility | Restored state has incompatible serializer or changed key semantics |

**Recovery trace:** after checkpoint C, a sink writes the count but crashes before all downstream acknowledgment; replay may produce a duplicate correction. Correctness depends on the sink's idempotent/upsert or transaction contract, plus a declared policy for reopening finalized windows. A business that prohibits changing settled invoices may need a separate adjustment event rather than silently revising totals.

The chapter's Flink and Kafka Streams documentation supports named state/checkpoint mechanisms at specified versions, not one universal exactly-once guarantee for arbitrary stores. **Proposed, not executed:** crash after a sink commit, restore state from C, inject a correction older than the watermark, compare full business totals and downstream duplicates. Reject the chosen stream architecture if its lateness/retraction policy cannot satisfy the real reconciliation requirement; a scheduled batch backfill may be safer.

<!-- /tycho-question-source -->

## Integrated decision and reading route

Treat event time, watermarks, retained state, checkpointing and replay as one declared processing contract.

A consistent processor checkpoint cannot recover an expired input or reverse an independently committed external effect.

The detailed pages separate the mechanisms that make this decision conditional:

- [CDC, task state and changelog replay](cdc-state.md) — Which records make an input and local processor state recoverable?
- [Checkpoints, watermarks and late data](checkpoints-time.md) — Which state boundary and late-data policy define a corrected result?
- [Processor selection and recovery experiments](processor-recovery.md) — Which topology and external effect must a recovery test actually cover?

[Chapter introduction, ordered pages and full source ledger](README.md). Original source labels retain their historical scope; this editorial decomposition does not turn proposed experiments into executed evidence.
