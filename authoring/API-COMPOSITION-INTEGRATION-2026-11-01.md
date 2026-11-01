# API Composition lane integration

Status: integrated and self-checked on 2026-11-01. The technical evidence is
4/4 supported, but coverage remains partial-bounded because no promotion record
exists; no promotion, sufficient-coverage claim, independent review or owner
acceptance is claimed.

## Commit chain

- Parent HEAD: `a1902d6447f2ebb5bca39889380791b38192a053` (`a1902d64`).
- Lane commit: `b8620a30`; cherry-pick on this branch: `025972e5`.
- This integration commit applies the shared register, ledger, source plan,
  registry and owner-unit metadata, the dedicated card split, content
  revisions, protected baseline and generated artifacts.

## Card split

- Dedicated page:
  `book/volumes/v11-pattern-atlas/c02-api-communication/api-composition.md`.
- Page identity: `tycho.page.ade9759a19a0402594773756d097c11c`.
- Page raw SHA-256:

      4feacd381be5d7c9ca768b278f9f08cb015103b7b0e2005f6569fd7d7bc2e392

- Page historical-view SHA-256:

      3bf67a6ede0daa883ff61376cc3f83359e4f67d0656906e86c4a2039249b34e9

- Page body SHA-256 (heading plus moved card):

      4ee59d73c9af596d246a11efeb965f3f5151c92bd116a317b3303b4bc537b13d

- README raw SHA-256:

      803624122e0f39680d0ab6cd52abf5a14714822b64991471653ca54b7e7235e2

- README historical-view SHA-256:

      b38cdc05de8dd1f2784a46e7a5e3dc89296ee0d6696df57ae8a80b5b94bda0a8

- Owner page raw SHA-256:

      c65b152cc6fb93934552f0ca595891768b7e2c3adfa9a48f86e6e406d74d220b

- Owner page historical-view SHA-256:

      c4536cfbf436229501f7699003fdbb76f74cc3f6317b3185b8274f1974259496

- The README keeps `### API Composition` at line 194 and links to the dedicated
  card; the card keeps the owner backlink at
  `http-rpc-contracts-and-compatibility.md#api-composition`. The moved card
  body is byte-identical to the lane block apart from the heading level.
- The page is registered as an id, atlas-manifest document, directory record,
  document identity, semantic-audit page and card path.

## Preserved BFF evidence

- BFF section: lines 125-191 plus the separating blank line, 4,962 bytes;
  SHA-256 before and after
  `0b9aeb9f06f54ca9bf269fd01c76f883e7e51cf421d0fb821dbb6815b38bc2e3`.
- BFF card SHA-256: `b9e9710f1ad4d40199de3aa7e4f2235c7a7601db55adfb37009c007185eef0f0`.
- `edition/patterns/sufficient-promotions.v1.json` is unchanged. The BFF
  promotion is not rebound: its `owner_page_sha256` still pins the pre-lane
  owner page, so `validate_pattern_owner_units.py` reports
  `owner-units-promotion-owner-hash` and three owner-unit test results cascade
  from that intentional deferral.

## Applied metadata

- `sources/register.json`: 356 -> 357 records. Added
  `src.microsoft-api-design`; `src.microsoft-cloud-patterns` gains the
  2026-11-01 Gateway Aggregation re-read and hash difference. The catalogue was
  regenerated.
- `edition/patterns/reading-ledger.v1.json`: 352 -> 354 records. Added
  `read.microsoft-gateway-aggregation.2026-11-01` and
  `read.microsoft-api-design.2026-11-01`; the 2026-10-21 Gateway Aggregation
  record remains historical.
- `edition/patterns/source-plan.v1.json`: the API Composition entry takes three
  units. Summary: 388 -> 390 required, 387 -> 389 read, 354 ledger records;
  planned stays 0 and blocked stays 1. The route snapshot is the legacy
  V1-V11 view required by the source-plan validator.
- `edition/patterns/registry.v1.json`: three read source units; the technical
  owner, technical coverage and overall coverage move from partial to
  partial-bounded; decision coverage stays partial-bounded.
