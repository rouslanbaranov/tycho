---
metadata_version: 1
id: "tycho.page.4961bb03a6534242a0977db265b68d95"
kind: "page"
parent_id: "tycho.chapter.6eba0cf391184a709f2e23e5ecc1c3d2"
canonical_path: "book/volumes/v04/c02/leader-recovery.md"
title: "Leader changes, reconfiguration and restoration"
topic_ids:
  - "distributed-systems"
perspectives:
  - "architecture"
summary: "How should clients classify outcomes while leadership or membership changes?"
route_hints:
  questions:
    - "How should clients classify outcomes while leadership or membership changes?"
  prerequisites:
    - "tycho.page.b93c892861fb4dd4afcfbdc2ced1af80"
  related_ids:
    - "tycho.chapter.6eba0cf391184a709f2e23e5ecc1c3d2"
    - "tycho.page.1b2657011d454460856103419095031b"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "leader"
    - "recovery"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Bounded question from tycho.page.1b2657011d454460856103419095031b; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
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
# Leader changes, reconfiguration and restoration

**Owning question:** How should clients classify outcomes while leadership or membership changes?

This page belongs to [V04/C02 — Replication, consensus and leader changes](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.1b2657011d454460856103419095031b:4 -->
## 4. Leader elections, logs and client observations

Under a Raft-style model:
1. At a time, a node believes itself a leader for a given term, but other nodes can still be unaware because messages are delayed.
2. The quorum/term/log rules govern which log entries can be committed without violating safety.
3. A newly elected leader may reconcile followers with divergent **uncommitted** suffixes.
4. An acknowledged committed log entry has a protocol-specific durability/leader-completeness guarantee, contingent on correct stable storage and membership behavior.
5. Reads require a separately defined policy: local follower reads can be stale; linearizable reads require valid confirmation/lease/read-index semantics as implemented.
6. Client retries need stable effect identity because a network error alone cannot tell whether the previous attempt committed.

A leader process's health endpoint or elected status is not the same as the cluster having quorum and serving correct reads. [Tycho causality/consensus](../c01/causality-ordering-and-consensus.md) explains order/time relationships; [transaction/idempotency](../../../distributed/transactional-outbox-and-idempotency.md) explains state effects across service boundaries.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.1b2657011d454460856103419095031b:5 -->
## 5. Reconfiguration and restoration are different actions

Replacing an unhealthy voter changes cluster membership; restoring lost business state from backup changes persisted data. Those are not interchangeable. A safe reconfiguration accounts for current voters, reachable quorum, catch-up state, target network identity, eligible leader placement, and whether the reconfiguration itself can commit.

A backup restore may have to be performed as a **separately authorized disaster-recovery procedure** after irrevocable quorum loss. Restarting replicas from inconsistent snapshots without respecting implementation-specific cluster identity and membership can create divergence. Avoid prescribing manual member steps for an unspecified product.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.1b2657011d454460856103419095031b:6 -->
## 6. Failure and negative experiment matrix

| Fault | Question | Failure to reject |
|---|---|---|
| Current leader crashes | Can a connected quorum elect, resume and preserve committed state? | Old leader makes a conflicting commit |
| Network 3/2 split | Does minority refuse unsafe writes/linearizable reads? | Two sides both claim incompatible authority |
| Delayed follower | Can it catch up without treating uncommitted suffix as truth? | Duplicate/incorrect applied business effect |
| Membership addition while degraded | Does quorum remain recoverable if newcomer never starts? | Unsafe quorum requirement increase |
| Client acknowledgment lost | Does replay resolve one stable effect? | Duplicate committed business command |
| Stale follower read | Is staleness explicit or forbidden by contract? | Client treats an outdated value as linearizable |
| Permanent quorum loss | Is recovery documented and data-loss bound understood? | Claim automatic normal operation without quorum |

These are proposed test cases, not results. Safety proofs require precise protocol assumptions, implementation/version checks and independent review.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](quorum-envelope.md) |
| Next | [Continue the reasoning](README.md) |
| Integrated question | [Original scenario and limits](replication-consensus-and-leader-change.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.
