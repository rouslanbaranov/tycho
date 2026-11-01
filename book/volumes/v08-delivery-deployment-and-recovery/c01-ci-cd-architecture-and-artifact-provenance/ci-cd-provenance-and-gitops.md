---
metadata_version: 1
id: "tycho.page.7921e82a71b9446790f185c818326911"
kind: "page"
parent_id: "tycho.chapter.8a2d2a79846d4567bb3d33957e19977f"
canonical_path: "book/volumes/v08-delivery-deployment-and-recovery/c01-ci-cd-architecture-and-artifact-provenance/ci-cd-provenance-and-gitops.md"
title: "CI/CD architecture, artifact provenance and GitOps reconciliation"
topic_ids:
  - "software-delivery"
perspectives:
  - "architecture"
  - "operations"
summary: "Integrated question, original scenario and transfer limits for CI/CD architecture and artifact provenance. Detailed mechanisms have separate question owners."
route_hints:
  questions:
    - "Which boundaries separate build, test, publication and production deployment?"
  prerequisites: []
  related_ids:
    - "tycho.page.81add4a0d86b4053ae77f9301fd2281d"
    - "tycho.page.1e89567050974052b13ba62b3b44484f"
    - "tycho.page.faf8361106c2458b97e046319d7fa979"
    - "tycho.page.6d05e9cca5a14d31a4637b8495ec0d05"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "CI/CD"
    - "architecture"
    - "artifact"
    - "provenance"
    - "and"
    - "GitOps"
    - "reconciliation"
evidence_scope:
  source_ids:
    - "src.opengitops"
  claim_ids: []
  status: "source-linked"
  notes: "Only exact URL matches to the global source register are normalized here. Page-local case and evidence ledger IDs remain in the body; no claim-level mapping or source inspection is inferred."
content_review:
  status: "draft"
  reviewed_at: null
  reviewer: null
  proof_uri: null
authored_at: "2026-10-19"
updated_at: "2026-11-01"
source_inspection_date: null
content_verified_at: null
---
<!-- tycho-question-source:tycho.page.7921e82a71b9446790f185c818326911:-1 -->

# CI/CD architecture, artifact provenance and GitOps reconciliation

