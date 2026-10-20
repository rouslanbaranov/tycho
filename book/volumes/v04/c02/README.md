---
metadata_version: 1
id: "tycho.chapter.6eba0cf391184a709f2e23e5ecc1c3d2"
kind: "chapter"
parent_id: "tycho.volume.c0927de8450647c49e2d33774eeb60be"
canonical_path: "book/volumes/v04/c02/README.md"
title: "V04/C02 — Replication, consensus and leader changes"
topic_ids:
  - "distributed-systems"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Which failure assumptions sustain agreement or availability?"
route_hints:
  questions:
    - "Which failure assumptions sustain agreement or availability?"
  prerequisites:
    - "tycho.chapter.510c0c78de2b450c8be93d708222a488"
  related_ids:
    - "tycho.chapter.510c0c78de2b450c8be93d708222a488"
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

# V04/C02 — Replication, consensus and leader changes

## Purpose and mission

Which failure assumptions sustain agreement or availability? This chapter owns that question within distributed coordination and event integration. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

State fault assumptions, quorum rules, leader terms and client-visible outcomes when explaining replicated authority.

An isolated former leader must not continue accepting authoritative effects merely because its process is healthy. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

| Page | Owning question |
|---|---|
| [Replication, consensus and leader change: safety and progress under failures](replication-consensus-and-leader-change.md) | Which failure assumptions sustain agreement or availability? |

The page is one bounded explanation. Its mechanism, failure analysis and evidence are kept together rather than split to meet a numerical page quota. Use these section entry points:

- [1. Separate replica types and required properties](replication-consensus-and-leader-change.md#1-separate-replica-types-and-required-properties).
- [2. Majority quorum arithmetic and the failure envelope](replication-consensus-and-leader-change.md#2-majority-quorum-arithmetic-and-the-failure-envelope).
- [Engineering walkthrough — New leader, old client and a lost acknowledgment](replication-consensus-and-leader-change.md#engineering-walkthrough-new-leader-old-client-and-a-lost-acknowledgment).
- [7. Source ledger and limitations](replication-consensus-and-leader-change.md#7-source-ledger-and-limitations).

## Boundaries and further reading

- [V04/C01 — Time, causality and ordering](../c01/README.md) owns the adjacent question; compare assumptions before transferring the conclusion.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V04 — Distributed coordination and event integration](../README.md) |
| Previous | [V04/C01 — Time, causality and ordering](../c01/README.md) |
| Next | [V04/C03 — Consistency and distributed transactions](../c03/README.md) |
| Prerequisite | [V04/C01 — Time, causality and ordering](../c01/README.md) |
| Source reading | [Page-local evidence and versions](replication-consensus-and-leader-change.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.
