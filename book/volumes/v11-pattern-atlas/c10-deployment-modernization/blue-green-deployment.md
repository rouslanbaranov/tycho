---
metadata_version: 1
id: tycho.page.d6b64b621ab5754ade56735ee8e45d8a
kind: page
parent_id: tycho.chapter.dabaea8f5ab426edc08683ceec89c2c0
canonical_path: book/volumes/v11-pattern-atlas/c10-deployment-modernization/blue-green-deployment.md
title: Blue/Green Deployment
topic_ids:
- deployment
perspectives:
- architecture
- operations
- evaluation
summary: Decision card for Blue/Green Deployment.
route_hints:
  questions:
  - Should traffic switch between two complete environments rather than replace in
    place?
  prerequisites:
  - tycho.chapter.dabaea8f5ab426edc08683ceec89c2c0
  related_ids:
  - tycho.chapter.dabaea8f5ab426edc08683ceec89c2c0
  excludes:
  - No owner acceptance is claimed for this card.
  keywords:
  - pattern atlas
  - blue green deployment
evidence_scope:
  source_ids:
  - src.argo-rollouts
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

# Blue/Green Deployment

**Identity.** Blue/Green Deployment; family Deployment and legacy modernization; kind
deployment-pattern; priority core.

**Decision question.** Should traffic switch between two complete environments rather than
replace in place?

**Good-fit conditions.** Two environments fit the cost; state is externalized or readable by
both versions; in-flight work can drain or route to both; switch/rollback is quick; data
compatibility is explicit.

**Hard contraindications.** Reject when duplicate capacity is prohibitive, when state
cannot be shared, or when a switch would lose in-flight work.

**Competing alternative.** Rolling deployment or canary. Reverse the choice when duplicate
environment cost exceeds rollback benefit.

**Failure and recovery.** Data compatibility and switch atomicity are common; verify state
in the owner section.

**Technical owner.**
 [GitOps, rolling, blue/green and canary release
architecture](../../v08-delivery-deployment-and-recovery/c04-gitops-rollout-and-progressive-delivery/gitops-canary-and-progressive-rollout.md#blue-green-deployment)
— traffic switch and rollback are bounded; infrastructure provisioning is platform-specific.

**Sources.** [src.argo-rollouts](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch5-argo-bluegreen.2026-10-21: all fifteen served headings
read. The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Rolling Deployment; Canary Release; Immutable Infrastructure;
Controlled Cutover.
