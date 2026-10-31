# B57 Synthetic Monitoring lane integration

Status: integrated and self-checked on 2026-10-31. Coverage remains
partial-bounded; no promotion, sufficient coverage, owner acceptance or
independent AI review is claimed.

## Commit chain

- Parent: `2a34ec15075331eedcecf3d716edd6e319285234` (`2a34ec15`).
- B57 book-binding cherry-pick: `86ec4203bf8e4416eacf4497e8dc01e4f2a83db7`
  (`docs(atlas): bind synthetic monitoring dimensions to public sources`).
- This integration commit applies the shared metadata, counters, revisions
  and generated artifacts; it does not edit the lane's book argument.

The cherry-pick applied cleanly. It contains the B57 lane note, the V09/C01
owner-page edits and the registered V11/C11 card edits. The card is already
dedicated at
`book/volumes/v11-pattern-atlas/c11-security-operations/synthetic-monitoring.md`;
the integration does not split or move it, and the C11 chapter landing is
untouched.

## Applied metadata

- `sources/register.json`: 322 -> 323 sources. Added
  `src.azure-app-insights-availability`; `src.sre`, `src.prometheus` and
  `src.aws-cloudwatch-synthetics` gain the 2026-10-31 representations,
  access dates and verification scopes. `sources/CATALOG.md` was
  regenerated from the register.
- `edition/patterns/reading-ledger.v1.json`: 273 -> 276 records. Added
  `read.sre-book-blackbox-monitoring.2026-10-31`,
  `read.prometheus-blackbox-exporter.2026-10-31` and
  `read.azure-app-insights-availability.2026-10-31`. The AWS record
  `read.aws-synthetics-canaries.2026-10-30` is retained unchanged because
  the 2026-10-31 re-fetch was byte-identical. The retired
  `read.batch6-sre-workbook-monitoring.2026-10-21` is marked
  `intentionally-unused` and added to the plan's foundation records.
- `edition/patterns/source-plan.v1.json`: the synthetic entry takes R1-R4
  in lane order with the exact sections, URLs and record ids. Summary:
  318/317/273 -> 321/320/276 required/read/ledger; blocked stays 1.
- `edition/patterns/registry.v1.json`: source units 318 -> 321. The
  synthetic entry gains four read units; technical owner, atlas owner,
  technical coverage, decision coverage and overall coverage move from
  partial/partial-bounded to partial-bounded. Notes name the four units.
- `edition/patterns/owner-units.v1.json`: all four dimensions are
  `supported`, each with one primary binding and supporting bindings. The
  owner line moves 124 -> 134; `source_support.ledger_record` is
  `read.sre-book-blackbox-monitoring.2026-10-31`, the other three records
  are auxiliary, and the competing alternative is rebased to the edited card
  text. Coverage stays partial-bounded. Counters: mechanism 122 -> 123,
  invariant 87 -> 88, failure/recovery 82 -> 83, alternative 87 -> 88,
  technical partial-bounded 15 -> 16 and technical partial 60 -> 59.
  Decision partial-bounded stays 75 and sufficient stays 70.
- `edition/patterns/card-batches.v1.json`: the entry keeps the dedicated
  `card_path` and cites the new Google SRE primary record.
- `edition/content-revisions.json`: one issue-540 revision authorizes the
  owner page and card historical-view changes. It stores
  `4715ba64...` for the owner page and `74afe624...` for the card.
- `edition/patterns/delivery-evidence.v1.json` and its schema constants:
  323 sources, 276 ledger records, 59 technical partial and 16 technical
  partial-bounded. The phase4, semantic-audit and page counts stay 510
  pages, 87 V11 documents and 145 entries.
- Route index, section index, census, coverage/reverse maps, phase 4,
  semantic summary, qrels, inventory, sufficient candidates, re-review
  scope and packets were refreshed. Guards move to 321 registry units,
  320 read units and 276 ledger records. Packet counts move to 47 reviewed,
  88 page-changed and 10 awaiting.

## Page hashes

- Owner page raw SHA-256:

      c2471af256f738c1bfbfd307e1dea995d90ebc61f891510e25fe6bc6b6f8e0dd

- Owner page historical-view SHA-256:

      4715ba648fd18f4960ead55abc2fc207704d53fee96ca36ce72db5ccc5e5a7b2

- Card page raw SHA-256:

      5305b92339a62260f9bf11c31f4ad3312464f1f6d6002d33d8a9c8421849f4e9

- Card page historical-view SHA-256:

      74afe624315525a022e5b3270615a551b575cbfb854413475d22a455c6ad8afa

The owner heading remains `### Synthetic Monitoring` at line 134. The card
remains the dedicated V11/C11 page registered by
`tycho.pattern.synthetic-monitoring`.

## Deviations from the lane note

- The lane proposes unit type `implementation-repository` for the
  Prometheus README. The plan and ledger schemas do not allow that value, so
  the unit is recorded as `documentation-page`, consistent with the other
  Prometheus records. The URL, digest and sections are unchanged.
- The lane sets the owner page `source_inspection_date` to 2026-10-31.
  The page is a decomposition question page without `fresh_source_ids`;
  `validate_decomposition.py` requires that field to stay null to preserve
  decomposition provenance. The integration keeps it null; the owner section,
  card and ledger carry the 2026-10-31 binding. `content_verified_at` stays
  null.
- The lane leaves "proposed" labels on the card and owner notes. The
  integration replaces them with the registered state; it does not change
  the argument or add a promotion.
- The lane's owner hash `a4a30410...` and card hash `30d6fd9c...` are its
  local base/result pair. The repository authorizes historical-view hashes,
  which are recorded above and in `content-revisions.json`.

## Validation

- `preflight_sufficient.py --pattern tycho.pattern.synthetic-monitoring`:
  PASS, 1/1.
- PASS: sources (323), source catalogue, source plan (320 read, 276
  records), registry (321 units), owner units, cards, atlas (87 documents),
  coverage, phase 4 (510 pages), semantic audit (510 pages), delivery
  evidence, edition, directory migration (510 documents), enrichment,
  decomposition, book metadata, claim references, corpus qrels, sufficient
  promotions, owner acceptance, AI reviews and sufficient pilot.
- PASS: V11 prose line length, 145 exact owner-link exceptions.
- PASS: configured lexical boundary checks; independent-origin review
  remains required.
- PASS: `git diff --check`.
- `book_change.py --plan`: clean, no changed pages, missing revisions or
  stale artifacts.
- Full suite: 688 tests pass (688 OK, 49.638 s).
- `preflight_sufficient.py --all-supported` also reports a pre-existing,
  unrelated `tycho.pattern.branch-by-abstraction` failure; the synthetic
  entry itself passes.

## Limits

- Partial-bounded coverage only; no Synthetic Monitoring promotion,
  sufficient coverage or owner acceptance.
- No external AI content review was run for this integration; the book and
  atlas review gate remains outstanding.
- The integrator applied the lane's recorded revisions. No source was
  re-fetched, and no probe, canary, availability test, exporter or monitoring
  deployment was created or run.
- All four units are living public book, repository and documentation pages,
  not benchmarks, standards or production observations. Their digests pin
  the 2026-10-31 representations, not future revisions.
- The real-user comparison, choice rule, runbook and all scenario text
  remain Tycho guidance, not source claims. The card and owner section are
  self-checked, not independently reviewed.