> Tycho E14-10 [#88](https://github.com/rouslanbaranov/tycho/issues/88). Original technical chapter; official public sections inspected 2026-10-19. All examples are synthetic. No release, signature verification, compromise experiment or independent expert review has been performed.
>
> The content_review field retains the decomposition-era draft state; no independent
> acceptance is asserted.

<!-- /tycho-question-source -->

> **Pattern atlas:**
> [GitOps](../../v11-pattern-atlas/c10-deployment-modernization/README.md#gitops) — decision conditions and contraindications.

<!-- tycho-question-source:tycho.page.7921e82a71b9446790f185c818326911:0 -->
## Purpose and mission

A passing build pipeline does not prove that the tested artifact was the one actually deployed, that its dependencies were trustworthy, or that the runtime remains compatible with durable state. This chapter separates **source identity, build execution, artifact identity, deployment authority and live acceptance**. Its decision question: how can a change be built, verified, promoted and reconciled without losing traceability or combining incompatible privileges?

The [companion migration chapter](../../../delivery/progressive-delivery-and-schema-evolution.md) owns progressive release and schema compatibility; [safe rollout and recovery](../../../delivery/safe-rollout-and-recovery.md) explains failures after attempted rollback.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.7921e82a71b9446790f185c818326911:8 -->
## Engineering walkthrough — Compromised build worker and a tempting image rollback

**Original hypothetical attack/failure:** a pipeline resolves the correct source revision but runs on a compromised shared worker. The worker produces an artifact with unexpected bytes and a generated signature from a key available to that same compromised job. A signed artifact can still be unauthorized if builder identity, key policy or provenance verification is wrong. An image-only rollback may additionally be incompatible with durable schema writes.

| Gate | Required independent trust decision | Negative case |
|---|---|---|
| Source admission | Authorized repository/ref, protected change approvals | Build uses an unreviewed transient ref |
| Build provenance | Builder identity, materials, invocation and output digest within declared trust model | Artifact digest is unrelated to verified source/approved workflow |
| Deployment admission | Verify exact digest, environment, approved provenance and signer constraints | Any valid signature is allowed regardless of key policy |
| Runtime rollback | Check old-reader compatibility and previously committed new effects | Controller restores an old image that cannot decode stored data |

Direct push gives the build system deployment credentials; a GitOps pull/reconcile controller can separate rights but still needs strong trust in desired configuration and artifact references. Neither removes the need for live operational authorization, business outcome checks and restore drills. The current GitHub Actions security, SLSA and OpenGitOps references describe bounded controls, not this invented attack's observed outcome.

**GitOps mechanism.** Desired state is stored in a versioned repository; a reconciler pulls
it, compares the live state and applies the difference. Rollout and rollback are commits to
that state, not ad hoc commands. The artifact reference, admission policy and credentials
must be reviewed with the desired state.

**Invariant and failure.** The reconciled commit must be the reviewed desired state; drift is
detected rather than silently overwritten, and the controller has least-privilege access.
Controller outage, drift, a compromised repository and stale artifact references are common.
Reconcile deliberately, revert the reviewed commit, rotate credentials and alert on drift.
Direct push/CD or an imperative platform operator may be preferable when a separate pull
controller adds more operational surface than it removes.

**Proposed verification, not executed:** replace one artifact digest, simulate a compromised ephemeral worker, submit an otherwise valid signature from an untrusted key, then attempt rollback after a new-only schema write. Confirm deterministic rejection or forward repair rather than relying on a green pipeline. The final decision must account for who can approve a deployment, how credentials are scoped, and whether maintaining a separate pull controller is proportionate to the team's threat model.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.7921e82a71b9446790f185c818326911:9 -->
## Applied M9 evidence: what transfers and what does not

These examples connect the chapter's conditional mechanism to published experiences or synthetic decision exercises. A historical company report is **first-party, time-scoped evidence**, not a controlled Tycho benchmark; an M9 decision playbook is **original synthetic analysis**, not a company decision.

**Case lens — [Airbnb — Bazel JVM build migration](../../../cases/airbnb-jvm-monorepo-bazel.md)**. **Relevant mechanism or architectural contrast:** Build-system coexistence and controlled migration are engineering work separate from selecting Bazel. **Not established by this report/playbook:** Airbnb's historical premerge times and build improvements are not a transferable benchmark or proof every polyrepo needs Bazel.

**Transfer test:** before applying the lesson to another legacy system, identify the exact workload, source date, relevant runtime/protocol versions, state authority, failure/recovery gate and the new observation that would reverse the choice. Follow the case's public evidence ledger rather than treating its link as independent proof.
<!-- /tycho-question-source -->

## Integrated decision and reading route

Keep source revision, build identity, artifact digest, promotion and user-health acceptance as separate release boundaries.

A successful pipeline run does not prove that the intended artifact was deployed or that its persisted effects remain correct.

The detailed pages separate the mechanisms that make this decision conditional:

- [Build boundaries and artifact identity](build-identity.md) — Which source, runner and artifact evidence supports a reproducible release?
- [Promotion, reconciliation and user-health gates](promotion-rollout.md) — Which failure and authority boundaries separate deployment from accepted release?

[Chapter introduction, ordered pages and full source ledger](README.md). Original source labels retain their historical scope; this editorial decomposition does not turn proposed experiments into executed evidence.

## Bounded pattern ownership notes

### GitOps

GitOps treats a versioned desired-state repository as reviewed intent. OpenGitOps requires desired
state "expressed declaratively" and "stored in a way that enforces immutability, versioning", pulled
by agents that "automatically pull the desired state declarations from the source" and "continuously
observe actual system state and attempt to apply the desired state" (OpenGitOps — Principles
v1.0.0). Argo CD compares "the desired manifests in Git" with "the live state in the cluster" (Argo
CD — Automated Sync Policy); Flux describes an automated process that "ensures that the deployed
environment matches the state specified in one or more Git repositories" (Flux — Core Concepts). The
reconciler records the observed revision; the repository is neither a build log nor a credentials
store.

Rollback is a revert commit, which needs a linear, reviewable history and an immutable artifact
reference. Pin image digests and verify the commit signature: Argo CD warns that "gaining
unauthorized write access to a git repository trusted by Argo CD will have serious security
implications" (Argo CD — Security), and Flux can enable "the verification of Git commit signatures"
against keys of "trusted Git authors" (Flux — GitRepository). Secrets stay out of plaintext: use an
external secret reference or sealed value that the controller can resolve with least privilege.

**Failure and recovery (Tycho synthesis).** Controller outage, drift, repository compromise and
stale artifact references are the common failures: reconciliation is periodic and controller-driven,
a green sync does not prove convergence, failed syncs are not retried against the same revision, and
a trusted repository is a deployment path. Argo CD polls Git "every 3m by default" (Argo CD — High
Availability) and Flux reconciles "every five minutes by default" (Flux — Core Concepts), so an
unavailable controller stops convergence while workloads keep serving. "It is possible for an
application to be OutOfSync even immediately after a successful Sync operation", for example because
"A controller or mutating webhook is altering the object after it was submitted to Kubernetes" (Argo
CD — Diffing Customization); Flux warns that direct `kubectl` edits "will be promptly reverted"
(Flux — Core Concepts). Recovery is constrained: "Automatic sync will not reattempt a sync if the
previous sync attempt against the same commit-SHA and parameters had failed", and "Rollback cannot
be performed against an application with automated sync enabled" (Argo CD — Automated Sync Policy),
so the reviewed commit must be reverted deliberately. Repository compromise is a deployment path: an
attacker with "access to a trusted git repo" can "update the deployment manifest deploy malicious
container images" or "delete resources in git causing them to be pruned in the live environment"
(Argo CD — Security). Stale references survive caching and remote bases: Argo CD "caches the
generated manifests (for 24h by default)" and "the expected manifests can change even though the
repo has not changed" when a Kustomize remote base or an unversioned Helm chart moves (Argo CD —
High Availability); pin "a Git tag or commit SHA" rather than a moving base (Argo CD — Best
Practices). Alert on reconciliation failure instead of assuming convergence: Flux's monitoring example
uses `gotk_resource_info`, whose `ready` label "shows the readiness of the resource" (Flux —
Prometheus metrics). Verify commit signatures, pin tags and digests, keep secrets external, and name a drift
owner. The controller-outage consequence and this runbook are Tycho guidance; the selected pages
document periodic reconciliation, caching and repository trust, not an outage drill.

