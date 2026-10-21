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

## Bounded pattern ownership notes

These notes define the decision boundary for atlas cards whose mechanism is
not the main subject of this page. They are synthetic design guidance, not
measured evidence, and they do not create a new source claim.

### Dark Launching / Shadow Traffic

Dark launching sends mirrored or synthetic traffic to new code while the old path remains
authoritative. It needs side-effect suppression, a comparison method, a bounded load
budget and a rule for sensitive data. Use it when behavior can be observed without
changing user-visible state. Do not use it when shadow requests would write, charge,
notify or leak data.

The failure path is a mirrored request that causes a real effect or doubles load; isolate
the shadow path and stop it when the comparison or capacity contract fails. A canary that
receives a small real share is the alternative when shadow traffic cannot be made
side-effect free.

### Rolling Deployment

A rolling deployment replaces instances in batches, so old and new versions serve traffic together
during the rollout. Both versions must be compatible with the shared data and contracts for the
whole overlap, or the rollout must stop before an incompatible state is written.

Mixed versions expose an incompatibility that a single-version test missed; gate each batch on
readiness and error signals and keep a tested stop condition. Blue/green switches a complete
environment at once; choose rolling when the extra capacity for a second environment is unavailable.

### Blue/Green Deployment

Blue/green runs two complete environments and switches traffic at a routing boundary, leaving the
previous environment available for a short reversal. The switch must remain reversible until the new
version's persisted effects are proven compatible with the old version.

A half-switched route or a new-only write makes reversal unsafe; verify routing completeness and
data compatibility before declaring the cutover. A rolling or canary rollout uses less spare
capacity; choose blue/green when a fast, complete reversal and a clean environment comparison
justify the double capacity.
