# B49 — Expand-and-Contract four-dimension lane

Status: lane-local book edit, self-checked on 2026-10-31. No shared edition
metadata, promotion, generated artifact or owner acceptance is included. The
entry was 0/4 at the parent HEAD: zero dimensions supported and all four
`partial`. This lane binds all four dimensions to public sources and labels the
compatibility invariant, the held-window failure handling, the choice rule and
the reading of the engine evidence as Tycho. The card remains inline in V11/C10.

## Lane coordinates

- Parent HEAD: `6ff2546cc57c2f670744fe1dbcaf875a2a01e311` (`6ff2546c`).
- Branch: `b49-expand-contract`; worktree:
  `/Users/rbaranov/Projects/tycho-worktrees/b49-expand-contract`.
- Scope: the owner section `### Expand-and-Contract` in the V08/C05 page and
  the inline V11/C10 card `### Expand-and-Contract`. Single-entry lane; no
  other entry, shared JSON, promotion or generated file is changed.
- Owner path (concatenate):

      book/volumes/v08-delivery-deployment-and-recovery/
      c05-backward-compatible-database-change/reader-writer-matrix.md

- Card path:
  `book/volumes/v11-pattern-atlas/c10-deployment-modernization/README.md`.
- Exactly three files change: the owner page, the inline card and this note.
  No shared JSON file is edited.
- The task brief named V11/C06 or C04 for the inline card. The registered
  `tycho.pattern.expand-and-contract` card is in V11/C10 (deployment and legacy
  modernization); V11/C06 owns the sibling `expand-and-contract-schema` entry.
  This lane edits the registered `expand-and-contract` card in V11/C10 and does
  not touch C06 or C04.
- Existing source ids: `src.aws-blue-green-deployments` (already in the card),
  `src.postgresql` and `src.mysql`. The Fowler unit needs a new source id,
  `src.fowler-parallel-change`, which is proposed here but not added to the
  shared register.
- New ledger records proposed: `read.fowler-parallel-change.2026-10-31`,
  `read.postgresql-alter-table.2026-10-31`,
  `read.postgresql-explicit-locking.2026-10-31`,
  `read.mysql-online-ddl.2026-10-31` and
  `read.mysql-alter-table.2026-10-31`.
- Retained record reused byte-for-byte:
  `read.aws-blue-green-data.2026-10-30`.
- Baseline line-length and boundary checks pass before and after the edit.

## Baseline and gap

`edition/patterns/owner-units.v1.json` records all four dimensions as
`partial`: mechanism, invariant, failure/recovery and alternative. The
`technical_coverage` is `partial` and `decision_coverage` is
`partial-bounded`. The recorded reasons are respectively:

- mechanism: "Flyway page has no expand/migrate/contract phases."
- invariant: "Flyway has no old-reader/new-writer invariant."
- failure/recovery: "Flyway has no forward-repair or incompatible-write
  recovery."
- alternative: "Flyway Undo is not a big-bang/parallel-run alternative."

The existing `read.batch3-flyway.2026-10-21` record supports ordered migrations
and the statement that expand-and-contract requires compatible schema steps and
deployment sequencing beyond migration tooling. It does not define the phases,
the reader/writer invariant, forward repair or the alternative set. The entry's
`source_support` therefore names Flyway only.

The base owner page has SHA-256
`053ad0001c32bcd5a85f862ed801f5c2cd39295da90e31b5f3fad963ff0ada7c`. This is
the same `page_sha256` recorded in the candidate review record for this entry,
so the baseline is the reviewed representation. The edited page has a different
hash; the independent review is outstanding and must be re-run after
integration. The base card has SHA-256
`15b22acf27f975da66edc49cb562069190d04ee4cf07e9e3e50babf76221b88e`.

The gap was evidential and editorial. The owner section already stated the
protocol in general terms, but no exact public quote, revision and
representation hash were bound to the four dimensions. The shared metadata
still shows 0/4 until an integrator applies the proposals below.

## Candidate evaluation

- Danilo Sato, "Parallel Change," martinfowler.com (selected). Defines the
  three phases, the continue-the-old-version rule, the unexecuted-contract
  downside, the explicit-versioning alternative and the branch-by-abstraction
  comparison.
