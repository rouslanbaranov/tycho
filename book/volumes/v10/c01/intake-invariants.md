---
metadata_version: 1
id: "tycho.page.84fa4a7505904bb2a492be1593690ed2"
kind: "page"
parent_id: "tycho.chapter.289750444f8040d292a474e3876046a1"
canonical_path: "book/volumes/v10/c01/intake-invariants.md"
title: "Outcomes, constraints and workload intake"
topic_ids:
  - "architecture-decisions"
perspectives:
  - "architecture"
  - "migration"
summary: "Which inputs must be explicit before candidate architectures are compared?"
route_hints:
  questions:
    - "Which inputs must be explicit before candidate architectures are compared?"
  prerequisites:
    - "tycho.page.868027aee4884210bea1d8a6542fbfb0"
  related_ids:
    - "tycho.chapter.289750444f8040d292a474e3876046a1"
    - "tycho.page.868027aee4884210bea1d8a6542fbfb0"
    - "tycho.page.4e96abb6d4504ef1b09cbc355485108a"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "intake"
    - "invariants"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Bounded question from tycho.page.868027aee4884210bea1d8a6542fbfb0; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
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
# Outcomes, constraints and workload intake

**Owning question:** Which inputs must be explicit before candidate architectures are compared?

This page belongs to [V10/C01 — Architecture requirement and workload profiles](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.868027aee4884210bea1d8a6542fbfb0:1 -->
## 1. Begin with a user outcome and a system boundary

**Original fictional case:** people reserve shared workshop equipment through a web application. A successful action allocates one available timeslot exactly once and provides a durable booking ID. Two users may contend for the same slot, and external clients may retry a booking after losing a response.

A useful business boundary includes the actor, requested outcome, external systems, irreversible changes and failure ownership. It should not be defined as "the Java backend" before we know who owns allocation state and whether an external payment or calendar write is mandatory. If relevant interfaces are outside the evaluated boundary, their failure assumptions must still be recorded.

```mermaid
flowchart LR
    C["Person / booking client"] --> A["Booking contract boundary"]
    A --> S["Authoritative slot allocation"]
    A --> N["Optional notification dependency"]
    S --> R["Durable booking result"]
    N -.-> R
```

**Diagram explanation:** The slot allocation and durable booking ID are required for correctness. Notification is optional under this *invented* contract and may complete later. A notification failure must not turn a successfully committed booking into a new booking attempt. The diagram does not prescribe monolithic or distributed deployment; both could implement it with different cost and failure risk.

Define what is **in scope** (booking acceptance, allocation consistency, outcomes, rejection) and **out of scope** (equipment inventory procurement, unrelated reporting). Write separate ingress/egress and state-authority boundaries, not only a list of code packages.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.868027aee4884210bea1d8a6542fbfb0:2 -->
## 2. Four kinds of requirement must stay distinct

| Statement kind | Fictional example | Treatment during selection |
|---|---|---|
| Business outcome | An accepted reservation has a durable identifier | Evaluate the observable journey and its final state |
| Hard invariant | A slot must not have two simultaneously valid owners | Reject any design that cannot enforce it; measure correctness under contention |
| Measurable quality target | For a defined 10-minute peak, 99% of eligible completed booking attempts receive a final result within 700 ms | Requires a precise clock, population, failure treatment and verification method |
| Preference / cost envelope | Prefer small on-call burden and predictable monthly cost | Compare only candidates that first pass non-negotiable gates |

A hard invariant is not the same as an availability SLO: a 99.9% success objective does **not** permit 0.1% duplicate bookings. Nor may an architecture score trade away an authorization failure or data-loss constraint to gain p95 latency. Unknown hard-gate evidence remains a blocker to unconditional approval; it is not equivalent to passing the gate.

The example 700 ms and 99% are **invented targets**, not an engineering recommendation. Before using them, define whose clock starts the attempt, whether the 99% population includes rejected, timed-out or retried requests, how errors contribute to success, and what workload mix and geographical environment are represented.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.868027aee4884210bea1d8a6542fbfb0:3 -->
## 3. Workload is a vector, not a user count

An initial workload description records:

| Dimension | Questions a meaningful profile answers |
|---|---|
| Offered arrival rate | How many attempts per time unit reach the boundary, including failed and retried demand? |
| Admitted and completed rate | How much work is accepted, completed, rejected, queued and timed out in the same window? |
| Request mix | What proportion is read, booking write, cancellation, bulk synchronization, search or administrative change? |
| Concurrent work | How many requests are resident, waiting for resources, awaiting I/O or in durable background processing? |
| State size and skew | How much storage and how many active keys; do a few slots attract most concurrent writes? |
| Temporal shape | Is the peak 3 seconds, 10 minutes or 4 hours; what is normal and seasonal behavior? |
| Dependency limits | What external quotas, DB pool sizes, lock durations, connection budgets and network deadlines apply? |
| Growth and degradation | What happens under doubled offered load, partial loss or failed downstream dependencies? |
| Cost/team horizon | Staffing, recovery skill, operating envelopes and cost constraints across environments |

These values cannot be inferred from "daily active users" alone. Distinguish a *request arrival* from a *concurrent session*, and a client retry from a new business operation. Queueing identities such as L = λW constrain long-run mean resident work under a stable compatible boundary; they do not convert active accounts into requests per second. Read [queueing and measurement boundaries](../../v07/c01/queueing-littles-law.md).

### Synthetic contrast: same daily users, different architecture pressure

Two **fictional** products each have 10,000 registered users.

- **Scenario A:** most use the system at separate times to read static workshop schedules. A small number write bookings; dominant costs are cache freshness, search usability and delivery of public content.
- **Scenario B:** a short opening window drives 2,000 booking attempts in 20 seconds, many against the same few workshop slots, while clients retry uncertain outcomes. The peak offered rate in the invented scenario is 100 attempts/second; **it does not imply** 100 successful transactions/second or independent slot keys.

One user-count metric cannot distinguish A from B. Even in B, adding service replicas does not remove serialization at a single authoritative slot. Before considering scale-out, measure key skew, duplicate effects, contention duration and the success definition under burst.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](requirements-and-workload-architecture-profiles.md) |
| Next | [Continue the reasoning](evidence-screening.md) |
| Integrated question | [Original scenario and limits](requirements-and-workload-architecture-profiles.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.
