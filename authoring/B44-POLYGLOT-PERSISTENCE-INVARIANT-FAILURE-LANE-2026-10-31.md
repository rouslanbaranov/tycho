# B44 — Polyglot Persistence invariant and failure/recovery lane

Status: lane-local book edit, self-checked on 2026-10-31. No shared edition
metadata, promotion, generated artifact or owner acceptance is included. The
entry was 2/4 at the parent HEAD: mechanism and alternative were supported;
invariant and failure/recovery were partial. This lane binds both partial
dimensions to public AWS, Microsoft, Debezium and PostgreSQL pages and labels
the four-part invariant and recovery rules as Tycho. The card remains inline in
V11/C06.

## Lane coordinates

- Parent HEAD: `24e8edf7392efa6fde870579983cffb7f66e0159` (`24e8edf7`).
- Branch: `b44-polyglot`; worktree:
  `/Users/rbaranov/Projects/tycho-worktrees/b44-polyglot`.
- Scope: the owner section `### Polyglot Persistence` in V05/C04 and the
  inline V11/C06 card `### Polyglot Persistence`. Single-entry lane; no other
  entry, shared JSON, promotion or generated file is changed.
- Owner path (concatenate):

      book/volumes/v05-data-models-engines-and-lifecycle/
      c04-alternative-data-models-and-stores/multi-store-selection.md

- Card path:
  `book/volumes/v11-pattern-atlas/c06-database-storage/README.md`.
- Existing source ids: `src.fowler-polyglot`, `src.aws-cqrs`,
  `src.microsoft-cloud-patterns`, `src.debezium-outbox` and
  `src.postgresql`. No new source id is proposed.
- New ledger records: `read.debezium-outbox.2026-10-31`,
  `read.postgresql-logical-replication.2026-10-31`,
  `read.postgresql-logical-replication-conflicts.2026-10-31` and
  `read.postgresql-logical-replication-restrictions.2026-10-31`.
- Retained records reused byte-for-byte by canonical text:
  `read.batch3-fowler-polyglot.2026-10-22`,
  `read.aws-cqrs.2026-10-30` and `read.microsoft-cqrs.2026-10-30`.
- Baseline and final line-length and boundary checks pass.

## Candidate evaluation

- AWS, "CQRS pattern" (selected, retained record). The 2026-10-31 fetch is
  byte-identical to the retained 2026-10-30 representation: raw HTML
  `4e6f9305...`, canonical text `d3bcb473...`. It binds the eventual-
  consistency statement; it does not define a freshness bound, a rebuild or a
  reconciliation procedure.
- Microsoft, "CQRS pattern" (selected, retained record). The 2026-10-31
  canonical text is byte-identical to the retained 2026-10-30 record at
  `469253bc...`, although the raw HTML differs (`20f41ffd...` to
  `6accae39...`) because the served chrome changed. It binds stale reads,
  outbox atomicity, idempotent consumers and replay-based regeneration. The
  page does not make a derived row and its cursor atomic, and does not define a
  rebuild or reconciliation procedure.
- Debezium, "Outbox Event Router" (selected, 2026-10-31 refresh). The retained
  2026-10-21 record at `68873ce9...` is historical; the current page canonical
  text is `26c1b278...` and raw HTML is `382f0b...`. It binds the outbox
  table's event id for duplicate removal. The page is one living stable
  documentation page and does not test a consumer.
- PostgreSQL, "Chapter 29. Logical Replication" (selected, new record). It
  binds the initial snapshot followed by continual change delivery and the
  publisher-order application guarantee. It does not cover conflicts, schema
  restrictions or subscription operation.
- PostgreSQL, "29.7. Conflicts" (selected, new record). It binds the conflict
  definition, the manual-resolution rule and the skip-or-reconcile options. It
  does not reproduce a conflict or operate a subscription.
- PostgreSQL, "29.8. Restrictions" (selected, new record). It binds the
  non-replication of schema and DDL and the manual schema-sync obligation. It
  does not execute a schema change.
- Microsoft, "Idempotent Consumer" (examined, not selected). Its check-then-
  process failure window is a stronger consumer-side quote, but the retained
  `read.microsoft-cqrs.2026-10-30` record already carries the idempotent-
  consumer requirement, so adding the page would widen the lane without adding
  a new claim.
- Fowler, "Polyglot Persistence" (retained). It still supports the mechanism
  and the single-store alternative; it does not support freshness, rebuild,
  deduplication, schema migration or recovery, so those dimensions must bind
  other sources.