- AWS, "Best Practices for Managing Data Synchronization and Schema Changes"
  (selected). Binds schema-first and schema-last deployment, backward
  compatibility of database updates, additive versus deletive changes, the
  rollback dependency on current blue data and the risk of a deletive cutover.
- PostgreSQL 18.6, "ALTER TABLE" and "Explicit Locking" (selected). Binds the
  ACCESS EXCLUSIVE default, the lock-until-transaction-end rule, the volatile
  default rewrite, the volatile rewrite's MVCC hazard and the logical
  `DROP COLUMN` behaviour.
- MySQL 8.4 Reference Manual, "Online DDL Operations" and "ALTER TABLE"
  (selected). Binds instant add/drop, the type-change COPY-only limit, the
  row-version cap and COPY/INPLACE fallback, and the COPY/INPLACE/INSTANT
  concurrent-DML differences.
- Flyway, "Migrations" (retained, not selected for the four dimensions). It
  supports migration ordering and tooling boundaries but not the phases,
  invariant, recovery or alternatives.
- gh-ost and the GCP Spanner cutover page were not read as units for this lane
  and are not used as support. They are tool- and product-specific migration
  mechanisms, not a general compatibility protocol.
- No origin claim is made. This lane reads current public documentation and
  articles; it does not establish an independent implementation, benchmark or
  production observation.

## Source binding

Quotes reproduce the served prose. Line breaks inside a quote are editorial
wrapping. The binding revision is the canonical-text SHA-256 shown for each new
record, or the retained record's `content_sha256` for AWS. Quoted fragments were
checked as whitespace-normalized substrings of the named representation on
2026-10-31; curly quotes and link-extraction spaces before punctuation were
normalized. The Tycho-labelled sentences are not presented as source quotes.

### Danilo Sato — Parallel Change

- Source id: `src.fowler-parallel-change` (proposed; not yet admitted).
- Proposed record: `read.fowler-parallel-change.2026-10-31`.
- URL: `https://martinfowler.com/bliki/ParallelChange.html`.
- Unit label: "Parallel Change — martinfowler.com bliki"; unit type
  `article`; published 2014-05-13; access date 2026-10-31.
- Representation: HTTP 200 on 2026-10-31T14:01:40Z; 22,616 bytes;
  Last-Modified 2026-10-29T16:11:21Z; ETag `"5858-65efcee2d9c40"`; raw HTML
  SHA-256 `4d958f564dc7e44e12b4233202d20cdadd1e0ba30a9ccfc0517d1a568f6d8bcc`;
  canonical text 7,879 characters and 1,268 words, SHA-256
  `af2cd77b9048f39fdee984b371305ecc362f236d485a21ff02008a65787dfed7`.
- Sections used: the article body, including the Grid example, the
  database-refactoring paragraph, the remote-API paragraph, the
  branch-by-abstraction paragraph and the downside paragraph.
- Exact quotes:

      Parallel change, also known as expand and contract, is a pattern to
      implement backward-incompatible changes to an interface in a safe manner,
      by breaking the change into three distinct phases: expand, migrate, and
      contract.

      In the expand phase you augment the interface to support both the old and
      the new versions.

      During the migrate phase you update all clients using the old version to
      the new version.

      Once all usages have been migrated to the new version, you perform the
      contract phase to remove the old version and change the interface so that
      it only supports the new version.

      Existing clients will continue to consume the old version, and the new
      changes can be introduced incrementally without affecting them.

      The downside of using parallel change is that during the migrate phase the
      supplier has to support two different versions, and clients could get
      confused about which version is new versus old.

      If the contract phase is not executed you might end up in a worse state
      than you started, therefore you need discipline to finish the transition
      successfully.

      This is an alternative to using an explicit version in the exposed API.

      However, when you have a large number of clients, using branch by
      abstraction is a better strategy to narrow the surface of change and
      reduce confusion during the migrate phase.

- Limits: living bliki article with no version selector; one author's article;
  no database engine was exercised; the article's examples are not reproduced.
  The quote beginning "Parallel change, also known as..." is the fetched text
  with the link-extraction space before the comma normalized.

### AWS — Blue/Green Deployments on AWS, data and schema section

