---
metadata_version: 1
id: "tycho.page.49052c97325309f3830419b2290e521f"
kind: "page"
parent_id: "tycho.chapter.dabaea8f5ab426edc08683ceec89c2c0"
canonical_path: >-
  book/volumes/v11-pattern-atlas/c10-deployment-modernization/gitops.md
title: "GitOps"
topic_ids:
  - "deployment-architecture"
  - "software-delivery"
perspectives:
  - "architecture"
  - "operations"
summary: >-
  Decision card for GitOps; source-anchored on OpenGitOps principles v1.0.0,
  Argo CD reconciliation, drift, security and availability, and Flux concepts,
  drift, verification and monitoring; coverage remains partial-bounded, no
  promotion.
route_hints:
  questions:
    - >-
      Should desired state be versioned and reconciled automatically from a Git
      source?
  prerequisites:
    - "tycho.chapter.dabaea8f5ab426edc08683ceec89c2c0"
  related_ids:
    - "tycho.chapter.dabaea8f5ab426edc08683ceec89c2c0"
  excludes:
    - >-
      No sufficient coverage, promotion or owner acceptance is claimed for this
      moved page.
  keywords:
    - "pattern atlas"
    - "gitops"
    - "deployment and legacy modernization"
evidence_scope:
  source_ids:
    - "src.opengitops"
    - "src.argocd"
    - "src.flux"
  claim_ids: []
  status: "source-linked"
  notes: >-
    Card cites read.opengitops-principles.2026-11-01,
    read.argocd-auto-sync.2026-11-01, read.argocd-diffing.2026-11-01,
    read.argocd-best-practices.2026-11-01, read.argocd-security.2026-11-01,
    read.argocd-ha.2026-11-01, read.flux-concepts.2026-11-01,
    read.flux-kustomization.2026-11-01, read.flux-gitrepository.2026-11-01 and
    read.flux-monitoring.2026-11-01; read.batch5-opengitops.2026-10-21 is
    retained historical context; owner section and limits are bounded.
content_review:
  status: "self-checked"
  reviewed_at: "2026-11-01"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-11-01"
updated_at: "2026-11-01"
source_inspection_date: "2026-11-01"
content_verified_at: null
---
# GitOps

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
read records `read.opengitops-principles.2026-11-01`;
[src.argocd](../../../../edition/patterns/reading-ledger.v1.json) read
records `read.argocd-auto-sync.2026-11-01`,
`read.argocd-diffing.2026-11-01`,
`read.argocd-best-practices.2026-11-01`,
`read.argocd-security.2026-11-01` and `read.argocd-ha.2026-11-01`;
[src.flux](../../../../edition/patterns/reading-ledger.v1.json) read
records `read.flux-concepts.2026-11-01`,
`read.flux-kustomization.2026-11-01`,
`read.flux-gitrepository.2026-11-01` and
`read.flux-monitoring.2026-11-01`.
`read.batch5-opengitops.2026-10-21` is retained historical context.
Public documentation, not a benchmark, cluster run, outage drill or
repository-compromise test.

**Decision state.** applicable-under-conditions.

**Related entries.** Immutable Infrastructure; Rolling Deployment; Feature Flags; CI/CD
Provenance.

**Limits.** Coverage is partial-bounded and self-checked, not independent review,
promotion or owner acceptance. The controller-outage consequence and the
selection rule are Tycho synthesis; no reconciler, cluster, outage or
compromised repository was exercised.
