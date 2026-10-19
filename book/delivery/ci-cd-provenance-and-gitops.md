---
metadata_version: 1
id: "tycho.page.7921e82a71b9446790f185c818326911"
kind: "page"
parent_id: "tycho.landing.fe2eace7b2df4ae480adbdf844b68100"
canonical_path: "book/delivery/ci-cd-provenance-and-gitops.md"
title: "CI/CD architecture, artifact provenance and GitOps reconciliation"
topic_ids:
  - "software-delivery"
perspectives:
  - "architecture"
  - "operations"
summary: "Reader entry for CI/CD architecture, artifact provenance and GitOps reconciliation. Scope includes 1. Five separately controlled boundaries; Original delivery-flow diagram; 2. Workflow and runner topology."
route_hints:
  questions:
    - "What are the scope, mechanisms and limits of CI/CD architecture, artifact provenance and GitOps reconciliation?"
  prerequisites: []
  related_ids:
    - "tycho.page.81add4a0d86b4053ae77f9301fd2281d"
    - "tycho.page.1e89567050974052b13ba62b3b44484f"
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
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---

# CI/CD architecture, artifact provenance and GitOps reconciliation

> Tycho E14-10 [#88](https://github.com/rouslanbaranov/tycho/issues/88). Original technical chapter; official public sections inspected 2026-10-19. All examples are synthetic. No release, signature verification, compromise experiment or independent expert review has been performed.

## Purpose and mission

A passing build pipeline does not prove that the tested artifact was the one actually deployed, that its dependencies were trustworthy, or that the runtime remains compatible with durable state. This chapter separates **source identity, build execution, artifact identity, deployment authority and live acceptance**. Its decision question: how can a change be built, verified, promoted and reconciled without losing traceability or combining incompatible privileges?

The [companion migration chapter](progressive-delivery-and-schema-evolution.md) owns progressive release and schema compatibility; [safe rollout and recovery](safe-rollout-and-recovery.md) explains failures after attempted rollback.

## 1. Five separately controlled boundaries

| Boundary | Evidence identity | Success requires | A false inference |
|---|---|---|---|
| Source | Repo/commit, reviewed dependencies, accepted changes | Immutable reviewed revision and authorized inputs | A branch name is immutable |
| Build | Runner/build recipe/toolchain/dependency revisions | Bounded runner permissions, recorded inputs and test outputs | Green CI proves release safety |
| Artifact | Digest, package and build provenance | Tested object exactly matches published object | A mutable tag is sufficient |
| Promotion | Environment identity, approved artifact/config and authorizer | Exactly eligible digest and runtime/config version promoted | Signing alone authorizes deployment |
| Runtime acceptance | User outcomes, integrity checks, source revision and deployed digest | Measured service/data invariants at a named exposure | Reconciler reports Synced, therefore business succeeds |

An artifact signing key and a release credential are distinct authorities. A compromised runner with both may bypass intended separation even if source review succeeded.

### Original delivery-flow diagram

Source revision and dependency lock → isolated runner → tests and build → artifact digest plus provenance → verification/promotion gate → approved desired state → reconciler or controlled release → user/data health gate → accept or recover.

The flow is conceptual, not an assertion that any tool implements all steps or that failures cannot bypass a gate.

## 2. Workflow and runner topology

A pipeline is a dependency DAG: compile/test/static checks can run in parallel when their inputs are isolated, but package publication must consume the **actual immutable outputs** of the required successful checks. An optional job cannot quietly satisfy a mandatory policy.

- **Untrusted contributions** must not obtain deployment identities or release signing material. Restrict jobs, workflow changes, protected environments, runner permissions and external network access.
- **Third-party workflow actions** should be pinned to full commit revisions. Official GitHub Actions secure-use guidance identifies full-length commit SHA pinning as the immutable reference mechanism for third-party actions. [E01]
- **Caching** accelerates builds but creates provenance ambiguity if cache contents, scope and validation are not defined. Verify dependency digests after retrieval and segregate cache keys across trust boundaries and toolchains.
- **Ephemeral runners** can reduce state persistence between jobs but depend on reliable bootstrap, approved base images and network/artifact access. Persistent runners require stronger cleanup and cross-job isolation.
- **Concurrency controls** should avoid contradictory promotions: serial release to a given environment or application version, explicit supersession rules and a verified candidate identity.
- **Human approvals** have to bind the exact artifact, target and configuration. Approving a run before a downstream job resolves a mutable tag is not equivalent to approving deployed bytes.

Record input revision, full toolchain/repository source identity, test scope, known skipped checks, output digest, source/target relationships and failed jobs. A job cancelled because of an external outage is **not a pass**.

## 3. Provenance, reproducibility and signatures

SLSA v1.0 Build requirements describe producing provenance for identifiable build outputs; higher Build levels increase the controls against tampering and unreliable provenance. [E02] Treat SLSA as a versioned published specification, not as a label that proves any arbitrary pipeline conformant.

A consumer-side verification gate should test: the deployed package digest; expected builder identity; verified provenance signature/trust root; approved source revision and build recipe; approved dependency/source constraints; valid authorization for the target environment; key rotation/revocation policy; and expiration where appropriate.

A signed malicious artifact remains malicious. Build reproducibility allows byte comparison under equivalent inputs, but a reproducible vulnerability remains a vulnerability. Provenance about **how** bytes were built does not establish that the application meets its correctness/security requirements.

## 4. Direct push versus GitOps pull

In a push-style release, CI itself possesses credentials to mutate target runtime state. In GitOps, the desired configuration is versioned and a reconciler inside the target environment observes declared state and actual state, applying approved changes according to policy. OpenGitOps describes declarative, versioned, automatically pulled and continuously reconciled desired state. [E03]

Argo CD documents automated sync on differences between Git desired manifests and live resources; the CI job can update Git rather than use direct deployment API credentials. Pruning and self-healing are **separate controls** and can be disabled; enabling auto-sync does not mean all drift is repaired. [E04]

| Criterion | CI push | Reconciler pull |
|---|---|---|
| Deployment privilege | Held by release job or deployment actor | Held by reconciler under environment policy |
| Drift | May require separate monitoring/reapply | Detectable by reconciliation; correction depends on configuration |
| Candidate identity | Artifact plus release invocation | Desired-state Git revision plus artifact digest |
| Primary compromise concern | Build runner can become deployer | Desired-state repository/reconciler permission expands blast radius |
| Recovery | Explicit release/restore | Adjust desired state, verify controller won't undo emergency changes |
| Hidden complexity | Secret transport, manual drift and environment scripts | Controller lifecycle, sync ownership, prunes, loops and configuration precedence |

Argo CD's automated-sync documentation explicitly cautions that rollback cannot be performed while automated sync is enabled. Recovery procedures must coordinate with desired-state reconciliation, not create opposing control loops. [E04]

A resource declared healthy does not prove the application honors its data, availability or user-journey invariants.

## 5. Progressive promotion and stop conditions

Promotion is a conditional authorization to expose an approved artifact at a **named workload and data-compatibility boundary**, not just a command to scale replicas. Before exposure, prove candidate identity, rollback/forward-repair availability, data/read compatibility, representative readiness, downstream capacity, required security policy and measured SLIs.

Stop promotion when: p99 or client errors breach a stated gate with adequate sample; a business invariant fails; auth is broken; queue/connection budgets saturate; release identity mismatches the validated digest; or a source/evidence gap prevents an irreversible step. A too-small canary cannot prove absence of rare corruption.

The narrower runtime mechanisms are explained in [progressive delivery and schema evolution](progressive-delivery-and-schema-evolution.md), rather than repeating Kubernetes controller documentation here.

## 6. Failure matrix and discriminating checks

| Failure or abuse | Superficial symptom | Required action |
|---|---|---|
| Cached untrusted dependency | Reused green build | Pin/verify dependencies, invalidate cache and rebuild under known inputs |
| Tag points to different image | Runtime may appear ready | Compare actual digest to the digest that passed gates; freeze promotion |
| Overbroad runner permissions | Source/test checks still pass | Separate build credentials from release authority; review provenance and rotate compromised credentials |
| Reconciler stuck or racing an emergency change | CI reports published | Inspect reconciliation history, freeze conflicting automation, assess actual resource state |
| Release rolled back after incompatible writes | Older image becomes ready | Check old-version read compatibility before routing users; choose forward repair if needed |
| Signing service unavailable | Build completes | Use authorized verification/recovery policy, never accept unsigned artifacts by default |

## 7. Architecture decision and evidence boundary

Prefer the simplest delivery chain that can independently demonstrate source identity, artifact integrity, release authorization and runtime correctness. GitOps is useful where persistent configuration drift and deployment-credential separation matter; a separate reconciler is not automatically justified for every static deployment.

**No-go:** if the released digest or the old/new data compatibility is unknown, do not infer safety from a green CI or synchronized resources. The next step is a bounded reproduction: build from an exact source revision, verify digest/provenance, promote to an isolated environment, simulate a failed release and observe business-level outcomes.

| Evidence ID | Official public source, inspected scope | What it does NOT establish |
|---|---|---|
| E01 | [GitHub Actions secure-use](https://docs.github.com/en/actions/reference/security/secure-use), section on pinning to a full commit SHA | No Tycho runner configuration or permission audit was executed |
| E02 | [SLSA v1.0 Producing Artifacts](https://slsa.dev/spec/v1.0/requirements), provenance generation and distribution; [SLSA levels](https://slsa.dev/spec/v1.0/levels) | No achieved build trust level, artifact signing or observed integrity test |
| E03 | [OpenGitOps principles](https://opengitops.dev/), four declarative/pulled/reconciled principles | No specific reconciler's behavior independently tested |
| E04 | [Argo CD Automated Sync Policy](https://argo-cd.readthedocs.io/en/stable/user-guide/auto_sync/), automated sync, prune, self-heal and rollback notes | Depends on actual installed version/policy; no production behavior inferred |

All diagrams, recommendations and failure cases in this chapter are conceptual. No pipeline, signer, reconciler, live environment or recovery drill has been executed, and no independent domain review is claimed.
