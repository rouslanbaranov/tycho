---
metadata_version: 1
id: "tycho.chapter.0a5e430b39094337aa6a211d9b5b4bd0"
kind: "chapter"
parent_id: "tycho.volume.e826731e3543471f94d5eb9af68cbfa7"
canonical_path: "book/volumes/v10/c05/README.md"
title: "V10/C05 — Target architecture versus transition states"
topic_ids:
  - "architecture-decisions"
perspectives:
  - "architecture"
  - "evaluation"
summary: "What is safe during coexistence, migration, rollback and recovery? The reading route separates 3 detailed questions from the integrated decision."
route_hints:
  questions:
    - "What is safe during coexistence, migration, rollback and recovery?"
  prerequisites:
    - "tycho.chapter.809c2f1d12e544b38af2460b80d6d24e"
  related_ids:
    - "tycho.chapter.3d0f6dd1e8e94cd397326e129b5c287f"
    - "tycho.chapter.7d434d1a41e142d38bb729ee124ac548"
    - "tycho.page.cf0ce38c73e44950aec5a9c2869bee63"
    - "tycho.page.78d0f89ac4184b19bfef3a72e8b4f2cc"
    - "tycho.page.47b67ebf3dbf477e818e83f9e1683ffe"
    - "tycho.page.ea1c3ca31f974bcbb6a432c55e56bc03"
  excludes:
    - "No new benchmark, source inspection or independent edition review is asserted."
  keywords:
    - "system-design"
    - "edition-navigation"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Editorial synthesis of the linked accepted manuscript; exact source versions and nonclaims remain in its page-local evidence ledger."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-20"
  reviewer: "Codex editorial assembly"
  proof_uri: null
authored_at: "2026-10-20"
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---

# V10/C05 — Target architecture versus transition states

## Purpose and mission

What is safe during coexistence, migration, rollback and recovery? This chapter owns that question within decision support and modernization playbooks. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Plan coexistence, authority transfer, no-return conditions and recovery as real intermediate operating states.

Rolling back an image cannot undo new-only durable effects; transition safety requires a separate forward-repair path. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

Begin with the integrated decision, then open the independent question that matches the missing mechanism or observed failure. Read source limits before applying the conclusion.

| Page | Independent question and role |
|---|---|
| [Integrated decision and original walkthrough](target-and-transition-architecture-states.md) | What is safe during coexistence, migration, rollback and recovery? |
| [State authority and coexistence transitions](authority-states.md) | Which owner is authoritative in every real intermediate configuration? |
| [Rollback limits and semantic reconciliation](rollback-data.md) | Which durable differences survive reverting the deployed binary? |
| [Migration mechanisms and no-return gates](cutover-gates.md) | What evidence permits a transition to cross an irreversible boundary? |

## Boundaries and further reading

- [V05/C06 — Schema evolution, data migration and retention](../../v05/c06/README.md) owns the adjacent question; compare assumptions before transferring the conclusion.
- [V08/C05 — Backward-compatible database change](../../v08/c05/README.md) owns the adjacent question; compare assumptions before transferring the conclusion.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V10 — Decision support and modernization playbooks](../README.md) |
| Previous | [V10/C04 — Alternatives, experiments and ADRs](../c04/README.md) |
| Next | [V10/C06 — Search and question routes for architecture agents](../c06/README.md) |
| Prerequisite | [V10/C04 — Alternatives, experiments and ADRs](../c04/README.md) |
| Source reading | [Page-local evidence and versions](target-and-transition-architecture-states.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.

## Chapter source ledger

The following original citation rows, review limits and earlier topical routes are retained once for this chapter. Each question page points here and retains its inline citations. Evidence coverage must be judged at the actual claim and version, not inferred from source-list length.

<!-- tycho-question-source:tycho.page.cf0ce38c73e44950aec5a9c2869bee63:8 -->
## 8. Source and nonclaim ledger

| Independently inspected source | Applies to | Not verified |
|---|---|---|
| [Fowler, Strangler Fig, 22 Aug 2024](https://martinfowler.com/bliki/StranglerFigApplication.html) | Incremental outcomes-led displacement and coexisting capabilities | Feasibility for the hypothetical catalogue |
| [Microsoft, Strangler Fig pattern, revision available 2026](https://learn.microsoft.com/en-us/azure/architecture/patterns/strangler-fig) | Interception/coexistence, façade bottleneck and inapplicability conditions | Actual routing, data integrity or recovery |
| [arc42 Architecture Decisions §9](https://docs.arc42.org/section-9/) | Decision context, evidence, alternatives and consequences | Approval of any migration design |
| [Tycho target/transition authoring model](../../../../authoring/models/target-transition-architecture.md) | Existing independent workflow and scope fields | Executed migration, model conformance or external test |

The example, diagrams, client versions, recovery gates and migration states are original hypothetical material, not production facts. No architecture approval, full repository boundary check, deployed migration, source snapshot verification or independently reviewed acceptance is claimed.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.cf0ce38c73e44950aec5a9c2869bee63:9 -->
## Navigation

Proposed **V10/C05**, currently [decision support landing](../../../decisions/README.md). Prerequisites: [legacy baseline](../c02/legacy-baseline-and-modernization-evidence.md), [API compatibility](../../v02/c05/http-rpc-contracts-and-compatibility.md), [data ownership](../../v02/c02/domain-boundaries-data-ownership-and-contracts.md). Next: [architecture alternatives/ADR](../c04/architecture-alternatives-experiments-and-adrs.md), [safe rollout](../../../delivery/safe-rollout-and-recovery.md), and [question-driven decision routes](../c06/question-routes-for-architecture-analysis.md).

<!-- /tycho-question-source -->
