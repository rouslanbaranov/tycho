---
metadata_version: 1
id: "tycho.page.8679c110343d4dfd862c15581b49c350"
kind: "page"
parent_id: "tycho.chapter.bee261b76181706235dd8fa7ccde01a9"
canonical_path: "book/volumes/v11-pattern-atlas/c08-coordination/session-consistency.md"
title: "Session Consistency"
topic_ids:
  - "distributed-systems"
  - "architecture-decisions"
perspectives:
  - "architecture"
  - "evaluation"
summary: >-
  Decision card for Session Consistency; all four dimensions source-bound;
  coverage remains partial-bounded, no promotion.
route_hints:
  questions:
    - >-
      Should one client session preserve selected read/write observations across
      replicas?
  prerequisites:
    - "tycho.chapter.bee261b76181706235dd8fa7ccde01a9"
  related_ids:
    - "tycho.chapter.bee261b76181706235dd8fa7ccde01a9"
  excludes:
    - >-
      No sufficient coverage, promotion or owner acceptance is claimed for this
      moved page.
  keywords:
    - "pattern atlas"
    - "session consistency"
    - "distributed coordination"
evidence_scope:
  source_ids:
    - "src.azure-cosmos-consistency"
    - "src.mongodb-causal-consistency"
    - "src.jepsen-session-models"
    - "src.jepsen-read-your-writes"
    - "src.jepsen-monotonic-reads"
  claim_ids: []
  status: "source-linked"
  notes: >-
    Card cites read.azure-cosmos-consistency.2026-10-31,
    read.mongodb-causal-consistency.2026-10-31,
    read.jepsen-consistency-models.2026-10-31,
    read.jepsen-read-your-writes.2026-10-31 and
    read.jepsen-monotonic-reads.2026-10-31; owner section and limits are bounded.
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
# Session Consistency

**Identity.** Session Consistency; family Distributed coordination; kind
coordination-pattern; priority advanced.

**Decision question.** Should one client session preserve selected read/write observations
across replicas?

**Good-fit conditions.** The application can define a session and carry its requirement across
requests; a replica can satisfy a token-aware read or the router can wait or reroute. Cosmos DB
scopes the guarantee "within a single client session" and returns an updated session token
after each write. Read-your-writes and monotonic reads are per-process properties; Jepsen
scopes its session guarantees to a process. **Tycho condition:** name the guarantee set per
session (read-your-writes, monotonic reads, monotonic writes, writes-follow-reads) and test
each independently; also name token lifetime and the failure callers receive before the first
routed read.

**Hard contraindications.** Reject when global linearizability is required, when sessions
cannot be maintained, or when the required relation cannot be established. After client
recreation or failover, rebuild the requirement from durable state or narrow the guarantee;
an epoch or lineage field is required before a token may cross a leadership change. Cosmos
session tokens are
"partition-bound", and a re-created client cache begins without them. **Tycho rule:** a sticky
route or a token that cannot survive failover is not a session guarantee.

**Competing alternative.** **Tycho comparison:** causal consistency is the stronger adjacent
contract. With majority reads and writes MongoDB's causally consistent session provides "Read
own writes", "Monotonic reads", "Monotonic writes" and "Writes follow reads". Linearizable
reads are the strongest alternative. Jepsen notes that "All models at or stronger than read
your writes can be at most sticky available." **Tycho choice rule:** use session consistency
when per-client continuity is the requirement and token-aware routing is cheaper than global
coordination; causal consistency when cross-client dependencies travel; linearizable reads
when one latest state is required.
`{ w: 1 }` can roll back, so durability needs majority reads and writes. Reverse when token
propagation or failover cost exceeds the user-visible benefit, or when the weaker view cannot
be explained to the user.

**Failure and recovery.** Token loss, server switching and multiwriter frontiers are possible.
MongoDB shows that majority reads and writes keep causal guarantees "even in circumstances
(such as with a network partition) where two members in a replica set transiently believe that
they are the primary"; weaker write concern may roll back. Cosmos retries another replica when
the replica lacks the session's data, and returns the latest version when an old token meets
newer data. Validate and preserve the token only when its epoch or lineage is comparable,
bound waits, and return a retryable failure rather than serving an older snapshot.
**Tycho runbook:** validate token scope and epoch, rebuild the requirement from durable state
after client recreation or failover (or narrow the guarantee), and never collapse a
multiwriter frontier into one scalar.

**Technical owner.** [Session Consistency](../../v04-distributed-coordination-and-events/c02-replication-consensus-and-leader-changes/session-consistency.md#session-consistency) — session consistency is bounded, not a complete client-session protocol.

**Sources.** Five records in the
[shared reading ledger](../../../../edition/patterns/reading-ledger.v1.json):

- `read.azure-cosmos-consistency.2026-10-31` (src.azure-cosmos-consistency),
  section "Session consistency"; revision `2e1f621c...`.
- `read.mongodb-causal-consistency.2026-10-31` (src.mongodb-causal-consistency),
  sections "Causal Consistency and Read and Write Concerns" and "Scenarios"; revision
  `4e7c1d14...`.
- `read.jepsen-consistency-models.2026-10-31` (src.jepsen-session-models), sections
  "Consistency Models", "Processes" and "Histories"; revision `05d547d3...`.
- `read.jepsen-read-your-writes.2026-10-31` (src.jepsen-read-your-writes), whole page;
  revision `c5069583...`.
- `read.jepsen-monotonic-reads.2026-10-31` (src.jepsen-monotonic-reads), whole page;
  revision `1c5d413f...`.

The units are public living pages, not benchmarks or production observations. No database,
replica set, partition or client session was created or run.

**Decision state.** applicable-under-conditions.

**Related entries.** Causal Ordering; Read Replicas; Leader-Follower Replication.
