---
metadata_version: 1
id: "tycho.chapter.3b9ec227ed58b92c0004eb0d39099142"
kind: "chapter"
parent_id: "tycho.volume.fe327f72cf81df0237ce47b841e8aef5"
canonical_path: "book/volumes/v11-pattern-atlas/c09-scalability/README.md"
title: "V11/C09 — Scalability and load distribution"
topic_ids:
  - "scaling-mechanisms"
  - "performance-engineering"
perspectives:
  - "architecture"
  - "operations"
summary: "All 10 C09 cards with bounded owner links; decision coverage partial."
route_hints:
  questions:
    - "Which scaling patterns fit the bottleneck and failure domain?"
  prerequisites:
    - "tycho.chapter.b20625a099bc4c82b7d547c32c7da28a"
  related_ids:
    - "tycho.volume.fe327f72cf81df0237ce47b841e8aef5"
    - "tycho.chapter.b20625a099bc4c82b7d547c32c7da28a"
    - "tycho.chapter.bee261b76181706235dd8fa7ccde01a9"
    - "tycho.chapter.dabaea8f5ab426edc08683ceec89c2c0"
  excludes:
    - "Bounded owner links; no sufficient coverage or independent review."
  keywords:
    - "pattern atlas"
    - "scalability and load distribution"
    - "decision layer"
evidence_scope:
  source_ids:
    - "src.sre-frontend-enrichment"
    - "src.k8s-hpa"
    - "src.kubernetes"
    - "src.keda"
    - "src.microsoft-cloud-patterns"
    - "src.cortex-shuffle-sharding"
    - "src.cell-boundaries"
    - "src.microsoft-multitenant"
    - "src.sre-workbook"
  claim_ids: []
  status: "source-linked"
  notes: >-
    10 cards cite read units; owner links are bounded. Tenant-Based Resource
    Isolation moved to a dedicated page on 2026-10-31 with AWS SaaS Lens tenant,
    pool and cross-tenant guidance, Kubernetes multi-tenancy, PostgreSQL row
    security and Microsoft multitenant approaches. Geode moved to a dedicated
    page on 2026-11-01 with the Geodes pattern, Traffic Manager routing,
    monitoring and FAQ, multiregion network design and multiple-region App
    Service guidance; coverage remains partial-bounded.
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
# V11/C09 — Scalability and load distribution

**Owning question:** Which scaling patterns fit the bottleneck and failure domain?

## Purpose and mission

This chapter is the atlas entry point for **Scalability and load distribution**. It
owns the conditional decision route for 10 catalog entries, not the deep mechanism
explanations. Read the exact owner section before applying a mechanism claim.

All 10 entries have a self-checked card. Owner sections are bounded: a scaling or
placement page may own the bottleneck/failure contract without owning every pattern.

## Pages and reasoning route

Page count is content-dependent. This chapter currently uses one landing page for all
entries; a later split is an editorial change, not a plan failure. Start with the card,
check its conditions and contraindications, then read the exact owner section.

## Entry inventory

Each level-three heading is a stable atlas anchor. Owner links are bounded sections;
none claims sufficient technical or decision coverage.

### Load Balancing

See [Load Balancing](load-balancing.md).


### Horizontal Scaling

See the [Horizontal Scaling](horizontal-scaling.md) card.

### Vertical Scaling

See the [dedicated Vertical Scaling card](vertical-scaling.md).

### Autoscaling

See the [Autoscaling](autoscaling.md) card.

### Cell-Based Architecture

See the [Cell-Based Architecture](cell-based-architecture.md) card.

### Shuffle Sharding

See the [Shuffle Sharding](shuffle-sharding.md) card.

### Deployment Stamps

See the [dedicated Deployment Stamps card](deployment-stamps.md).

### Geode

See the [dedicated Geode card](geode.md).

### Static Content Hosting

See the [dedicated Static Content Hosting card](static-content-hosting.md).

### Tenant-Based Resource Isolation

See the [dedicated Tenant-Based Resource Isolation card](tenant-based-resource-isolation.md).

## Chapter result and counterexample

Ten cards establish a conditional decision route. Owner sections are bounded; none
establishes technical sufficiency.

Counterexample: adding replicas to a workload with one shared writer is not evidence
for the horizontal-scaling card's conditions.

## Navigation and prerequisites

- Parent: [V11](../README.md).
- Previous: [V11/C08](../c08-coordination/README.md).
- Next: [V11/C10](../c10-deployment-modernization/README.md).
- Prerequisite: V10/C03 — pattern applicability and contraindications.
- Registry: [pattern registry](../../../../edition/patterns/registry.v1.json).
- Card batch: [card batches](../../../../edition/patterns/card-batches.v1.json).
- Coverage map: [candidate coverage](../../../../edition/patterns/coverage-map.v1.json).

## Evidence and known limits

- All 10 cards cite read ledger units; owner links and backlinks are self-checked.
- Owner links are bounded sections, not dedicated pattern pages.
- No entry claims sufficient technical or decision coverage.
- No independent editorial review, benchmark, production observation or runtime test
  is asserted.
