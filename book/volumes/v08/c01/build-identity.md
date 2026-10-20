---
metadata_version: 1
id: "tycho.page.faf8361106c2458b97e046319d7fa979"
kind: "page"
parent_id: "tycho.chapter.8a2d2a79846d4567bb3d33957e19977f"
canonical_path: "book/volumes/v08/c01/build-identity.md"
title: "Build boundaries and artifact identity"
topic_ids:
  - "software-delivery"
perspectives:
  - "architecture"
  - "operations"
summary: "Which source, runner and artifact evidence supports a reproducible release?"
route_hints:
  questions:
    - "Which source, runner and artifact evidence supports a reproducible release?"
  prerequisites:
    - "tycho.page.7921e82a71b9446790f185c818326911"
  related_ids:
    - "tycho.chapter.8a2d2a79846d4567bb3d33957e19977f"
    - "tycho.page.7921e82a71b9446790f185c818326911"
    - "tycho.page.6d05e9cca5a14d31a4637b8495ec0d05"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "build"
    - "identity"
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
# Build boundaries and artifact identity

**Owning question:** Which source, runner and artifact evidence supports a reproducible release?

This page belongs to [V08/C01 — CI/CD architecture and artifact provenance](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.7921e82a71b9446790f185c818326911:1 -->
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

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.7921e82a71b9446790f185c818326911:2 -->
## 2. Workflow and runner topology

A pipeline is a dependency DAG: compile/test/static checks can run in parallel when their inputs are isolated, but package publication must consume the **actual immutable outputs** of the required successful checks. An optional job cannot quietly satisfy a mandatory policy.

- **Untrusted contributions** must not obtain deployment identities or release signing material. Restrict jobs, workflow changes, protected environments, runner permissions and external network access.
- **Third-party workflow actions** should be pinned to full commit revisions. Official GitHub Actions secure-use guidance identifies full-length commit SHA pinning as the immutable reference mechanism for third-party actions. [E01]
- **Caching** accelerates builds but creates provenance ambiguity if cache contents, scope and validation are not defined. Verify dependency digests after retrieval and segregate cache keys across trust boundaries and toolchains.
- **Ephemeral runners** can reduce state persistence between jobs but depend on reliable bootstrap, approved base images and network/artifact access. Persistent runners require stronger cleanup and cross-job isolation.
- **Concurrency controls** should avoid contradictory promotions: serial release to a given environment or application version, explicit supersession rules and a verified candidate identity.
- **Human approvals** have to bind the exact artifact, target and configuration. Approving a run before a downstream job resolves a mutable tag is not equivalent to approving deployed bytes.

Record input revision, full toolchain/repository source identity, test scope, known skipped checks, output digest, source/target relationships and failed jobs. A job cancelled because of an external outage is **not a pass**.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.7921e82a71b9446790f185c818326911:3 -->
## 3. Provenance, reproducibility and signatures

SLSA v1.0 Build requirements describe producing provenance for identifiable build outputs; higher Build levels increase the controls against tampering and unreliable provenance. [E02] Treat SLSA as a versioned published specification, not as a label that proves any arbitrary pipeline conformant.

A consumer-side verification gate should test: the deployed package digest; expected builder identity; verified provenance signature/trust root; approved source revision and build recipe; approved dependency/source constraints; valid authorization for the target environment; key rotation/revocation policy; and expiration where appropriate.

A signed malicious artifact remains malicious. Build reproducibility allows byte comparison under equivalent inputs, but a reproducible vulnerability remains a vulnerability. Provenance about **how** bytes were built does not establish that the application meets its correctness/security requirements.

### SLSA version separation: Build v1.0 guidance versus Build/Source v1.2

This chapter's source ledger deliberately cites [SLSA v1.0 Build requirements](https://slsa.dev/spec/v1.0/requirements). The separately owned [release-verification chapter](../c02/sbom-attestation-and-release-verification.md) discusses [SLSA v1.2 Build Track Basics](https://slsa.dev/spec/v1.2/build-track-basics) and the version's **Source** track. Do not merge their level names into an undocumented universal `SLSA level`. In **v1.2**, Build L1 means provenance exists; Build L2 requires authenticity of provenance generated by a hosted build platform (typically signed); Build L3 adds hardened platform protections against build-time tampering. Source-level checks are a **different track**, not a substitute for Build L2/3.

**Original counterexample:** a pipeline outputs a signed JSON provenance record using a key accessible to arbitrary build steps. Calling it `SLSA Build L3` because a cryptographic signature verifies would ignore the hardened-builder key-isolation/tenant separation requirements. Conversely, genuine Build L3 provenance does not prove user authorization, domain correctness, old-client data compatibility or the resulting runtime's actual provenance-policy enforcement.

**Editorial verification requirement:** before stating compliance, pin the exact SLSA version, **track and level**, subject digest, builder identity, source dependencies, signing/trust-root mechanism and actual independent verification policy. This is **version-scoped research**, not evidence of any implemented SLSA level.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](ci-cd-provenance-and-gitops.md) |
| Next | [Continue the reasoning](promotion-rollout.md) |
| Integrated question | [Original scenario and limits](ci-cd-provenance-and-gitops.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.
