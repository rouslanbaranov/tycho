---
metadata_version: 1
id: "tycho.landing.6f58e5c00dea4f4086963169a2590bf5"
kind: "landing"
parent_id: "tycho.book.37c50125355948f1b52ec66229ef59bd"
canonical_path: "book/deployment/README.md"
title: "Deployment topology, availability and disaster recovery"
topic_ids:
  - "deployment-architecture"
perspectives:
  - "architecture"
  - "operations"
summary: "Reader entry for Deployment topology, availability and disaster recovery. Scope includes Canonical chapters; Boundaries and reading routes; Research and completion status."
route_hints:
  questions:
    - "What are the scope, mechanisms and limits of Deployment topology, availability and disaster recovery?"
  prerequisites: []
  related_ids:
    - "tycho.page.ea94649bfd8c4be183f9114618d7ccaa"
    - "tycho.page.6b3725950fad4c0db82417b3d0225d32"
    - "tycho.page.2f6602f8e20b4f80a22e0ef85a6d1765"
    - "tycho.page.2536d18422944e27abe4ea8549beb9ab"
    - "tycho.page.f784d6ef723c4c0e8836ff9085bf7dcc"
    - "tycho.page.1e89567050974052b13ba62b3b44484f"
    - "tycho.page.ddeff7f1556f44f18c67659b73e6e15f"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Deployment"
    - "topology"
    - "availability"
    - "and"
    - "disaster"
    - "recovery"
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
authored_at: "2026-10-19"
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---

# Deployment topology, availability and disaster recovery

## Purpose and mission

This part of Tycho answers two questions before naming a deployment product: **where does a system run, and which failure can it survive without violating its business invariants?** Runtime form, service placement, control-plane availability, recoverable business state and operators' actual restore ability are separate architectural responsibilities.

## Canonical chapters

1. [Deployment topology and control-plane independence](../volumes/v08-delivery-deployment-and-recovery/c03-vms-containers-orchestration-and-serverless/runtime-placement-and-control-plane.md) — bare metal, VMs, containers, managed functions, cluster placement, service mesh, data/control planes, IaC state and failure isolation. Use this first when a runtime or placement recommendation is requested.
2. [Availability zones, placement and failure domains](../volumes/v08-delivery-deployment-and-recovery/c06-high-availability-and-failure-domain-placement/availability-zones-placement-and-failure-domains.md) — **V08/C06** replicas, gateway/state dependencies, quorum placement and zonal failure acceptance.
3. [Disaster recovery, RTO/RPO and state reconciliation](../volumes/v08-delivery-deployment-and-recovery/c07-multi-region-recovery-and-data-reconciliation/disaster-recovery-and-recovery-objectives.md) — **V08/C07** disaster-class recovery, fencing, acknowledged-state reconciliation and synthetic restore drills.
4. [Earlier multi-zone/multi-region research](multi-region-disaster-recovery-contracts.md) — preserved combined source for provenance mapping; no longer shared primary owner.

## Boundaries and reading routes

| Question | Start | Expand when needed |
|---|---|---|
| Containers, VMs or serverless for this workload? | [Runtime/placement](../volumes/v08-delivery-deployment-and-recovery/c03-vms-containers-orchestration-and-serverless/runtime-placement-and-control-plane.md) | [Workload shape and capacity experiments](../performance/workload-profiles-and-capacity-experiments.md) |
| How can traffic survive one zone failure? | [Failure-domain placement](../volumes/v08-delivery-deployment-and-recovery/c06-high-availability-and-failure-domain-placement/availability-zones-placement-and-failure-domains.md) | [Recovery](../volumes/v08-delivery-deployment-and-recovery/c07-multi-region-recovery-and-data-reconciliation/disaster-recovery-and-recovery-objectives.md) and [safe rollout](../delivery/safe-rollout-and-recovery.md) |
| Does multi-region deployment mean RPO=0? | [Recovery](multi-region-disaster-recovery-contracts.md) | [PostgreSQL WAL and recovery](../volumes/v05-data-models-engines-and-lifecycle/c02-postgresql-mvcc-wal-and-recovery/postgresql-wal-replication-and-recovery.md) |
| Is an application image rollback also a data rollback? | [Safe rollout](../delivery/safe-rollout-and-recovery.md) | [Recovery](multi-region-disaster-recovery-contracts.md) |
| Can the system safely operate while orchestration services are impaired? | [Runtime/placement](../volumes/v08-delivery-deployment-and-recovery/c03-vms-containers-orchestration-and-serverless/runtime-placement-and-control-plane.md) | [Recovery](multi-region-disaster-recovery-contracts.md) |

A topological diagram is not evidence of RPO/RTO compliance, even where it shows multiple regions. Each decision needs the relevant business operation, data owner, client-visible SLI, exact failure injection, successful restore and a named reviewer.

## Research and completion status

These topic chapters are original, source-linked technical drafts for [E14-09 #87](https://github.com/rouslanbaranov/tycho/issues/87). The failure timelines and comparative examples are **synthetic**; no cloud account, disaster exercise, VM/container benchmark or independent human review is claimed. Their evidence-ledger passages distinguish official publisher mechanisms from unknown provider and workload-specific outcomes.

Other topics in V08 (CI/CD, GitOps and data schema evolution) are owned by subsequent E14-10 work and should not be declared covered by this landing page.
