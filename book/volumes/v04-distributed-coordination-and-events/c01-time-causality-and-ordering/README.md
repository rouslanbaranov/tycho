---
metadata_version: 1
id: "tycho.chapter.510c0c78de2b450c8be93d708222a488"
kind: "chapter"
parent_id: "tycho.volume.c0927de8450647c49e2d33774eeb60be"
canonical_path: "book/volumes/v04-distributed-coordination-and-events/c01-time-causality-and-ordering/README.md"
title: "V04/C01 — Time, causality and ordering"
topic_ids:
  - "distributed-systems"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Which ordering can a distributed system observe or guarantee? The reading route separates 2 detailed questions from the integrated decision."
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
    - "tycho.page.d4822cc1e71c4f73896b7f6509f6daae"
    - "tycho.page.a0d3dfe1c8a245e98d9c9ae4813b8c85"
    - "tycho.page.d664f65295644726ae1234a982f81fa8"
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

Begin with the integrated decision, then open the independent question that matches the missing mechanism or observed failure. Read source limits before applying the conclusion.

| Page | Independent question and role |
|---|---|
| [Integrated decision and original walkthrough](causality-ordering-and-consensus.md) | Which ordering can a distributed system observe or guarantee? |
| [Causal knowledge and ordering scope](causal-order.md) | What can happens-before, timestamps and per-key order each establish? |
| [Agreement, availability and uncertain observations](agreement-failure.md) | Which fault assumption separates an ordering claim from an agreement guarantee? |

## Boundaries and further reading

- [V04/C02 — Replication, consensus and leader changes](../c02-replication-consensus-and-leader-changes/README.md) owns the adjacent question; compare assumptions before transferring the conclusion.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V04 — Distributed coordination and event integration](../README.md) |
| Previous | [V03/C06 — Memory, GC, CPU and blocking diagnostics](../../v03-execution-concurrency-and-flow-control/c06-memory-gc-cpu-and-blocking-diagnostics/README.md) |
| Next | [V04/C02 — Replication, consensus and leader changes](../c02-replication-consensus-and-leader-changes/README.md) |
| Prerequisite | [V02/C02 — Domain boundaries, data ownership and contracts](../../v02-application-boundaries-and-contracts/c02-domain-boundaries-data-ownership-and-contracts/README.md) |
| Prerequisite | [V02/C05 — Public APIs, HTTP/RPC and compatibility](../../v02-application-boundaries-and-contracts/c05-public-apis-http-rpc-and-compatibility/README.md) |
| Prerequisite | [V03/C03 — Reactive streams, demand and cancellation](../../v03-execution-concurrency-and-flow-control/c03-reactive-streams-demand-and-cancellation/README.md) |
| Prerequisite | [V03/C05 — Thread, connection and buffer pools](../../v03-execution-concurrency-and-flow-control/c05-thread-connection-and-buffer-pools/README.md) |
| Source reading | [Page-local evidence and versions](causality-ordering-and-consensus.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.


## Further mechanism and recovery questions

- [Clock domains, deadlines and expiry](causal-order.md#clock-domains-deadlines-and-expiry) — source-scoped enrichment; examples and proposed tests are not executed results.

## Chapter source ledger

The following original citation rows, review limits and earlier topical routes are retained once for this chapter. Each question page points here and retains its inline citations. Evidence coverage must be judged at the actual claim and version, not inferred from source-list length.

<!-- tycho-question-source:tycho.page.d4822cc1e71c4f73896b7f6509f6daae:7 -->
## Exact public evidence

| ID | Source and bounded read scope | Supports and limitations |
|---|---|---|
| E01 | [Leslie Lamport, *Time, Clocks, and the Ordering of Events in a Distributed System*](https://www.microsoft.com/en-us/research/publication/time-clocks-ordering-events-distributed-system/), CACM 21(7), 1978, **official abstract and bibliographic record**, accessed 2026-10-18 | Establishes partial-order logical-time problem and total-order extension; **full PDF not inspected for this issue**, so detailed formal lemmas are explanations to be independently verified before formal-methods use |
| E02 | [Ongaro/Ousterhout, *In Search of an Understandable Consensus Algorithm*, extended version](https://ying-zhang.cn/dist/2014-raft.html), May 20 2014, **§2, §5.1–5.4**, cross-linked from [Raft's official publication portal](https://raft.github.io/) | Replicated state machines, leader/term election, majority log replication, commit and election restrictions; no Tycho production Raft implementation or proof of external read consistency |

**Review state:** original research draft, mechanical/readability checks only. No full Lamport PDF review, formal implementation verification, adversarial Raft simulation, consensus benchmark or independent domain reviewer has been claimed. Never treat an illustrative Mermaid diagram as a machine-checked proof.
<!-- /tycho-question-source -->
