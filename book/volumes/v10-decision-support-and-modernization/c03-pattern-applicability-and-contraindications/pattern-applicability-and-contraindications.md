---
metadata_version: 1
id: "tycho.page.35d5be6a4e074758afff95bf3ec68bc5"
kind: "page"
parent_id: "tycho.chapter.b20625a099bc4c82b7d547c32c7da28a"
canonical_path: "book/volumes/v10-decision-support-and-modernization/c03-pattern-applicability-and-contraindications/pattern-applicability-and-contraindications.md"
title: "Architecture patterns: applicability, contraindications and evidence gates"
topic_ids:
  - "architecture-decisions"
perspectives:
  - "architecture"
  - "migration"
summary: "Integrated question, original scenario and transfer limits for Pattern applicability and contraindications. Detailed mechanisms have separate question owners."
route_hints:
  questions:
    - "Which evidence, preconditions and failures bound a pattern's usefulness?"
  prerequisites: []
  related_ids:
    - "tycho.page.868027aee4884210bea1d8a6542fbfb0"
    - "tycho.page.b2d1285c1c1a4a698a2306c4e766a4f1"
    - "tycho.page.c226850223614886b61b7cb36c7d5032"
    - "tycho.page.ace968ab1de8409383c6a9b22a00d006"
    - "tycho.page.0b493340594c4c4392c5d93940a7f319"
    - "tycho.page.98616bdc3c514ea997b2cfe30ad7c070"
    - "tycho.page.ded52d8d012347b79d70e608488cf6a4"
    - "tycho.page.0d34dd26886340b89fd4f1499d790a81"
    - "tycho.page.02238832b395417bae63939cd96b9134"
    - "tycho.page.114da51171c2474ebd56ee3bebad3bcb"
    - "tycho.page.b6cecfd7301b408db611228b4cec59c5"
    - "tycho.page.0ce5d0aaf63f425ebf556ea97e2d24a9"
    - "tycho.landing.1a9054fd18f64dfe911f34a4d17458c0"
    - "tycho.landing.b656116463d9480f83199d8202b127a4"
    - "tycho.page.2176fe3dcdf24a199d1656cba602e8e1"
    - "tycho.page.2debc63415184b02ad0a144b2649c171"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Architecture"
    - "patterns"
    - "applicability"
    - "contraindications"
    - "and"
    - "evidence"
    - "gates"
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
<!-- tycho-question-source:tycho.page.35d5be6a4e074758afff95bf3ec68bc5:-1 -->

# Architecture patterns: applicability, contraindications and evidence gates

> **Tycho chapter draft V10/C03**, 2026-10-19, original general-purpose explanations and synthetic examples. This is the book-level interpretation of pattern selection. The separately maintained [pattern applicability authoring model](../../../../authoring/models/pattern-applicability-card.md) remains a reusable decision-record tool and is not substituted for technical prose. No real design review, measured service or automatic selector is claimed.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.35d5be6a4e074758afff95bf3ec68bc5:0 -->
## Purpose and mission

An architecture pattern is a **conditional intervention** into an existing set of constraints. Microservices can create independent deployments but add remote failure and data ownership questions; caching can avoid repeated work but weaken freshness unless tightly controlled; sharding can distribute independent keys but does not solve contention on a single logical record. Knowing a pattern's definition is not enough to decide whether to apply it.

This chapter teaches how to turn a requirements and legacy baseline into **applicability conditions, disqualifying evidence, alternatives and a falsifiable experiment**. The chapter is neither a broad taxonomy nor a ranked list of favorite technologies. [Martin Fowler's Microservice Trade-Offs (2015)](https://martinfowler.com/articles/microservice-trade-offs.html) explicitly analyzes benefits against distribution, consistency and operational costs. [SEI ATAM](https://www.sei.cmu.edu/library/the-architecture-tradeoff-analysis-method/) studies quality-attribute interactions. These public methods support conditional selection rather than universal adoption.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.35d5be6a4e074758afff95bf3ec68bc5:9 -->
## Engineering walkthrough — Two attractive patterns fail the same hot-key workload

**Original synthetic requirement:** a small booking platform has moderate aggregate traffic but one hot exclusive item, one PostgreSQL writer, strict immediate confirmation and limited on-call capacity. The choice cannot be made from fleet RPS alone.

| Pattern | When it may fit | Contraindication here |
|---|---|---|
| Modular monolith with admission | Local invariant, current team and release mode fit | Independent deployment mandated by a different hard requirement |
| Microservices | Independent domain ownership and measured deployment benefit | Extra remote failure and authority migration do not remove one serialized key |
| Kafka/queue | Pending outcomes and replay are acceptable | Client requires immediate confirmed result |
| Distributed cache | Stale public catalogue descriptions allowed | Cache cannot confirm exclusive booking independently |
| Sharding | Load spreads across independent keys | One hot key remains single-owner serialized work |
| Virtual threads | Large blocking I/O population with bounded downstream | CPU/DB locks dominate current symptom |
| Reactive | End-to-end nonblocking APIs and flow control are justified | Blocking downstream just relocates the backlog |

**Decision:** retain a single booking authority and test bounded admission and query/lock optimization first. **Reject sharding and service decomposition as unsupported current cures for the single hot-key invariant.** A later team-autonomy or isolation requirement may reverse that choice without invalidating the present analysis.

**Proposed tests, not run:** offered demand with representative key skew, lock and pool wait, correct confirmed completions and change-lead-time measurements. Route specialized claims to their existing canonical chapters instead of reproducing each implementation here. This pattern-selection exercise is original, not a benchmark or general prohibition on distributed services.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.35d5be6a4e074758afff95bf3ec68bc5:10 -->
## Applied M9 evidence: what transfers and what does not

These examples connect the chapter's conditional mechanism to published experiences or synthetic decision exercises. A historical company report is **first-party, time-scoped evidence**, not a controlled Tycho benchmark; an M9 decision playbook is **original synthetic analysis**, not a company decision.

**Case lens — [Monolith vs services](../../../cases/decisions/monolith-vs-services.md)**. **Relevant mechanism or architectural contrast:** Synthetic ADR contrasts Shopify modularity and Netflix/Uber distribution under explicit ownership and team cost. **Not established by this report/playbook:** The proposed monolith-first choice is Tycho's fictional decision, never a decision those companies jointly evaluated.

**Transfer test:** before applying the lesson to another legacy system, identify the exact workload, source date, relevant runtime/protocol versions, state authority, failure/recovery gate and the new observation that would reverse the choice. Follow the case's public evidence ledger rather than treating its link as independent proof.
<!-- /tycho-question-source -->

## Integrated decision and reading route

Treat a pattern as a conditional intervention with explicit prerequisites, contraindications and reversal evidence.

A cache and a service split can both fail the same serialized hot-key workload; naming a pattern does not establish causal fit.

The detailed pages separate the mechanisms that make this decision conditional:

- [Conditional applicability cards and baseline fit](pattern-cards.md) — Which invariant, workload and operating precondition makes a pattern useful?
- [Contraindications and transition falsification](contraindications-transition.md) — Which counterexample or migration cost should reverse the pattern choice?

[Chapter introduction, ordered pages and full source ledger](README.md). Original source labels retain their historical scope; this editorial decomposition does not turn proposed experiments into executed evidence.
