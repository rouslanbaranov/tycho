---
metadata_version: 1
id: "tycho.page.65f9616c034643f9bf5f297037f027e4"
kind: "page"
parent_id: "tycho.chapter.c5f8456752f34dd6a5b6b5c7e3e14715"
canonical_path: "book/volumes/v02-application-boundaries-and-contracts/c01-layered-modular-and-ports-and-adapters-design/adapter-scenarios.md"
title: "Adapter substitution and falsification"
topic_ids:
  - "application-architecture"
perspectives:
  - "architecture"
summary: "How do local and remote adapter replacements change the tests and operational obligations?"
route_hints:
  questions:
    - "How do local and remote adapter replacements change the tests and operational obligations?"
  prerequisites:
    - "tycho.page.f375bfcea48045d2a5d1f46014ca7758"
  related_ids:
    - "tycho.chapter.c5f8456752f34dd6a5b6b5c7e3e14715"
    - "tycho.page.77b512c4e2e946bd92d70b4a714600c8"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "adapter"
    - "scenarios"
evidence_scope:
  source_ids:
    - "src.hexagonal"
  claim_ids: []
  status: "source-linked"
  notes: "Bounded question from tycho.page.77b512c4e2e946bd92d70b4a714600c8; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
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
# Adapter substitution and falsification

**Owning question:** How do local and remote adapter replacements change the tests and operational obligations?

This page belongs to [V02/C01 — Layered, modular and ports-and-adapters design](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.77b512c4e2e946bd92d70b4a714600c8:3 -->
## 3. Original fictional example: a shared workshop equipment scheduler

An independently invented tool-booking application supports **ReserveUnit**, **CancelReservation**, and **ListPublicEquipment**. Its reservation rule is that a physical unit cannot have overlapping *accepted* allocations in the same time interval. External HTTP and CLI clients should invoke the same authoritative use-case rule.

A poor implementation tests the rule only in an HTTP controller and allows a batch importer to write reservations directly. The code appears layered, yet bypasses the invariant. Better design defines a use-case contract that both adapters must call. This contract identifies caller authorization, logical operation identity, transactional authority and possible errors such as already-reserved or outcome-unknown.

**Important limit:** replacing the SQL adapter with an in-memory object in a unit test cannot prove database locking, transaction isolation or cross-replica behavior. Separate integration tests against the actual data backend and concurrent callers are mandatory if the service promises exclusivity.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.77b512c4e2e946bd92d70b4a714600c8:5 -->
## 5. Scope dependency direction across build, tests and runtime

Ask three distinct questions:
1. **Source dependency:** does a business module import a concrete driver or HTTP framework? A static dependency check can verify much of this policy.
2. **Runtime dependency:** does invoking the use case block on a datastore even if the type dependency is inverted? Hexagonal code still depends on the *availability* of the external capability.
3. **Organizational change dependency:** must two teams coordinate contracts, migrations and deployments? Compile-time inversion alone does not solve ownership or release coupling.

A port can reduce compile-time coupling while introducing indirection and more integration tests. If there is only one stable adapter, interfaces everywhere may add ceremony rather than useful replaceability. A useful port expresses a real boundary whose isolation or substitution matters to business rules or testing.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.77b512c4e2e946bd92d70b4a714600c8:6 -->
## 6. Failure and test matrix

| Scenario | Required evidence | Frequent invalid conclusion |
|---|---|---|
| HTTP controller replaced by CLI | Same use-case outcome and authorization policy | UI independence means database independence |
| Real DB loses connectivity | Defined error/degraded read state, no invented success | Mocked repository test proves recovery |
| Two concurrent same-unit bookings | At most one accepted authoritative reservation | A pure overlap predicate guarantees transaction correctness |
| Client response lost after commit | Stable operation identity and read-back/reconciliation | Timeout guarantees no side effect occurred |
| Import job bypasses public use-case port | Dependency or integration test rejects bypass | Class/package names alone enforce invariants |
| Repository implementation changed | Contract + transactional/failure behavior checked | All adapters have identical durability by interface alone |
| Driver has a new latency profile | End-to-end capacity and deadline test | Compiler dependency inversion removes runtime network cost |

These are **proposed tests**, not measurements. A genuine architecture acceptance must include negative authorization and state-recovery tests.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.77b512c4e2e946bd92d70b4a714600c8:7 -->
## 7. When not to impose this structure

A tiny fixed-format batch transformation with no alternate drivers and little independent business logic may not need elaborate adapter abstractions. Conversely, code that must support several frontends, isolated rule testing, storage substitutions or staged modernization may benefit strongly from clear ports. Neither observation mandates microservices.

A **modular monolith with well-defined ports** can be a finished target. Splitting each port into a remote service would add network timeout, retry, versioning and operational boundaries that this internal design does not require.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](dependencies-ports.md) |
| Next | [Continue the reasoning](README.md) |
| Integrated question | [Original scenario and limits](layered-hexagonal-ports-and-adapters.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.
