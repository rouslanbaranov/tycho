# B63 — Online Data Migration invariant, recovery and alternative lane

Status: lane-local book edit, self-checked on 2026-10-31. No shared edition
metadata, promotion, generated artifact or owner acceptance is included. The
entry was 1/4 at the parent HEAD: mechanism was supported; invariant,
failure/recovery and alternative were partial. This lane binds the three partial
dimensions and refreshes the mechanism binding using four public sources (six
pages): Stripe, *Online migrations at scale*; PostgreSQL 18.6, *pg_dump* and
*COPY*; the AWS DMS *User Guide*, *What is AWS Database Migration Service?* and
*Creating tasks for ongoing replication using AWS DMS*; and Flyway,
*Rolling out updates from a single schema to multiple production databases*
(expand/contract guidance). The card is inline in V11/C06 and this lane edits
that block. Label Tycho.

## Lane coordinates

- Parent HEAD: 09bbe5a622e367c35f3fe38c8132c725ebaa68ac (09bbe5a6).
- Lane label: Tycho.
- Branch: b63-online-migration; worktree:
  /Users/rbaranov/Projects/tycho-worktrees/b63-online-migration.
- Scope: the owner section "Online Data Migration" in V05/C06, the inline
  "Online Data Migration" card in V11/C06, and this note. Single-entry lane; no
  other entry, shared JSON, promotion or generated file is changed.
- Owner path (concatenate):

      book/volumes/v05-data-models-engines-and-lifecycle/
      c06-schema-evolution-data-migration-and-retention/migration-retirement.md

- Inline card path:
  book/volumes/v11-pattern-atlas/c06-database-storage/README.md.
- Exactly three files change: the owner page, the inline card host and this
  note.
- Existing source ids: src.m9-st01, src.postgresql, src.flyway, src.gh-ost.
- New source ids proposed: src.aws-dms, src.flyway-expand-contract.
- New ledger records proposed: six, listed below.
- Retained historical record: read.batch3-gh-ost.2026-10-21, kept as earlier
  mechanism context but no longer the current binding.
- Baseline and final line-length and boundary checks pass.

## Card location

The registry records atlas_owner.chapter = V11/C06 and section
online-data-migration. card-batches.v1.json records no card_path for this
pattern, and the C06 chapter landing already contains the card body. This lane
edits the inline block rather than creating a dedicated page. The chapter
frontmatter evidence_scope.source_ids and notes are updated because they describe
the cards hosted by that page; the registry, card batches and atlas manifest are
left for the integrator. Precedent: B38, B53, B59, B60, B61 and B62 edited
inline card hosts and their chapter source lists the same way.

## Baseline and gap

edition/patterns/owner-units.v1.json records mechanism as supported and the
other three dimensions as partial. The recorded reasons are:

- mechanism: "Explains copy-while-live-writes and the change-capture/reconciliation
  arrangement." Its binding is read.batch3-gh-ost.2026-10-21, section "How?".
- invariant: "gh-ost README has no two-writer atomicity or dual-schema rule."
- failure_recovery: "README has no crash checkpoint or row-reconciliation
  procedure."
- alternative: "README names modes/tools, not stop-the-world or dual-write
  alternatives."

The entry records technical_coverage partial, decision_coverage partial-bounded
and review_state self-checked. The online-data-migration record does not carry a
separate external-review verdict, so this lane does not claim one.

The base owner page is 228 lines, 2,179 words, SHA-256
dea4123f9efb50ba8bc5f751c5f2f36694da909232bf4e51a2e3275926883bde. The base
owner subsection (lines 215-228) is 14 lines, 130 words, SHA-256
874f17e7a788f4770d021ea50f8e0f338fa0ed7c797b09bb8b236c6ed6da2555. The base
chapter landing is 323 lines, 1,426 words, SHA-256
962ea787e3b8726f19719d45153397a42bf6ef9868809afed8a6b2388a0339d0. The base
card block (lines 263-292) is 30 lines, 148 words, SHA-256
2c5747e14e701bb343a07f6f904b0f5c4ec319af00563b6c4e4c32e7e4b30432.

The final owner page is 286 lines, 2,749 words, SHA-256
182dde543c8b935a66005c4cdac4b9625af74997f70f9c4b71b3025c42a40db1. The final
owner subsection (line 223 to end) is 64 lines, 655 words, SHA-256
7f4b18a0dd6928419e4bd32601e052d220db590f901415dcd6e31d292dafdaef. The final
chapter landing is 345 lines, 1,654 words, SHA-256
e9910dc7219a1c0ad4debccf890afe8ab457334cbd796a4df2242b21e2118eca. The final
card block (lines 269-315, including the separating blank) is 47 lines, 340
words, SHA-256
94324f2bb219cd8edcb8b86f1cd96cc2ca7ff17387b16aab9516ed9bc8142da2.

The gap was evidential. The owner page and card already stated the live-copy
shape, the non-atomic two-writer risk, the checkpoint/mapping hazard and the
offline/dual-write comparison as Tycho guidance, but no exact public quote,
section and representation hash bound those claims. Shared metadata still shows
1/4 and partial-bounded until the integrator applies the proposals below.

The lane narrows four claims. First, Stripe's dual-write pattern is an
application-level sequence of writes and read-path comparisons; the article does
not claim one atomic commit across both stores. Second, AWS DMS caches a
checkpoint "from time to time", so the checkpoint is a recovery point, not a
per-commit record. Third, no selected unit tests a changed business-key mapping;
Flyway's immutable-applied-change rule is related delivery discipline, not a
data-mapping test. Fourth, the stop-the-world quiesce/export/load/verify sequence
is a Tycho operating shape; the PostgreSQL pages document export, COPY and
restore behavior, not that procedure. Stripe calls its consistency checks
Scientist experiments; "reconciliation" is the Tycho umbrella term for those
checks plus the final backfill recheck.

