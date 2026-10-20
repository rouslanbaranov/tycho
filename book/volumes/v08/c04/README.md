---
metadata_version: 1
id: "tycho.chapter.5e4761e1a3e34c2f8023ec8ac4fa81d5"
kind: "chapter"
parent_id: "tycho.volume.cb10070ba233477fae8aa5d18e74fee8"
canonical_path: "book/volumes/v08/c04/README.md"
title: "V08/C04 — GitOps, rollout and progressive delivery"
topic_ids:
  - "software-delivery"
perspectives:
  - "architecture"
  - "evaluation"
summary: "How do rolling, blue/green, canary, rollback and analysis gates differ?"
route_hints:
  questions:
    - "How do rolling, blue/green, canary, rollback and analysis gates differ?"
  prerequisites:
    - "tycho.chapter.94b4b6d9e2e1490abd0055a5265141ff"
  related_ids:
    - "tycho.chapter.8a2d2a79846d4567bb3d33957e19977f"
  excludes:
    - "No new benchmark, source inspection or independent edition review is asserted."
  keywords:
    - "system-design"
    - "edition-navigation"
evidence_scope:
  source_ids:
    - "src.k8s-deployments"
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

# V08/C04 — GitOps, rollout and progressive delivery

## Purpose and mission

How do rolling, blue/green, canary, rollback and analysis gates differ? This chapter owns that question within delivery, deployment and disaster recovery. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Define exposure, analysis, stop and recovery conditions across both application versions and shared data.

A small canary can write incompatible state visible to all old instances; limiting traffic alone does not bound that effect. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

| Page | Owning question |
|---|---|
| [GitOps, rolling, blue/green and canary release architecture](gitops-canary-and-progressive-rollout.md) | How do rolling, blue/green, canary, rollback and analysis gates differ? |

The page is one bounded explanation. Its mechanism, failure analysis and evidence are kept together rather than split to meet a numerical page quota. Use these section entry points:

- [1. GitOps reconciles desired configuration, not business outcomes](gitops-canary-and-progressive-rollout.md#1-gitops-reconciles-desired-configuration-not-business-outcomes).
- [2. Release strategies and their limits](gitops-canary-and-progressive-rollout.md#2-release-strategies-and-their-limits).
- [6. Proposed negative experiments](gitops-canary-and-progressive-rollout.md#6-proposed-negative-experiments).
- [7. Public source ledger](gitops-canary-and-progressive-rollout.md#7-public-source-ledger).

## Boundaries and further reading

- [V08/C01 — CI/CD architecture and artifact provenance](../c01/README.md) owns the adjacent question; compare assumptions before transferring the conclusion.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V08 — Delivery, deployment and disaster recovery](../README.md) |
| Previous | [V08/C03 — VMs, containers, orchestration and serverless](../c03/README.md) |
| Next | [V08/C05 — Backward-compatible database change](../c05/README.md) |
| Prerequisite | [V08/C03 — VMs, containers, orchestration and serverless](../c03/README.md) |
| Source reading | [Page-local evidence and versions](gitops-canary-and-progressive-rollout.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.