- Source id: `src.aws-blue-green-deployments` (existing, admitted).
- Retained record: `read.aws-blue-green-data.2026-10-30`.
- URL (concatenate):

      https://docs.aws.amazon.com/whitepapers/latest/blue-green-deployments/
      best-practices-for-managing-data-synchronization-and-schema-changes.html

- Unit label: "Best Practices for Managing Data Synchronization and Schema
  Changes — Blue/Green Deployments on AWS"; unit type `documentation-page`;
  access date 2026-10-30 (retained), re-fetched 2026-10-31.
- Representation: HTTP 200 on 2026-10-31T14:01:41Z; 18,886 bytes;
  Last-Modified 2026-10-30T22:43:40Z; ETag
  `"6f77fJBpTRQ6FW+4n93f1lUXzig="`; raw HTML SHA-256
  `07eaa6ff45ca86872f743c07deb17577761f1216e04a840de89ae9c5bfa99442`,
  byte-identical to the retained record; canonical text 4,363 characters and
  677 words, SHA-256
  `6cc6f620bb867f4200ea0323fd939a0925bae30266c715b2ed1e73168a40ee41`, which
  matches the existing register entry.
- Sections used: "Best Practices for Managing Data Synchronization and Schema
  Changes"; "Decoupling Schema Changes from Code Changes".
- Exact quotes:

      A general recommendation is to decouple schema changes from the code
      changes.

      The schema is changed first, before the blue/green code deployment.
      Database updates must be backward compatible, so the old version of the
      application can still interact with the data.

      Schema modifications in the first approach are often additive.

      It's important to follow coding best practices when developing
      applications to ensure your application can tolerate the presence of
      additional fields in existing tables, even if they are not used.

      The schema is changed last, after the blue/green code deployment. Code
      changes in the new version of the application must be backward compatible
      with the old schema.

      Schema modifications in the second approach are often deletive.

      After this removal, the earlier application version is no longer
      operational.

      There's an increased risk involved when managing schema with a deletive
      approach: failures in the schema modification process can impact your
      production environment.

      The blue environment needs up-to-date data in the event of a rollback,
      when production is either shifts back or remains on the blue environment.

- Limits: the whitepaper page is marked "for historical reference only"; it is
  AWS-specific and does not test a schema change, a deployment or a rollback.
  The awkward "is either shifts back" wording is in the served text and is
  retained only if quoted; the owner page does not quote that sentence.

### PostgreSQL 18.6 — ALTER TABLE

- Source id: `src.postgresql` (existing).
- Proposed record: `read.postgresql-alter-table.2026-10-31`.
- URL: `https://www.postgresql.org/docs/current/sql-altertable.html`.
- Unit label: "PostgreSQL 18.6 Documentation — ALTER TABLE"; unit type
  `documentation-page`; access date 2026-10-31.
- Representation: HTTP/2 200 on 2026-10-31T11:07:55Z; 102,234 bytes; no
  Last-Modified or ETag served; raw HTML SHA-256
  `d9f4df96a79a07b39a58a6820c8ed5753d8dd80bd7b60bddb0f31525591f1a76`;
  canonical text 51,194 characters and 8,669 words, SHA-256
  `2f8630304b6159e52681a0d9502a1d09b497da7ffb8918b86c0ebf4d76003924`.
- Sections used: "Description", "Notes", and the examples for adding and
  dropping a column.
- Exact quotes:

      ALTER TABLE changes the definition of an existing table. There are
      several subforms described below. Note that the lock level required may
      differ for each subform. An ACCESS EXCLUSIVE lock is acquired unless
      explicitly noted.

      When multiple subcommands are given, the lock acquired will be the
      strictest one required by any subcommand.

      When a column is added with ADD COLUMN and a non-volatile DEFAULT is
      specified, the default value is evaluated at the time of the statement and
      the result stored in the table's metadata, where it will be returned when
      any existing rows are accessed. The value will be only applied when the
      table is rewritten, making the ALTER TABLE very fast even on large tables.
      If no column constraints are specified, NULL is used as the DEFAULT. In
      neither case is a rewrite of the table required.

      Adding a column with a volatile DEFAULT (e.g., clock_timestamp() ), a
      stored generated column, an identity column, or a column with a domain
      data type that has constraints will cause the entire table and its
      indexes to be rewritten.

      The DROP COLUMN form does not physically remove the column, but simply
      makes it invisible to SQL operations.

      The rewriting forms of ALTER TABLE are not MVCC-safe. After a table
      rewrite, the table will appear empty to concurrent transactions, if they
      are using a snapshot taken before the rewrite occurred.

      Table and/or index rebuilds may take a significant amount of time for a
      large table, and will temporarily require as much as double the disk
      space.

