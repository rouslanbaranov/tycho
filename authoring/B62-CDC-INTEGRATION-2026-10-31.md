# B62 Change Data Capture lane integration

Status: integrated and self-checked on 2026-10-31. Coverage remains
partial-bounded; no promotion, sufficient coverage, owner acceptance or
independent AI review is claimed.

## Commit chain

- Parent: `027e591fd5051599e1211834a92bd6686a49b2a0` (`027e591f`).
- Lane commit cherry-picked: `4c3888c4` ("docs(book): bind CDC invariant,
  recovery and alternative").
- Cherry-pick on this branch: `8b5f2343`, same three files.
- This integration commit applies the shared metadata, the dedicated card
  split, counters, revisions and generated artifacts. It does not change the
  lane's book argument.

## Card split

- Dedicated page:
  `book/volumes/v11-pattern-atlas/c04-consistency-events/change-data-capture-cdc.md`.
- Page identity: `tycho.page.b92e251caf4b47d58bd3101fde058206`.
- Page raw SHA-256:

      7e0cdaf1dcd393add499cfb7f2e8f44c170c019eb1b150c7284413c03051844d

- Page historical-view SHA-256:

      1cc74fb34be6c9564aeae0dacaa5f94df6184a10b1474953446d01547ee46929

- Page body SHA-256:

      9fbbc6c597122ed2a209cc6afde4ee1712402342c3f9070093623b966e0fba29

- README raw SHA-256:

      2d94a3f8d757fec8ea753541b44994882cc7cdfba5d5f7d81458bfc85401000f

- README historical-view SHA-256:

      7aab3f02a3f572e42bb5996533f234c94d13cd50c6ccaa32f359688723979f93

- Owner page raw SHA-256:

      8df7cdb40625aaafdd65e8803b7a6682e56483b7af0b00a276deff5faa287b75

- Owner page historical-view SHA-256:

      6998460d751e03ab8f0836a783dd843e76a3b2e996986ec9220e6fe440698c68

- Owner page body SHA-256:

      b86656379ef84e385f345d4f5921967e437ec7b9c2e869ba62aa4fef239411b4

- The card moved from the shared chapter page; the section heading becomes the
  page H1. The README keeps `### Change Data Capture (CDC)` with a link to the
  dedicated card, so the owner backlink at
  `cdc-state.md#change-data-capture-cdc` resolves through the chapter anchor.
  The chapter page drops the six card-only source ids; the pre-existing
  `src.debezium-outbox` and `src.postgres-logical` remain as chapter history.
- The card section is 655 body words; the page is 140 lines. The owner page is
  253 lines with 1,727 body words; the owner heading is line 154.

## Applied metadata

- `sources/register.json`: 329 -> 335 sources. Added
  `src.debezium-architecture`, `src.debezium-postgresql`,
  `src.postgres-logical-decoding`, `src.postgres-replication-config`,
  `src.kafka-connect` and `src.kafka-connect-guide`; the source catalogue was
  regenerated.
- `edition/patterns/reading-ledger.v1.json`: 295 -> 301 records. Added
  `read.debezium-architecture.2026-10-31`,
  `read.debezium-postgresql.2026-10-31`,
  `read.postgres-logical-decoding.2026-10-31`,
  `read.postgres-slot-retention.2026-10-31`,
  `read.kafka-connect-offsets.2026-10-31` and
  `read.kafka-connect-overview.2026-10-31`. The retained
  `read.debezium-outbox-binding.2026-10-31` supports the alternative.
  `read.batch8-postgres-logical.2026-10-22` and
  `read.batch2-debezium-outbox.2026-10-21` move to `foundation_records` with
  `citation_status: intentionally-unused`.
- `edition/patterns/source-plan.v1.json`: the entry takes the six selected
  units plus the retained outbox unit. Summary: 342 required, 341 read, 301
  ledger records; planned stays 0 and blocked stays 1.
- `edition/patterns/registry.v1.json`: seven read source units for the entry;
  technical owner, atlas owner and overall coverage move to partial-bounded.
- `edition/patterns/owner-units.v1.json`: mechanism, invariant,
  failure/recovery and alternative are `supported`, each with one primary
  binding and supporting bindings. The owner line moves 129 -> 154. Technical
  and decision coverage stay partial-bounded. Counters: mechanism 123
  (unchanged), invariant 92 -> 93, failure/recovery 87 -> 88, alternative
  92 -> 93, technical partial-bounded 15 -> 16, technical partial 55 -> 54,
  technical sufficient 75 and decision counters unchanged.
- `edition/patterns/card-batches.v1.json`: the entry gains the dedicated
  `card_path` and cites `read.postgres-logical-decoding.2026-10-31`.
- `edition/content-revisions.json`: one issue-540 revision authorizes the
  owner-page and chapter historical-view changes plus owner source block 1. The
  new page baseline is its historical-view hash, so it needs no separate
  authorization.
- `edition/atlas-manifest.json`, `edition/directory-migration.json`,
  `sources/document-identities.json` and
  `edition/patterns/semantic-audit.v1.json`: register the page, identity,
  baseline and atlas review entry. Atlas documents move 90 -> 91; directory
  documents move 513 -> 514; semantic-audit pages move 513 -> 514.
- Route index (snapshot `3486557e...`), section index, census, coverage and
  reverse maps, phase 4, semantic summary, qrels, inventory, sufficient
  candidates, review reconciliation and re-review packets were refreshed. Test
  guards move to 91 atlas documents, 91 V11 documents, 342 registry units, 341
  read units and 301 ledger records. Delivery counters move to 54 technical
  partial and 16 technical partial-bounded at 514 pages and 335 sources.
- The 2026-10-22 re-review record now pins its historical
  `reviewed_page_sha256`; the CDC packet status becomes
  `page-changed-since-review`. Reviewed packets move 46 -> 45 and changed
  packets 89 -> 90.

## Deviations from the lane note

- The lane leaves the card inline at V11/C04. The task and the card granularity
  policy require a dedicated page, so the card moves and the chapter keeps a
  stub link at the stable anchor. It is registered as id, manifest document,
  directory record, document identity and card path.
- The lane proposes technical and decision coverage `sufficient`. The task
  keeps partial-bounded, so the four dimensions are supported while coverage
  stays partial-bounded and no promotion is recorded.
- The lane sets the owner page `source_inspection_date` to 2026-10-31. The page
  is a decomposition question page, and `validate_decomposition.py` requires a
  null inspection date for pages without `fresh_source_ids`. The integration
  restores it; the binding remains in the shared ledger, owner units and
  dedicated card.
- The lane's plan sections are expanded where the ledger records additional
  read sections, because the source-plan and ledger schemas require identical
  section lists; `truncate events` is named so the single-partition limit can
  be bound.
- The lane leaves the outbox unit on the historical batch-2 record. The
  integration binds the outbox alternative to
  `read.debezium-outbox-binding.2026-10-31`, which the card cites, and keeps
  the older records in `foundation_records`.
- The lane lists the historical PostgreSQL logical-replication record as an
  auxiliary. The owner-unit validator only accepts a plan unit as an
  auxiliary, so the record stays historical in the metadata notes rather than
  as a binding.
- The lane proposes no registry content change. The task requires registry
  units, so the registry entry mirrors the seven plan units and the
  partial-bounded coverage.

## Validation

- `python3 scripts/preflight_sufficient.py --pattern
  tycho.pattern.change-data-capture-cdc`: PASS, 1/1.
- `python3 scripts/premerge_check.py --branch
  feature/TYCHO-540-b9-coverage-growth --issue-title '[E17-89] B9 coverage
  growth'`: PASS. Full suite: 688 tests OK (44.9 s). One intermediate run
  stopped on a stale sufficient-candidate matrix after the historical review
  pin; it was regenerated forward before the final pass.
- PASS: sources (335), source catalogue, source plan (342 required, 341 read,
  301 records), registry (342 units), owner units, cards, atlas (91 documents),
  coverage, phase 4 (514 pages), semantic audit (514 pages), delivery evidence,
  edition, directory migration (514 documents), decomposition, book metadata
  and page census.
- PASS: V11 prose line length, 145 exact owner-link exceptions.
- PASS: configured lexical boundary checks; independent-origin review remains
  required.
- PASS: `git diff --check`.
- `book_change.py --plan`: clean, no changed pages, missing revisions or stale
  artifacts.

## Limits

- Partial-bounded coverage only; no Change Data Capture (CDC) promotion,
  sufficient coverage or owner acceptance.
- No external AI content review was run for this integration; the book and
  atlas review gate remains outstanding and is not waived.
- The integrator applied the lane's recorded revisions. No source was
  re-fetched, and no CDC, connector, replication-slot, benchmark or failure
  exercise was run.
- The Debezium and Kafka Connect pages are living documentation; PostgreSQL 18
  is the current documentation. The digests pin the 2026-10-31
  representations, not future revisions.
- The per-key/partition and transaction-grouping rule, the monitoring rule, the
  resnapshot procedure and the dual-write comparison remain Tycho guidance, not
  source claims.
