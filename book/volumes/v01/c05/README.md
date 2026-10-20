---
metadata_version: 1
id: "tycho.chapter.abcbb298887b49e79525ca00fead8926"
kind: "chapter"
parent_id: "tycho.volume.4d10f5c93f3b4356a553c8732e513a38"
canonical_path: "book/volumes/v01/c05/README.md"
title: "V01/C05 — Architecture descriptions and decision records"
topic_ids:
  - "application-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: "What belongs in diagrams, views, assumptions, ADRs and source-linked evidence?"
route_hints:
  questions:
    - "What belongs in diagrams, views, assumptions, ADRs and source-linked evidence?"
  prerequisites:
    - "tycho.chapter.ee2cd95003ab4018a9d49e2ff0b6b2f4"
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

# V01/C05 — Architecture descriptions and decision records

## Purpose and mission

What belongs in diagrams, views, assumptions, ADRs and source-linked evidence? This chapter owns that question within requirements, quality attributes and architecture fundamentals. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Use consistent identities across context, runtime, deployment and decision views so a failure can be followed without changing its meaning.

A tidy component view does not establish a working timeout, permission or recovery contract; follow the same ambiguous operation through every relevant view. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

| Page | Owning question |
|---|---|
| [Architecture descriptions, complementary views and decision records](architecture-views-and-decision-records.md) | What belongs in diagrams, views, assumptions, ADRs and source-linked evidence? |

The page is one bounded explanation. Its mechanism, failure analysis and evidence are kept together rather than split to meet a numerical page quota. Use these section entry points:

- [1. Start with concerns and a coherent vocabulary](architecture-views-and-decision-records.md#1-start-with-concerns-and-a-coherent-vocabulary).
- [2. The main views answer separate questions](architecture-views-and-decision-records.md#2-the-main-views-answer-separate-questions).
- [7. Public source ledger and limits](architecture-views-and-decision-records.md#7-public-source-ledger-and-limits).
- [Engineering walkthrough — Reconciling one failure across architectural views](architecture-views-and-decision-records.md#engineering-walkthrough-reconciling-one-failure-across-architectural-views).

## Boundaries and further reading

The preceding and following chapters supply context; this landing does not replace their canonical mechanisms. Follow the exact source ledger on the child page when a claim depends on a product version or historical period.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V01 — Requirements, quality attributes and architecture fundamentals](../README.md) |
| Previous | [V01/C04 — Evidence, hypotheses and architecture experiments](../c04/README.md) |
| Next | [V01/C06 — Capacity, operational constraints and total cost](../c06/README.md) |
| Prerequisite | [V01/C04 — Evidence, hypotheses and architecture experiments](../c04/README.md) |
| Source reading | [Page-local evidence and versions](architecture-views-and-decision-records.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.
