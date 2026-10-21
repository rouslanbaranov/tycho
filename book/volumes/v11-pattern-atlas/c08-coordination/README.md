---
metadata_version: 1
id: "tycho.chapter.bee261b76181706235dd8fa7ccde01a9"
kind: "chapter"
parent_id: "tycho.volume.fe327f72cf81df0237ce47b841e8aef5"
canonical_path: "book/volumes/v11-pattern-atlas/c08-coordination/README.md"
title: "V11/C08 — Distributed coordination"
topic_ids:
  - "distributed-systems"
  - "architecture-decisions"
perspectives:
  - "architecture"
  - "evaluation"
summary: "All 9 C08 cards with bounded owner links; decision coverage partial."
route_hints:
  questions:
    - "Which coordination mechanisms preserve safety and progress?"
  prerequisites:
    - "tycho.chapter.b20625a099bc4c82b7d547c32c7da28a"
  related_ids:
    - "tycho.volume.fe327f72cf81df0237ce47b841e8aef5"
    - "tycho.chapter.b20625a099bc4c82b7d547c32c7da28a"
    - "tycho.chapter.69085752a11c69305aa2a369b8ec9d29"
    - "tycho.chapter.3b9ec227ed58b92c0004eb0d39099142"
  excludes:
    - "Bounded owner links; no sufficient coverage or independent review."
  keywords:
    - "pattern atlas"
    - "distributed coordination"
    - "decision layer"
evidence_scope:
  source_ids:
    - "src.raft"
    - "src.kubernetes"
    - "src.kleppmann-distributed-locking"
    - "src.jepsen-consistency"
    - "src.temporal"
  claim_ids: []
  status: "source-linked"
  notes: "9 cards cite read units; owner links are bounded."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-21"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-21"
updated_at: "2026-10-21"
source_inspection_date: "2026-10-21"
content_verified_at: null
---
# V11/C08 — Distributed coordination

**Owning question:** Which coordination mechanisms preserve safety and progress?

## Purpose and mission

This chapter is the atlas entry point for **Distributed coordination**. It owns the
conditional decision route for 9 catalog entries, not the deep mechanism explanations.
Read the exact owner section before applying a mechanism claim.

All 9 entries have a self-checked card. Owner sections are bounded: a leader-recovery
or quorum page may own the safety contract without owning every coordination mechanism.

## Pages and reasoning route

Page count is content-dependent. This chapter currently uses one landing page for all
entries; a later split is an editorial change, not a plan failure. Start with the card,
check its conditions and contraindications, then read the exact owner section.

## Entry inventory

Each level-three heading is a stable atlas anchor. Owner links are bounded sections;
none claims sufficient technical or decision coverage.

### Leader Election

**Identity.** Leader Election; family Distributed coordination; kind coordination-pattern;
priority core.

**Decision question.** Should one node be chosen to coordinate work while others stand by?

**Good-fit conditions.** A single coordinator is useful; terms/epochs are available;
failover and stale leaders are handled; clients can observe leadership.

**Hard contraindications.** Reject when work is safely partitioned without a leader, when
election cannot be made safe, or when leader failover would block progress.

**Competing alternative.** Leaderless/quorum coordination or static assignment. Reverse
the choice when election latency and split-brain risk exceed coordination benefit.

**Failure and recovery.** Stale leaders and election churn are common; verify terms in the
owner section.

