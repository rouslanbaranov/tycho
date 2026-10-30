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
    - "src.hashicorp-immutable-vms"
  claim_ids: []
  status: "source-linked"
  notes: "12 cards cite read units; owner links are bounded."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-30"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-21"
updated_at: "2026-10-30"
source_inspection_date: "2026-10-30"
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

**Identity.** Feature Flags / Feature Toggles; family Deployment and legacy modernization;
kind deployment-pattern; priority core.

**Decision question.** Should activation be decoupled from deployment through a runtime
toggle?

**Good-fit conditions.** Toggle ownership, expiry, scope and kill switch are defined; the
default fails safe; flag evaluation is observable.

**Hard contraindications.** Reject when a toggle would become permanent configuration
debt, when no owner removes it, or when it hides a broken deployment.

**Competing alternative.** Deploy dark code with no toggle or a separate release train.
Reverse the choice when toggle lifecycle cost exceeds decoupling benefit.

**Failure and recovery.** Stale snapshots, flag interactions, permanent flags and
unauthorized overrides are common; audit changes, expire flags and bound snapshot age.

**Technical owner.** [Feature Flags / Feature Toggles](../../v08-delivery-deployment-and-recovery/c04-gitops-rollout-and-progressive-delivery/configuration-rollout.md#feature-flags-feature-toggles) — flags are bounded, not a full toggle-lifecycle platform.

**Sources.**
[src.fowler-feature-toggles](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch5-fowler-feature-toggles.2026-10-21: all seven top-level sections
and 40 headings read. The source is a public
pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Canary Release; Dark Launching; GitOps; Configuration Rollout.

### GitOps

**Identity.** GitOps; family Deployment and legacy modernization; kind delivery-pattern;
priority core.

**Decision question.** Should desired state be versioned and reconciled automatically from
a Git source?

**Good-fit conditions.** Desired state is declarative and reviewed; reconciliation is
observable; secrets/drift are handled; rollback is a revert commit.

**Hard contraindications.** Reject when imperative one-off changes dominate, when the
reconciler is unowned, or when secrets cannot be managed safely.

**Competing alternative.** Pipeline-driven deployment or manual release. Reverse the
choice when reconciliation latency/ownership exceeds audit benefit.

**Failure and recovery.** Drift, controller outage, a compromised repository and stale
artifact references are common; alert on drift, revert reviewed commits and scope credentials.

**Technical owner.** [GitOps](../../v08-delivery-deployment-and-recovery/c01-ci-cd-architecture-and-artifact-provenance/ci-cd-provenance-and-gitops.md#gitops) — GitOps is bounded to desired-state reconciliation.

**Sources.** [src.opengitops](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch5-opengitops.2026-10-21: all seven served headings read. The source
is a public pattern/documentation
unit, not a benchmark.

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

**Identity.** Expand-and-Contract; family Deployment and legacy modernization; kind
migration-pattern; priority core.

**Decision question.** Should a schema change be rolled out in expand, migrate and
contract stages?

**Good-fit conditions.** Old/new readers coexist; compatibility window is owned;
backfill/validation are explicit.

**Hard contraindications.** Reject when downtime is acceptable and a direct migration is
simpler, when no compatibility window exists, or when rollback is impossible.

**Competing alternative.** Big-bang migration, parallel run or versioned API cutover.
Reverse when no compatibility window is possible or the dataset is small enough to pause.

**Failure and recovery.** Partial backfills and old readers are common; verify gates in
the owner section.

**Technical owner.** [Expand-and-Contract](../../v08-delivery-deployment-and-recovery/c05-backward-compatible-database-change/reader-writer-matrix.md#expand-and-contract) — expand/contract is bounded to reader/writer compatibility.

**Sources.** [src.flyway](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch3-flyway.2026-10-21: all seventeen served headings read.
The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Online Data Migration; Controlled Cutover; Reader/Writer
Compatibility; Backup/PITR.

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
