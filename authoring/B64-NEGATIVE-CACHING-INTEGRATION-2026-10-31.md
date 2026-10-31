# B64 Negative Caching lane integration

Status: integrated and self-checked on 2026-10-31. Coverage remains
partial-bounded; no promotion, sufficient coverage, owner acceptance or
independent AI review is claimed.

## Commit chain

- Parent: `dce2a6f8ce2c00c655223addd28af5e70a311e96` (`dce2a6f8`).
- Lane commit cherry-picked: `5710451e` ("docs(book): bind negative caching
  invariant, recovery and alternative").
- Cherry-pick on this branch: `1404052e`, same three files.
- This integration commit applies the shared metadata, the dedicated card
  split, counters, revisions and generated artifacts. It does not change the
  lane's book argument.

## Card split

- Dedicated page:
  `book/volumes/v11-pattern-atlas/c05-caching-retrieval/negative-caching.md`.
- Page identity: `tycho.page.b6f0e0ea50474e29901d5b7b7f471bac`.
- Page raw SHA-256:

      e7ae55919443b597df7d0f82357acd8365033a9f41417e6b24aa162ff783ca2f

- Page historical-view SHA-256:

      c4847c93817e8289b096a7f3a33aef69ebe0b58548295461472b05beacf1191c

- Page body SHA-256:

      d834893b7bda2701be3accce23376c6783b13e443eadd09e47518e1ad723110d

- README raw SHA-256:

      65ede6e8ab99cf99525bf1dece018e83ab33bbe2527733228a4d64a9e605acd8

- README historical-view SHA-256:

      da83f2c47abff5aeb1fe4bbe8b5bb88925de34c398ce8099bb7038c39a35df81

- Owner page raw SHA-256:

      0898d4b4483b7d07744833a89c70268d23c4348b453c2fdfd8d1ccb4836797b0

- Owner page historical-view SHA-256:

      2032a3eb76eea434c01eb6ab7ee732c762ed69edc3f37c9e5442611b18cace61

- Owner page body SHA-256:

      cba7a466ec4eb8becef2e23d192672aef1f9cc029ddfe3e20054bb8c18979436

- The card moved from the shared chapter page; the section heading becomes the
  page H1. The README keeps `### Negative Caching` with a link to the dedicated
  card, so the owner backlink at
  `negative-cache.md#4-negative-caching-and-evicted-authorization` resolves
  through the chapter anchor. The chapter page drops the three card-only source
  ids added by the lane; the pre-existing `src.rfc9111-enrichment` and
  `src.google-cdn-negative-caching` remain as chapter history.
- The page is registered as an id, atlas manifest document, directory record,
  document identity and card path.

## Applied metadata

- `sources/register.json`: 337 -> 339 sources. Added
  `src.owasp-authorization-decisions` and `src.cloudflare-cache-status`;
  `src.rfc9111-enrichment` and `src.cloudfront` gain the 2026-10-31 revision
  and verification-scope notes; the source catalogue was regenerated.
- `edition/patterns/reading-ledger.v1.json`: 307 -> 311 records. Added
  `read.rfc9111-negative-caching.2026-10-31`,
  `read.cloudfront-status-codes.2026-10-31`,
  `read.owasp-authorization-decisions.2026-10-31` and
  `read.cloudflare-cache-status.2026-10-31`. The retained
  `read.batch3-google-negative.2026-10-21` stays the per-status TTL example.
- `edition/patterns/source-plan.v1.json`: the entry takes five units.
  Summary: 351 required, 350 read, 311 ledger records; planned stays 0 and
  blocked stays 1.
- `edition/patterns/registry.v1.json`: five read source units; technical
  owner, atlas owner and technical/decision/overall coverage move to
  partial-bounded, with confidence high.
- `edition/patterns/owner-units.v1.json`: mechanism, invariant,
  failure/recovery and alternative are `supported`, each with one primary
  binding and supporting bindings. The owner line moves 49 -> 58. Technical
  and decision coverage stay partial-bounded. Counters: mechanism 123
  (unchanged), invariant 94 -> 95, failure/recovery 89 -> 90, alternative
  94 -> 95, technical partial-bounded 15 -> 16, technical partial 53 -> 52,
  decision counters unchanged.
- `edition/patterns/card-batches.v1.json`: the entry gains the dedicated
  `card_path` and cites `read.owasp-authorization-decisions.2026-10-31`.
- `edition/content-revisions.json`: one issue-540 revision authorizes the
  owner-page and chapter historical-view changes and the changed section-4
  source block. The new page baseline is its historical-view hash, so it needs
  no separate authorization.
- `edition/atlas-manifest.json`, `edition/directory-migration.json`,
  `sources/document-identities.json` and
  `edition/patterns/semantic-audit.v1.json`: register the page, identity,
  baseline and atlas review entry. Atlas documents move 92 -> 93; directory
  documents move 515 -> 516; semantic-audit pages move 515 -> 516.
- Route index, section index, census, coverage and reverse maps, phase 4,
  delivery evidence, qrels, inventory, sufficient candidates, review
  reconciliation and re-review packets were refreshed. Test guards move to 93
  atlas documents, 516 pages, 351 registry units, 350 read units and 311 ledger
  records. Delivery counters move to 52 technical partial and 16 technical
  partial-bounded at 516 pages and 339 sources.
- Schema page caps move to 516 for phase 4 and the semantic audit; delivery
  evidence pins 311 ledger records and 339 sources. These are counter bumps,
  not evidence relaxation.

## Deviations from the lane note

- The lane leaves the card inline at V11/C05 and proposes sufficient coverage.
  The task and the card granularity policy require a dedicated page and keep
  partial-bounded coverage. The four dimensions are supported; no promotion is
  recorded.
- The lane sets the owner page `source_inspection_date` to 2026-10-31. The
  page is a decomposition question page, and `validate_decomposition.py`
  requires a null inspection date for pages without `fresh_source_ids`. The
  integration restores it; the binding remains in the shared ledger, owner
  units and dedicated card.
- The lane's proposed notes and section lists are expanded where the ledger
  records the sections actually read, because the source-plan and ledger
  schemas require identical section lists.

## Validation

- `python3 scripts/preflight_sufficient.py --pattern
  tycho.pattern.negative-caching`: PASS, 1/1 clean.
- `python3 scripts/premerge_check.py --branch
  feature/TYCHO-540-b9-coverage-growth --issue-title '[E17-89] B9 coverage
  growth'`: PASS. Full suite: 688 tests OK (47.5 s).
- PASS: sources (339), source catalogue, source plan (351 required, 350 read,
  311 records), registry (351 units), owner units, cards, atlas (93 documents),
  coverage, phase 4 (516 pages), semantic audit (516 pages), delivery evidence,
  edition, directory migration (516 documents), decomposition, book metadata
  and page census.
- PASS: V11 prose line length, 145 exact owner-link exceptions.
- PASS: configured lexical boundary checks; independent-origin review remains
  required.
- PASS: `git diff --check`.

## Limits

- Partial-bounded coverage only; no Negative Caching promotion, sufficient
  coverage or owner acceptance.
- No external AI content review was run for this integration; the book and
  atlas review gate remains outstanding and is not waived.
- The integrator applied the lane's recorded revisions. No source was
  re-fetched, and no cache, CDN or revocation exercise was run.
- The RFC, CloudFront, OWASP and Cloudflare pages are living documents; the
  digests pin the 2026-10-31 representations, not future revisions.
- The per-principal key, revocation deadline and fail-open/closed guidance is
  Tycho synthesis, not a claim that any selected unit tested this page's design.
