---
metadata_version: 1
id: "tycho.page.7079edf1ceeb4b1594083edf7a2c680e"
kind: "page"
parent_id: "tycho.chapter.809c2f1d12e544b38af2460b80d6d24e"
canonical_path: "book/volumes/v10-decision-support-and-modernization/c04-alternatives-experiments-and-adrs/decision-discriminators.md"
title: "Alternatives and discriminating hypotheses"
topic_ids:
  - "architecture-decisions"
perspectives:
  - "architecture"
  - "migration"
summary: "Which observation would make one feasible option preferable to another?"
route_hints:
  questions:
    - "Which observation would make one feasible option preferable to another?"
  prerequisites:
    - "tycho.page.f05854fcc406435bbf38a192bc7ab2f1"
  related_ids:
    - "tycho.chapter.809c2f1d12e544b38af2460b80d6d24e"
    - "tycho.page.f05854fcc406435bbf38a192bc7ab2f1"
    - "tycho.page.a5285941dcba43d5a6a7c091cb4c99f9"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "decision"
    - "discriminators"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Bounded question from tycho.page.f05854fcc406435bbf38a192bc7ab2f1; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
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
# Alternatives and discriminating hypotheses

**Owning question:** Which observation would make one feasible option preferable to another?

This page belongs to [V10/C04 — Alternatives, experiments and ADRs](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.f05854fcc406435bbf38a192bc7ab2f1:1 -->
## 1. A precise problem statement comes before alternatives

An original fictional equipment-booking site experiences slow responses during a short opening window. A stakeholder proposes splitting its one deployed application into reservation and catalogue microservices.

Known in the invented prompt: reservations must be exclusive, and responses are slow during bursts. Unknown: offered versus completed arrivals, key skew, connection waits, database locking, client deadline, runtime CPU usage, and the real benefit expected from separate releases.

A valid *question* is therefore not "How do we adopt microservices?" but "Which bounded architectural change most reliably preserves exclusive reservations while meeting an agreed user-visible deadline during the specified arrival and contention pattern?"

A decision frame has four types of information:

| Type | Synthetic example | Evidence status |
|---|---|---|
| Correctness invariant | At most one accepted booking per physical unit/time window | Proposed non-negotiable requirement |
| Quality scenario | Final result within a named deadline under a specified burst | Incomplete until workload and denominator are defined |
| Constraint | Existing clients must remain supported through transition | Hypothetical hard compatibility gate |
| Preference | Lower on-call complexity, cheaper operation, independent component changes | Competing objectives; cannot override hard gates |

When a hard requirement is unknown, *measure first* is a legitimate decision. Do not pretend an unspecified SLO or operational budget passed.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.f05854fcc406435bbf38a192bc7ab2f1:2 -->
## 2. Enumerate a genuine retained/simple option

Three viable candidates for evaluation—not selection—are:

- **A — retain and instrument the modular deployable.** Measure lock/pool/CPU/arrival conditions and repair a proven bottleneck without introducing a new remote owner.
- **B — keep one state authority, add bounded admission or a durable accepted/pending workflow.** Useful only if the user can receive a pending outcome or explicit rejection under the signed contract.
- **C — extract reservation into a separately deployed service.** Potentially worthwhile if independently managed capabilities, release cadence or isolated capacity are real requirements and transactional authority can move safely.

The hard-gate matrix must be completed before weighted preference scoring:

| Gate | A | B | C |
|---|---|---|---|
| No duplicate exclusive allocations | Must test current transaction | Must test queue + authority | Must prove remote authority transfer |
| Mandatory final-result semantics | Might preserve | Async/pending may **fail** current contract | Might preserve, but adds network failure |
| Old/new client coexistence | Small interface surface | Pending/error contract change | Mixed-version routing and data ownership |
| Bounded loss and recovery | Requires restore evidence | Queue replay and status reconciliation | Fencing/cutover and restore proof |
| Operational/cost limit | Existing footprint not yet measured | Extra queue/runbook | Extra deployment/on-call surfaces |

**Fail** means exclude unless requirements legitimately change; **unknown** means withhold unconditional acceptance. The table deliberately leaves actual outcomes unproven. A low cost score cannot rescue an option that fails booking exclusivity.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.f05854fcc406435bbf38a192bc7ab2f1:3 -->
## 3. Hypothesis → discriminator → possible reversal

For each candidate, specify a causal benefit that another source of evidence could disprove.

| Hypothesis | Proposed discriminating experiment | Falsifying observation |
|---|---|---|
| A: requests wait mainly for one DB lock | Correlate per-key contention, transaction time and parent spans under a replayed skewed burst | Most critical-path wait is elsewhere, and optimizing the lock does not improve outcomes |
| B: admission protects accepted correct work under overload | Hold offered demand fixed; compare queue age, rejects, success, retries, fairness and deadlines | Apparent p99 gain is only from hiding or dropping required work |
| C: independent deployments materially reduce change risk | Rehearse N/N+1 clients, read/write ownership and rollback of bounded capability changes | A common store/writer still forces coordinated releases or cutover violates an invariant |

One experiment should vary one decision-relevant mechanism at a time where possible. Equivalent test inputs include **offered logical operations**, not merely completed requests. A result at different data cardinality or resource budgets may not distinguish architecture from an accidental test setup. [Benchmark validity](../../v07-performance-scale-and-resilience/c03-load-test-methods-and-benchmark-validity/load-testing-and-benchmark-validity.md) owns arrival-generator and denominator mechanics.

A negative result is evidence, not a failed research task. Retain the baseline when it satisfies hard constraints and new complexity has no demonstrated incremental benefit.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](architecture-alternatives-experiments-and-adrs.md) |
| Next | [Continue the reasoning](adr-sensitivity.md) |
| Integrated question | [Original scenario and limits](architecture-alternatives-experiments-and-adrs.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.
