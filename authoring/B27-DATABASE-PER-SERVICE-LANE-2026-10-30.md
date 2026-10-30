# B27 — Database per Service failure/recovery and alternative lane

Status: lane-local book edit, self-checked on 2026-10-30. No shared edition
metadata, promotion, generated artifact or owner acceptance is included. The
entry was 2/4 at the parent HEAD: mechanism and invariant were supported;
failure/recovery and alternative were partial. This lane binds both dimensions
to public microservices.io pattern pages and the existing Monolith First record.
Stale replica freshness, enforced module ownership inside a shared database and
the shared release-cadence condition remain Tycho guidance. The metadata patch
was exercised in a detached scratch copy: preflight passes 1/1; owner units,
registry, cards, sources, book metadata, directory migration, decomposition and
enrichment all pass. Coverage and atlas validators still report registry-hash
staleness until their batch-end regeneration. The patch is not in the lane
commit; promotion is not claimed or ready.

## Lane coordinates

- Parent HEAD: `0614c5a1` ("feat(research): promote Modular Monolith").
- Branch: `b27-db-per-service`; worktree:
  `/Users/rbaranov/Projects/tycho-worktrees/b27-db-per-service`.
- Scope: the V02/C02 owner section `### Database per Service` and the inline
  V11/C01 card `### Database per Service`. Single-entry lane; no other entry,
  shared owner page, promotion or generated file is changed.
- Owner path (concatenate the three lines):

      book/volumes/v02-application-boundaries-and-contracts/
      c02-domain-boundaries-data-ownership-and-contracts/
      ownership-isolation.md

- Card path: `book/volumes/v11-pattern-atlas/c01-application-boundaries/README.md`.
- The card remains inline; the integrator owns any split and `card_path`
  registration.

## Candidate evaluation

- `src.microservices-patterns`, record
  `read.microservices-database-per-service.2026-10-21`: the existing mechanism
  and invariant binding. The current raw HTML digest
  `09a42dc873ba914208f3b2dc90a28a1287b883da6080805b318ff6a28d484d31`
  reproduces the record. The page also states the cross-service transaction and
  query drawbacks and the replication force. Reused for failure/recovery and
  for the Database per Service side of the shared-database disagreement.
- `src.microservices-patterns`, record `read.batch2-saga.2026-10-21`: the
  existing Saga record. The current raw HTML digest
  `54805df89f619c8432fd280263a88670ed66fac6cbe0b5429a1ebdc5d4cd1047`
  reproduces the record. Selected for coordinated local transactions and
  compensating recovery; the page does not address dual writes, replicas or
  cross-service queries.
- `src.microservices-patterns`, record `read.batch2-outbox.2026-10-21`: the
  existing Transactional Outbox record. The current raw HTML digest
  `7b9d9b224d9b985bf03d581dcdef5c94a21f49a93f3ac1e74c6bc2104a48b3eb`
  reproduces the record. Selected for the atomic database-plus-message
  requirement, the outbox relay and the idempotent consumer. The page does not
  claim that an outbox removes every coordination cost.
- `src.microservices-patterns`, Shared database page: a new unit. The current
  raw HTML digest is
  `4dc5fcf1a9bdf1d4c97c3ba916f997611cebdc2bc4b87927a6bb0a61c11c5731`.
  Selected for the shared-database benefits and for the development-time and
  runtime coupling drawbacks. The page presents shared database as a pattern
  with trade-offs; the Database per Service page calls the same option a
  problem source. Both readings are recorded.
- `src.monolith-first`, record `read.monolith-first.2026-10-21`: the existing
  article record. The current raw HTML digest
  `722d8d78beddd9e0f6ff3e856eec94dfa2b9fa3bebcaaf4c9e80ccdd3c0e1446`
  reproduces the record. Selected for the team-simplicity argument and for
  modularity at the API and data-storage boundaries. The article does not
  discuss shared databases, enforced module ownership or release cadence.
- No selected page supports replica lag or a freshness check, or enforced
  module ownership inside a shared database. Those parts of the owner text are
  labelled Tycho guidance.

