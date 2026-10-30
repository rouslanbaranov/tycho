# B35 — Quorum-Based Reads/Writes invariant and failure/recovery lane

Status: lane-local book edit, self-checked on 2026-10-30. No shared edition
metadata, promotion, generated artifact or owner acceptance is included. The
entry was 2/4 at the parent HEAD: mechanism and alternative were supported;
invariant and failure/recovery were partial. This lane binds the source-supported
parts of both dimensions to Apache Cassandra, the SOSP 2007 Dynamo paper and
Riak KV 2.2.3, and labels the old/new quorum-overlap rule and the
highest-version selector as Tycho guidance. The metadata patch was exercised in a
detached scratch copy: all targeted validators and preflight pass after
derived-artifact refresh. The patch is not in the lane commit; promotion is not
claimed or ready.

## Lane coordinates

- Parent HEAD: `49fe18df67046970bf4cd12663335c9c5ee4feb0` (`49fe18df`).
- Branch: `b35-quorum`; worktree:
  `/Users/rbaranov/Projects/tycho-worktrees/b35-quorum`.
- Scope: the owner section `### Quorum-Based Reads-Writes` in the V04/C02
  owner page and the inline V11/C06 card `### Quorum-Based Reads / Writes`.
  Single-entry lane; no other entry, shared owner page, promotion or generated
  file is changed.
- Owner path (concatenate the three lines):

      book/volumes/v04-distributed-coordination-and-events/
      c02-replication-consensus-and-leader-changes/
      quorum-envelope.md

- Card path:
  `book/volumes/v11-pattern-atlas/c06-database-storage/README.md`.
- Path discrepancy: the parent brief named V11/C04. At this HEAD V11/C04 is the
  data-consistency and event-sourcing chapter with 14 unrelated cards and no
  quorum card. The registry names V11/C06 as the atlas owner, and the card is
  inline in V11/C06. No C04 card was created.
- The card remains inline; the integrator owns any split and `card_path`
  registration.

## Candidate evaluation

- Apache Cassandra, "Dynamo — multi-master replication and tunable consistency"
  (existing source `src.cassandra`, record
  `read.batch3-cassandra-dynamo.2026-10-21`). Selected for the R + W > N
  statement, timestamp versioning, best-effort read repair and hinted handoff,
  anti-entropy repair, and the warning that simultaneous range movements can
  violate monotonic consistency and cause data loss. The page is current
  documentation for a prerelease release line; it is not a cluster experiment.
- Apache Cassandra, "Read repair" (proposed record
  `read.cassandra-read-repair.2026-10-30`). Selected for blocking read repair,
  the most-up-to-date return, the monotonic-quorum-reads expectation and the
  blocking-versus-none trade-off. It supports repair and freshness but does not
  define a membership-change overlap protocol.
- Amazon, "Dynamo: Amazon's Highly Available Key-value Store" (existing source
  `src.dynamo`, proposed record `read.dynamo-sosp2007.2026-10-30`). Selected
  for quorum arithmetic, vector clocks, divergent-version reconciliation,
  hinted handoff, Merkle-tree anti-entropy, membership handoff with a
  confirmation round, and the explicit sloppy-quorum choice. It is a 2007
  historical design paper, not evidence about current service internals.
- Riak KV 2.2.3, "Replication Properties" (proposed source `src.riak`, proposed
  record `read.riak-replication-properties.2026-10-30`). Selected for the
  half-plus-one quorum definition, sloppy and strict quorum, read repair and
  active anti-entropy, and vector-clock or timestamp conflict resolution. The
  page is pinned to a Markdown commit; no Riak cluster was run.
- Apache Cassandra, "Topology changes" (examined, not selected as a separate
  unit). It supports range streaming, consistent bootstrap failure when a
  source replica is unavailable, and repair after replacement, but adds no
  old/new quorum-overlap statement beyond the selected pages. It remains a
  candidate for a later topology-specific lane.
- Riak, "Replication" and "Strong Consistency Reference" (examined, not
  selected as separate units). They add read-repair detail and a quorum-loss
  failure rule, but the selected Replication Properties page already carries
  the quorum, repair and conflict statements used here. Adding both would
  enlarge the metadata patch without changing the decision.
- No selected page states an old/new quorum-overlap rule, and no selected page
  tests a highest-version selector or a membership change. Those parts are
  labelled Tycho guidance in the page.

## Source binding

Quotes reproduce the served prose. Markdown inline-code, bold and italic
markers are not repeated where they are formatting only. The binding revision
always identifies the exact representation.