## Candidate evaluation

- Stripe, "Online migrations at scale" (selected). Publishes the four-step
  dual-write pattern, the old/new store sequence, read-path comparison, offline
  backfill and retirement. Primary source for mechanism, invariant and the
  dual-write comparison.
- PostgreSQL 18.6, "pg_dump" (selected). Defines consistent exports under
  concurrent readers and writers, the serializable-deferrable caveat, and the
  interrupted-restore catalog warning. Primary source for the snapshot boundary
  and the offline export alternative.
- PostgreSQL 18.6, "COPY" (selected). Defines positional field mapping, bulk
  row insertion, trigger and constraint behavior, and the deleted-row residue of
  a failed COPY. Primary source for the mapping and partial-load limits.
- AWS DMS, "What is AWS Database Migration Service?" (selected). Defines
  one-time migration versus ongoing replication and the service boundary.
  Supporting source for the managed full-load plus CDC alternative.
- AWS DMS, "Creating tasks for ongoing replication using AWS DMS" (selected).
  Defines full-load plus CDC and CDC-only task types, checkpoint caching,
  recovery from a checkpoint and CDC start-point selection. Primary source for
  failure and recovery.
- Flyway, "Rolling out updates from a single schema to multiple production
  databases" (selected). Its "Backward-compatible changes (expand/contract)"
  section defines the expand/migrate/contract sequence and the nullable,
  dual-write, backfill, switch-reads, drop order. Primary source for the
  expand/contract alternative.
- gh-ost README, read.batch3-gh-ost.2026-10-21 (retained historical). It
  describes a ghost-table copy with ongoing change propagation, but it does not
  state the two-writer, checkpoint or stop-the-world rules this entry needs. It
  is not the current binding.
- PostgreSQL 17 ALTER TABLE, already cited by the owner page (considered, not
  newly bound). It supports the DDL lock and no-return discussion elsewhere on
  the page, not the online data-copy dimensions.
- Flyway "Migrations" concepts page (considered, not bound). It describes
  versioned and repeatable migrations, schema history and migration execution;
  it does not contain the expand/contract guidance. The fleet-rollout page is
  the current Flyway page with that section.
- Flyway and Redgate blue/green articles (considered, not bound). They discuss
  database deployment patterns but are not the selected documentation page and
  add no needed claim beyond the expand/contract section.
- AWS DMS marketing, pricing and PDF user-guide copies (considered, not bound).
  The user-guide markdown pages carry the exact statements and revision metadata.
- Vendor tutorials and third-party summaries (considered, not bound). They are
  not primary documentation for the four claims and would add unverified
  restatements.

No PostgreSQL, AWS DMS, Flyway or Stripe runtime exercise, benchmark or failure
drill was run.

## Source units and revisions

All fetches were public HTTPS GETs on 2026-10-31, twice per page. Raw bytes were
hashed from the served decompressed representation. HTTP dates are UTC. Where a
page served a markdown alternate, this lane read that alternate and records both
the human page URL and the representation used.

Canonical extraction for HTML: select the named content subtree; remove
script/style/nav/footer/header elements and elements with class navheader or
navfooter; convert block tags to newlines; strip remaining tags; decode
entities; normalize non-breaking spaces; normalize typographic quotes and
dashes to ASCII; collapse space runs and blank lines; strip. The selected
subtrees are section.BlogPost__body for Stripe, div#docContent for PostgreSQL and
div#main-content for Flyway. Character counts include spaces and newlines; word
counts split on whitespace. Markdown alternates are normalized only for line
endings, trailing whitespace and repeated blank lines.

### R1 — Stripe, "Online migrations at scale"

- Record: read.stripe-online-migrations.2026-10-31 (proposed).
- Source: src.m9-st01 (existing; proposed reconciliation from pending to read).
- URL: https://stripe.com/blog/online-migrations
- Label/type: "Online migrations at scale — Stripe engineering article";
  engineering article by Jacqueline Xu, published 2017-02-02.
- Representation: HTTP/2 200 on 2026-10-31T21:58:56Z and again at
  2026-10-31T21:58:57Z; 411,763-byte and 399,214-byte decompressed HTML; no
  Last-Modified or ETag served; raw HTML SHA-256
  d6315d487efcae0d7ce41a201075a58a3bc51b209ccc43159661cacfb5350a17 on the
  first fetch and
  decc39e7e5b1f2c867d79e7aeb414d7f88e9a1f3063c3589ff9a86fc960fb114 on the
  second, differing in dynamic experiment and edge markup. Canonical article
  text is identical on both fetches: 11,056 characters / 1,801 words, SHA-256
  f55df9ddac4a2b47514a9570da5f9a5f3d1f09145af5d865bcca6704fbad9519.
- Sections read: "A pattern for online migrations"; "Part 1: Dual writing";
  "Part 2: Changing all read paths"; "Part 3: Changing all write paths";
  "Part 4: Removing old data"; "Conclusion". The article body was read in full.
- Sections not read: linked pages, images and unrelated site chrome.
- Claims supported: Q1-Q8.
- Limits: a 2017 engineering article about one subscription data-model
  migration; not a formal specification, benchmark or current Stripe system
  description. It does not state an atomic cross-store transaction.

### R2 — PostgreSQL 18.6, "pg_dump"

- Record: read.postgres-pgdump.2026-10-31 (proposed).
- Source: src.postgresql (existing; add this unit).
- URL: https://www.postgresql.org/docs/current/app-pgdump.html
- Label/type: "PostgreSQL 18: pg_dump"; official documentation, PostgreSQL
  18.6.