## Source binding

### Database per Service — existing record

- Existing source id: `src.microservices-patterns`.
- Existing record: `read.microservices-database-per-service.2026-10-21`.
- URL (concatenate the two lines):

      https://microservices.io/patterns/data/
      database-per-service.html

- Unit label: "Database per Service — pattern page".
- Unit type: `pattern-page`; access date 2026-10-21; rechecked 2026-10-30.
- Access: public HTTPS GET; HTTP `Last-Modified` 2026-10-23T01:10:11Z;
  ETag `"6adab3f3-65f5"`.
- Recorded HTML revision:
  `09a42dc873ba914208f3b2dc90a28a1287b883da6080805b318ff6a28d484d31`.
- Canonical text digest from `scripts/source_content_hash.py`:
  `5624b9c8d22fd3f8880c29fa97113c327018acc65cde51f5579e1b54cccc42e9`.
  The record stores the raw HTML digest, so the two values are not expected to
  match. No new record is required.
- Sections read: `Pattern: Database per service`, `Context`, `Problem`,
  `Forces`, `Solution`, `Example`, `Resulting context`,
  `Related patterns`.
- Exact quotes used:

      Implementing business transactions that span multiple services is not
      straightforward.

      Implementing queries that join data that is now in multiple databases is
      challenging.

      Databases must sometimes be replicated and sharded in order to scale.

      The Shared Database anti-pattern describes the problems that result from
      microservices sharing a database

- Limits: one pattern page. It names the drawbacks and links the related
  patterns; it does not test a distributed transaction, a query composition, a
  replica-lag path or a shared-database deployment.

### Saga — existing record

- Existing source id: `src.microservices-patterns`.
- Existing record: `read.batch2-saga.2026-10-21`.
- URL (concatenate the two lines):

      https://microservices.io/patterns/data/
      saga.html

- Unit label: "Saga — pattern page".
- Unit type: `pattern-page`; access date 2026-10-21; rechecked 2026-10-30.
- Access: public HTTPS GET; HTTP `Last-Modified` 2026-10-23T01:10:10Z;
  ETag `"6adab3f2-7531"`.
- Recorded HTML revision:
  `54805df89f619c8432fd280263a88670ed66fac6cbe0b5429a1ebdc5d4cd1047`.
- Canonical text digest:
  `d6a4a989bf382419f6792d9afdf3baa49eabc0ab5879222ea1a5f2d2bae4814e`.
  No new record is required.
- Sections read: the existing record lists `Pattern: Saga`, `Context`,
  `Problem`, `Forces`, `Solution`, both examples, `Resulting context`,
  `Related patterns`, `Learn more` and `Example code`.
- Exact quotes used:

      A saga is a reliably coordinated sequence of local transactions.

      changes made by the completed steps are undone by compensating
      transactions.

- Limits: one pattern page. It explains coordination and compensation but does
  not describe dual writes, message relays, replica lag or cross-service joins.

### Transactional Outbox — existing record

- Existing source id: `src.microservices-patterns`.
- Existing record: `read.batch2-outbox.2026-10-21`.
- URL (concatenate the two lines):

      https://microservices.io/patterns/data/
      transactional-outbox.html

- Unit label: "Transactional Outbox — pattern page".
- Unit type: `pattern-page`; access date 2026-10-21; rechecked 2026-10-30.
- Access: public HTTPS GET; HTTP `Last-Modified` 2026-10-23T01:10:10Z;
  ETag `"6adab3f2-6382"`.
- Recorded HTML revision:
  `7b9d9b224d9b985bf03d581dcdef5c94a21f49a93f3ac1e74c6bc2104a48b3eb`.
- Canonical text digest:
  `845c4306d1318b019f2f4b9f773316bb85d60050fccc78e42e47850e53dca7eb`.
  No new record is required.
- Sections read: the existing record lists `Pattern: Transactional outbox`,
  `Also known as`, `Context`, `Problem`, `Forces`, `Solution`,
  `Result context`, `Related patterns` and `Learn more`.