### Apache Cassandra — Dynamo architecture page

- Source id: `src.cassandra` (existing).
- Existing record: `read.batch3-cassandra-dynamo.2026-10-21`.
- URL:
  `https://cassandra.apache.org/doc/latest/cassandra/architecture/dynamo.html`.
- Unit label: "Dynamo — multi-master replication and tunable consistency";
  unit type `documentation-page`; access date 2026-10-21; re-read 2026-10-30.
- Recheck 2026-10-30: served HTML 76,252 bytes; HTTP Date
  2026-10-30T18:26:41Z; Last-Modified 2026-08-26T07:20:02Z; ETag
  `"129dc-659ee0c3b6c6d"`; raw HTML SHA-256
  `6392972302ba65e62eab354d4b754003847ce869a464979ba894f4daf0514a65`,
  equal to the record's `content_sha256`. This is the binding revision.
- Sections used: "Ring Membership and Failure Detection", "Data Versioning",
  "Replica Synchronization", "Tunable Consistency".
- Exact quotes used:

      This also helps to prevent simultaneous range movements, where multiple
      replicas of a token range are moving at the same time, which can violate
      monotonic consistency and can even cause data loss.

      These techniques are only best-effort, however, and to guarantee eventual
      consistency Cassandra implements anti-entropy repair

      Cassandra’s consistency levels are a version of Dynamo’s R + W > N
      consistency mechanism where operators could configure the number of nodes
      that must participate in reads ( R ) and writes ( W ) to be larger than the
      replication factor ( N ).

- Limits: current documentation for a prerelease release line; one page; no
  cluster experiment, failure test or membership-change test. The
  anti-entropy quote stops before the page's linked-placeholder markup for
  "repair".

### Apache Cassandra — Read repair

- Source id: `src.cassandra` (existing).
- Proposed record: `read.cassandra-read-repair.2026-10-30`.
- URL:
  `https://cassandra.apache.org/doc/latest/cassandra/managing/operating/read_repair.html`.
- Unit label: "Read repair — Apache Cassandra documentation"; unit type
  `documentation-page`; access date 2026-10-30.
- Access: public HTTPS GET; served HTML 59,750 bytes; HTTP Date
  2026-10-30T18:27:54Z; Last-Modified 2026-08-26T07:20:02Z; ETag
  `"e966-659ee0c3b8f95"`; raw HTML SHA-256
  `104508d54a14dc5f6268504c295437ee72561733c57cc18239c2acd4712a3980`.
  This is the binding revision.
- Sections used: "Read repair", "Expectation of Monotonic Quorum Reads",
  "Table level configuration of monotonic reads".
- Exact quotes used:

      Cassandra uses a blocking read repair to ensure the expectation of
      "monotonic quorum reads" i.e. that in 2 successive quorum reads, it’s
      guaranteed the 2nd one won’t get something older than the 1st one, and
      this even if a failed quorum write made a write of the most up to date
      value only to a minority of replicas.

      The most up-to-date data is returned to the client.

      Read Repair is the process of repairing data replicas during a read
      request.

      When monotonic quorum reads are not provided and a write fails to reach a
      quorum of replicas, it may be visible in one read, and then disappear in a
      subsequent read.

      When read_repair is set to NONE, the coordinator will reconcile any
      differences between replicas, but will not attempt to repair them.

- Limits: one documentation page; no cluster experiment or failure test. The
  page presents blocking read repair as the default and the none setting as a
  trade-off, not as an old/new membership rule.

### Amazon — Dynamo: Amazon's Highly Available Key-value Store

- Source id: `src.dynamo` (existing).
- Proposed record: `read.dynamo-sosp2007.2026-10-30`.
- URL:
  `https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf`.
- Unit label: "Dynamo: Amazon's Highly Available Key-value Store — SOSP 2007
  paper"; unit type `paper`; access date 2026-10-30.
- Access: public HTTPS download; PDF 900,468 bytes, 16 pages; PDF creation
  2007-08-15, modification 2007-09-26; HTTP Date 2026-10-30T14:18:58Z;
  Last-Modified 2026-08-26T16:00:16Z; ETag
  `"d9383e34b6e8292796bfe54b0aeeb93c"`; PDF SHA-256
  `5cacd624cd7bfd37e3d22e04d8c2e347a49579d2927dbb06f40a89c0bcd40bd4`.
  This is the binding revision. Text was extracted with `pdftotext -raw`;
  extracted text is 1,663 lines, 14,930 words, SHA-256
  `2da247073d091ba83236b71dd9c5c56a19516f9f7b2e29258a0e3b5c4d4fb140`.