- DDIA remains blocked and is not cited as support.

## Source binding

Quotes reproduce the served prose. Line breaks inside a quote are editorial
wrapping. The binding revision is the record's `content_sha256`: the canonical
text digest extracted with `scripts/source_content_hash.py`. Quoted fragments
were checked as whitespace-normalized substrings of the served canonical text.
The Tycho-labelled sentences are not presented as source quotes.

### AWS — CQRS pattern (retained record)

- Source id: `src.aws-cqrs` (existing).
- Retained record: `read.aws-cqrs.2026-10-30`, revision
  `d3bcb473e011c43db8df0e09f568a0ba7c6c05a9014c1c7ef06fdf7bf60b8258`.
- URL (concatenate the two lines):

      https://docs.aws.amazon.com/prescriptive-guidance/latest/
      modernization-data-persistence/cqrs-pattern.html

- Unit label: "CQRS pattern — AWS Prescriptive Guidance"; unit type
  `documentation-page`; access date 2026-10-30 (retained).
- Representation: HTTP 200, 18,222 bytes, HTTP Date
  2026-10-31T04:24:45Z, Last-Modified 2026-10-30T23:31:18Z, ETag
  `qDFM5+0szYdO9ZrmKTBvo/Fqfpk=`; raw HTML SHA-256
  `4e6f93053f75665a2efce9079b551847db05c6b375075c53a0be5127bd5382e9`,
  byte-identical to the retained record. Canonical text: 4,250 characters,
  666 words, SHA-256 `d3bcb473...`.
- Sections used: "CQRS pattern".
- Exact quote:

      The CQRS pattern typically results in eventual consistency between the
      data stores.

- Limits: one AWS Prescriptive Guidance page with no published version
  identifier; it states eventual consistency but not a bound, a rebuild or a
  reconciliation owner.

### Microsoft — CQRS pattern (retained record)

- Source id: `src.microsoft-cloud-patterns` (existing).
- Retained record: `read.microsoft-cqrs.2026-10-30`, revision
  `469253bc1c554fc0697cff4f1bbdbcbf851bb40840d39579850c92e03d7f591f`.
- URL: `https://learn.microsoft.com/en-us/azure/architecture/patterns/cqrs`.
- Unit label: "CQRS pattern — Azure Architecture Center"; unit type
  `pattern-page`; access date 2026-10-30 (retained).
- Representation: HTTP 200, 69,680 bytes, HTTP Date
  2026-10-31T04:26:54Z, Last-Modified 2026-10-11T01:05:22Z, ETag
  `t4PEUx/8c4rPNK5V/Liq3jCGllc=`; raw HTML SHA-256
  `6accae3913bc0fa8d3dd708e19da45c475bf3047da5500e1b9587912684ab065`.
  The 2026-10-30 record pinned raw HTML `20f41ffd...`; the canonical text is
  byte-identical at `469253bc...`, so the retained binding remains valid. The
  raw delta is served chrome, not article text.
- Sections used: "Separate models in different data stores", "Problems and
  considerations", "Benefits of combining the Event Sourcing and CQRS
  patterns".
- Exact quotes:

      When the read databases and write databases are separated, the read data
      might not show the most recent changes immediately. This delay results in
      stale data.

      The read model is eventually consistent with the write model.

      Because you usually can't enlist message brokers and databases into a
      single distributed transaction, consistency problems can occur when you
      update the database and publish events.

      Use the Transactional Outbox pattern to persist the state change and event
      atomically, and make the read-model consumer idempotent to tolerate
      duplicate delivery.

      Because the event store acts as the single source of truth, you can easily
      regenerate materialized views or adapt to changes in the read model by
      replaying historical events.

- Limits: one living Microsoft Learn page with no published version
  identifier. It does not make a derived read row and its cursor atomic, does
  not define a projection cursor or rebuild procedure, and does not test a
  projector crash.

### Debezium — Outbox Event Router (2026-10-31 refresh)

- Source id: `src.debezium-outbox` (existing).
- New record: `read.debezium-outbox.2026-10-31`.
- Retained historical record: `read.batch2-debezium-outbox.2026-10-21`,
  revision
  `68873ce994e90fe95e9813ef38ea232937825e5d0505b1fafa842c792b6e2e1b`.
- URL:
  `https://debezium.io/documentation/reference/stable/transformations/outbox-event-router.html`.
- Unit label: "Outbox Event Router — Debezium documentation (2026-10-31
  refresh)"; unit type `documentation-page`; access date 2026-10-31.