- Limits: rolling "current" documentation, identified here as 18.6 by the
  served footer; no PostgreSQL instance was run and no schema change was
  executed. Lock level can differ by subform; the default ACCESS EXCLUSIVE rule
  is not a statement about every ALTER TABLE form. The page does not prescribe
  expand-and-contract phases.

### PostgreSQL 18.6 — Explicit Locking

- Source id: `src.postgresql` (existing).
- Proposed record: `read.postgresql-explicit-locking.2026-10-31`.
- URL: `https://www.postgresql.org/docs/current/explicit-locking.html`.
- Unit label: "PostgreSQL 18.6 Documentation — Explicit Locking"; unit type
  `documentation-page`; access date 2026-10-31.
- Representation: HTTP/2 200 on 2026-10-31T12:36:21Z; 46,826 bytes; no
  Last-Modified or ETag served; raw HTML SHA-256
  `88b12e1ceb015e5cd9326e6b43a6f5b6160c3970f19416e5160522da611274cb`;
  canonical text 17,232 characters and 2,931 words, SHA-256
  `defdd38bf3d5aeaa3174012e51c6e02c56cb76e1153fc21da8c5ffcb42646e23`.
- Sections used: "13.3.1. Table-Level Locks", including the ACCESS EXCLUSIVE
  definition and the lock-duration paragraph.
- Exact quotes:

      ACCESS EXCLUSIVE ( AccessExclusiveLock ) Conflicts with locks of all
      modes ( ACCESS SHARE , ROW SHARE , ROW EXCLUSIVE , SHARE UPDATE EXCLUSIVE
      , SHARE , SHARE ROW EXCLUSIVE , EXCLUSIVE , and ACCESS EXCLUSIVE ).

      Many forms of ALTER INDEX and ALTER TABLE also acquire a lock at this
      level.

      Once acquired, a lock is normally held until the end of the transaction.

- Limits: one documentation section; no lock was observed and no transaction
  was run. The page describes PostgreSQL's lock manager, not a deployment
  procedure.

### MySQL 8.4 — Online DDL Operations

- Source id: `src.mysql` (existing).
- Proposed record: `read.mysql-online-ddl.2026-10-31`.
- Canonical URL:
  `https://dev.mysql.com/doc/refman/8.4/en/innodb-online-ddl-operations.html`;
  that host returned HTTP 403 to this lane on 2026-10-31.
- Representation URL:
  `https://docs.oracle.com/cd/E17952_01/mysql-8.4-en/innodb-online-ddl-operations.html`.
- Unit label: "MySQL 8.4 Reference Manual — 17.12.1 Online DDL Operations";
  unit type `documentation-page`; access date 2026-10-31.
- Representation: HTTP/2 200 on 2026-10-31T14:02:20Z; 86,823 bytes; no
  Last-Modified; ETag
  `"92922c7d72a1485d6da8814ab0be4914:1777984310.111838"`; raw HTML SHA-256
  `aa0f53d803220d1745b029c1a75639281096982087d08bf9b6f32d342f42b6ae`;
  canonical text 30,947 characters and 4,728 words, SHA-256
  `6f7b0113f99388ab4a29f9016a05fedb46b86277174162fe4bc5cbca295de3de`.
- Sections used: "Column Operations", including the support table for adding,
  dropping and changing a column; "Adding a column"; "Dropping a column";
  "Changing the column data type".
- Exact quotes:

      Adding a column Yes* Yes No* Yes* Yes

      Dropping a column Yes* Yes Yes Yes Yes

      Changing the column data type No No Yes No No

      INSTANT is the default algorithm in MySQL 8.4.

      Changing the column data type is only supported with ALGORITHM=COPY.

      The maximum number of row versions permitted is 64 (255 as of MySQL
      9.1.0), as each row version requires additional space for table metadata.

      When the row version limit is reached, ADD COLUMN and DROP COLUMN
      operations using ALGORITHM=INSTANT are rejected with an error message that
      recommends rebuilding the table using the COPY or INPLACE algorithm.

      A column with a functional index cannot be dropped using the INSTANT
      algorithm.

      The table is rebuilt if ALGORITHM=INPLACE is used to add a column.