- Exact quotes used:

      The command must atomically update the database and send messages in
      order to avoid data inconsistencies and bugs.

      first store the message in the database as part of the transaction that
      updates the business entities. A separate process then sends the messages
      to the message broker.

      a message consumer must be idempotent, perhaps by tracking the IDs of the
      messages that it has already processed.

      The Message relay might publish a message more than once.

- Limits: one pattern page. The record already states that deduplication and
  relay ownership are required. The page does not measure duplicate delivery or
  prove an idempotent consumer implementation.

### Shared database — new unit

- Existing source id: `src.microservices-patterns`.
- Proposed record: `read.microservices-shared-database.2026-10-30`.
- URL (concatenate the two lines):

      https://microservices.io/patterns/data/
      shared-database.html

- Unit label: "Shared database — pattern page".
- Unit type: `pattern-page`; access date 2026-10-30.
- Access: public HTTPS GET; HTTP `Last-Modified` 2026-10-23T01:10:10Z;
  ETag `"6adab3f2-54d3"`.
- Raw HTML SHA-256:
  `4dc5fcf1a9bdf1d4c97c3ba916f997611cebdc2bc4b87927a6bb0a61c11c5731`.
- Canonical text SHA-256:
  `673d6967ca97a66b6d6619700d469ee2b8ed4d7e7430989f92bb59b745d9aed9`.
- Sections read: `Pattern: Shared database`, `Context`, `Problem`,
  `Forces`, plus the untitled solution, benefits and drawbacks prose after
  `Forces`.
- Exact quotes used:

      A single database is simpler to operate

      A developer uses familiar and straightforward ACID transactions to
      enforce data consistency

      Development time coupling - a developer working on, for example, the
      OrderService will need to coordinate schema changes with the developers
      of other services that access the same tables.

      Runtime coupling

- Limits: one pattern page. It describes a shared database with free
  cross-service table access, not a shared database with enforced module
  ownership. It presents the option as a pattern with benefits and drawbacks,
  while the Database per Service page calls it a problem source; the owner
  section records both readings. No benchmark or deployment is reported.

### Monolith First — existing record

- Existing source id: `src.monolith-first`.
- Existing record: `read.monolith-first.2026-10-21`.
- URL (concatenate the two lines):

      https://martinfowler.com/bliki/
      MonolithFirst.html

- Unit label: "Monolith First — article".
- Unit type: `article`; access date 2026-10-21; rechecked 2026-10-30.
- Access: public HTTPS GET; HTTP `Last-Modified` 2026-10-29T16:11:21Z;
  ETag `"5746-65efcee2d9c40"`.
- Recorded HTML revision:
  `722d8d78beddd9e0f6ff3e856eec94dfa2b9fa3bebcaaf4c9e80ccdd3c0e1446`.
  The `scripts/source_content_hash.py` digest is
  `9cb2a6797a8c41fabba65adcff1d5408c46814616d17e5430e1aac3ce491539f`
  because that script's fallback includes page chrome; this is not a content
  change. No new record is required.
- Sections read: `Monolith First`, `Microservices Guide`,
  `Further Reading`, `Notes`, `Acknowledgements`.
- Exact quotes used:

      will slow down a team, favoring a monolith for simpler applications

      the API boundaries and how the data is stored

- Limits: one author article. It argues for a monolith first and modular
  design; it does not describe a shared database, an enforced module boundary or
  a release-cadence rule. The shared release condition is Tycho inference.

## Book edits

### V02/C02 owner section

- Frontmatter: `content_review.reviewed_at` and `updated_at` move to
  2026-10-30; the reviewer is "Automated authoring agent". The
  `evidence_scope.notes` now points to the body Source boundary.
  `source_inspection_date` stays `null`: the decomposition plan does not
  declare fresh sources for this page, and setting a date would fail
  `validate_decomposition.py` with `fabricated-question-verification`.