**Alternative (Tycho comparison).** A pipeline that applies directly remains a valid deployment
model, a manual sync remains available for pruning, and an imperative change is sometimes
deliberate: Argo CD's benefit is that "CI/CD pipelines no longer need direct access to the Argo CD
API server to perform the deployment", because "the pipeline makes a commit and push to the Git
repository" instead (Argo CD — Automated Sync Policy). Argo CD's guidance says "It may be desired to
leave room for some imperativeness/automation, and not have everything defined in your Git
manifests" (Argo CD — Best Practices). Flux also documents a "Gitless GitOps" model whose
controllers are "fully decoupled from Git" and use container registries as the source of truth (Flux
— Core Concepts). These alternatives are preferable when imperative one-off changes dominate, when
the pipeline already holds deployment authority, or when no reconciler owner exists; that selection
rule is Tycho guidance, not a source claim. GitOps fits when the environment can be reconciled from
a reviewable repository.

**Sources and limits.** Proposed 2026-11-01 records bind OpenGitOps *GitOps Principles v1.0.0* (tag
`v1.0.0`); Argo CD *Automated Sync Policy*, *Diffing Customization*, *Best Practices*, *Security*
and *High Availability* read through the moving `stable` alias; and Flux *Core Concepts*,
*Kustomization*, *GitRepository* and *Prometheus metrics*. Read records:
`read.opengitops-principles.2026-11-01`, `read.argocd-auto-sync.2026-11-01`,
`read.argocd-diffing.2026-11-01`, `read.argocd-best-practices.2026-11-01`,
`read.argocd-security.2026-11-01`, `read.argocd-ha.2026-11-01`, `read.flux-concepts.2026-11-01`,
`read.flux-kustomization.2026-11-01`, `read.flux-gitrepository.2026-11-01` and
`read.flux-monitoring.2026-11-01`. The four failure modes, the controller-outage consequence and the
selection rule are Tycho synthesis; no reconciler, cluster, outage or compromised repository was
exercised, and no independent review is claimed.
