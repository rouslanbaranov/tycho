# B42 — Causal ordering failure/recovery and alternative lane

Status: lane-local book edit, self-checked on 2026-10-30. No shared edition
metadata, promotion, generated artifact or owner acceptance is included. The
entry was 2/4 at the parent HEAD: mechanism and invariant were supported;
failure/recovery and alternative were partial. This lane binds both partial
dimensions to the public Lamport 1978 paper, Mattern's vector-time paper, the
Apache Kafka 4.1 Introduction and Design pages, and the retained Jepsen causal
page. The card remains inline in V11/C08; the task described it as V11/C04,
but the repository has no causal card in C04 and the registered atlas section
is C08.

## Lane coordinates

- Parent HEAD: `3cebce623e6efe3a3fd4b166372172d28edf3c1d` (`3cebce62`).
- Branch: `b42-causal`; worktree:
  `/Users/rbaranov/Projects/tycho-worktrees/b42-causal`.
- Scope: the owner section `### Causal Ordering` in V04/C01 and the inline
  V11/C08 card `### Causal Ordering`. Single-entry lane; no other entry,
  shared JSON, promotion or generated file is changed.
- Owner path (concatenate):

      book/volumes/v04-distributed-coordination-and-events/
      c01-time-causality-and-ordering/causal-order.md

- Card path:
  `book/volumes/v11-pattern-atlas/c08-coordination/README.md`.
- Existing source id: `src.jepsen-consistency` (record
  `read.batch4-causal.2026-10-21`; the 2026-10-30 refetch is byte-identical
  at `3dbd842b...`).
- Existing source ids newly bound for this entry: `src.lamport-time`,
  `src.kafka` and `src.kafka-design`.
- Proposed new source id: `src.mattern-vector-time`.
- Baseline line-length and boundary checks pass before and after the edit.

## Candidate evaluation

- Lamport, *Time, Clocks, and the Ordering of Events in a Distributed
  System* (selected). The author-hosted PDF gives the partial-order
  definition, the three generating rules, the clock condition, the explicit
  note that messages may be received out of order, and the non-uniqueness of
  the total-order extension. These are the failure/recovery and alternative
  claims the earlier abstract-only record could not support.
- Mattern, *Virtual Time and Global States of Distributed Systems* (selected).
  The author-hosted paper defines vector clocks, gives each process a vector
  of length equal to the process count, piggybacks that vector on messages,
  distinguishes causally independent events, and explicitly covers delivery
  where messages may be received out of order.
- Apache Kafka 4.1, *Introduction* (selected). The "Main Concepts and
  Terminology" section binds same-key routing and per-partition read order.
- Apache Kafka 4.1, *Design* (selected). "Replicated Logs" binds the
  replicated log as a consensus-on-order mechanism and the leader as the
  order chooser; "Replication" binds the network-partition availability
  limit; "Consumer Position" binds totally ordered partitions.
- Jepsen, *Causal Consistency* (retained). The existing record already
  supports sticky availability, convergence, and the sequential-consistency
  recommendation under total order. Additional exact passages are bound under
  the same revision; no new Jepsen ledger record is required.
- Dynamo is not used in this lane. Its vector-clock discussion addresses
  replica version reconciliation, not the ordering-decision claim, and adding
  it would widen the entry without a new failure path.

## Source binding

Quotes reproduce the served prose. Line breaks inside a quote are editorial
wrapping; a hyphenated line break in the extracted PDF is joined. The binding
revision is the SHA-256 of the raw served bytes. PDF text was extracted with
`pdftotext -raw`; `-layout` interleaves the two columns of the Lamport and
Mattern papers and is not suitable for substring checks.

### Lamport — Time, Clocks, and the Ordering of Events in a Distributed System

- Source id: `src.lamport-time` (existing).
- New record: `read.lamport-time.2026-10-30`.
- URL: `https://lamport.azurewebsites.net/pubs/time-clocks.pdf`.
- Unit label: "Time, Clocks, and the Ordering of Events in a Distributed
  System — Leslie Lamport (CACM 1978)"; unit type `paper`; access date
  2026-10-30.
- Representation: HTTP 200, 854,562 bytes, 8 pages, PDF 1.3, CACM 21(7),
  July 1978, first page 558. HTTP Date 2026-10-30T22:37:41Z; Last-Modified
  2026-09-15T03:24:34Z; ETag `"0858abac144dd1:0"`; raw PDF SHA-256
  `c55e7cab4230aa3d7126748a149b2db6f0d7a67296d5eccfdd50a210299a96b2`.
  Extracted text with `pdftotext -raw`: 862 lines, 7,374 words, SHA-256
  `afec82afda75e089a3e3e34b1a9db2136f9aadb5e07c7a8fefc4bd7aa1ebb737`.