- Representation: HTTP/2 200 on 2026-10-31T21:09:33Z and again at
  2026-10-31T19:06:17Z (cached responses); 89,919-byte HTML both times; no
  Last-Modified or ETag served; raw HTML
  SHA-256 1a32251a83e6dec1a967dbfc93e1add0ba99bfe84fae471ea56613e6e7306d30 on
  both fetches. Canonical text 41,961 characters / 6,578 words, SHA-256
  3ea3630d2df755269048563c7468de0bb9f4b98d17f924e436d38dfe46820fdf.
- Sections read: Description; Options, including --serializable-deferrable and
  --disable-triggers; Notes; Examples; Diagnostics. The page was read in full.
- Sections not read: linked pages and the PostgreSQL source code.
- Claims supported: Q9-Q13.
- Limits: documentation of a utility and its options; no dump, restore or
  concurrent workload was run. The serializable-deferrable caveat describes
  consistency with serial execution, not a universal failure of every dump.

### R3 — PostgreSQL 18.6, "COPY"

- Record: read.postgres-copy.2026-10-31 (proposed).
- Source: src.postgresql (existing; add this unit).
- URL: https://www.postgresql.org/docs/current/sql-copy.html
- Label/type: "PostgreSQL 18: COPY"; official documentation, PostgreSQL 18.6.
- Representation: HTTP/2 200 on 2026-10-31T16:05:57Z on both fetches;
  62,490-byte HTML both times; no Last-Modified or ETag served; raw HTML
  SHA-256 d85166d9fc149ef73c181533b1ff89ce1346948349dcf5d4c028b994d3f4ac53 on
  both fetches. Canonical text 28,697 characters / 4,956 words, SHA-256
  ed656babcaf6d93cb64b4514ad9259da08988cb71d08ddfaa7823605a56ddc4c.
- Sections read: Description; Parameters, including column_name and query;
  Outputs; Notes; File Formats; Examples; Compatibility. The page was read in
  full.
- Sections not read: linked pages and the PostgreSQL source code.
- Claims supported: Q14-Q18.
- Limits: documentation of a SQL command; no COPY, trigger, constraint or
  failure scenario was executed. "Deleted state" describes physical residue,
  not a guarantee that a retry sees those rows.

### R4 — AWS DMS, "What is AWS Database Migration Service?"

- Record: read.aws-dms-overview.2026-10-31 (proposed).
- Source: src.aws-dms (proposed).
- URL: https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html
- Representation used: the AWS-served markdown alternate,
  https://docs.aws.amazon.com/dms/latest/userguide/Welcome.md
- Label/type: "What is AWS Database Migration Service? — AWS DMS User Guide";
  official documentation.
- Representation: HTTP/1.1 200 on 2026-10-31T21:55:32Z; 6,106-byte markdown
  alternate, 2,369 transferred bytes; Last-Modified
  Sat, 31 Oct 2026 03:33:41 GMT; ETag "3Zr0CA1pp+fv62L067zSK/e1kVQ=-gzip";
  raw markdown SHA-256
  31b345aa2f638daa752802e49da1e8b3ea5409759189a0f28b20be369a0ea5ed on both
  fetches. Canonical text 6,086 characters / 934 words, SHA-256
  9391024f929dea3d8824ab956e9c20749dea9bdf865b9ee02d033b08c695dcc0.
- Sections read: the full page, including "What is AWS Database Migration
  Service?" and "Migration tasks that AWS DMS performs".
- Sections not read: linked user-guide pages and images.
- Claims supported: Q19-Q20.
- Limits: a living service guide; it describes service intent, not a benchmark,
  service-level guarantee or local reproduction.

### R5 — AWS DMS, "Creating tasks for ongoing replication using AWS DMS"

- Record: read.aws-dms-cdc.2026-10-31 (proposed).
- Source: src.aws-dms (proposed).
- URL: https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Task.CDC.html
- Representation used: the AWS-served markdown alternate,
  https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Task.CDC.md
- Label/type: "Creating tasks for ongoing replication using AWS DMS — AWS DMS
  User Guide"; official documentation.
- Representation: HTTP/1.1 200 on 2026-10-31T21:57:36Z; 23,791-byte markdown
  alternate, 7,553 transferred bytes; Last-Modified
  Sat, 31 Oct 2026 03:33:44 GMT; ETag "WQqQO6K0X4jUTQRVuNbDk/Bvyn4=-gzip";
  raw markdown SHA-256
  0d96560346e974c2450e392f4696f81235ad36861f832ae2e41672b66312ba7a on both
  fetches. Canonical text 23,581 characters / 3,591 words, SHA-256
  9a4d986bbef7aaff8385f6ed6c0bbc51b12cfbdbd4e2154f7f368c9e78380918.
- Sections read: the full page, including full-load plus CDC and CDC-only task
  types, CDC start points, using a checkpoint as a CDC start point, stopping at
  a commit or server time, and bidirectional replication.
- Sections not read: linked endpoint pages, images and the PDF rendering.
- Claims supported: Q21-Q26.
- Limits: a living guide; it documents task settings and intended recovery
  behavior, not a tested recovery. It does not define a per-commit checkpoint.

### R6 — Flyway, "Rolling out updates from a single schema to multiple production databases"

- Record: read.flyway-expand-contract.2026-10-31 (proposed).
- Source: src.flyway-expand-contract (proposed).
- URL: https://documentation.red-gate.com/x/NoJvF (public short link; resolves
  to page ID 342852150).
- Resolved URL (concatenate):

      https://documentation.red-gate.com/fd/
      rolling-out-updates-from-a-single-schema-to-multiple-production-databases-342852150.html

