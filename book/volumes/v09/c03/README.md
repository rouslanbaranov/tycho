---
metadata_version: 1
id: "tycho.chapter.03ec5acf85e043a5a6d552a036bf4659"
kind: "chapter"
parent_id: "tycho.volume.4a94b1e6f8234841afaa51af14330627"
canonical_path: "book/volumes/v09/c03/README.md"
title: "V09/C03 — Distributed tracing and propagation"
topic_ids:
  - "observability"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Which context, sampling and async boundaries determine trace usefulness?"
route_hints:
  questions:
    - "Which context, sampling and async boundaries determine trace usefulness?"
  prerequisites:
    - "tycho.chapter.ef166b5f7d76454ca4c8a685c6ce033e"
  related_ids:
    - "tycho.chapter.49cb8db3af4e406ea6988c8e5e852acf"
  excludes:
    - "No new benchmark, source inspection or independent edition review is asserted."
  keywords:
    - "system-design"
    - "edition-navigation"
evidence_scope:
  source_ids:
    - "src.trace-context"
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

# V09/C03 — Distributed tracing and propagation

## Purpose and mission

Which context, sampling and async boundaries determine trace usefulness? This chapter owns that question within observability, security and operational architecture. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Interpret traces as sampled, propagated observations with explicit trust and asynchronous boundaries.

A missing span does not prove no effect occurred, and untrusted baggage must not become an authorization decision. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

| Page | Owning question |
|---|---|
| [Distributed tracing: context propagation, sampling and causal limits](distributed-tracing-context-and-sampling.md) | Which context, sampling and async boundaries determine trace usefulness? |

The page is one bounded explanation. Its mechanism, failure analysis and evidence are kept together rather than split to meet a numerical page quota. Use these section entry points:

- [1. A trace, a span and a request are different entities](distributed-tracing-context-and-sampling.md#1-a-trace-a-span-and-a-request-are-different-entities).
- [2. Causal and temporal interpretation](distributed-tracing-context-and-sampling.md#2-causal-and-temporal-interpretation).
- [6. Original diagnostic decision](distributed-tracing-context-and-sampling.md#6-original-diagnostic-decision).
- [7. Public source ledger and nonclaims](distributed-tracing-context-and-sampling.md#7-public-source-ledger-and-nonclaims).

## Boundaries and further reading

- [V09/C04 — Logging, audit and lineage](../c04/README.md) owns the adjacent question; compare assumptions before transferring the conclusion.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V09 — Observability, security and operational architecture](../README.md) |
| Previous | [V09/C02 — Metrics ingestion, cardinality and time-series storage](../c02/README.md) |
| Next | [V09/C04 — Logging, audit and lineage](../c04/README.md) |
| Prerequisite | [V09/C02 — Metrics ingestion, cardinality and time-series storage](../c02/README.md) |
| Source reading | [Page-local evidence and versions](distributed-tracing-context-and-sampling.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.
