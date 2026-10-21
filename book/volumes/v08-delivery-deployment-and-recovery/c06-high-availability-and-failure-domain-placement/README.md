---
metadata_version: 1
id: "tycho.chapter.9e35eb7b056f428093e36a2faf644a23"
kind: "chapter"
parent_id: "tycho.volume.cb10070ba233477fae8aa5d18e74fee8"
canonical_path: "book/volumes/v08-delivery-deployment-and-recovery/c06-high-availability-and-failure-domain-placement/README.md"
title: "V08/C06 — High availability and failure-domain placement"
topic_ids:
  - "deployment-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: "What survives machine, zone, dependency or region loss? The reading route separates 2 detailed questions from the integrated decision."
route_hints:
  questions:
    - "What survives machine, zone, dependency or region loss?"
  prerequisites:
    - "tycho.chapter.7d434d1a41e142d38bb729ee124ac548"
  related_ids:
    - "tycho.page.6b3725950fad4c0db82417b3d0225d32"
    - "tycho.page.3e79e1a21bd944a5bddf9564daed5066"
    - "tycho.page.c579aa863be74f9ca5718e58f6f34c21"
  excludes:
    - "No new benchmark, source inspection or independent edition review is asserted."
  keywords:
    - "system-design"
    - "edition-navigation"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Editorial synthesis of the linked accepted manuscript; exact source versions and nonclaims remain in its page-local evidence ledger."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-20"
  reviewer: "Codex editorial assembly"
  proof_uri: null
authored_at: "2026-10-20"
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---

# V08/C06 — High availability and failure-domain placement

## Purpose and mission

What survives machine, zone, dependency or region loss? This chapter owns that question within delivery, deployment and disaster recovery. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Model shared dependencies and traffic authority when placing replicas across failure domains.

Two zones can still depend on one datastore or control path; nominal placement diversity does not demonstrate surviving user journeys. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

Begin with the integrated decision, then open the independent question that matches the missing mechanism or observed failure. Read source limits before applying the conclusion.

| Page | Independent question and role |
|---|---|
| [Integrated decision and original walkthrough](availability-zones-placement-and-failure-domains.md) | What survives machine, zone, dependency or region loss? |
| [Shared dependencies and replica placement](failure-domains.md) | Which dependency sets remain common despite nominal zone diversity? |
| [Authority, control loss and availability tests](authority-availability.md) | Which traffic and state ownership transfer must be validated after a domain fails? |


## Additional mechanism and project routes

These independently scoped pages extend the chapter without replacing its original walkthrough or source ledger.

| Page | Owning question |
| --- | --- |
| [Cells and shuffle sharding](cells-shuffle-sharding.md) | Which state, routing and rollout boundaries actually contain a tenant-triggered failure? |

## Boundaries and further reading

The preceding and following chapters supply context; this landing does not replace their canonical mechanisms. Follow the exact source ledger on the child page when a claim depends on a product version or historical period.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V08 — Delivery, deployment and disaster recovery](../README.md) |
| Previous | [V08/C05 — Backward-compatible database change](../c05-backward-compatible-database-change/README.md) |
| Next | [V08/C07 — Multi-region recovery and data reconciliation](../c07-multi-region-recovery-and-data-reconciliation/README.md) |
| Prerequisite | [V08/C05 — Backward-compatible database change](../c05-backward-compatible-database-change/README.md) |
| Source reading | [Page-local evidence and versions](availability-zones-placement-and-failure-domains.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.

## Chapter source ledger

The following original citation rows, review limits and earlier topical routes are retained once for this chapter. Each question page points here and retains its inline citations. Evidence coverage must be judged at the actual claim and version, not inferred from source-list length.

<!-- tycho-question-source:tycho.page.6b3725950fad4c0db82417b3d0225d32:8 -->
## 7. Evidence ledger and limits

| Public source inspected | Supports | Not established |
|---|---|---|
| [Kubernetes topology spread](https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/) | Scheduling preferences/requirements and placement limits | End-to-end app/DB failure tolerance |
| [AWS Well-Architected recovery strategy](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_planning_for_recovery_disaster_recovery.html) | Named recovery strategy/failure domains and cost/recovery trade-offs | Any executed regional failover |
| [Earlier Tycho combined regional/DR research](../../../deployment/multi-region-disaster-recovery-contracts.md) | Prior version-bound disaster scenarios | Reviewed and independently tested design |

All examples and topology representations are synthetic; no cloud or cluster action was made and no recovery objective achieved. Publication chapter/page structure and independent source-by-claim review remain open.

**Navigation:** owner **V08/C06**, via [deployment landing](../../../deployment/README.md) and [book outline](../../../PROPOSED-STRUCTURE.md). Related [runtime placement](../c03-vms-containers-orchestration-and-serverless/runtime-placement-and-control-plane.md), [quorum](../../v04-distributed-coordination-and-events/c02-replication-consensus-and-leader-changes/replication-consensus-and-leader-change.md), [disaster recovery](../c07-multi-region-recovery-and-data-reconciliation/disaster-recovery-and-recovery-objectives.md).
<!-- /tycho-question-source -->
