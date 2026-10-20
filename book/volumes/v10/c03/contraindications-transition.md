---
metadata_version: 1
id: "tycho.page.2debc63415184b02ad0a144b2649c171"
kind: "page"
parent_id: "tycho.chapter.b20625a099bc4c82b7d547c32c7da28a"
canonical_path: "book/volumes/v10/c03/contraindications-transition.md"
title: "Contraindications and transition falsification"
topic_ids:
  - "architecture-decisions"
perspectives:
  - "architecture"
  - "migration"
summary: "Which counterexample or migration cost should reverse the pattern choice?"
route_hints:
  questions:
    - "Which counterexample or migration cost should reverse the pattern choice?"
  prerequisites:
    - "tycho.page.2176fe3dcdf24a199d1656cba602e8e1"
  related_ids:
    - "tycho.chapter.b20625a099bc4c82b7d547c32c7da28a"
    - "tycho.page.35d5be6a4e074758afff95bf3ec68bc5"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "contraindications"
    - "transition"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Bounded question from tycho.page.35d5be6a4e074758afff95bf3ec68bc5; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
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
# Contraindications and transition falsification

**Owning question:** Which counterexample or migration cost should reverse the pattern choice?

This page belongs to [V10/C03 — Pattern applicability and contraindications](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.35d5be6a4e074758afff95bf3ec68bc5:5 -->
## 5. Contraindications are not generic anti-pattern labels

A pattern can be a poor fit **here and now** without being inherently bad. For example, event-driven processing may be appropriate for an asynchronous catalog index even if it is inappropriate for a synchronous safety-critical allocation decision. The difference is not the popularity of event sourcing but **authority and required consistency**.

Record one of these explicit decision states:

- **Applicable:** required preconditions are supported and no hard-gate violation is established; still requires implementation tests.
- **Conditionally applicable:** plausible under stated but unverified assumptions; proposed experiment/guarded transition required.
- **Contraindicated:** an observed non-negotiable requirement is demonstrably violated by the proposed design as specified.
- **Not required:** baseline meets known outcomes and no incremental benefit justifies new complexity.
- **Insufficient evidence:** important owner, workload, dependency or recovery facts are missing.
- **Historical/obsolete candidate:** supported only for a dated runtime/migration snapshot, not current guidance without re-verification.

**Crucial:** a missing measurement is not evidence that an option can never work. In a decision tool, "unknown" must not silently become "pass" or "fail"; it triggers source or experiment work.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.35d5be6a4e074758afff95bf3ec68bc5:6 -->
## 6. Original synthetic decision: bursty reservations

A fictional resource reservation application guarantees that each timeslot is committed to at most one eligible requester. An input says "busy mornings," but gives no observed contention, latency, arrival or retry distribution. The team proposes "Kafka + sharded microservices + distributed cache."

**Test hard gates first:**
1. No double allocation under simultaneous attempts and ambiguous responses.
2. Correct authorization to reserve or cancel a named slot.
3. A visible final-result or accepted/pending contract for the user.
4. Stable operation identity across retries and no untracked divergent writers.

**Compare realistic candidates:**

| Option | Why it might help | What must first be true |
|---|---|---|
| Keep local authority, instrument/tune | Preserves simple invariant and measures actual bottleneck | Existing transaction semantics verified, observed demand profile available |
| Bounded admission + async result | Protects backend when deferred completion is allowed | Business/client can accept pending status and durable tracking |
| Separate service with owned store | Useful for measured independent deployment/capacity boundaries | One-writer migration, safe cross-version clients, recoverable cutover |
| Shard slot authority | Could distribute *independent* slot keys | Hot-key distribution and migration ownership validated |
| Cache available slots | Speeds eligible reads when staleness understood | Final allocation always revalidated at authority |
| Reactive/virtual execution | Reduces waiting overhead under I/O-heavy admission | Downstream actually has capacity and cancellation semantics are correct |

The composite proposal is **not yet warranted**. It adds multiple state, network and operational boundaries while leaving a single-slot invariant unresolved. Adopt **MEASURE_FIRST** for queue, contention and user-visible outcomes, then test one reversible change at a time.

### Reversing the initial decision

If a consistent multi-day measurement demonstrates isolated per-key transactions, distinct independent capability owners and safe asynchronous customer semantics, an extracted/sharded service or durable work queue may be conditionally viable. If the bottleneck is a single hot timeslot, more partitions or threads do not alter the invariant that only one requester can win. If clients strictly require final outcomes synchronously, a queue-based acceptance change is a contract change, not a transparent optimization.

This invented example is **not** evidence that a particular implementation meets the given numbers; no load test or service exists.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.35d5be6a4e074758afff95bf3ec68bc5:7 -->
## 7. A complete pattern decision includes transition risk and falsification

An architecture decision record should include:
- concrete user outcome and failure class, units/time window and budget;
- current evidence versus assumptions, including source revisions and confidence;
- options with current/retained design, hard-constraint screening and cost;
- why selected and rejected patterns fit or fail **this** context;
- a minimal discriminating experiment with correctness and operational acceptance;
- target **and transitional** data/client boundaries;
- irreversible steps, rollback/forward repair and explicit stop gates;
- conditions and owner for re-evaluation.

Cross-domain examples belong in the separate [decision synthesis](../c07/cross-domain-modernization-and-adr-examples.md). General option scoring and ADR formatting remain in the supporting [candidate comparison model](../../../../authoring/models/candidate-comparison-adr.md). Do not copy canonical technical explanations into every pattern card; link them.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](pattern-cards.md) |
| Next | [Continue the reasoning](README.md) |
| Integrated question | [Original scenario and limits](pattern-applicability-and-contraindications.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.