- Representation: HTTP 200, 90,537 bytes, HTTP Date 2026-10-31T04:26:54Z, no
  Last-Modified or ETag served; raw HTML SHA-256
  `382f0bd0cd99f5c8206f9ba0381f3ec71f12ffe373154d351baa8823fd11ad53`.
  Canonical text: 21,348 characters, 2,872 words, SHA-256
  `26c1b278b6e7bd2a85787fa38064b0e9651836ca1bf1e7830df46781d9b6872e`.
- Sections used: "Outbox Event Router"; "Example outbox message"; "Basic
  outbox table"; "Basic configuration"; "Configuration options".
- Exact quote:

      You can use this ID, for example, to remove duplicate messages.

- Limits: one living "stable" documentation page; it describes the outbox
  table, event id and routing configuration, not a consumer implementation, a
  delivery guarantee or a failure drill. Linked pages and examples were not
  read.

### PostgreSQL — Chapter 29. Logical Replication

- Source id: `src.postgresql` (existing).
- New record: `read.postgresql-logical-replication.2026-10-31`.
- URL: `https://www.postgresql.org/docs/current/logical-replication.html`.
- Unit label: "Chapter 29. Logical Replication — PostgreSQL 18 documentation";
  unit type `documentation-page`; access date 2026-10-31.
- Representation: HTTP 200, 19,728 bytes, HTTP Date
  2026-10-30T23:54:23Z, no Last-Modified or ETag served; raw HTML SHA-256
  `588d7a5bfa50fafada6e3bda0cfb39e979e924af84fee4bdcf40944a47ebc42f`.
  Canonical text: 3,830 characters, 555 words, SHA-256
  `2f803799559f1397ed6f6af2aa2fb3d04b678418e3ef5c7b901438d2062c4c1d`.
- Sections used: "Chapter 29. Logical Replication".
- Exact quote:

      When logical replication of a table typically starts, PostgreSQL takes a
      snapshot of the table's data on the publisher database and copies it to the
      subscriber. Once complete, changes on the publisher since the initial copy
      are sent continually to the subscriber.

- Limits: one PostgreSQL 18 chapter landing page; it gives the high-level
  copy-then-stream model and states that subscriber-side writes can create
  conflicts, but it does not cover conflict handling or schema restrictions.

### PostgreSQL — 29.7. Conflicts

- Source id: `src.postgresql` (existing).
- New record: `read.postgresql-logical-replication-conflicts.2026-10-31`.
- URL:
  `https://www.postgresql.org/docs/current/logical-replication-conflicts.html`.
- Unit label: "29.7. Conflicts — PostgreSQL 18 documentation"; unit type
  `documentation-page`; access date 2026-10-31.
- Representation: HTTP 200, 27,805 bytes, HTTP Date
  2026-10-31T00:36:14Z, no Last-Modified or ETag served; raw HTML SHA-256
  `03928cc562272d536f3067a145e2e668f123a0ccb28ff205bf799315223c4a59`.
  Canonical text: 9,303 characters, 1,462 words, SHA-256
  `14702e9d7f4291babb23509b3193a7e3720618e2c1de01f674f858e60478c4d3`.
- Sections used: "29.7. Conflicts".
- Exact quotes:

      A conflict that produces an error will stop the replication; it must be
      resolved manually by the user.

      The resolution can be done either by changing data or permissions on the
      subscriber so that it does not conflict with the incoming change or by
      skipping the transaction that conflicts with the existing data.

- Limits: one PostgreSQL 18 documentation page; no conflict was reproduced and
  no subscription was operated. Missing rows for UPDATE/DELETE are skipped
  rather than treated as errors, so the quoted stop rule is scoped to conflicts
  that raise an error.

### PostgreSQL — 29.8. Restrictions

- Source id: `src.postgresql` (existing).
- New record:
  `read.postgresql-logical-replication-restrictions.2026-10-31`.
- URL:
  `https://www.postgresql.org/docs/current/logical-replication-restrictions.html`.
- Unit label: "29.8. Restrictions — PostgreSQL 18 documentation"; unit type
  `documentation-page`; access date 2026-10-31.
- Representation: HTTP 200, 16,197 bytes, HTTP Date
  2026-10-31T00:36:14Z, no Last-Modified or ETag served; raw HTML SHA-256
  `ebcbea9f2af8d99e9df1c0a981fe031177fb90a522b92745b1d1549d8687243c`.
  Canonical text: 4,093 characters, 658 words, SHA-256
  `85de74cc6d352a20becc5282482c542367c143d18d66cb9612db2287244a179a`.
