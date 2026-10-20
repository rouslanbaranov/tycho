---
metadata_version: 1
id: "tycho.chapter.9d4f989ec9304e418f60f1ad7248094a"
kind: "chapter"
parent_id: "tycho.volume.4d10f5c93f3b4356a553c8732e513a38"
canonical_path: "book/volumes/v01/c01/README.md"
title: "V01/C01 — Problem framing and system boundaries"
topic_ids:
  - "application-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Which actors, outcomes, interfaces and external failure dependencies define the system?"
route_hints:
  questions:
    - "Which actors, outcomes, interfaces and external failure dependencies define the system?"
  prerequisites: []
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

# V01/C01 — Problem framing and system boundaries

## Purpose and mission

Which actors, outcomes, interfaces and external failure dependencies define the system? This chapter owns that question within requirements, quality attributes and architecture fundamentals. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Draw the outcome boundary before selecting a component boundary: name the caller, authoritative effect, external decision owner and recovery lookup.

A third-party timeout can leave an external effect committed while the local request is unresolved; moving the dependency outside a diagram does not remove that obligation. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

| Page | Owning question |
|---|---|
| [Problem framing and system boundaries: architecture begins outside the code](problem-framing-and-system-boundaries.md) | Which actors, outcomes, interfaces and external failure dependencies define the system? |

The page is one bounded explanation. Its mechanism, failure analysis and evidence are kept together rather than split to meet a numerical page quota. Use these section entry points:

- [1. Begin with observable outcomes](problem-framing-and-system-boundaries.md#1-begin-with-observable-outcomes).
- [2. Separate business context from technical context](problem-framing-and-system-boundaries.md#2-separate-business-context-from-technical-context).
- [8. Public evidence and review limitations](problem-framing-and-system-boundaries.md#8-public-evidence-and-review-limitations).
- [Engineering walkthrough — Third-party outage exposes a missing system boundary](problem-framing-and-system-boundaries.md#engineering-walkthrough-third-party-outage-exposes-a-missing-system-boundary).

## Boundaries and further reading

The preceding and following chapters supply context; this landing does not replace their canonical mechanisms. Follow the exact source ledger on the child page when a claim depends on a product version or historical period.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V01 — Requirements, quality attributes and architecture fundamentals](../README.md) |
| Previous | [Book contents](../../../README.md) |
| Next | [V01/C02 — Workload and demand models](../c02/README.md) |
| Source reading | [Page-local evidence and versions](problem-framing-and-system-boundaries.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.
