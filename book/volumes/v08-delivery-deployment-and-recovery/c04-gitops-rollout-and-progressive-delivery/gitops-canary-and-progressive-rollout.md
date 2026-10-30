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
updated_at: "2026-10-30"
source_inspection_date: null
content_verified_at: null
---
<!-- tycho-question-source:tycho.page.b938ff1a06264492a425f2eff555ae7d:-1 -->

# GitOps, rolling, blue/green and canary release architecture

> **Independent Tycho V08/C04 manuscript**, 2026-10-19. Public Kubernetes Deployment and Argo Rollouts documentation informs controller mechanisms. All rollout examples, diagrams and acceptance criteria are original hypotheticals; no cluster, deployment, pipeline, experiment or external review was executed. Prior [mixed rollout/schema research](../../../delivery/progressive-delivery-and-schema-evolution.md) is preserved for editorial mapping.
>
> The content_review field retains the decomposition-era draft state; no independent
> acceptance is asserted.

<!-- /tycho-question-source -->

> **Pattern atlas:**
> [Rolling Deployment](../../v11-pattern-atlas/c10-deployment-modernization/README.md#rolling-deployment) — decision conditions and contraindications.
> [Blue/Green Deployment](../../v11-pattern-atlas/c10-deployment-modernization/README.md#blue-green-deployment) — decision conditions and contraindications.
> [Canary Release](../../v11-pattern-atlas/c10-deployment-modernization/README.md#canary-release) — decision conditions and contraindications.
> [Dark Launching / Shadow Traffic](../../v11-pattern-atlas/c10-deployment-modernization/dark-launching.md#dark-launching--shadow-traffic) — decision conditions and contraindications.

<!-- tycho-question-source:tycho.page.b938ff1a06264492a425f2eff555ae7d:0 -->
## Purpose and mission

A release mechanism decides which version is **deployed and exposed**. It does not by itself prove which data, users or business effects each version can safely interpret. Progressive deployment can limit a failure's initial blast radius, but cannot prevent a small canary from writing incompatible shared state used by every older instance.

**Canary mechanism.** Route a small, identifiable cohort to the new version, compare its
SLIs with a baseline, then expand or abort. It needs exposure control, a representative
cohort, measurable gates and a rollback/forward-repair decision. The exposure slice is not a
data-compatibility boundary: a canary can write state that older instances cannot read.

**Failure and recovery.** Small samples hide rare errors, the canary can contaminate shared
state, and a binary rollback does not undo committed data. Stop expansion, drain the cohort,
inspect the shared-state effect and reconcile before resuming. Blue/green, shadow traffic or
a feature flag may be preferable when a canary cannot isolate users or state.

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
not the main subject of this page. They are synthetic design guidance unless a
sentence explicitly attributes the claim to a dedicated source record; all other
guidance remains synthetic. They are not measured evidence and do not create a new
source claim by themselves.

### Dark Launching-Shadow Traffic

See the [dedicated Dark Launching-Shadow Traffic owner note](dark-launching-shadow-traffic.md).

### Rolling Deployment

A rolling deployment replaces instances in batches, so old and new versions serve traffic together
during the rollout. Both versions must be compatible with the shared data and contracts for the
whole overlap, or the rollout must stop before an incompatible state is written.

Mixed versions expose an incompatibility that a single-version test missed; gate each batch on
readiness and error signals and keep a tested stop condition. Blue/green switches a complete
environment at once; choose rolling when the extra capacity for a second environment is unavailable.
Before the first batch, define the drain window and the rollback gate: a failed batch must be
replaceable without replacing the whole fleet. Recreate is an alternative when a brief full outage
is acceptable and mixed versions cannot coexist.

**Limits.** Batch size, drain time and mixed-version compatibility are costs; a rolling rollout
cannot prove a new-only write is reversible. Capacity during the overlap must be budgeted,
and a canary analysis does not replace this overlap check.

### Blue-Green Deployment

Blue/green runs two complete environments and switches traffic at a routing boundary, leaving the
previous environment available for a short reversal. The switch must remain reversible until the new
version's persisted effects are proven compatible with the old version.

A half-switched route or a new-only write makes reversal unsafe; verify routing completeness and
data compatibility before declaring the cutover. State must be externalized or readable by both
versions, and in-flight work must drain or route to both; a switch that drops in-flight work is not
reversible. A rolling or canary rollout uses less spare
capacity; choose blue/green when a fast, complete reversal and a clean environment comparison
justify the double capacity.

**Limits.** Double capacity, data compatibility and switch atomicity are costs; a routing switch
does not roll back persisted effects. Test the reverse switch under load, give the old
environment an owner and expiry, and treat a rehearsed reverse switch as acceptance evidence.

### Canary Release

Route a small, identifiable cohort to the new version and check that it is representative;
compare its SLIs with a baseline over a window long enough to expose rare errors, then expand or
abort. The cohort, window and abort threshold are the release contract.

The exposure slice is not a data-compatibility boundary. That separation is Tycho guidance,
not a source rule: Google SRE notes that "the canary population and the control may share
backends, frontends, networks, data stores, and other infrastructure," and AWS requires both
blue and green environments to use "up-to-date data" with schema updates that stay "backward
compatible" for the old version. A canary that writes through a shared store can therefore
leave state the baseline cannot read; that consequence is Tycho's inference, and rollback does
not undo committed data. Tycho guidance, not a source claim: watch metric leakage across cohorts and sample size;
small samples hide rare errors, and an unrepresentative cohort can pass while a rare failure
hides. Shared-state contamination is the source-backed risk described above.

Traffic mirroring is safe only when requests are idempotent or can be processed twice:
Flagger says mirroring "should be used for requests that are idempotent or capable of being
processed twice" and warns that a write may be "duplicated and handled by the primary and
canary." Treat reads-only mirroring as the safe default; suppressing writes is Tycho
guidance, not a Flagger requirement. AWS's blue/green account shares the data stores
rather than moving them: both environments need "up-to-date data," and schema updates must
be "backward compatible." Google SRE describes feature flags that "separate feature
launches from binary releases," so activation can be scoped without a second environment;
that no-second-copy comparison is Tycho guidance. Google SRE also notes that blue/green uses
"twice as many resources as a more traditional deployment," a cost the canary comparison must
include. A rolling deployment replaces instances
in batches without a separate cohort, and Argo notes that a canary without steps "will
mimic the rolling update behavior." Choosing among these is Tycho guidance; use an
alternative when the canary cohort cannot be isolated.

Canary is a fit when traffic can be split safely and the SLI comparison has enough signal and an
owner.

**Source boundary.**

- Argo Rollouts `read.batch5-argo-canary.2026-10-21`, raw HTML
  `925398c1c97a8e700b22ec0354648ae6240b405d73e219f2f3e5ffc286c982e7`:
  canary steps, analysis abort and the rolling mimic.
- Flagger `read.flagger-deployment-strategies.2026-10-30`, raw Markdown
  `2d57c5d5bd950da50cf3fc73e1aff83f84981959e544cd8a40cc25c97d66b745`:
  canary, A/B, blue/green and mirroring; mirroring idempotency.
- Google SRE `read.sre-workbook-canarying.2026-10-30`, raw HTML
  `2129ec6fefdb7807073a7877344e7f0409c27e4fde1021d30114a38338fd039f`:
  shared infrastructure, stateful teeing limits, feature flags and blue/green
  resource cost.
- AWS `read.aws-blue-green-data.2026-10-30`, raw HTML
  `07eaa6ff45ca86872f743c07deb17577761f1216e04a840de89ae9c5bfa99442`:
  shared data stores and backward-compatible schema changes.
- Limits: none of these pages tests a canary against an incompatible schema;
  the data-compatibility separation and the reads-only mirroring rule are Tycho
  guidance built from the quoted passages.
