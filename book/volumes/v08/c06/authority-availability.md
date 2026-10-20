---
metadata_version: 1
id: "tycho.page.c579aa863be74f9ca5718e58f6f34c21"
kind: "page"
parent_id: "tycho.chapter.9e35eb7b056f428093e36a2faf644a23"
canonical_path: "book/volumes/v08/c06/authority-availability.md"
title: "Authority, control loss and availability tests"
topic_ids:
  - "deployment-architecture"
perspectives:
  - "architecture"
  - "operations"
summary: "Which traffic and state ownership transfer must be validated after a domain fails?"
route_hints:
  questions:
    - "Which traffic and state ownership transfer must be validated after a domain fails?"
  prerequisites:
    - "tycho.page.3e79e1a21bd944a5bddf9564daed5066"
  related_ids:
    - "tycho.chapter.9e35eb7b056f428093e36a2faf644a23"
    - "tycho.page.6b3725950fad4c0db82417b3d0225d32"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "authority"
    - "availability"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Bounded question from tycho.page.6b3725950fad4c0db82417b3d0225d32; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
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
# Authority, control loss and availability tests

**Owning question:** Which traffic and state ownership transfer must be validated after a domain fails?

This page belongs to [V08/C06 — High availability and failure-domain placement](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.6b3725950fad4c0db82417b3d0225d32:4 -->
## 4. Data authority and control-plane loss change availability claims

A control plane schedules or configures resources; a data plane carries user operations. Some existing pods may continue handling work when the control plane is unavailable, but new deployments, scaling, secret updates, node repair or replacement may be impaired. Recovery plans must identify which actions require inaccessible infrastructure services.

For stateful systems, a primary can become unreachable while a lagging secondary still accepts reads. If a write must be linearizable, an isolated minority must not present itself as a new authoritative writer without correct fencing/election. [Quorum and leader changes](../../v04/c02/replication-consensus-and-leader-change.md) owns the underlying protocol; this chapter owns placement and failure-domain consequences.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.6b3725950fad4c0db82417b3d0225d32:5 -->
## 5. Trade-offs in fault isolation

| Topology | Strength | Important failure mode |
|---|---|---|
| One host/process | Lowest operational footprint | Host failure removes all compute |
| Several replicas on one node | More processes | Node loss takes all copies |
| Several nodes in one zone | Node tolerance | Zonal loss and shared dependencies |
| Multizone service + replicated state | Can tolerate some zone failures | Gateway/quorum placement and correlated storage loss |
| Multiregion active/passive | Regional alternative possible | Recovery time, replica lag, artifact/access availability |
| Multiregion active/active | Potential concurrent regional service | Conflict resolution, multi-writer invariants and higher cost |

No row promises an actual availability number. Correlated dependencies and measured time-to-recovery determine whether a design meets the stated user contract.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.6b3725950fad4c0db82417b3d0225d32:6 -->
## 6. Architecture acceptance and negative experiments

Proposed experiments (not executed): kill one application pod, node and zone; interrupt the gateway; remove the database primary or a quorum voter; test region-control-plane unavailability; exhaust capacity during an expected reschedule; verify no competing authoritative writers and no duplicate accepted business effects.

For each failure, measure client-level correct outcomes, explicit rejections, timeouts, state reconciliation, routed traffic, dependency recovery and total operating cost. A test that checks only desired replica count can pass while users cannot access correct data.

The [AWS Well-Architected DR strategy guidance](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_planning_for_recovery_disaster_recovery.html) distinguishes zonal mitigation from regional recovery; its vendor strategy examples do not prove the invented topology works.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](failure-domains.md) |
| Next | [Continue the reasoning](README.md) |
| Integrated question | [Original scenario and limits](availability-zones-placement-and-failure-domains.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.