- Limits: the three table rows are quoted as table cells, not prose; they are
  meaningful only with the page's column headings. The manual describes
  operations, not a migration plan. No MySQL server was run and no ALTER TABLE
  was executed. The Oracle-hosted manual copy is used as the representation
  because the canonical host blocked automated retrieval; the digest pins this
  copy.

### MySQL 8.4 — ALTER TABLE

- Source id: `src.mysql` (existing).
- Proposed record: `read.mysql-alter-table.2026-10-31`.
- Canonical URL: `https://dev.mysql.com/doc/refman/8.4/en/alter-table.html`;
  that host returned HTTP 403 to this lane on 2026-10-31.
- Representation URL:
  `https://docs.oracle.com/cd/E17952_01/mysql-8.4-en/alter-table.html`.
- Unit label: "MySQL 8.4 Reference Manual — ALTER TABLE"; unit type
  `documentation-page`; access date 2026-10-31.
- Representation: HTTP/2 200 on 2026-10-31T14:02:20Z; 109,740 bytes; no
  Last-Modified; ETag
  `"bf95c7de5c876800a74caa7bca15fde8:1777984295.275"`; raw HTML SHA-256
  `942e4f1e5eee59463efa1a0a1d8276ef2579c228b3b3f99cb1b10acfe028f1e6`;
  canonical text 46,542 characters and 7,609 words, SHA-256
  `d47cb8ed8933e515b8ec2771583aeea9916741840eb45704c2a5235a9c5d92f2`.
- Sections used: "Performance and Space Requirements", specifically the COPY,
  INPLACE and INSTANT algorithm definitions and the default-algorithm
  paragraph.
- Exact quotes:

      ALTER TABLE operations are processed using one of the following
      algorithms:

      COPY : Operations are performed on a copy of the original table, and
      table data is copied from the original table to the new table row by row.
      Concurrent DML is not permitted.

      INPLACE : Operations avoid copying table data but may rebuild the table in
      place. An exclusive metadata lock on the table may be taken briefly during
      preparation and execution phases of the operation. Typically, concurrent
      DML is supported.

      INSTANT : Operations only modify metadata in the data dictionary. An
      exclusive metadata lock on the table may be taken briefly during the
      execution phase of the operation. Table data is unaffected, making
      operations instantaneous. Concurrent DML is permitted.

      If the ALGORITHM clause is omitted, MySQL uses ALGORITHM=INSTANT for
      storage engines and ALTER TABLE clauses that support it. Otherwise,
      ALGORITHM=INPLACE is used. If ALGORITHM=INPLACE is not supported,
      ALGORITHM=COPY is used.

- Limits: one manual page; algorithm availability depends on storage engine,
  version and operation. No server was run and no timing was measured.

## Dimension binding

The owner-unit quote for each dimension is preserved verbatim at the start of
the corresponding paragraph. The proposed state for
`tycho.pattern.expand-and-contract` is all four dimensions `supported`;
`technical_coverage` becomes `partial-bounded` and `decision_coverage` remains
`partial-bounded`. No `sufficient` claim is made.

- mechanism: "Expand-and-contract is a rollout protocol, not a schema diagram:
  each phase must remain compatible with readers still running the previous
  version, and the contract phase is gated by observed reader absence." Reason:
  Fowler's expand, migrate and contract phases; AWS's schema-first and
  schema-last ordering; PostgreSQL's ACCESS EXCLUSIVE default and lock duration;
  MySQL's instant add/drop and COPY-only type change.
- invariant: "New writers must preserve enough old representation for old
  supported readers until a verified cutover." Reason: Fowler's "Existing
  clients will continue to consume the old version"; AWS's backward-compatible
  database updates and tolerate-additional-fields rule; PostgreSQL's logical
  `DROP COLUMN` behaviour; MySQL's instant add/drop path is a table-copy saving,
  not a compatibility guarantee.