- Sections used: "4.4 Data Versioning", "4.5 Execution of get() and put()
  operations", "4.6 Handling Failures: Hinted Handoff", "4.7 Handling permanent
  failures: Replica synchronization", "4.8 Membership and Failure Detection",
  "4.9 Adding/Removing Storage Nodes".
- Exact quotes used:

      Setting R and W such that R + W > N yields a quorum-like system.

      If the coordinator ends up gathering multiple versions of the data, it
      returns all the versions it deems to be causally unrelated. The divergent
      versions are then reconciled and the reconciled version superseding the
      current versions is written back.

      When X is added to the system, it is in charge of storing keys in the
      ranges (F, G], (G, A] and (A, X]. As a consequence, nodes B, C and D no
      longer have to store the keys in these respective ranges. Therefore,
      nodes B, C, and D will offer to and upon confirmation from X transfer the
      appropriate set of keys.

      Finally, by adding a confirmation round between the source and the
      destination, it is made sure that the destination node does not receive
      any duplicate transfers for a given key range.

      To remedy this it does not enforce strict quorum membership and instead
      it uses a “sloppy quorum”; all read and write operations are performed on
      the first N healthy nodes from the preference list, which may not always
      be the first N nodes encountered while walking the consistent hashing
      ring.

      To handle this and other threats to durability, Dynamo implements an
      anti-entropy (replica synchronization) protocol to keep the replicas
      synchronized.

      Dynamo uses vector clocks [12] in order to capture causality between
      different versions of the same object.

- Limits: 2007 paper; historical design; extracted PDF text; no Dynamo
  deployment was tested. The paper explicitly chooses sloppy quorum over strict
  quorum membership, so it bounds the trade-off rather than supporting a strict
  overlap requirement.

### Riak KV 2.2.3 — Replication Properties

- Source id: `src.riak` (new).
- Proposed record: `read.riak-replication-properties.2026-10-30`.
- Unit URL (pinned Markdown; concatenate the two lines):

      https://github.com/basho/basho_docs/blob/6409dd9c93b08f0a6e959a1874b5568c88172f3a/
      content/riak/kv/2.2.3/developing/app-guide/replication-properties.md
- Human page:
  `https://docs.riak.com/riak/kv/2.2.3/developing/app-guide/replication-properties/index.html`.
- Unit label: "Replication Properties — Riak KV 2.2.3"; unit type
  `documentation-page`; access date 2026-10-30.
- Access: public HTTPS GET of the pinned Markdown at basho/basho_docs commit
  `6409dd9c93b08f0a6e959a1874b5568c88172f3a` (master commit date
  2022-12-12); 26,963 bytes, 580 lines, 3,802 words; SHA-256
  `b185c0be8be5d03ef51cd696ff375901edd84b707e8fad165845b7ae689f0f30`.
  HTTP Date 2026-10-30T18:28:51Z; ETag
  `"3edddb531b5b673f218ca42fe1b6a91e74b236fd5dad0d6b55559cfb24da6715"`;
  no Last-Modified header. This is the binding revision.
- Sections used: "N Value and Replication", "Primary Reads and Writes with PR
  and PW", "Durable Writes with DW", "Symbolic Consistency Names",
  "Illustrative Scenarios".
- Exact quotes used:

      A majority of the replicas must respond, that is, half plus one.

      Setting PR and/or PW to non-zero values produces a mode of operation
      called strict quorum. This mode has the advantage that the client is more
      likely to receive the most up-to-date values, but at the cost of a higher
      probability that reads or writes will fail because primary vnodes are
      unavailable.

      Riak will attempt reads and writes to primary vnodes first, but in case
      of failure, those operations will go to failover nodes in order to
      comply with the R and W values that you have set. This failover option is
      called sloppy quorum.

      When the failed vnode returns to service, it will receive the new copy of
      the data via either read repair or active anti-entropy.

      The vector clocks are used to resolve the conflict and return a single
      value, which is propagated via read repair to the relevant vnodes

      The object with the most recent timestamp is returned and propagated via
      read repair to the relevant vnodes

      Riak will decide which object "wins" on the basis of timestamps; no
      sibling will be created

