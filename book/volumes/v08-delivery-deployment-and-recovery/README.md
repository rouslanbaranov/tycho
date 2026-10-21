---
metadata_version: 1
id: "tycho.volume.cb10070ba233477fae8aa5d18e74fee8"
kind: "volume"
parent_id: "tycho.book.37c50125355948f1b52ec66229ef59bd"
canonical_path: "book/volumes/v08-delivery-deployment-and-recovery/README.md"
title: "V08 — Delivery, deployment and disaster recovery"
topic_ids:
  - "deployment-architecture"
  - "software-delivery"
perspectives:
  - "architecture"
  - "evaluation"
summary: "A cutover chain linking artifact trust, mixed versions, deployments, failure domains, data authority and recovery after the no-return point."
route_hints:
  questions:
    - "A cutover chain linking artifact trust, mixed versions, deployments, failure domains, data authority and recovery after the no-return point."
  prerequisites:
    - "tycho.chapter.53b6bb88a00549e491949aeb426b83f2"
    - "tycho.chapter.4a3cbf0617e44be5b1e8d72568109dad"
    - "tycho.chapter.18aa94285a164b6f94530cebcfd87b8b"
    - "tycho.chapter.3d0f6dd1e8e94cd397326e129b5c287f"
    - "tycho.chapter.388c48be24414421a63481b37d05fdce"
  related_ids:
    - "tycho.chapter.8a86707018773def410689efbc79cf94"
    - "tycho.chapter.8a2d2a79846d4567bb3d33957e19977f"
    - "tycho.chapter.92bd770bf87d4d6c9ab6e71cfa291132"
    - "tycho.chapter.94b4b6d9e2e1490abd0055a5265141ff"
    - "tycho.chapter.5e4761e1a3e34c2f8023ec8ac4fa81d5"
    - "tycho.chapter.7d434d1a41e142d38bb729ee124ac548"
    - "tycho.chapter.9e35eb7b056f428093e36a2faf644a23"
    - "tycho.chapter.30e63461f024419ab87cd012b140c600"
  excludes:
    - "No new benchmark, source inspection or independent edition review is asserted."
  keywords:
    - "system-design"
    - "edition-navigation"
evidence_scope:
  source_ids:
    - "src.aws-static-stability"
    - "src.k8s-deployments"
    - "src.opengitops"
    - "src.slsa"
  claim_ids: []
  status: "source-linked"
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

# V08 — Delivery, deployment and disaster recovery

## Purpose and mission

Distinguish producing deployable software from safely releasing and operating it.

The outcome of this volume is: A cutover chain linking artifact trust, mixed versions, deployments, failure domains, data authority and recovery after the no-return point.

## A worked cross-chapter synthesis

A fictional release uses a signed artifact and a small canary. The canary writes a value old binaries cannot interpret. Later a zone fails while the former writer remains reachable. Artifact authenticity, safe exposure, data compatibility and exclusive recovery authority are four separate questions.

Follow the cutover chain from source/build identity through digest verification and authorized promotion to mixed-version execution. Place replicas with shared dependencies visible. Define stop conditions, no-return points, writer fencing, reconciliation and user-level recovery clocks before declaring a rollout or region switch successful.

## Questions and chapters

