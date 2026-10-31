# B47 — Consistent Hashing four-dimension lane

Status: lane-local book edit, self-checked on 2026-10-31. No shared edition
metadata, promotion, generated artifact or owner acceptance is included. The
entry was 0/4 at the parent HEAD: zero dimensions supported and all four
`partial`. This lane binds all four dimensions to public sources and labels
the 1/N invariant, hotspot runbook, ownership-epoch rule and range/rendezvous
comparison as Tycho. The card remains inline in V11/C06.

## Lane coordinates

- Parent HEAD: `90896137789f57fe42cf74d03e9d4ad64688a814` (`90896137`).
- Branch: `b47-consistent-hashing`; worktree:
  `/Users/rbaranov/Projects/tycho-worktrees/b47-consistent-hashing`.
- Scope: the owner section `### Consistent Hashing` in the V05/C05 page and
  the inline V11/C06 card `### Consistent Hashing`. Single-entry lane; no
  other entry, shared JSON, promotion or generated file is changed.
- Owner path (concatenate):

      book/volumes/v05-data-models-engines-and-lifecycle/
      c05-partitioning-sharding-and-rebalancing/resharding-transition.md

- Card path:
  `book/volumes/v11-pattern-atlas/c06-database-storage/README.md`.
- Exactly three files change: the owner page, the inline card and this note.
  No shared JSON file is edited.

## Baseline and gap

The owner-unit entry for `tycho.pattern.consistent-hashing` records all four
states as `partial`; `technical_coverage` is `partial` and
`decision_coverage` is `partial-bounded`. The recorded reasons are:

- mechanism: "Local Cassandra Architecture Overview has no consistent-hashing
  ring or key-movement text."
- invariant: "Local text has no versioned mapping or authoritative owner per
  key."
- failure/recovery: "Local text has no ring-change, wrong-owner or dual-read
  transition."
- alternative: "Local text does not compare consistent hashing with explicit
  key ranges."

Finding B4-015 added that the card required virtual nodes and replication
while the owner text called virtual nodes optional and did not discuss
hotspots. At this HEAD the card cited only the Cassandra overview record,
whose own `claims_not_supported` list includes "consistent hashing or a token
ring." The gap is therefore evidential, not only editorial.

Existing records and their limits:

- `read.batch3-cassandra-arch.2026-10-21` covers the Cassandra overview and
  explicitly excludes consistent hashing, the token ring and replication
  factor. It remains a scope limit, not support.
- `read.dynamo-sosp2007.2026-10-30` covers sections 4.4-4.9. It overlaps
  4.6 and 4.9 but not 4.2 or 4.3, where the ring and virtual nodes are
  described.
- `read.riak-replication-properties.2026-10-30` covers quorum and repair
  properties, not the ring, vnodes or membership transfer.
- No Karger source or record exists in the register or ledger.

This lane therefore proposes one new source identity and six new bounded read
records. It does not apply them to shared metadata.

## Candidate evaluation

- Karger, Lehman, Leighton, Panigrahy, Levine and Lewin, "Consistent Hashing
  and Random Trees: Distributed Caching Protocols for Relieving Hot Spots on
  the World Wide Web" (selected). It is the origin paper for the term and
  supplies the hot-spot purpose, the shared-space construction, the
  multiple-points-per-bucket device and the 1/N movement argument.
- DeCandia et al., "Dynamo: Amazon's Highly Available Key-value Store"
  (selected). It states the ring, virtual nodes, immediate-neighbour movement,
  node-loss load dispersal, hinted handoff and anti-entropy repair.
- Apache Cassandra 5.0, "Dynamo" (selected). It supplies the explicit
  modulo-versus-consistent-hashing contrast, the token ring, vnode trade-offs,
  uneven-token hotspot risk, outage risk and repair cost.
- Riak KV 2.2.3, "Vnodes", "Clusters" and "Adding / Removing Nodes" (selected).
  They supply the 160-bit ring, vnode partitions, the 1/(number of nodes)
  ownership statement, crash removal and non-deterministic ring changes.
- The existing Cassandra overview, Dynamo paper and Riak replication records
  are retained as narrower records and are not stretched to cover these
  claims.
- Rendezvous hashing was not fetched as a separate public unit. The note names
  it only as a Tycho-labelled alternative, not as source support.

## Source binding

Quotes reproduce the served or pinned prose. Line breaks inside a quote are
editorial wrapping. Karger PDF line-end hyphenation is joined; Cassandra
extraction spaces before punctuation are normalized; Riak Markdown emphasis
and link markup are removed. Every quote was checked as a whitespace-normalized
substring of the named representation on 2026-10-31. Tycho-labelled sentences
are not presented as source quotes.

