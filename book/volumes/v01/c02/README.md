---
metadata_version: 1
id: "tycho.chapter.316b50ac3db440ae82c0986b896ff468"
kind: "chapter"
parent_id: "tycho.volume.4d10f5c93f3b4356a553c8732e513a38"
canonical_path: "book/volumes/v01/c02/README.md"
title: "V01/C02 — Workload and demand models"
topic_ids:
  - "performance-engineering"
perspectives:
  - "architecture"
  - "evaluation"
summary: "How do active users, offered arrivals, concurrency, operation mix and skew differ?"
route_hints:
  questions:
    - "How do active users, offered arrivals, concurrency, operation mix and skew differ?"
  prerequisites:
    - "tycho.chapter.9d4f989ec9304e418f60f1ad7248094a"
  related_ids:
    - "tycho.chapter.e365b78505784c20a4f3d72fe7904d9b"
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

# V01/C02 — Workload and demand models

## Purpose and mission

How do active users, offered arrivals, concurrency, operation mix and skew differ? This chapter owns that question within requirements, quality attributes and architecture fundamentals. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Separate offered attempts, admitted work, successful outcomes, concurrency and per-operation demand before estimating capacity.

Two equally sized user populations can impose different bursts and hot-key pressure; average requests per second conceals that difference. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

| Page | Owning question |
|---|---|
| [Workload and demand models: from user behavior to measurable offered work](workload-demand-and-arrival-models.md) | How do active users, offered arrivals, concurrency, operation mix and skew differ? |

The page is one bounded explanation. Its mechanism, failure analysis and evidence are kept together rather than split to meet a numerical page quota. Use these section entry points:

- [1. Workload nouns that must not be interchanged](workload-demand-and-arrival-models.md#1-workload-nouns-that-must-not-be-interchanged).
- [2. Arrival shape is part of the architecture requirement](workload-demand-and-arrival-models.md#2-arrival-shape-is-part-of-the-architecture-requirement).
- [7. Architecture implications are conditional](workload-demand-and-arrival-models.md#7-architecture-implications-are-conditional).
- [8. Public evidence and unverified claims](workload-demand-and-arrival-models.md#8-public-evidence-and-unverified-claims).

## Boundaries and further reading

- [V07/C01 — Queueing, Little's Law and measurement boundaries](../../v07/c01/README.md) owns the adjacent question; compare assumptions before transferring the conclusion.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V01 — Requirements, quality attributes and architecture fundamentals](../README.md) |
| Previous | [V01/C01 — Problem framing and system boundaries](../c01/README.md) |
| Next | [V01/C03 — Quality attributes and trade-offs](../c03/README.md) |
| Prerequisite | [V01/C01 — Problem framing and system boundaries](../c01/README.md) |
| Source reading | [Page-local evidence and versions](workload-demand-and-arrival-models.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.
