---
metadata_version: 1
id: "tycho.chapter.dabaea8f5ab426edc08683ceec89c2c0"
kind: "chapter"
parent_id: "tycho.volume.fe327f72cf81df0237ce47b841e8aef5"
canonical_path: "book/volumes/v11-pattern-atlas/c10-deployment-modernization/README.md"
title: "V11/C10 — Deployment and legacy modernization"
topic_ids:
  - "deployment-architecture"
  - "software-delivery"
perspectives:
  - "architecture"
  - "migration"
summary: "All 12 C10 cards with bounded owner links; decision coverage partial."
route_hints:
  questions:
    - "Which deployment patterns keep change reversible?"
  prerequisites:
    - "tycho.chapter.b20625a099bc4c82b7d547c32c7da28a"
  related_ids:
    - "tycho.volume.fe327f72cf81df0237ce47b841e8aef5"
    - "tycho.chapter.b20625a099bc4c82b7d547c32c7da28a"
    - "tycho.chapter.3b9ec227ed58b92c0004eb0d39099142"
    - "tycho.chapter.419769c372ccaa569796954878e3bef9"
  excludes:
    - "Bounded owner links; no sufficient coverage or independent review."
  keywords:
    - "pattern atlas"
    - "deployment and legacy modernization"
    - "decision layer"
evidence_scope:
  source_ids:
    - "src.aws-immutable-infrastructure"
    - "src.fowler-dark-launching"
    - "src.istio-traffic-mirroring"
    - "src.k8s-deployments"
    - "src.argo-rollouts"
    - "src.flagger-deployment-strategies"
    - "src.sre-workbook"
    - "src.aws-blue-green-deployments"
    - "src.fowler-feature-toggles"
    - "src.opengitops"
    - "src.ibm-immutable-infrastructure"
    - "src.fowler-strangler"
    - "src.aws-strangler"
    - "src.fowler-branch"
    - "src.flyway"
    - "src.mysql"
    - "src.postgresql"
    - "src.appconfig-rollout"
    - "src.aws-branch"
    - "src.hashicorp-immutable-vms"
  claim_ids: []
  status: "source-linked"
  notes: >-
    12 cards cite read units; owner links are bounded. GitOps moved to a
    dedicated page on 2026-11-01 with OpenGitOps principles v1.0.0, Argo CD
    reconciliation, drift, security and availability, and Flux concepts, drift,
    verification and monitoring; no sufficient coverage.
content_review:
  status: "self-checked"
  reviewed_at: "2026-11-01"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-21"
updated_at: "2026-11-01"
source_inspection_date: "2026-11-01"
content_verified_at: null
---
# V11/C10 — Deployment and legacy modernization

**Owning question:** Which deployment patterns keep change reversible?

## Purpose and mission

This chapter is the atlas entry point for **Deployment and legacy modernization**. It
owns the conditional decision route for 12 catalog entries, not the deep mechanism
explanations. Read the exact owner section before applying a mechanism claim.

All 12 entries have a self-checked card. Owner sections are bounded: a rollout or
transition-state page may own the reversibility contract without owning every pattern.

## Pages and reasoning route

Page count is content-dependent. This chapter uses a landing page plus a dedicated
card page; a later split is an editorial change, not a plan failure. Start with the card,
check its conditions and contraindications, then read the exact owner section.

## Entry inventory

Each level-three heading is a stable atlas anchor. Owner links are bounded sections;
none claims sufficient technical or decision coverage.

### Rolling Deployment

See the [Rolling Deployment](rolling-deployment.md) card.

### Blue-Green Deployment

See the [Blue/Green Deployment](blue-green-deployment.md) card.

### Canary Release

See the [dedicated Canary Release card](canary-release.md).

### Feature Flags-Feature Toggles

See the [dedicated Feature Flags-Feature Toggles card](feature-flags.md).

### GitOps

See the [dedicated GitOps card](gitops.md).

### Immutable Infrastructure

See the [dedicated Immutable Infrastructure card](immutable-infrastructure.md).

### Strangler Fig

See the [dedicated Strangler Fig card](strangler-fig.md).

### Branch by Abstraction

See the [dedicated Branch by Abstraction card](branch-by-abstraction.md).

### Parallel Run

See the [dedicated Parallel Run card](parallel-run.md).

### Dark Launching / Shadow Traffic

See the [dedicated Dark Launching card](dark-launching.md).

### Expand-and-Contract

See the [dedicated Expand-and-Contract card](expand-and-contract.md).

### Controlled Cutover

See the [dedicated Controlled Cutover card](controlled-cutover.md).

## Chapter result and counterexample

Twelve cards establish a conditional decision route. Owner sections are bounded; none
establishes technical sufficiency.

Counterexample: a canary that receives no meaningful traffic is not evidence for the
canary card's analysis conditions.

## Navigation and prerequisites

- Parent: [V11](../README.md).
- Previous: [V11/C09](../c09-scalability/README.md).
- Next: [V11/C11](../c11-security-operations/README.md).
- Prerequisite: V10/C03 — pattern applicability and contraindications.
- Registry: [pattern registry](../../../../edition/patterns/registry.v1.json).
- Card batch: [card batches](../../../../edition/patterns/card-batches.v1.json).
- Coverage map: [candidate coverage](../../../../edition/patterns/coverage-map.v1.json).

## Evidence and known limits

- All 12 cards cite read ledger units; owner links and backlinks are self-checked.
- Owner links are bounded sections, not dedicated pattern pages.
- No entry claims sufficient technical or decision coverage.
- No independent editorial review, benchmark, production observation or runtime test
  is asserted.