### Karger et al. — Consistent Hashing and Random Trees (1997)

- Source id: `src.karger` (proposed; not in the register).
- Proposed record: `read.karger-consistent-hashing.2026-10-31`.
- Bibliographic revision: STOC '97, pages 654-663, ACM Press, 1997,
  DOI `10.1145/258533.258660`; Crossref confirms the title, six authors,
  page range and 1997 publication.
- Representation: public PDF at
  `https://www.cs.princeton.edu/courses/archive/fall09/cos521/Handouts/consistenthashing.pdf`;
  HTTP 200, 1,729,694 bytes, 10 pages, HTTP Date 2026-10-31T11:45:42Z,
  Last-Modified 2009-11-16T20:21:18Z, ETag `"1a649e-47882c0870b80"`;
  PDF creation 1997-06-17 18:41:52 CEST, modification 1997-08-10 02:32:52
  CEST; PDF SHA-256
  `0ccf4b8b1b4a1d4b7e5a411c98d1a1c890e863f71cccdddaf9cdc272015262d2`.
  Extracted with `pdftotext -raw`: 1,163 lines, 11,838 words, text SHA-256
  `cdaf06a423a62b790cea18bc0adc50fbc71a4c17682f7e08b098c13c0d8fe6c4`.
- Sections used: Abstract, "1 Introduction", "4.1 Definitions",
  "4.2 Construction".
- Exact quotes:

      Consistent Hashing and Random Trees: Distributed Caching Protocols for
      Relieving Hot Spots on the World Wide Web

      Our caching protocols are based on a special kind of hashing that we
      call consistent hashing.

      Our protocols are particularly designed for use with very large networks
      such as the Internet, where delays caused by hot spots can be severe,
      and where it is not feasible for every server to have complete
      information about the current state of the entire network.

      When a machine is added to or removed from the set of caches, the
      expected fraction of objects that must be moved to a new cache is the
      minimum needed to maintain a balanced load across the caches.

      When a new bucket is added, the only items that move are those that are
      now closest to one of the new bucket's associated points. No items move
      between old buckets.

      Since there are many ways to formalize the notion of consistency as
      described above, we will not commit to a precise definition.

- Limits: the public PDF is an author copy with OCR text, not the ACM
  typesetting; the text has OCR ligature and line-break artifacts. The paper
  does not describe modern vnodes, rendezvous hashing or range partitioning.
  No theorem proof was re-run, and no production measurement is claimed.

### Dynamo — SOSP 2007 paper

- Source id: `src.dynamo` (existing, admitted).
- Proposed record: `read.dynamo-consistent-hashing.2026-10-31`.
- Representation: public PDF at
  `https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf`;
  HTTP 200, 900,468 bytes, 16 pages, PDF creation 2007-08-15, modification
  2007-09-26; served Date 2026-10-30T14:18:58Z, Last-Modified
  2026-08-26T16:00:16Z, ETag `"d9383e34b6e8292796bfe54b0aeeb93c"`;
  PDF SHA-256
  `5cacd624cd7bfd37e3d22e04d8c2e347a49579d2927dbb06f40a89c0bcd40bd4`.
  Re-fetched on 2026-10-31 and byte-identical to the retained record.
  Extracted with `pdftotext -raw`: 1,663 lines, 14,930 words, text SHA-256
  `2da247073d091ba83236b71dd9c5c56a19516f9f7b2e29258a0e3b5c4d4fb140`.
- Sections used: "4.2 Partitioning Algorithm", "4.3 Replication",
  "4.6 Handling Failures: Hinted Handoff",
  "4.7 Handling permanent failures: Replica synchronization",
  "4.9 Adding/Removing Storage Nodes".
- Exact quotes:

      Dynamo's partitioning scheme relies on consistent hashing to distribute
      the load across multiple storage hosts.

      In consistent hashing [10], the output range of a hash function is
      treated as a fixed circular space or "ring" (i.e. the largest hash value
      wraps around to the smallest hash value).

      The principle advantage of consistent hashing is that departure or
      arrival of a node only affects its immediate neighbors and other nodes
      remain unaffected.

      If a node becomes unavailable (due to failures or routine maintenance),
      the load handled by this node is evenly dispersed across the remaining
      available nodes.

      In this example, if node A is temporarily down or unreachable during a
      write operation then a replica that would normally have lived on A will
      now be sent to node D.

      To handle this and other threats to durability, Dynamo implements an
      anti-entropy (replica synchronization) protocol to keep the replicas
      synchronized.

      When a new node (say X) is added into the system, it gets assigned a
      number of tokens that are randomly scattered on the ring.

