---
metadata_version: 1
id: "tycho.page.7921e82a71b9446790f185c818326911"
kind: "page"
parent_id: "tycho.chapter.8a2d2a79846d4567bb3d33957e19977f"
canonical_path: "book/volumes/v08/c01/ci-cd-provenance-and-gitops.md"
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
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---
<!-- tycho-question-source:tycho.page.7921e82a71b9446790f185c818326911:-1 -->

# CI/CD architecture, artifact provenance and GitOps reconciliation

> Tycho E14-10 [#88](https://github.com/rouslanbaranov/tycho/issues/88). Original technical chapter; official public sections inspected 2026-10-19. All examples are synthetic. No release, signature verification, compromise experiment or independent expert review has been performed.

<!-- /tycho-question-source -->
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