- The mechanism and invariant paragraphs are retained. The failure and
  alternative paragraph is replaced by:
  - **Failure and recovery** with the Database per Service drawback and
    replication quotes, the Transactional Outbox atomic-update, relay and
    idempotency quotes, and the Saga compensation quote, followed by Tycho
    labels for replica freshness and reconciliation.
  - **Alternative** with the Shared database simplicity, ACID and coupling
    quotes, the Database per Service anti-pattern wording, the Tycho
    enforced-ownership and shared-release conditions, and the Monolith First
    team-simplicity and modularity quotes.
- A Source boundary list records the five records and their revisions.
- Heading `### Database per Service` stays at line 87. The page is 150 lines.
- Raw SHA-256:
  `6595efa81030671491a42c85adcf3892f7657364e759d10716197546c40d5d70`.
- Historical-view SHA-256:
  `fe200aab9c937e45a4f96b6b873bd9d4b9970ec982266b974ad4fe1006023823`.

### V11/C01 inline card

- Frontmatter is unchanged: both `src.microservices-patterns` and
  `src.monolith-first` are already declared, and the review, update and
  inspection dates already read 2026-10-30.
- **Failure and recovery** now names the cross-service transaction and query
  drawbacks, the dual-write requirement, the outbox relay, the idempotent
  consumer and Saga compensation, and labels replica freshness and
  reconciliation as Tycho guidance.
- **Competing alternative** now names the shared-database benefits and coupling
  drawbacks, records the Database per Service anti-pattern wording, and labels
  the enforced-ownership condition as Tycho synthesis.
- **Sources** cites `read.microservices-database-per-service.2026-10-21` and
  names the Saga, Transactional Outbox, Shared database and Monolith First
  material, with exact quotes and revisions in the owner section.
- Heading `### Database per Service` stays at line 245. The chapter page is
  338 lines.
- Raw SHA-256:
  `93e7d5b19ed8f5ac098ef5da3bd5eaac2b5b8399fdfd5a44e746e9a41a1f0759`.
- Historical-view SHA-256:
  `064882458be87c42218a45aab4925670e877ca1e977dc3d60bcc4d9b5e3db5e7`.

No other book file is changed by this lane.

## Metadata needs (integrator)

The following patch is not in the lane commit. It was exercised in a detached
scratch copy of this worktree with the two book files and the ledger,
source-plan, registry, owner-unit, card and content-revision updates. The
scratch results are in the Validation section; no scratch file is part of the
lane commit.

### Reading ledger `edition/patterns/reading-ledger.v1.json`

Add one record; keep the three existing microservices records and the Monolith
First record unchanged.

- `read.microservices-shared-database.2026-10-30` — `src.microservices-patterns`;
  URL `https://microservices.io/patterns/data/shared-database.html`; unit
  label "Shared database — pattern page"; `unit_type` `pattern-page`;
  access date 2026-10-30; access method "public HTTP fetch; served HTML and
  rendered text inspected"; sections `Pattern: Shared database`, `Context`,
  `Problem`, `Forces`, plus the untitled solution/benefits/drawbacks prose;
  `content_sha256`
  `4dc5fcf1a9bdf1d4c97c3ba916f997611cebdc2bc4b87927a6bb0a61c11c5731`;
  `status` `read`; reviewer "Automated authoring agent".
- Claims supported: one shared database simplifies operation and supports
  familiar ACID transactions, while development-time coupling and runtime
  coupling constrain independent service ownership; Database per Service is
  presented as an alternative.
- Claims not supported: enforced module ownership inside a shared database;
  release-cadence effects; implementation behavior; independent reproduction
  or benchmark.
- Limits: one public page; linked pages and implementations were not read; no
  benchmark or independent review.

### Source plan `edition/patterns/source-plan.v1.json`

For `tycho.pattern.database-per-service.required_units`, add four units and
keep the Database per Service unit:

- Saga — `src.microservices-patterns`, `pattern-page`,
  `https://microservices.io/patterns/data/saga.html`, the existing record's
  section list, `status: "read"`,
  `read_record_id: "read.batch2-saga.2026-10-21"`.
- Transactional Outbox — `src.microservices-patterns`, `pattern-page`,
  `https://microservices.io/patterns/data/transactional-outbox.html`, the
  existing record's section list, `status: "read"`,
  `read_record_id: "read.batch2-outbox.2026-10-21"`.
