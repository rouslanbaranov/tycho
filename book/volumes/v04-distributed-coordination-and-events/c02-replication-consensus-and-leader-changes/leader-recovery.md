---
metadata_version: 1
id: "tycho.page.4961bb03a6534242a0977db265b68d95"
kind: "page"
parent_id: "tycho.chapter.6eba0cf391184a709f2e23e5ecc1c3d2"
canonical_path: "book/volumes/v04-distributed-coordination-and-events/c02-replication-consensus-and-leader-changes/leader-recovery.md"
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

A leader process's health endpoint or elected status is not the same as the cluster having quorum and serving correct reads.

**Failure and recovery.** Elections can fail to reach quorum, split votes, or elect a
leader whose log is behind. Randomized timeouts and pre-vote reduce disruption; log
reconciliation, stable storage and membership rules preserve committed entries. A leader
that cannot confirm quorum must stop serving authoritative writes and linearizable reads.
Client retries still need stable effect identity because an election does not resolve an
unknown outcome. [Raft](https://raft.github.io/) documents the election and log rules.

**Alternative.** Leaderless quorum coordination, static primary assignment or single-writer
partitioning may be simpler when elections add latency without a real failover
requirement. Reverse the choice when election latency and split-brain risk exceed the
coordination benefit. [Tycho causality/consensus](../c01-time-causality-and-ordering/causality-ordering-and-consensus.md) explains order/time relationships; [transaction/idempotency](../../../distributed/transactional-outbox-and-idempotency.md) explains state effects across service boundaries.

<!-- /tycho-question-source -->

> **Pattern atlas:**
> [Leader Election](../../v11-pattern-atlas/c08-coordination/README.md#leader-election) — decision conditions and contraindications.
> [Distributed Lock](../../v11-pattern-atlas/c08-coordination/README.md#distributed-lock) — decision conditions and contraindications.
> [Lease-Based Ownership](../../v11-pattern-atlas/c08-coordination/README.md#lease-based-ownership) — decision conditions and contraindications.
> [Fencing Tokens](../../v11-pattern-atlas/c08-coordination/README.md#fencing-tokens) — decision conditions and contraindications.

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

## Leases, stale owners and fencing at the destination

**Enrichment contract:** distinguish who currently owns a lease from which external writes the destination will accept. This section owns application coordination; [region failback](../../v08-delivery-deployment-and-recovery/c07-multi-region-recovery-and-data-reconciliation/authority-failback.md) applies the idea at recovery scope.

A lock service can give worker B ownership after worker A stops renewing. It cannot make A's paused process disappear. AWS's leader-election discussion identifies timing and process pauses as practical lease hazards. etcd 3.6 documents KV ordering, leases and delayed watches; a watch notification is not a timely external write fence.

**Lock semantics.** A lease-based lock is a time-bounded grant from a lock service.
[Kubernetes leases](https://kubernetes.io/docs/concepts/architecture/leases/) record
ownership and renewal/expiry times, not a guarantee that the holder has stopped. Mutual
exclusion depends on the service's own consistency and on bounded process pauses, not on
the holder's local belief.

**Failure classes.** A holder can pause past expiry; a delayed write can arrive after a
new holder is established; the lock service can lose quorum; release can race with
expiry. The destination must reject stale epochs or the operation remains explicitly
unsafe. A lock service that cannot establish a quorum cannot safely grant a new lease.

**Alternative.** For one database, a conditional update or unique constraint can provide
the same exclusion without a separate lock service. For cross-process coordination,
single-writer partitioning or a consensus-backed lease may be safer than an independent
lock service. Choose a lock only when its failure and clock assumptions are acceptable.

### Original stale-owner trace

Assume a fictional thumbnail job updates an authoritative manifest. The destination stores an accepted epoch alongside the manifest.

1. A receives epoch 41, reads the current manifest, and pauses.
2. A's lease expires. B receives epoch 42.
3. B establishes epoch 42 at the destination using its authorized takeover protocol.
4. A resumes and submits a write carrying 41.
5. The destination atomically rejects 41 because its active epoch is 42.
6. B writes with 42 under the destination's compare-and-update rule.

~~~mermaid
sequenceDiagram
    participant A as Old worker
    participant L as Lease authority
    participant B as New worker
    participant D as Destination
    L-->>A: Grant epoch 41
    Note over A: Process pauses
    L-->>B: Grant epoch 42 after expiry
    B->>D: Establish active epoch 42
    A->>D: Delayed write with epoch 41
    D-->>A: Reject stale authority
    B->>D: Write with epoch 42
    D-->>B: Accept under atomic guard
~~~

Text alternative: the destination rejects the resumed former owner's writes after takeover is established there. The synthetic example does not assert that a distributed lock alone enforces this protocol.

**Important limit:** monotonically increasing tokens protect only where the destination checks and persists them atomically. If B has not yet established its newer epoch there, comparing only against the last observed token does not prove A still owns the lease. Define the takeover linearization point, handling of in-flight writes and whether lease ownership or destination epoch is the actual authority. Unrelated side effects need their own guard.

For a single database, a transactional conditional update or unique constraint may satisfy the invariant without a separate lock service. For an external API that cannot fence stale callers, serialize through an authoritative effect owner, use stable idempotent operation identities where supported, or retain an explicit unresolved-safety boundary.

**Alternatives to a lease.** Static ownership or quorum-backed ownership avoids lease
renewal but risks stale owners on failure. A transactional conditional update at the
destination can replace a separate lease when the resource is one database. Reverse the
lease choice when renewal cost exceeds the availability benefit, or when the destination
cannot fence a stale holder.

### Failure and recovery decisions

| Event | Required response |
|---|---|
| Renewal timeout | Treat ownership as uncertain; do not infer a successful renewal |
| Local process pause | Revalidate authority before new work, while retaining destination enforcement |
| Old delayed request | Check epoch atomically with the protected effect |
| Lease-store restoration | Prevent token reuse across restored histories; generation/epoch continuity needs its own recovery contract |
| Duplicate write in the same epoch | Use effect identity or a conditional state version; fencing alone does not deduplicate |
| Coordination quorum unavailable | Prefer stopping protected mutations to inventing a second authority |

Use local elapsed time for local budgets under the runtime's actual clock contract. Do not compare arbitrary wall clocks to establish distributed ownership; see [time and deadlines](../c01-time-causality-and-ordering/causal-order.md#clock-domains-deadlines-and-expiry).

### Exact evidence and completion boundary

Selected passages inspected 2026-10-20: [Leader election in distributed systems](https://aws.amazon.com/builders-library/leader-election-in-distributed-systems/) (lease duration and pauses); [etcd API guarantees](https://etcd.io/docs/v3.6/learning/api_guarantees/) (KV versus watch/lease guarantees). The epoch protocol, trace and guard requirements are original synthetic reasoning. No lock client or destination implementation was executed. Proposed acceptance is to pause A across expiry, let B take over, resume A, and require stale effects to be rejected at the actual resource.

## Bounded pattern ownership notes

### Distributed Lock

A lease-based lock is a time-bounded grant from a lock service. The holder may believe it still
owns the lease after a pause, so the grant alone is not proof of exclusive access.

Mutual exclusion depends on the service's own consistency and on bounded process pauses, not on
the holder's local belief. Define what the lock protects, the acquisition and release path, and
the maximum pause the design tolerates. The destination must reject stale epochs or the operation
remains explicitly unsafe.

For one database, a conditional update or unique constraint can provide the same exclusion without
a separate lock service. A lock is justified when multiple resources need one coordination grant
and the destination can enforce the epoch; otherwise the database constraint is simpler and
stronger.

### Lease-Based Ownership

A lock service can give worker B ownership after worker A stops renewing. That reassignment is a
new ownership epoch, not a repair of A's local state.

Define the takeover linearization point, handling of in-flight writes and whether lease ownership
or destination epoch is the actual authority. On renewal timeout, treat ownership as uncertain; do
not infer a successful renewal. A stop-write deadline follows. The old holder must stop writing before its lease could expire,
and the destination must reject its delayed effects.

Static ownership or quorum-backed ownership avoids lease renewal but risks stale owners on failure.
Choose leases when fast takeover matters and the destination can fence; choose quorum ownership
when the coordination service itself must survive a partition.

### Fencing Tokens

A fencing token is a monotonically increasing value issued with ownership. It protects only where
the destination checks and persists the token atomically; a token carried in a request header but
never compared is decoration.

If B has not yet established its newer epoch at the destination, comparing only against the last
observed token does not prove A still owns the lease. The destination atomically rejects a delayed
write whose token is below its active epoch, so a paused former owner cannot commit.

For an external API that cannot fence stale callers, serialize through an authoritative effect
owner, use stable idempotent operation identities where supported, or retain an explicit
unresolved-safety boundary. Do not claim mutual exclusion from a token the destination ignores.

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](quorum-envelope.md) |
| Next | [Continue the reasoning](README.md) |
| Integrated question | [Original scenario and limits](replication-consensus-and-leader-change.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.
