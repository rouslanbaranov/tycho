---
metadata_version: 1
id: "tycho.page.15ffb7535c424b0eac6445cddaeb4a25"
kind: "page"
parent_id: "tycho.chapter.9d4f989ec9304e418f60f1ad7248094a"
canonical_path: "book/volumes/v01/c01/authority-dependencies.md"
title: "Authority and external dependencies"
topic_ids:
  - "application-architecture"
perspectives:
  - "architecture"
summary: "Who owns each state transition and what can an external dependency leave unknown?"
route_hints:
  questions:
    - "Who owns each state transition and what can an external dependency leave unknown?"
  prerequisites:
    - "tycho.page.de62a6f0e5a145aea3798ee69715f033"
  related_ids:
    - "tycho.chapter.9d4f989ec9304e418f60f1ad7248094a"
    - "tycho.page.4318e542ac7e445b9e8b3150effd2cff"
    - "tycho.page.b6be128c3e714ac68ef3311a30d65141"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "authority"
    - "dependencies"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Bounded question from tycho.page.4318e542ac7e445b9e8b3150effd2cff; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
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
# Authority and external dependencies

**Owning question:** Who owns each state transition and what can an external dependency leave unknown?

This page belongs to [V01/C01 — Problem framing and system boundaries](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.4318e542ac7e445b9e8b3150effd2cff:3 -->
## 3. Ownership boundaries are not deployment boundaries

A system context diagram says who interacts; it does not prove which processes, repositories, teams or servers implement the behavior. A process boundary is where an application can fail and deploy independently. A **state-authority boundary** is where a business invariant is finally enforced. An **authorization boundary** is where access to that effect must be validated. A **data-exchange boundary** is where a versioned contract must be preserved. These can coincide, but should be modeled separately.

For the fictional reservation system, splitting command ingestion from authoritative slot allocation may be sensible for isolation only if the acceptance contract, duplicate identity and state owner are well defined. Simply naming "Reservation Service" does not eliminate the need for a database consistency model. Conversely, retaining one deployable with strong internal module boundaries can satisfy the user-visible contract while avoiding needless distributed failure modes.

The [C4 software-system abstraction](https://c4model.com/abstractions/software-system) emphasizes value delivered to users, rather than equating a system with any particular individual deployable. Domain capabilities, modules, runtime units and software systems should not be treated as interchangeable names. For implementation choices, use [Application styles and ownership](../../../application/architecture-styles-and-module-boundaries.md), not the introductory context diagram alone.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.4318e542ac7e445b9e8b3150effd2cff:4 -->
## 4. Track neighbors with real failure and trust semantics

External systems are outside the team's direct control, even when owned by a friendly organization or accessed on the same private network. Every external edge needs a small contract:

- Purpose, actor and direction of the exchanged effect or data.
- Which side owns identity, authorization and authoritative state.
- Protocol/version/freshness expectations only when technical realization is selected.
- Unavailable/slow/error/timeout behavior, including ambiguous acknowledgment.
- Operational owner, escalation path and version/deprecation window.
- Security/privacy classification and explicitly allowed data exchange.
- Required observability and evidence scope (documented, observed, assumed).

**Failure scenario (fully synthetic):** the external notification provider times out after reservation commit. A flawed design rolls back or retries the whole reservation to "make sure the email went out." The design then violates the intended independence of the authoritative allocation decision and communication delivery. Instead, define a durable record of the accepted allocation; separately track a bounded notification outcome and its retry policy. This is a conditional architectural recommendation under the fictional contract, not a measured incident.

**Counterexample:** if the actual product requirement is "an external licensing authority must approve a reservation before it is accepted," that authority is on the mandatory business critical path. The safe design cannot simply mark licensing "optional" to remove latency. Under unknown authority/availability guarantees, the honest outcome is insufficient evidence and a stakeholder/contract decision.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](outcomes-context.md) |
| Next | [Continue the reasoning](evidence-contract.md) |
| Integrated question | [Original scenario and limits](problem-framing-and-system-boundaries.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.
