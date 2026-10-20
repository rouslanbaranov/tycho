---
metadata_version: 1
id: "tycho.chapter.8a2d2a79846d4567bb3d33957e19977f"
kind: "chapter"
parent_id: "tycho.volume.cb10070ba233477fae8aa5d18e74fee8"
canonical_path: "book/volumes/v08/c01/README.md"
title: "V08/C01 — CI/CD architecture and artifact provenance"
topic_ids:
  - "software-delivery"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Which boundaries separate build, test, publication and production deployment?"
route_hints:
  questions:
    - "Which boundaries separate build, test, publication and production deployment?"
  prerequisites:
    - "tycho.chapter.53b6bb88a00549e491949aeb426b83f2"
    - "tycho.chapter.4a3cbf0617e44be5b1e8d72568109dad"
    - "tycho.chapter.18aa94285a164b6f94530cebcfd87b8b"
    - "tycho.chapter.3d0f6dd1e8e94cd397326e129b5c287f"
    - "tycho.chapter.388c48be24414421a63481b37d05fdce"
  related_ids:
    - "tycho.chapter.5e4761e1a3e34c2f8023ec8ac4fa81d5"
  excludes:
    - "No new benchmark, source inspection or independent edition review is asserted."
  keywords:
    - "system-design"
    - "edition-navigation"
evidence_scope:
  source_ids:
    - "src.opengitops"
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

# V08/C01 — CI/CD architecture and artifact provenance

## Purpose and mission

Which boundaries separate build, test, publication and production deployment? This chapter owns that question within delivery, deployment and disaster recovery. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Keep source revision, build identity, artifact digest, promotion and user-health acceptance as separate release boundaries.

A successful pipeline run does not prove that the intended artifact was deployed or that its persisted effects remain correct. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

| Page | Owning question |
|---|---|
| [CI/CD architecture, artifact provenance and GitOps reconciliation](ci-cd-provenance-and-gitops.md) | Which boundaries separate build, test, publication and production deployment? |

The page is one bounded explanation. Its mechanism, failure analysis and evidence are kept together rather than split to meet a numerical page quota. Use these section entry points:

- [1. Five separately controlled boundaries](ci-cd-provenance-and-gitops.md#1-five-separately-controlled-boundaries).
- [2. Workflow and runner topology](ci-cd-provenance-and-gitops.md#2-workflow-and-runner-topology).
- [Engineering walkthrough — Compromised build worker and a tempting image rollback](ci-cd-provenance-and-gitops.md#engineering-walkthrough-compromised-build-worker-and-a-tempting-image-rollback).
- [Applied M9 evidence: what transfers and what does not](ci-cd-provenance-and-gitops.md#applied-m9-evidence-what-transfers-and-what-does-not).

## Boundaries and further reading

- [V08/C04 — GitOps, rollout and progressive delivery](../c04/README.md) owns the adjacent question; compare assumptions before transferring the conclusion.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V08 — Delivery, deployment and disaster recovery](../README.md) |
| Previous | [V07/C07 — Capacity planning and cost/performance trade-offs](../../v07/c07/README.md) |
| Next | [V08/C02 — Supply chain and release verification](../c02/README.md) |
| Prerequisite | [V02/C05 — Public APIs, HTTP/RPC and compatibility](../../v02/c05/README.md) |
| Prerequisite | [V04/C03 — Consistency and distributed transactions](../../v04/c03/README.md) |
| Prerequisite | [V04/C05 — Outbox, inbox, sagas and durable workflows](../../v04/c05/README.md) |
| Prerequisite | [V05/C06 — Schema evolution, data migration and retention](../../v05/c06/README.md) |
| Prerequisite | [V05/C07 — Replication, backups and restore drills](../../v05/c07/README.md) |
| Source reading | [Page-local evidence and versions](ci-cd-provenance-and-gitops.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.