**Technical owner.** [Leader elections, logs and client observations](../../v04-distributed-coordination-and-events/c02-replication-consensus-and-leader-changes/leader-recovery.md#4-leader-elections-logs-and-client-observations) — leader election is bounded, not a complete Raft implementation.

**Sources.** [src.raft](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch4-raft.2026-10-21: sections "Leader Election", "Safety". The source
is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Consensus; Lease-Based Ownership; Fencing Tokens; Quorum
Coordination.

### Consensus

**Identity.** Consensus; family Distributed coordination; kind coordination-pattern;
priority advanced.

**Decision question.** Should replicas agree on an ordered log despite failures and
partitions?

**Good-fit conditions.** A quorum exists; safety and progress requirements are explicit;
membership changes are owned; clients tolerate retries.

**Hard contraindications.** Reject when a single writer suffices, when the network cannot
provide a stable quorum, or when availability must override consistency.

**Competing alternative.** Leader-follower replication with weaker guarantees. Reverse the
choice when consensus latency/availability cost exceeds agreement benefit.

**Failure and recovery.** Quorum loss and leader churn are common; verify safety/progress
in the owner section.

**Technical owner.** [Replication, consensus and leader change](../../v04-distributed-coordination-and-events/c02-replication-consensus-and-leader-changes/replication-consensus-and-leader-change.md#engineering-walkthrough-new-leader-old-client-and-a-lost-acknowledgment) — consensus is bounded to safety/progress discussion.

**Sources.** [src.raft](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch4-raft.2026-10-21: sections "Raft Consensus Algorithm", "Safety".
The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Leader Election; Quorum Coordination; Leader-Follower Replication;
2PC.

### Distributed Lock

**Identity.** Distributed Lock; family Distributed coordination; kind
coordination-pattern; priority core.

**Decision question.** Should a shared lock prevent concurrent access to one resource
across processes?

**Good-fit conditions.** The lock protects a correctness-critical section; the service
can maintain quorum; expiry and ownership are explicit; the resource checks a fencing
epoch, or the operation is safe under uncertain ownership.

**Hard contraindications.** Reject when work is naturally partitioned, when lock loss
would corrupt state, when the lock service cannot maintain quorum, or when the resource
cannot reject a stale holder.

**Competing alternative.** Lease-based ownership with fencing or single-writer
partitioning. Reverse the choice when lock safety cannot be proven.

**Failure and recovery.** Pauses, delayed writes, quorum loss and release races are
common. Treat ownership as uncertain after a missed renewal; fence stale epochs at the
resource or keep the outcome explicitly unsafe.

**Technical owner.** [Leases, stale owners and fencing at the destination](../../v04-distributed-coordination-and-events/c02-replication-consensus-and-leader-changes/leader-recovery.md#leases-stale-owners-and-fencing-at-the-destination) — locks/leases/fencing are bounded, not a lock-service API guide.

**Sources.** [src.kubernetes](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch4-k8s-leases.2026-10-21: sections "Leases", "Lease objects", "Leader
election". The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Lease-Based Ownership; Fencing Tokens; Leader Election; Consensus.

### Lease-Based Ownership

**Identity.** Lease-Based Ownership; family Distributed coordination; kind
coordination-pattern; priority core.

**Decision question.** Should ownership expire after a bounded lease rather than remain
until explicit release?

**Good-fit conditions.** A lease duration is known; renewal is observable; expired owners
stop acting; destination fencing exists.

**Hard contraindications.** Reject when the owner cannot renew, when clock skew is
unbounded, or when expiry could allow two active owners without fencing.

**Competing alternative.** Static ownership or quorum-backed ownership. Reverse the choice
when lease renewal cost exceeds availability benefit.

**Failure and recovery.** Expired owners continuing to act is common; verify fencing in
the owner section.

**Technical owner.** [Leases, stale owners and fencing at the destination](../../v04-distributed-coordination-and-events/c02-replication-consensus-and-leader-changes/leader-recovery.md#leases-stale-owners-and-fencing-at-the-destination) — lease ownership is bounded, not a scheduler implementation.

**Sources.** [src.kubernetes](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch4-k8s-leases.2026-10-21: sections "Leases", "Lease objects". The
source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Distributed Lock; Fencing Tokens; Leader Election; Health Endpoint
Monitoring.

### Fencing Tokens

**Identity.** Fencing Tokens; family Distributed coordination; kind coordination-pattern;
priority advanced.

**Decision question.** Should every write carry an epoch/token so the destination rejects
a stale owner?

**Good-fit conditions.** The destination can compare tokens; tokens increase
monotonically; stale owners may still run but cannot commit.

**Hard contraindications.** Reject when the resource cannot enforce tokens, when tokens
can be reused, or when the lock is only an efficiency optimization.

**Competing alternative.** Lease-only ownership or single-writer routing. Reverse the
choice when destination changes are cheaper than stale-write risk.

**Failure and recovery.** Token bypass and epoch reuse are common; verify destination
enforcement in the owner section.

**Technical owner.** [Leases, stale owners and fencing at the destination](../../v04-distributed-coordination-and-events/c02-replication-consensus-and-leader-changes/leader-recovery.md#leases-stale-owners-and-fencing-at-the-destination) — destination fencing is bounded, not a universal token protocol.

**Sources.**
[src.kleppmann-distributed-locking](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch4-fencing.2026-10-21: sections "Making the lock safe with fencing",
"The synchrony assumptions of Redlock". The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Distributed Lock; Lease-Based Ownership; Leader Election; Idempotent
Receiver.

### Quorum Coordination

**Identity.** Quorum Coordination; family Distributed coordination; kind
coordination-pattern; priority advanced.

**Decision question.** Should decisions require a majority of replicas rather than one
node?

**Good-fit conditions.** Replica set and failure domains are known; majority arithmetic is
explicit; latency of quorum calls is acceptable.

**Hard contraindications.** Reject when a single authority suffices, when the network
cannot maintain a majority, or when quorum latency violates the budget.

**Competing alternative.** Leader-based coordination or static assignment. Reverse the
choice when quorum availability/latency exceeds safety benefit.

**Failure and recovery.** Quorum loss and slow replicas are common; verify envelope in the
owner section.

**Technical owner.** [Majority quorum arithmetic and the failure envelope](../../v04-distributed-coordination-and-events/c02-replication-consensus-and-leader-changes/quorum-envelope.md#2-majority-quorum-arithmetic-and-the-failure-envelope) — quorum arithmetic is bounded, not a consensus protocol.

**Sources.** [src.raft](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch4-raft.2026-10-21: sections "Raft Consensus Algorithm", "Safety".
The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Consensus; Leader Election; Quorum-Based Reads/Writes; 2PC.

### Causal Ordering

**Identity.** Causal Ordering; family Distributed coordination; kind coordination-pattern;
priority advanced.

**Decision question.** Should operations that are causally related preserve their order
without requiring a total order?

**Good-fit conditions.** Happens-before relationships are meaningful; causal metadata such
as vector clocks can be carried; concurrent operations may diverge but must converge once
the same updates are visible.

**Hard contraindications.** Reject when a total order is required, when causal metadata
cannot be kept with the operation, when clients switch servers without a session
guarantee, or when concurrent writes have no merge rule.

**Competing alternative.** Total ordering via consensus or per-key ordering. Reverse the
choice when causal metadata cost exceeds ordering benefit.

**Failure and recovery.** Partition, reordered delivery, lost metadata and server switching
can expose missing dependencies. Keep durable causal metadata, replay/deduplicate, and
define a merge; if total order is mandatory, use consensus and accept its cost.

**Technical owner.** [The happens-before relation describes causal knowledge](../../v04-distributed-coordination-and-events/c01-time-causality-and-ordering/causal-order.md#1-the-happens-before-relation-describes-causal-knowledge) — causal ordering is bounded, not a universal clock service.

**Sources.** [src.jepsen-consistency](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch4-causal.2026-10-21: sections "Causal Consistency", "Example",
"Convergent causal systems", "Sticky availability", "Formally". The source is a public
pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Session Consistency; Consensus; Read Replicas; Event Sourcing.

### Session Consistency

**Identity.** Session Consistency; family Distributed coordination; kind
coordination-pattern; priority advanced.

**Decision question.** Should one client session preserve selected read/write observations
across replicas?

**Good-fit conditions.** A session token can route/stick; monotonic reads or
read-your-writes are required; failover preserves the token.

**Hard contraindications.** Reject when global linearizability is required, when sessions
cannot be maintained, or when failover loses session state.

**Competing alternative.** Strong consistency or eventual consistency without session
guarantees. Reverse the choice when session routing/failover cost exceeds client
experience benefit.

**Failure and recovery.** Token loss and replica routing are common; verify observations
in the owner section.

**Technical owner.** [Session-visible consistency](../../v04-distributed-coordination-and-events/c02-replication-consensus-and-leader-changes/session-consistency.md#an-explicit-session-token) — session consistency is bounded, not a complete client-session protocol.

**Sources.** [src.jepsen-consistency](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch4-jepsen.2026-10-21: sections "Consistency Models", "Session
guarantees". The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Causal Ordering; Read Replicas; Leader-Follower Replication; Session
Token.

### Distributed Workflow Orchestration

**Identity.** Distributed Workflow Orchestration; family Distributed coordination; kind
coordination-pattern; priority core.

**Decision question.** Should a durable orchestration engine own multi-step progress,
timers and recovery?

**Good-fit conditions.** Steps span services or long timers; progress must survive crashes;
activities can be idempotent; retries, cancellation and compensation are business
decisions; the team can operate a durable engine and version its histories.

**Hard contraindications.** Reject when one local transaction suffices, when workflow state
has no owner, when replay/versioning cannot be governed, or when orchestration becomes a
hidden monolith.

**Competing alternative.** Saga choreography or a simple queue pipeline. Reverse the
choice when central workflow state and engine operations exceed coordination benefit.

**Failure and recovery.** Stuck workflows, duplicate activities, lost timers,
nondeterministic replay and version conflicts are common. Replay from durable history,
keep activities idempotent and use a repair state for unknown external effects.

**Technical owner.** [Outbox, inbox, sagas and durable workflow coordination](../../v04-distributed-coordination-and-events/c05-outbox-inbox-sagas-and-durable-workflows/outbox-inbox-sagas-and-durable-workflows.md#purpose-and-decision-question) — durable workflow coordination is bounded, not a Temporal product guide.

**Sources.** [src.temporal](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-temporal-workflows.2026-10-21: sections "Workflows", "Workflow
Execution", "Determinism". The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Saga Orchestration; Process Manager; Transactional Outbox;
Lease-Based Ownership.

## Chapter result and counterexample

Nine cards establish a conditional decision route. Owner sections are bounded; none
establishes technical sufficiency.

Counterexample: a lease without destination fencing is not evidence for the fencing
card's safety conditions.

## Navigation and prerequisites

- Parent: [V11](../README.md).
- Previous: [V11/C07](../c07-resilience/README.md).
- Next: [V11/C09](../c09-scalability/README.md).
- Prerequisite: V10/C03 — pattern applicability and contraindications.
- Registry: [pattern registry](../../../../edition/patterns/registry.v1.json).
- Card batch: [card batches](../../../../edition/patterns/card-batches.v1.json).
- Coverage map: [candidate coverage](../../../../edition/patterns/coverage-map.v1.json).

## Evidence and known limits

- All 9 cards cite read ledger units; owner links and backlinks are self-checked.
- Owner links are bounded sections, not dedicated pattern pages.
- No entry claims sufficient technical or decision coverage.
- No independent editorial review, benchmark, production observation or runtime test
  is asserted.
