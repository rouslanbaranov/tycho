# B38 — Sharding failure/recovery and alternative lane

Status: lane-local book edit, self-checked on 2026-10-30. No shared edition
metadata, promotion, generated artifact or owner acceptance is included. The
entry was 2/4 at the parent HEAD: mechanism and invariant were supported;
failure/recovery and alternative were partial. This lane binds both partial
dimensions to public MongoDB 9.0, Citus 13.0.1 and PostgreSQL 18.6 pages, and
labels map drift, split brain, per-key throttling, dual-read/verify and the
selection rule as Tycho guidance. The card remains inline in V11/C06.

## Lane coordinates

- Parent HEAD: `8020601a3501a401ffd15bedba11ed3a79334778` (`8020601a`).
- Branch: `b38-sharding`; worktree:
  `/Users/rbaranov/Projects/tycho-worktrees/b38-sharding`.
- Scope: the owner section `### Sharding` in the V05/C05 page and the inline
  V11/C06 card `### Sharding`. Single-entry lane; no other entry, shared JSON,
  promotion or generated file is changed.
- Owner path (concatenate):

      book/volumes/v05-data-models-engines-and-lifecycle/
      c05-partitioning-sharding-and-rebalancing/
      shard-keys-hotspots-and-resharding.md

- Card path:
  `book/volumes/v11-pattern-atlas/c06-database-storage/README.md`.
- Path check: the parent brief named V11 (C04/C06). At this HEAD V11/C04 is
  distributed coordination and events and has no sharding card; V11/C06 is
  database and storage and carries the inline card at line 77. No C04 card
  was created, and the card stays inline rather than being split.
- Current source register: `src.mongo-sharding`, `src.citus` and
  `src.postgresql` are admitted. This lane adds no new source identity.
- Baseline line-length and boundary checks pass before and after the edit.

## Candidate evaluation

- MongoDB, "Sharding" (selected). Supplies the vertical-versus-horizontal
  scaling comparison, the practical maximum for vertical scaling and the
  infrastructure-complexity trade-off.
- MongoDB, "Choose a Shard Key" (selected). Supplies the low-cardinality,
  frequency and monotonic-key statements used to explain skew and hotspots.
- MongoDB, "Troubleshoot Shard Keys" (selected). Supplies the explicit
  `hot shard` and `hot chunk` wording, uneven load distribution and jumbo
  chunks.
- MongoDB, "Sharded Cluster Balancer" (selected). Supplies data-size migration
  thresholds, the brief read/write pause for range-location metadata, the
  metadata update rule, secondary throttle and failover cleanup.
- MongoDB, "Reshard a Collection" (selected). Supplies the two-second write
  block, duplicate-`_id` failure and five-minute retry window.
- Citus, "Cluster Management" (selected). Supplies the brief write-lock while
  promoting the subscriber shard, worker-node failure tolerance, coordinator
  metadata replication/restore and the Zipfian tenant-skew statement.
- Citus, "Choosing Distribution Column" (selected). Supplies the skew
  accumulation statement, the recommendation to use PostgreSQL table
  partitioning for time and the cross-network joins statement.
- PostgreSQL, "High Availability, Load Balancing, and Replication" (selected).
  Supplies hot-standby read-only service and the stale-asynchronous-read
  warning.
- PostgreSQL, "Table Partitioning" (retained). The existing record
  `read.batch3-pg-partition.2026-10-21` still matches the 2026-10-30
  representation and binds the partitioning alternative.
- Citus, "Concepts" (retained, not replaced). The existing record
  `read.batch3-citus.2026-10-21` remains the mechanism binding; it was
  truncated at 100,000 characters and is not reused for the new claims.
- PostgreSQL, "Comparison of Different Solutions" (examined, not selected).
  Its feature matrix confirms read-only replicas, but the chapter landing page
  carries the prose quotes used here; a second unit would duplicate them.
- MongoDB, "Replication" (examined, not selected). It describes replica-set
  availability but not the sharded-cluster failure modes bound here.
- MongoDB, "Sharding Strategy" and "Hashed Sharding" (examined, not selected).
  They define strategy choices but add no hotspot, migration or alternative
  evidence beyond the selected pages.
- MongoDB, "Back Up Cluster Metadata" and "Restore a Sharded Cluster"
  (examined, not selected). They cover backup and restore of cluster state,
  not drift detection, split-brain handling or a read-verification procedure.

## Source binding

Quotes reproduce the served prose. Markdown emphasis, inline code markers and
link markup are removed, and the extractor's inserted space before punctuation
is normalized; line breaks inside a quote are editorial wrapping. The binding
revision is the SHA-256 of the whitespace-collapsed article-region text, not
the raw HTML digest. MongoDB and the PostgreSQL documentation serve dynamic
markup and CDN variants, so their raw HTML digests differ between fetches while
the article text stayed stable on 2026-10-30. Each subsection records both
digests.

### MongoDB — Sharding