- Limits: 2007 design paper; historical and not a current service contract.
  The paper chooses a sloppy quorum, so its failure handling is not a strict
  quorum-overlap rule. No deployment or benchmark is claimed.

### Apache Cassandra 5.0 — Dynamo

- Source id: `src.cassandra` (existing, admitted).
- Proposed record: `read.cassandra-dynamo-consistent-hashing.2026-10-31`.
- Representation: public page at
  `https://cassandra.apache.org/doc/latest/cassandra/architecture/dynamo.html`;
  documentation version selector current value `5.0` (the selector also lists
  `5.0.9` and `6.0-alpha2`); HTTP 200, 76,252 bytes, HTTP Date
  2026-10-31T11:45:44Z, Last-Modified 2026-08-26T07:20:02Z, ETag
  `"129dc-659ee0c3b6c6d"`; raw HTML SHA-256
  `6392972302ba65e62eab354d4b754003847ce869a464979ba894f4daf0514a65`.
  Article-region text: 25,291 characters, 3,967 words, SHA-256
  `b613129d96ffae22bf20f43807093b18973b75d5e1b79c1b43aa2ffad4b45f39`.
- Sections used: "Dataset Partitioning: Consistent Hashing", "Consistent
  Hashing using a Token Ring", "Multiple Tokens per Physical Node (vnodes)",
  and the token-aware load statement in the same section.
- Exact quotes:

      In naive data hashing, you typically allocate keys to buckets by taking
      a hash of the key modulo the number of buckets.

      In this naive scheme, however, adding a single node might invalidate
      almost all of the mappings.

      Cassandra instead maps every node to one or more tokens on a continuous
      hash ring, and defines ownership by hashing a key onto the ring and then
      "walking" the ring in one direction, similar to the Chord algorithm.

      The main difference of consistent hashing to naive data hashing is that
      when the number of nodes (buckets) to hash into changes, consistent
      hashing only has to move a small fraction of the keys.

      For example, in the previous example there is no way to add a ninth
      token without causing imbalance; instead we would have to insert 8
      tokens in the midpoints of the existing ranges.

      Cassandra seeks to avoid token imbalance because uneven token ranges
      lead to uneven request load.

      If a node becomes unavailable, query load (especially token-aware query
      load), is evenly distributed across many other nodes.

      Every token introduces up to 2 * (RF - 1) additional neighbors on the
      token ring, which means that there are more combinations of node
      failures where we lose availability for a portion of the token ring. The
      more tokens you have, the higher the probability of an outage.

      Cluster-wide maintenance operations are often slowed. For example, as
      the number of tokens per node is increased, the number of discrete
      repair operations the cluster must do also increases.

- Limits: living documentation on the 5.0 branch, not a release tag or an
  executed cluster test. The page describes Cassandra's implementation, not a
  universal ring contract. The article-text digest covers the `article.doc`
  region, excluding navigation and scripts.

### Riak KV 2.2.3 — Vnodes, Clusters, Adding / Removing Nodes

- Source id: `src.riak` (existing, admitted).
- Proposed records: `read.riak-vnodes.2026-10-31`,
  `read.riak-clusters.2026-10-31`,
  `read.riak-adding-removing-nodes.2026-10-31`.
- Representation: pinned Markdown in `basho/basho_docs` at commit
  `6409dd9c93b08f0a6e959a1874b5568c88172f3a` (master commit date
  2022-12-12), docs version 2.2.3. The live pages returned HTTP 200 on
  2026-10-31, but the binding revision is the pinned commit.
- Unit facts:
  - `content/riak/kv/2.2.3/learn/concepts/vnodes.md`: 7,064 bytes,
    157 lines, 962 words, SHA-256
    `3fe623f7bbe206b9b289894607b0ff08748414a65060c6229a274ef7d986c204`.
  - `content/riak/kv/2.2.3/learn/concepts/clusters.md`: 5,006 bytes,
    114 lines, 730 words, SHA-256
    `ea246f176b17e21a6225d4fb9f5ba7a60fe90958ed07ef5da07efff05afbdfc5`.
  - `content/riak/kv/2.2.3/using/cluster-operations/adding-removing-nodes.md`:
    7,027 bytes, 195 lines, 943 words, SHA-256
    `67d14c75a3edb078f0d49591eea02d0b60cd5d7b4ebbfd49e632ec60705fe23f`.
