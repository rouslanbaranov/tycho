# B58 Distributed Tracing lane integration

Status: integrated and self-checked on 2026-10-31. Coverage remains
partial-bounded; no promotion, sufficient coverage, owner acceptance or
independent AI review is claimed.

## Commit chain

- Parent: `69acde64207d12870edb843761dcf2fe929fb6ce` (`69acde64`).
- Lane commit cherry-picked: `24b5f3a5d44996282fd15cca27339f1f7450e68c`
  (`docs(atlas): bind distributed tracing dimensions to public sources`).
- Cherry-pick on this branch: `6ba01cb0` with the same content.
- This integration commit applies the shared metadata, counters, revisions
  and generated artifacts. It does not change the lane's book argument.

The card is already dedicated at
`book/volumes/v11-pattern-atlas/c11-security-operations/distributed-tracing.md`;
the integration does not split or move it, and the C11 chapter landing is
untouched.

## Applied metadata

- `sources/register.json`: 323 -> 324 sources. Added `src.dapper` (Google
  technical report dapper-2010-1). `src.otel` and `src.trace-context` gain the
  2026-10-31 representations, access dates and verification scopes.
  `sources/CATALOG.md` was regenerated from the register.
- `edition/patterns/reading-ledger.v1.json`: 276 -> 281 records. Added
  `read.otel-traces.2026-10-31`,
  `read.otel-context-propagation.2026-10-31`,
  `read.otel-sampling.2026-10-31`,
  `read.w3c-trace-context.2026-10-31` and
  `read.dapper-tracing.2026-10-31`. The retained
  `read.batch6-otel-traces.2026-10-21` is marked `intentionally-unused` and
  added to the plan's foundation records, because the rebinding removes it
  from the plan and card citations.
- `edition/patterns/source-plan.v1.json`: the distributed-tracing entry takes
  R1-R5 in lane order with the exact sections, URLs and record ids. Summary:
  321/320/276 -> 325/324/281 required/read/ledger; planned stays 0 and
  blocked stays 1.
- `edition/patterns/registry.v1.json`: source units 321 -> 325. The entry
  gains five read units; technical owner, technical coverage and overall
  coverage move from partial to partial-bounded; decision stays
  partial-bounded. Notes name the five units.
- `edition/patterns/owner-units.v1.json`: mechanism, invariant,
  failure/recovery and alternative are `supported`, each with one primary
  binding and supporting bindings. The owner line moves 90 -> 101. Primary
  records are `read.otel-traces.2026-10-31`,
  `read.dapper-tracing.2026-10-31` (twice) and
  `read.otel-sampling.2026-10-31`; the other records are auxiliary. Coverage
  stays partial-bounded. Counters: mechanism 123 (unchanged), invariant
  88 -> 89, failure/recovery 83 -> 84, alternative 88 -> 89, technical
  partial-bounded 15 -> 16 and technical partial 59 -> 58. Technical
  sufficient stays 71 and decision partial-bounded stays 74.
- `edition/patterns/card-batches.v1.json`: the entry keeps the dedicated
  `card_path` and cites `read.otel-traces.2026-10-31`.
- `edition/content-revisions.json`: one issue-540 revision authorizes the
  owner-page evidence-scope change and the 2026-10-31 evidence-bound banner
  from the decomposition baseline; a second authorizes the owner-page and
  card historical-view changes. The historical-view hashes are
  `79865da7...` for the owner page and `4f7da1f5...` for the card.
- `edition/patterns/delivery-evidence.v1.json` and its schema constants:
  324 sources, 281 ledger records, 58 technical partial and 16 technical
  partial-bounded. Page, entry, card and sufficient counts stay unchanged.
- Route index, section index, census, coverage/reverse maps, phase 4,
  semantic summary, qrels, inventory, sufficient candidates, re-review
  scope and packets were refreshed. Test guards move to 325 registry units,
  324 read units and 281 ledger records.

## Page hashes

- Owner page raw SHA-256:

      930f9e82b46f3ca3ca792426944e9a2e798fe70f5287d677d6ac70515583862c

- Owner page historical-view SHA-256:

      79865da7d02ff43e049e2d345288c3d4bcd2fbca2984435d0f790fae007a5551

- Card page raw SHA-256:

      e27f7cb50f020ca08eb483150def70eec0d710c862863f30514b7665b0c133a2

- Card page historical-view SHA-256:

      4f7da1f5720e62d068fcdabb13a61628af338532360ba9fe793d6486f443eabe

## Deviations from the lane note

- The lane's proposed owner-unit quotes for invariant, failure/recovery and
  alternative were not verbatim in the edited owner section. The integration
  rebinds those quotes to the actual owner-section sentences:
  "A trace is a sampled, propagated observation, not an authoritative record
  of every business effect.";
  "Instrumentation gaps and sampling loss are normal failure modes."; and
  "Metrics and structured logs are alternatives for different questions."
  The source bindings and supported states are unchanged.
- The owner page `content_review` stays `draft` with null reviewer and date,
  and `source_inspection_date` stays null. The page is a protected
  decomposition source body; the decomposition validator rejects a changed
  review field and a fabricated inspection date for a question page without
  `fresh_source_ids`. The card remains self-checked on 2026-10-31.
- The evidence-scope change and the 2026-10-31 draft banner are authorized
  explicitly in `edition/content-revisions.json` as
  `decomposition_metadata` and `source_blocks` revisions. Document
  identity, path and source history are retained.
- The lane leaves "proposed" labels on the card and owner notes. The
  integration replaces them with the registered state; it does not change
  the argument or add a promotion.

## Validation

- `preflight_sufficient.py --pattern tycho.pattern.distributed-tracing`:
  PASS, 1/1.
- PASS: sources (324), source catalogue, source plan (324 read, 281
  records), registry (325 units), owner units, cards, atlas (87 documents),
  coverage, phase 4 (510 pages), semantic audit (510 pages), delivery
  evidence, edition, directory migration, decomposition, book metadata,
  claim references, metadata schemas, sufficient promotions, owner
  acceptance, AI reviews, sufficient pilot, pattern census and research
  checkpoints.
- PASS: V11 prose line length, 145 exact owner-link exceptions.
- PASS: configured lexical boundary checks; independent-origin review
  remains required.
- PASS: `git diff --check`.
- `book_change.py --plan`: clean, no changed pages, missing revisions or
  stale artifacts.
- Full suite: 688 tests pass (688 OK, 47.710 s), run once on the integrated
  tree.

## Limits

- Partial-bounded coverage only; no Distributed Tracing promotion,
  sufficient coverage or owner acceptance.
- No external AI content review was run for this integration; the book and
  atlas review gate remains outstanding.
- The integrator applied the lane's recorded revisions. No source was
  re-fetched, and no trace, span, sampler, collector, backend or
  distributed experiment was created or run.
- The OTel pages are living documentation, the W3C unit is the dated 2021
  Recommendation and the Dapper PDF is the 2010 technical report. Their
  digests pin the 2026-10-31 representations, not future revisions.
- The missing-span interpretation, metrics/log choice rule, runbook and all
  scenario text remain Tycho guidance, not source claims. The card and
  owner section are self-checked, not independently reviewed.
