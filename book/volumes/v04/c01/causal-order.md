---
metadata_version: 1
id: "tycho.page.a0d3dfe1c8a245e98d9c9ae4813b8c85"
kind: "page"
parent_id: "tycho.chapter.510c0c78de2b450c8be93d708222a488"
canonical_path: "book/volumes/v04/c01/causal-order.md"
title: "Causal knowledge and ordering scope"
topic_ids:
  - "distributed-systems"
perspectives:
  - "architecture"
summary: "What can happens-before, timestamps and per-key order each establish?"
route_hints:
  questions:
    - "What can happens-before, timestamps and per-key order each establish?"
  prerequisites:
    - "tycho.page.d4822cc1e71c4f73896b7f6509f6daae"
  related_ids:
    - "tycho.chapter.510c0c78de2b450c8be93d708222a488"
    - "tycho.page.d4822cc1e71c4f73896b7f6509f6daae"
    - "tycho.page.d664f65295644726ae1234a982f81fa8"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "causal"
    - "order"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Bounded question from tycho.page.d4822cc1e71c4f73896b7f6509f6daae; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-20"
  reviewer: "Codex editorial decomposition"
  proof_uri: null
authored_at: "2026-10-20"
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---
# Causal knowledge and ordering scope

**Owning question:** What can happens-before, timestamps and per-key order each establish?

This page belongs to [V04/C01 — Time, causality and ordering](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.d4822cc1e71c4f73896b7f6509f6daae:1 -->
## 1. The happens-before relation describes causal knowledge

Leslie Lamport's 1978 paper *Time, Clocks, and the Ordering of Events in a Distributed System* introduces an ordering relation on events that can represent a partial order; its published abstract specifically contrasts this causal relation with the total-order extensions possible through logical-clock schemes. The paper is listed in Lamport's publication bibliography and Microsoft Research's original-paper record. This page uses that *abstract and bibliographic scope*, rather than claiming a line-by-line review of its PDF. [E01]

For two events `a` and `b`, the commonly used happens-before definition has three generating rules:

- Events on a single sequential process are ordered by their process execution.
- Sending a specific message causally precedes its receiving event.
- The relation is transitive: if `a` precedes `b` and `b` precedes `c`, then `a` precedes `c`.

Events for which neither direction follows may be **concurrent** even if each machine records a clock time. Concurrency here denotes insufficient causal ordering, not necessarily simultaneous physical execution.

```mermaid
sequenceDiagram
    participant P as Process P
    participant Q as Process Q
    participant R as Process R
    P->>P: a — update local state
    P->>Q: m1 — send update
    Q->>Q: b — receive m1
    R->>R: c — independent local event
    Note over P,Q: a happens before b
    Note over Q,R: b and c have no shown causal path
```

Text alternative: process P acts and sends a message to Q, so its event precedes Q's reception. R acts independently; the diagram contains no evidence that Q's event precedes or follows R's.

An integer **Lamport logical clock** can be incremented for a local event, attached to messages, and advanced on reception so that causal predecessors have smaller timestamps. However, the converse does **not** follow: two events with ordered clock numbers may still be causally unrelated. Adding a deterministic process-ID tie-breaker produces one reproducible total ordering; it does not create a real causal dependency. A vector-clock mechanism can represent additional causal distinctions at the cost of metadata associated with participating processes; a full algorithm comparison is outside this page's bounded evidence.

**Decision impact:** if the business only needs every item to preserve its own update order, requiring global total order can introduce unnecessary coordination. If conflicting updates of a shared invariant must be serialized, merely generating timestamps does not create atomic or correct resolution.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.d4822cc1e71c4f73896b7f6509f6daae:3 -->
## 3. Ordering scopes: per-key versus global

In a **fictional** registration service, events for workshop A could need a consistent order independent of workshop B. If both operate under separate authoritative owners, a single global sequence may add coordination without improving correctness. But if one operation atomically transfers a limited shared resource between A and B, the owners must specify a coordination protocol for that invariant.

```mermaid
flowchart LR
    A1["Workshop A: event 1"] --> A2["Workshop A: event 2"]
    B1["Workshop B: event 1"] --> B2["Workshop B: event 2"]
    A2 -. "No implied order" .- B1
    Shared["Cross-workshop invariant"] --> Coordination["Explicit coordination / transaction"]
```

Text alternative: A's changes are ordered within A, and B's changes within B. The drawing does not establish an order between unrelated streams. A cross-stream invariant may still require a separate coordination mechanism.

Ordering must be defined by **where it is enforced**: a transaction log's commit order, a message partition's append order, one actor's sequential mailbox, or an API's linearizable key-value access are different contracts. The next integration research issue (#81) owns broker-specific partition ordering and consumer replay.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](causality-ordering-and-consensus.md) |
| Next | [Continue the reasoning](agreement-failure.md) |
| Integrated question | [Original scenario and limits](causality-ordering-and-consensus.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.
