---
metadata_version: 1
id: "tycho.chapter.b7924b3db65949df952fbb5ca706236c"
kind: "chapter"
parent_id: "tycho.volume.f7679623ca274bff8a00389d409d68c6"
canonical_path: "book/volumes/v07/c07/README.md"
title: "V07/C07 — Capacity planning and cost/performance trade-offs"
topic_ids:
  - "performance-engineering"
perspectives:
  - "architecture"
  - "evaluation"
summary: "What experiments can confirm or falsify a scaling hypothesis?"
route_hints:
  questions:
    - "What experiments can confirm or falsify a scaling hypothesis?"
  prerequisites:
    - "tycho.chapter.1d8d87e683bc428e8dbed087106f37fd"
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

# V07/C07 — Capacity planning and cost/performance trade-offs

## Purpose and mission

What experiments can confirm or falsify a scaling hypothesis? This chapter owns that question within performance, scale and resilience under load. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Compare correct work per total operating cost over steady, peak and degraded conditions with sensitivity to uncertain inputs.

Raw requests per second per instance ignores rejected work, recovery and shared-state costs; an apparent optimum can violate a hard requirement. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

| Page | Owning question |
|---|---|
| [Capacity planning and cost/performance trade-offs](capacity-planning-and-cost-performance.md) | What experiments can confirm or falsify a scaling hypothesis? |

The page is one bounded explanation. Its mechanism, failure analysis and evidence are kept together rather than split to meet a numerical page quota. Use these section entry points:

- [1. Write a capacity envelope, not a magic instance count](capacity-planning-and-cost-performance.md#1-write-a-capacity-envelope-not-a-magic-instance-count).
- [2. Cost must include more than infrastructure instance prices](capacity-planning-and-cost-performance.md#2-cost-must-include-more-than-infrastructure-instance-prices).
- [7. Public sources and nonclaims](capacity-planning-and-cost-performance.md#7-public-sources-and-nonclaims).
- [Engineering walkthrough — Provision, shed, optimize or simplify under uncertain prices](capacity-planning-and-cost-performance.md#engineering-walkthrough-provision-shed-optimize-or-simplify-under-uncertain-prices).

## Boundaries and further reading

The preceding and following chapters supply context; this landing does not replace their canonical mechanisms. Follow the exact source ledger on the child page when a claim depends on a product version or historical period.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V07 — Performance, scale and resilience under load](../README.md) |
| Previous | [V07/C06 — Horizontal/vertical scaling and autoscaling delay](../c06/README.md) |
| Next | [V08/C01 — CI/CD architecture and artifact provenance](../../v08/c01/README.md) |
| Prerequisite | [V07/C06 — Horizontal/vertical scaling and autoscaling delay](../c06/README.md) |
| Source reading | [Page-local evidence and versions](capacity-planning-and-cost-performance.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.
