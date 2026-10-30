# B42 Causal Ordering split and metadata integration

Status: integrated and self-checked on 2026-10-30. Coverage remains
partial-bounded; no Causal Ordering promotion, owner acceptance or independent
AI review is claimed.

## Commit chain

- Parent: `3cebce623e6efe3a3fd4b166372172d28edf3c1d` (`3cebce62`).
- Fencing promotion protection: `a27e8aec`.
- B42 book-binding cherry-pick: `a744591c`, source `2b728815`.
- This commit: Causal split, metadata integration, counters and tests.

The cherry-pick applied cleanly. `a744591c` contains the B42 note, the V04
Causal Ordering owner edits and the updated inline V11/C08 card.

## Card splits

### Fencing Tokens

- Dedicated page: `book/volumes/v11-pattern-atlas/c08-coordination/fencing-tokens.md`.
- Page SHA-256:
  `39b75daf58966aa8586d6bd76c9a96af3601f209d5391521c1899705d4aaec0a`.
- Card body SHA-256 `536becf7...` equals the old shared-page section body;
  the promotion `card_sha256` is rebound to the new page. The proof is in
  `authoring/B42-FENCING-VERBATIM-MOVE-2026-10-30.md`.
- Owner page hash, review date, reviewed HEAD and report are unchanged.

### Causal Ordering

- Dedicated page:
  `book/volumes/v11-pattern-atlas/c08-coordination/causal-ordering.md`.
- Page SHA-256:
  `13f2ef22943f87fb70de7e8a8cda3be96441d0dacd21ae5b0862129ff4c8adf4`.
- README SHA-256:
  `094c8d382dfaab6412e16ad14efc422cdc5bca85769fef86a75f79eb0e61229a`.
- Owner page SHA-256:
  `75f843ac87cff8250fafcf5851836a839d4042a5d81276895a118fb2745c3b34`.
- The post-cherry-pick README section body and the new page card body are
  byte-identical after one trailing newline: SHA-256
  `72a924d96d2f37e1330f4d210f649da4d602e04c2116c3711498a99d9e91643e`;
  `diff -u` and `git diff -w` exit 0.

## Applied metadata

- `sources/register.json`: 303 -> 304 sources; add
  `src.mattern-vector-time`; mark Lamport, Kafka Introduction and Kafka
  Design as inspected with the 2026-10-30 revisions.
- `edition/patterns/reading-ledger.v1.json`: 203 -> 207 records.
- `edition/patterns/source-plan.v1.json`: 244/243 -> 248/247 required/read;
  blocked stays 1; ledger records 207; registry and route snapshots
  refreshed.
- `edition/patterns/registry.v1.json`: five causal source units; coverage
  stays `partial-bounded`.
- `edition/patterns/owner-units.v1.json`: failure/recovery and alternative
  set to `supported` with primary and supporting bindings; coverage stays
  `partial-bounded`; counters 69 failure/recovery and 74 alternative.
- `edition/patterns/card-batches.v1.json`: Fencing and Causal cards point to
  their dedicated pages.
- `edition/content-revisions.json`: one revision for the README, Causal
  owner page, Causal source block and enrichment baseline.
- `edition/atlas-manifest.json`, `edition/directory-migration.json`,
  `sources/document-identities.json`, `edition/patterns/semantic-audit.v1.json`:
  register both pages and keep the README anchors.
- `sources/CATALOG.md` and the generated atlas artifacts were rebuilt.

## Deviations from the B42 note

- `source_blocks` authorization was required: the B42 owner edit changes the
  Causal source block hash. The B42 note said to leave it empty; the actual
  decomposition validator requires the recorded previous/current pair.
- `enrichment_baselines` authorization was required for the modified owner
  page; the B42 note also said to leave it empty.
- The delivery-evidence schema constants moved to 207 ledger records and 304
  sources, and the delivery summary was rebound to the derived counters.
- The new Causal page uses a 2026-10-30 self-check date so the targeted
  preflight passes; this is an integration self-check, not a new external
  review. The B42 card had kept the historical 2026-10-21 date while moving
  `source_inspection_date` to 2026-10-30, which the preflight rejects.
- The causal review packet now records the changed owner page as
  `page-changed-since-review` and pins the historical
  `reviewed_page_sha256`; the historical verdict is not rewritten.

## Validation

- `preflight_sufficient.py --pattern tycho.pattern.causal-ordering`:
  PASS, 1/1.
- Full suite: 681 tests pass.
- Passing validators include sources, registry, owner units, cards, atlas,
  promotions, decomposition, enrichment, directory migration, book metadata,
  coverage, delivery evidence, phase4, semantic audit, line length, boundary,
  census, edition, source catalogue, sufficient pilot and AI-review index.
- The unrelated pre-existing book-navigation warnings remain outside this
  lane's scope.

## Limits

- Partial-bounded coverage only; no Causal promotion or owner acceptance.
- No external AI content review was run for this integration.
- No benchmark, production observation or runtime experiment is claimed.
- The historical Fencing review is applied only to the unchanged card text,
  not to any new Causal content.
