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
summary: "Which failure assumptions sustain agreement or availability? The reading route separates 2 detailed questions from the integrated decision."
route_hints:
  questions:
    - "Which failure assumptions sustain agreement or availability?"
  prerequisites:
    - "tycho.chapter.510c0c78de2b450c8be93d708222a488"
  related_ids:
    - "tycho.chapter.510c0c78de2b450c8be93d708222a488"
    - "tycho.page.1b2657011d454460856103419095031b"
    - "tycho.page.b93c892861fb4dd4afcfbdc2ced1af80"
    - "tycho.page.4961bb03a6534242a0977db265b68d95"
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

Begin with the integrated decision, then open the independent question that matches the missing mechanism or observed failure. Read source limits before applying the conclusion.

| Page | Independent question and role |
|---|---|
| [Integrated decision and original walkthrough](replication-consensus-and-leader-change.md) | Which failure assumptions sustain agreement or availability? |
| [Replica properties and quorum failure envelopes](quorum-envelope.md) | Which partitions can make progress without allowing divergent authority? |
| [Leader changes, reconfiguration and restoration](leader-recovery.md) | How should clients classify outcomes while leadership or membership changes? |


## Additional mechanism and project routes

These independently scoped pages extend the chapter without replacing its original walkthrough or source ledger.

| Page | Owning question |
| --- | --- |
| [Session-visible consistency](session-consistency.md) | Which observations must a user session retain when requests move between replicas? |

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


## Further mechanism and recovery questions

- [Leases, stale owners and fencing at the destination](leader-recovery.md#leases-stale-owners-and-fencing-at-the-destination) — source-scoped enrichment; examples and proposed tests are not executed results.

## Chapter source ledger

The following original citation rows, review limits and earlier topical routes are retained once for this chapter. Each question page points here and retains its inline citations. Evidence coverage must be judged at the actual claim and version, not inferred from source-list length.

<!-- tycho-question-source:tycho.page.1b2657011d454460856103419095031b:8 -->
## 7. Source ledger and limitations

| Public source reviewed | Narrow support | Not established |
|---|---|---|
| [Raft project — Ongaro/Ousterhout extended consensus paper](https://raft.github.io/) | Leader-based log replication, terms, elections and safety principles | Correctness of an invented or third-party service implementation |
| [etcd 3.6 FAQ, membership and quorum](https://etcd.io/docs/v3.6/faq/) | Majority calculations and reconfiguration hazards | Resilience of an untested specific cluster |
| [Tycho causality/consensus page](../c01/causality-ordering-and-consensus.md) | Existing source-grounded related consensus concepts | A checked formal proof or live fault test |

Every failure, cluster layout, client result and diagram above is an original illustrative proposal. No environment, network, snapshot or node was touched. Actual versioned replication behavior and chapter-level technical review remain outstanding.

**Navigation:** proposed **V04/C02** in [outline](../../../PROPOSED-STRUCTURE.md), current [Distributed coordination landing](../../../distributed/README.md). Background: [Causal ordering and consensus](../c01/causality-ordering-and-consensus.md), [Isolation and sagas](../c03/transaction-isolation-and-sagas.md), [Safe recovery](../../../deployment/multi-region-disaster-recovery-contracts.md).
<!-- /tycho-question-source -->