- Label/type: "Rolling out updates from a single schema to multiple production
  databases — Redgate Flyway documentation"; official documentation, published
  2026-05-12 and page-last-updated 2026-08-18.
- Representation: HTTP/1.1 200 on 2026-10-31T21:59:04Z and again at
  2026-10-31T21:59:05Z; 62,417-byte HTML both times; no Last-Modified or ETag served; raw HTML
  SHA-256 5078c8ee35868b0b2013ccc5d54c9c173e4e03948ce0d44f17590aac4db83459 on
  both fetches. Canonical text 21,271 characters / 3,235 words, SHA-256
  a85f51e81ffce1075853639f07d6e3661f8d98f939e8b5478c87f26a4777ea6f.
- Sections read: the full page, including "Core principles", "Backward-compatible
  changes (expand/contract)", "Handling failures", "Proactive drift checks" and
  the safe-rollout sequence.
- Sections not read: linked tutorials and images.
- Claims supported: Q27-Q31.
- Limits: current Flyway documentation for a fleet rollout; it describes intended
  deployment practice, not a benchmark or a data-migration run. The task brief
  says "Flyway expand-contract"; the current Flyway documentation has no page
  titled "Expand-Contract". This fleet-rollout page contains the exact
  expand/contract section and is the closest exact public Flyway unit.

## Selected exact quotes

Quotes reproduce the served prose after the whitespace normalization described
above. Typographic apostrophes and quotation marks are ASCII in this note.
Thirty-one passages were checked against the named canonical representations on
2026-10-31; 31/31 were present. The owner and card use a subset; every fragment
used there was also checked.

### Mechanism

- Q1, R1, "A pattern for online migrations":

      There's a common 4 step dual writing pattern that people often use to do
      large online migrations like this.

- Q2, R1, "A pattern for online migrations":

      Dual writing to the existing and new tables to keep them in sync.

- Q14, R3, "Description":

      COPY moves data between PostgreSQL tables and standard file-system files.
      COPY TO copies the contents of a table to a file, while COPY FROM copies
      data from a file to a table (appending the data to whatever is in the
      table already). COPY TO can also copy the results of a SELECT query.

- Q19, R4, "What is AWS Database Migration Service?":

      You can perform one-time migrations or replicate ongoing changes to keep
      sources and targets in sync.

- Q21, R5, "Creating tasks for ongoing replication using AWS DMS":

      You can create an AWS DMS task that captures ongoing changes from the
      source data store. You can do this capture while you are migrating your
      data.

- Q22, R5, "Creating tasks for ongoing replication using AWS DMS":

      There are two types of ongoing replication tasks:

### Invariant

- Q3, R1, "Part 1: Dual writing":

      All new writes should update both stores.

- Q4, R1, "Part 3: Changing all write paths":

      Our two tables need to stay consistent with each other at every step.

- Q5, R1, "Part 2: Changing all read paths":

      If the results don't match, raise an error alerting our engineers to the
      inconsistency.

- Q9, R2, "Description":

      pg_dump is a utility for exporting a PostgreSQL database. It makes
      consistent exports even if the database is being used concurrently.

- Q10, R2, "Description":

      Script dumps are plain-text files containing the SQL commands required to
      reconstruct the database to the state it was in at the time it was saved.

- Q11, R2, "Options":

      Without it the dump may reflect a state which is not consistent with any
      serial execution of the transactions eventually committed. For example, if
      batch processing techniques are used, a batch may show as closed in the
      dump without all of the items which are in the batch appearing.

- Q15, R3, "Parameters":

      If a column list is specified, COPY TO copies only the data in the
      specified columns to the file. For COPY FROM, each field in the file is
      inserted, in order, into the specified column.

### Failure and recovery

- Q7, R1, "Part 1: Dual writing":

      Once the migration is complete, run the Scalding job once again to make
      sure there are no existing subscriptions missing from the Subscriptions
      table.

- Q8, R1, "Part 3: Changing all write paths":

      If we miss any cases, we might end up with data inconsistency.

- Q12, R2, "Notes":

      If the restore is stopped in the middle, the system catalogs might be left
      in the wrong state.

- Q13, R2, "Notes":

      When a dump without schema is chosen and the option --disable-triggers is
      used

- Q16, R3, "Notes":

      COPY FROM will invoke any triggers and check constraints on the
      destination table. However, it will not invoke rules.

- Q17, R3, "Notes":

      The COPY FROM command physically inserts input rows into the table as it
      progresses. If the command fails, these rows are left in a deleted state;
      these rows will not be visible, but still occupy disk space.

- Q18, R3, "Description":

      By default, COPY will fail if it encounters an error during processing.

- Q23, R5, "Using a checkpoint as a CDC start point":

      An ongoing replication task migrates changes, and AWS DMS caches
      checkpoint information specific to AWS DMS from time to time. The
      checkpoint that AWS DMS creates contains information so the replication
      engine knows the recovery point for the change stream. You can use the
      checkpoint to go back in the timeline of changes and recover a failed
      migration task.

- Q24, R5, "Determining a CDC native start point":

      DMS captures transactions that started after the chosen CDC start point.

- Q25, R5, "Determining a CDC native start point":

      To avoid any data inconsistencies, carefully choose the start point for
      the replication-only task.

- Q26, R5, "Creating tasks for ongoing replication using AWS DMS":

      AWS DMS CDC does not provide real-time replication. Replication latency
      varies based on source workload, network conditions, replication instance
      resources, target ingestion capacity, and data characteristics. There are
      no SLAs for CDC latency.

- Q28, R6, "Core principles":

      Immutability of applied changes. Once a change has been applied to any
      production database, never edit the artefact that produced it; add a new
      change instead.

### Alternative

