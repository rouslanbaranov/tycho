---
metadata_version: 1
id: "tycho.page.1b2657011d454460856103419095031b"
kind: "page"
parent_id: "tycho.chapter.6eba0cf391184a709f2e23e5ecc1c3d2"
canonical_path: "book/volumes/v04-distributed-coordination-and-events/c02-replication-consensus-and-leader-changes/replication-consensus-and-leader-change.md"
title: "Replication, consensus and leader change: safety and progress under failures"
topic_ids:
  - "distributed-systems"
perspectives:
  - "architecture"
summary: "Integrated question, original scenario and transfer limits for Replication, consensus and leader changes. Detailed mechanisms have separate question owners."
route_hints:
  questions:
    - "Which failure assumptions sustain agreement or availability?"
  prerequisites: []
  related_ids:
    - "tycho.page.d4822cc1e71c4f73896b7f6509f6daae"
    - "tycho.page.ace968ab1de8409383c6a9b22a00d006"
    - "tycho.landing.1a9054fd18f64dfe911f34a4d17458c0"
    - "tycho.landing.ddbfbbbe1a85406faa2705102378beea"
    - "tycho.page.3c78e2b17ac74973b2ae658977843c2a"
    - "tycho.page.2536d18422944e27abe4ea8549beb9ab"
    - "tycho.page.b93c892861fb4dd4afcfbdc2ced1af80"
    - "tycho.page.4961bb03a6534242a0977db265b68d95"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Replication"
    - "consensus"
    - "and"
    - "leader"
    - "change"
    - "safety"
    - "progress"
    - "under"
    - "failures"
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
authored_at: "2026-10-19"
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---
<!-- tycho-question-source:tycho.page.1b2657011d454460856103419095031b:-1 -->

# Replication, consensus and leader change: safety and progress under failures

> **Tycho independent V04/C02 manuscript draft (2026-10-19).** Source scope: the public Raft project/paper entry and etcd 3.6 quorum/membership documentation, plus original synthetic figures. No distributed cluster, fault injection, model checker or independently reviewed proof was executed.

<!-- /tycho-question-source -->

> **Pattern atlas:**
> [Consensus](../../v11-pattern-atlas/c08-coordination/README.md#consensus) — decision conditions and contraindications.


> **Pattern atlas:**
> [Leader-Follower Replication](../../v11-pattern-atlas/c06-database-storage/README.md#leader-follower-replication) — decision conditions and contraindications.
> [Multi-Leader Replication](../../v11-pattern-atlas/c06-database-storage/README.md#multi-leader-replication) — decision conditions and contraindications.
> [Read Replicas](../../v11-pattern-atlas/c06-database-storage/README.md#read-replicas) — decision conditions and contraindications.

<!-- tycho-question-source:tycho.page.1b2657011d454460856103419095031b:0 -->
## Purpose and mission

Replication makes copies of state available, but copies can disagree after a crash, network delay or concurrent writes. Consensus protocols coordinate a sequence of state-machine decisions under stated fault assumptions. The key distinction is between **safety**—forbidden outcomes never occur—and **liveness/availability**—the cluster eventually makes progress under supported conditions.

Having several replicas does not mean a system can accept any write while partitioned, restore all committed effects after every failure, or survive loss of a majority without explicit recovery.

The [Raft project and extended paper](https://raft.github.io/) describe a leader-based replicated-log algorithm; [etcd 3.6 FAQ](https://etcd.io/docs/v3.6/faq/) documents its quorum and membership change considerations. These are examples of *consensus under defined fault models*, not universal guarantees for all replicated services.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.1b2657011d454460856103419095031b:7 -->
## Engineering walkthrough — New leader, old client and a lost acknowledgment

**Original three-node quorum illustration:** nodes A, B and C replicate one state machine. A was leader. A's network connection to B and C fails; B and C may form a quorum and eventually select a new leader. A can remain reachable to some clients, but must not be allowed to commit new authoritative writes without a valid quorum/term contract. A client whose response was lost before the partition cannot decide whether its operation committed.

| Failure point | Safety claim requiring proof | Liveness limitation |
|---|---|---|
| A isolated from B,C | Quorum/term enforcement prevents conflicting committed log entries | Some clients of A cannot complete writes |
| B/C elect successor | New leader reconciles log according to protocol | Election delay may exceed request deadline |
| Old A reappears with stale state | Reject stale leader commands, catch up log | Cannot blindly serve fresh reads before state catches up |
| Membership changes | Respect the protocol's configuration transition safety | Removing too many voters can lose progress |

An acknowledged write's durability depends on the actual replication/commit acknowledgment boundary; a client timeout is ambiguous and requires stable operation identity on retry. Read consistency depends on the concrete algorithm and read path, not simply on "three replicas". Raft's public paper and the etcd versioned FAQ support protocol discussion, but do not certify an invented deployment's failover timings.

**Proposed, not run:** partition old leader, issue reads/writes on both sides, restore connectivity and change membership while checking committed-history invariants, stale-term rejection, duplicate effects and correct client error classification. For read-mostly telemetry where temporary staleness is acceptable, simpler asynchronous replicas may avoid quorum overhead; if single-key linearizable authority is mandatory, that alternative may fail the requirement.

<!-- /tycho-question-source -->

## Integrated decision and reading route

State fault assumptions, quorum rules, leader terms and client-visible outcomes when explaining replicated authority.

An isolated former leader must not continue accepting authoritative effects merely because its process is healthy.

The detailed pages separate the mechanisms that make this decision conditional:

- [Replica properties and quorum failure envelopes](quorum-envelope.md) — Which partitions can make progress without allowing divergent authority?
- [Leader changes, reconfiguration and restoration](leader-recovery.md) — How should clients classify outcomes while leadership or membership changes?

[Chapter introduction, ordered pages and full source ledger](README.md). Original source labels retain their historical scope; this editorial decomposition does not turn proposed experiments into executed evidence.

## Bounded pattern ownership notes

These notes define the decision boundary for atlas cards whose mechanism is not the main subject of
this page. They are synthetic design guidance, not measured evidence, and they do not create a new
source claim.

### Multi-Leader Replication

Several nodes accept writes for the same logical data and replicate them to each other, so every
accepted write must eventually converge to one declared outcome. The system must define a
conflict-resolution rule and preserve every acknowledged effect according to that rule; silent
last-writer-wins is not a convergence proof.

Concurrent writes to one key produce conflicts that surface later during reads or reconciliation;
record the conflicting versions and expose a deterministic resolution path. Single-leader
replication avoids write conflicts at the cost of write availability across regions; choose
multi-leader only when accepting local writes outweighs the conflict contract.

### Read Replicas

Read replicas serve read-only traffic from followers, reducing load on the leader while accepting
that a replica can lag behind the latest committed write. A read must state the freshness it
requires, and read-your-writes or monotonic guarantees must be enforced by routing, a position wait
or an authority read.

A lag spike serves stale data even though replication is healthy; monitor applied position and lag,
and route freshness-critical reads away from a lagging replica. Read from the leader or use a quorum
read when freshness dominates; add replicas when read volume and tolerance for bounded staleness
justify the extra copies.
