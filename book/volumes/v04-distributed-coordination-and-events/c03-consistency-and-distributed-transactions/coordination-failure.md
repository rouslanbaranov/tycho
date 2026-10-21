---
metadata_version: 1
id: "tycho.page.db64c44e7af846f9b54a524a37a1b9dd"
kind: "page"
parent_id: "tycho.chapter.4a3cbf0617e44be5b1e8d72568109dad"
canonical_path: "book/volumes/v04-distributed-coordination-and-events/c03-consistency-and-distributed-transactions/coordination-failure.md"
title: "Concurrency, compensation and negative experiments"
topic_ids:
  - "distributed-systems"
perspectives:
  - "architecture"
summary: "What schedule would expose an unsafe cross-owner invariant or failed compensation?"
route_hints:
  questions:
    - "What schedule would expose an unsafe cross-owner invariant or failed compensation?"
  prerequisites:
    - "tycho.page.e4a2ae7fb1d74eadbdc6d8eb07db46ec"
  related_ids:
    - "tycho.chapter.4a3cbf0617e44be5b1e8d72568109dad"
    - "tycho.page.3c78e2b17ac74973b2ae658977843c2a"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "coordination"
    - "failure"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Bounded question from tycho.page.3c78e2b17ac74973b2ae658977843c2a; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
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
# Concurrency, compensation and negative experiments

**Owning question:** What schedule would expose an unsafe cross-owner invariant or failed compensation?

This page belongs to [V04/C03 — Consistency and distributed transactions](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.3c78e2b17ac74973b2ae658977843c2a:5 -->
## 5. Failure matrix and an experiment contract

| Failure injected | Expected question | Required validation |
|---|---|---|
| Crash before local commit | Can either source record partially persist? | Atomic source transaction and rollback test |
| Crash after commit but before reply | Can retry recover the same outcome? | Client key + stored result; concurrent duplicate attempts |
| Remote service times out | Is its effect committed, rejected or unknown? | Query/reconciliation contract; no blind secondary effect |
| Compensation action fails | Does the process preserve pending repair state? | Durable workflow state, eventual retry, alarm and deadline |
| Two sagas race for same resource | Can both violate global capacity? | Isolation/invariant protocol with adversarial overlap tests |
| Broker delivers twice | Does consumer apply a second logical effect? | Stable event identity, consumer atomic dedup and retention |
| Domain rule changes during rollout | Can old and new steps interpret pending states? | Versioned workflow, old/new compatibility and forward repair |

**SLOs cannot substitute for invariants.** A 99.9% workflow-success objective permits bad events under its definition; it is not proof that acknowledged money or bookings are never double-applied.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.3c78e2b17ac74973b2ae658977843c2a:6 -->
## 6. Alternatives, boundaries and unanswered questions

Prefer one authoritative **local** transaction when the high-value invariant fits one owner and operating limits are acceptable. Introduce a saga when a business process must span multiple independent owners, the participating steps can be modeled and recovered, and the team can support reconciliation and failure handling. Consider synchronous composition when no durable state transition is required; choose orchestration only after observing that workflow complexity warrants it.

Insufficient-evidence question: "Three independent services all use PostgreSQL SERIALIZABLE. Are our cross-service registrations globally serializable?" **No.** Local isolation is not a global cross-database protocol. Need a single authoritative allocation model, participating transaction mechanism or application-level invariant protocol, retry/compensation policy and actual overlapping-failure tests.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](distributed-protocols.md) |
| Next | [Continue the reasoning](README.md) |
| Integrated question | [Original scenario and limits](transaction-isolation-and-sagas.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.
