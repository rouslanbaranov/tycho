# B63 Online Data Migration lane integration

Status: integrated and self-checked on 2026-10-31. Coverage remains
partial-bounded; no promotion, sufficient coverage, owner acceptance or
independent AI review is claimed.

## Commit chain

- Parent: `09bbe5a622e367c35f3fe38c8132c725ebaa68ac` (`09bbe5a6`).
- Lane commit cherry-picked: `68f7f625` ("docs(book): bind online data
  migration invariant, recovery and alternative").
- Cherry-pick on this branch: `4c011047`, same three files.
- This integration commit applies the shared metadata, the dedicated card
  split, counters, revisions and generated artifacts. It does not change the
  lane's book argument.

## Card split

- Dedicated page:
  `book/volumes/v11-pattern-atlas/c06-database-storage/online-data-migration.md`.
- Page identity: `tycho.page.480477bf68a84b33b01440df8a0ccc96`.
- Page raw SHA-256:

      6fa17c1c0edefc9106efdd86bce77a5ec468b7cb696e090ae7f64bf4ec876550

- Page historical-view SHA-256:

      20932fc0df6fb64a4985d393c31366927101e0b892dddf594315885271171316

- Page body SHA-256:

      67ea94071d4ea99654bc68fb017c9ae29553974e68b655a16b43d3af08220b6b

- README raw SHA-256:

      d8f2fae9f924922f659b4e2671e54196c1a585c210d511abd252031f2c2d223a

- README historical-view SHA-256:

      d2792204f23d6cd53d967b31d16757973157ed80af7b884fd77fa6ab467f0002

- Owner page raw SHA-256:

      2e7e3c39dc022fd34b23c2d8d1378aac1bd6898ef42020db3c64e82c4b2f6251

- Owner page historical-view SHA-256:

      c7e23d92c3c47077b0f980bfafcc53dbb68e3a65a00ca45aa92a9ceedfe27f36

- Owner page body SHA-256:

      0211b5c7bd99ebaa9a0154e6e7830bb29ba61e42b74e6cf03d7322d42f36f341

- The card moved from the shared chapter page; the section heading becomes the
  page H1. The README keeps `### Online Data Migration` with a link to the
  dedicated card, so the owner backlink at
  `migration-retirement.md#online-data-migration` resolves through the chapter
  anchor. The chapter page drops the three card-only source ids added by the
  lane; the pre-existing `src.postgresql`, `src.flyway` and `src.gh-ost`
  remain as chapter history.
- The card section is 340 body words; the page is 104 lines. The owner page is
  286 lines with 2,749 body words; the owner heading is line 223.

## Applied metadata

- `sources/register.json`: 335 -> 337 sources. Added `src.aws-dms` and
  `src.flyway-expand-contract`; `src.m9-st01` moves from
  `pending-content-access` / `fetch-incomplete` to `admitted-for-research` /
  `full-public-page-inspected`; `src.postgresql` gains the pg_dump and COPY
  revision notes; the source catalogue was regenerated.
- `edition/patterns/reading-ledger.v1.json`: 301 -> 307 records. Added
  `read.stripe-online-migrations.2026-10-31`,
  `read.postgres-pgdump.2026-10-31`, `read.postgres-copy.2026-10-31`,
  `read.aws-dms-overview.2026-10-31`, `read.aws-dms-cdc.2026-10-31` and
  `read.flyway-expand-contract.2026-10-31`. The retained
  `read.batch3-gh-ost.2026-10-21` moves to `foundation_records` with
  `citation_status: intentionally-unused`.
- `edition/patterns/source-plan.v1.json`: the entry takes the six selected
  units. Summary: 347 required, 346 read, 307 ledger records; planned stays 0
  and blocked stays 1.
- `edition/patterns/registry.v1.json`: six read source units for the entry;
  technical owner, atlas owner and overall coverage move to partial-bounded,
  with confidence high.
- `edition/patterns/owner-units.v1.json`: mechanism, invariant,
  failure/recovery and alternative are `supported`, each with one primary
  binding and supporting bindings. The owner line moves 215 -> 223. Technical
  and decision coverage stay partial-bounded. Counters: mechanism 123
  (unchanged), invariant 93 -> 94, failure/recovery 88 -> 89, alternative
  93 -> 94, technical partial-bounded 15 -> 16, technical partial 55 -> 54,
  decision counters unchanged. The sibling Expand-and-Contract owner line moves
  200 -> 208 after the lane's frontmatter growth.
- `edition/patterns/card-batches.v1.json`: the entry gains the dedicated
  `card_path` and cites `read.stripe-online-migrations.2026-10-31`.
- `edition/content-revisions.json`: one issue-540 revision authorizes the
  owner-page and chapter historical-view changes plus the owner enrichment
  baseline. The new page baseline is its historical-view hash, so it needs no
  separate authorization.
- `edition/atlas-manifest.json`, `edition/directory-migration.json`,
  `sources/document-identities.json`,
  `edition/patterns/semantic-audit.v1.json` and
  `edition/patterns/sufficient-review-records.v1.json`: register the page,
  identity, baseline and atlas review entry, and pin the historical reviewed
  hash for the sibling Expand-and-Contract record. Atlas documents move
  91 -> 92; directory documents move 514 -> 515; semantic-audit pages move
  514 -> 515; review packets move 45 reviewed / 90 changed to 43 reviewed /
  92 changed.
- Route index (snapshot `d4c2cff8...`), section index, census, coverage and
  reverse maps, phase 4, semantic summary, qrels, inventory, sufficient
  candidates, review reconciliation and re-review packets were refreshed.
  Test guards move to 92 atlas documents, 92 V11 documents, 347 registry units,
  346 read units and 307 ledger records. Delivery counters move to 53 technical
  partial and 16 technical partial-bounded at 515 pages and 337 sources.
- Schema page caps move to 515 for phase 4 and the semantic audit; delivery
  evidence pins 307 ledger records and 337 sources. These are counter bumps, not
  evidence relaxation.

## Deviations from the lane note

- The lane leaves the card inline at V11/C06. The task and the card granularity
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
  section lists.
- The lane leaves the gh-ost unit as an auxiliary. The source-plan schema has
  no historical unit kind and the owner-unit validator only accepts a plan unit
  as an auxiliary, so the record stays in `foundation_records` and is named in
  the notes instead of as a current binding.

## Validation

- `python3 scripts/preflight_sufficient.py --pattern
  tycho.pattern.online-data-migration`: PASS, 1/1 clean.
- `python3 scripts/premerge_check.py --branch
  feature/TYCHO-540-b9-coverage-growth --issue-title '[E17-89] B9 coverage
  growth'`: PASS. Full suite: 688 tests OK (69.5 s). Two intermediate runs
  stopped on a stale sufficient-candidate matrix and a stale re-review packet
  source after the historical review pin; both were regenerated forward before
  the final pass.
- PASS: sources (337), source catalogue, source plan (347 required, 346 read,
  307 records), registry (347 units), owner units, cards, atlas (92 documents),
  coverage, phase 4 (515 pages), semantic audit (515 pages), delivery evidence,
  edition, directory migration (515 documents), decomposition, book metadata
  and page census.
- PASS: V11 prose line length, 145 exact owner-link exceptions.
- PASS: configured lexical boundary checks; independent-origin review remains
  required.
- PASS: `git diff --check`.
- `book_change.py --plan`: clean, no changed pages, missing revisions or stale
  artifacts.

## Limits

- Partial-bounded coverage only; no Online Data Migration promotion, sufficient
  coverage or owner acceptance.
- No external AI content review was run for this integration; the book and
  atlas review gate remains outstanding and is not waived.
- The integrator applied the lane's recorded revisions. No source was
  re-fetched, and no Stripe, PostgreSQL, AWS DMS, Flyway, benchmark, restore or
  migration exercise was run.
- The AWS DMS and Flyway pages are living documentation; the digests pin the
  2026-10-31 representations, not future revisions.
- The changed business-key mapping, the replay-window procedure and the
  stop-the-world quiesce/export/load/verify shape remain Tycho guidance, not
  source claims.
