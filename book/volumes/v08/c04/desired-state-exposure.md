---
metadata_version: 1
id: "tycho.page.3d13e39bb42a4458999803e40d7137cc"
kind: "page"
parent_id: "tycho.chapter.5e4761e1a3e34c2f8023ec8ac4fa81d5"
canonical_path: "book/volumes/v08/c04/desired-state-exposure.md"
title: "Desired state, release identity and exposure"
topic_ids:
  - "software-delivery"
perspectives:
  - "architecture"
  - "operations"
summary: "Which state does a reconciler control and which outcome remains outside it?"
route_hints:
  questions:
    - "Which state does a reconciler control and which outcome remains outside it?"
  prerequisites:
    - "tycho.page.b938ff1a06264492a425f2eff555ae7d"
  related_ids:
    - "tycho.chapter.5e4761e1a3e34c2f8023ec8ac4fa81d5"
    - "tycho.page.b938ff1a06264492a425f2eff555ae7d"
    - "tycho.page.21388c50717d4fa89384bedadcb0d3bd"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "desired"
    - "state"
    - "exposure"
evidence_scope:
  source_ids:
    - "src.k8s-deployments"
  claim_ids: []
  status: "source-linked"
  notes: "Bounded question from tycho.page.b938ff1a06264492a425f2eff555ae7d; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
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
# Desired state, release identity and exposure

**Owning question:** Which state does a reconciler control and which outcome remains outside it?

This page belongs to [V08/C04 — GitOps, rollout and progressive delivery](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.b938ff1a06264492a425f2eff555ae7d:1 -->
## 1. GitOps reconciles desired configuration, not business outcomes

A GitOps controller observes versioned desired deployment state and tries to align cluster/runtime resources with it. A clean diff or converged resource state does not mean downstream effects, durable writes or API contracts are correct.

Separate:
- **source/build artifact identity**: which immutable bytes were tested and approved;
- **deployment state**: which revision and configuration an authorized controller attempts to apply;
- **runtime readiness**: which instances are ready to accept some work;
- **traffic exposure**: which eligible requests reach old or candidate version;
- **user outcome**: correctly completed effects under the declared SLO and state contract.

The [CI/CD and GitOps provenance chapter](../c01/ci-cd-provenance-and-gitops.md) owns artifact source trust and reconciliation authority. This chapter considers what happens during controlled release exposure.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.b938ff1a06264492a425f2eff555ae7d:2 -->
## 2. Release strategies and their limits

| Strategy | Version exposure | Trade-off and hidden failure |
|---|---|---|
| Recreate | Stop old, start new; possible downtime | Avoids some simultaneous binaries, not lingering clients/events |
| Rolling | Gradually replace old replicas | N/N+1 coexist, shared DB and queues may carry both versions |
| Blue/green | Maintain two serving environments, switch routing | Extra capacity, sessions, shared state and irreversible N+1 writes |
| Canary | Candidate receives a bounded traffic slice; observe before expansion | Traffic percentage is not percentage of data effects or rare tenants |
| Feature-controlled rollout | Enable capability by identity/cohort/flag | State write may outlive a flag reversal |

[Kubernetes Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) documents rolling strategy knobs maxUnavailable and maxSurge. These govern resource availability/extra pods, not application-level data compatibility or a human approved exposure schedule.

The [Argo Rollouts Canary guide](https://argo-rollouts.readthedocs.io/en/stable/features/canary/) describes setWeight, pause, analysis and optional traffic management. Controller-specific weights should not be conflated with exact business-operation or tenant-level exposure without verifying routing behavior.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.b938ff1a06264492a425f2eff555ae7d:4 -->
## 4. Release identity and evidence gates

A controlled rollout needs:
1. immutable artifact digest/source provenance, policy-approved signer and target;
2. explicit old/new API, event and state compatibility matrix;
3. workload and expected client/tenant mix, not merely pod percentage;
4. observability of *offered, admitted and correct* user journeys;
5. hard authorization/consistency and known source-of-truth invariants;
6. stop/hold/abort controls and permissions to invoke them;
7. complete business-effect reconciliation on failure;
8. proven rollback **or** forward-recovery strategy before exposure;
9. promotion and decommissioning evidence.

A controller's “Available” status is one necessary operational signal; it is not evidence that an exclusive reservation or cross-version read still works.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](gitops-canary-and-progressive-rollout.md) |
| Next | [Continue the reasoning](canary-compatibility.md) |
| Integrated question | [Original scenario and limits](gitops-canary-and-progressive-rollout.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.
