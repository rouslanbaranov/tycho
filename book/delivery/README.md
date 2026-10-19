# Delivery pipelines, progressive releases and schema evolution

## Purpose and mission

This section distinguishes producing trusted artifacts, promoting those artifacts, operating mixed-version applications and recovering correct business state after a failed change. Neither green CI nor a successful resource rollout is proof of data correctness.

## Canonical chapters

1. [CI/CD architecture, artifact provenance and GitOps reconciliation](ci-cd-provenance-and-gitops.md) — source/build/artifact/release identity, runner trust and permissions, signing/provenance, direct push versus GitOps pull, drift and deployment authority.
2. [Progressive delivery, mixed-version contracts and database evolution](progressive-delivery-and-schema-evolution.md) — rolling/blue-green/canary, N/N+1 compatibility matrices, expand/migrate/contract, online DDL and rollback versus forward repair.
3. [Safe rollout, compatibility and recovery under partial failure](safe-rollout-and-recovery.md) — original synthetic failed deployment timeline, user-visible acceptance gates, recovery objectives and limitations.

## Directed question routes

| User/agent question | Read first | Related evidence |
|---|---|---|
| How do we prove the deployed artifact is the one tested? | [CI/CD provenance](ci-cd-provenance-and-gitops.md) | [Safe rollout](safe-rollout-and-recovery.md) |
| When does GitOps actually reconcile live resources? | [CI/CD provenance](ci-cd-provenance-and-gitops.md) | [Deployment control-plane assumptions](../deployment/runtime-placement-and-control-plane.md) |
| Can we run old and new application versions against one database? | [Mixed-version contracts](progressive-delivery-and-schema-evolution.md) | [Target and transition model](../../authoring/models/target-transition-architecture.md) |
| Is rolling back an image a safe recovery? | [Safe rollout](safe-rollout-and-recovery.md) | [Progressive delivery](progressive-delivery-and-schema-evolution.md) |
| How should a region-wide loss change the release/recovery plan? | [Disaster recovery](../deployment/multi-region-disaster-recovery-contracts.md) | [Safe rollout](safe-rollout-and-recovery.md) |

The three chapters are original evidence-linked research documents. Their diagrams, incompatibility examples, controls and incidents are **synthetic**; no deployed pipeline, signature verification, schema upgrade, multi-version experiment, restore drill or independent human review is claimed. The full V08 chapter coverage still requires a distinct editorial crosswalk, not only a landing-page assertion.
