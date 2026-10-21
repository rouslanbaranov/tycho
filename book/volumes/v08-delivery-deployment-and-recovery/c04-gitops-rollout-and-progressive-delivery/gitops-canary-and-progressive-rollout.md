---
metadata_version: 1
id: "tycho.page.b938ff1a06264492a425f2eff555ae7d"
kind: "page"
parent_id: "tycho.chapter.5e4761e1a3e34c2f8023ec8ac4fa81d5"
canonical_path: "book/volumes/v08-delivery-deployment-and-recovery/c04-gitops-rollout-and-progressive-delivery/gitops-canary-and-progressive-rollout.md"
title: "GitOps, rolling, blue/green and canary release architecture"
topic_ids:
  - "software-delivery"
perspectives:
  - "architecture"
  - "operations"
summary: "Integrated question, original scenario and transfer limits for GitOps, rollout and progressive delivery. Detailed mechanisms have separate question owners."
route_hints:
  questions:
    - "How do rolling, blue/green, canary, rollback and analysis gates differ?"
  prerequisites: []
  related_ids:
    - "tycho.page.81add4a0d86b4053ae77f9301fd2281d"
    - "tycho.page.77957bf0f2d44c4a9bc819fc5b3e1ddb"
    - "tycho.page.357c2d162bd44f3aa06a995a1e691551"
    - "tycho.page.7921e82a71b9446790f185c818326911"
    - "tycho.landing.1a9054fd18f64dfe911f34a4d17458c0"
    - "tycho.landing.fe2eace7b2df4ae480adbdf844b68100"
    - "tycho.page.1e89567050974052b13ba62b3b44484f"
    - "tycho.page.3d13e39bb42a4458999803e40d7137cc"
    - "tycho.page.21388c50717d4fa89384bedadcb0d3bd"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "GitOps"
    - "rolling"
    - "blue/green"
    - "and"
    - "canary"
    - "release"
    - "architecture"
evidence_scope:
  source_ids:
    - "src.k8s-deployments"
  claim_ids: []
  status: "source-linked"
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
<!-- tycho-question-source:tycho.page.b938ff1a06264492a425f2eff555ae7d:-1 -->

# GitOps, rolling, blue/green and canary release architecture

> **Independent Tycho V08/C04 manuscript**, 2026-10-19. Public Kubernetes Deployment and Argo Rollouts documentation informs controller mechanisms. All rollout examples, diagrams and acceptance criteria are original hypotheticals; no cluster, deployment, pipeline, experiment or external review was executed. Prior [mixed rollout/schema research](../../../delivery/progressive-delivery-and-schema-evolution.md) is preserved for editorial mapping.

<!-- /tycho-question-source -->

> **Pattern atlas:**
> [Rolling Deployment](../../v11-pattern-atlas/c10-deployment-modernization/README.md#rolling-deployment) — decision conditions and contraindications.
> [Blue/Green Deployment](../../v11-pattern-atlas/c10-deployment-modernization/README.md#blue-green-deployment) — decision conditions and contraindications.
> [Canary Release](../../v11-pattern-atlas/c10-deployment-modernization/README.md#canary-release) — decision conditions and contraindications.
> [Dark Launching / Shadow Traffic](../../v11-pattern-atlas/c10-deployment-modernization/README.md#dark-launching-shadow-traffic) — decision conditions and contraindications.

<!-- tycho-question-source:tycho.page.b938ff1a06264492a425f2eff555ae7d:0 -->
## Purpose and mission

A release mechanism decides which version is **deployed and exposed**. It does not by itself prove which data, users or business effects each version can safely interpret. Progressive deployment can limit a failure's initial blast radius, but cannot prevent a small canary from writing incompatible shared state used by every older instance.

This chapter owns **release-controller behavior, routing/exposure, analysis gates and GitOps reconciliation**. [V08/C05 data compatibility](../c05-backward-compatible-database-change/mixed-version-database-compatibility-and-online-ddl.md) owns old/new readers and online DDL; [V05/C06 data lifecycle](../../v05-data-models-engines-and-lifecycle/c06-schema-evolution-data-migration-and-retention/schema-lifecycle-and-semantic-migration.md) owns semantic migration itself.

<!-- /tycho-question-source -->

## Integrated decision and reading route

Define exposure, analysis, stop and recovery conditions across both application versions and shared data.

A small canary can write incompatible state visible to all old instances; limiting traffic alone does not bound that effect.

The detailed pages separate the mechanisms that make this decision conditional:

- [Desired state, release identity and exposure](desired-state-exposure.md) — Which state does a reconciler control and which outcome remains outside it?
- [Canary acceptance and shared-state damage](canary-compatibility.md) — How can a small rollout create effects that a binary rollback cannot undo?

[Chapter introduction, ordered pages and full source ledger](README.md). Original source labels retain their historical scope; this editorial decomposition does not turn proposed experiments into executed evidence.
