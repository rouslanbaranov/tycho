---
metadata_version: 1
id: "tycho.page.0ce5d0aaf63f425ebf556ea97e2d24a9"
kind: "page"
parent_id: "tycho.chapter.5fb14670d0b24967a5e6c24df7221d74"
canonical_path: "book/volumes/v10-decision-support-and-modernization/c07-cross-domain-worked-comparisons-and-unresolved-cases/cross-domain-modernization-and-adr-examples.md"
title: "Cross-domain architecture decisions and modernization under constraints"
topic_ids:
  - "architecture-decisions"
perspectives:
  - "architecture"
  - "migration"
summary: "Integrated question, original scenario and transfer limits for Cross-domain worked comparisons and unresolved cases. Detailed mechanisms have separate question owners."
route_hints:
  questions:
    - "How does a decision stay falsifiable and attributable to its sources?"
  prerequisites: []
  related_ids:
    - "tycho.page.a9a28aaa4d1e4e9cb0accd2fc2c5ba9b"
    - "tycho.page.f784d6ef723c4c0e8836ff9085bf7dcc"
    - "tycho.page.dc2470904e004a4aa733abcdb25517ed"
    - "tycho.page.ace968ab1de8409383c6a9b22a00d006"
    - "tycho.page.81add4a0d86b4053ae77f9301fd2281d"
    - "tycho.page.9176c39f97f544f884666e291ae38b90"
    - "tycho.page.ded52d8d012347b79d70e608488cf6a4"
    - "tycho.page.0d34dd26886340b89fd4f1499d790a81"
    - "tycho.page.ea94649bfd8c4be183f9114618d7ccaa"
    - "tycho.page.2536d18422944e27abe4ea8549beb9ab"
    - "tycho.page.1e89567050974052b13ba62b3b44484f"
    - "tycho.page.dde63373c50f4f4a80e727b6e160def5"
    - "tycho.page.0b493340594c4c4392c5d93940a7f319"
    - "tycho.page.2eb290f6307f4797a5981510f1248d70"
    - "tycho.page.22b12598c23b4fc5ac74b1adc960ebe5"
    - "tycho.page.aaed70abf79447c89a544eaf84f0da96"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Cross-domain"
    - "architecture"
    - "decisions"
    - "and"
    - "modernization"
    - "under"
    - "constraints"
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
<!-- tycho-question-source:tycho.page.0ce5d0aaf63f425ebf556ea97e2d24a9:-1 -->

# Cross-domain architecture decisions and modernization under constraints

> Tycho E14-12 [issue #90](https://github.com/rouslanbaranov/tycho/issues/90), original synthesis of existing canonical models and technical chapters, 2026-10-19. All scenarios are fictional and all outcomes conditional. No live modernization project, benchmark, review board decision or independent domain review is claimed.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.0ce5d0aaf63f425ebf556ea97e2d24a9:0 -->
## Purpose and mission

Architecture selection is a process of excluding proven bad fits, measuring unknowns and comparing the cost of feasible options. There is no universally preferable topology: a modular monolith, a service split, asynchronous queue or caching tier can each be correct under different state ownership, failure and workload constraints.

**Question:** Given a requirement, an operational symptom, a legacy constraint or a modernization objective, how do we select an architecture and a safe transition with auditable evidence rather than fashionable technology names?

Canonical methods already exist: [requirements/workload](../../../../authoring/models/requirements-workload-profile.md), [legacy baseline](../../../../authoring/models/legacy-modernization-profile.md), [pattern applicability](../../../../authoring/models/pattern-applicability-card.md), [ADR comparison](../../../../authoring/models/candidate-comparison-adr.md), [target/transition architecture](../../../../authoring/models/target-transition-architecture.md) and [decision navigation](../../../../authoring/models/decision-navigation.md). This chapter applies them rather than inventing a second framework.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.0ce5d0aaf63f425ebf556ea97e2d24a9:10 -->
## Applied M9 evidence: what transfers and what does not

These examples connect the chapter's conditional mechanism to published experiences or synthetic decision exercises. A historical company report is **first-party, time-scoped evidence**, not a controlled Tycho benchmark; an M9 decision playbook is **original synthetic analysis**, not a company decision.

**Case lens — [Agent-assisted migration safety](../../../cases/decisions/agentic-migration-safety.md)**. **Relevant mechanism or architectural contrast:** Synthetic ADR requires behavior, isolation and evidence gates before agent-generated code can change production. **Not established by this report/playbook:** Shopify/Spotify reports do not provide authorization for fully autonomous unsafe changes or benchmarked universal agent correctness.

**Transfer test:** before applying the lesson to another legacy system, identify the exact workload, source date, relevant runtime/protocol versions, state authority, failure/recovery gate and the new observation that would reverse the choice. Follow the case's public evidence ledger rather than treating its link as independent proof.
<!-- /tycho-question-source -->

## Integrated decision and reading route

Carry source scope, requirements, alternatives and falsification through a complete worked modernization decision.

A historical company's result or a synthetic comparison cannot promise the same benefit elsewhere without matching its conditions.

The detailed pages separate the mechanisms that make this decision conditional:

- [Workload and runtime modernization comparisons](workload-runtime.md) — Which bottleneck and migration invariant distinguish the first alternatives?
- [Data, availability and hard feasibility gates](data-availability.md) — Which authoritative-state and recovery assumptions reject an appealing design?
- [Worked ADR and unresolved conclusions](worked-adr.md) — How is a complete recommendation kept falsifiable and source-scoped?

[Chapter introduction, ordered pages and full source ledger](README.md). Original source labels retain their historical scope; this editorial decomposition does not turn proposed experiments into executed evidence.