- Source id: `src.mongo-sharding` (existing).
- Proposed record: `read.mongo-sharding.2026-10-30`.
- URL: `https://www.mongodb.com/docs/manual/sharding/`.
- Unit label: "Sharding — MongoDB Database Manual"; unit type
  `documentation-page`; access date 2026-10-30.
- Representation: HTTP 200, 842,364 bytes, HTTP Date
  2026-10-30T20:19:24Z, ETag `W/"qm2optbcnvi1sw"`, `x-nextjs-date`
  2026-10-30T20:18:00Z; raw HTML SHA-256
  `b3b9dd5dab4ef65c49cdfe3c5276917e5777984ceb3c562c0c9b1ec98cd00944`.
  Article-region text 13,477 characters, SHA-256
  `09c9f5c2f2d4f3d80052cbc49a35dc941b4725b53c5768ab3303fb1315e07719`.
  Page version badge: 9.0 (Current). This is the binding revision.
- Sections used: "Sharding", "Sharded Cluster", "Shard Keys", "Chunks",
  "Balancer and Even Data Distribution", "Advantages of Sharding",
  "Considerations Before Sharding", "Reshard to Shard", "Sharded and
  Non-Sharded Collections", "Connecting to a Sharded Cluster".
- Exact quotes used:

      Sharding is a method for distributing data across multiple machines.
      MongoDB uses sharding to support deployments with very large data sets
      and high throughput operations.

      Two methods address system growth: vertical and horizontal scaling.

      Vertical Scaling increases the capacity of a single server by using a
      more powerful CPU, adding more RAM, or expanding storage. Available
      technology and cloud provider hardware configurations impose a practical
      maximum for vertical scaling.

      Horizontal Scaling involves dividing the system dataset and load over
      multiple servers, adding more servers to increase capacity as required.
      Each machine handles a subset of the overall workload, which can cost
      less than high-end hardware for a single machine. The trade-off is
      increased complexity in infrastructure and maintenance.

- Limits: one rolling product page; no deployment or benchmark was run. The
  page states a practical maximum for vertical scaling but gives no sizing
  rule or cost comparison.

### MongoDB — Choose a Shard Key

- Source id: `src.mongo-sharding` (existing).
- Proposed record: `read.mongo-choose-key.2026-10-30`.
- URL:
  `https://www.mongodb.com/docs/manual/core/sharding-choose-a-shard-key/`.
- Unit label: "Choose a Shard Key — MongoDB Database Manual"; unit type
  `documentation-page`; access date 2026-10-30.
- Representation: HTTP 200, 774,818 bytes, HTTP Date
  2026-10-30T20:19:25Z, ETag `W/"z7ax9r4i8qglos"`, `x-nextjs-date`
  2026-10-30T20:19:05Z; raw HTML SHA-256
  `8d8431a19179dd4047eefe6431fa1c606594332939f878ebf713596a65a0d8a8`.
  Article-region text 7,879 characters, SHA-256
  `028080d0468f7760db4f907ec18092f6e4e66a0a7b28e6b0b380e29d0a391bae`.
  Page version badge: 9.0 (Current). This is the binding revision.
- Sections used: "Shard Key Cardinality", "Shard Key Frequency",
  "Monotonically Changing Shard Keys", "Sharding Query Patterns".
- Exact quotes used:

      A shard key with low cardinality reduces the effectiveness of
      horizontal scaling in the cluster.

      The frequency of the shard key represents how often a given shard key
      value occurs in the data. If the majority of documents contain only a
      subset of the possible shard key values, then the chunks storing the
      documents with those values can become a bottleneck within the cluster.

      A shard key on a value that increases or decreases monotonically is more
      likely to distribute inserts to a single chunk within the cluster.

- Limits: one rolling product page; no shard-key distribution or hotspot was
  measured. The page gives design guidance, not a universal key choice.

### MongoDB — Troubleshoot Shard Keys

- Source id: `src.mongo-sharding` (existing).
- Proposed record: `read.mongo-troubleshoot-key.2026-10-30`.
- URL:
  `https://www.mongodb.com/docs/manual/core/sharding-troubleshooting-shard-keys/`.
- Unit label: "Troubleshoot Shard Keys — MongoDB Database Manual"; unit type
  `documentation-page`; access date 2026-10-30.
- Representation: HTTP 200, 726,175 bytes, HTTP Date
  2026-10-30T20:19:26Z, ETag `W/"13u0kr3887yfk68"`, `x-nextjs-date`
  2026-10-30T20:19:26Z; raw HTML SHA-256
  `7b9a9c4ac929dad8182414436ad46e35cdd6190c52e55d8463e423ab9127873c`.
  Article-region text 3,418 characters, SHA-256
  `b88b641ccfc4b86a622fb9110be6ed724867466120872d70d27358f77fa9e12b`.
  Page version badge: 9.0 (Current). This is the binding revision.
- Sections used: "Jumbo Chunks", "Uneven Load Distribution", "Decreased Query
  Performance Over Time".
