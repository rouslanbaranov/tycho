---
metadata_version: 1
id: "tycho.chapter.510c0c78de2b450c8be93d708222a488"
kind: "chapter"
parent_id: "tycho.volume.c0927de8450647c49e2d33774eeb60be"
canonical_path: "book/volumes/v04/c01/README.md"
title: "V04/C01 — Time, causality and ordering"
topic_ids:
  - "distributed-systems"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Which ordering can a distributed system observe or guarantee?"
route_hints:
  questions:
    - "Which ordering can a distributed system observe or guarantee?"
  prerequisites:
    - "tycho.chapter.7031445877fb4f8d831d962d170521c8"
    - "tycho.chapter.53b6bb88a00549e491949aeb426b83f2"
    - "tycho.chapter.b9bf60e22dc04878a05aeca98610b5d1"
    - "tycho.chapter.e436af815dc442f694deb55966077d9e"
  related_ids:
    - "tycho.chapter.6eba0cf391184a709f2e23e5ecc1c3d2"
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

# V04/C01 — Time, causality and ordering

## Purpose and mission

Which ordering can a distributed system observe or guarantee? This chapter owns that question within distributed coordination and event integration. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Distinguish causal precedence, concurrent events and a chosen total order before relying on timestamps.

Clock order cannot prove that one event observed another, and an ordered log alone does not establish a business invariant. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

| Page | Owning question |
|---|---|
| [Causality, ordering and consensus in distributed systems](causality-ordering-and-consensus.md) | Which ordering can a distributed system observe or guarantee? |

The page is one bounded explanation. Its mechanism, failure analysis and evidence are kept together rather than split to meet a numerical page quota. Use these section entry points:

- [1. The happens-before relation describes causal knowledge](causality-ordering-and-consensus.md#1-the-happens-before-relation-describes-causal-knowledge).
- [2. Agreement, linearizability and availability solve different problems](causality-ordering-and-consensus.md#2-agreement-linearizability-and-availability-solve-different-problems).
- [Engineering walkthrough — Wall-clock order cannot prove causality or commit order](causality-ordering-and-consensus.md#engineering-walkthrough-wall-clock-order-cannot-prove-causality-or-commit-order).
- [Exact public evidence](causality-ordering-and-consensus.md#exact-public-evidence).

## Boundaries and further reading

- [V04/C02 — Replication, consensus and leader changes](../c02/README.md) owns the adjacent question; compare assumptions before transferring the conclusion.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V04 — Distributed coordination and event integration](../README.md) |
| Previous | [V03/C06 — Memory, GC, CPU and blocking diagnostics](../../v03/c06/README.md) |
| Next | [V04/C02 — Replication, consensus and leader changes](../c02/README.md) |
| Prerequisite | [V02/C02 — Domain boundaries, data ownership and contracts](../../v02/c02/README.md) |
| Prerequisite | [V02/C05 — Public APIs, HTTP/RPC and compatibility](../../v02/c05/README.md) |
| Prerequisite | [V03/C03 — Reactive streams, demand and cancellation](../../v03/c03/README.md) |
| Prerequisite | [V03/C05 — Thread, connection and buffer pools](../../v03/c05/README.md) |
| Source reading | [Page-local evidence and versions](causality-ordering-and-consensus.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.
