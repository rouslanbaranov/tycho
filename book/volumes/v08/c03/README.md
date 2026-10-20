---
metadata_version: 1
id: "tycho.chapter.94b4b6d9e2e1490abd0055a5265141ff"
kind: "chapter"
parent_id: "tycho.volume.cb10070ba233477fae8aa5d18e74fee8"
canonical_path: "book/volumes/v08/c03/README.md"
title: "V08/C03 — VMs, containers, orchestration and serverless"
topic_ids:
  - "deployment-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Which topology suits operational and workload requirements?"
route_hints:
  questions:
    - "Which topology suits operational and workload requirements?"
  prerequisites:
    - "tycho.chapter.92bd770bf87d4d6c9ab6e71cfa291132"
  related_ids: []
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

| Page | Owning question |
|---|---|
| [Deployment topology and control-plane independence](runtime-placement-and-control-plane.md) | Which topology suits operational and workload requirements? |

The page is one bounded explanation. Its mechanism, failure analysis and evidence are kept together rather than split to meet a numerical page quota. Use these section entry points:

- [Decision question and scope](runtime-placement-and-control-plane.md#decision-question-and-scope).
- [Compute models and their real trade-offs](runtime-placement-and-control-plane.md#compute-models-and-their-real-trade-offs).
- [Source-to-claim ledger — inspected primary scope](runtime-placement-and-control-plane.md#source-to-claim-ledger-inspected-primary-scope).
- [Architecture-selection outcome](runtime-placement-and-control-plane.md#architecture-selection-outcome).

## Boundaries and further reading

The preceding and following chapters supply context; this landing does not replace their canonical mechanisms. Follow the exact source ledger on the child page when a claim depends on a product version or historical period.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V08 — Delivery, deployment and disaster recovery](../README.md) |
| Previous | [V08/C02 — Supply chain and release verification](../c02/README.md) |
| Next | [V08/C04 — GitOps, rollout and progressive delivery](../c04/README.md) |
| Prerequisite | [V08/C02 — Supply chain and release verification](../c02/README.md) |
| Source reading | [Page-local evidence and versions](runtime-placement-and-control-plane.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.
