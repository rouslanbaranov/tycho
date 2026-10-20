---
metadata_version: 1
id: "tycho.chapter.9e35eb7b056f428093e36a2faf644a23"
kind: "chapter"
parent_id: "tycho.volume.cb10070ba233477fae8aa5d18e74fee8"
canonical_path: "book/volumes/v08/c06/README.md"
title: "V08/C06 — High availability and failure-domain placement"
topic_ids:
  - "deployment-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: "What survives machine, zone, dependency or region loss?"
route_hints:
  questions:
    - "What survives machine, zone, dependency or region loss?"
  prerequisites:
    - "tycho.chapter.7d434d1a41e142d38bb729ee124ac548"
  related_ids: []
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

| Page | Owning question |
|---|---|
| [Availability zones, placement and failure-domain architecture](availability-zones-placement-and-failure-domains.md) | What survives machine, zone, dependency or region loss? |

The page is one bounded explanation. Its mechanism, failure analysis and evidence are kept together rather than split to meet a numerical page quota. Use these section entry points:

- [1. Failure domains are dependency sets, not just geographical labels](availability-zones-placement-and-failure-domains.md#1-failure-domains-are-dependency-sets-not-just-geographical-labels).
- [2. Redundancy must be combined with correct traffic routing](availability-zones-placement-and-failure-domains.md#2-redundancy-must-be-combined-with-correct-traffic-routing).
- [Engineering walkthrough — Two zones, one shared dependency and no real isolation](availability-zones-placement-and-failure-domains.md#engineering-walkthrough-two-zones-one-shared-dependency-and-no-real-isolation).
- [7. Evidence ledger and limits](availability-zones-placement-and-failure-domains.md#7-evidence-ledger-and-limits).

## Boundaries and further reading

The preceding and following chapters supply context; this landing does not replace their canonical mechanisms. Follow the exact source ledger on the child page when a claim depends on a product version or historical period.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V08 — Delivery, deployment and disaster recovery](../README.md) |
| Previous | [V08/C05 — Backward-compatible database change](../c05/README.md) |
| Next | [V08/C07 — Multi-region recovery and data reconciliation](../c07/README.md) |
| Prerequisite | [V08/C05 — Backward-compatible database change](../c05/README.md) |
| Source reading | [Page-local evidence and versions](availability-zones-placement-and-failure-domains.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.
