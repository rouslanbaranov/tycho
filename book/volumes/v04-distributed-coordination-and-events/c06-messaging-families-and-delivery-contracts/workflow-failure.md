---
metadata_version: 1
id: "tycho.page.148a37ff87ca4e42a2fec625c65319b0"
kind: "page"
parent_id: "tycho.chapter.23e79f6cb03b4206a5c82494bc5c2928"
canonical_path: "book/volumes/v04-distributed-coordination-and-events/c06-messaging-families-and-delivery-contracts/workflow-failure.md"
title: "Workflow state and messaging failure gates"
topic_ids:
  - "integration-architecture"
perspectives:
  - "architecture"
summary: "When does a queue need an additional durable business-state protocol?"
route_hints:
  questions:
    - "When does a queue need an additional durable business-state protocol?"
  prerequisites:
    - "tycho.page.0eee61f261054af0ad728d791036c5f4"
  related_ids:
    - "tycho.chapter.23e79f6cb03b4206a5c82494bc5c2928"
    - "tycho.page.98616bdc3c514ea997b2cfe30ad7c070"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "workflow"
    - "failure"
evidence_scope:
  source_ids:
    - "src.nats"
    - "src.rabbitmq"
  claim_ids: []
  status: "source-linked"
  notes: "Bounded question from tycho.page.98616bdc3c514ea997b2cfe30ad7c070; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-20"
  reviewer: "Codex editorial decomposition"
  proof_uri: null
authored_at: "2026-10-20"
updated_at: "2026-10-22"
source_inspection_date: null
content_verified_at: null
---
# Workflow state and messaging failure gates

**Owning question:** When does a queue need an additional durable business-state protocol?