- failure_recovery: "Incompatible writes hold the rollout and may require
  forward repair rather than redeploying N." Reason: AWS's deletive-change risk
  and non-operational earlier version; PostgreSQL's volatile-default rewrite
  and non-MVCC-safe rewrite hazard; MySQL's row-version cap and COPY/INPLACE
  fallback. The recovery order (stop new-format writes, keep the expansion,
  reconcile and validate, restore old-reader service, repair forward) is Tycho's
  runbook, not a source procedure.
- alternative: "A big-bang migration, a parallel run or a versioned API cutover
  may be preferable when no mixed-version compatibility window is possible or
  the dataset is small enough to migrate under a verified pause." Reason:
  Fowler's explicit-versioning alternative and branch-by-abstraction comparison;
  MySQL's online DDL for a single compatible change versus COPY-only type
  change; Tycho's reversal condition.

Counter deltas if the four states move from `partial` to `supported`, derived
from the current `owner-units.v1.json` and not applied:

- mechanism 115 -> 116; invariant 80 -> 81; failure/recovery 74 -> 75;
  alternative 79 -> 80.
- technical partial 68 -> 67; technical partial-bounded 15 -> 16; sufficient
  stays 62; decision coverage stays 83 partial-bounded and 62 sufficient.

## Book edits

### Owner page

- Frontmatter: `evidence_scope.source_ids` adds
  `src.aws-blue-green-deployments`, `src.postgresql` and `src.mysql`;
  `evidence_scope.status` moves from `unknown` to `source-linked`; `updated_at`
  moves from 2026-10-20 to 2026-10-31. Other fields are unchanged. The Fowler
  source id is not added because it is not yet in the shared register; adding
  it would make the page metadata invalid.
- The four existing owner-unit sentences are preserved at the start of the
  mechanism, invariant, failure/recovery and alternative paragraphs.
- The section adds source-bound mechanism, invariant, failure/recovery and
  alternative paragraphs and a source-boundary list. It labels the synthesized
  invariant, runbook, choice rule and engine reading as Tycho.
- `### Expand-and-Contract` moves from 101 to 104 because of the three added
  source ids. `## Navigation, prerequisites and source scope` moves from 117 to
  215. The page grows from 126 to 224 lines.
- Every newly written line is <=100 characters. Pre-existing frontmatter,
  table, prose and navigation lines that already exceeded 100 are unchanged.
- Raw SHA-256:
  `efe87cc53859c786d9708f5094287cd77ba449593b0dbdcbd92e1dae1cef9a6c`.
- Base raw SHA-256:
  `053ad0001c32bcd5a85f862ed801f5c2cd39295da90e31b5f3fad963ff0ada7c`.

### V11/C10 inline card

- `evidence_scope.source_ids` adds `src.mysql` and `src.postgresql`;
  `src.aws-blue-green-deployments` and `src.flyway` were already declared.
- `updated_at` and `source_inspection_date` move from 2026-10-30 to 2026-10-31.
  The content review remains a historical self-check dated 2026-10-30.
- Good-fit conditions add additive/backward-compatible phases, a known DDL lock
  or rewrite budget, and a rollback or forward-repair path. Hard
  contraindications add a destructive rewrite with no window, a rollback that
  cannot restore the old schema and data, and unowned reader inventory.
- Competing alternative adds explicit API versioning, branch by abstraction and
  engine-native online DDL, with the Fowler and MySQL bounds. Failure and
  recovery adds deletive-change risk, non-MVCC-safe rewrites and the MySQL
  instant-version cap and COPY/INPLACE fallback.
- Sources adds the Fowler, AWS, PostgreSQL and MySQL records and the five
  proposed records; the retained Flyway record remains tooling context. The
  technical-owner link and gloss are unchanged.
- `### Expand-and-Contract` moves from 276 to 278 because of the two added
  source ids. `## Navigation and prerequisites` moves from 320 to 343. The
  chapter page grows from 336 to 359 lines.
- Raw SHA-256:
  `1102d84531eaec4c93cf701dc4e52f98771b62085465e035aa4e9ac5793d2580`.
- Base raw SHA-256:
  `15b22acf27f975da66edc49cb562069190d04ee4cf07e9e3e50babf76221b88e`.

No other book file is changed by this lane.