- Sections used: Abstract; Introduction; The Partial Ordering; Logical
  Clocks; Ordering the Events Totally.
- Exact quotes:

      The concept of one event happening before another in a distributed system is
      examined, and is shown to define a partial ordering of the events.

      The relation "happened before" is therefore only a partial ordering of the
      events in the system.

      Two events are concurrent if neither can causally affect the other.

      Observe that messages may be received out of order.

      Note that we cannot expect the converse condition to hold as well, since that
      would imply that any two concurrent events must occur at the same time.

      We can use a system of clocks satisfying the Clock Condition to place a total
      ordering on the set of all system events.

      Different choices of clocks which satisfy the Clock Condition yield different
      relations

      It is only the partial ordering which is uniquely determined by the system of
      events.

- Limits: the paper defines a logical construction, not a production system.
  It does not measure coordination cost, prove a particular implementation, or
  require consensus. The total-order construction is one logical-clock
  construction, not a general theory of consensus.

### Mattern — Virtual Time and Global States of Distributed Systems

- Source id: `src.mattern-vector-time` (proposed).
- Proposed record: `read.mattern-vector-time.2026-10-30`.
- URL:
  `https://vs.inf.ethz.ch/publ/papers/VirtTimeGlobStates.pdf` (the
  `www.vs.inf.ethz.ch` URL returns a 301 to this final URL).
- Unit label: "Virtual Time and Global States of Distributed Systems —
  Friedemann Mattern (author-hosted paper)"; unit type `paper`; access date
  2026-10-30.
- Representation: HTTP 200, 1,255,805 bytes, 15 pages, PDF 1.3. HTTP Date
  2026-10-30T22:37:42Z; Last-Modified 2006-03-07T22:00:42Z; ETag
  `"13297d-40e6ec63e3680"`; raw PDF SHA-256
  `9dea637ae03a9ec2cdeae442a2c99739d6437bf2941b2b024590d4d684078fd7`.
  Extracted text with `pdftotext -raw`: 1,304 lines, 7,441 words, SHA-256
  `6543ac600e97adab8c585a0d37e24925607ca6ccf87bf162383542f478a6433f`.
  The first page identifies an edited version of a paper in the Proceedings
  of the International Workshop on Parallel and Distributed Algorithms
  (Chateau de Bonas, France, October 1988), copyright 1989 Elsevier, used
  with the author's permission.
- Sections used: Abstract; 1 Introduction; 5 The concept of time; 6 Virtual
  time; 7 Vector time; 8 The structure of vector time.
- Exact quotes:

      We argue that a linearly ordered structure of time is not (always) adequate
      for distributed systems and propose a generalized non-standard model of time
      which consists of vectors of clocks. These clock-vectors are partially ordered
      and form a lattice.

      Finally, we present a new algorithm to compute a consistent global snapshot of
      a distributed system where messages may be received out of order.

      For that, we equip each process Pi with a clock Ci consisting of a vector of
      length n, where n is the total number of processes.

      each message gets a piggybacked timestamp consisting of the vector of the
      local clock.

      Causally independent events may happen in any order.

- Limits: the paper constructs vector time and global snapshots; it does not
  measure per-message metadata overhead, prescribe a production merge policy,
  or test a broker. The per-replica cost characterization is Tycho's, not a
  source measurement.

### Kafka — Introduction (4.1 documentation)

- Source id: `src.kafka` (existing).
- New record: `read.kafka-introduction.2026-10-30`.
- URL: `https://kafka.apache.org/41/getting-started/introduction/`.
- Unit label: "Introduction — Apache Kafka 4.1 documentation"; unit type
  `documentation-page`; access date 2026-10-30.
- Representation: HTTP 200, 72,330 bytes. HTTP Date
  2026-10-30T22:37:40Z; Last-Modified 2026-10-28T19:19:52Z; ETag
  `"11a8a-65eeb729212bd"`; raw HTML SHA-256
  `f288579b9ed405c44df2f31e9245794902ff6f99f1369290c17dce1ddde2333f`.
- Sections used: Introduction; Main Concepts and Terminology.
- Exact quote:

      Events with the same event key (e.g., a customer or vehicle ID) are written to
      the same partition, and Kafka guarantees that any consumer of a given
      topic-partition will always read that partition’s events in exactly the same
      order as they were written.

- Limits: one public documentation page; it states same-key routing and
  per-partition order, not a topic-wide order. The cross-partition reading is
  Tycho's.

### Kafka — Design (4.1 documentation)

- Source id: `src.kafka-design` (existing).
- New record: `read.kafka-design.2026-10-30`.
- URL: `https://kafka.apache.org/41/design/design/`.
- Unit label: "Design — Apache Kafka 4.1 documentation"; unit type
  `documentation-page`; access date 2026-10-30.
