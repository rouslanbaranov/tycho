---
metadata_version: 1
id: "tycho.page.6d05e9cca5a14d31a4637b8495ec0d05"
kind: "page"
parent_id: "tycho.chapter.8a2d2a79846d4567bb3d33957e19977f"
canonical_path: "book/volumes/v08-delivery-deployment-and-recovery/c01-ci-cd-architecture-and-artifact-provenance/promotion-rollout.md"
title: "Promotion, reconciliation and user-health gates"
topic_ids:
  - "software-delivery"
perspectives:
  - "architecture"
  - "operations"
summary: "Which failure and authority boundaries separate deployment from accepted release?"
route_hints:
  questions:
    - "Which failure and authority boundaries separate deployment from accepted release?"
  prerequisites:
    - "tycho.page.faf8361106c2458b97e046319d7fa979"
  related_ids:
    - "tycho.chapter.8a2d2a79846d4567bb3d33957e19977f"
    - "tycho.page.7921e82a71b9446790f185c818326911"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "promotion"
    - "rollout"
evidence_scope:
  source_ids:
    - "src.opengitops"
  claim_ids: []
  status: "source-linked"
  notes: "Bounded question from tycho.page.7921e82a71b9446790f185c818326911; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
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
# Promotion, reconciliation and user-health gates

**Owning question:** Which failure and authority boundaries separate deployment from accepted release?

This page belongs to [V08/C01 — CI/CD architecture and artifact provenance](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.7921e82a71b9446790f185c818326911:4 -->
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

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.7921e82a71b9446790f185c818326911:5 -->
## 5. Progressive promotion and stop conditions

Promotion is a conditional authorization to expose an approved artifact at a **named workload and data-compatibility boundary**, not just a command to scale replicas. Before exposure, prove candidate identity, rollback/forward-repair availability, data/read compatibility, representative readiness, downstream capacity, required security policy and measured SLIs.

Stop promotion when: p99 or client errors breach a stated gate with adequate sample; a business invariant fails; auth is broken; queue/connection budgets saturate; release identity mismatches the validated digest; or a source/evidence gap prevents an irreversible step. A too-small canary cannot prove absence of rare corruption.

The narrower runtime mechanisms are explained in [progressive delivery and schema evolution](../../../delivery/progressive-delivery-and-schema-evolution.md), rather than repeating Kubernetes controller documentation here.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.7921e82a71b9446790f185c818326911:6 -->
## 6. Failure matrix and discriminating checks

| Failure or abuse | Superficial symptom | Required action |
|---|---|---|
| Cached untrusted dependency | Reused green build | Pin/verify dependencies, invalidate cache and rebuild under known inputs |
| Tag points to different image | Runtime may appear ready | Compare actual digest to the digest that passed gates; freeze promotion |
| Overbroad runner permissions | Source/test checks still pass | Separate build credentials from release authority; review provenance and rotate compromised credentials |
| Reconciler stuck or racing an emergency change | CI reports published | Inspect reconciliation history, freeze conflicting automation, assess actual resource state |
| Release rolled back after incompatible writes | Older image becomes ready | Check old-version read compatibility before routing users; choose forward repair if needed |
| Signing service unavailable | Build completes | Use authorized verification/recovery policy, never accept unsigned artifacts by default |

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.7921e82a71b9446790f185c818326911:7 -->
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

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Source map | [Chapter source index](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](build-identity.md) |
| Next | [Continue the reasoning](README.md) |
| Integrated question | [Original scenario and limits](ci-cd-provenance-and-gitops.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.
