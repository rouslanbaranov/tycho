---
metadata_version: 1
id: "tycho.chapter.dabaea8f5ab426edc08683ceec89c2c0"
kind: "chapter"
parent_id: "tycho.volume.fe327f72cf81df0237ce47b841e8aef5"
canonical_path: "book/volumes/v11-pattern-atlas/c10-deployment-modernization/README.md"
title: "V11/C10 — Deployment and legacy modernization"
topic_ids:
  - "deployment-architecture"
  - "software-delivery"
perspectives:
  - "architecture"
  - "migration"
summary: "All 12 C10 cards with bounded owner links; decision coverage partial."
route_hints:
  questions:
    - "Which deployment patterns keep change reversible?"
  prerequisites:
    - "tycho.chapter.b20625a099bc4c82b7d547c32c7da28a"
  related_ids:
    - "tycho.volume.fe327f72cf81df0237ce47b841e8aef5"
    - "tycho.chapter.b20625a099bc4c82b7d547c32c7da28a"
    - "tycho.chapter.3b9ec227ed58b92c0004eb0d39099142"
    - "tycho.chapter.419769c372ccaa569796954878e3bef9"
  excludes:
    - "Bounded owner links; no sufficient coverage or independent review."
  keywords:
    - "pattern atlas"
    - "deployment and legacy modernization"
    - "decision layer"
evidence_scope:
  source_ids:
    - "src.aws-immutable-infrastructure"
    - "src.fowler-dark-launching"
    - "src.istio-traffic-mirroring"
    - "src.k8s-deployments"
    - "src.argo-rollouts"
    - "src.flagger-deployment-strategies"
    - "src.sre-workbook"
    - "src.aws-blue-green-deployments"
    - "src.fowler-feature-toggles"
    - "src.opengitops"
    - "src.ibm-immutable-infrastructure"
    - "src.fowler-strangler"
    - "src.aws-strangler"
    - "src.fowler-branch"
    - "src.flyway"
    - "src.mysql"
    - "src.postgresql"
    - "src.appconfig-rollout"
    - "src.aws-branch"
    - "src.hashicorp-immutable-vms"
    - "src.argocd"
    - "src.flux"
  claim_ids: []
  status: "source-linked"
  notes: "12 cards cite read units; GitOps binds Argo CD and Flux 2026-11-01; owner links bounded."
content_review:
  status: "self-checked"
  reviewed_at: "2026-11-01"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-21"
updated_at: "2026-11-01"
source_inspection_date: "2026-11-01"
content_verified_at: null
---
# V11/C10 — Deployment and legacy modernization

**Owning question:** Which deployment patterns keep change reversible?

## Purpose and mission

This chapter is the atlas entry point for **Deployment and legacy modernization**. It
owns the conditional decision route for 12 catalog entries, not the deep mechanism
explanations. Read the exact owner section before applying a mechanism claim.

All 12 entries have a self-checked card. Owner sections are bounded: a rollout or
transition-state page may own the reversibility contract without owning every pattern.

## Pages and reasoning route

Page count is content-dependent. This chapter uses a landing page plus a dedicated
card page; a later split is an editorial change, not a plan failure. Start with the card,
check its conditions and contraindications, then read the exact owner section.

## Entry inventory

Each level-three heading is a stable atlas anchor. Owner links are bounded sections;
none claims sufficient technical or decision coverage.

### Rolling Deployment

**Identity.** Rolling Deployment; family Deployment and legacy modernization; kind
deployment-pattern; priority core.

**Decision question.** Should instances be replaced incrementally while traffic continues?

**Good-fit conditions.** Multiple instances and a readiness signal exist; old/new versions
are compatible; drain/rollback is defined.

**Hard contraindications.** Reject when versions cannot coexist, when no readiness/drain
control exists, or when rollback requires simultaneous replacement.

**Competing alternative.** Blue/green or recreate. Reverse the choice when incremental
compatibility cost exceeds rollout benefit.

**Failure and recovery.** Partial-version exposure is common; verify readiness in the
owner section.