- Representation: HTTP 200, 143,123 bytes. HTTP Date
  2026-10-30T22:37:40Z; Last-Modified 2026-10-28T19:19:52Z; ETag
  `"22f13-65eeb7291ff35"`; raw HTML SHA-256
  `d01981797402d75cada10599d586b753d02f8a9deb08d658a0e07758dedadfb7`.
- Sections used: Design; Replication; Replicated Logs: Quorums, ISRs, and
  State Machines (Oh my!); Consumer Position.
- Exact quotes:

      Our topic is divided into a set of totally ordered partitions, each of which
      is consumed by exactly one consumer within each subscribing consumer group at
      any given time.

      A replicated log models the process of coming into consensus on the order of
      a series of values (generally numbering the log entries 0, 1, 2, …).

      There are many ways to implement this, but the simplest and fastest is with a
      leader who chooses the ordering of values provided to it.

      Kafka will remain available in the presence of node failures after a short
      fail-over period, but may not remain available in the presence of network
      partitions.

- Limits: one public design page. It describes an implementation family and
  its availability limit; it does not prove that every total order requires
  consensus, measure coordination cost, or cover application-level merge.

### Jepsen — Causal Consistency

- Source id: `src.jepsen-consistency` (existing).
- Retained record: `read.batch4-causal.2026-10-21`, revision
  `3dbd842b05924a8bdee10daa1eaa53bb8d1eea83a915ecd4cbb7199756ddebc8`.
- URL: `https://jepsen.io/consistency/models/causal`.
- Representation: 2026-10-30 refetch is HTTP 200, 6,377 bytes, HTTP Date
  2026-10-30T22:37:40Z, ETag
  `58eb048b4e98f88105b8a9e16ca30eff2c614952`, no Last-Modified. The raw
  digest is byte-identical to the retained record. No new record is required.
- Sections used: Causal Consistency; Formally.
- Exact quotes:

      Causal consistency is sticky available: even in the presence of network
      partitions, every client connected to a non-faulty node can make progress.
      However, clients must stick to the same server.

      Convergent causal systems require that the values of objects in the system
      converge to identical values, once the same operations are visible.

      When a total order is required, and you’re willing to sacrifice availability
      (and latency), consider sequential consistency

      Mahajan et al. leave conflict resolution (what to do with concurrent writes)
      up to the implementation, requiring only that all concurrent writes are
      returned for a read.

- Limits: one public model page; it defines consistency models and does not
  describe a broker, a merge implementation or a production history.

## Book edits

### Owner page

- Frontmatter: only `updated_at` moves from 2026-10-20 to 2026-10-30.
  `evidence_scope`, `source_inspection_date`, `content_review` and
  `content_verified_at` are unchanged. The new records are supporting
  bindings, not new `evidence_scope` ids.
- The Lamport paragraph now records that short passages from the author-hosted
  PDF were inspected on 2026-10-30; the old abstract-only sentence is removed.
  The Lamport/Mattern paragraph adds the partial-order definition, the
  clock-condition converse limit, vector length and metadata, and labels the
  per-replica cost as Tycho.
- Section 1's failure and alternative paragraphs are rewritten with inline
  quotes, explicit Tycho labels and the model/mechanism distinction.
- The `### Causal Ordering` ownership section is rewritten in the same terms,
  with the two new owner-unit claim quotes and the Tycho labels.
- The ownership heading moves from line 168 to line 206. The page grows from
  183 to 231 lines.
- Raw SHA-256:
  `75f843ac87cff8250fafcf5851836a839d4042a5d81276895a118fb2745c3b34`.
- Historical-view SHA-256:
  `f6f5bd2ba6b3ba70e334c861aac7b02510f2e261fe597a62b5c4258d359c2e7f`.
- Base raw SHA-256:
  `50788725aab1831d58c7391be1af344c2afbc4f52543df37a69eeb0751d5e785`;
  base historical-view SHA-256:
  `264bd1362a1cbaed219021414a79607676cae2aa7d43c3a6c76583e2e7f3d172`.

### V11/C08 inline card

- `evidence_scope.source_ids` adds `src.lamport-time`,
  `src.mattern-vector-time`, `src.kafka` and `src.kafka-design`;
  `src.jepsen-consistency` was already declared.
- Good-fit conditions add that the delivery path preserves or re-establishes
  causal metadata.
- Competing alternative now distinguishes sequential consistency, a
  consensus-backed replicated log and per-key ordering; it states the
  per-partition and cross-partition limits and labels the cross-partition
  reading as Tycho.
- Failure and recovery now states the sticky-server condition, the
  reordered/lost-metadata paths and Tycho's inference label.