| Chapter | Owning question |
|---|---|
| [V08/C01 — CI/CD architecture and artifact provenance](c01-ci-cd-architecture-and-artifact-provenance/README.md) | Which boundaries separate build, test, publication and production deployment? |
| [V08/C02 — Supply chain and release verification](c02-supply-chain-and-release-verification/README.md) | How are reproducibility, signatures and promotion controls established? |
| [V08/C03 — VMs, containers, orchestration and serverless](c03-vms-containers-orchestration-and-serverless/README.md) | Which topology suits operational and workload requirements? |
| [V08/C04 — GitOps, rollout and progressive delivery](c04-gitops-rollout-and-progressive-delivery/README.md) | How do rolling, blue/green, canary, rollback and analysis gates differ? |
| [V08/C05 — Backward-compatible database change](c05-backward-compatible-database-change/README.md) | What permits old and new binaries/data schemas to coexist? |
| [V08/C06 — High availability and failure-domain placement](c06-high-availability-and-failure-domain-placement/README.md) | What survives machine, zone, dependency or region loss? |
| [V08/C07 — Multi-region recovery and data reconciliation](c07-multi-region-recovery-and-data-reconciliation/README.md) | How are RPO/RTO, split brain, recovery routes and failback validated? |
| [V08/C08 — Network request paths, routing and edge delivery](c08-network-request-paths-routing-and-edge-delivery/README.md) | Which network boundary owns routing, transport, trust and the fate of an interrupted request? |

## Choosing a reading route

For a first reading, follow the chapter order. For diagnosis, connect the observed outcome to its authority and failure boundary using: [V08/C01](c01-ci-cd-architecture-and-artifact-provenance/README.md), [V08/C02](c02-supply-chain-and-release-verification/README.md), [V08/C04](c04-gitops-rollout-and-progressive-delivery/README.md), [V08/C05](c05-backward-compatible-database-change/README.md), [V08/C07](c07-multi-region-recovery-and-data-reconciliation/README.md). Return to the exact page-local source ledger before making a version-specific claim.

Prerequisite context: V02/C05; V04/C03–C05; V05/C06–C07.

Read [V02/C05](../v02-application-boundaries-and-contracts/c05-public-apis-http-rpc-and-compatibility/README.md), [V04/C03](../v04-distributed-coordination-and-events/c03-consistency-and-distributed-transactions/README.md), [V04/C05](../v04-distributed-coordination-and-events/c05-outbox-inbox-sagas-and-durable-workflows/README.md), [V05/C06](../v05-data-models-engines-and-lifecycle/c06-schema-evolution-data-migration-and-retention/README.md), [V05/C07](../v05-data-models-engines-and-lifecycle/c07-replication-backups-and-restore-drills/README.md) for the named entry assumptions.

### Reasoning boundaries

This original conceptual map separates competing inputs rather than promising a universal solution.

~~~mermaid
flowchart TD
    Q["V08/C01 — CI/CD architecture and artifact provenance"] --> M["V08/C02 — Supply chain and release verification"]
    Q --> E["Evidence and unknown inputs"]
    M --> D{"Meets the declared constraints?"}
    E --> D
    D -->|Supported| R["V08/C07 — Multi-region recovery and data reconciliation"]
    D -->|Unresolved| U["Measure, revise or retain the baseline"]
~~~

Text alternative: establish ci/cd architecture and artifact provenance, compare supply chain and release verification with the available evidence, and either carry a supported result forward or return to unresolved inputs. The figure describes a reasoning route, not observed runtime behavior.

## Counterexample and handoff

Reverting a binary does not restore discarded data or reverse an external effect.
Placement across zones does not remove a shared control or storage dependency. Hand
operations over to a tested recovery procedure and a clear evidence boundary;
documentation and proposed drills are not evidence that a live recovery occurred.

## Navigation and source boundaries

| Route | Destination |
|---|---|
| Parent | [Book contents](../../README.md) |
| Previous volume | [V07](../v07-performance-scale-and-resilience/README.md) |
| Next volume | [V09](../v09-observability-security-and-operations/README.md) |
| Historical applications | [Casebook and synthetic playbooks](../../cases/README.md) |

## Evidence and known limits

The scenario is original synthetic reasoning. The chapters contain the accepted manuscript and its published evidence; no synthetic number or historical result is a measured prediction for another system. This new synthesis is editorially self-checked, not independently certified. Source-access restrictions, unexecuted technology experiments and original case denominators remain explicit in their owning pages. Product-specific adoption still requires compatible versions and the target workload.