- Q27, R6, "Core principles":

      Forward-compatible schema changes. Changes should be safe to apply while
      the previous version of the application is still running. Use the
      expand/contract pattern (add new columns nullable, dual-write, backfill,
      switch reads, then drop) so a partial rollout -- application v1 against
      schema v2 -- keeps working.

- Q29, R6, "Driving the fleet":

      Sequential rollout is the safe default. A failure on the first node halts
      the rollout before the rest of the fleet diverges.

- Q30, R6, "Backward-compatible changes (expand/contract)":

      The expand/contract pattern splits a breaking change into a sequence of
      non-breaking ones, each released independently:

- Q31, R6, "Backward-compatible changes (expand/contract)":

      Update application code to write to both old and new structures, then to
      read from the new one. Backfill historical data with a one-off change.

- Q6, R1, "Part 1: Dual writing":

      We make snapshots of our databases available to our Hadoop cluster

- Q20, R4, "What is AWS Database Migration Service?":

      AWS Database Migration Service (AWS DMS) is a cloud service that makes it
      possible to migrate relational databases, data warehouses, NoSQL databases,
      and other types of data stores.

## Dimension mapping

- Mechanism. Primary: Q2, record read.stripe-online-migrations.2026-10-31,
  source src.m9-st01, section "A pattern for online migrations", revision
  f55df9ddac4a2b47514a9570da5f9a5f3d1f09145af5d865bcca6704fbad9519.
  Supporting: Q1 (four-step pattern), Q6 (offline snapshot backfill), Q10
  (export/restore state), Q14 (COPY moves rows), Q19 and Q21-Q22 (DMS
  full-load plus CDC). Tycho reading:
  an online migration is a copy plus a change stream plus a reconciliation
  boundary; it is not a single distributed transaction.
- Invariant. Primary: Q4, record read.stripe-online-migrations.2026-10-31,
  source src.m9-st01, section "Part 3: Changing all write paths", revision
  f55df9ddac4a2b47514a9570da5f9a5f3d1f09145af5d865bcca6704fbad9519.
  Supporting: Q2-Q3 and Q5 (dual writes and read-path comparison), Q9 and Q11
  (a consistent export is distinct from serial execution history), Q15
  (positional COPY mapping). Tycho rule: one authoritative writer, or an
  idempotent reconciled projection; mapping revisions must be single-valued.
  The sources do not claim that a shared schema field makes two writes atomic.
- Failure and recovery. Primary: Q23, record read.aws-dms-cdc.2026-10-31,
  source src.aws-dms, section "Using a checkpoint as a CDC start point",
  revision 9a4d986bbef7aaff8385f6ed6c0bbc51b12cfbdbd4e2154f7f368c9e78380918.
  Supporting: Q7-Q8 (backfill recheck and missed cases), Q12-Q13 (interrupted
  restore), Q16-Q18 (COPY side effects and failed residue), Q24-Q25
  (start-point choice), Q26
  (latency), Q28 (immutable applied changes). Tycho runbook: persist a
  checkpoint with the data commit where possible, record mapping and source
  revisions, detect post-snapshot changes, and reconcile before declaring
  completion. Narrowing: no selected unit tests a changed business-key mapping;
  Q28 is a delivery rule for applied migration artifacts, not a mapping test.
- Alternative. Primary: Q27, record read.flyway-expand-contract.2026-10-31,
  source src.flyway-expand-contract, section "Core principles", revision
  a85f51e81ffce1075853639f07d6e3661f8d98f939e8b5478c87f26a4777ea6f.
  Supporting: Q30-Q31 (expand/contract phases), Q9-Q10 and Q14 (consistent
  export and bulk load), Q19 and Q22 (managed full-load plus CDC), Q1-Q2
  (dual write). Tycho choice rule: stop-the-world export/restore when a bounded
  maintenance window and whole-dataset copy are acceptable; expand/contract when
  old and new application versions must coexist; managed full-load plus CDC or
  dual-write with reconciliation when the team can operate capture, checkpoint
  and reconciliation. Reverse when the changed-row set is small or the team
  cannot operate those controls.
- Retention and coverage. The lane proposes technical_coverage sufficient and
  decision_coverage sufficient because each owner claim now has a bound primary
  passage, supporting passages, explicit limits and a narrowed alternative.
  This is a self-check, not independent review or owner acceptance.

## Proposed shared metadata

The following changes are proposals only. No shared JSON is edited in this lane.

### sources/register.json

Add src.aws-dms:

- title "AWS Database Migration Service User Guide"; category databases;
  publisher Amazon Web Services; kind official-docs; URL
  https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html; topics
  database-migration, change-data-capture, replication; priority supporting;
  planned_use "Managed full-load and CDC behavior, checkpoint recovery and
  start-point limits for the online migration entry."; admission
  admitted-for-research; access public-web-or-author-download; reading_status
  full-public-page-inspected; access_checked and content_verified 2026-10-31;
  version "AWS DMS User Guide, fetched 2026-10-31; Welcome page Last-Modified
  2026-10-31T03:33:41Z, ETag 3Zr0CA1pp+fv62L067zSK/e1kVQ=-gzip; CDC page
  Last-Modified 2026-10-31T03:33:44Z, ETag WQqQO6K0X4jUTQRVuNbDk/Bvyn4=-gzip;
  canonical text 6,086 characters / 934 words and 23,581 / 3,591, SHA-256
  9391024f... and 9a4d986b...; living documentation, no pinned release.";
  verification_scope "Welcome and CDC task pages read for one-time versus
  ongoing replication, task types, checkpoint recovery and start-point limits;
  no DMS task run."

Add src.flyway-expand-contract:

