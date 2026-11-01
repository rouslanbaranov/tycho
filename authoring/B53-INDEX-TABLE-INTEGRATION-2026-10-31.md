# B53 Index Table split and metadata integration

Status: integrated and self-checked on 2026-10-31. Coverage remains
partial-bounded; no promotion, owner acceptance or independent AI review is
claimed.

## Commit chain

- Parent: `3139b632a72227660e557001dbc0e806d1177473` (`3139b632`).
- B53 book-binding cherry-pick: `bb57a8cb` from source `ba3da089`
  (`docs: bind Index Table dimensions to four public sources`).
- This integration: dedicated card page, shared metadata, counters and tests.

The cherry-pick applied cleanly. It contains the B53 lane note, the V05/C03
owner edits and the expanded inline V11/C06 card.

## Card split

- Dedicated page:
  `book/volumes/v11-pattern-atlas/c06-database-storage/index-table.md`.
- Page identity: `tycho.page.41daaaaf1b34f0d26e3346804ac0e85e`.
- Page raw SHA-256:

      f967b13fbd7572c9dcdd68db01f7fe1120f299252510186077caed26e792c93a

- Historical-view SHA-256:

      8c76f63c5a11b8fa9919f853b0ba87e5a052ac153807c50b58a7180a3a344c3a

- Body SHA-256:

      bca9999ec64fccc1ca636dd9820ab5696bf49ae2c074cda7aaad76524c28ffd8

- README raw SHA-256:

      cec0559914457314e578715d7e03f69e12ad5493e859478c9f5eced4cf3a63aa

- README historical-view SHA-256:

      3d9ce3ecbba6d98dceb3778619e8a93ca6ccf785bbdd19e0a11bc9000ec34417

- Owner page raw SHA-256:

      dfef693ea2541715c3c64493dc465ac1e4823fb3a946bdad2e35bc69d10607e8

- Owner page historical-view SHA-256:

      67d0e8235c323681cba8393cab19f2d72b061b662756a13da9848fce637b31ff

- The card moved verbatim from the shared chapter page; the section heading
  becomes the page H1. The README keeps `### Index Table` and points to the
  dedicated card, so the owner backlink (`README.md#index-table`) and the card
  owner link both resolve. The card section is 51 body lines and 352 words;
  the page is 108 lines with frontmatter and 355 words.
- The README drops the three card-only source ids, which now belong to the
  dedicated page; `src.postgresql` remains because other C06 cards cite it.

## Applied metadata

- `sources/register.json`: 315 -> 318 sources. Added
  `src.microsoft-sql-server`, `src.use-the-index-luke` and
  `src.aws-dynamodb-gsi`; `src.postgresql` gains the PostgreSQL 17 section 11.9
  representation, access and content-verified dates 2026-10-31, and the
  11.9 verification scope. The source catalogue was regenerated.
- `edition/patterns/reading-ledger.v1.json`: 253 -> 257 records. The four new
  records are `read.pg17-index-only-scans.2026-10-31`,
  `read.microsoft-included-columns.2026-10-31`,
  `read.luke-index-only-scan.2026-10-31` and
  `read.aws-dynamodb-gsi-overloading.2026-10-31`. The retained
  `read.batch3-pg-indexes.2026-10-21` record is unchanged and stays the card
  citation.
- `edition/patterns/source-plan.v1.json`: 301/300/253 -> 305/304/257
  required/read/ledger; blocked stays 1. Four units are appended to the
  index-table entry after the retained PostgreSQL chapter unit in R1-R4 order,
  and its notes name the 2026-10-31 binding.
- `edition/patterns/registry.v1.json`: the entry gains four source units (five
  total); the technical owner and technical/overall coverage move to
  `partial-bounded`; decision coverage stays `partial-bounded`. The notes name
  the four bindings.
- `edition/patterns/owner-units.v1.json`: all four dimensions are
  `supported`, with one primary binding plus supporting bindings each. The
  owner line moves 104 -> 107, and `unit_terms` is rebased from
  `native secondary index` to `native covering index`, the wording the lane
  edited. Counters: mechanism 118 -> 119, invariant 83 -> 84, failure/recovery
  78 -> 79, alternative 83 -> 84, technical partial-bounded 15 -> 16 and
  technical partial 64 -> 63. The retained PostgreSQL record remains the card
  citation; the four new records are auxiliary source support.
- `edition/patterns/card-batches.v1.json`: the entry gains the dedicated
  `card_path`; the retained `read.batch3-pg-indexes.2026-10-21` record stays
  the card ledger citation.
- `edition/content-revisions.json`: one issue-540 revision authorizes the
  owner page and README historical-view changes, using the historical-view
  hashes the repository stores. The new page baseline is its historical-view
  hash, so it needs no separate authorization.
