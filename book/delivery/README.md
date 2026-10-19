---
metadata_version: 1
id: "tycho.landing.fe2eace7b2df4ae480adbdf844b68100"
kind: "landing"
parent_id: "tycho.book.37c50125355948f1b52ec66229ef59bd"
canonical_path: "book/delivery/README.md"
title: "Delivery pipelines, progressive releases and schema evolution"
topic_ids:
  - "software-delivery"
perspectives:
  - "architecture"
  - "operations"
summary: "Reader entry for Delivery pipelines, progressive releases and schema evolution. Scope includes Release and recovery boundaries; Canonical chapters; Directed question routes."
route_hints:
  questions:
    - "What are the scope, mechanisms and limits of Delivery pipelines, progressive releases and schema evolution?"
  prerequisites: []
  related_ids:
    - "tycho.page.7921e82a71b9446790f185c818326911"
    - "tycho.page.38bb8a14ebb54866a7004080318b47e1"
    - "tycho.page.b938ff1a06264492a425f2eff555ae7d"
    - "tycho.page.77957bf0f2d44c4a9bc819fc5b3e1ddb"
    - "tycho.page.81add4a0d86b4053ae77f9301fd2281d"
    - "tycho.page.1e89567050974052b13ba62b3b44484f"
    - "tycho.page.ea94649bfd8c4be183f9114618d7ccaa"
    - "tycho.page.2f6602f8e20b4f80a22e0ef85a6d1765"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Delivery"
    - "pipelines"
    - "progressive"
    - "releases"
    - "and"
    - "schema"
    - "evolution"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Only exact URL matches to the global source register are normalized here. Page-local case and evidence ledger IDs remain in the body; no claim-level mapping or source inspection is inferred."
content_review:
  status: "draft"
  reviewed_at: null
  reviewer: null
  proof_uri: null
authored_at: "2026-10-18"
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---

# Delivery pipelines, progressive releases and schema evolution

## Purpose and mission

This section distinguishes producing trusted artifacts, promoting those artifacts, operating mixed-version applications and recovering correct business state after a failed change. Neither green CI nor a successful resource rollout is proof of data correctness.

## Release and recovery boundaries

The following original, synthetic decision flow separates artifact eligibility,
application rollout and data recovery. It is a reading guide, not a report of
an executed deployment or a complete release policy.

```mermaid
flowchart TD
    A["Verify artifact identity and provenance"] --> B{"Release evidence sufficient?"}
    B -->|No| H["Hold release and investigate"]
    B -->|Yes| C["Check mixed-version data compatibility"]
    C --> D["Progressively expose the release"]
    D --> E{"Application and data checks pass?"}
    E -->|Yes| F["Promote and continue observation"]
    E -->|No| G{"Is rollback compatible with stored data?"}
    G -->|Yes| R["Roll back and verify recovery"]
    G -->|No| I["Stop exposure and plan forward repair"]
```

Text alternative: verify the artifact before releasing it, check data
compatibility before exposing mixed versions, and evaluate application and data
behavior during rollout. On failure, choose rollback only when the data
contract permits it; otherwise stop exposure and use a validated forward-repair
plan. The chapters below explain the assumptions and evidence for each boundary.

## Canonical chapters

1. [CI/CD architecture, artifact provenance and GitOps reconciliation](ci-cd-provenance-and-gitops.md) — source/build/artifact/release identity, runner trust and permissions, signing/provenance, direct push versus GitOps pull, drift and deployment authority.
2. [Software supply-chain evidence, SBOM and attestations](sbom-attestation-and-release-verification.md) — V08/C02 independently scoped SLSA 1.2, SPDX/CycloneDX and Sigstore verification policies; no build or signing executed.
3. [GitOps, rolling, blue/green and canary releases](gitops-canary-and-progressive-rollout.md) — **V08/C04** release controllers, traffic exposure and rollback safety gates.
4. [Backward-compatible database change and online DDL](mixed-version-database-compatibility-and-online-ddl.md) — **V08/C05** mixed-version reader/writer matrix, schema-change locks, replay and forward repair.
5. [Earlier combined rollout/schema research](progressive-delivery-and-schema-evolution.md) — preserved historical source, no longer the primary owner of V05/C06, V08/C04 or V08/C05.
6. [Safe rollout, compatibility and recovery under partial failure](safe-rollout-and-recovery.md) — original synthetic failed deployment timeline, user-visible acceptance gates, recovery objectives and limitations.

## Directed question routes

| User/agent question | Read first | Related evidence |
|---|---|---|
| How do we prove the deployed artifact is the one tested? | [CI/CD provenance](ci-cd-provenance-and-gitops.md) | [Safe rollout](safe-rollout-and-recovery.md) |
| Which artifact digest, signer, SBOM and provenance claims justify release eligibility? | [SBOM/attestation verification](sbom-attestation-and-release-verification.md) | [CI/CD provenance](ci-cd-provenance-and-gitops.md) |
| When does GitOps actually reconcile live resources? | [CI/CD provenance](ci-cd-provenance-and-gitops.md) | [Deployment control-plane assumptions](../deployment/runtime-placement-and-control-plane.md) |
| Can we run old and new application versions against one database? | [Mixed-version database contracts](mixed-version-database-compatibility-and-online-ddl.md) | [Target and transition model](../../authoring/models/target-transition-architecture.md) |
| Is rolling back an image a safe recovery? | [Safe rollout](safe-rollout-and-recovery.md) | [Progressive delivery](gitops-canary-and-progressive-rollout.md) |
| How should a region-wide loss change the release/recovery plan? | [Disaster recovery](../deployment/disaster-recovery-and-recovery-objectives.md) | [Safe rollout](safe-rollout-and-recovery.md) |

The new chapter owners are original evidence-linked research drafts; the earlier combined study is preserved for editorial evidence migration. Their diagrams, incompatibility examples, controls and incidents are **synthetic**; no deployed pipeline, signature verification, schema upgrade, multi-version experiment, restore drill or independent human review is claimed. The full V08 chapter coverage still requires a distinct editorial crosswalk, not only a landing-page assertion.