- title "Rolling out updates from a single schema to multiple production
  databases"; observed_title "Rolling out updates from a single schema to
  multiple production databases - Redgate Flyway - Product Documentation";
  category delivery; publisher Redgate; kind official-docs; URL
  https://documentation.red-gate.com/x/NoJvF; resolved URL the page-ID URL above;
  topics schema-migration, expand-contract, compatibility; priority supporting;
  planned_use "Exact public Flyway expand/contract guidance for the online
  migration alternative."; admission
  admitted-for-research; access public-web-or-author-download; reading_status
  full-public-page-inspected; access_checked and content_verified 2026-10-31;
  version "Flyway fleet-rollout page, published 2026-05-12, last updated
  2026-08-18; fetched 2026-10-31; 62,417-byte HTML; no Last-Modified or ETag;
  canonical text 21,271 characters / 3,235 words, SHA-256 a85f51e8...";
  verification_scope "Full fleet-rollout page read for the expand/contract
  section, immutable applied changes and sequential rollout; no Flyway run."

Reconcile src.m9-st01:

- admission admitted-for-research; reading_status full-public-page-inspected;
  access_checked and content_verified 2026-10-31; version "Online migrations at
  scale, Jacqueline Xu, Stripe, published 2017-02-02; fetched 2026-10-31;
  411,763- and 399,214-byte HTML; no Last-Modified or ETag; raw HTML differs
  between fetches in dynamic markup; canonical article text 11,056 characters /
  1,801 words, SHA-256 f55df9dd...; observed_title Online migrations at scale.";
  verification_scope "Full article read for the four-step dual-write pattern,
  read-path comparison, offline backfill and retirement; no Stripe system
  observed."

Extend src.postgresql:

- append to version "PostgreSQL 18.6 pg_dump and COPY pages fetched 2026-10-31;
  pg_dump 89,919-byte HTML, canonical text 41,961 characters / 6,578 words,
  SHA-256 3ea3630d...; COPY 62,490-byte HTML, canonical text 28,697 / 4,956,
  SHA-256 ed656bab...; no Last-Modified or ETag on either."
- append to verification_scope "pg_dump and COPY pages read on 2026-10-31 for
  consistent exports, the serializable-deferrable caveat, positional COPY
  mapping, failed-COPY residue and interrupted restore; no dump, restore or COPY
  executed."

### Reading ledger edition/patterns/reading-ledger.v1.json

Add six records. All use access_date 2026-10-31, reviewer "Automated authoring
agent" and status "read".

- read.stripe-online-migrations.2026-10-31
  - source: src.m9-st01
  - unit_url: https://stripe.com/blog/online-migrations
  - unit_label: Online migrations at scale — Stripe engineering article
  - unit_type: engineering-article
  - sections_read: A pattern for online migrations; Part 1: Dual writing;
    Part 2: Changing all read paths; Part 3: Changing all write paths;
    Part 4: Removing old data; Conclusion
  - sections_not_read: linked pages; images; unrelated site chrome
  - content_sha256: f55df9ddac4a2b47514a9570da5f9a5f3d1f09145af5d865bcca6704fbad9519
  - characters/words: 11,056 / 1,801
  - claims_supported: Q1-Q8
  - claims_not_supported: benchmark; production observation; atomic cross-store
    transaction; current Stripe architecture
  - limitations: 2017 engineering article about one migration; not a formal
    guarantee; raw HTML varies between fetches, canonical text does not.
- read.postgres-pgdump.2026-10-31
  - source: src.postgresql
  - unit_url: https://www.postgresql.org/docs/current/app-pgdump.html
  - unit_label: PostgreSQL 18.6 pg_dump
  - unit_type: documentation-page
  - sections_read: Description; Options; Notes; Examples; Diagnostics
  - sections_not_read: linked pages; PostgreSQL source code
  - content_sha256: 3ea3630d2df755269048563c7468de0bb9f4b98d17f924e436d38dfe46820fdf
  - characters/words: 41,961 / 6,578
  - claims_supported: Q9-Q13
  - claims_not_supported: dump execution; restore execution; benchmark
  - limitations: utility documentation; no concurrent dump or restore run.
- read.postgres-copy.2026-10-31
  - source: src.postgresql
  - unit_url: https://www.postgresql.org/docs/current/sql-copy.html
  - unit_label: PostgreSQL 18.6 COPY
  - unit_type: documentation-page
  - sections_read: Description; Parameters; Outputs; Notes; File Formats;
    Examples; Compatibility
  - sections_not_read: linked pages; PostgreSQL source code
  - content_sha256: ed656babcaf6d93cb64b4514ad9259da08988cb71d08ddfaa7823605a56ddc4c
  - characters/words: 28,697 / 4,956
  - claims_supported: Q14-Q18
  - claims_not_supported: COPY execution; trigger or constraint test; benchmark
  - limitations: command documentation; no failure or retry exercise.
- read.aws-dms-overview.2026-10-31
  - source: src.aws-dms
  - unit_url: https://docs.aws.amazon.com/dms/latest/userguide/Welcome.md
  - unit_label: AWS DMS User Guide — What is AWS DMS?
  - unit_type: documentation-page
  - sections_read: full page
  - sections_not_read: linked pages; images; PDF rendering
  - content_sha256: 9391024f929dea3d8824ab956e9c20749dea9bdf865b9ee02d033b08c695dcc0
  - characters/words: 6,086 / 934
  - claims_supported: Q19-Q20
  - claims_not_supported: DMS task execution; benchmark; SLA
  - limitations: living service guide; no pinned release.