- `edition/atlas-manifest.json`, `edition/directory-migration.json`,
  `sources/document-identities.json` and
  `edition/patterns/semantic-audit.v1.json`: register the page, identity,
  baseline and atlas review entry. Directory documents move to 508 and V11
  documents to 85.
- Route and section indexes, census, coverage/reverse maps, phase 4, delivery
  evidence, semantic summary, qrels, inventory, sufficient candidates and
  re-review packets were refreshed. Guards move to 508 pages, 85 V11
  documents, 305 registry units, 304 read units and 257 ledger records.
  Delivery counters move to 63 technical partial and 16 technical
  partial-bounded; decision partial-bounded stays 79.
- `edition/patterns/sufficient-review-records.v1.json`: the index-table
  re-review record gains `reviewed_page_sha256` with its own recorded page hash
  `5ed6aead...`, so the later evidence wave is explicit rather than silently
  treated as reviewed. Packet counts move to 49 reviewed and 86 page-changed;
  the lane's stale-review warning stands and no review is claimed for the
  moved card.
- Phase 4 regeneration also reconciles the promoted Cache Stampede entry to
  its registry state: its audit row now records the technical owner and both
  coverage fields as sufficient. The promotion commit had left that row at
  partial; the refreshed artifact follows the registry.

## Deviations from the B53 note

- The note leaves the card inline. The task and the card granularity policy
  require a dedicated page, so the card moves verbatim and the README keeps a
  stub link at the stable anchor.
- The note advances the owner `source_inspection_date` to 2026-10-31. The page
  is a decomposition question page, and `validate_decomposition.py` requires a
  null inspection date for pages without `fresh_source_ids`. The integration
  restores null; the 2026-10-31 inspection remains recorded in the shared
  ledger, the owner-unit bindings and the dedicated card.
- The note gives owner-unit line 104. The lane edit shifted the
  `### Index Table` heading to line 107, so the owner-unit line is corrected.
- The note's owner `unit_terms` include `native secondary index`, which the
  lane wording no longer contains. The integration uses
  `native covering index` from the edited section.
- The note leaves the card-batch registration without a `card_path`. The
  integration adds it, as the task requires.
- The note quotes raw owner and card hashes for `content-revisions`. The
  repository authorizes historical-view hashes, so the revision stores
  `67d0e823...` and `3d9ce3ec...`.
- The owner-unit `decision_evidence` fields are rebased to the edited card's
  decision question and competing alternative; the old values no longer match
  the card.
- `schemas/pattern-delivery-evidence.v1.schema.json` pins 257 ledger records
  and 318 sources; the phase 4 and semantic audit schemas allow 508 pages.
- `preflight_sufficient.py --all-supported` also selects
  `tycho.pattern.branch-by-abstraction`, whose missing card path and
  source-support entry predate this integration and are untouched.

## Validation

- `preflight_sufficient.py --pattern tycho.pattern.index-table`: PASS, 1/1.
- PASS: sources (318), source catalogue, registry, atlas (85 documents),
  coverage, cards, owner units, source plan (304 read, 257 records),
  directory migration (508 documents), edition, enrichment, decomposition,
  semantic audit (508 pages), phase 4 (508 pages), delivery evidence,
  sufficient promotions, sufficient pilot, owner acceptance, AI reviews,
  claim references, corpus qrels and page census.
- PASS: V11 prose line length, 145 exact owner-link exceptions.
- PASS: configured lexical boundary checks; independent-origin review remains
  required.
- PASS: `git diff --check` (no whitespace errors).
- `validate_book_navigation.py` still reports four missing local anchors in
  untouched dark-launching and RBAC/ABAC pages; unchanged from earlier notes.
- Full suite: 688 tests pass (688 OK). The batch-end run was repeated
  after one review-record assertion and one stale-artifact failure; both were
  resolved, the artifacts refreshed, and the final run is clean.

## Limits

- Partial-bounded coverage only; no Index Table promotion, sufficient coverage
  or owner acceptance.
- No external AI content review was run for this integration; the book/atlas
  review gate remains outstanding and the existing sufficient review is stale
  for the changed owner page.
- The integrator applied the lane's recorded revisions. No source was
  re-fetched, and no database, index, query plan, GSI or covering scan was
  executed.
- PostgreSQL 17 and Microsoft Learn pages are versioned or living
  documentation; the Use The Index, Luke chapter is a living practitioner
  book page; the DynamoDB topic is a short developer-guide page. Their raw and
  canonical digests pin the 2026-10-31 representations, not release tags.
- The PostgreSQL served Date header predates the retrieval wall time; the
  content digests, not the header, are the binding evidence. Luke's
  Last-Modified header varied between fetches while its raw digest stayed
  stable.
- The canonical-text extraction uses the repository script's fallback
  whole-page text because the four pages expose no article-body marker; the
  digests cover page chrome as well as article prose.
- The moved card is a verbatim decomposition move plus frontmatter; the
  README stub, owner page and new page are self-checked, not
  independently reviewed.
