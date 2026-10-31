# B56 Session Consistency split and metadata integration

Status: integrated and self-checked on 2026-10-31. Coverage remains
partial-bounded; no promotion, sufficient coverage, owner acceptance or
independent AI review is claimed.

## Commit chain

- Parent: `b0d651e3f785750f880d2552aa6a2b2d622bf9bb` (`b0d651e3`).
- B56 book-binding cherry-pick: `b7c7a2e1` from source `d4182e74`
  (`docs(session-consistency): bind four dimensions to public sources`).
- This integration: dedicated card page, shared metadata, counters and tests.

The cherry-pick applied cleanly. It contains the B56 lane note, the V04/C02
owner-page edits and the expanded inline V11/C08 card.

## Card split

- Dedicated page:
  `book/volumes/v11-pattern-atlas/c08-coordination/session-consistency.md`.
- Page identity: `tycho.page.8679c110343d4dfd862c15581b49c350`.
- Page raw SHA-256:

      3b7e064b5f002f97e1ecdb0eea77fb7a03adc2963d2f8a5aa32dc1d7bd77343c

- Historical-view SHA-256:

      396451b729a024befd53f377461c83f3ecfb0bd1bfc6a6dede7c50f60dd301b8

- Body SHA-256:

      f19ebad72a6ff6faade8c5ff4dde8fe5e012caaa8ac6e83ad08dcfa87c917966

- README raw SHA-256:

      b7f4b4e8a04a7d7b42242647374b362128697f4d0c8588f6a6d96ef1072e4c69

- README historical-view SHA-256:

      721171455cd2769bee2bb6051e2a6a9399bb96e7cb997d5dac3fdc324c5694aa

- Owner page raw SHA-256:

      25c2e61320bc437d94a16b7fa75835cba446c97e021692163b9ccb6f448c9363

- Owner page historical-view SHA-256:

      30c8ddb361b07179d7a63acfdc5e797db044dacdfcd73a769c99d1be87935862

- The card body moved from the README section to the new page; the section
  heading becomes the page H1. The README keeps `### Session Consistency`
  and points to the dedicated card, so the owner backlink
  (`README.md#session-consistency`) and the card owner link both resolve.
  The moved body is 62 body lines and 467 words; the page is 120 lines with
  frontmatter and 605 words.
- The README drops the five session-only source ids, which now belong to the
  dedicated page; the chapter source list keeps the ids used by other C08
  cards.
- The page and card wording no longer calls the five records proposed or
  absent from the ledger; the integration records the registered state.

## Applied metadata

- `sources/register.json`: 320 -> 322 sources. Added
  `src.azure-cosmos-consistency` and `src.mongodb-causal-consistency`;
  `src.jepsen-session-models`, `src.jepsen-read-your-writes` and
  `src.jepsen-monotonic-reads` gain the 2026-10-31 representations, access
  dates, readers and verification scopes. The source catalogue was
  regenerated.
- `edition/patterns/reading-ledger.v1.json`: 268 -> 273 records. The five
  new records are `read.azure-cosmos-consistency.2026-10-31`,
  `read.mongodb-causal-consistency.2026-10-31`,
  `read.jepsen-consistency-models.2026-10-31`,
  `read.jepsen-read-your-writes.2026-10-31` and
  `read.jepsen-monotonic-reads.2026-10-31`. The retained
  `read.batch4-jepsen.2026-10-21` record is marked
  `intentionally-unused` and added to the foundation records because the
  card and plan now cite the 2026-10-31 reads.
- `edition/patterns/source-plan.v1.json`: 314/313/268 -> 318/317/273
  required/read/ledger; blocked stays 1. The session entry takes R1-R5 in
  lane order with exact sections, URLs and record ids.
- `edition/patterns/registry.v1.json`: source units 314 -> 318. The session
  entry gains five bound units; technical owner, atlas owner, technical
  coverage, decision coverage and overall coverage move to
  `partial-bounded`; notes name the five units.
- `edition/patterns/owner-units.v1.json`: all four dimensions are
  `supported`, each with one primary binding and supporting bindings. The
  owner line moves 153 -> 155, `source_support.ledger_record` is
  `read.azure-cosmos-consistency.2026-10-31`, the other four records are
  auxiliary, and `decision_evidence.competing_alternative` is rebased to
  the edited card text. Counters: mechanism 121 -> 122, invariant 86 -> 87,
  failure/recovery 81 -> 82, alternative 86 -> 87, technical partial-bounded
  15 -> 16 and technical partial 61 -> 60. Decision partial-bounded stays 76
  and sufficient stays 69.