- Exact quotes used:

      If your cluster is experiencing uneven load distribution, check if your
      shard key increases monotonically. A shard key that is a monotonically
      increasing field, leads to an uneven read and write distribution.

      New documents are generally written to the same shard and chunk. The
      shard and chunk that receive the writes are called hot shard and hot
      chunk. The hot shard changes over time. When chunks are split, the hot
      chunk moves to a different shard to optimize data distribution.

      If users are more likely to interact with recent orders, which are all on
      the same shard, the shard that contains recent orders will receive most
      of the traffic.

- Limits: one rolling troubleshooting page; it names symptoms and remedies but
  does not provide an automatic skew detector or a measured hotspot profile.

### MongoDB — Sharded Cluster Balancer

- Source id: `src.mongo-sharding` (existing).
- Proposed record: `read.mongo-balancer.2026-10-30`.
- URL:
  `https://www.mongodb.com/docs/manual/core/sharding-balancer-administration/`.
- Unit label: "Sharded Cluster Balancer — MongoDB Database Manual"; unit type
  `documentation-page`; access date 2026-10-30.
- Representation: HTTP 200, 807,135 bytes, HTTP Date
  2026-10-30T20:19:27Z, ETag `W/"bma9d14zhghaml"`, `x-nextjs-date`
  2026-10-30T20:19:27Z; raw HTML SHA-256
  `db8c13fbd3d9b1c29cdef05da613edbb3504c08ce2e51b527445ab57566b7c2d`.
  Article-region text 14,579 characters, SHA-256
  `94054402b2335b4dd8330d82b692d9d15fbd40852b3832b443d5b5384bfabb59`.
  Page version badge: 9.0 (Current). This is the binding revision.
- Sections used: "Balancer Internals", "Range Migration Procedure", "Migration
  Thresholds", "Range Migration and Replication", "Maximum Number of Documents
  Per Range to Migrate", "Range Deletion Performance Tuning", "Reshard to
  Balance".
- Exact quotes used:

      The MongoDB balancer is a background process that monitors the amount of
      data on each shard for each sharded collection. When the amount of data
      for a sharded collection on a given shard reaches specific migration
      thresholds, the balancer attempts to automatically migrate data between
      shards and reach an even amount of data per shard while respecting the
      zones.

      The balancing procedure for sharded clusters is entirely transparent to
      the user and application layer, though there may be some performance
      impact while the procedure takes place.

      MongoDB briefly pauses all application reads and writes to the collection
      being migrated to on the source shard before updating the config servers
      with the range location. MongoDB resumes application reads and writes
      after the update. The range move requires all writes to be acknowledged
      by majority of the members of the replica set both before and after
      committing the range move to config servers.

      When chunks are moved, split, or merged, the shard metadata is updated
      after the chunk operation is committed by a config server. Shards not
      involved in the chunk operation are also updated with new metadata.

      Range migrations are enhanced to be more resilient in the event of a
      failover during the delete phase. Orphaned documents are cleaned up even
      if a replica set's primary crashes or restarts during this phase.

- Limits: one rolling product page; it describes the balancing procedure, not
  a measured migration, downtime window or recovery test.

### MongoDB — Reshard a Collection

- Source id: `src.mongo-sharding` (existing).
- Proposed record: `read.mongo-reshard.2026-10-30`.
- URL:
  `https://www.mongodb.com/docs/manual/core/sharding-reshard-a-collection/`.
- Unit label: "Reshard a Collection — MongoDB Database Manual"; unit type
  `documentation-page`; access date 2026-10-30.
- Representation: HTTP 200, 835,762 bytes, HTTP Date
  2026-10-30T20:19:28Z, ETag `W/"11sov8nl4pohwo3"`, `x-nextjs-date`
  2026-10-30T20:19:28Z; raw HTML SHA-256
  `fe734f74a1b56c02c7253093c8788dfcb507dee977927ca898beedf9f138d6a8`.
  Article-region text 11,038 characters, SHA-256
  `23518406020a852d3c31729059ef204fb0924777948babd90bd39c4e8fea3795`.
  Page version badge: 9.0 (Current). This is the binding revision.
- Sections used: "About this Task", "Before you Begin", "Behavior", "Minimum
  Duration of a Resharding Operation", "Retryable Writes", "Reshard
  Limitations", "Error Case", "Duplicate _id Values".
- Exact quotes used:

      Your application can tolerate a period of two seconds where the affected
      collection blocks writes. During the time period where writes are
      blocked, your application experiences an increase in latency. If your
      workload cannot tolerate this requirement, consider refining your shard
      key instead.

      Retryable writes initiated before or during resharding can be retried
      during and after the collection has been resharded for up to 5 minutes.
      After 5 minutes you may be unable to find the definitive result of the
      write and subsequent attempts to retry the write fail with an
      IncompleteTransactionHistory error.

      The resharding operation fails if _id values are not globally unique to
      avoid corrupting collection data. Duplicate _id values can also prevent
      successful chunk migration.

- Limits: one rolling product page; it states application requirements and
  failure behavior but reports no migration test or data-verification result.

### Citus — Cluster Management

- Source id: `src.citus` (existing).
- Proposed record: `read.citus-cluster.2026-10-30`.
- URL:
  `https://docs.citusdata.com/en/v13.0/admin_guide/cluster_management.html`.