- Sources names the retained Jepsen record and the four new records.
- `updated_at` and `source_inspection_date` move to 2026-10-30; the card
  content review stays a historical self-check dated 2026-10-21.
- The `### Causal Ordering` card heading moves from line 281 to line 285
  because of the four added source ids. `### Session Consistency` moves from
  316 to 326. The chapter page grows from 410 to 420 lines.
- Raw SHA-256:
  `e967000b077a6d3866471db7dec806f41b65d06950cee434462ab8a169b32a52`.
- Historical-view SHA-256:
  `56b61a5a59ffeca6b3108cad3c9959464ba9a4bfa22d5a20ba28dc2ea06c1e45`.
- Base raw SHA-256:
  `3c25d9b5eaf1dec34bfe43a44a583a5769e6f6e8caac83829112f40c1b63702c`;
  base historical-view SHA-256:
  `d067e85e11fce863ff3f54e9cc2f56cea0f49d393310b31ee25a3aaa9d5f6944`.

No other book file is changed by this lane.

## Metadata needs (integrator)

The following changes are not in the lane commit. They are required before the
entry can be classified 4/4, promoted or reviewed as integrated. No scratch
copy was exercised for this lane; the proposed records and bindings below are
self-checked against the source text and the existing record shapes.

### Source register `sources/register.json`

Set `updated` to 2026-10-30; the source count moves from 303 to 304.

- `src.mattern-vector-time` — title "Virtual Time and Global States of
  Distributed Systems"; category `foundations`; publisher "Friedemann
  Mattern"; kind `paper`; URL the final PDF URL above; resolved URL the same;
  topics `["ordering","vector-clocks","distributed-systems"]`; priority
  `supporting`; planned use "Vector-clock construction, concurrency
  distinction and per-process metadata for the causal-ordering
  failure/recovery and alternative dimensions."; admission
  `admitted-for-research`; access `public-web-or-author-download`; reading
  status `full-public-page-inspected`; version records the 2026-10-30 access,
  1,255,805-byte PDF, 15 pages, raw SHA-256 `9dea637a...`, HTTP Date
  2026-10-30T22:37:42Z, Last-Modified 2006-03-07T22:00:42Z, ETag
  `13297d-40e6ec63e3680` (without surrounding quotes), the 1988 workshop /
  1989 Elsevier origin stated on page 1, and the absence of a separate version
  identifier; `access_checked` and `content_verified` 2026-10-30; license
  note "Author-hosted public conference paper; cite short excerpts and
  paraphrase; publisher copyright may restrict redistribution; do not mirror.";
  verification scope names the full 15-page PDF and the sections above, and
  excludes figures, references and linked material; observed title "Virtual
  Time and Global States of Distributed Systems".
- `src.lamport-time` — set `reading_status` to
  `full-public-page-inspected`; set `access_checked` and
  `content_verified` to 2026-10-30. Append to `version`: 854,562-byte PDF
  fetched 2026-10-30; raw SHA-256 `c55e7cab...`; HTTP Date
  2026-10-30T22:37:41Z; Last-Modified 2026-09-15T03:24:34Z; ETag
  `"0858abac144dd1:0"`; CACM 21(7), July 1978. Append to
  `verification_scope`: "Abstract, Introduction, The Partial Ordering,
  Logical Clocks and Ordering the Events Totally were read on 2026-10-30;
  formal proofs, figures, references and linked material were not verified."
  Do not change the URL or admission state.
- `src.kafka` — set `reading_status` to `full-public-page-inspected`;
  set `access_checked` and `content_verified` to 2026-10-30. Append to
  `version`: the 4.1 Introduction page was inspected 2026-10-30; 72,330-byte
  HTML; raw SHA-256 `f288579b...`; HTTP Date 2026-10-30T22:37:40Z;
  Last-Modified 2026-10-28T19:19:52Z; ETag `11a8a-65eeb729212bd` (without
  surrounding quotes). Append to `verification_scope`: "Introduction and
  Main Concepts and Terminology were read on 2026-10-30; other Kafka pages
  were not read in this lane." The entry URL may remain the documentation
  landing page; the ledger record carries the unit URL.
- `src.kafka-design` — set `reading_status` to
  `full-public-page-inspected`; set `access_checked` and
  `content_verified` to 2026-10-30. Append to `version`: the 4.1 Design
  page was inspected 2026-10-30; 143,123-byte HTML; raw SHA-256
  `d0198179...`; HTTP Date 2026-10-30T22:37:40Z; Last-Modified
  2026-10-28T19:19:52Z; ETag `22f13-65eeb7291ff35` (without surrounding
  quotes). Append to `verification_scope`: "Design, Replication, Replicated
  Logs: Quorums, ISRs, and State Machines (Oh my!) and Consumer Position were
  read on 2026-10-30; other design sections and linked pages were not read in
  this lane." Do not change the URL or admission state.