- read.aws-dms-cdc.2026-10-31
  - source: src.aws-dms
  - unit_url: https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Task.CDC.md
  - unit_label: AWS DMS User Guide — Creating tasks for ongoing replication
  - unit_type: documentation-page
  - sections_read: full page, including checkpoint and start-point sections
  - sections_not_read: linked endpoint pages; images; PDF rendering
  - content_sha256: 9a4d986bbef7aaff8385f6ed6c0bbc51b12cfbdbd4e2154f7f368c9e78380918
  - characters/words: 23,581 / 3,591
  - claims_supported: Q21-Q26
  - claims_not_supported: task recovery execution; benchmark; end-to-end
    exactly-once
  - limitations: living guide; recovery behavior is documented, not tested.
- read.flyway-expand-contract.2026-10-31
  - source: src.flyway-expand-contract
  - unit_url: https://documentation.red-gate.com/x/NoJvF
  - unit_label: Flyway fleet rollout — expand/contract guidance
  - unit_type: documentation-page
  - sections_read: full page, including Core principles and
    Backward-compatible changes (expand/contract)
  - sections_not_read: linked tutorials; images
  - content_sha256: a85f51e81ffce1075853639f07d6e3661f8d98f939e8b5478c87f26a4777ea6f
  - characters/words: 21,271 / 3,235
  - claims_supported: Q27-Q31
  - claims_not_supported: Flyway execution; data migration run; benchmark
  - limitations: current Flyway fleet-rollout documentation; no page titled
    Expand-Contract; this page supplies the exact section.

### Source plan edition/patterns/source-plan.v1.json

Replace the required_units array for tycho.pattern.online-data-migration with
the six units below. Retain the existing gh-ost unit only as a historical
auxiliary if the schema permits; otherwise record it in the entry notes.

    [
      {
        "source_id": "src.m9-st01",
        "unit": "Online migrations at scale — Stripe engineering article",
        "unit_type": "engineering-article",
        "url": "https://stripe.com/blog/online-migrations",
        "sections": ["A pattern for online migrations", "Part 1: Dual writing",
                     "Part 2: Changing all read paths",
                     "Part 3: Changing all write paths",
                     "Part 4: Removing old data", "Conclusion"],
        "status": "read",
        "read_record_id": "read.stripe-online-migrations.2026-10-31",
        "blocked_reason": null
      },
      {
        "source_id": "src.postgresql",
        "unit": "PostgreSQL 18.6 pg_dump",
        "unit_type": "documentation-page",
        "url": "https://www.postgresql.org/docs/current/app-pgdump.html",
        "sections": ["Description", "Options", "Notes", "Examples"],
        "status": "read",
        "read_record_id": "read.postgres-pgdump.2026-10-31",
        "blocked_reason": null
      },
      {
        "source_id": "src.postgresql",
        "unit": "PostgreSQL 18.6 COPY",
        "unit_type": "documentation-page",
        "url": "https://www.postgresql.org/docs/current/sql-copy.html",
        "sections": ["Description", "Parameters", "Notes", "File Formats"],
        "status": "read",
        "read_record_id": "read.postgres-copy.2026-10-31",
        "blocked_reason": null
      },
      {
        "source_id": "src.aws-dms",
        "unit": "AWS DMS User Guide — What is AWS DMS?",
        "unit_type": "documentation-page",
        "url": "https://docs.aws.amazon.com/dms/latest/userguide/Welcome.md",
        "sections": ["What is AWS Database Migration Service?",
                     "Migration tasks that AWS DMS performs"],
        "status": "read",
        "read_record_id": "read.aws-dms-overview.2026-10-31",
        "blocked_reason": null
      },
      {
        "source_id": "src.aws-dms",
        "unit": "AWS DMS User Guide — Creating tasks for ongoing replication",
        "unit_type": "documentation-page",
        "url": "https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Task.CDC.md",
        "sections": ["Creating tasks for ongoing replication using AWS DMS",
                     "Using a checkpoint as a CDC start point"],
        "status": "read",
        "read_record_id": "read.aws-dms-cdc.2026-10-31",
        "blocked_reason": null
      },
      {
        "source_id": "src.flyway-expand-contract",
        "unit": "Flyway fleet rollout — expand/contract guidance",
        "unit_type": "documentation-page",
        "url": "https://documentation.red-gate.com/x/NoJvF",
        "sections": ["Core principles",
                     "Backward-compatible changes (expand/contract)"],
        "status": "read",
        "read_record_id": "read.flyway-expand-contract.2026-10-31",
        "blocked_reason": null
      }
    ]

Proposed notes: "Four public sources (six pages) bound 2026-10-31: Stripe's
dual-write article; PostgreSQL 18.6 pg_dump and COPY; the AWS DMS User Guide
overview and CDC task pages; and Flyway's fleet-rollout expand/contract section.
The invariant is an application-level consistency rule, the DMS checkpoint is
cached rather than per-commit, and a changed mapping remains an untested Tycho
hazard."

### Owner units edition/patterns/owner-units.v1.json

Keep the document id, path, heading, anchor and level; update owner.line from
215 to 223. Keep unit_kind dedicated. Consider unit_terms ["online migration",
"dual writing", "checkpoint", "stop-the-world"].

Technical evidence:

- mechanism: state supported. Claim quote: "An online migration copies or
  transforms data while the source continues serving writes. If backfill takes
  hours, it may read records while new writes occur. A design needs an
  authoritative writer and a change-capture/reconciliation plan." Reason:
  Stripe describes dual writing and offline backfill; PostgreSQL documents
  consistent exports and COPY; AWS DMS documents full-load plus CDC. Primary
  binding: Q2, read.stripe-online-migrations.2026-10-31, section "A pattern for
  online migrations", revision f55df9dd.... Supporting: Q1, Q6, Q14, Q19 and
  Q21-Q22. Tycho reading: a copy plus change stream plus reconciliation
  boundary, not one distributed transaction.