- Limits: one documentation page pinned to a commit; no Riak cluster was run.
  The page documents sloppy failover and an optional strict-quorum mode; it
  does not state an old/new quorum-overlap rule. Emphasis markers around
  "strict quorum" and "sloppy quorum" are not repeated in the quotes.

## Book edits

### Owner section

- Frontmatter: only `updated_at` moves to 2026-10-30. `evidence_scope` and
  `content_review` remain byte-identical to the decomposition baseline because
  `validate_decomposition.py` protects them. `source_inspection_date` and
  `content_verified_at` stay `null`.
- The mechanism paragraph names the Cassandra, Dynamo and Riak statements of
  R + W > N and states that the arithmetic is a consistency contract.
- The invariant paragraph now separates the source-supported hazard from the
  Tycho rule. It quotes Cassandra's simultaneous-range-movement warning, records
  Dynamo's confirmation-round handoff, and records the sloppy-quorum choice in
  Dynamo and Riak. It then labels the old/new overlap rule, the refusal of
  minority authority and the repair obligation as Tycho design guidance.
- The failure/recovery paragraph now states that overlap is necessary but not
  sufficient, binds Cassandra's blocking read repair and most-up-to-date
  return, binds Cassandra's best-effort and anti-entropy language, binds
  Dynamo's version reconciliation and hinted handoff, and binds Riak's
  vector-clock resolution and read repair. It labels the highest-version
  selector as Tycho policy because Dynamo and Riak can expose concurrent
  siblings.
- A limits and source-boundary list names the four records and exact revisions.
  The heading stays at line 164; the page is 246 lines.
- Raw SHA-256:
  `0e1c24190d9ff7a6ca84d317c652d166d540d44fea5ac3424d553a3885796f21`.
- Historical-view SHA-256:
  `ed1de747f1723ca9d28e88acf8739d769f6d737b677d2a9bd1d38fb0d92c5cc6`.

### V11/C06 inline card

- Frontmatter adds `src.dynamo` and `src.riak` to
  `evidence_scope.source_ids`. The card review, update and inspection dates move
  to 2026-10-30; `content_verified_at` stays `null`.
- **Good-fit conditions** now require an application version selector and a
  repair path.
- **Hard contraindications** now reject concurrent versions that cannot be
  ordered or repaired.
- **Competing alternative** now names strict quorum and the sloppy-quorum
  availability trade-off.
- **Failure and recovery** now states the insufficiency of intersection, the
  Cassandra, Dynamo and Riak repair and version-resolution behavior, the
  application-defined total order and the membership-change overlap or
  sloppy-quorum choice.
- **Sources** names the four records and their sections. The owner link is
  unchanged.
- The heading stays at line 236; the chapter page is 505 lines.
- Raw SHA-256:
  `9ae99b3f5a4312cf8e11327a40070bc74f03ed48ca6a1ed35e23c6f41dd782c4`.
- Historical-view SHA-256:
  `ec5e84c413d2b505a341964faae59d4f70f7df02e322e7b2fcf4fd03424e73a1`.

No other book file is changed by this lane.

## Metadata needs (integrator)

The following patch is not in the lane commit. It was exercised in a detached
scratch copy of this worktree. The scratch results are in the Validation
section. The patch must not be merged until the book/atlas independent review
gate is satisfied.

### Source register `sources/register.json`

Add one source record. Set `updated` to 2026-10-30. The source count moves from
293 to 294.

- `src.riak` — title "Riak KV Documentation"; category "databases"; publisher
  "Riak KV project"; kind "official-docs"; URL the Riak KV 2.2.3 replication
  properties HTML page; resolved URL the pinned GitHub blob at commit
  `6409dd9c93b08f0a6e959a1874b5568c88172f3a`; topics
  `["databases", "replication", "quorum", "eventual-consistency",
  "read-repair"]`; priority "core"; planned use "Quorum reads/writes, sloppy
  and strict quorum, version conflict resolution and read repair for the
  Quorum-Based Reads/Writes entry."; admission "admitted-for-research"; access
  "public-web-or-author-download"; reading status
  "full-public-page-inspected"; version records the 2026-10-30 access, the
  26,963-byte/580-line Markdown at the pinned commit, SHA-256
  `b185c0be...`, HTTP Date 2026-10-30T18:28:51Z, ETag `"3edddb53..."` and no
  Last-Modified; `access_checked` and `content_verified` 2026-10-30; license
  note "Public Riak KV documentation; cite short excerpts and paraphrase; do
  not mirror."; verification scope covers the named five sections, excluding
  linked pages and Riak behavior; observed title "Replication Properties —
  Riak KV 2.2.3".