## Metadata needs (integrator)

The following changes are not in the lane commit. They are required before the
owner unit can move to 4/4 supported and before the atlas hash checks pass.

### Source register `sources/register.json`

Set `updated` to 2026-10-31; the source count moves from 306 to 307.

- Add `src.fowler-parallel-change`: title "Parallel Change"; URL
  `https://martinfowler.com/bliki/ParallelChange.html`; author Danilo Sato;
  published 2014-05-13; admission `admitted-for-research`; reading status
  `full-public-page-inspected`; access and content-verified dates 2026-10-31;
  version note with the 22,616-byte HTML, raw SHA-256
  `4d958f56...`, canonical text SHA-256 `af2cd77b...`, HTTP Date
  2026-10-31T14:01:40Z, Last-Modified 2026-10-29T16:11:21Z and ETag
  `"5858-65efcee2d9c40"`; license note "Public page; cite short excerpts and
  paraphrase; do not mirror."
- `src.postgresql`: set `access_checked` and `content_verified` to 2026-10-31.
  Append to `version`: ALTER TABLE canonical text
  `2f863030...` and Explicit Locking canonical text `defdd38b...`, both served
  2026-10-31 on PostgreSQL 18.6. Append to `verification_scope`: "ALTER TABLE
  and Explicit Locking were read on 2026-10-31 for the ACCESS EXCLUSIVE default,
  lock duration, volatile-default rewrite, DROP COLUMN visibility and MVCC
  rewrite hazard; no DDL was executed."
- `src.mysql`: set `reading_status` to `full-public-page-inspected` and
  `access_checked`/`content_verified` to 2026-10-31. Replace the placeholder
  `version` with "MySQL 8.4 Reference Manual; Online DDL Operations and ALTER
  TABLE read 2026-10-31 from the Oracle-hosted manual copy because the
  dev.mysql.com host returned HTTP 403; raw HTML SHA-256
  `aa0f53d8...` and `942e4f1e...`; canonical text SHA-256 `6f7b0113...` and
  `d47cb8ed...`; no Last-Modified; ETags recorded in the lane note." Append to
  `verification_scope`: "Online DDL Operations and ALTER TABLE were read on
  2026-10-31 for column-operation support, instant add/drop, type-change
  COPY-only behaviour, row-version limits and COPY/INPLACE/INSTANT concurrency;
  no server was run."
- `src.aws-blue-green-deployments`: no change. The 2026-10-31 raw HTML digest
  matches the retained record and the canonical digest matches the register.

### Reading ledger `edition/patterns/reading-ledger.v1.json`

Add five records; records move from 226 to 231. Each record is `status: read`,
`reviewer: "Automated authoring agent"`, and uses the URL, label, sections and
`content_sha256` below.

- `read.fowler-parallel-change.2026-10-31` — source
  `src.fowler-parallel-change`; label "Parallel Change — martinfowler.com
  bliki"; type `article`; sections equal to the article body; content SHA-256
  `af2cd77b...`; claims limited to the three phases, the old-client rule, the
  unexecuted-contract downside, explicit versioning and branch by abstraction.
- `read.postgresql-alter-table.2026-10-31` — source `src.postgresql`; label
  "PostgreSQL 18.6 Documentation — ALTER TABLE"; type `documentation-page`;
  sections "Description", "Notes" and the add/drop column examples; content
  SHA-256 `2f863030...`.
- `read.postgresql-explicit-locking.2026-10-31` — source `src.postgresql`;
  label "PostgreSQL 18.6 Documentation — Explicit Locking"; type
  `documentation-page`; section "13.3.1. Table-Level Locks"; content SHA-256
  `defdd38b...`.
- `read.mysql-online-ddl.2026-10-31` — source `src.mysql`; label "MySQL 8.4
  Reference Manual — 17.12.1 Online DDL Operations"; type
  `documentation-page`; sections "Column Operations", "Adding a column",
  "Dropping a column" and "Changing the column data type"; content SHA-256
  `6f7b0113...`.
- `read.mysql-alter-table.2026-10-31` — source `src.mysql`; label "MySQL 8.4
  Reference Manual — ALTER TABLE"; type `documentation-page`; section
  "Performance and Space Requirements"; content SHA-256 `d47cb8ed...`.