- Sections used: "29.8. Restrictions".
- Exact quotes:

      The database schema and DDL commands are not replicated.

      Subsequent schema changes would need to be kept in sync manually.

- Limits: one PostgreSQL 18 documentation page; no schema change was executed.
  The page also says additive subscriber-side changes can avoid intermittent
  errors, which Tycho reads as an ordering constraint, not a complete migration
  procedure.

## Book edits

### Owner page

- Frontmatter: only `updated_at` moves from 2026-10-20 to 2026-10-31.
  `evidence_scope`, `source_inspection_date`, `content_review` and
  `content_verified_at` are unchanged. The new records are supporting
  bindings, not page-level evidence-scope ids.
- The mechanism sentence and the single-store alternative sentence are
  unchanged, preserving the existing owner-unit quotes. The phrase "projection
  view may lag" is retained so the existing unit term stays present.
- A Tycho-labelled four-part invariant adds freshness, rebuild, deduplication
  and schema migration, each followed by the exact public quote and a
  Tycho-labelled serving rule.
- A Tycho-labelled failure/recovery paragraph keeps the existing reconciliation
  sentence and adds the Microsoft outbox constraint, the PostgreSQL conflict
  stop and resolution options, and Tycho's recovery sequence.
- A source-boundary list records the canonical and raw revisions for the six
  units and labels the extracted quotes.
- `### Polyglot Persistence` stays at line 110. `## Navigation, prerequisites
  and source scope` moves from 127 to 199. The page grows from 136 to 208
  lines.
- Raw SHA-256:
  `018d68edd93eb3fd748ae6f336d9dac583e1d8412430ad75ab934c6ad0bd8111`.
- Historical-view SHA-256:
  `d035250db784219dc65a9579eaec658aec674a26bb4f193d00224ba5fe23d584`.
- Base raw SHA-256:
  `5d19778ca3e1256b72740b96cce73647fc47d1fd257ece0904ff1bd1d525210a`;
  base historical-view SHA-256:
  `0123387e61f31f2a51b43c5d6b78bab463f3021ed26693949a860a1ed6999151`.

### V11/C06 inline card

- `evidence_scope.source_ids` adds `src.aws-cqrs`,
  `src.microsoft-cloud-patterns` and `src.debezium-outbox`;
  `src.postgresql` was already declared.
- `updated_at` and `source_inspection_date` move to 2026-10-31;
  `content_review.reviewed_at` moves to 2026-10-31 with the existing
  `Automated authoring agent` reviewer. This is a self-check, not independent
  review.
- Good-fit conditions add rebuild, deduplication, schema migration and failure
  handling. Hard contraindications add unassigned reconciliation ownership.
- Failure and recovery adds the AWS, Microsoft, PostgreSQL and Debezium
  evidence and Tycho's freshness, rebuild and half-migration rules.
- Sources adds the retained AWS and Microsoft records and the four proposed
  records; the Fowler record remains the primary citation.
- `### Polyglot Persistence` moves from 243 to 246 because of the three added
  source ids. `### CQRS Read Projections` moves from 279 to 303. `##
  Navigation and prerequisites` moves from 415 to 439. The chapter page grows
  from 432 to 456 lines.
- Raw SHA-256:
  `c63c8b64b6b420076cfe82daa4189a53b8d4c9dddd3c42428f5afa70dee9904f`.
- Historical-view SHA-256:
  `06b5719bbe2886e9470752db4ab4ad17973b7151d984738316d358c9ef1ea8b6`.
- Base raw SHA-256:
  `afb666ef86de477506eb7421b8f7b0798b5ce8088ef590bb7e677e36048135ae`;
  base historical-view SHA-256:
  `72fa546459820ab4f404c59d39f1eddfdda94e56f4e8a6cdd949351cae25ca2c`.

No other book file is changed by this lane.

## Metadata needs (integrator)

The following changes are not in the lane commit. They are required before the
owner unit can move to 4/4 supported and before the atlas hash checks pass.

### Source register `sources/register.json`

Set `updated` to 2026-10-31; the source count stays 304.