The retained Jepsen record stays unchanged. Its 2026-10-30 refetch returned
the same raw digest, so no new record or date update is required.

### Reading ledger `edition/patterns/reading-ledger.v1.json`

Add four records; set `updated` to 2026-10-30. Records move from 203 to 207.
Each record is `status: read`, `reviewer: "Automated authoring agent"`, and
uses the exact URL, label, sections and `content_sha256` below.

- `read.lamport-time.2026-10-30` — source `src.lamport-time`; label "Time,
  Clocks, and the Ordering of Events in a Distributed System — Leslie Lamport
  (CACM 1978)"; type `paper`; sections "Abstract", "Introduction", "The
  Partial Ordering", "Logical Clocks", "Ordering the Events Totally";
  content_sha256 `c55e7cab4230aa3d7126748a149b2db6f0d7a67296d5eccfdd50a210299a96b2`.
- `read.mattern-vector-time.2026-10-30` — source
  `src.mattern-vector-time`; label "Virtual Time and Global States of
  Distributed Systems — Friedemann Mattern (author-hosted paper)"; type
  `paper`; sections "Abstract", "1 Introduction", "5 The concept of time",
  "6 Virtual time", "7 Vector time", "8 The structure of vector time";
  content_sha256 `9dea637ae03a9ec2cdeae442a2c99739d6437bf2941b2b024590d4d684078fd7`.
- `read.kafka-introduction.2026-10-30` — source `src.kafka`; label
  "Introduction — Apache Kafka 4.1 documentation"; type
  `documentation-page`; sections "Introduction", "Main Concepts and
  Terminology"; content_sha256
  `f288579b9ed405c44df2f31e9245794902ff6f99f1369290c17dce1ddde2333f`.
- `read.kafka-design.2026-10-30` — source `src.kafka-design`; label
  "Design — Apache Kafka 4.1 documentation"; type `documentation-page`;
  sections "Design", "Replication", "Replicated Logs: Quorums, ISRs, and
  State Machines (Oh my!)", "Consumer Position"; content_sha256
  `d01981797402d75cada10599d586b753d02f8a9deb08d658a0e07758dedadfb7`.

### Source plan `edition/patterns/source-plan.v1.json`

Append four units to `tycho.pattern.causal-ordering` after the existing
Jepsen unit, in this order:

1. Lamport: label "Time, Clocks, and the Ordering of Events in a Distributed
   System — Leslie Lamport (CACM 1978)", type `paper`, URL the PDF above,
   record `read.lamport-time.2026-10-30`, sections equal to that record's
   five-entry `sections_read`.
2. Mattern: label "Virtual Time and Global States of Distributed Systems —
   Friedemann Mattern (author-hosted paper)", type `paper`, URL the final PDF
   above, record `read.mattern-vector-time.2026-10-30`, sections equal to
   that record's six-entry `sections_read`.
3. Kafka Introduction: label "Introduction — Apache Kafka 4.1
   documentation", type `documentation-page`, URL the Introduction page
   above, record `read.kafka-introduction.2026-10-30`, sections equal to that
   record's two-entry `sections_read`.
4. Kafka Design: label "Design — Apache Kafka 4.1 documentation", type
   `documentation-page`, URL the Design page above, record
   `read.kafka-design.2026-10-30`, sections equal to that record's four-entry
   `sections_read`.

Set every unit `status` to `read` and `blocked_reason` to `null`.
Replace the entry notes with: "Failure/recovery and alternative bound
2026-10-30 to Lamport's partial-order paper, Mattern's vector-time paper,
Kafka's 4.1 Introduction and Design pages and Jepsen's causal-consistency
page; server-switch and metadata-loss inferences, the cross-partition reading
and the choice rule remain Tycho."

Summary: `required_units` 244 -> 248; `read_units` 243 -> 247;
`blocked_units` stays 1; `ledger_records` 203 -> 207. Recompute
`registry_sha256` after saving the registry and refresh
`route_index_snapshot` from the rebuilt route index; no scratch value is
claimed.

### Registry `edition/patterns/registry.v1.json`

For `tycho.pattern.causal-ordering`:

- Keep `technical_owner.state`, `atlas_owner.state` and all coverage values
  at `partial-bounded`.
- Append the four units above to `source_units` after the existing Jepsen
  unit, in the source-plan order, all with status `read`; the unit labels must
  equal the plan labels.
- Replace `notes` with the source-plan notes plus "Coverage partial-bounded;
  no promotion."
- Keep `review_status` `self-checked`. The registry pattern entry has no
  `updated_at` field in the current schema; do not add one.

### Owner units `edition/patterns/owner-units.v1.json`

Entry `tycho.pattern.causal-ordering`:

- Set `owner.line` from 168 to 206. Keep the heading, document id and unit
  terms unchanged.
- Failure/recovery: set `state` to `supported`; replace `quote` with
  "A partition is therefore survivable only while a client stays on one
  non-faulty server; reconnecting elsewhere can expose missing dependencies."
  This sentence is verbatim in the owner section. Reason: "Jepsen states that
  causal consistency is sticky available only while clients stay on the same
  server; Lamport and Mattern both note that messages may be received out of
  order; Mattern's vector metadata travels with each message and convergence
  is required once operations are visible. The server-switch and metadata-loss
  failure paths are Tycho inferences, labelled in the page; the durable,
  replay and merge rule is Tycho guidance."
- Failure/recovery primary binding: `src.jepsen-consistency`, record
  `read.batch4-causal.2026-10-21`, section "Causal Consistency", quote
  "Causal consistency is sticky available: even in the presence of network
  partitions, every client connected to a non-faulty node can make progress.
  However, clients must stick to the same server.", revision
  `3dbd842b05924a8bdee10daa1eaa53bb8d1eea83a915ecd4cbb7199756ddebc8`.
- Failure/recovery supporting bindings:
  - Lamport, `read.lamport-time.2026-10-30`, section "The Partial Ordering",
    quote "Observe that messages may be received out of order.", revision
    `c55e7cab...`.
  - Mattern, `read.mattern-vector-time.2026-10-30`, section "Abstract",
    quote "Finally, we present a new algorithm to compute a consistent global
    snapshot of a distributed system where messages may be received out of
    order.", revision `9dea637a...`.
  - Mattern, same record, section "7 Vector time", quote "For that, we equip
    each process Pi with a clock Ci consisting of a vector of length n, where
    n is the total number of processes.", revision `9dea637a...`.
  - Jepsen, same record, section "Causal Consistency", quote "Convergent
    causal systems require that the values of objects in the system converge
    to identical values, once the same operations are visible.", revision
    `3dbd842b...`.
  - Jepsen, same record, section "Formally", quote "Mahajan et al. leave
    conflict resolution (what to do with concurrent writes) up to the
    implementation, requiring only that all concurrent writes are returned
    for a read.", revision `3dbd842b...`.
- Alternative: set `state` to `supported`; replace `quote` with "A total
  order is therefore a stronger serialization contract than causality: it adds
  a chosen order and its coordination, availability or latency cost." This
  sentence is verbatim in the owner section. Reason: "Jepsen recommends
  sequential consistency when total order is required and names the
  availability/latency cost; Kafka describes a replicated log that comes into
  consensus on the order and a leader that chooses it, and states the
  network-partition availability limit; Lamport's total-order extension
  depends on the chosen clocks and is not unique. The stronger-contract
  synthesis, the per-key/cross-partition reading and the choice rule are
  Tycho, labelled in the page."
- Alternative primary binding: `src.jepsen-consistency`, record
  `read.batch4-causal.2026-10-21`, section "Causal Consistency", quote
  "When a total order is required, and you’re willing to sacrifice
  availability (and latency), consider sequential consistency.", revision
  `3dbd842b...`.
- Alternative supporting bindings:
  - Kafka Design, `read.kafka-design.2026-10-30`, section "Replicated Logs:
    Quorums, ISRs, and State Machines (Oh my!)", quote "A replicated log
    models the process of coming into consensus on the order of a series of
    values", revision `d0198179...`.
  - Kafka Design, same record and section, quote "There are many ways to
    implement this, but the simplest and fastest is with a leader who chooses
    the ordering of values provided to it.", revision `d0198179...`.
  - Kafka Design, same record, section "Replication", quote "Kafka will remain
    available in the presence of node failures after a short fail-over
    period, but may not remain available in the presence of network
    partitions.", revision `d0198179...`.
  - Kafka Design, same record, section "Consumer Position", quote "Our topic
    is divided into a set of totally ordered partitions, each of which is
    consumed by exactly one consumer within each subscribing consumer group at
    any given time.", revision `d0198179...`.
  - Kafka Introduction, `read.kafka-introduction.2026-10-30`, section "Main
    Concepts and Terminology", quote "Events with the same event key (e.g., a
    customer or vehicle ID) are written to the same partition, and Kafka
    guarantees that any consumer of a given topic-partition will always read
    that partition’s events in exactly the same order as they were written.",
    revision `f288579b...`.
  - Lamport, `read.lamport-time.2026-10-30`, section "Ordering the Events
    Totally", quote "It is only the partial ordering which is uniquely
    determined by the system of events.", revision `c55e7cab...`.
  - Lamport, same record and section, quote "Different choices of clocks which
    satisfy the Clock Condition yield different relations", revision
    `c55e7cab...`.