- Update `src.cassandra`: `reading_status` "full-public-page-inspected";
  `access_checked` and `content_verified` 2026-10-30; version records both the
  Dynamo architecture page (76,252 bytes, SHA-256 `63929723...`, ETag
  `"129dc-659ee0c3b6c6d"`) and the read-repair page (59,750 bytes, SHA-256
  `104508d5...`, ETag `"e966-659ee0c3b8f95"`), HTTP Last-Modified
  2026-08-26T07:20:02Z, and the prerelease documentation notice; verification
  scope names the four Dynamo-page sections and the three read-repair sections.
- Update `src.dynamo`: `reading_status` "full-public-page-inspected";
  `access_checked` and `content_verified` 2026-10-30; priority "core"; topics
  add "quorum" and "versioning"; planned use updated to the quorum, versioning,
  handoff, anti-entropy and membership-handoff scope; version records the
  900,468-byte/16-page PDF, SHA-256 `5cacd624...`, PDF creation and
  modification dates, HTTP Date 2026-10-30T14:18:58Z, Last-Modified
  2026-08-26T16:00:16Z and ETag `"d9383e34..."`; verification scope covers
  sections 4.4-4.7 and 4.9 only.

### Reading ledger `edition/patterns/reading-ledger.v1.json`

Add three records. Set `updated` to 2026-10-30. Records move from 172 to 175.

- `read.cassandra-read-repair.2026-10-30` — source `src.cassandra`; unit
  "Read repair — Apache Cassandra documentation"; type
  `documentation-page`; URL the read-repair page; access 2026-10-30; sections
  "Read repair", "Expectation of Monotonic Quorum Reads" and "Table level
  configuration of monotonic reads"; `content_sha256` `104508d5...`; status
  `read`; reviewer "Automated authoring agent". Claims supported: read repair
  makes read replicas consistent and returns the most up-to-date data;
  blocking read repair supports monotonic quorum reads; the none setting trades
  that for write atomicity. Claims not supported: linked pages, implementation
  behavior, independent reproduction. Limit: one documentation page; no cluster
  experiment.
- `read.dynamo-sosp2007.2026-10-30` — source `src.dynamo`; unit
  "Dynamo: Amazon's Highly Available Key-value Store — SOSP 2007 paper"; type
  `paper`; URL the PDF; access 2026-10-30; sections 4.4-4.7 and 4.9;
  `content_sha256` `5cacd624...`; status `read`; reviewer "Automated authoring
  agent". Claims supported: R + W > N; vector-clock causality; divergent
  versions returned and reconciled; hinted handoff and Merkle-tree
  anti-entropy; membership handoff with a confirmation round; sloppy quorum
  does not enforce strict membership. Claims not supported: current service
  internals, implementation behavior, independent reproduction. Limit: 2007
  paper; historical design; extracted text.
- `read.riak-replication-properties.2026-10-30` — source `src.riak`; unit
  "Replication Properties — Riak KV 2.2.3"; type `documentation-page`; URL the
  pinned GitHub blob; access 2026-10-30; sections "N Value and Replication",
  "Primary Reads and Writes with PR and PW", "Durable Writes with DW",
  "Symbolic Consistency Names" and "Illustrative Scenarios";
  `content_sha256` `b185c0be...`; status `read`; reviewer "Automated authoring
  agent". Claims supported: R/W quorum semantics; sloppy and strict quorum;
  read repair; vector-clock and timestamp conflict resolution. Claims not
  supported: implementation behavior, independent reproduction, clients and
  screencast. Limit: one page pinned to a commit; no Riak cluster.

### Source plan `edition/patterns/source-plan.v1.json`

Append three units to `tycho.pattern.quorum-based-reads-writes` after the
existing Cassandra Dynamo-architecture unit:

- `src.cassandra`: unit "Read repair — Apache Cassandra documentation", type
  `documentation-page`, URL the read-repair page, sections
  `["Read repair", "Expectation of Monotonic Quorum Reads",
  "Table level configuration of monotonic reads"]`, status `read`, record
  `read.cassandra-read-repair.2026-10-30`.
