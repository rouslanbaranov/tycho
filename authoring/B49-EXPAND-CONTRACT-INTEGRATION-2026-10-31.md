# B49 Expand-and-Contract split and metadata integration

Status: integrated and self-checked on 2026-10-31. Coverage remains
partial-bounded; no promotion, owner acceptance or independent AI review is
claimed.

## Commit chain

- Parent: `6ff2546cc57c2f670744fe1dbcaf875a2a01e311` (`6ff2546c`).
- B49 book-binding cherry-pick: `7307fe8e`, source `577c44a3` (final amended
  lane commit).
- This integration: dedicated card page, shared metadata, counters and tests.

The cherry-pick applied cleanly. It contains the B49 lane note, the V08/C05
owner edits and the updated inline V11/C10 card.

## Card split

- Dedicated page:
  `book/volumes/v11-pattern-atlas/c10-deployment-modernization/expand-and-contract.md`.
- Page identity: `tycho.page.301477f3c7324fe8932d3a2608516a20`.
- Page raw SHA-256:

       a13db7e9176aa67b57b540946c924a1bbd8c32eb65a807b4d813f6c957e081a1

- Historical-view SHA-256:

       66518f71e9f3e18d5ec8bbc172de212ce5f6900a3793841fa0267ddf295da4c4

- Body SHA-256:

       798d65aebd7d1654b41689e744e6fc1c1ac469e36eebecfa97007b1886f3bbd4

- README raw SHA-256:

       ca9f17e7795c178b18fa6433b83c70080d30e1cabaf6571996abd5c89761e7a3

- README historical-view SHA-256:

       60e2ab91bd662787c8952b7257ca0caf79215da761b8a4f6f833dc054b3b39bd

- Owner page raw SHA-256:

       e7fa8a1d3e6b49dbd7f282321ed4b416133c7121815a04e40ecef2dfbf0d3385

- Owner page historical-view SHA-256:

       487690d2f57e71b8d326231ff4e9b56628c5e4f57f64d4d769a1ee3eee392db5

- The README keeps `### Expand-and-Contract` and points to the dedicated card.
  The owner backlink remains the README anchor and the card keeps the owner
  link. The owner section is level 3 at line 104.

## Applied metadata

- `sources/register.json`: 306 -> 307 sources. `src.fowler-parallel-change`
  is added with public origin, access dates, representation hashes and the
  licence note. `src.postgresql` and `src.mysql` gain their 2026-10-31
  ALTER TABLE, explicit-locking and online-DDL scopes. The source catalogue was
  regenerated.
- `edition/patterns/reading-ledger.v1.json`: 226 -> 231 records. The five new
  records are `read.fowler-parallel-change.2026-10-31`,
  `read.postgresql-alter-table.2026-10-31`,
  `read.postgresql-explicit-locking.2026-10-31`,
  `read.mysql-online-ddl.2026-10-31` and
  `read.mysql-alter-table.2026-10-31`. The AWS record is retained unchanged.
- `edition/patterns/source-plan.v1.json`: 272/271/226 ->
  278/277/231 required/read/ledger; blocked stays 1. Six units are appended:
  Fowler, the retained AWS data-synchronization page, PostgreSQL ALTER TABLE,
  PostgreSQL Explicit Locking, MySQL Online DDL and MySQL ALTER TABLE.
- `edition/patterns/registry.v1.json`: source units 272 -> 278; the technical
  owner and technical/overall coverage move to `partial-bounded`; decision
  coverage stays `partial-bounded`.
- `edition/patterns/owner-units.v1.json`: all four dimensions are
  `supported` with one primary binding and supporting bindings each; the
  source support names Fowler as primary and six auxiliary records. Counters:
  mechanism 115 -> 116, invariant 80 -> 81, failure/recovery 74 -> 75,
  alternative 79 -> 80; technical partial-bounded 15 -> 16 and technical
  partial 68 -> 67; sufficient stays 62.
- `edition/patterns/card-batches.v1.json`: the entry gains the dedicated
  `card_path`; the Fowler record becomes its primary cited record.
- `edition/content-revisions.json`: one issue-540 revision authorizes the
  owner page and README historical-view changes. The new page baseline is its
  historical-view hash, so it needs no separate authorization.
- `edition/atlas-manifest.json`, `edition/directory-migration.json`,
  `sources/document-identities.json` and
  `edition/patterns/semantic-audit.v1.json`: register the page, identity,
  baseline, documents count 504 and atlas review entry.
- Route and section indexes, census, coverage/reverse maps, phase 4, delivery
  evidence, semantic summary, qrels, inventory, sufficient candidates and
  re-review packets were refreshed. Guards move to 504 pages, 81 V11
  documents, 278 registry units, 277 read units and 231 ledger records.

## Deviations from the B49 note

- The note says "append five units" but lists six. Six are appended because
  the retained AWS record is a bound support and preflight requires every
  bound source and record to exist in the source plan and registry. Ledger
  records stay +5; source-plan and registry units are +6.
- The primary `source_support` record is the Fowler article; Flyway remains
  an auxiliary tooling record. The dedicated card describes the records as
  applied. The owner page keeps the lane's "proposed" wording as historical
  lane text, matching the B48 integration convention.
- The final lane amendment moves `evidence_scope.status` from `unknown` to
  `source-linked`; the owner hash is `efe87cc5...`, not the earlier
  `54b60760...`.
- The card Sources paragraph was rewritten to cite the applied record ids and
  source ids; the technical-owner link and gloss are unchanged.
- The lane rewrite dropped the page sentence "The protocol owns the
  compatibility window, the reader inventory and the rollback or forward-repair
  decision." Two phase-2 qrels answers cite it. The integration restores the
  sentence verbatim as a forward fix; the owner raw and view hashes above are
  the post-restoration values.

## Validation

- `preflight_sufficient.py --pattern tycho.pattern.expand-and-contract`:
  PASS, 1/1.
- PASS: sources (307), source catalogue, registry, cards, owner units,
  source plan (277 read, 231 records), directory migration (504 documents),
  edition, semantic audit (504 pages), claim references, phase 4 (504 pages),
  delivery evidence, markdown line length (145 exact owner-link exceptions)
  and the boundary check.
- `validate_book_navigation.py` still reports four missing local anchors in
  untouched dark-launching and RBAC/ABAC pages; they are unchanged by this
  integration.
- `validate_sufficient_promotions.py` still fails on the pre-existing B48
  promotion record whose `reviewed_head` is the eight-character `830937d0`;
  that record is outside this change and was not altered.
- Full suite: 688 tests pass (688 OK, 71.1 s), run once on the final tree.
  The exact command and duration are recorded in the commit message.

## Limits

- Partial-bounded coverage only; no Expand-and-Contract promotion or owner
  acceptance.
- No external AI content review was run for this integration; the book/atlas
  review gate remains outstanding.
- The integrator applied the lane's recorded revisions. The Fowler
  representation was re-fetched on 2026-10-31 and its raw HTML digest matched
  `4d958f56...`; PostgreSQL and MySQL digests were not re-fetched.
- The MySQL canonical host returned HTTP 403 to the lane; the Oracle-hosted
  manual copy is the pinned representation.
- No benchmark, production observation, database run or DDL execution is
  claimed.
