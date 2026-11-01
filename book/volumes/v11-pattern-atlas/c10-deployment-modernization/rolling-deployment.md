---
metadata_version: 1
id: tycho.page.85a65c363be7ef02fe02d8b551e5b5c1
kind: page
parent_id: tycho.chapter.dabaea8f5ab426edc08683ceec89c2c0
canonical_path: book/volumes/v11-pattern-atlas/c10-deployment-modernization/rolling-deployment.md
title: Rolling Deployment
topic_ids:
- deployment-and-legacy-modernization
perspectives:
- architecture
- operations
- evaluation
summary: Decision card for Rolling Deployment.
route_hints:
  questions:
  - Should instances be replaced incrementally while traffic continues?
  prerequisites:
  - tycho.chapter.dabaea8f5ab426edc08683ceec89c2c0
  related_ids:
  - tycho.chapter.dabaea8f5ab426edc08683ceec89c2c0
  excludes:
  - No owner acceptance is claimed for this card.
  keywords:
  - pattern atlas
  - rolling deployment
evidence_scope:
  source_ids:
  - src.k8s-deployments
  claim_ids: []
  status: source-linked
  notes: Source-level bindings remain in the owner unit.
content_review:
  status: self-checked
  reviewed_at: '2026-11-01'
  reviewer: Automated authoring agent
  proof_uri: null
authored_at: '2026-11-01'
updated_at: '2026-11-01'
source_inspection_date: '2026-10-21'
content_verified_at: null
---

# Rolling Deployment

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

**Technical owner.**
 [GitOps, rolling, blue/green and canary release
architecture](../../v08-delivery-deployment-and-recovery/c04-gitops-rollout-and-progressive-delivery/gitops-canary-and-progressive-rollout.md#rolling-deployment)
— rolling replacement and readiness are bounded; controller-specific surge math is
platform-specific.

**Sources.** [src.k8s-deployments](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch5-k8s-deployment.2026-10-21: all 48 headings read.
The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Blue/Green Deployment; Canary Release; Feature Flags; Readiness
Probes.
