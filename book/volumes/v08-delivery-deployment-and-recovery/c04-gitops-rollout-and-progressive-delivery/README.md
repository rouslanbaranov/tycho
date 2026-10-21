---
metadata_version: 1
id: "tycho.chapter.5e4761e1a3e34c2f8023ec8ac4fa81d5"
kind: "chapter"
parent_id: "tycho.volume.cb10070ba233477fae8aa5d18e74fee8"
canonical_path: "book/volumes/v08-delivery-deployment-and-recovery/c04-gitops-rollout-and-progressive-delivery/README.md"
title: "V08/C04 — GitOps, rollout and progressive delivery"
topic_ids:
  - "software-delivery"
perspectives:
  - "architecture"
  - "evaluation"
summary: "How do rolling, blue/green, canary, rollback and analysis gates differ? The reading route separates 2 detailed questions from the integrated decision."
route_hints:
  questions:
    - "How do rolling, blue/green, canary, rollback and analysis gates differ?"
  prerequisites:
    - "tycho.chapter.94b4b6d9e2e1490abd0055a5265141ff"
  related_ids:
    - "tycho.chapter.8a2d2a79846d4567bb3d33957e19977f"
    - "tycho.page.b938ff1a06264492a425f2eff555ae7d"
    - "tycho.page.3d13e39bb42a4458999803e40d7137cc"
    - "tycho.page.21388c50717d4fa89384bedadcb0d3bd"
  excludes:
    - "No new benchmark, source inspection or independent edition review is asserted."
  keywords:
    - "system-design"
    - "edition-navigation"
evidence_scope:
  source_ids:
    - "src.k8s-deployments"
    - "src.sre"
  claim_ids: []
  status: "source-linked"
  notes: "Editorial synthesis of the linked accepted manuscript; exact source versions and nonclaims remain in its page-local evidence ledger."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-20"
  reviewer: "Codex editorial assembly"
  proof_uri: null
authored_at: "2026-10-20"
updated_at: "2026-10-21"
source_inspection_date: null
content_verified_at: null
---

# V08/C04 — GitOps, rollout and progressive delivery

## Purpose and mission

How do rolling, blue/green, canary, rollback and analysis gates differ? This chapter owns that question within delivery, deployment and disaster recovery. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Define exposure, analysis, stop and recovery conditions across both application versions and shared data.

A small canary can write incompatible state visible to all old instances; limiting traffic alone does not bound that effect. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

Begin with the integrated decision, then open the independent question that matches the missing mechanism or observed failure. Read source limits before applying the conclusion.

| Page | Independent question and role |
|---|---|
| [Integrated decision and original walkthrough](gitops-canary-and-progressive-rollout.md) | How do rolling, blue/green, canary, rollback and analysis gates differ? |
| [Desired state, release identity and exposure](desired-state-exposure.md) | Which state does a reconciler control and which outcome remains outside it? |
| [Canary acceptance and shared-state damage](canary-compatibility.md) | How can a small rollout create effects that a binary rollback cannot undo? |


## Additional mechanism and project routes

These independently scoped pages extend the chapter without replacing its original walkthrough or source ledger.

| Page | Owning question |
| --- | --- |
| [Dynamic configuration and feature flags](configuration-rollout.md) | How can configuration change safely while different processes observe different versions? |

## Boundaries and further reading

- [V08/C01 — CI/CD architecture and artifact provenance](../c01-ci-cd-architecture-and-artifact-provenance/README.md) owns the adjacent question; compare assumptions before transferring the conclusion.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V08 — Delivery, deployment and disaster recovery](../README.md) |
| Previous | [V08/C03 — VMs, containers, orchestration and serverless](../c03-vms-containers-orchestration-and-serverless/README.md) |
| Next | [V08/C05 — Backward-compatible database change](../c05-backward-compatible-database-change/README.md) |
| Prerequisite | [V08/C03 — VMs, containers, orchestration and serverless](../c03-vms-containers-orchestration-and-serverless/README.md) |
| Source reading | [Page-local evidence and versions](gitops-canary-and-progressive-rollout.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.

## Chapter source ledger

The following original citation rows, review limits and earlier topical routes are retained once for this chapter. Each question page points here and retains its inline citations. Evidence coverage must be judged at the actual claim and version, not inferred from source-list length.

<!-- tycho-question-source:tycho.page.b938ff1a06264492a425f2eff555ae7d:7 -->
## 7. Public source ledger

| Versioned/public source | Narrow support | Not established |
|---|---|---|
| [Kubernetes Deployments — rolling updates](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) | maxSurge/maxUnavailable, rollout progress and controller mechanics | Product/data compatibility |
| [Argo Rollouts Canary](https://argo-rollouts.readthedocs.io/en/stable/features/canary/) | Weighted steps, pauses, analysis concepts | Representative business-outcome measurement |
| [Prior combined rollout/schema study](../../../delivery/progressive-delivery-and-schema-evolution.md) | Existing source-led mixed-version and rollout research | Run release, restore or independently accepted decision |

- [SRE, *Reliable Product Launches*](https://sre.google/sre-book/reliable-product-launches/),
  inspected 2026-10-21: capacity planning, client behavior, launch traffic and
  overload tests. The chapter's examples are contextual, not universal estimates.

All examples, diagrams and acceptance steps are invented for teaching. No cluster, signed release, test, rollback or source-to-claim independent approval occurred.

**Navigation:** canonical chapter in the current edition. Start at the
[volume landing](../README.md).
<!-- /tycho-question-source -->