- Unit label: "Cluster Management — Citus 13.0.1 documentation"; unit type
  `documentation-page`; access date 2026-10-30.
- Representation: HTTP 200, 159,200 bytes, HTTP Date
  2026-10-30T20:19:29Z, Last-Modified 2025-02-06T16:10:03Z, ETag
  `W/"09f19f539086badabb8421370c493aa4"`; raw HTML SHA-256
  `f7ff15fc783546679ea9fd2310477374427f668f7978c8d9a46f905c640747f3`.
  Article-region text 37,025 characters, SHA-256
  `1bf0aeeced99fa77d25aae053c6f5997beca2b1bed4e0ede2f02ce3a85415640`.
  Version: Citus 13.0.1. This is the binding revision.
- Sections used: "Choosing Cluster Size", "Rebalance Shards without Downtime",
  "How it Works", "Dealing With Node Failures", "Worker Node Failures",
  "Coordinator Node Failures", "Tenant Isolation".
- Exact quotes used:

      Citus uses PostgreSQL streaming replication, allowing it to tolerate
      worker-node failures.

      The Citus coordinator maintains metadata tables to track all of the
      cluster nodes and the locations of the database shards on those nodes.
      The metadata tables are small (typically a few MBs in size) and do not
      change very often. This means that they can be replicated and quickly
      restored if the node ever experiences a failure.

      Citus’s shard rebalancing uses PostgreSQL logical replication to move
      data from the old shard (called the “publisher” in replication terms) to
      the new (the “subscriber.”) Logical replication allows application reads
      and writes to continue uninterrupted while copying shard data. Citus
      puts a brief write-lock on a shard only during the time it takes to
      update metadata to promote the subscriber shard as active.

      Citus Community edition 11.0+ supports fully online shard rebalancing.

      However, sharing shards can cause resource contention when tenants
      differ drastically in size. This is a common situation for systems with
      a large number of tenants – we have observed that the size of tenant data
      tend to follow a Zipfian distribution as the number of tenants increases.

- Limits: one versioned documentation page; no Citus cluster, rebalance or
  failover was exercised. The page states mechanisms, not a zero-downtime
  guarantee for every workload.

### Citus — Choosing Distribution Column

- Source id: `src.citus` (existing).
- Proposed record: `read.citus-datamodel.2026-10-30`.
- URL:
  `https://docs.citusdata.com/en/v13.0/sharding/data_modeling.html`.
- Unit label: "Choosing Distribution Column — Citus 13.0.1 documentation"; unit
  type `documentation-page`; access date 2026-10-30.
- Representation: HTTP 200, 115,467 bytes, HTTP Date
  2026-10-30T20:19:29Z, Last-Modified 2025-02-06T16:10:02Z, ETag
  `W/"47434077141e17c0e7e3f02ef5263f96"`; raw HTML SHA-256
  `53274a187382fd63189610b0d91536f2f1aeed3b002198f22a018c5a85fff7c9`.
  Article-region text 17,124 characters, SHA-256
  `5081a6810d6f9e3b0ed5370af4b648aaee513657d065129593f6c531c0d654aa`.
  Version: Citus 13.0.1. This is the binding revision.
- Sections used: "Best Practices", "Table Co-Location", "Distributing Tables
  by ID", "Distributing Tables by tenant".
- Exact quotes used:

      If you distribute a table on a column skewed to certain common values,
      then data in the table will tend to accumulate in certain shards. The
      nodes holding those shards will end up doing more work than other nodes.

      Use PostgreSQL table partitioning for time instead.

      The solution to rapidly scaling databases is to distribute them, but
      this creates a performance problem of its own: relational operations
      such as joins then need to cross the network boundary.

- Limits: one versioned documentation page; it gives modeling guidance, not a
  cost model or a measured comparison with replicas or vertical scaling.

### PostgreSQL — High Availability, Load Balancing, and Replication

- Source id: `src.postgresql` (existing).
- Proposed record: `read.pg18-ha.2026-10-30`.
- URL: `https://www.postgresql.org/docs/18/high-availability.html`.
- Unit label: "High Availability, Load Balancing, and Replication —
  PostgreSQL 18 documentation"; unit type `documentation-page`; access date
  2026-10-30.
- Representation: HTTP 200, 20,418 bytes, HTTP Date 2026-10-30T20:08:03Z; no
  ETag or Last-Modified; raw HTML SHA-256
  `6abaf4548a557ec8142ca7eebe8d1a62e7645a0f50c29b698d8c8bfed1c68592`.
  Article-region text 3,686 characters, SHA-256
  `d698df8b9a70f099937b74505a17be21a69f53c133668a6fca28563149d56f9d`.
  Version: PostgreSQL 18.6. This is the binding revision.
- Sections used: "Chapter 26. High Availability, Load Balancing, and
  Replication".
