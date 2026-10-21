---
metadata_version: 1
id: "tycho.page.d4822cc1e71c4f73896b7f6509f6daae"
kind: "page"
parent_id: "tycho.chapter.510c0c78de2b450c8be93d708222a488"
canonical_path: "book/volumes/v04-distributed-coordination-and-events/c01-time-causality-and-ordering/causality-ordering-and-consensus.md"
title: "Causality, ordering and consensus in distributed systems"
topic_ids:
  - "distributed-systems"
perspectives:
  - "architecture"
summary: "Integrated question, original scenario and transfer limits for Time, causality and ordering. Detailed mechanisms have separate question owners."
route_hints:
  questions:
    - "Which ordering can a distributed system observe or guarantee?"
  prerequisites: []
  related_ids:
    - "tycho.page.a0d3dfe1c8a245e98d9c9ae4813b8c85"
    - "tycho.page.d664f65295644726ae1234a982f81fa8"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Causality"
    - "ordering"
    - "and"
    - "consensus"
    - "distributed"
    - "systems"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Only exact URL matches to the global source register are normalized here. Page-local case and evidence ledger IDs remain in the body; no claim-level mapping or source inspection is inferred."
content_review:
  status: "draft"
  reviewed_at: null
  reviewer: null
  proof_uri: null
authored_at: "2026-10-18"
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---
<!-- tycho-question-source:tycho.page.d4822cc1e71c4f73896b7f6509f6daae:-1 -->

# Causality, ordering and consensus in distributed systems

> Tycho research page for [Issue #80](https://github.com/rouslanbaranov/tycho/issues/80), proposed V04/C01–C02. Source inspection: 2026-10-18. Original explanatory prose and **synthetic** diagrams; not a formal proof, operational consensus deployment or independently reviewed implementation.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.d4822cc1e71c4f73896b7f6509f6daae:0 -->
## Purpose and mission

Several machines cannot generally infer a single complete history merely by comparing their wall clocks. Before choosing event ordering, a replicated state machine, a database read policy or a failure-recovery approach, specify **which observations must be ordered** and what must happen when communication fails.

**Primary question:** What do causal ordering, total log ordering and consensus actually establish, and which guarantees do they *not* provide for an application's end-to-end state?

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.d4822cc1e71c4f73896b7f6509f6daae:6 -->
## Engineering walkthrough — Wall-clock order cannot prove causality or commit order

**Original synthetic distributed trace:** service A records command X at local clock `10:00:00.200`, sends event E, and service B receives E after applying a 400 ms backward clock adjustment. B writes `09:59:59.950` in a log. B's timestamp is earlier than A's, but E's send causally precedes its receipt. Sorting timestamps would invert that relationship.

Lamport's happened-before relation distinguishes program order and message edges. A Lamport-style logical counter can preserve those causal constraints but does **not** prove that two concurrent events are causally related merely because their counters differ. A total-order service or consensus can choose one sequence for a declared authority, but that adds coordination, availability and latency implications; it is not equivalent to clock synchronization.

| Question | Appropriate scope | Counterexample |
|---|---|---|
| What did B learn from A? | Message/causal relation | Clock offset reverses logged timestamps |
| Which write is legally first for one booking key? | Single authoritative serializing writer/consensus contract | Per-partition queue order across different keys is global order |
| Can a client observe a completed write on subsequent reads? | Linearizability/consistency contract | Lamport counter on logs proves read-after-write visibility |

**Proposed, unexecuted test:** reorder cross-service messages and skew clocks, then verify which statements remain true without any synchronized wall clocks. If the product requires a global order of conflicting writes, state an explicit ordering authority; if it needs only trace correlation, causal links and operation IDs may suffice without consensus. The original Lamport paper defines the causal abstraction, not any claim of a running global clock or order service.

<!-- /tycho-question-source -->

## Integrated decision and reading route

Distinguish causal precedence, concurrent events and a chosen total order before relying on timestamps.

Clock order cannot prove that one event observed another, and an ordered log alone does not establish a business invariant.

The detailed pages separate the mechanisms that make this decision conditional:

- [Causal knowledge and ordering scope](causal-order.md) — What can happens-before, timestamps and per-key order each establish?
- [Agreement, availability and uncertain observations](agreement-failure.md) — Which fault assumption separates an ordering claim from an agreement guarantee?

[Chapter introduction, ordered pages and full source ledger](README.md). Original source labels retain their historical scope; this editorial decomposition does not turn proposed experiments into executed evidence.