- `edition/patterns/owner-units.v1.json`: invariant and failure/recovery are
  supported with the Gateway Aggregation binding; failure/recovery also carries
  an unresponsive-service supporting quote, a partial-or-fail supporting quote
  and a trace-context supporting binding from Microsoft API design. Mechanism
  and alternative stay unchanged. All four technical dimensions are supported,
  but technical coverage remains partial-bounded because the validator derives
  `sufficient` only from a promotion record. Counters: invariant 98 -> 99,
  failure/recovery 96 -> 97, technical partial 49 -> 48 and technical
  partial-bounded 11 -> 12. Decision coverage remains partial-bounded.
- `edition/patterns/card-batches.v1.json`: the entry gains the dedicated
  `card_path` and uses `read.microsoft-gateway-aggregation.2026-11-01`.
- `edition/content-revisions.json`: one issue-540 revision authorizes the
  owner-page and V11/C02 historical-view changes.
- `edition/v12/protected-baseline.json`: refreshed for the two changed book
  pages and the registry, atlas-manifest and re-review-packet hashes. The file
  was already stale at the parent HEAD for the promoted SOA page and for
  `sufficient-promotions.v1.json`; those two entries are refreshed mechanically
  without changing promotion content or rebinding BFF.
- Atlas, coverage and reverse maps, page census, phase 4, semantic audit,
  delivery evidence, route and section indexes, qrels, inventory, candidates
  and re-review packets were refreshed. Counts: 101 atlas documents, 524
  canonical pages, 357 sources and 354 ledger records.

## Coverage state

- Mechanism: supported; invariant: supported; failure/recovery: supported;
  alternative: supported. This is a four-of-four technical binding.
- `technical_coverage` is `partial-bounded`, not `sufficient`, because no
  promotion record exists; `decision_coverage` remains `partial-bounded`.
- Registry technical, decision and overall coverage are `partial-bounded`.
- Freshness format, per-call deadline contract, versioned adapter, trace
  propagation, query-shape limits and transaction boundary remain Tycho
  synthesis.

## Verification

- `python3 scripts/preflight_sufficient.py --pattern
  tycho.pattern.api-composition`: PASS, 1/1 clean.
- PASS: sources (357), catalogue, source plan (390/389/354), registry (390
  units), cards (145), atlas (101 documents), coverage, delivery evidence,
  directory migration (524 documents), book metadata, edition, phase 4 (524
  pages), semantic audit (524 pages) and V12.
- FAIL by design: `validate_pattern_owner_units.py` reports the unrebound BFF
  promotion owner hash. All other owner-unit structure validates.
- `validate_v12.py` passes after the protected-baseline refresh; the parent HEAD
  baseline was already stale for the SOA page and the promotion record.
- PASS: V11 prose line length with 145 exact owner-link exceptions; configured
  lexical boundary checks; `git diff --check`.
- Full suite run once:
  `python3 -m unittest discover -s tests -p 'test_tycho*.py' -v` ran 776 tests
  with seven failures and three errors. Three results are the intentional
  unrebound BFF promotion hash (one owner-unit error and two negative-test
  assertions that the stale hash shadows). Seven results are pre-existing at
  `a1902d64`: two phase-2/phase-3 verbatim quote checks on the cache-aside page,
  two V12 qrels snapshot checks, the AI-review index unindexed error, and two
  promotion-count assertions that still expect 84 promotions after the SOA
  promotion made the count 85. No second full suite was run.

## Deviations from the lane note

- The lane note proposes unit type `best-practice`. The reading-ledger and
  source-plan schemas do not allow it, so both units use `documentation-page`;
  the source register keeps `kind: best-practice`.
- The lane note proposes `technical_coverage: sufficient` after four supported
  dimensions. The owner-unit validator derives `sufficient` only with a
  promotion record, so the honest integration state is `partial-bounded` with
  4/4 supported; no promotion is claimed.
- The lane note's BFF rebind is intentionally not applied, per instruction. The
  BFF section and card remain byte-identical.
- The refresh script writes the full route snapshot into the source plan; the
  source-plan validator requires the legacy V1-V11 snapshot. The integration
  sets the legacy value after refresh and records it here.
- No external AI content review was run for this integration; the book and
  atlas review gate remains outstanding and is not waived.

## Limits

- Partial-bounded coverage only; no promotion, sufficient coverage, owner
  acceptance, CI result or production observation.
- The binding uses one Azure pattern page, one public pattern page and one
  Microsoft API-design page. The Azure page is titled "Gateway Aggregation
  pattern"; it supports per-request timeouts, partial-result-or-failure choices
  and failure visibility, not a freshness protocol or an executed composition.
  Microsoft API design supports versioning and trace context only.