- `src.debezium-outbox` — change `reading_status` from
  `landing-or-abstract-inspected` to `full-public-page-inspected`; set
  `access_checked` and `content_verified` to 2026-10-31. Replace the
  placeholder `version` with: "Living Debezium 3.7 documentation, refreshed
  2026-10-31; 90,537-byte HTML; canonical text SHA-256
  `26c1b278b6e7bd2a85787fa38064b0e9651836ca1bf1e7830df46781d9b6872e`;
  raw HTML SHA-256
  `382f0bd0cd99f5c8206f9ba0381f3ec71f12ffe373154d351baa8823fd11ad53`;
  no Last-Modified or ETag; no published edition identifier." Replace
  `verification_scope` with: "Outbox Event Router page read on 2026-10-31 for
  the outbox table, event id, routing and configuration options; linked pages
  and examples were not read."
- `src.postgresql` — set `access_checked` and `content_verified` to
  2026-10-31. Append to `version`: logical replication chapter canonical
  `2f803799...`; conflicts canonical `14702e9d...`; restrictions canonical
  `85de74cc...`; all served 2026-10-31. Append to `verification_scope`:
  "Chapter 29 Logical Replication, 29.7 Conflicts and 29.8 Restrictions were
  read on 2026-10-31 for snapshot/stream startup, manual conflict resolution
  and schema non-replication; no subscription, conflict or schema change was
  executed."
- `src.aws-cqrs` — no change; the 2026-10-31 fetch is byte-identical to the
  retained 2026-10-30 record.
- `src.microsoft-cloud-patterns` — no new record. Optionally append to
  `version`: "CQRS pattern page refetched 2026-10-31; canonical text SHA-256
  remains `469253bc...`; raw HTML is `6accae39...` because the served
  chrome changed." Do not replace the retained 2026-10-30 record.

### Reading ledger `edition/patterns/reading-ledger.v1.json`

Add four records; records move from 208 to 212. Each record is `status:
read`, `reviewer: "Automated authoring agent"`, and uses the URL, label,
sections and `content_sha256` below.

- `read.debezium-outbox.2026-10-31` — source `src.debezium-outbox`;
  label "Outbox Event Router — Debezium documentation (2026-10-31 refresh)";
  type `documentation-page`; sections "Outbox Event Router", "Example outbox
  message", "Basic outbox table", "Basic configuration", "Configuration
  options"; content_sha256 `26c1b278...`. Access method records the raw
  revision, canonical revision, HTTP Date, no Last-Modified/ETag and the
  sections read. Claims are limited to outbox table/event-id/routing
  configuration; linked pages and examples are not supported.
- `read.postgresql-logical-replication.2026-10-31` — source
  `src.postgresql`; label "Chapter 29. Logical Replication — PostgreSQL 18
  documentation"; type `documentation-page`; section "Chapter 29. Logical
  Replication"; content_sha256 `2f803799...`.
- `read.postgresql-logical-replication-conflicts.2026-10-31` — source
  `src.postgresql`; label "29.7. Conflicts — PostgreSQL 18 documentation";
  type `documentation-page`; section "29.7. Conflicts"; content_sha256
  `14702e9d...`.
- `read.postgresql-logical-replication-restrictions.2026-10-31` — source
  `src.postgresql`; label "29.8. Restrictions — PostgreSQL 18
  documentation"; type `documentation-page`; section "29.8. Restrictions";
  content_sha256 `85de74cc...`.

The retained `read.batch2-debezium-outbox.2026-10-21` record stays unchanged
as historical evidence. The retained Fowler, AWS and Microsoft records stay
unchanged.

### Source plan `edition/patterns/source-plan.v1.json`

Append six units to `tycho.pattern.polyglot-persistence` after the existing
Fowler unit, in this order:

1. AWS, label "CQRS pattern — AWS Prescriptive Guidance", type
   `documentation-page`, URL the AWS page above, record
   `read.aws-cqrs.2026-10-30`, sections `["CQRS pattern"]`.
2. Microsoft, label "CQRS pattern — Azure Architecture Center", type
   `pattern-page`, URL the Microsoft page above, record
   `read.microsoft-cqrs.2026-10-30`, sections equal to that record's fifteen
   `sections_read`.
3. Debezium, label "Outbox Event Router — Debezium documentation (2026-10-31
   refresh)", type `documentation-page`, URL the Debezium page above, record
   `read.debezium-outbox.2026-10-31`, sections equal to that record's
   `sections_read`.
4. PostgreSQL logical replication, label "Chapter 29. Logical Replication —
   PostgreSQL 18 documentation", type `documentation-page`, URL the logical
   replication page above, record
   `read.postgresql-logical-replication.2026-10-31`, section "Chapter 29.
   Logical Replication".
