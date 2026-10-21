---
metadata_version: 1
id: "tycho.page.5d5dd1d008b848a39dfae29a147da6d0"
kind: "page"
parent_id: "tycho.chapter.94b4b6d9e2e1490abd0055a5265141ff"
canonical_path: "book/volumes/v08-delivery-deployment-and-recovery/c03-vms-containers-orchestration-and-serverless/compute-models.md"
title: "Compute models and operating constraints"
topic_ids:
  - "deployment-architecture"
perspectives:
  - "architecture"
  - "operations"
summary: "Which workload, isolation and operating constraints make a runtime topology viable?"
route_hints:
  questions:
    - "Which workload, isolation and operating constraints make a runtime topology viable?"
  prerequisites:
    - "tycho.page.ea94649bfd8c4be183f9114618d7ccaa"
  related_ids:
    - "tycho.chapter.94b4b6d9e2e1490abd0055a5265141ff"
    - "tycho.page.ea94649bfd8c4be183f9114618d7ccaa"
    - "tycho.page.b7913b53d5ea439697bc5236f902d76e"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "compute"
    - "models"
evidence_scope:
  source_ids:
    - "src.aws-static-stability"
  claim_ids: []
  status: "source-linked"
  notes: "Bounded question from tycho.page.ea94649bfd8c4be183f9114618d7ccaa; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
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
# Compute models and operating constraints

**Owning question:** Which workload, isolation and operating constraints make a runtime topology viable?

This page belongs to [V08/C03 — VMs, containers, orchestration and serverless](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.ea94649bfd8c4be183f9114618d7ccaa:0 -->
## Decision question and scope

Given a required user journey, workload, failure class, operational team and data-residency constraints, **which runtime boundary, placement arrangement and control-plane dependencies can preserve the stated behavior?** The deployment unit alone—bare metal, VM, container or function—cannot answer that question. A container in one failure zone is not automatically more available than a VM with proven restore; a service mesh adds configuration and a data plane but does not make application state consistent.

Record separately: state writer, ingress, runtime instance, scheduler/control service, deployment mechanism, network path, secrets/identity service, availability zone/host/region and operator responsibility.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.ea94649bfd8c4be183f9114618d7ccaa:1 -->
## Compute models and their real trade-offs

| Model | Isolation and ownership boundary | Relative advantages when conditions fit | Constraints, failure questions and disqualifiers |
|---|---|---|---|
| **Bare metal / dedicated host** | Physical machine and its firmware/storage/network plus chosen OS | Direct device control, predictable specialized capacity, hardware/locality requirements | Provision and repair time, host loss, replacement inventory, OS patching, storage replication, team operation burden |
| **Virtual machine** | Guest OS with hypervisor and virtualized devices; placement is still physical | Established OS/kernel isolation and explicit runtime image lifecycle; can host legacy services | Host and zone fault domains, VM boot/restore, hypervisor dependency, attached volume recovery, deployment velocity |
| **Container on shared host/orchestrator** | Namespaced processes and images; kernel may be shared; scheduler/node placement matter | Repeatable image artifact and selected scheduling/rescheduling policy, if node/registry/control services are healthy | Container is NOT its own kernel or zone; image registry, cluster control plane, network overlay, storage/secret fetch and autoscaler delay can block recovery |
| **Managed function/serverless** | Provider-managed execution and scaling, with invocation/event/timeout boundaries | Scale-to-demand and reduced direct host operations when workload execution model matches | Runtime quotas/concurrency, start delay, state externalization, connection spikes, event retry/delivery and vendor control-plane/region dependencies |
| **Managed platform service** | Provider-defined database/broker/queue/cache failure domain | Reduces operational ownership for versioned service features | Actual failover and consistency semantics require exact provider/region/version evidence; not a universal RPO/RTO guarantee |

Comparisons require the **same observable outcome, admitted/offered load, logical data correctness and named outage**, plus staffing, steady-state cost and restore test. Package type does not imply a number of safe replicas. A migration to containers may be contraindicated by a hard device driver/kernel dependency, unsupported legacy licensing, or an immutable on-disk contract; those are evidence questions, not stereotypes.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](runtime-placement-and-control-plane.md) |
| Next | [Continue the reasoning](static-stability.md) |
| Integrated question | [Original scenario and limits](runtime-placement-and-control-plane.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.