- `source_support`: keep `read.batch4-causal.2026-10-21` as the primary
  record and add auxiliary entries for `read.lamport-time.2026-10-30`
  (`c55e7cab...`), `read.mattern-vector-time.2026-10-30` (`9dea637a...`),
  `read.kafka-introduction.2026-10-30` (`f288579b...`) and
  `read.kafka-design.2026-10-30` (`d0198179...`).
- Set `technical_coverage` to `partial-bounded`; keep `decision_coverage`
  at `partial-bounded` and `review_state` at `self-checked`. Set `notes`
  to the registry notes above, with the Tycho-labelled inferences named.
- Set `decision_evidence.competing_alternative` to the exact squashed card
  text: "Sequential consistency as the total-order model, a consensus-backed
  replicated log as one implementation, or per-key ordering. Jepsen notes that
  total order sacrifices availability and latency; Kafka guarantees order per
  partition and routes same-key events to one partition, not a topic-wide
  order. Reverse the choice when causal metadata cost exceeds the ordering
  benefit; the cross-partition reading is Tycho."
- Summary counters: `failure_recovery_supported` 68 -> 69;
  `alternative_supported` 73 -> 74. `technical_partial_bounded` stays 16
  and `technical_partial` stays 74 because coverage is derived from
  mechanism and invariant for this entry.

### Card registration `edition/patterns/card-batches.v1.json`

No change is required while the card remains inline: the
`tycho.pattern.causal-ordering` entry already has the C08 `atlas_section`
and `ledger_record`. If the integrator splits the card to isolate it from the
shared-page promotion, add `card_path` to the new file and keep the same
`ledger_record`.

### Content revisions `edition/content-revisions.json`

Add one issue-540 revision with `authorized_at` 2026-10-30 and authorization
"B42 causal ordering failure/recovery and alternative source binding; no
promotion or owner acceptance." Use these historical-view hashes:

- Owner path, previous:
  `264bd1362a1cbaed219021414a79607676cae2aa7d43c3a6c76583e2e7f3d172`;
  current:
  `f6f5bd2ba6b3ba70e334c861aac7b02510f2e261fe597a62b5c4258d359c2e7f`.
- Card path, previous:
  `d067e85e11fce863ff3f54e9cc2f56cea0f49d393310b31ee25a3aaa9d5f6944`;
  current:
  `56b61a5a59ffeca6b3108cad3c9959464ba9a4bfa22d5a20ba28dc2ea06c1e45`.
- Leave `source_blocks`, `enrichment_documents`, `enrichment_additions`
  and `enrichment_baselines` empty.

Raw file hashes for reference:
`75f843ac87cff8250fafcf5851836a839d4042a5d81276895a118fb2745c3b34`
(owner) and
`e967000b077a6d3866471db7dec806f41b65d06950cee434462ab8a169b32a52`
(card).

### Atlas manifest `edition/atlas-manifest.json`

Set the V11/C08 document `sha256` to
`e967000b077a6d3866471db7dec806f41b65d06950cee434462ab8a169b32a52` and
`registry_sha256` to the new registry file hash after the registry edit.
No atlas route changes.

### Chapter source ledger (shared book page, not edited)

The chapter page
`book/volumes/v04-distributed-coordination-and-events/c01-time-causality-and-ordering/README.md`
still records E01 as "official abstract and bibliographic record, accessed
2026-10-18" and "full PDF not inspected." That row is now stale. Update E01 to
add the author-hosted PDF URL, the 2026-10-30 access date and the sections
read, and narrow its limitation to "no formal proof verification, figure
inspection or implementation experiment." This is a shared book page outside
the lane's edit scope; it is not changed here.

### Promotion impact on the shared V11/C08 page

Editing the inline card changes the c08 chapter page from
`3c25d9b5eaf1dec34bfe43a44a583a5769e6f6e8caac83829112f40c1b63702c` to
`e967000b077a6d3866471db7dec806f41b65d06950cee434462ab8a169b32a52`.
The `tycho.pattern.fencing-tokens` promotion in
`edition/patterns/sufficient-promotions.v1.json` stores the old page hash as
its `card_sha256`, so
`python3 scripts/validate_pattern_owner_units.py` now fails
`owner-units-promotion-card-hash: tycho.pattern.fencing-tokens`.

Do not overwrite that hash as a bookkeeping change. The promotion reviewed the
old page. Integration must either (a) split the fencing-tokens card into its
own file and run a delta review plus a new promotion record, or (b) re-review
the changed c08 page, confirm the fencing-tokens section is unchanged and
record a new promotion. This lane does not edit shared JSON, does not claim
either path, and does not claim that the promotion remains valid.

### Derived artifacts and review metadata

