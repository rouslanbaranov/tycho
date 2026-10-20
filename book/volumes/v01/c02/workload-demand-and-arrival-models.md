---
metadata_version: 1
id: "tycho.page.fdb4ef7f69154f8c8c433591f71494f9"
kind: "page"
parent_id: "tycho.chapter.316b50ac3db440ae82c0986b896ff468"
canonical_path: "book/volumes/v01/c02/workload-demand-and-arrival-models.md"
title: "Workload and demand models: from user behavior to measurable offered work"
topic_ids:
  - "performance-engineering"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Integrated question, original scenario and transfer limits for Workload and demand models. Detailed mechanisms have separate question owners."
route_hints:
  questions:
    - "How do active users, offered arrivals, concurrency, operation mix and skew differ?"
  prerequisites: []
  related_ids:
    - "tycho.page.868027aee4884210bea1d8a6542fbfb0"
    - "tycho.page.f784d6ef723c4c0e8836ff9085bf7dcc"
    - "tycho.page.1cfb9cfdf1604fada0f508c123fe8b2e"
    - "tycho.page.a9a28aaa4d1e4e9cb0accd2fc2c5ba9b"
    - "tycho.page.0d34dd26886340b89fd4f1499d790a81"
    - "tycho.page.49d9df04c0b4488e936b02e580a62271"
    - "tycho.page.35d5be6a4e074758afff95bf3ec68bc5"
    - "tycho.landing.1a9054fd18f64dfe911f34a4d17458c0"
    - "tycho.landing.b08f16ced4a142a785c37b43eb340260"
    - "tycho.page.4318e542ac7e445b9e8b3150effd2cff"
    - "tycho.page.2a3a20bc92314c7597b1792b8607c9d5"
    - "tycho.page.f66686aeabca4f5b8f550696bf37e557"
    - "tycho.page.59682af71a9f435680917ae5ece63088"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Workload"
    - "and"
    - "demand"
    - "models"
    - "from"
    - "user"
    - "behavior"
    - "measurable"
    - "offered"
    - "work"
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
<!-- tycho-question-source:tycho.page.fdb4ef7f69154f8c8c433591f71494f9:-1 -->

# Workload and demand models: from user behavior to measurable offered work

> **Original Tycho book draft V01/C02**, prepared 2026-10-19. Independently public queueing and load-model references, with invented examples. No population analytics, experiment, observed user trace, or validated production forecast exists for this chapter.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.fdb4ef7f69154f8c8c433591f71494f9:0 -->
## Purpose and mission

“Ten thousand users” is not a sufficient workload specification. A system may have ten thousand accounts and almost no concurrent work; another with the same account count may receive a short burst of writes against one state key. Architecture decisions need a model of **arrivals, logical operations, concurrency, resource demand, key skew and time**. A good model makes assumptions visible and can be disproved by real observations.

This foundational chapter describes how to define those quantities and estimate offered work without converting user population into requests per second by an invented universal constant. The [V10 architecture requirement profile](../../v10/c01/requirements-and-workload-architecture-profiles.md) applies workloads to option selection; [capacity experiments](../../../performance/workload-profiles-and-capacity-experiments.md) and [benchmark methodology](../../v07/c03/load-testing-and-benchmark-validity.md) own testing procedures. The [Little's Law chapter](../../v07/c01/queueing-littles-law.md) owns the conservation identity and its finite-window limits.

<!-- /tycho-question-source -->

## Integrated decision and reading route

Separate offered attempts, admitted work, successful outcomes, concurrency and per-operation demand before estimating capacity.

Two equally sized user populations can impose different bursts and hot-key pressure; average requests per second conceals that difference.

The detailed pages separate the mechanisms that make this decision conditional:

- [Population, arrival and admission models](arrivals-population.md) — How do user population and arrival process change offered work?
- [Demand arithmetic and skew](demand-skew.md) — What does a demand estimate conceal about operation mix, bursts and hot keys?
- [Workload contracts for architecture choices](workload-contract.md) — What must a workload contract state before it can reject or support an option?

[Chapter introduction, ordered pages and full source ledger](README.md). Original source labels retain their historical scope; this editorial decomposition does not turn proposed experiments into executed evidence.
