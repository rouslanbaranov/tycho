---
metadata_version: 1
id: "tycho.page.aaed70abf79447c89a544eaf84f0da96"
kind: "page"
parent_id: "tycho.chapter.5fb14670d0b24967a5e6c24df7221d74"
canonical_path: "book/volumes/v10-decision-support-and-modernization/c07-cross-domain-worked-comparisons-and-unresolved-cases/worked-adr.md"
title: "Worked ADR and unresolved conclusions"
topic_ids:
  - "architecture-decisions"
perspectives:
  - "architecture"
  - "migration"
summary: "How is a complete recommendation kept falsifiable and source-scoped?"
route_hints:
  questions:
    - "How is a complete recommendation kept falsifiable and source-scoped?"
  prerequisites:
    - "tycho.page.22b12598c23b4fc5ac74b1adc960ebe5"
  related_ids:
    - "tycho.chapter.5fb14670d0b24967a5e6c24df7221d74"
    - "tycho.page.0ce5d0aaf63f425ebf556ea97e2d24a9"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "worked"
    - "adr"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Bounded question from tycho.page.0ce5d0aaf63f425ebf556ea97e2d24a9; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
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
# Worked ADR and unresolved conclusions

**Owning question:** How is a complete recommendation kept falsifiable and source-scoped?

This page belongs to [V10/C07 — Cross-domain worked comparisons and unresolved cases](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.0ce5d0aaf63f425ebf556ea97e2d24a9:7 -->
## 7. Reproducible decision record (original synthetic ADR)

**ADR-SYN-04: retain the single registration state owner while instrumenting burst behavior.**

- **Status:** PROPOSED, no real stakeholder acceptance.
- **Context:** hypothetical temporary surge; success invariant and client feedback timing matter; actual bottleneck unmeasured.
- **Hard constraints:** no double-confirmed seat, bounded user deadline, one authoritative state writer; old API compatibility through any trial.
- **Alternatives:** A retain+instrument; B admission/queue; C service extraction with independent store.
- **Decision:** select **measure first**; provisionally retain A. Consider B only if admission semantics fit and a controlled experiment demonstrates service protection. Do not choose C without a proven separation benefit and migration plan.
- **Evidence:** source-linked queueing, pooling and transaction chapters; **no production data**.
- **Falsification:** measured offered arrivals, bottleneck, logical duplicates, p99 and retry amplification show existing design cannot meet defined constraints after smaller safe changes.
- **Transition:** no irreversible change authorized; instrument and run bounded experiments; record rollback for any admission policy.
- **Review trigger:** workload shift, new hard isolation requirement, repeated exhausted resource boundary or failed controlled capacity experiment.

The [arc42 architecture decisions guidance](https://docs.arc42.org/section-9/) explains why important decisions should record alternatives and rationale; this original ADR is **not** an implementation of an accepted organization-specific governance process.


### Complete synthetic ADR: improve a legacy reservation service without a forced decomposition

**Original fictional baseline (not a real benchmark):** one Java modular application and one PostgreSQL authority manage 12,000 accounts. A timed event presents a proposed 120 new intents/s during 15 seconds; no verified ingress trace exists. SLO requirement: correct exclusive booking decisions with a bounded user-visible deadline. Constraints: the current public contract must remain supported, no simultaneous independent booking writers, limited on-call capacity, and a reversible first rollout. No real organizational approval or cost quotes exist.

| Candidate | Hypothesis | Hard gate | Observation that reverses preference |
|---|---|---|---|
| A — Retain modular architecture, improve SQL/admission | Database and queue behavior may be optimized without remote calls | One authoritative booking transaction; old clients supported | Controlled load still misses accepted completion requirement after safe changes |
| B — Durable admission queue for booking commands | Queue protects one hot authority during burst | Product permits pending/async responses; durable operation ID and backlog visibility | Clients require immediate final confirmation or backlog recovery breaches deadline |
| C — Extract booking service with independent datastore | Boundary-specific scaling and team autonomy repay distribution cost | Verified migration of state authority, fencing, mixed-client compatibility and on-call ownership | No independently measured boundary gain, or invariant fails in coexistence |

**Decision:** `MEASURE_FIRST`, provisionally A; this is not approval to deploy. Collect offered-versus-delivered load, correct completions, DB pool waits, per-key contention, retries, p99 and an explicit source snapshot. If A fails a fair test and product semantics accept pending work, evaluate B next. Candidate C requires a separate source-of-truth migration and a demonstrated operating benefit, not simply a higher peak RPS estimate.

| Transition state | What is deployed and authoritative | Gate and recovery |
|---|---|---|
| T0 baseline | Existing Java service and PostgreSQL writer | Capture trace/model, pinned code and restorable data |
| T1 observe and bound | Instrumentation and bounded admission, **same database writer** | Revert configuration if admission harms correct outcomes; no domain-data move |
| T2 pilot alternate | Canary queue/adapter for a permitted cohort, old API semantics preserved | Reconcile accepted command IDs; hold promotion on unknown/duplicate effects |
| T3 optional authority transition | Only after evidence favors C: compatible old/new clients, a *fenced* single writer | Prove identity mapping, replay and failback; never let two owners independently confirm |
| T4 stabilize / retire | Remove legacy path only after replay horizon and restore proof | Document irreversible state and forward-repair route; old binary rollback may be unsafe |

**Failure test:** commit a booking before losing the response, then retry while the canary is switching. Correctness is *one logical booking and a discoverable outcome*, not "one HTTP request." An interrupted migration must preserve one accepted authority and known restoration options. If real requirements, acceptable queue semantics or authoritative failure telemetry remain unknown, the final recommendation stays **INSUFFICIENT_EVIDENCE**.

**Transfer evidence limits:** the [Shopify modular-monolith case](../../../cases/shopify-modular-monolith.md) supports conditional modularity, [Uber DOMA](../../../cases/uber-doma-domains.md) illustrates governing distributed domain dependencies, and [Stripe's online migration](../../../cases/stripe-online-subscriptions-migration.md) illustrates staged change of data ownership. None establishes that this invented application should adopt its historical architecture. The numbers, options, states and acceptance tests above are invented; **no modernization, rollback or benchmark was performed**.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.0ce5d0aaf63f425ebf556ea97e2d24a9:8 -->
## 8. Verification and question-answering contract

A complete answer for an engineering choice should include:
- user outcome and exact system/source boundaries,
- workload, error/failure class and old data/API constraints,
- assumptions separated from inspected source claims and measured values,
- at least the retained/simple option and realistic alternatives,
- disqualifiers, operational/security costs and irreversible transition risks,
- a falsifiable measurement, test or source request for unknowns,
- decision status, accountable review and a revisiting condition.

When the question lacks a workload profile, ownership model or mandatory permission constraints, the valid answer may be **MEASURE_FIRST** or **INSUFFICIENT_EVIDENCE**. No universal number of requests, nodes, services or team members chooses microservices, Kafka, distributed caches or vector retrieval.

This synthesis relies on canonical Tycho material rather than inventing a hidden knowledge graph; a page or source reference must be read and verified at its actual version before making a consequential decision.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](data-availability.md) |
| Next | [Continue the reasoning](README.md) |
| Integrated question | [Original scenario and limits](cross-domain-modernization-and-adr-examples.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.