- Shared database — `src.microservices-patterns`, `pattern-page`,
  `https://microservices.io/patterns/data/shared-database.html`, sections
  `Pattern: Shared database`, `Context`, `Problem`, `Forces`,
  `status: "read"`,
  `read_record_id: "read.microservices-shared-database.2026-10-30"`.
- Monolith First — `src.monolith-first`, `article`,
  `https://martinfowler.com/bliki/MonolithFirst.html`, the existing record's
  section list, `status: "read"`,
  `read_record_id: "read.monolith-first.2026-10-21"`.
- Replace the entry notes with the bounds text proposed for the owner unit.

### Registry `edition/patterns/registry.v1.json`

For `tycho.pattern.database-per-service`:

- Keep `technical_owner.state`, `coverage.technical`, `atlas_owner.state`,
  `coverage.decision` and `coverage.overall` at `partial-bounded`; all four
  dimensions being supported does not create a sufficient claim.
- Add `source_units` entries for the Saga, Transactional Outbox, Shared
  database and Monolith First units, each with status `read`.
- Replace `notes` with: "Failure/recovery and alternative bound 2026-10-30 to
  microservices.io Database per Service, Saga, Transactional outbox and Shared
  database pages plus the existing Monolith First record; replica freshness and
  enforced shared-database ownership remain Tycho guidance. Coverage
  partial-bounded; no promotion."
- Keep `review_status` `self-checked`. The registry pattern entry has no
  `updated_at` field in the current schema; do not add one.

### Owner units `edition/patterns/owner-units.v1.json`

Entry `tycho.pattern.database-per-service`:

- Keep `owner.line` at 87 and the unit terms unchanged.
- Failure/recovery:
  - `state`: `supported`.
  - `quote`: "Dual writes, stale replicas and cross-service queries are
    common; use an outbox or idempotent reconciliation for cross-service
    effects and verify replica freshness before joining."
  - `reason`: "Database per Service names cross-service transactions and joins
    as hard; Transactional Outbox documents atomic database-plus-message
    publication, an outbox relay and an idempotent consumer; Saga documents
    compensating local transactions. Replica lag and reconciliation as a repair
    loop are Tycho guidance, not source claims."
  - `binding`: `src.microservices-patterns`, record
    `read.batch2-outbox.2026-10-21`, section `Context`, quote "The command
    must atomically update the database and send messages in order to avoid
    data inconsistencies and bugs.", revision
    `7b9d9b224d9b985bf03d581dcdef5c94a21f49a93f3ac1e74c6bc2104a48b3eb`.
  - Supporting bindings: outbox `Solution` quote "first store the message in
    the database as part of the transaction that updates the business entities.
    A separate process then sends the messages to the message broker.";
    outbox `Result context` quote "a message consumer must be idempotent,
    perhaps by tracking the IDs of the messages that it has already processed.";
    Database per Service `Resulting context` quotes "Implementing business
    transactions that span multiple services is not straightforward." and
    "Implementing queries that join data that is now in multiple databases is
    challenging."; Saga `Solution` quote "changes made by the completed steps
    are undone by compensating transactions."; Database per Service `Forces`
    quote "Databases must sometimes be replicated and sharded in order to
    scale.".
- Alternative:
  - `state`: `supported`.
  - `quote`: "A shared database with enforced module ownership is simpler when
    teams release together; choose separate stores only when independent
    ownership, scaling or recovery justify the coordination cost."
  - `reason`: "Shared database documents a single database that is simpler to
    operate and supports familiar ACID transactions, while warning that schema
    changes create development-time coupling; Monolith First favors a monolith
    for simpler applications and modular data/API boundaries. Enforced module
    ownership and the shared release-cadence condition are Tycho synthesis, and
    the Database per Service page calls the shared option an anti-pattern."
  - `binding`: `src.microservices-patterns`, record
    `read.microservices-shared-database.2026-10-30`, section
    `Pattern: Shared database`, quote "A single database is simpler to
    operate", revision
    `4dc5fcf1a9bdf1d4c97c3ba916f997611cebdc2bc4b87927a6bb0a61c11c5731`.
  - Supporting bindings: Shared database `Pattern: Shared database` quotes
    "A developer uses familiar and straightforward ACID transactions to enforce
    data consistency" and "Development time coupling - a developer working on,
    for example, the OrderService will need to coordinate schema changes with
    the developers of other services that access the same tables."; Database
    per Service `Related patterns` quote "The Shared Database anti-pattern
    describes the problems that result from microservices sharing a database";
    Monolith First `Monolith First` quotes "will slow down a team, favoring a
    monolith for simpler applications" and "the API boundaries and how the data
    is stored".
