---
metadata_version: 1
id: "tycho.page.113050e25ec643da98578b98eba1c519"
kind: "page"
parent_id: "tycho.chapter.13ad4371e75b49dcb5e082ea62083ee3"
canonical_path: "book/volumes/v03/c01/shared-state-effects.md"
title: "Shared invariants and irreversible effects"
topic_ids:
  - "execution-models"
perspectives:
  - "architecture"
summary: "Why do concurrency-safe classes and cancellation not establish a business invariant?"
route_hints:
  questions:
    - "Why do concurrency-safe classes and cancellation not establish a business invariant?"
  prerequisites:
    - "tycho.page.2cdffb0fc6394a1596c8358c852a30e8"
  related_ids:
    - "tycho.chapter.13ad4371e75b49dcb5e082ea62083ee3"
    - "tycho.page.4e075e4ebc644f0e9b92c05294f62ca4"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "shared"
    - "state"
    - "effects"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Bounded question from tycho.page.4e075e4ebc644f0e9b92c05294f62ca4; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
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
# Shared invariants and irreversible effects

**Owning question:** Why do concurrency-safe classes and cancellation not establish a business invariant?

This page belongs to [V03/C01 — Threads, tasks and coordination](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.4e075e4ebc644f0e9b92c05294f62ca4:4 -->
## 4. Concurrency-safe classes do not enforce business invariants automatically

**Original fictional case:** two threads reserve the last available device from a workshop catalogue. Both read an availability counter of one and attempt to decrement it. A concurrent collection or atomic increment alone may not protect a multi-step invariant across database writes and separate application instances.

Correctness requires a valid atomic transaction or state-owner protocol covering the full check-and-commit decision. A JVM-local semaphore protects one process only; it cannot serialize writes across multiple independently deployed replicas. Adding virtual threads or larger pools does not change the exclusivity rule.

A lock can also be harmful if held across unreliable remote calls. Shorten critical sections and retain explicit authorization and state ownership rules.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.4e075e4ebc644f0e9b92c05294f62ca4:5 -->
## 5. A cancellation is a request, not a rollback

Timeouts, explicit client cancellation, interruption and server shutdown have different observability and cleanup semantics. The [gRPC cancellation guide](https://grpc.io/docs/guides/cancellation/) recommends stopping initiated work and propagating cancellation to dependent calls where practical. Neither gRPC cancellation nor Java interruption guarantees that previously committed database or external effects never occurred.

| Mechanism | Can help | Cannot guarantee |
|---|---|---|
| Parent deadline | Limits useful wait | No prior business commit |
| Executor shutdown | Stops accepting new tasks and tries cleanup | Arbitrary uncooperative tasks terminate immediately |
| Scoped child tasks | Explicit fork/join and lifetime | Durable message/effect exactly once |
| Bounded queue | Limits waiting objects | Fast external dependency |
| Semaphore | Limits one shared resource's concurrency | Correct state authority across processes |
| Virtual threads | Reduces many blocking task costs for eligible workloads | More CPU, datastore throughput or external quota |


### Worked original failure trace: cancelled parent, committed child

Consider a fictional reservation endpoint that starts two child operations: **A** commits a single-authority reservation, while **B** requests a noncritical notification. Assume the reservation has a stable logical operation key, a database uniqueness constraint and a five-second user deadline; these are *design assumptions*, not measured infrastructure. The parent deadline expires after A's commit but before its acknowledgement reaches the parent. B is still queued.

| Order | Actor's observable state | Durable state and required response |
|---|---|---|
| T0 | Parent validates and forks A/B with one deadline | No reservation yet; both tasks belong to one request lifetime |
| T1 | A obtains a bounded connection and commits R7 with key K42 | **R7 is authoritative** even if the caller never receives a success response |
| T2 | Parent deadline fires; parent requests cancellation of outstanding tasks | Stop waiting for B and release resources; **do not infer R7 was undone** |
| T3 | Client retries K42 after a transport timeout | Resolve K42 from durable authority; duplicate transport attempts must not make R8 |
| T4 | B's notification may or may not have been sent | Reconcile via durable publication/inbox semantics when notification delivery is required |

The safe normal path joins all *required* children before reporting success. The partial-failure path reports an **unknown outcome** if the response was lost, rather than treating interruption as an automatic business abort. On retry the state owner either returns R7 or exposes a bounded pending/reconciliation state. A cancellation-aware executor improves cleanup, not durability or exactly-once effects. The [deduplication owner](../../v04/c04/retries-idempotency-and-ambiguous-effects.md) defines logical-effect identity; the [outbox owner](../../v04/c05/outbox-inbox-sagas-and-durable-workflows.md) defines durable notification recovery. Their mechanisms should not be copied into this concurrency chapter.

**Alternative and reversal:** if B is essential to the invariant, the API may need a durable workflow and asynchronous response instead of parent-scoped fire-and-forget tasks. If the operation is pure computation, a scoped fork/join and cancellation policy may be sufficient. A proposed test would kill the parent between database commit and reply and verify one authoritative reservation, bounded threads/connections and a discoverable eventual result. **This test was not executed.**

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](task-lifetime.md) |
| Next | [Continue the reasoning](README.md) |
| Integrated question | [Original scenario and limits](threads-tasks-structured-coordination.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.