5. PostgreSQL conflicts, label "29.7. Conflicts — PostgreSQL 18
   documentation", type `documentation-page`, URL the conflicts page above,
   record `read.postgresql-logical-replication-conflicts.2026-10-31`,
   section "29.7. Conflicts".
6. PostgreSQL restrictions, label "29.8. Restrictions — PostgreSQL 18
   documentation", type `documentation-page`, URL the restrictions page
   above, record
   `read.postgresql-logical-replication-restrictions.2026-10-31`, section
   "29.8. Restrictions".

Set every unit `status` to `read` and `blocked_reason` to `null`. Replace
the entry notes with: "Invariant and failure/recovery bound 2026-10-31 to AWS,
Microsoft, Debezium and PostgreSQL public units; the four-part invariant and
recovery sequence remain Tycho."

Summary: `required_units` 251 -> 257; `read_units` 250 -> 256;
`blocked_units` stays 1; `ledger_records` 208 -> 212. Recompute
`registry_sha256` after saving the registry and refresh
`route_index_snapshot` from the rebuilt route index; the authoritative values
are the saved-file hashes.

### Registry `edition/patterns/registry.v1.json`

For `tycho.pattern.polyglot-persistence`:

- Set `technical_owner.state` to `partial-bounded`.
- Set `coverage.technical` and `coverage.overall` to
  `partial-bounded`; keep `coverage.decision` at `partial-bounded`.
- Append the six units above to `source_units` in the source-plan order, all
  with status `read`; unit labels must equal the plan labels.
- Replace `notes` with: "Invariant and failure/recovery bound 2026-10-31 to
  AWS, Microsoft, Debezium and PostgreSQL public units; the four-part invariant
  and recovery sequence remain Tycho. Coverage partial-bounded; no promotion."
- Keep `review_status` `self-checked`. Set the registry `updated_at` to
  2026-10-31.

### Owner units `edition/patterns/owner-units.v1.json`

Entry `tycho.pattern.polyglot-persistence`:

- Keep `owner.line` at 110, the heading, document id, unit kind and unit terms
  unchanged. The terms remain present in the body.