- Exact quotes used:

      Database servers can work together to allow a second server to take over
      quickly if the primary server fails (high availability), or to allow
      several computers to serve the same data (load balancing).

      In fact, read-only database servers can be combined relatively easily
      too.

      A standby server that cannot be connected to until it is promoted to a
      primary server is called a warm standby server, and one that can accept
      connections and serves read-only queries is called a hot standby server.

      In contrast, asynchronous solutions allow some delay between the time of
      a commit and its propagation to the other servers, opening the
      possibility that some transactions might be lost in the switch to a
      backup server, and that load balanced servers might return slightly
      stale results.

- Limits: one chapter landing page; it introduces replication and failover
  options but does not configure a replica, measure lag or test a failover.

### PostgreSQL — Table Partitioning (retained)

- Source id: `src.postgresql` (existing).
- Retained record: `read.batch3-pg-partition.2026-10-21`; content SHA-256
  `6f4540b06405f349bbffa5a003e1788584c1f3dbe6167e997e76c7e721406001`.
- URL: `https://www.postgresql.org/docs/current/ddl-partitioning.html`.
- The page was fetched again on 2026-10-30 and returned the same 71,640
  bytes and the same raw digest as the retained record; the record is not
  replaced.
- Sections used: "5.12.1. Overview".
- Exact quotes used:

      Partitioning refers to splitting what is logically one large table into
      smaller physical pieces.

      These benefits will normally be worthwhile only when a table would
      otherwise be very large.

- Limits: one documentation page; no partition was created, pruned or
  benchmarked.

## Book edits

### Owner section

- Frontmatter: only `updated_at` moves from 2026-10-20 to 2026-10-30.
  `evidence_scope`, `content_review`, `source_inspection_date` and
  `content_verified_at` are unchanged; the new sources are proposed records,
  not new `evidence_scope` ids.
- The mechanism and invariant sentences are unchanged.
- The failure/recovery paragraph is labelled **Tycho synthesis**. It binds
  MongoDB's hot-shard and low-cardinality statements, the balancer's
  data-size thresholds and read/write pause, Citus's brief write-lock, and
  MongoDB's reshard failure and retry bounds. The paragraph labels map drift,
  split brain, application-level hot-key throttling and dual-read/verify as
  Tycho failure modes; no selected page states a drift detector, split-brain
  protocol or read-verification procedure.
- The alternative paragraph is labelled **Tycho comparison**. It binds
  PostgreSQL partitioning, PostgreSQL hot-standby reads and asynchronous
  staleness, MongoDB vertical scaling and Citus cross-network joins. The
  rule that these alternatives are preferable when distribution adds
  cross-shard coordination without relieving the measured constraint is
  labelled Tycho guidance.
- A sources-and-limits paragraph names the proposed records, editions and the
  retained PostgreSQL partition record; it states that no cluster, rebalance
  or migration was run.
- The `### Sharding` heading stays at line 126. The `## Sharding ownership
  notes` heading and the preceding `### Partitioning` section are unchanged,
  so the owner-unit line for Partitioning stays at 105. The page grows from
  140 to 171 lines.
- Raw SHA-256: `148542e538d59052e1817ebc95a69f1ddf5fd2d268e4ec62f054b3302e593818`.
- Historical-view SHA-256: `5a85a0b24bf295c67f3d7ffb65b5b5ce1273e0df88f9e69d6ff4592415409101`.
- Base raw SHA-256: `882d3cc6d9bedf396ce5fa395e6ae7560f32ad9da5e7d9d9a3d1a0d2e6a0b0e4`;
  base historical-view SHA-256:
  `e5ae4c19dd2335ab51bb8abd502a6316d5d13fc78f4ffa67444d1bc58900dab0`.

### V11/C06 inline card

- `evidence_scope.source_ids` adds `src.mongo-sharding`. The earlier
  `src.citus` and `src.postgresql` ids remain. Other frontmatter is
  unchanged.
- **Good-fit conditions** now require a bounded retry or rollback path for a
  failed migration.
- **Hard contraindications** now include a failed migration that cannot be
  detected and verified.
- **Competing alternative** now compares partitioning, read replicas (hot
  standby) and vertical scaling, names the PostgreSQL, MongoDB and Citus
  statements, and labels the reversal rule as Tycho synthesis.
- **Failure and recovery** now points to hot chunks, the balancer metadata
  pause, Citus's brief write-lock and bounded reshard retries, and labels map
  drift, split brain, hot-key throttling and dual-read/verify as Tycho
  failure modes.
- **Sources** retains the mechanism record and names the proposed records plus
  the retained PostgreSQL partition record; it states that no benchmark,
  cluster run or migration test was performed.
- The heading stays at line 77; the chapter page grows from 460 to 473 lines.
- Raw SHA-256: `747aa588f881122cdb21d7a907064833050810a85b3bccaf54d4b6be88af63ca`.
- Historical-view SHA-256: `c827f5a8a907d79b3be689022b14aa024b1c5e457c506eb2c785e247fec3c9f9`.
- Base raw SHA-256: `3c0ccfb2a3869020368d6d7b90d7bae95ec77a2065337f14d7712f05581b6a77`;
  base historical-view SHA-256:
  `ca6da267affe777ce4f894506145c6c6bb1524832081c8f36b1a66d6b058d105`.

