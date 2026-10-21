---
metadata_version: 1
id: "tycho.chapter.8605018cb9224f99bea9dd49be2b79e3"
kind: "chapter"
parent_id: "tycho.volume.e826731e3543471f94d5eb9af68cbfa7"
canonical_path: "book/volumes/v10-decision-support-and-modernization/c02-baseline-analysis-for-existing-software/README.md"
title: "V10/C02 — Baseline analysis for existing software"
topic_ids:
  - "architecture-decisions"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Which observed limitations justify changing the architecture? The reading route separates 3 detailed questions from the integrated decision."
route_hints:
  questions:
    - "Which observed limitations justify changing the architecture?"
  prerequisites:
    - "tycho.chapter.289750444f8040d292a474e3876046a1"
  related_ids:
    - "tycho.page.b2d1285c1c1a4a698a2306c4e766a4f1"
    - "tycho.page.210134080fac4c09bebb593befd0cb25"
    - "tycho.page.19145078d87143b28387ab187d345c32"
    - "tycho.page.fbf4c3d642d14ce2a69f009efd17b1a8"
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

# V10/C02 — Baseline analysis for existing software

## Purpose and mission

Which observed limitations justify changing the architecture? This chapter owns that question within decision support and modernization playbooks. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Describe observed legacy behavior and limitations before assigning expected benefits to a target architecture.

Old technology is not itself evidence of a defect; retaining and improving the baseline must remain a real alternative. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

Begin with the integrated decision, then open the independent question that matches the missing mechanism or observed failure. Read source limits before applying the conclusion.

| Page | Independent question and role |
|---|---|
| [Integrated decision and original walkthrough](legacy-baseline-and-modernization-evidence.md) | Which observed limitations justify changing the architecture? |
| [Observed legacy behavior and baseline ownership](legacy-observation.md) | Which existing behavior must be measured and preserved before change is justified? |
| [Modernization alternatives and transition obligations](modernization-options.md) | How do retained, replaced and incrementally migrated options differ in required proof? |
| [Migration failure tests and decision reversal](migration-falsification.md) | Which recovery observation would reject the attractive target? |

## Boundaries and further reading

The preceding and following chapters supply context; this landing does not replace their canonical mechanisms. Follow the exact source ledger on the child page when a claim depends on a product version or historical period.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V10 — Decision support and modernization playbooks](../README.md) |
| Previous | [V10/C01 — Architecture requirement and workload profiles](../c01-architecture-requirement-and-workload-profiles/README.md) |
| Next | [V10/C03 — Pattern applicability and contraindications](../c03-pattern-applicability-and-contraindications/README.md) |
| Prerequisite | [V10/C01 — Architecture requirement and workload profiles](../c01-architecture-requirement-and-workload-profiles/README.md) |
| Source reading | [Page-local evidence and versions](legacy-baseline-and-modernization-evidence.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.

## Chapter source ledger

The following original citation rows, review limits and earlier topical routes are retained once for this chapter. Each question page points here and retains its inline citations. Evidence coverage must be judged at the actual claim and version, not inferred from source-list length.

<!-- tycho-question-source:tycho.page.b2d1285c1c1a4a698a2306c4e766a4f1:8 -->
## 8. Public source ledger and review limits

| Independently accessible reference reviewed | Supports | Does not establish |
|---|---|---|
| [Fowler, Strangler Fig (2024)](https://martinfowler.com/bliki/StranglerFigApplication.html) | Incremental legacy replacement rationale | That all older applications should be extracted |
| [Cartwright, Horn & Lewis, Patterns of Legacy Displacement (2024)](https://martinfowler.com/articles/patterns-legacy-displacement/) | Outcome-led, staged modernization and displacement patterns | Measurements for the synthetic catalog |
| [Microsoft Architecture Center, Strangler Fig](https://learn.microsoft.com/en-us/azure/architecture/patterns/strangler-fig) | Coexistence/routing trade-offs and phased substitution | A validated single-writer migration in this page |
| [AWS Prescriptive Guidance, modernization considerations](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-aspnet-web-services/considerations.html) | Interim versus target-state considerations | Platform-independent universal implementation details |
| [Tycho safe rollout and recovery](../../../delivery/safe-rollout-and-recovery.md) | Page-local test and recovery explanation | An actual exercised rollback |

**Provenance boundaries:** every component, observation, workflow, diagram, decision and failure in the fictional catalog is original synthetic teaching material. No private or restricted architecture source was consulted. No live application, actual schema, production measurement, independent compliance/domain review or recovery exercise exists for it. Public pattern descriptions are documented design options, not verified implementation outcomes. Actual source/version/access limitations require a fresh review for real use.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.b2d1285c1c1a4a698a2306c4e766a4f1:9 -->
## Navigation

- Planned home: **V10/C02** in [Tycho's proposed chapters](../../../PROPOSED-STRUCTURE.md), currently linked from [decision-support landing](../../../decisions/README.md).
- Before: [Requirements/workload profile](../c01-architecture-requirement-and-workload-profiles/requirements-and-workload-architecture-profiles.md).
- Mechanisms: [Application architecture evolution](../../../application/architecture-evolution-and-extraction.md); [Transactional outbox](../../../distributed/transactional-outbox-and-idempotency.md); [HTTP/RPC compatibility](../../v02-application-boundaries-and-contracts/c05-public-apis-http-rpc-and-compatibility/http-rpc-contracts-and-compatibility.md).
- Transition owners: [Safe rollout and recovery](../../../delivery/safe-rollout-and-recovery.md); [Schema evolution](../../../delivery/progressive-delivery-and-schema-evolution.md).
- Supporting method (not book chapter): [Legacy baseline authoring model](../../../../authoring/models/legacy-modernization-profile.md).

<!-- /tycho-question-source -->
