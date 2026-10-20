---
metadata_version: 1
id: "tycho.page.e067b74eabc24cabb209ca8835c0f7cd"
kind: "page"
parent_id: "tycho.chapter.7a07973ba5314c3983a4c93acc1d1b89"
canonical_path: "book/volumes/v03/c04/resume-cancellation.md"
title: "Cancellation, reconnect and durable resume"
topic_ids:
  - "execution-models"
perspectives:
  - "architecture"
summary: "Which persisted state permits replay after a disconnect and when must a client resnapshot?"
route_hints:
  questions:
    - "Which persisted state permits replay after a disconnect and when must a client resnapshot?"
  prerequisites:
    - "tycho.page.fbb4bc905d02495dbe3d7675d8670235"
  related_ids:
    - "tycho.chapter.7a07973ba5314c3983a4c93acc1d1b89"
    - "tycho.page.da7cd1ad59584b8a8ece7aab0f8f35b5"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "resume"
    - "cancellation"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Bounded question from tycho.page.da7cd1ad59584b8a8ece7aab0f8f35b5; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
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
# Cancellation, reconnect and durable resume

**Owning question:** Which persisted state permits replay after a disconnect and when must a client resnapshot?

This page belongs to [V03/C04 — Asynchronous APIs and streaming](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.da7cd1ad59584b8a8ece7aab0f8f35b5:4 -->
## 4. Cancellation is not rollback, and reconnect is not replay

The [gRPC cancellation guide](https://grpc.io/docs/guides/cancellation/) explains that when clients cancel or deadlines expire, servers should stop work and propagate the signal where possible; application code may need to cooperate. This cannot undo an already committed write or external effect.

A reconnecting stream must define:
- cursor/checkpoint or stable event ID, if replay is supported;
- exact ordering scope (one connection, one partition, one entity or total order);
- delivery mode and gap/duplicate handling;
- expiration and retention after which resume cannot succeed;
- whether a stream acknowledgment means transport received, consumer processed, or committed business effect;
- how protocol/schema versions coexist and unsupported events fail.

An ephemeral live stream with no durable source **cannot promise resumability**. If durable replay is required, store the relevant event/offset outside the connection and make consumer effects idempotent as appropriate. See [Kafka/partition ordering](../../v04/c07/kafka-partitions-replication-and-contracts.md), [outbox](../../../distributed/transactional-outbox-and-idempotency.md) and [stateful streaming](../../v04/c08/stateful-stream-processing-and-cdc.md).

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.da7cd1ad59584b8a8ece7aab0f8f35b5:5 -->
## 5. Which architecture is justified?

| Candidate | Benefit when applicable | Failure condition |
|---|---|---|
| Unary API + pagination | Simple bounded reads and retries | Interactive updates are truly continuous |
| Server-streaming RPC | Progressive responses without waiting for entire data | Slow subscribers retain unbounded state |
| Bidirectional RPC | Concurrent producer/consumer interaction needed | No cancellation, order or backpressure contract |
| Reactor/Reactive Streams | End-to-end nonblocking demand coordination under supported drivers | A blocking adapter defeats bounded demand |
| Durable job + status/stream | Work must survive client disconnect | Job identity/state/cleanup not persisted |

A transport's popularity is not evidence of fit. Prefer a unary bounded API when the user needs one result; choose streaming for genuine incremental value, and durable jobs when completion survives the connection.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.da7cd1ad59584b8a8ece7aab0f8f35b5:6 -->
## 6. Proposed negative experiments

1. Fast producer with slow consumer: assert bounded memory and known overload behavior.
2. Cancel after the stream has emitted data: assert cleanup and correct partial-result labeling.
3. Timeout immediately after committing a side effect: reconcile by stable operation identity.
4. Disconnect/reconnect at a message boundary: verify duplicates, gaps and cursor expiry under the stated replay contract.
5. Mix old/new event schemas: unsupported/unknown fields must not silently corrupt semantics.
6. Make downstream connection pool saturate while streaming: record wait, admitted work and user-visible outcomes.
7. Keep open and closed load schedules distinct; measure transport bytes and *business completions* separately.

These fixtures are **not executed**, and a published Reactive Streams or gRPC specification does not prove the tested implementation conforms.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](stream-contracts.md) |
| Next | [Continue the reasoning](README.md) |
| Integrated question | [Original scenario and limits](asynchronous-apis-streaming-and-cancellation.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.