No other book file is changed by this lane.

## Metadata needs (integrator)

The following changes are not in the lane commit. They require the book/atlas
independent review gate before merge.

### Source register `sources/register.json`

Set `updated` to 2026-10-30; the source count stays 297.

- `src.mongo-sharding`: set reading status to
  `full-public-page-inspected`; set `access_checked` and
  `content_verified` to 2026-10-30; record version "MongoDB 9.0 (Current);
  Sharding, Choose a Shard Key, Troubleshoot Shard Keys, Sharded Cluster
  Balancer and Reshard a Collection inspected 2026-10-30; article-text
  SHA-256 09c9f5c2..., 028080d0..., b88b641c..., 94054402... and 23518406..."
  with the full values from the Source binding section; extend
  `verification_scope` to name the five pages and their sections and to state
  that no shard cluster, migration or benchmark was run.
- `src.citus`: set reading status to `full-public-page-inspected`; set
  `content_verified` to 2026-10-30; record "Citus 13.0.1; Cluster Management
  and Choosing Distribution Column inspected 2026-10-30; article-text
  SHA-256 1bf0aeee... and 5081a681...; Last-Modified 2025-02-06"; extend
  `verification_scope` to the two pages and exclude implementation tests.
- `src.postgresql`: set `content_verified` to 2026-10-30; append the
  PostgreSQL 18.6 High Availability page and article-text SHA-256
  `d698df8b...` to `version` and `verification_scope`; keep the existing
  Table Partitioning representation.
- Do not change the URLs or admission state of any of the three sources.

### Reading ledger `edition/patterns/reading-ledger.v1.json`

Add eight records; set `updated` to 2026-10-30. Records move from 186 to 194.
Each record is `status: read`, `reviewer: "Automated authoring agent"`, unit
type `documentation-page`, and uses the exact URL, sections and
`content_sha256` (the article-text revision) below.

- `read.mongo-sharding.2026-10-30` — `src.mongo-sharding`; sections as in
  the source binding; content_sha256
  `09c9f5c2f2d4f3d80052cbc49a35dc941b4725b53c5768ab3303fb1315e07719`.
- `read.mongo-choose-key.2026-10-30` — `src.mongo-sharding`; sections
  "Shard Key Cardinality", "Shard Key Frequency", "Monotonically Changing
  Shard Keys", "Sharding Query Patterns"; content_sha256
  `028080d0468f7760db4f907ec18092f6e4e66a0a7b28e6b0b380e29d0a391bae`.
- `read.mongo-troubleshoot-key.2026-10-30` — `src.mongo-sharding`;
  sections "Jumbo Chunks", "Uneven Load Distribution", "Decreased Query
  Performance Over Time"; content_sha256
  `b88b641ccfc4b86a622fb9110be6ed724867466120872d70d27358f77fa9e12b`.
- `read.mongo-balancer.2026-10-30` — `src.mongo-sharding`; sections as in
  the source binding; content_sha256
  `94054402b2335b4dd8330d82b692d9d15fbd40852b3832b443d5b5384bfabb59`.
- `read.mongo-reshard.2026-10-30` — `src.mongo-sharding`; sections as in
  the source binding; content_sha256
  `23518406020a852d3c31729059ef204fb0924777948babd90bd39c4e8fea3795`.
- `read.citus-cluster.2026-10-30` — `src.citus`; sections as in the source
  binding; content_sha256
  `1bf0aeeced99fa77d25aae053c6f5997beca2b1bed4e0ede2f02ce3a85415640`.
- `read.citus-datamodel.2026-10-30` — `src.citus`; sections as in the
  source binding; content_sha256
  `5081a6810d6f9e3b0ed5370af4b648aaee513657d065129593f6c531c0d654aa`.
- `read.pg18-ha.2026-10-30` — `src.postgresql`; section "Chapter 26. High
  Availability, Load Balancing, and Replication"; content_sha256
  `d698df8b9a70f099937b74505a17be21a69f53c133668a6fca28563149d56f9d`.

The retained `read.batch3-citus.2026-10-21` and
`read.batch3-pg-partition.2026-10-21` records stay unchanged.

Binding revisions for the owner-units patch (each must equal the ledger
`content_sha256`):

- `read.mongo-balancer.2026-10-30`: `94054402...`;
- `read.mongo-troubleshoot-key.2026-10-30`: `b88b641c...`;
- `read.mongo-choose-key.2026-10-30`: `028080d0...`;
- `read.mongo-reshard.2026-10-30`: `23518406...`;
- `read.citus-cluster.2026-10-30`: `1bf0aeee...`;
- `read.citus-datamodel.2026-10-30`: `5081a681...`;
- `read.mongo-sharding.2026-10-30`: `09c9f5c2...`;
- `read.pg18-ha.2026-10-30`: `d698df8b...`;
- `read.batch3-pg-partition.2026-10-21`: `6f4540b0...`;
- `read.batch3-citus.2026-10-21`: `87d1d3ad...`.

### Source plan `edition/patterns/source-plan.v1.json`