- Sections used: "Vnodes"; "The Number of Vnodes in a Cluster"; "The Role of
  Vnodes"; "Vnodes and Replication Properties"; "The Ring"; "Intelligent
  Replication"; "Gossiping"; "Add a Node to an Existing Cluster"; "Joining
  Nodes to Form a Cluster"; "Note on ring changes"; "Removing a Node From a
  Cluster".
- Exact quotes:

      Virtual nodes, more commonly referred to as vnodes, are processes that
      manage partitions in the Riak ring. Each data partition in a Riak
      cluster has a vnode that claims that partition.

      Internally, Riak computes a 160-bit binary hash of each bucket/key pair
      and maps this value to a position on an ordered ring of all such values.
      This ring is divided into partitions, with each Riak vnode responsible
      for one of these partitions (we say that each vnode claims that
      partition).

      The nodes of a Riak cluster each attempt to run a roughly equal number
      of vnodes at any given time. In the general case, this means that each
      node in the cluster is responsible for 1/(number of nodes) of the ring,
      or (number of partitions)/(number of nodes) vnodes.

      The second is relevant for failure scenarios in which a node has crashed
      and is irrecoverable and thus must be removed from the cluster from
      another node.

      The algorithm that distributes partitions across the cluster during
      membership changes is non-deterministic. As a result, there is no
      optimal ring.

- Limits: pinned 2022 documentation for Riak KV 2.2.3. The page states the
  general case and an example distribution; it does not guarantee an exact
  moved fraction. No Riak cluster was run.

## Proposed metadata (not applied)

### Source register

Add one source; the count would move from 305 to 306.

- `src.karger` — title "Consistent Hashing and Random Trees: Distributed
  Caching Protocols for Relieving Hot Spots on the World Wide Web";
  category `foundations`; publisher ACM; kind `paper`; canonical URL
  `https://doi.org/10.1145/258533.258660`; resolved URL the Princeton PDF
  above; topics `distributed-systems`, `hashing`, `caching`,
  `load-balancing`; priority `core`; planned use "Origin, ring mechanism,
  smoothness and classical-hash contrast for the Consistent Hashing entry.";
  admission `admitted-for-research`; access
  `public-web-or-author-download`; reading status
  `full-public-page-inspected`; version records the 2026-10-31 access, the
  10-page author-copy PDF, PDF SHA-256 `0ccf4b8b...`, extracted-text
  SHA-256 `cdaf06a4...`, HTTP Date, Last-Modified and ETag above;
  `access_checked` and `content_verified` 2026-10-31; license note
  "Public conference paper copy; cite short excerpts and paraphrase; do not
  mirror. ACM copyright; public access is not a redistribution license.";
  verification scope names Abstract, Section 1, 4.1 and 4.2 and excludes
  linked references, proof details and implementation; observed title is the
  paper title.

### Reading ledger

Add six records; the count would move from 218 to 224.

- `read.karger-consistent-hashing.2026-10-31` — source `src.karger`;
  paper; sections Abstract, 1, 4.1, 4.2; content SHA-256 the PDF digest;
  claims: shared-space construction, multiple bucket points, smoothness,
  new-bucket-only movement, hot-spot motivation; excludes vnodes, rendezvous,
  range partitioning, proofs and deployment.
- `read.dynamo-consistent-hashing.2026-10-31` — source `src.dynamo`;
  paper; sections 4.2, 4.3, 4.6, 4.7, 4.9; content SHA-256 the PDF digest;
  claims: ring, virtual nodes, immediate-neighbour movement, node-loss load
  dispersal, hinted handoff, anti-entropy, token assignment; excludes current
  service internals and deployment.
- `read.cassandra-dynamo-consistent-hashing.2026-10-31` — source
  `src.cassandra`; documentation-page; sections "Dataset Partitioning:
  Consistent Hashing", "Consistent Hashing using a Token Ring", "Multiple
  Tokens per Physical Node (vnodes)"; content SHA-256 the raw HTML digest;
  claims: modulo contrast, token ring, vnode benefits and costs, uneven-load
  and outage warnings, node-unavailable load distribution; excludes linked
  pages and cluster behavior.
- `read.riak-vnodes.2026-10-31` — source `src.riak`; documentation-page;
  sections "Vnodes", "The Number of Vnodes in a Cluster", "The Role of
  Vnodes", "Vnodes and Replication Properties"; content SHA-256
  `3fe623f7...`; claims: vnode partition ownership, 160-bit ring, partition
  count.