- `edition/patterns/card-batches.v1.json`: the entry gains the dedicated
  `card_path` and the new Azure ledger citation.
- `edition/content-revisions.json`: one issue-540 revision authorizes the
  owner page and README historical-view changes and the updated enrichment
  record. It stores historical-view hashes: owner
  `b6183720...` -> `30c8ddb3...`, README `1760eebb...` ->
  `72117145...` and enrichment `7968e33b...` -> `30c8ddb3...`.
  The note's raw base/result pair for the owner page is recorded above and in
  the lane note.
- `edition/atlas-manifest.json`, `edition/directory-migration.json`,
  `sources/document-identities.json` and
  `edition/patterns/semantic-audit.v1.json`: register the page identity,
  manifest entry, directory baseline, document identity and atlas review
  entry. Directory documents move to 510 and V11 documents to 87.
- `edition/enrichment-manifest.json` and
  `sources/enrichment-inspections-2026-10-20.json`: the session-consistency
  owner record takes the five source ids and the 2026-10-31 inspection date;
  the two new sources receive environment-free inspection entries.
- Delivery evidence moves to 322 sources, 273 ledger records, 60 technical
  partial and 16 technical partial-bounded. The delivery-evidence schema
  constants and the phase4/semantic-audit item limits move to 273, 322 and
  510.
- Route and section indexes, census, coverage/reverse maps, phase 4,
  semantic summary, qrels, inventory, sufficient candidates and re-review
  packets were refreshed. Guards move to 510 pages, 87 V11 documents,
  318 registry units, 317 read units and 273 ledger records. Packet counts
  move to 47 reviewed, 88 page-changed and 10 awaiting.

## Deviations from the B56 note

- The note leaves the card inline. The task and the card granularity policy
  require a dedicated page, so the card moves and the README keeps a stub
  link at the stable anchor.
- The note proposes `technical_coverage: supported` for the registry and
  owner units. The task keeps partial-bounded; the validator derives
  `partial-bounded` without a promotion.
- The note quotes raw owner hashes. The repository authorizes historical-view
  hashes in content revisions; both sets are recorded above.
- The note leaves the "proposed" and "not yet in the shared reading ledger"
  wording on the card and in the owner notes. The integration records the
  registered state instead.
- The note gives the owner section start line 153. The final heading is line
  155 after the frontmatter source-id additions; the owner section is 77 lines
  and 874 words (line 155 through EOF).
- The note says to keep the chapter review date and notes unchanged. The
  integration follows that; the README's card anchor and owner backlink are
  unchanged.

## Validation

- `preflight_sufficient.py --pattern tycho.pattern.session-consistency`:
  PASS, 1/1.
- PASS: sources (322), source catalogue, source plan (317 read, 273
  records), registry (318 units), owner units, cards, atlas (87 documents),
  coverage, phase 4 (510 pages), semantic audit (510 pages), delivery
  evidence, edition, directory migration (510 documents), enrichment,
  decomposition, book metadata, claim references, corpus qrels, sufficient
  promotions, owner acceptance, AI reviews and sufficient pilot.
- PASS: V11 prose line length, 145 exact owner-link exceptions.
- PASS: configured lexical boundary checks; independent-origin review remains
  required.
- PASS: `git diff --check`.
- `book_change.py --plan`: clean, no changed pages, missing revisions or
  stale artifacts.
- Full suite: 709 tests pass (709 OK, 45.624 s).
- `validate_book_navigation.py` still reports the four pre-existing
  missing-local-anchor issues in untouched V08/V09 pages recorded in the
  hand-off; outside this change.

## Limits

- Partial-bounded coverage only; no Session Consistency promotion, sufficient
  coverage or owner acceptance.
- No external AI content review was run for this integration; the book/atlas
  review gate remains outstanding and the existing review for the owner page
  is stale after the B56 edit.
- The integrator applied the lane's recorded revisions. No source was
  re-fetched, and no database, replica set, partition, client session or
  failover was created or run.
- All five units are living public documentation pages, not benchmarks,
  standards or production observations. Their digests pin the 2026-10-31
  representations, not future revisions.
- The token lifetime, epoch/lineage comparison, multiwriter frontier,
  validation and rejection rules remain Tycho synthetic guidance. The moved
  card is a verbatim decomposition move plus frontmatter and two
  registration-label edits; the README stub, owner page and new page are
  self-checked, not independently reviewed.