Append the eight units to `tycho.pattern.sharding` after the existing Citus
concepts unit, in the order above. Use the same source ids, labels, URLs,
unit types, section lists, status `read` and record ids as the Source binding
section. Set `updated` to 2026-10-30. Summary moves:

- `required_units` 223 -> 231;
- `read_units` 222 -> 230;
- `ledger_records` 186 -> 194.

Replace the entry notes with: "The 2026-10-30 MongoDB, Citus and PostgreSQL
units support hotspot, balancer, reshard, replication and alternative
statements; map drift, split brain, per-key throttle, dual-read/verify and the
selection rule remain Tycho guidance." Recompute `registry_sha256` after
saving the registry and refresh `route_index_snapshot` from the rebuilt route
index.

### Registry `edition/patterns/registry.v1.json`

For `tycho.pattern.sharding`:

- Set `technical_owner.state` to `partial-bounded` (unchanged).
- Keep `coverage.technical`, `coverage.decision` and `coverage.overall`
  at `partial-bounded`.
- Append eight `source_units` after the existing Citus concepts unit, in the
  source-plan order, all with status `read`.
- Replace `notes` with: "Failure/recovery and alternative bound 2026-10-30 to
  MongoDB 9.0, Citus 13.0.1 and PostgreSQL 18.6; map drift, split brain,
  per-key throttle, dual-read/verify and the selection rule remain Tycho
  guidance. Coverage partial-bounded; no promotion."
- Keep `review_status` `self-checked` and `atlas_owner` at V11/C06.
- Set `updated_at` to 2026-10-30.

### Owner units `edition/patterns/owner-units.v1.json`

Entry `tycho.pattern.sharding`:

- Keep `owner.line` at 126, the heading, document id and unit terms unchanged.
- Failure/recovery: set `state: supported`; `quote` to the exact owner
  sentence:

      Map drift, split brain, application-level hot-key throttling and
      dual-read/verify are Tycho failure modes: the selected pages document
      metadata replication/restore and write fencing, not drift detection,
      split-brain resolution, a per-key throttle or a read-verification step.

  Reason separates the MongoDB and Citus statements from the Tycho labels;
  primary binding `src.mongo-sharding`, record
  `read.mongo-balancer.2026-10-30`, section "Range Migration and
  Replication", quote "MongoDB briefly pauses all application reads and
  writes ...", revision `94054402...`; supporting bindings for
  `read.mongo-troubleshoot-key.2026-10-30`,
  `read.mongo-choose-key.2026-10-30`,
  `read.mongo-reshard.2026-10-30` and
  `read.citus-cluster.2026-10-30`.
- Alternative: set `state: supported`; `quote` to the exact owner sentence:

      These alternatives are preferable when distribution adds cross-shard
      coordination without relieving the measured constraint; that decision
      rule is Tycho guidance, not a source claim.

  Reason separates the PostgreSQL, MongoDB and Citus statements from the Tycho
  selection rule; primary binding `src.citus`, record
  `read.citus-datamodel.2026-10-30`, section "Table Co-Location", quote
  "The solution to rapidly scaling databases ...", revision `5081a681...`;
  supporting bindings for `read.mongo-sharding.2026-10-30`,
  `read.pg18-ha.2026-10-30` and
  `read.batch3-pg-partition.2026-10-21`.
- Keep mechanism and invariant states, quotes and bindings unchanged.
- `source_support`: keep `read.batch3-citus.2026-10-21` as the primary
  record and add auxiliary records for the eight new records with their
  revisions. Set `technical_coverage` to `partial-bounded`; set `notes`
  to the registry notes above.
- Set `decision_evidence.competing_alternative` to the new card text:
  "Partitioning within one database, read replicas (hot standby) or vertical
  scaling. PostgreSQL documents partitioning and hot-standby read-only
  replicas; MongoDB contrasts vertical scaling with horizontal scaling and its
  infrastructure complexity; Citus warns that joins cross the network
  boundary. Reverse the choice when distribution adds cross-shard coordination
  without relieving the measured constraint; that reversal rule is Tycho
  synthesis."
- No `owner.line` changes: the Partitioning heading stays at line 105 and
  the Sharding heading stays at line 126.
- Summary counters: `failure_recovery_supported` 64 -> 65;
  `alternative_supported` 70 -> 71. No other counter changes. The
  `technical_partial_bounded` and `technical_partial` counters stay at 19
  and 75.

### Card registration `edition/patterns/card-batches.v1.json`

Add `card_path`:
`book/volumes/v11-pattern-atlas/c06-database-storage/README.md` to the
`tycho.pattern.sharding` entry. This is the same file as the chapter, not a
split. Keep `ledger_record` `read.batch3-citus.2026-10-21`.

### Content revisions `edition/content-revisions.json`

Add one issue-540 revision with `authorized_at` 2026-10-30 and authorization
"B38 Sharding failure/recovery and alternative source binding; no promotion or
owner acceptance." Use these historical-view hashes:

- Owner path, previous:
  `e5ae4c19dd2335ab51bb8abd502a6316d5d13fc78f4ffa67444d1bc58900dab0`;
  current:
  `5a85a0b24bf295c67f3d7ffb65b5b5ce1273e0df88f9e69d6ff4592415409101`.
- Card path, previous:
  `ca6da267affe777ce4f894506145c6c6bb1524832081c8f36b1a66d6b058d105`;
  current:
  `c827f5a8a907d79b3be689022b14aa024b1c5e457c506eb2c785e247fec3c9f9`.
- Leave `source_blocks`, `enrichment_additions` and
  `enrichment_baselines` empty.

Raw file hashes for reference:
`148542e538d59052e1817ebc95a69f1ddf5fd2d268e4ec62f054b3302e593818` (owner) and
`747aa588f881122cdb21d7a907064833050810a85b3bccaf54d4b6be88af63ca` (card).

### Frontmatter and evidence scope

The lane leaves the owner page's `evidence_scope`,
`source_inspection_date` and `content_review` unchanged. The new records are
supporting bindings, not new `evidence_scope` ids. The card gains
`src.mongo-sharding` in `evidence_scope.source_ids` because preflight
requires every binding source to be declared on the card. If the integrator
also wants the new records in the owner `evidence_scope.source_ids`, treat it
as a separate change: add inspection entries to
`sources/enrichment-inspections-2026-10-20.json`, update the owner
`edition/enrichment-manifest.json` record's source ids, inspection date and
`sha256`, and recompute both historical-view hashes and content-revision
values.

### Derived artifacts

The book edit changes one canonical owner page and one atlas chapter. The
source register gains no new id, but the ledger, source plan, registry,
owner-units, card registration and content revision changes make the route
index, atlas registry hash, edition inventory and the coverage, census,
reverse-map, semantic-audit and delivery artifacts stale. Refresh them once at
batch end; do not treat a stale derived hash as a lane content failure. The
atlas manifest must record the new V11/C06 chapter SHA-256
`747aa588f881122cdb21d7a907064833050810a85b3bccaf54d4b6be88af63ca` and the
new owner page SHA-256
`148542e538d59052e1817ebc95a69f1ddf5fd2d268e4ec62f054b3302e593818`. The prior
sufficient review, if any, predates this edit and does not cover the changed
bytes. The book/atlas
independent review gate applies.

## Validation

Checker output in the lane worktree after the two book edits, before the lane
note:

    PASS: V11 prose <=100; 145 exact owner-link exceptions
    PASS: configured lexical boundary checks; independent-origin review still
    required.

Targeted validator results with the book edits only:

- `python3 scripts/check_markdown_line_length.py` — PASS.
- `python3 scripts/check_boundary.py` — PASS.
- `python3 scripts/validate_book_metadata.py` — PASS, 491 documents.
- `python3 scripts/validate_pattern_cards.py` — PASS, 11 batches, 145
  entries.
- `python3 scripts/validate_sources.py` — PASS, 297 source records.
- `python3 scripts/validate_enrichment.py` — PASS, explicit membership and
  byte conservation.
- `python3 scripts/validate_pattern_owner_units.py` — expected FAIL on
  `owner-units-quote-not-verbatim: tycho.pattern.sharding:
  failure_recovery` because the lane changes the owner quote and does not
  edit the shared JSON.
- `python3 scripts/preflight_sufficient.py --pattern
  tycho.pattern.sharding` — expected FAIL on failure/recovery and alternative
  states `partial` and on `card_path missing or absent`.
- `python3 scripts/validate_pattern_atlas.py` — expected FAIL on
  `atlas-document-sha` because the lane intentionally does not refresh
  derived artifacts.

The full unit suite is not run; batch-end tests remain with the integrator.
No runtime MongoDB, Citus or PostgreSQL cluster, balancer, reshard or failover
was exercised.

## Limits

The binding uses five MongoDB 9.0 (Current) pages, two Citus 13.0.1 pages and
one PostgreSQL 18.6 page, plus the retained PostgreSQL 18 Table Partitioning
record. None of the selected pages reports a deployment test, a measured hot
shard, a completed reshard or a failover result. Map drift, split brain,
application-level hot-key throttling, dual-read/verify and the selection rule
are Tycho synthesis; the dimensions are `supported` only because the owner
section separates those additions from the source-supported statements. A
reviewer that requires every word of the owner quote to be source-quoted
should treat the dimensions as partial instead.

The raw HTML digests for MongoDB and PostgreSQL changed between fetches on
2026-10-30; the article-text digests were stable across independent fetches.
The binding revisions are therefore article-text digests, and the raw digests
are representation evidence only. The lane does not claim that the rolling
MongoDB pages will remain unchanged after 2026-10-30.

No independent AI review, owner acceptance, promotion, CI or production
observation is claimed. The card remains inline in V11/C06; this lane did not
create a second card.

## Commit scope

The lane commit contains this note and the two book files only:

- the owner path listed under Lane coordinates;
- the card path `book/volumes/v11-pattern-atlas/c06-database-storage/README.md`.

No shared JSON, promotion, test or generated file is in the lane commit.