**Technical owner.** [GitOps, rolling, blue/green and canary release architecture](../../v08-delivery-deployment-and-recovery/c04-gitops-rollout-and-progressive-delivery/gitops-canary-and-progressive-rollout.md#rolling-deployment) — rolling replacement and readiness are bounded; controller-specific surge math is platform-specific.

**Sources.** [src.k8s-deployments](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch5-k8s-deployment.2026-10-21: all 48 headings read.
The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Blue/Green Deployment; Canary Release; Feature Flags; Readiness
Probes.

### Blue-Green Deployment

**Identity.** Blue/Green Deployment; family Deployment and legacy modernization; kind
deployment-pattern; priority core.

**Decision question.** Should traffic switch between two complete environments rather than
replace in place?

**Good-fit conditions.** Two environments fit the cost; state is externalized or readable by
both versions; in-flight work can drain or route to both; switch/rollback is quick; data
compatibility is explicit.

**Hard contraindications.** Reject when duplicate capacity is prohibitive, when state
cannot be shared, or when a switch would lose in-flight work.

**Competing alternative.** Rolling deployment or canary. Reverse the choice when duplicate
environment cost exceeds rollback benefit.

**Failure and recovery.** Data compatibility and switch atomicity are common; verify state
in the owner section.

**Technical owner.** [GitOps, rolling, blue/green and canary release architecture](../../v08-delivery-deployment-and-recovery/c04-gitops-rollout-and-progressive-delivery/gitops-canary-and-progressive-rollout.md#blue-green-deployment) — traffic switch and rollback are bounded; infrastructure provisioning is platform-specific.

**Sources.** [src.argo-rollouts](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch5-argo-bluegreen.2026-10-21: all fifteen served headings
read. The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Rolling Deployment; Canary Release; Immutable Infrastructure;
Controlled Cutover.

### Canary Release

See the [dedicated Canary Release card](canary-release.md).

### Feature Flags-Feature Toggles

See the [dedicated Feature Flags-Feature Toggles card](feature-flags.md).

### GitOps

**Identity.** GitOps; family Deployment and legacy modernization; kind delivery-pattern;
priority core.

**Decision question.** Should desired state be versioned and reconciled automatically from
a Git source?

**Good-fit conditions.** Desired state is declarative and reviewed; reconciliation is
observable; secrets/drift are handled; rollback is a revert commit; repository write access and
commit signatures can be verified; reconciliation failure is monitored.

**Hard contraindications.** Reject when imperative one-off changes dominate, when the
reconciler is unowned, when secrets cannot be managed safely, or when desired-state revisions and
artifact references cannot be pinned and verified.

**Competing alternative.** Pipeline-driven deployment, a manual sync or imperative changes.
Argo CD records that automatic sync removes the pipeline's need for direct API access, that a
manual sync remains available, and that some imperativeness may stay outside Git; Flux documents a
registry-backed Gitless model. Reverse the choice when imperative changes dominate, the pipeline
already holds deployment authority, or no reconciler owner exists; that rule is Tycho synthesis.

**Failure and recovery.** Controller outage, drift, repository compromise and stale artifact
references are common. Argo CD and Flux document periodic reconciliation, OutOfSync state after a
successful sync, no retry against the same failed revision, rollback disabled under automated sync,
manifest caching and repository write trust; verify commit signatures, pin tags to commit SHAs or
digests, monitor reconciliation readiness, and revert the reviewed commit deliberately.

**Technical owner.** [GitOps](../../v08-delivery-deployment-and-recovery/c01-ci-cd-architecture-and-artifact-provenance/ci-cd-provenance-and-gitops.md#gitops) — GitOps is bounded to desired-state reconciliation.

**Sources.** [src.opengitops](../../../../edition/patterns/reading-ledger.v1.json)
retained record `read.batch5-opengitops.2026-10-21`; proposed 2026-11-01 records
`read.opengitops-principles`, `read.argocd-auto-sync`, `read.argocd-diffing`,
`read.argocd-best-practices`, `read.argocd-security`, `read.argocd-ha`, `read.flux-concepts`,
`read.flux-kustomization`, `read.flux-gitrepository` and `read.flux-monitoring` (all dated
2026-11-01). Public documentation, not a benchmark, cluster run, outage drill or
repository-compromise test.

**Decision state.** applicable-under-conditions.

**Related entries.** Immutable Infrastructure; Rolling Deployment; Feature Flags; CI/CD
Provenance.

### Immutable Infrastructure

See the [dedicated Immutable Infrastructure card](immutable-infrastructure.md).

### Strangler Fig

See the [dedicated Strangler Fig card](strangler-fig.md).

### Branch by Abstraction

**Identity.** Branch by Abstraction; family Deployment and legacy modernization; kind
modernization-pattern; priority core.

**Decision question.** Should an internal abstraction seam allow old/new implementations
to coexist in one deployable?

**Good-fit conditions.** The seam can be introduced without breaking callers; both
implementations preserve the same contract; removal date and reversible switch are owned.

**Hard contraindications.** Reject when no internal seam exists, when the abstraction adds
no substitution value, when the old implementation cannot coexist, or when data consistency
is involved.

**Competing alternative.** Strangler Fig, a façade or a parallel run. Reverse the choice
when abstraction cost exceeds incremental change benefit.

**Failure and recovery.** Keep each increment reversible and backward compatible, and use an
easily flipped switch so the team can return to the old functionality if problems appear. An
intermediate verification step that calls both new and old functionality can implement a
fallback. A named removal owner and date remain Tycho review conditions, not source claims.

**Technical owner.** [Branch by Abstraction](../../v10-decision-support-and-modernization/c05-target-architecture-versus-transition-states/cutover-gates.md#branch-by-abstraction) — branch by abstraction is bounded to internal interface replacement.

**Sources.** [src.fowler-branch](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch5-fowler-branch.2026-10-21: sections "Branch By Abstraction",
"Further Reading", "Acknowledgements", "Notes".
Failure and recovery also uses
[src.aws-branch](../../../../edition/patterns/reading-ledger.v1.json) read record
read.aws-branch.2026-10-29: the public AWS Prescriptive Guidance page "Branch by
abstraction pattern", accessed 2026-10-29; canonical text revision
`618648d7274e985f417915ecd4eeffe83e6c7db8b2ee1d0691293aee04f09d1c`.
The page supports reversible, backward-compatible increments, fallback verification,
switch-back recovery and the data-consistency limit.
The sources are public documentation/articles, not benchmarks.

**Decision state.** applicable-under-conditions.

**Related entries.** Strangler Fig; Parallel Run; Feature Flags; Controlled Cutover.

### Parallel Run

See the [dedicated Parallel Run card](parallel-run.md).

### Dark Launching / Shadow Traffic

See the [dedicated Dark Launching card](dark-launching.md).

### Expand-and-Contract

See the [dedicated Expand-and-Contract card](expand-and-contract.md).

### Controlled Cutover

See the [dedicated Controlled Cutover card](controlled-cutover.md).

## Chapter result and counterexample

Twelve cards establish a conditional decision route. Owner sections are bounded; none
establishes technical sufficiency.

Counterexample: a canary that receives no meaningful traffic is not evidence for the
canary card's analysis conditions.

## Navigation and prerequisites

- Parent: [V11](../README.md).
- Previous: [V11/C09](../c09-scalability/README.md).
- Next: [V11/C11](../c11-security-operations/README.md).
- Prerequisite: V10/C03 — pattern applicability and contraindications.
- Registry: [pattern registry](../../../../edition/patterns/registry.v1.json).
- Card batch: [card batches](../../../../edition/patterns/card-batches.v1.json).
- Coverage map: [candidate coverage](../../../../edition/patterns/coverage-map.v1.json).

## Evidence and known limits

- All 12 cards cite read ledger units; owner links and backlinks are self-checked.
- Owner links are bounded sections, not dedicated pattern pages.
- No entry claims sufficient technical or decision coverage.
- No independent editorial review, benchmark, production observation or runtime test
  is asserted.
