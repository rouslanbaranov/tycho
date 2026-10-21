---
metadata_version: 1
id: "tycho.page.3c78e2b17ac74973b2ae658977843c2a"
kind: "page"
parent_id: "tycho.chapter.4a3cbf0617e44be5b1e8d72568109dad"
canonical_path: "book/volumes/v04-distributed-coordination-and-events/c03-consistency-and-distributed-transactions/transaction-isolation-and-sagas.md"
title: "Consistency, transaction isolation and sagas across service boundaries"
topic_ids:
  - "distributed-systems"
perspectives:
  - "architecture"
summary: "Integrated question, original scenario and transfer limits for Consistency and distributed transactions. Detailed mechanisms have separate question owners."
route_hints:
  questions:
    - "Which invariants need coordination, isolation or reconciliation?"
  prerequisites: []
  related_ids:
    - "tycho.page.ace968ab1de8409383c6a9b22a00d006"
    - "tycho.page.5da19d9b920940fb837bbb28e8fefe77"
    - "tycho.page.e4a2ae7fb1d74eadbdc6d8eb07db46ec"
    - "tycho.page.db64c44e7af846f9b54a524a37a1b9dd"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Consistency"
    - "transaction"
    - "isolation"
    - "and"
    - "sagas"
    - "across"
    - "service"
    - "boundaries"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Only exact URL matches to the global source register are normalized here. Page-local case and evidence ledger IDs remain in the body; no claim-level mapping or source inspection is inferred."
content_review:
  status: "draft"
  reviewed_at: null
  reviewer: null
  proof_uri: null
authored_at: "2026-10-18"
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---
<!-- tycho-question-source:tycho.page.3c78e2b17ac74973b2ae658977843c2a:-1 -->

# Consistency, transaction isolation and sagas across service boundaries

> Tycho Issue [#80](https://github.com/rouslanbaranov/tycho/issues/80), proposed V04/C03/C05. Research: 2026-10-18. Public-source-grounded explanation and entirely fictional registration workflow. **Not** a tested transaction framework or guarantee of exactly-once operation.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.3c78e2b17ac74973b2ae658977843c2a:0 -->
## Purpose and mission

Business invariants survive only when the enforcing mechanism covers **every concurrent operation that can violate them**. A local transaction, serializable isolation, an event publication and a compensating action solve different problems. This page describes their boundaries before recommending any distributed transaction strategy.

**Primary question:** Which consistency requirements can be enforced within one authoritative local transaction, and what changes when a business operation must coordinate multiple separately committed owners?

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.3c78e2b17ac74973b2ae658977843c2a:7 -->
## Engineering walkthrough — The cancel-versus-accept invariant crosses a transaction boundary

**Original fictional reservation:** Booking accepts one seat and Payment authorizes a deposit in separate databases. Cancellation can race with payment confirmation. Two transactions may each be locally ACID yet produce a globally invalid result: booking CANCELLED while the external payment is captured as if the booking remained ACTIVE.

A local PostgreSQL serializable transaction can protect a booking-state transition inside one data authority, subject to retries. It cannot atomically roll back a committed capture in an unrelated payment provider. A saga must define valid durable states and compensating actions, including cases where payment capture cannot be reversed instantaneously.

| Event race | Business protocol response | Incorrect shortcut |
|---|---|---|
| Cancel before payment authorized | Mark cancellation intent; prevent new capture through fenced operation/state | Assume last message received always wins |
| Payment captured, cancel then arrives | Transition to refund-pending and reconcile actual refund effect | Rewrite captured to never-happened |
| Deposit reply lost | Query provider by stable payment intent | Blindly capture a second payment |
| Compensation fails | Durable retry/manual repair state with accountable owner | Declare saga complete while money remains captured |

**Choice:** if all required state can remain in one local database, prefer its transaction/invariant over a saga for that operation; when independent business authorities are non-negotiable, accept explicit intermediate states and compensation contracts. A message order alone cannot substitute for versioned business transitions. The saga pattern and PostgreSQL isolation documents support bounded mechanisms, not guaranteed reversibility.

**Proposed, not executed:** synchronize cancel and accept operations, lose payment acknowledgments, crash during compensation and replay messages out of order. The test oracle is one legal booking outcome plus independently reconciled payment status, not a globally atomic transaction claim.

<!-- /tycho-question-source -->

## Integrated decision and reading route

Place invariants at their enforcing transaction boundary and state how cross-boundary uncertainty is reconciled.

A compensating action can fail or arrive late; a saga is not an atomic transaction across independent owners.

The detailed pages separate the mechanisms that make this decision conditional:

- [Invariants and local transaction isolation](invariants-isolation.md) — Which state owner and anomaly define the required coordination boundary?
- [Distributed transactions and business protocols](distributed-protocols.md) — Which obligations remain when local transactions cannot atomically coordinate owners?
- [Concurrency, compensation and negative experiments](coordination-failure.md) — What schedule would expose an unsafe cross-owner invariant or failed compensation?

[Chapter introduction, ordered pages and full source ledger](README.md). Original source labels retain their historical scope; this editorial decomposition does not turn proposed experiments into executed evidence.