The retained `read.aws-blue-green-data.2026-10-30` record stays unchanged.

### Source plan `edition/patterns/source-plan.v1.json`

Append five units to `tycho.pattern.expand-and-contract` after the existing
Flyway unit, in this order: Fowler, AWS, PostgreSQL ALTER TABLE, PostgreSQL
Explicit Locking, MySQL Online DDL, MySQL ALTER TABLE. Set every unit `status`
to `read` and `blocked_reason` to `null`. Replace the entry notes with
"Mechanism, invariant, failure/recovery and alternative bound 2026-10-31 to
Fowler Parallel Change, AWS blue/green schema guidance, PostgreSQL 18.6 DDL
locking and MySQL 8.4 online DDL; no runtime test or sufficiency claim."

### Owner units `edition/patterns/owner-units.v1.json`

For `tycho.pattern.expand-and-contract`, set mechanism, invariant,
failure/recovery and alternative to `supported`; set `technical_coverage` to
`partial-bounded`; keep `decision_coverage` at `partial-bounded`. Keep the four
quoted sentences; add the proposed counts above. Update `notes` to name the
2026-10-31 binding and the engine boundary. Replace `source_support` with the
Fowler record as the primary citation and retain Flyway as supporting tooling
evidence, or keep Flyway and add the new records as supplementary; the
integrator should choose one representation and record it.

### Downstream metadata and review

Registry, card batches, coverage map, sufficient candidates, source plan
counters and the atlas manifest need their usual recomputation after the shared
records are added. The `sufficient-candidates.v1.json` review record for this
entry still carries `page_sha256`
`053ad0001c32bcd5a85f862ed801f5c2cd39295da90e31b5f3fad963ff0ada7c`, which no
longer matches the edited page. Re-run the independent review against the new
hash; the candidate status must not be treated as a pass for the edited text.

## Validation

- `python3 scripts/check_markdown_line_length.py`: PASS; 145 exact owner-link
  exceptions. The card's only long line is the existing `**Technical owner.**`
  exception.
- `python3 scripts/check_boundary.py`: PASS; independent-origin review is still
  required.
- Owner page: every newly written line is <=100 characters. Pre-existing long
  frontmatter, table, prose and navigation lines are unchanged.
- This note: every line is <=100 characters.
- Quotes: 42 quote blocks were checked as whitespace-normalized substrings of
  the six fetched representations; all 42 passed (the AWS concatenated URL is
  not a quote). The blocks include three MySQL table rows. Curly quotes,
  Markdown escapes and link-extraction spaces before punctuation were
  normalized.
- `git diff --check`: no whitespace errors.
- Links in the owner and card are unchanged; the card anchor remains
  `#expand-and-contract`. The technical-owner link still resolves to line 104
  of the owner page.
- `git diff --stat` reports two modified files before this note is added; the
  lane commit changes three files.
- Raw SHA-256 after the book edits:
  - owner page:
    `efe87cc53859c786d9708f5094287cd77ba449593b0dbdcbd92e1dae1cef9a6c`
  - card:
    `1102d84531eaec4c93cf701dc4e52f98771b62085465e035aa4e9ac5793d2580`

## Limits

- Shared metadata is not updated. The generated owner units, registry, source
  plan, ledger, card batches and indexes still show the entry as 0/4 or partial
  until an integrator applies the proposals above.
- No promotion, owner acceptance, coverage sufficiency or independent AI review
  is claimed. The book/atlas review gate remains outstanding, and the existing
  review hash is stale for the edited page.
- No benchmark, production observation, database run, DDL execution or runtime
  measurement is claimed.
- The Fowler page is a living bliki article with no version selector; AWS is a
  historical-reference whitepaper; PostgreSQL and MySQL documentation are
  rolling/current representations. Their hashes are the revision evidence, not
  release tags.
- The MySQL canonical host returned HTTP 403. The Oracle-hosted manual copy is
  the representation; a reviewer who requires the canonical host must re-fetch
  and compare it.
- The owner page is in V08, so the repository's line-length checker only covers
  the V11 card; the owner page was checked directly for new-line length.
- The card is in V11/C10, not the V11/C06 or C04 location named in the task
  brief; V11/C06 owns the separate `expand-and-contract-schema` entry.