- `src.dynamo`: unit "Dynamo: Amazon's Highly Available Key-value Store — SOSP
  2007 paper", type `paper`, URL the PDF, sections `["4.4 Data Versioning",
  "4.5 Execution of get() and put() operations", "4.6 Handling Failures:
  Hinted Handoff", "4.7 Handling permanent failures: Replica
  synchronization", "4.8 Membership and Failure Detection",
  "4.9 Adding/Removing Storage Nodes"]`, status `read`, record
  `read.dynamo-sosp2007.2026-10-30`.
- `src.riak`: unit "Replication Properties — Riak KV 2.2.3", type
  `documentation-page`, URL the pinned GitHub blob, sections
  `["N Value and Replication", "Primary Reads and Writes with PR and PW",
  "Durable Writes with DW", "Symbolic Consistency Names",
  "Illustrative Scenarios"]`, status `read`, record
  `read.riak-replication-properties.2026-10-30`.

Replace the entry notes with: "The Dynamo architecture page supports R + W > N
and best-effort repair; the read-repair page supports monotonic quorum reads
and most-up-to-date returns; the SOSP 2007 paper supports quorum arithmetic,
vector-clock reconciliation, hinted handoff, anti-entropy and membership
handoff; Riak 2.2.3 supports sloppy/strict quorum, read repair and
timestamp/vector-clock resolution. Old/new quorum overlap and a highest-version
selector remain Tycho guidance."

Set `updated` to 2026-10-30. Summary: `required_units` 209 -> 212;
`read_units` 208 -> 211; `ledger_records` 172 -> 175. Recompute
`registry_sha256` after saving the registry (scratch value
`9a4d0de2112127bef3c2712bd51056deffa7b1e4be2f709346a3f7bcf43b6ae9`) and
refresh `route_index_snapshot` from the rebuilt route index (scratch value
`d3cff509696769ba878c2a4647df6f547f7fd4191548a67831c96b972ca7713b` after the
final owner edit).

### Registry `edition/patterns/registry.v1.json`

For `tycho.pattern.quorum-based-reads-writes`:

- Set `technical_owner.state` to `partial-bounded`.
- Set `coverage.technical` and `coverage.overall` to `partial-bounded`; keep
  `coverage.decision` at `partial-bounded`.
- Replace `source_units` with, in order: the existing Cassandra unit "Dynamo —
  multi-master replication and tunable consistency"; "Read repair — Apache
  Cassandra documentation"; "Dynamo: Amazon's Highly Available Key-value Store
  — SOSP 2007 paper"; "Replication Properties — Riak KV 2.2.3". All four have
  status `read`.
- Replace `notes` with: "Invariant and failure/recovery bound 2026-10-30 to
  Cassandra, Dynamo (SOSP 2007) and Riak 2.2.3; old/new quorum overlap and a
  highest-version selector remain Tycho guidance. Coverage partial-bounded; no
  promotion."
- Keep `review_status` `self-checked` and `atlas_owner` at V11/C06.

### Owner units `edition/patterns/owner-units.v1.json`

Entry `tycho.pattern.quorum-based-reads-writes`:

- Keep `owner.line` at 164, the heading and the four unit terms unchanged.
- Invariant:
  - `state`: `supported`.
  - `quote`: "Membership changes that move replicas can violate consistency. A
    strict system must require the old and new quorums to overlap."
  - `reason`: "Cassandra says simultaneous range movements can violate
    monotonic consistency and can even cause data loss; Dynamo transfers ranges
    only after a confirmation round but explicitly uses a sloppy quorum instead
    of strict membership; Riak offers strict quorum as an option but describes
    sloppy failover as its default mode. These sources bound the hazard and the
    availability trade-off. The requirement that old and new quorum sets
    overlap, and that a minority refuse authoritative commits, is Tycho design
    guidance, not a source claim."
  - `binding`: `src.cassandra`, record
    `read.batch3-cassandra-dynamo.2026-10-21`, section "Ring Membership and
    Failure Detection", the "This also helps to prevent simultaneous range
    movements ..." passage, revision `63929723...`.
  - Supporting bindings: Dynamo, record `read.dynamo-sosp2007.2026-10-30`,
    section "4.9 Adding/Removing Storage Nodes", the "When X is added to the
    system ..." passage, revision `5cacd624...`; Dynamo, record
    `read.dynamo-sosp2007.2026-10-30`, section "4.6 Handling Failures: Hinted
    Handoff", the "To remedy this it does not enforce strict quorum membership
    ..." passage, revision `5cacd624...`; Riak, record
    `read.riak-replication-properties.2026-10-30`, section "Primary Reads and
    Writes with PR and PW", the "Setting PR and/or PW ..." passage, revision
    `b185c0be...`.
- Failure/recovery:
  - `state`: `supported`.
  - `quote`: "Overlap is necessary but not sufficient for freshness: choose the
    application's version selector and repair replicas behind it."
  - `reason`: "Cassandra's blocking read repair makes replicas consistent and
    returns the most up-to-date data, supporting monotonic quorum reads even
    when a failed write reached only a minority; Cassandra also calls read
    repair and hinted handoff best-effort and relies on anti-entropy repair.
    Dynamo states R + W > N, returns causally unrelated versions, and writes
    back a reconciled version; Riak resolves vector-clock conflicts and
    propagates the result via read repair or active anti-entropy. The 'highest
    version wins' rule and the total order it needs are Tycho policy because
    Dynamo and Riak can expose concurrent siblings."
  - `binding`: `src.cassandra`, record
    `read.cassandra-read-repair.2026-10-30`, section "Expectation of Monotonic
    Quorum Reads", the "Cassandra uses a blocking read repair ..." passage,
    revision `104508d5...`.
  - Supporting bindings: Cassandra, record
    `read.batch3-cassandra-dynamo.2026-10-21`, section "Replica
    Synchronization", the "These techniques are only best-effort ..." passage,
    revision `63929723...`; Dynamo, record
    `read.dynamo-sosp2007.2026-10-30`, section "4.5 Execution of get() and put()
    operations", the "Setting R and W ..." passage, revision `5cacd624...`;
    Dynamo, same record and section, the "If the coordinator ends up gathering
    multiple versions ..." passage; Riak, record
    `read.riak-replication-properties.2026-10-30`, section "Illustrative
    Scenarios", the "The vector clocks are used to resolve the conflict ..."
    passage, revision `b185c0be...`; Riak, same record, section "Primary Reads
    and Writes with PR and PW", the "When the failed vnode returns to service
    ..." passage.
- Keep mechanism and alternative states, quotes and bindings unchanged.
- `source_support`: keep the existing Cassandra main record and add auxiliary
  records for `read.cassandra-read-repair.2026-10-30`, revision
  `104508d5...`; `read.dynamo-sosp2007.2026-10-30`, revision `5cacd624...`;
  `read.riak-replication-properties.2026-10-30`, revision `b185c0be...`.
- Set `technical_coverage` to `partial-bounded`; set `notes` to the registry
  notes above.
- Shared page (`quorum-envelope.md`): `bounded_entries` 0 -> 1. The second
  unit on this page, `tycho.pattern.quorum-coordination`, moves from
  `owner.line` 179 to 231 because this lane inserts 52 lines above it. Keep its
  heading, terms and evidence unchanged.
- Summary counters: `invariant_supported` 70 -> 71;
  `failure_recovery_supported` 63 -> 64; `technical_partial_bounded` 19 -> 20;
  `technical_partial` 78 -> 77. No other counter changes.

### Card registration `edition/patterns/card-batches.v1.json`

Add `card_path`:
`book/volumes/v11-pattern-atlas/c06-database-storage/README.md` to the
`tycho.pattern.quorum-based-reads-writes` entry. This is the same file as the
chapter, not a split. Without it, `preflight_sufficient.py` reports
`card_path missing or absent`. Keep `ledger_record`
`read.batch3-cassandra-dynamo.2026-10-21`.

### Content revisions `edition/content-revisions.json`

Add one issue-540 revision with `authorized_at` 2026-10-30 and authorization
"B35 quorum-based-reads-writes invariant and failure/recovery source binding;
no promotion or owner acceptance." The historical-view hashes are:

- Owner path, previous (migration baseline):
  `6bfc8f0b5a385142dd0085c017eb40afa08c3a09f2ee5659b56ad84762e5ad25`;
  current: `ed1de747f1723ca9d28e88acf8739d769f6d737b677d2a9bd1d38fb0d92c5cc6`.
- Card path, previous (migration baseline):
  `81235b0c96b51df43c2190ae76b271ad7b2cb01141751145f275f84e6021a826`;
  current: `ec5e84c413d2b505a341964faae59d4f70f7df02e322e7b2fcf4fd03424e73a1`.

Leave `source_blocks`, `enrichment_documents`, `enrichment_additions` and
`enrichment_baselines` empty. The owner page is retained and no split is
performed. These are historical-view hashes, not the raw file hashes in the
Book edits section.

### Derived artifacts

The book edit changes one canonical page and one atlas chapter. The source
register gains one record, so regenerate `sources/CATALOG.md` (scratch count
294). The registry, card, source-plan and owner-unit changes make the route
index, atlas registry hash, edition inventory and the coverage, census and
reverse-map artifacts stale. Refresh them once at batch end; do not treat a
stale derived hash as a lane content failure. Scratch values after the full
patch and final owner edit: registry SHA-256
`9a4d0de2112127bef3c2712bd51056deffa7b1e4be2f709346a3f7bcf43b6ae9`; route
snapshot `d3cff509696769ba878c2a4647df6f547f7fd4191548a67831c96b972ca7713b`;
edition content snapshot
`07064435a092934964b3e389e1fecb48c1e19440531b9b02447f8838d0e45cfc`;
544 inventory files.

The atlas manifest must also record the new C06 chapter SHA-256
`9ae99b3f5a4312cf8e11327a40070bc74f03ed48ca6a1ed35e23c6f41dd782c4` and the
new registry SHA-256. The coverage map and reverse map must record the new
registry hash and route snapshot. The 2026-10-27 external review recorded in
`edition/patterns/sufficient-candidates.v1.json` predates this edit and no
longer covers the changed owner page or card bytes. The book/atlas independent
review gate applies; do not update the recorded hash without a fresh review.
The prior review is historical evidence, not acceptance of this lane.

## Validation

Checker output in the lane worktree after the two book edits, before the
metadata patch:

    PASS: V11 prose <=100; 145 exact owner-link exceptions
    PASS: configured lexical boundary checks; independent-origin review still
    required.

Targeted validator results with the book edits only, in the lane worktree:

- `python3 scripts/check_markdown_line_length.py` — PASS.
- `python3 scripts/check_boundary.py` — PASS.
- `python3 scripts/validate_pattern_owner_units.py` — expected FAIL on the
  unchanged metadata (old invariant/failure quotes and line number).
- `python3 scripts/preflight_sufficient.py --pattern
  tycho.pattern.quorum-based-reads-writes` — expected FAIL on invariant,
  failure/recovery and `card_path`.

In the detached scratch copy with the metadata patch, the three new ledger
records, the regenerated source catalogue and the derived-artifact refresh:

    PASS: V11 prose <=100; 145 exact owner-link exceptions
    PASS: configured lexical boundary checks; independent-origin review still required.
    PASS: tycho.pattern.quorum-based-reads-writes
    1/1 entries preflight clean
    PASS: owner units 145 entries, 145 units, 30 shared pages
    PASS: pattern registry 145 entries, 11 families
    PASS: pattern cards 11 batch(es), 145 entries
    PASS: source plan 145 entries; 211 read; 175 ledger records
    PASS: 294 source records, mandatory IDs, cross-references and catalogue freshness
    PASS: 488 documents, structural metadata and registry references
    PASS: coverage 145 entries, 89 reverse documents
    PASS: atlas V11 11 chapters, 65 documents, 145 patterns
    PASS: 488 canonical documents; 544 inventory files
    PASS: directory migration; 488 canonical documents, 339 moved documents
    PASS: decomposition; 739 preserved source blocks, 174 new question pages
    PASS: enrichment; explicit membership and byte conservation

The scratch tree was not used to claim review, promotion or owner acceptance.
The full unit suite is not run; batch-end tests remain with the integrator.

## Limits

The binding uses two Apache Cassandra documentation pages, one 2007 SOSP paper
and one Riak KV 2.2.3 documentation page. Cassandra's pages are the current
prerelease documentation line, pinned here by digest rather than a release tag;
the Dynamo paper is a historical design; Riak's page is pinned to a commit in
an archived documentation repository. None of the selected sources states an
old/new quorum-overlap protocol, and none tests a highest-version selector, a
membership change, or a partition in a running system. The overlap rule, the
minority-refusal rule and the application-defined highest-version order are
Tycho guidance. The `invariant` and `failure_recovery` states are `supported`
only because the page separates those Tycho additions from the source-supported
hazard, repair and trade-off claims; a reviewer that requires every word of the
owner quote to be source-quoted should treat the invariant dimension as partial
instead.

No independent AI review, owner acceptance, promotion or production
observation is claimed. The card is inline in V11/C06, not V11/C04; this lane
did not create a second card.

## Commit scope

The lane commit contains this note and the two book files only:

- the owner path listed under Lane coordinates;
- the card path `book/volumes/v11-pattern-atlas/c06-database-storage/README.md`.

No shared JSON, promotion, test or generated file is in the lane commit.
