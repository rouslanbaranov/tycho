---
metadata_version: 1
id: "tycho.chapter.94b4b6d9e2e1490abd0055a5265141ff"
kind: "chapter"
parent_id: "tycho.volume.cb10070ba233477fae8aa5d18e74fee8"
canonical_path: "book/volumes/v08-delivery-deployment-and-recovery/c03-vms-containers-orchestration-and-serverless/README.md"
title: "V08/C03 — VMs, containers, orchestration and serverless"
topic_ids:
  - "deployment-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Which topology suits operational and workload requirements? The reading route separates 2 detailed questions from the integrated decision."
route_hints:
  questions:
    - "Which topology suits operational and workload requirements?"
  prerequisites:
    - "tycho.chapter.92bd770bf87d4d6c9ab6e71cfa291132"
  related_ids:
    - "tycho.page.ea94649bfd8c4be183f9114618d7ccaa"
    - "tycho.page.5d5dd1d008b848a39dfae29a147da6d0"
    - "tycho.page.b7913b53d5ea439697bc5236f902d76e"
  excludes:
    - "No new benchmark, source inspection or independent edition review is asserted."
  keywords:
    - "system-design"
    - "edition-navigation"
evidence_scope:
  source_ids:
    - "src.aws-static-stability"
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

# V08/C03 — VMs, containers, orchestration and serverless

## Purpose and mission

Which topology suits operational and workload requirements? This chapter owns that question within delivery, deployment and disaster recovery. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Compare runtime topologies against the same outcome, failure model, resource needs and operating capability.

A container or orchestration label does not establish fault isolation, useful spare capacity or recoverable state. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

Begin with the integrated decision, then open the independent question that matches the missing mechanism or observed failure. Read source limits before applying the conclusion.

| Page | Independent question and role |
|---|---|
| [Integrated decision and original walkthrough](runtime-placement-and-control-plane.md) | Which topology suits operational and workload requirements? |
| [Compute models and operating constraints](compute-models.md) | Which workload, isolation and operating constraints make a runtime topology viable? |
| [Control planes, placement and reversibility](static-stability.md) | What work can continue when orchestration or placement control is unavailable? |

## Boundaries and further reading

The preceding and following chapters supply context; this landing does not replace their canonical mechanisms. Follow the exact source ledger on the child page when a claim depends on a product version or historical period.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V08 — Delivery, deployment and disaster recovery](../README.md) |
| Previous | [V08/C02 — Supply chain and release verification](../c02-supply-chain-and-release-verification/README.md) |
| Next | [V08/C04 — GitOps, rollout and progressive delivery](../c04-gitops-rollout-and-progressive-delivery/README.md) |
| Prerequisite | [V08/C02 — Supply chain and release verification](../c02-supply-chain-and-release-verification/README.md) |
| Source reading | [Page-local evidence and versions](runtime-placement-and-control-plane.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.

## Chapter source ledger

The following original citation rows, review limits and earlier topical routes are retained once for this chapter. Each question page points here and retains its inline citations. Evidence coverage must be judged at the actual claim and version, not inferred from source-list length.

<!-- tycho-question-source:tycho.page.ea94649bfd8c4be183f9114618d7ccaa:6 -->
## Source-to-claim ledger — inspected primary scope

| Ref | Exact publicly inspected material (2026-10-19) | Supports and exclusions |
|---|---|---|
| D87-01 | [AWS Builders' Library: Static stability using Availability Zones](https://aws.amazon.com/builders-library/static-stability-using-availability-zones/), *Static stability*, *Static stability patterns* and *Control/Data plane* explanation | Failure readiness/preprovisioned capacity in AWS examples; does **not** establish an exact generic overprovisioning ratio or a service's SLA |
| D87-02 | [Kubernetes: Pod Topology Spread Constraints](https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/), *Spread constraints for Pods* and scheduler behavior | Versioned topology scheduling parameters; not a proof of actual placement or healthy nodes |
| D87-03 | [Kubernetes: Nodes](https://kubernetes.io/docs/concepts/architecture/nodes/), node components and status documentation | Control/worker relationships and node lifecycle; not application failover |
| D87-04 | [Envoy: xDS configuration API overview](https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/operations/dynamic_configuration), *xDS overview*, living latest documentation inspected 2026-10-19 | Control configuration of Envoy proxies; cannot assert mesh behavior for every vendor/version or independent data-plane consistency |
| D87-05 | [HashiCorp Terraform: State](https://developer.hashicorp.com/terraform/language/state/purpose), *State purpose*, documentation inspected 2026-10-19 | Declared-resource ↔ real-resource mapping and state importance; no claim that a disaster-recovery runbook exists |
| D87-06 | [AWS DR Whitepaper: Disaster recovery options](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html), *Backup and restore* and *Pilot light* | Need to restore infrastructure/configuration and exercise DR; not a universal recovery duration |

### Open source and version gaps

No single inspected umbrella reference in this issue establishes comparable isolation/latency/cold-start guarantees for **all bare-metal, VM, container and serverless vendors**. A dedicated primary-source packet must be added before a vendor-specific selection or quantitative cost ranking: exact container runtime and kernel isolation docs, hypervisor/security policy, selected FaaS concurrency/start limits, actual mesh version and provider quotas. A future benchmark must include equipment, region, topology and time window. Until then, the table is a **conditional mechanism comparison**, not a measured product ranking.

<!-- /tycho-question-source -->
