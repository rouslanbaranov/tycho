---
metadata_version: 1
id: "tycho.page.ba4ee752a40342cfb6d6be5ac81c4bd3"
kind: "page"
parent_id: "tycho.chapter.22fa23c6c7a6b0c29a52137bc67a00c9"
canonical_path: "book/volumes/v11-pattern-atlas/c06-database-storage/consistent-hashing.md"
title: "Consistent Hashing"
topic_ids:
  - "data-architecture"
  - "distributed-systems"
perspectives:
  - "architecture"
  - "evaluation"
summary: >-
  Decision card for Consistent Hashing; all four dimensions source-bound;
  coverage remains partial-bounded, no promotion.
route_hints:
  questions:
    - >-
      Should keys and nodes share a hash ring so membership changes move only a
      fraction of data?
  prerequisites:
    - "tycho.chapter.22fa23c6c7a6b0c29a52137bc67a00c9"
  related_ids:
    - "tycho.chapter.22fa23c6c7a6b0c29a52137bc67a00c9"
  excludes:
    - >-
      No sufficient coverage, promotion or owner acceptance is claimed for this
      moved page.
  keywords:
    - "pattern atlas"
    - "consistent hashing"
    - "database and storage architecture"
evidence_scope:
  source_ids:
    - "src.karger"
    - "src.dynamo"
    - "src.cassandra"
    - "src.riak"
  claim_ids: []
  status: "source-linked"
  notes: >-
    Card cites read.karger-consistent-hashing.2026-10-31,
    read.dynamo-consistent-hashing.2026-10-31,
    read.cassandra-dynamo-consistent-hashing.2026-10-31,
    read.riak-vnodes.2026-10-31, read.riak-clusters.2026-10-31 and
    read.riak-adding-removing-nodes.2026-10-31; the existing Cassandra overview
    record remains a scope limit, not support.
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-31"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-31"
updated_at: "2026-10-31"
source_inspection_date: "2026-10-31"
content_verified_at: null
---
# Consistent Hashing

**Identity.** Consistent Hashing; family Database and storage architecture; kind
data-distribution-pattern; priority core.

**Decision question.** Should keys and nodes share a hash ring so membership changes move
only a fraction of data?

**Good-fit conditions.** Membership changes often; the ring, token/vnode count and replication
factor are owned; key and token distribution are measured; a rebalance and repair path exists;
ownership can be fenced during a change.

**Hard contraindications.** Reject when a static assignment is stable, when ring hotspots cannot
be mitigated, when rebalancing cannot be observed, or when no one can fence stale ownership during
a membership change.

**Competing alternative.** Explicit range assignment, modulo sharding or rendezvous
(highest-random-weight) hashing. Tycho's choice rule: use consistent hashing when membership churns
and per-key movement must be bounded; use ranges when range locality and operator control dominate;
use modulo only for fixed cardinality; use rendezvous when a shared ring is unacceptable. Reverse
the choice when ring operations and virtual-node tuning exceed the movement savings.

**Failure and recovery.** Hotspots, uneven token ranges and node loss are possible. Dynamo
disperses an unavailable node's load across remaining nodes and uses hinted handoff plus
anti-entropy repair; Cassandra warns that more tokens raise outage probability and maintenance cost;
Riak removes an irrecoverable node from another node. Tycho's rule: detect hot ranges, bound token
counts, verify ownership after every membership change, and treat hinted handoff as temporary
protection, not repair.

**Technical owner.** [Resharding is a multi-state data transition](../../v05-data-models-engines-and-lifecycle/c05-partitioning-sharding-and-rebalancing/resharding-transition.md#consistent-hashing) — resharding transition is bounded, not a consistent-hashing implementation.

**Sources.** [src.karger](../../../../edition/patterns/reading-ledger.v1.json)
read record `read.karger-consistent-hashing.2026-10-31`: sections "Abstract",
"1 Introduction", "4 Consistent Hashing", "4.1 Definitions" and "4.2 Construction".
[src.dynamo](../../../../edition/patterns/reading-ledger.v1.json) read record
`read.dynamo-consistent-hashing.2026-10-31`: sections "4.2 Partitioning Algorithm",
"4.3 Replication", "4.6 Handling Failures: Hinted Handoff", "4.7 Handling permanent
failures: Replica synchronization" and "4.9 Adding/Removing Storage Nodes".
[src.cassandra](../../../../edition/patterns/reading-ledger.v1.json) read record
`read.cassandra-dynamo-consistent-hashing.2026-10-31`: sections "Dataset Partitioning:
Consistent Hashing", "Consistent Hashing using a Token Ring" and "Multiple Tokens per
Physical Node (vnodes)". [src.riak](../../../../edition/patterns/reading-ledger.v1.json)
read records `read.riak-vnodes.2026-10-31`, `read.riak-clusters.2026-10-31` and
`read.riak-adding-removing-nodes.2026-10-31`: sections "Vnodes", "The Number of Vnodes
in a Cluster", "The Role of Vnodes", "Vnodes and Replication Properties", "The Ring",
"Intelligent Replication", "Gossiping", "Add a Node to an Existing Cluster", "Joining
Nodes to Form a Cluster", "Note on ring changes" and "Removing a Node From a Cluster".
The existing [src.cassandra] record `read.batch3-cassandra-arch.2026-10-21` explicitly
does not cover the token ring and remains a scope limit, not support. The sources are
public papers and documentation, not benchmarks; Tycho-labelled rules are synthesis.

**Decision state.** applicable-under-conditions.

**Related entries.** Sharding; Partitioning; Resharding; Read Replicas.