- invariant: state supported. Claim quote: "Two independent writers are not
  automatically atomic just because the schema includes both fields." Reason:
  Stripe requires both stores to be written and compares read paths; it does
  not claim an atomic cross-store commit. PostgreSQL distinguishes a consistent
  export from serial execution history and defines positional COPY mapping.
  Primary binding: Q4, read.stripe-online-migrations.2026-10-31, section
  "Part 3: Changing all write paths", revision f55df9dd.... Supporting: Q2-Q3,
  Q5, Q9, Q11 and Q15. Tycho rule: one authoritative writer or an idempotent
  reconciled projection; mapping revisions must be single-valued.
- failure_recovery: state supported (narrowed). Claim quote: "A crash can leave
  a checkpoint behind the last committed row; a changed mapping can strand a
  subset." Reason: DMS caches a checkpoint from time to time and can recover a
  failed task from it; DMS captures transactions that started after the chosen
  start point; failed COPY leaves deleted-row residue; an interrupted restore
  can leave catalogs in the wrong state. Primary binding: Q23,
  read.aws-dms-cdc.2026-10-31, section "Using a checkpoint as a CDC start
  point", revision 9a4d986b.... Supporting: Q7-Q8, Q12-Q13, Q16-Q18,
  Q24-Q26 and Q28. Narrowing: no selected unit tests a changed business-key
  mapping; Q28 is related delivery discipline, not a mapping test.
- alternative: state supported. Claim quote: "A stop-the-world export/restore is
  the simplest alternative when a maintenance window is acceptable." Reason:
  PostgreSQL documents consistent export and bulk load; Flyway documents the
  expand/contract sequence; AWS DMS documents managed full-load plus CDC; Stripe
  documents dual writing. Primary binding: Q27,
  read.flyway-expand-contract.2026-10-31, section "Core principles", revision
  a85f51e8.... Supporting: Q9-Q10, Q14, Q19, Q22, Q30-Q31 and Q1-Q2. Tycho
  choice rule: reverse when the changed-row set is small or capture, checkpoint
  and reconciliation cannot be operated.

Other owner-units fields:

- technical_coverage "sufficient"; decision_coverage "sufficient";
  review_state "self-checked".
- notes: "Four dimensions bound 2026-10-31 to Stripe, PostgreSQL 18.6 pg_dump
  and COPY, the AWS DMS User Guide and Flyway expand/contract guidance; the
  invariant is application-level, the checkpoint is cached rather than
  per-commit, and a changed mapping remains an untested Tycho hazard; coverage
  is self-checked, not independently reviewed."
- source_support: primary ledger_record read.stripe-online-migrations.2026-10-31,
  source_id src.m9-st01, unit_type engineering-article, status read,
  card_citation true; auxiliary entries for read.postgres-pgdump.2026-10-31,
  read.postgres-copy.2026-10-31, read.aws-dms-overview.2026-10-31,
  read.aws-dms-cdc.2026-10-31 and read.flyway-expand-contract.2026-10-31;
  retain read.batch3-gh-ost.2026-10-21 as historical.
- decision_evidence.competing_alternative: "Stop-the-world export/restore
  (pg_dump plus COPY), Flyway expand/contract, AWS DMS full-load plus CDC, or
  Stripe-style dual-write with verification. Reverse when the changed-row set is
  small or capture, checkpoint and reconciliation cannot be operated.";
  decision_state applicable-under-conditions; card_components 10;
  atlas_section online-data-migration.

### Registry, card batches and derived artifacts

The registry currently records technical_owner.state partial,
atlas_owner.state partial-bounded and coverage partial. After the owner-units
proposal is applied, regenerate those fields from owner-units rather than editing
them by hand. The proposed state is technical_owner.state sufficient,
atlas_owner.state sufficient and coverage technical/decision/overall sufficient,
confidence high. source_units should list the six units above plus the retained
gh-ost record as historical. The registry notes should say the four dimensions
are self-checked and promotion is not part of this lane.

card-batches.v1.json needs no card_path; the card remains inline in V11/C06.
edition/atlas-manifest.json and generated indexes should be regenerated by the
integrator after the owner and card hashes are final. This lane does not claim
that regeneration.

## Verification

Commands run in /Users/rbaranov/Projects/tycho-worktrees/b63-online-migration:

- python3 scripts/check_markdown_line_length.py
  Result: PASS: V11 prose <=100; 145 exact owner-link exceptions.
- python3 scripts/check_boundary.py
  Result: PASS: configured lexical boundary checks; independent-origin review
  still required.
- Added-line length scan: 75 added owner lines and 34 added card lines; none
  exceeds 100 characters.
- Quote check: 31 named passages checked against the six canonical
  representations; 31/31 present.
- git status: exactly three paths, the owner page, the V11/C06 landing and
  this note.
- No shared JSON, generated index, promotion record, review report or test file
  is changed.

No full unit suite was run. The lane is a content slice; the batch-end suite is
the integrator's step.

## Limits

- Coverage and review are self-checked. No independent AI review, owner
  acceptance, promotion, CI result or production observation is claimed.
- The changed business-key mapping remains a Tycho hazard; no selected unit
  evaluates it.
- The stop-the-world quiesce/export/load/verify procedure is a Tycho operating
  shape, not a documented PostgreSQL procedure.
- Stripe is a 2017 engineering article about one migration; it is not a formal
  atomicity guarantee or a current system description.
- PostgreSQL, AWS DMS and Flyway pages are living documentation. The recorded
  hashes pin the fetched representations, not future revisions.
- The Flyway task brief says "Flyway expand-contract"; the exact public Flyway
  page used here is the fleet-rollout page whose section defines expand/contract.
  No page titled "Expand-Contract" exists in the current Flyway documentation.
- No runtime exercise, benchmark, restore, DMS task, Flyway run or database
  operation was performed.