- Invariant: set `state` to `supported`; keep the existing `quote`
  ("Define freshness, rebuild, deduplication, schema migration and failure
  recovery explicitly."). Reason: "PostgreSQL binds the copy-then-stream start
  of logical replication; AWS and Microsoft bind eventual consistency and stale
  reads; Microsoft binds transactional outbox, idempotent delivery and replay-
  based regeneration; Debezium binds the event id used to remove duplicates;
  PostgreSQL binds the non-replication of schema and DDL. The four-part wording
  and the serving rules are Tycho, labelled in the page."
- Invariant primary binding: `src.postgresql`, record
  `read.postgresql-logical-replication.2026-10-31`, section "Chapter 29.
  Logical Replication", quote "When logical replication of a table typically
  starts, PostgreSQL takes a snapshot of the table's data on the publisher
  database and copies it to the subscriber. Once complete, changes on the
  publisher since the initial copy are sent continually to the subscriber.",
  revision `2f803799...`.
- Invariant supporting bindings:
  - AWS, record `read.aws-cqrs.2026-10-30`, section "CQRS pattern", quote "The
    CQRS pattern typically results in eventual consistency between the data
    stores.", revision `d3bcb473...`.
  - Microsoft, record `read.microsoft-cqrs.2026-10-30`, section "Problems and
    considerations", quote "When the read databases and write databases are
    separated, the read data might not show the most recent changes
    immediately. This delay results in stale data.", revision `469253bc...`.
  - Microsoft, same record, section "Separate models in different data stores",
    quote "Use the Transactional Outbox pattern to persist the state change and
    event atomically, and make the read-model consumer idempotent to tolerate
    duplicate delivery.", revision `469253bc...`.
  - Microsoft, same record, section "Benefits of combining the Event Sourcing
    and CQRS patterns", quote "Because the event store acts as the single
    source of truth, you can easily regenerate materialized views or adapt to
    changes in the read model by replaying historical events.", revision
    `469253bc...`.
  - Debezium, record `read.debezium-outbox.2026-10-31`, section "Basic outbox
    table", quote "You can use this ID, for example, to remove duplicate
    messages.", revision `26c1b278...`.
  - PostgreSQL, record
    `read.postgresql-logical-replication-restrictions.2026-10-31`, section
    "29.8. Restrictions", quote "The database schema and DDL commands are not
    replicated.", revision `85de74cc...`.
  - PostgreSQL, same record and section, quote "Subsequent schema changes would
    need to be kept in sync manually.", revision `85de74cc...`.
- Failure/recovery: set `state` to `supported`; keep the existing `quote`
  ("Dual-write ambiguity and partial migration need an explicit reconciliation
  owner; a half-migrated projection is not a valid serving state."). Reason:
  "Microsoft states that broker and database writes cannot share one
  distributed transaction and recommends the transactional outbox plus an
  idempotent consumer. PostgreSQL states that a conflict that raises an error
  stops logical replication and must be resolved manually, by changing
  subscriber data or permissions or by skipping the conflicting transaction.
  The reconciliation-owner rule and the invalid half-migrated serving state are
  Tycho, labelled in the page."
- Failure/recovery primary binding: `src.postgresql`, record
  `read.postgresql-logical-replication-conflicts.2026-10-31`, section "29.7.
  Conflicts", quote "A conflict that produces an error will stop the
  replication; it must be resolved manually by the user.", revision
  `14702e9d...`.
- Failure/recovery supporting bindings:
  - PostgreSQL, same record and section, quote "The resolution can be done
    either by changing data or permissions on the subscriber so that it does
    not conflict with the incoming change or by skipping the transaction that
    conflicts with the existing data.", revision `14702e9d...`.
  - Microsoft, record `read.microsoft-cqrs.2026-10-30`, section "Separate
    models in different data stores", quote "Because you usually can't enlist
    message brokers and databases into a single distributed transaction,
    consistency problems can occur when you update the database and publish
    events.", revision `469253bc...`.
  - Microsoft, same record and section, quote "Use the Transactional Outbox
    pattern to persist the state change and event atomically, and make the
    read-model consumer idempotent to tolerate duplicate delivery.", revision
    `469253bc...`.
- `source_support`: keep `read.batch3-fowler-polyglot.2026-10-22` as the
  primary record and add auxiliary entries for
  `read.aws-cqrs.2026-10-30` (`d3bcb473...`),
  `read.microsoft-cqrs.2026-10-30` (`469253bc...`),
  `read.debezium-outbox.2026-10-31` (`26c1b278...`),
  `read.postgresql-logical-replication.2026-10-31` (`2f803799...`),
  `read.postgresql-logical-replication-conflicts.2026-10-31`
  (`14702e9d...`) and
  `read.postgresql-logical-replication-restrictions.2026-10-31`
  (`85de74cc...`).
- Set `technical_coverage` to `partial-bounded`. Set `notes` to:
  "Invariant and failure/recovery bound 2026-10-31 to AWS, Microsoft, Debezium
  and PostgreSQL public units; the four-part invariant and recovery sequence
  remain Tycho. Coverage partial-bounded; no promotion or acceptance."
- Leave `decision_evidence` unchanged: the decision question, competing
  alternative and decision state are unchanged in the card.
- Summary counters: `invariant_supported` 75 -> 76;
  `failure_recovery_supported` 69 -> 70; `technical_partial_bounded` 15 ->
  16; `technical_partial` 73 -> 72. `technical_sufficient` stays 57.

### Content revisions `edition/content-revisions.json`

Add one issue-540 revision with `authorized_at` 2026-10-31 and authorization
"B44 polyglot-persistence invariant and failure/recovery source binding; no
promotion or owner acceptance." Use these historical-view hashes:

- Directory document owner path, previous (baseline):
  `0123387e61f31f2a51b43c5d6b78bab463f3021ed26693949a860a1ed6999151`;
  current:
  `d035250db784219dc65a9579eaec658aec674a26bb4f193d00224ba5fe23d584`.
- Directory document card path, previous (baseline):
  `72fa546459820ab4f404c59d39f1eddfdda94e56f4e8a6cdd949351cae25ca2c`;
  current:
  `06b5719bbe2886e9470752db4ab4ad17973b7151d984738316d358c9ef1ea8b6`.
- Leave `source_blocks`, `enrichment_documents`, `enrichment_additions`
  and `enrichment_baselines` empty.

The owner page is not in the enrichment manifest and its source blocks are
outside sections 6-8, so no enrichment or decomposition revision is needed.
The decomposition validator confirms the protected payload is unchanged.

### Atlas manifest, inventory and derived artifacts

- `edition/atlas-manifest.json`: set the V11/C06 document `sha256` to
  `c63c8b64b6b420076cfe82daa4189a53b8d4c9dddd3c42428f5afa70dee9904f`.
  Set `registry_sha256` to the new registry file hash after the registry edit.
  No atlas route changes.
- `edition/inventory.json`: regenerate so the owner page hash is
  `018d68ed...` and the card hash is `c63c8b64...`; use
  `python3 scripts/validate_edition.py --write-inventory` before validating.
- Refresh once at batch end: route index, page census, coverage/reverse map,
  phase 4, delivery-evidence counts, semantic audit, edition inventory and the
  source catalogue. The sufficient-candidate and sufficient-ready-plan files
  must be reconciled from the new 4/4 state. The 2026-10-22 sufficient review
  record carries the old owner page hash; do not update that record without a
  fresh review.
- No promotion hash binds either changed page, so no promotion rebind is
  required.

### Preflight

The preflight checks cannot pass in this lane for two structural reasons: the
owner-unit dimensions are still recorded as partial because the shared JSON is
not in the lane, and the card has no `card_path` because it remains inline.
After the metadata above is applied, only the inline-card `card_path` check
should remain. Do not convert the card to a dedicated page in this lane.

## Validation

Checker output in the lane worktree after the two book edits:

    PASS: V11 prose <=100; 145 exact owner-link exceptions
    PASS: configured lexical boundary checks; independent-origin review still
    required.

Quote audit: 13 quoted fragments across six public units were checked as
whitespace-normalized substrings of the fetched canonical text. Zero missing.
The audit used the canonical extraction, not a search result.

Targeted validator results with the book edits only, in the lane worktree:

- `python3 scripts/validate_pattern_cards.py` — PASS; 145 entries.
- `python3 scripts/validate_book_metadata.py` — exit 0; structural
  metadata summary emitted.
- `python3 scripts/validate_decomposition.py` — exit 0; 839 fragment routes.
- `python3 scripts/validate_enrichment.py` — exit 0; 389 retained ids.
- `python3 scripts/validate_pattern_owner_units.py` — PASS; 145 entries,
  145 units, 30 shared pages.
- `python3 scripts/validate_pattern_atlas.py` — FAIL
  `atlas-document-sha`; expected until the atlas manifest is updated.
- `python3 scripts/validate_directory_migration.py` — FAIL
  `directory-baseline-payload-drift`; expected until the content revision is
  applied.
- `python3 scripts/preflight_sufficient.py --pattern
  tycho.pattern.polyglot-persistence` — FAIL on the two partial states and the
  missing inline `card_path`; expected until the metadata patch above.
- Full unit suite was not run; batch-end tests remain with the integrator.

## Limits

The binding uses six public units. They describe eventual consistency, stale
reads, outbox atomicity, idempotent consumers, replay-based regeneration,
outbox event ids, logical-replication startup, conflict handling and schema
non-replication. None observes this page's service, operates a subscription,
reproduces a conflict, executes a schema change, measures projection lag or
proves that one of the four invariant parts is sufficient by itself.

The owner section states a Tycho synthesis: the four-part invariant wording,
the freshness-bound rule, the rebuild-from-authority rule, the dedup-key and
marker-commit rule, the compatibility-window rule, the reconciliation-owner
rule, the invalid-half-migration rule and the recovery sequence. Those
sentences are labelled in the page; the exact public quotes are not.

The owner page's `evidence_scope.source_ids` still lists only `src.sqlite`.
The new records are supporting bindings, not page-level evidence-scope ids.
Adding them to the owner page would require the enrichment manifest, both
historical hashes, the content revision and the decomposition/enrichment
validators; treat that as a separate change.

No promotion, owner acceptance, CI, independent review or merge permission is
claimed. The book/atlas independent review gate applies.

## Review needs

- Request a fresh external review under the book/atlas gate. The reviewer
  should check quote-to-claim fit for the invariant and failure/recovery
  dimensions, the Tycho labels for the four-part rule and recovery sequence,
  the six revisions, the card wording, the shifted heading lines and the
  metadata patch.
- The reviewer must use read-only repository access and must not run tests.
- No existing promotion binds either changed page; confirm that before
  integration.

## Commit scope

The lane commit contains this note and the two book files only (owner path
concatenates the two segments):

- `book/volumes/v05-data-models-engines-and-lifecycle/`
  `c04-alternative-data-models-and-stores/multi-store-selection.md`;
- `book/volumes/v11-pattern-atlas/c06-database-storage/README.md`.

No shared JSON, promotion, test or generated file is in the lane commit.