The book edit changes one canonical owner page and one atlas chapter. The
source register gains one id and the ledger, source plan, registry, owner
units, content revision and atlas manifest change. Refresh once at batch end:
route index, page census, coverage/reverse map, phase 4, delivery-evidence
counts, edition inventory and the source catalogue
(`python3 scripts/source_catalog.py`). The sufficient-candidate and
sufficient-ready-plan files still reflect the 2026-10-22/27 states; regenerate
or reconcile them once the owner units are integrated.

The 2026-10-22 sufficient review record in
`edition/patterns/sufficient-review-records.v1.json` carries the old owner
page hash. This edit adds changed bytes; do not update the record without a
fresh review. The book/atlas independent review gate applies.

## Validation

Checker output in the lane worktree after the two book edits:

    PASS: V11 prose <=100; 145 exact owner-link exceptions
    PASS: configured lexical boundary checks; independent-origin review still
    required.

Owner-section quote audit: 17 quoted fragments in the edited owner prose are
whitespace-normalized substrings of the five served units; zero missing. The
audit used `pdftotext -raw` for the two PDFs and stripped HTML text for the
three web pages. The Lamport and Mattern PDFs are two-column; `pdftotext
-layout` interleaves columns and produces false misses. The Tycho-labelled
sentences are not presented as source quotes.

Targeted validator results with the book edits only, in the lane worktree:

- `python3 scripts/check_markdown_line_length.py` — PASS.
- `python3 scripts/check_boundary.py` — PASS.
- `python3 scripts/validate_pattern_cards.py` — PASS; 145 entries.
- `python3 scripts/validate_pattern_registry.py` — PASS; 145 entries.
- `python3 scripts/validate_pattern_sources.py` — PASS; 243 read; 203
  ledger records (the lane changes no source metadata).
- `python3 scripts/validate_book_metadata.py` — FAIL unknown source ID for
  `src.mattern-vector-time`; integrator register work.
- `python3 scripts/validate_pattern_atlas.py` — FAIL
  `atlas-document-sha`; expected until the atlas manifest is updated.
- `python3 scripts/validate_pattern_owner_units.py` — FAIL
  `owner-units-promotion-card-hash: tycho.pattern.fencing-tokens`; the
  shared-page promotion impact above. It also still carries the old causal
  quotes and line until the owner-units metadata is integrated.
- `python3 scripts/validate_decomposition.py` — FAIL
  `altered-source-payload`; expected until the content revision is applied.
- `python3 scripts/validate_enrichment.py` — FAIL
  `enrichment-baseline-altered`; expected until the content revision is
  applied.

The full unit suite was not run; batch-end tests remain with the integrator.

## Limits

The binding uses four public units and one retained public unit. They define
partial order, logical clocks, vector clocks, per-partition order, replicated
log ordering, sticky availability and the availability cost of total order.
None observes this page's service, measures coordination or metadata cost,
proves that every total order requires consensus, or supplies a production
merge policy.

The owner section states a Tycho synthesis: "A total order is therefore a
stronger serialization contract than causality: it adds a chosen order and its
coordination, availability or latency cost." The source-supported parts are the
sequential-consistency recommendation and its availability/latency cost, the
consensus-backed replicated-log implementation, the per-partition and same-key
guarantees, and Lamport's non-unique total-order extension. The stronger-
contract framing and the choice rule are Tycho guidance, labelled in the page.

The page does not assert that consensus is the only possible total-order
mechanism. Kafka supplies one implementation family; Lamport's logical-clock
construction is another. The earlier review's model/mechanism conflation is
resolved by naming sequential consistency as the required model and the
replicated log or logical-clock construction as implementation families.

The owner page's `evidence_scope.source_ids` still lists only
`src.jepsen-consistency`. The new records are supporting bindings, not new
page-level evidence-scope ids. Adding them to the owner page would require the
enrichment manifest, both historical hashes, the content revision and the
decomposition/enrichment validators; treat that as a separate change.

No owner acceptance, promotion, CI, independent review or merge permission is
claimed.

## Review needs

- Request a fresh external review under the book/atlas gate. The reviewer
  should check quote-to-claim fit for both dimensions, the Tycho labels for the
  server-switch/metadata-loss inferences, the cross-partition reading and the
  choice rule, the five revisions, the moved owner-unit line, the metadata
  patch and the shared-page promotion impact.
- The reviewer must use read-only repository access and must not run tests.
- The fencing-tokens promotion cannot be silently rebound; the review must
  cover whichever resolution the integrator chooses.

## Commit scope

The lane commit contains this note and the two book files only:

- `book/volumes/v04-distributed-coordination-and-events/`
  `c01-time-causality-and-ordering/causal-order.md`;
- `book/volumes/v11-pattern-atlas/c08-coordination/README.md`.

No shared JSON, promotion, test or generated file is in the lane commit.
