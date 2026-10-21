---
metadata_version: 1
id: "tycho.page.f05854fcc406435bbf38a192bc7ab2f1"
kind: "page"
parent_id: "tycho.chapter.809c2f1d12e544b38af2460b80d6d24e"
canonical_path: "book/volumes/v10-decision-support-and-modernization/c04-alternatives-experiments-and-adrs/architecture-alternatives-experiments-and-adrs.md"
title: "Architecture alternatives, discriminating experiments and decision records"
topic_ids:
  - "architecture-decisions"
perspectives:
  - "architecture"
  - "migration"
summary: "Integrated question, original scenario and transfer limits for Alternatives, experiments and ADRs. Detailed mechanisms have separate question owners."
route_hints:
  questions:
    - "Which hypotheses distinguish feasible options under hard constraints?"
  prerequisites: []
  related_ids:
    - "tycho.page.1cfb9cfdf1604fada0f508c123fe8b2e"
    - "tycho.page.f784d6ef723c4c0e8836ff9085bf7dcc"
    - "tycho.landing.1a9054fd18f64dfe911f34a4d17458c0"
    - "tycho.landing.b656116463d9480f83199d8202b127a4"
    - "tycho.page.868027aee4884210bea1d8a6542fbfb0"
    - "tycho.page.35d5be6a4e074758afff95bf3ec68bc5"
    - "tycho.page.b2d1285c1c1a4a698a2306c4e766a4f1"
    - "tycho.page.7079edf1ceeb4b1594083edf7a2c680e"
    - "tycho.page.a5285941dcba43d5a6a7c091cb4c99f9"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Architecture"
    - "alternatives"
    - "discriminating"
    - "experiments"
    - "and"
    - "decision"
    - "records"
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
authored_at: "2026-10-19"
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---
<!-- tycho-question-source:tycho.page.f05854fcc406435bbf38a192bc7ab2f1:-1 -->

# Architecture alternatives, discriminating experiments and decision records

> **Tycho independent book manuscript — proposed V10/C04, 2026-10-19.** The example, calculations and diagrams are original and hypothetical. This is a reader-facing explanation of how to compare options, not a real approved ADR, executable architecture experiment, or automated selector. The existing [candidate comparison authoring method](../../../../authoring/models/candidate-comparison-adr.md) remains a separately owned reusable record.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.f05854fcc406435bbf38a192bc7ab2f1:0 -->
## Purpose and mission

Architecture selection is not a competition between technology names. A useful decision starts with competing causal explanations of a problem and asks: **which observations could make one feasible candidate preferable to another without violating non-negotiable requirements?** An option that seems cheaper, faster or easier to operate cannot compensate for losing committed data or allowing unauthorized effects.

The [arc42 architecture decisions guidance, §9](https://docs.arc42.org/section-9/) recommends documenting important alternatives, criteria, rationale and consequences. It describes the familiar context/status/decision/consequences record, but does not supply a mathematical ranking that can replace evaluation. The [arc42 quality requirements guide, §10](https://docs.arc42.org/section-10/) emphasizes concrete, measurable scenarios. This chapter adds a systematic decision experiment to those principles and makes its uncertainty visible.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.f05854fcc406435bbf38a192bc7ab2f1:9 -->
## Engineering walkthrough — A hard requirement reverses a previously preferred ADR

**Original synthetic ADR-X17:** reporting currently shares one database and deployable application with the live booking API. A (retain modular deployment and add a bounded reporting worker) competes with B (separate reporting service and eventually a derived read model). The initial driver is slow analytical queries, not independently required tenant isolation.

| Test of choice | A: bounded worker | B: service extraction |
|---|---|---|
| Protect live write connections | Could pass by distinct admission/pools | Could pass with separate pools, but datastore may still be shared |
| Preserve existing authority | Same database transaction | Read projection consistency/replay and extra remote failures |
| Team operational readiness | Within initial staffing assumptions | Another critical service lacks agreed on-call owner |
| Independent security boundary | Shared process may have residual privileges | Potentially stronger if enforced and demonstrated |

**Provisional decision:** A, *conditional* on a controlled test showing isolated report concurrency cannot starve critical bookings. That is not a completed ADR approval. **Sensitivity reversal:** a subsequently confirmed legal rule demands separate execution principals and storage authorization that a shared process demonstrably cannot provide. A now fails a **hard constraint**, so B (or another truly isolated candidate) must be evaluated; no weighted preference for A's lower complexity can override the gate.

**Evidence plan, not executed:** same offered report and booking workload, authorized objects, old client versions, staff/on-call budget, recovery requirements and incident scenarios across feasible candidates. Record tested observations and uncertainty, explicit rejected alternatives and revision trigger in a versioned ADR. A plausible score or modern topology label cannot replace missing authority and rollback evidence. The arc42 ADR guidance motivates decision/history records, not this fictional organization's acceptance.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.f05854fcc406435bbf38a192bc7ab2f1:10 -->
## Applied M9 evidence: what transfers and what does not

These examples connect the chapter's conditional mechanism to published experiences or synthetic decision exercises. A historical company report is **first-party, time-scoped evidence**, not a controlled Tycho benchmark; an M9 decision playbook is **original synthetic analysis**, not a company decision.

**Case lens — [Reactive vs virtual threads](../../../cases/decisions/reactive-vs-virtual-threads.md)**. **Relevant mechanism or architectural contrast:** Synthetic comparison separates connection wait, CPU bound work, scheduler pinning and downstream pool budget. **Not established by this report/playbook:** Company observations are different workloads/JDK vintages, not a controlled head-to-head benchmark.

**Case lens — [GC vs tail latency](../../../cases/decisions/gc-and-tail-latency.md)**. **Relevant mechanism or architectural contrast:** Synthetic ADR chooses GC from SLO/cost workload objectives, using contrasting Netflix and contention cases. **Not established by this report/playbook:** The stated decision and candidate thresholds are hypothetical, not actual Netflix/Discord collector evaluations.

**Transfer test:** before applying the lesson to another legacy system, identify the exact workload, source date, relevant runtime/protocol versions, state authority, failure/recovery gate and the new observation that would reverse the choice. Follow the case's public evidence ledger rather than treating its link as independent proof.
<!-- /tycho-question-source -->

## Integrated decision and reading route

Compare feasible alternatives through experiments that can reverse the decision and record consequences in an ADR.

A changed hard requirement can invalidate a preferred score; a decision record should preserve why reconsideration is necessary.

The detailed pages separate the mechanisms that make this decision conditional:

- [Alternatives and discriminating hypotheses](decision-discriminators.md) — Which observation would make one feasible option preferable to another?
- [Sensitivity, consequences and stopping rules](adr-sensitivity.md) — When must a scored preference or recorded ADR be reconsidered?

[Chapter introduction, ordered pages and full source ledger](README.md). Original source labels retain their historical scope; this editorial decomposition does not turn proposed experiments into executed evidence.