- `source_support.auxiliary`: add the Saga, Transactional Outbox, Shared
  database and Monolith First record/revision tuples. The Database per Service
  record remains the primary `source_support.ledger_record`.
- `technical_coverage`: `partial-bounded`.
- `notes`: "Failure/recovery and alternative bound 2026-10-30 to
  microservices.io Database per Service, Saga, Transactional outbox and Shared
  database pages plus the existing Monolith First article; replica freshness and
  enforced shared-database ownership remain Tycho guidance. Coverage
  partial-bounded; no promotion."

Summary counters: `failure_recovery_supported` 57 -> 58;
`alternative_supported` 66 -> 67. No technical-coverage counter changes
because the entry was already `partial-bounded`.

### Card registration `edition/patterns/card-batches.v1.json`

Add `card_path: "book/volumes/v11-pattern-atlas/c01-application-boundaries/README.md"`
to the `tycho.pattern.database-per-service` entry. Keep `ledger_record`
`read.microservices-database-per-service.2026-10-21`. The card remains inline;
a later split must keep the two frontmatter source ids, the 2026-10-30 dates and
the owner anchor `database-per-service`. No split is performed by this lane.

### Frontmatter source ids

No new source id is introduced. The V11/C01 chapter already declares
`src.microservices-patterns` and `src.monolith-first`. Do not add source ids
to the owner page; its `evidence_scope` stays empty and the body Source
boundary is the binding record.

### Source register `sources/register.json`

Update the existing `src.microservices-patterns` record; do not add a new
source id.

- `reading_status`: `full-public-page-inspected`.
- `version`: living pattern catalog, accessed 2026-10-30; record that the
  Database per Service, Saga, Transactional outbox and Shared database pages
  were read in full, with their raw HTML digests, and that no version
  identifier is published.
- `access_checked` and `content_verified`: 2026-10-30.
- `verification_scope`: four public pattern pages read in full; the catalog
  index, linked child pages, implementations and benchmarks were not read; the
  three existing 2026-10-21 records reproduced their raw HTML digests.
- Keep the title, publisher, URL, topics, priority, admission, access and
  license notes. The source count stays 285 and `sources/CATALOG.md` does not
  need regeneration for an existing-record update; `validate_sources.py`
  passes in the scratch.

### Content revisions `edition/content-revisions.json`

Add an issue-540 revision with `authorized_at` 2026-10-30 and authorization
"B27 database-per-service failure/recovery and alternative binding; no
promotion or owner acceptance."

- `directory_documents`:
  - owner path previous
    `7fe7f97d8caeda6e55b1665c60afbeaeb41984066e35e78391dc873c68f5023a`
    (migration baseline), current
    `fe200aab9c937e45a4f96b6b873bd9d4b9970ec982266b974ad4fe1006023823`
    (historical-view text after the edit).
  - card path previous
    `0c5c26415aaa4a9d7744579492125d53f10e844bc85e90a881674c28310fed3f`
    (migration baseline), current
    `064882458be87c42218a45aab4925670e877ca1e977dc3d60bcc4d9b5e3db5e7`
    (historical-view text after the edit).
- Leave `source_blocks`, `enrichment_documents`, `enrichment_additions` and
  `enrichment_baselines` empty. The owner page is retained and no page split is
  performed.

### Derived artifacts and tests