- `read.riak-clusters.2026-10-31` — source `src.riak`; documentation-page;
  sections "The Ring", "Intelligent Replication", "Gossiping"; content
  SHA-256 `ea246f17...`; claims: 1/(number of nodes) ownership, ring gossip,
  replica placement.
- `read.riak-adding-removing-nodes.2026-10-31` — source `src.riak`;
  documentation-page; sections "Add a Node to an Existing Cluster",
  "Joining Nodes to Form a Cluster", "Note on ring changes", "Removing a Node
  From a Cluster"; content SHA-256 `67d14c75...`; claims: staged join,
  partition transfers, non-deterministic ring, crash removal.

### Owner units

Proposed state for `tycho.pattern.consistent-hashing`: all four dimensions
`supported`; `technical_coverage` `partial-bounded`;
`decision_coverage` `partial-bounded`; notes record this lane and its
source boundary.

- mechanism: quote "A consistent hash function maps keys and nodes into one
  circular space; each physical node claims many token positions, and a key
  belongs to the first node clockwise." Reason: Karger 1997 4.1-4.2, Dynamo
  4.2-4.3, Cassandra 5.0 token-ring/vnode sections, Riak 2.2.3 Vnodes and
  Clusters.
- invariant: quote "With K keys over N equal-share nodes, a single join or
  leave should move about K/N keys, not the whole keyspace; balance makes this
  an expectation, not a guarantee." Reason: Karger 1997 smoothness and
  new-bucket paragraphs; Dynamo 4.2; Cassandra 5.0 token-ring section; Riak
  2.2.3 Clusters.
- failure_recovery: quote "Hotspots, uneven token ranges and node loss require
  redistributing the affected ranges, hinted handoff and anti-entropy repair,
  and an ownership epoch verified after the change." Reason: Karger 1997
  hot-spot motivation; Dynamo 4.6-4.7 and 4.9; Cassandra 5.0 vnode benefits
  and outage costs; Riak 2.2.3 Vnodes and Adding/Removing Nodes.
- alternative: quote "Modulo remaps almost everything when N changes; explicit
  ranges preserve operator control, and rendezvous hashing needs no shared
  ring; choose by churn, locality and ring-operational cost." Reason:
  Cassandra 5.0 naive-modulo contrast and Karger 1997 classical-hash
  discussion; the range and rendezvous comparison is Tycho synthesis, not
  source-bound.

Counter deltas if the four states move from `partial` to `supported`:
mechanism 113 -> 114, invariant 78 -> 79, failure/recovery 72 -> 73,
alternative 77 -> 78; technical partial 70 -> 69 and partial-bounded 16 -> 17;
sufficient stays 59; decision coverage stays partial-bounded 86 and sufficient
59. These counts are derived from the current `owner-units.v1.json`; this
lane did not apply them.

### Source plan and registry

The integrator must add the new source and the six records, bind every record
to a read unit, and recompute the source-plan required/read/ledger counters
and registry source count. This lane does not claim those numbers.

## Validation

- `python3 scripts/check_markdown_line_length.py`: PASS; 145 exact
  owner-link exceptions.
- Owner page: every newly written line in the section is <=100 characters;
  pre-existing frontmatter, Mermaid and table lines are unchanged. Card: only
  the existing `**Technical owner.**` exception exceeds 100. This note:
  every line is <=100.
- `python3 scripts/check_boundary.py`: PASS; independent-origin review still
  required.
- Links in the owner and card are unchanged; the card anchor remains
  `#consistent-hashing`.
- `git diff --stat` after the edits: two modified files and this new note.
- Raw SHA-256 after the book edits:
  - owner page:
    `9d4f2d1c910e47106851a56b5e0fdc8e2970838430b3df8c9867961d07198cac`
  - card:
    `58aefadc717e0219e21ae64d6b55767c59e2f3dc06a7fa3769bb30fedc93eb4f`

## Limits

- Shared metadata is not updated. The generated owner units, registry, source
  plan, ledger, card batches and indexes still show the entry as 0/4 or
  partial until an integrator applies the proposals above.
- No promotion, owner acceptance, coverage sufficiency or independent AI
  review is claimed. The book/atlas review gate remains outstanding.
- No benchmark, production observation, cluster experiment or runtime
  measurement is claimed.
- The Karger representation is an OCR author copy; its formal theorem is not
  reproduced or re-proved.
- The Cassandra page is living 5.0-branch documentation, not a tagged release.
- The range and rendezvous comparison is Tycho synthesis and has no quoted
  source in this lane.