This page belongs to [V04/C06 — Messaging families and delivery contracts](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.98616bdc3c514ea997b2cfe30ad7c070:3 -->
## 3. A durable workflow is more than a queue

Suppose a fictional registration process must: hold a seat, request external approval, wait up to 24 hours for a human review, then either confirm or release capacity. A message queue can deliver each step, but does not by itself persist **the entire multi-step business state machine, timers, cancellation policy and compensation outcome**.

A durable workflow engine is an architectural **candidate** if it persistently records process progress, timer deadlines, retry identities, versions, transitions and compensation logic under an explicit recovery contract. However, no named workflow engine is recommended or behavior guaranteed by this page: version-specific product analysis and failure experiments must be performed before selecting one.

```mermaid
stateDiagram-v2
    [*] --> SeatHeld
    SeatHeld --> WaitingApproval: Send verified approval request
    WaitingApproval --> Confirmed: Approval accepted before deadline
    WaitingApproval --> Releasing: Rejected / timeout / cancellation
    Releasing --> Released: Compensation confirmed
    Releasing --> RequiresRepair: Compensation uncertain
    RequiresRepair --> Released: Durable reconciliation succeeds
    Confirmed --> [*]
    Released --> [*]
```

Text alternative: a long-running process holds a seat and waits for approval. It either confirms or initiates release. Failed or ambiguous compensation moves into a repair state, not an invented success. This original state machine is **not** executed by a workflow engine or broker.

Use the [saga/isolation research](../c03-consistency-and-distributed-transactions/transaction-isolation-and-sagas.md) for compensation and concurrency. Choosing a workflow product does not make its external SQL transactions automatically atomic.

<!-- /tycho-question-source -->

> **Pattern atlas:**
> [Request-Reply Messaging](../../v11-pattern-atlas/c03-messaging-integration/README.md#request-reply-messaging) — decision conditions and contraindications.
> [Correlation Identifier](../../v11-pattern-atlas/c03-messaging-integration/README.md#correlation-identifier) — decision conditions and contraindications.
> [Claim Check](../../v11-pattern-atlas/c03-messaging-integration/README.md#claim-check) — decision conditions and contraindications.
> [Dead Letter Channel / DLQ](../../v11-pattern-atlas/c03-messaging-integration/README.md#dead-letter-channel--dlq) — decision conditions and contraindications.

<!-- tycho-question-source:tycho.page.98616bdc3c514ea997b2cfe30ad7c070:4 -->
## 4. Failure and applicability gates

| Workload/failure property | What to measure or test before recommending |
|---|---|
| One hot queue/stream subject | Arrival mix, key skew, consumer concurrency and fair scheduling |
| Producer acknowledgement loss | Broker's accepted/durable state, retry identity and duplicate risk |
| Offline consumer for days | Retention, storage growth/backlog catch-up, expiry and resumption semantics |
| Rebalanced consumer ownership | In-flight effect, ack/cursor commit and side-effect idempotence |
| Cross-region or storage loss | Quorum location, backup/restore, RPO/RTO and replay tests |
| Poison message or schema mismatch | Quarantine/retry budget, dead-letter policy and source of truth |
| Long-running process | Durable state, timers, compensation and human intervention ownership |

**Insufficient evidence:** "We send 10,000 messages/s. Which broker is fastest and cheapest?" Cannot answer without payload/size distribution, replication/durability, subscriber count, retention, batch/ack mode, failure headroom, security and an apples-to-apples benchmark. User and message counts alone are not enough.

<!-- /tycho-question-source -->

## Scheduled runs, durable timers and poison-work recovery

**Enrichment contract:** keep scheduling, execution attempts and the resulting business effect separately identifiable. A queue acknowledgement or workflow completion flag is not proof that an external effect occurred once.

Generic scheduling, missed-run, overlap and durable-timer mechanics are owned by the
[V04/C05 periodic-work page](../c05-outbox-inbox-sagas-and-durable-workflows/periodic-work-leases-and-exactly-once.md).
This section keeps only the messaging-specific consequence: a queue acknowledgement or
workflow-completion flag is not proof that the scheduled external effect occurred once.

### Poison work is a policy state

An invalid schema or permanently rejected target is not repaired by retrying forever. Classify transient, permanent and unknown outcomes; cap attempts and total age; preserve enough evidence in quarantine to diagnose without leaking payloads. A dead-letter queue is a holding mechanism, not successful delivery or an automatically safe replayer.

For a fictional failed publication command K, repair may require correcting input while preserving the same logical effect identity, or creating an explicitly new operation if intent changes. Replaying with a new ID merely to bypass deduplication risks a duplicate external effect. Recheck current authorization before repair.

**Dead-letter mechanism.** A dead-letter channel routes a message that exceeds its retry or
age policy to a quarantine queue, preserving payload, headers and failure reason. It is a
holding and triage mechanism, not delivery, repair or an automatically safe replay.

**Alternative.** Retrying with backoff, dropping with an audit record, or parking the work in
a repair table/outbox may be preferable when the failure is deterministic or the broker
cannot retain evidence safely. Reverse the DLQ choice when quarantine retention and manual
repair cost exceed the value of preserving the message.

### Workflow history and upgrades

Temporal's overview describes replay against recorded history; its patching documentation explains explicit branches for compatible changes. That supports a concrete concern: changing code that old histories will replay is an ongoing compatibility obligation. It does not prove arbitrary application effects are exactly once.

An original upgrade plan separates new executions from histories already waiting for approval. Retain a compatible worker route or a supported history-aware change until old executions finish or are deliberately migrated. Record the schema/version of pending input, timer meaning and compensation step. Removing the old branch before its histories expire can make recovery fail only after a later worker restart.

~~~mermaid
stateDiagram-v2
    [*] --> Scheduled
    Scheduled --> Claimed: Stable run identity
    Claimed --> Waiting: Durable timer or external approval
    Waiting --> Running: Recorded event permits progress
    Running --> Completed: Required effect resolved
    Running --> Retryable: Transient failure within budget
    Retryable --> Claimed: Same logical identity
    Running --> Quarantined: Permanent or exhausted failure
    Quarantined --> RepairAuthorized: Reviewed correction
    RepairAuthorized --> Claimed: Explicit repair contract
~~~

Text alternative: durable state, not process memory, explains why a job may run again. Quarantine requires a separate repair decision. This synthetic state machine was not run in a workflow engine.

### Sources and acceptance

Inspected selected passages 2026-10-20: [Distributed Periodic Scheduling with Cron](https://sre.google/sre-book/distributed-periodic-scheduling/) (launch failure policy), [Workflow message passing and versioning](https://docs.temporal.io/workflow-execution) (history/replay), [Patching](https://docs.temporal.io/patching) (compatible changes). SDK-specific APIs and worker-version routing are not prescribed.

Proposed tests: kill scheduler after persisting intent but before dispatch; kill worker after effect but before acknowledgement; replay quarantined work; pause through several scheduled intervals; restore an old workflow history on a new worker version. Require correct interval coverage and effect identity. No scheduler, broker or workflow execution was performed.

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](message-selection.md) |
| Next | [Continue the reasoning](README.md) |
| Integrated question | [Original scenario and limits](messaging-families-and-durable-workflows.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.

## Bounded pattern ownership notes

These notes define the decision boundary for atlas cards whose mechanism is
not the main subject of this page. They are synthetic design guidance, not
measured evidence, and they do not create a new source claim.

### Claim Check

A claim check stores a large or sensitive payload outside the message and sends a claim
token instead. It needs payload lifecycle, authorization, expiry, integrity and a cleanup
rule for abandoned claims. Use it when message size, retention or access boundaries make
an inline payload unsafe. Do not use it when the payload is small enough to inline or when
an external store would create an unacceptable consistency dependency. An untracked
claim store becomes a data-retention liability. Bind the claim token to the message and
tenant and to a payload digest; a token must not resolve to another payload. The retrieval
hop needs a latency budget and bounded retries.

The failure path is an orphaned payload or a token that outlives its authorization; expire
and garbage-collect claims, and make the consumer fail closed when the claim cannot be
resolved. An inline payload with encryption and size limits is the alternative when the
transport can carry it safely.

### Correlation Identifier

A correlation identifier ties together messages that belong to one request, workflow or
conversation. It needs a generation rule, propagation across asynchronous boundaries, a
retention window and a collision check. Uniqueness is scoped to the operation, not global; a
value reused across operations is a collision, and generation must verify that scope. Use it
when independent messages must be joined for diagnosis, deduplication or reply
routing. Do not use it as an authorization token or when the transport already
provides an equivalent identity.

The failure path is a lost or duplicated identifier; carry it in the message contract and
record it at every boundary. Ambiguous matching or an expired identifier needs a disposition:
quarantine unmatched messages, resolve by a secondary key, or reissue; an expired identifier
maps to a dead-letter or audit record with an owner. A transport-native message
identity is the alternative when the broker guarantees the needed scope and
lifetime.

**Limits.** Correlation is not deduplication: it groups messages but does not prove one effect;
identifier retention and trust boundaries need an owner.

### Request-Reply Messaging

A requester sends a message with a reply address and a correlation value, and the responder returns
a message that the requester matches to the original request. The reply channel is durable, has an
owner and is cleaned after its retention window. A reply must correlate to exactly one
outstanding request and must not be processed as a new command by another consumer.

A lost request or reply leaves an unresolved operation; expose the outstanding request record, apply
a reply deadline and reconcile before retrying. A reply after the deadline is late, not valid for
a new operation: detect it from the request state and quarantine or audit it. A duplicate reply is
deduplicated by request and responder identity; only the first accepted reply is applied. Request
state and dedup records must outlive the reply deadline, or a late reply becomes an orphan with no
route. Synchronous RPC with a deadline is simpler when the responder is reachable and the work fits
the request budget; choose messaging when availability or
latency requires decoupling.

**Limits.** Reply queues, correlation state and orphaned replies are operational costs; a lost
reply must be distinguishable from a slow one, and the requester needs idempotent effects.

### Dead Letter Channel-DLQ

A quarantine queue receives a message after its retry or age policy is exhausted, retaining
payload, headers and failure context. The DLQ is a policy state, not a second work queue
that silently retries forever.

Retrying cannot repair an invalid schema or a permanently rejected target. Separate
transient, permanent and unknown outcomes; bound attempts and age; keep diagnostic evidence
without leaking payload. The DLQ needs an owner, an alert threshold, a retention horizon, a
capacity limit, an access policy and a cleanup owner. A replay procedure preserves the
original effect identity, reauthorizes the action and checks whether the effect was already
committed before republishing; a blind replay is a duplicate-effect risk.

When failure is deterministic or evidence cannot be retained safely, prefer bounded retry with
audit, drop with a record, or a repair table/outbox. A
DLQ is a fit when the failure is inspectable and a human or repair job can decide the terminal
outcome.