The book edit changes one canonical page and one atlas chapter. The coverage
and atlas validators fail on `coverage-registry-hash` and
`atlas-registry-hash` in the scratch until the affected route index, atlas
coverage/census, reverse-map, sufficient-workflow and semantic-audit artifacts
are regenerated once at batch end. Do not treat a stale derived hash as a lane
content failure. The full unit suite is not run; batch-end tests remain with the
integrator.

## Validation

Baseline checker output before the metadata patch, in the lane worktree:

    PASS: V11 prose <=100; 145 exact owner-link exceptions
    PASS: configured lexical boundary checks; independent-origin review still
    required.

After the two book edits only, in the lane worktree:

- `python3 scripts/check_markdown_line_length.py` — PASS.
- `python3 scripts/check_boundary.py` — PASS.
- `python3 scripts/validate_book_metadata.py` — PASS; 481 canonical
  documents.
- `python3 scripts/validate_pattern_cards.py` — PASS; 145 entries.
- `python3 scripts/validate_pattern_registry.py` — PASS; 145 entries.
- `python3 scripts/validate_pattern_owner_units.py` — FAIL
  `owner-units-alternative` because the card alternative changed and shared
  metadata is unchanged; integrator work.
- `python3 scripts/preflight_sufficient.py --pattern
  tycho.pattern.database-per-service` — FAIL: failure/recovery partial,
  alternative partial and `card_path` missing; all three are integrator
  metadata work.
- `python3 scripts/validate_directory_migration.py` — FAIL
  `directory-baseline-payload-drift` until the content revision is applied.
- `python3 scripts/validate_decomposition.py` — PASS; 739 preserved source
  blocks and 174 new question pages.
- `python3 scripts/validate_enrichment.py` — PASS; explicit membership and
  byte conservation.

In the detached scratch copy with the metadata patch above:

    PASS: tycho.pattern.database-per-service
    1/1 entries preflight clean

    PASS: owner units 145 entries, 145 units, 30 shared pages
    PASS: pattern registry 145 entries, 11 families
    PASS: pattern cards 11 batch(es), 145 entries
    PASS: 481 canonical documents
    PASS: 285 source records, mandatory IDs, cross-references and catalogue
    freshness
    PASS: directory migration; 481 canonical documents, 339 moved documents,
    12 post-migration directories
    PASS: decomposition; 739 preserved source blocks, 174 new question pages
    PASS: enrichment; explicit membership and byte conservation
    PASS: V11 prose <=100; 145 exact owner-link exceptions
    PASS: configured lexical boundary checks.

The quote-to-source check in the scratch verified every new binding quote
against the fetched canonical page text. Coverage and atlas remain
registry-hash stale until their batch-end refresh.

## Limits

The binding uses four versioned public pattern pages and one versioned public
article. The pages describe pattern trade-offs; they do not test a dual-write
failure, an outbox relay, an idempotent consumer, a stale replica, a
cross-service query, a shared database or a release cadence. The owner section
and card label the unsupported parts as Tycho guidance. The Database per Service
page and the Shared database page disagree about whether a shared database is a
pattern or an anti-pattern; both readings are preserved.

Coverage remains partial-bounded after the proposed metadata patch. Independent
review, promotion, owner acceptance, CI and merge permission are not claimed.
The prior independent pass reviewed the earlier page hash
`674a7336bcabf914eaafd118f9598b00f211f9eb510ecf06c392db45d0600220` and does
not cover this text.

## Review needs

- Request a fresh external review under the book/atlas gate. The reviewer
  should check quote-to-claim fit for each failure mode, the Tycho labels for
  replica freshness, reconciliation, enforced shared-database ownership and
  release cadence, the Database per Service versus Shared database
  contradiction, the five revisions, the metadata patch and the absence of a
  sufficient claim.
- The reviewer must use read-only repository access and must not run tests.
- Owner acceptance, promotion, CI and merge permission are not claimed.

## Commit scope

The lane commit contains this note and the two book files only:

- the owner path above;
- `book/volumes/v11-pattern-atlas/c01-application-boundaries/README.md`.

No shared JSON, promotion, test or generated file is in the lane commit.
