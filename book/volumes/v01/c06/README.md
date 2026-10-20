---
metadata_version: 1
id: "tycho.chapter.bbfd14751d274868b152ba431dc904c9"
kind: "chapter"
parent_id: "tycho.volume.4d10f5c93f3b4356a553c8732e513a38"
canonical_path: "book/volumes/v01/c06/README.md"
title: "V01/C06 — Capacity, operational constraints and total cost"
topic_ids:
  - "application-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Which hard gates and team/budget limits invalidate otherwise appealing options?"
route_hints:
  questions:
    - "Which hard gates and team/budget limits invalidate otherwise appealing options?"
  prerequisites:
    - "tycho.chapter.abcbb298887b49e79525ca00fead8926"
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

# V01/C06 — Capacity, operational constraints and total cost

## Purpose and mission

Which hard gates and team/budget limits invalidate otherwise appealing options? This chapter owns that question within requirements, quality attributes and architecture fundamentals. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Reject candidates that exceed an explicit operating, recovery, staffing or total-cost constraint before ranking attractive features.

A low instance price can conceal migration, dual-running and rollback costs; uncertain inputs must remain uncertain instead of becoming precise forecasts. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

| Page | Owning question |
|---|---|
| [Capacity, operational constraints and total-cost hard gates](operational-constraints-and-total-cost-gates.md) | Which hard gates and team/budget limits invalidate otherwise appealing options? |

The page is one bounded explanation. Its mechanism, failure analysis and evidence are kept together rather than split to meet a numerical page quota. Use these section entry points:

- [1. Constraints must be typed and owned](operational-constraints-and-total-cost-gates.md#1-constraints-must-be-typed-and-owned).
- [2. Separate hard feasibility from preference scoring](operational-constraints-and-total-cost-gates.md#2-separate-hard-feasibility-from-preference-scoring).
- [7. Source-to-claim ledger and limitations](operational-constraints-and-total-cost-gates.md#7-source-to-claim-ledger-and-limitations).
- [Engineering walkthrough — Hard constraints before weighted cost scoring](operational-constraints-and-total-cost-gates.md#engineering-walkthrough-hard-constraints-before-weighted-cost-scoring).

## Boundaries and further reading

The preceding and following chapters supply context; this landing does not replace their canonical mechanisms. Follow the exact source ledger on the child page when a claim depends on a product version or historical period.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V01 — Requirements, quality attributes and architecture fundamentals](../README.md) |
| Previous | [V01/C05 — Architecture descriptions and decision records](../c05/README.md) |
| Next | [V02/C01 — Layered, modular and ports-and-adapters design](../../v02/c01/README.md) |
| Prerequisite | [V01/C05 — Architecture descriptions and decision records](../c05/README.md) |
| Source reading | [Page-local evidence and versions](operational-constraints-and-total-cost-gates.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.
