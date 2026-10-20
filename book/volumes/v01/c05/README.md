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
summary: "What belongs in diagrams, views, assumptions, ADRs and source-linked evidence? The reading route separates 2 detailed questions from the integrated decision."
route_hints:
  questions:
    - "What belongs in diagrams, views, assumptions, ADRs and source-linked evidence?"
  prerequisites:
    - "tycho.chapter.ee2cd95003ab4018a9d49e2ff0b6b2f4"
  related_ids:
    - "tycho.page.b42e3ffc4a924b7089d261d0a3dc33b0"
    - "tycho.page.13760750168f4e339d5d014e189828af"
    - "tycho.page.629374fc3ed84a848794c0b63c4d4ddf"
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

Begin with the integrated decision, then open the independent question that matches the missing mechanism or observed failure. Read source limits before applying the conclusion.

| Page | Independent question and role |
|---|---|
| [Integrated decision and original walkthrough](architecture-views-and-decision-records.md) | What belongs in diagrams, views, assumptions, ADRs and source-linked evidence? |
| [Concerns and architectural views](concerns-views.md) | Which concern is answered by a context, building-block, runtime or deployment view? |
| [Identity and evolving decision records](identity-adrs.md) | How do stable identities and ADRs keep several views coherent through change? |

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

## Chapter source ledger

The following original citation rows, review limits and earlier topical routes are retained once for this chapter. Each question page points here and retains its inline citations. Evidence coverage must be judged at the actual claim and version, not inferred from source-list length.

<!-- tycho-question-source:tycho.page.b42e3ffc4a924b7089d261d0a3dc33b0:7 -->
## 7. Public source ledger and limits

| Public arc42 section inspected | Narrowly supported subject | Not demonstrated |
|---|---|---|
| [§3 Context and Scope](https://docs.arc42.org/section-3/) | External business and technical context | Fictional partners' real contracts |
| [§5 Building Block View](https://docs.arc42.org/section-5/) | Static hierarchy, responsibilities and interface/dependency abstraction | Enforced module dependencies in code |
| [§6 Runtime View](https://docs.arc42.org/section-6/) | Representative user and failure scenarios | A trace or runtime experiment |
| [§7 Deployment View](https://docs.arc42.org/section-7/) | Software mapping to physical/runtime infrastructure | A running, validated deployment |
| [§9 Architecture Decisions](https://docs.arc42.org/section-9/) | Context, rationale, rejected alternatives and decision lifecycle | Approval of ADR-SYN-08 |

Every component, failure path, ID and table in the fictional case is original teaching material. No real system, diagram export, experiment, source code, stakeholder acceptance or independent editorial approval was examined. This chapter needs integration into final volume/page structure.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.b42e3ffc4a924b7089d261d0a3dc33b0:9 -->
## Navigation

Proposed owner **V01/C05** in [the 69-chapter outline](../../../PROPOSED-STRUCTURE.md); current [application/foundations landing](../../../application/README.md). Read first [system boundaries](../c01/problem-framing-and-system-boundaries.md), then [quality drivers](../c03/quality-drivers-and-architecture-views.md), [modular boundaries](../../../application/architecture-styles-and-module-boundaries.md), [architectural alternatives and ADRs](../../v10/c04/architecture-alternatives-experiments-and-adrs.md).
<!-- /tycho-question-source -->
