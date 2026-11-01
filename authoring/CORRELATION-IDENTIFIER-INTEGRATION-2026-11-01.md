# Correlation Identifier integration

Status: integrated and self-checked on 2026-11-01. The V11/C03 Correlation Identifier
card is now a dedicated page; the Azure Service Bus identity evidence remains the lane
binding in the V04 owner section. No promotion, sufficient-coverage claim, independent
review, CI result or owner acceptance is claimed for this change.

## Base, branch and commits

- Base: `fe7fea2f0fa02bb5335a57fd49354a19382cdfc0` (`fe7fea2f`, the lane commit
  "docs(correlation): bind Azure Service Bus identity evidence").
- Branch: `feature/TYCHO-540-correlation-integration`; worktree
  `/tmp/tycho-correlation`.
- Repair commit: `d743ebf6` (authorized metadata-only zero-trust card repair).
- Integration HEAD is the commit that contains this record; run `git rev-parse HEAD`.

## Card split

- Dedicated page:
  `book/volumes/v11-pattern-atlas/c03-messaging-integration/correlation-identifier.md`.
- Page identity: `tycho.page.523433bb7da14cc48558302d7dc322f9`; parent
  `tycho.chapter.a4b31346a691566550633efe0cf2693e`; atlas section
  `correlation-identifier`.
- Page raw SHA-256:

      4a909094f6d15fd2c520a6d03b357f78f4ea1e84f2b850e5567390bf94702a76

- Page historical-view SHA-256:

      785a9c20c1209bc024835fb17eaffb115598e68aa279810ac2ac020e23f0359d

- Page body SHA-256 (heading plus moved card plus added source lines):

      2fb3d5504b043d872ae130207ea5092780b37979f54df7823bda3baa46d0b18d

- README raw SHA-256:

      a5ddd39ae4d40c417cb8cbe0659a01b5469c71a7bdb42322d47efb5d1d4cb46d

- README historical-view SHA-256:

      abff18f5ac04d17ffc1e08e600a70412bbdf7e61a16bdb0a8c617e8c8cbaffe1

- The README keeps `### Correlation Identifier` as the stable anchor (line 219) and
  replaces the 31-line inline card with one link to the dedicated page. The README
  drops from 482 to 452 lines; only `updated_at` changes in its frontmatter.
- The 26-line identity-through-enterprise-source block is byte-identical to the lane
  block (SHA-256
  `6b510942b91208b5d55c93cd9b300956fac21577f061932bb34577813793bd5b`). The whole
  former inline block was
  `6cca515b1d6f258b2d20b25ad0b30c9a72bafcb9bc749109566bd4974bb4183b`.
- The card keeps the owner backlink to `workflow-failure.md#correlation-identifier`
  under `book/volumes/v04-distributed-coordination-and-events/`
  `c06-messaging-families-and-delivery-contracts/`; the owner route list still points
  at the README anchor, and the owner page is not edited by this integration.

### Deviation: added Azure source citation

The dedicated card adds four lines after the Enterprise Integration Patterns source
entry: `src.azure-service-bus` with read record
`read.azure-service-bus-messages.2026-11-01`, naming the CorrelationId context,
MessageId uniqueness and duplicate detection. The lane rewrote the owner section and
bound the Azure source in the owner unit but left the inline decision card on the
2026-10-21 source only; the moved card declares both sources in
`evidence_scope.source_ids`, so the citation is added for consistency. Decision
question, good-fit conditions, contraindications, alternative, failure text, decision
state and related entries are unchanged.

## Preserved Dead Letter Channel evidence

- DLQ section: lines 207-273 of the owner page, 5,114 bytes, SHA-256
  `eb282cefb83a08110f039ac8afb5b551cf1837a3fc34526d464a0dbb1a8fe36f`; identical
  before and after this integration.
- DLQ card `dead-letter-channel.md`:
  `14ee8093145bf7ea1f5deededaeb551068a2db79df388cb9efb5e425011f0d68`, identical.
- The owner page is unchanged by this integration (SHA-256
  `41b81b0da5f69cc3fa7b811a14864bb141473776b43c699b12b915e5ff852d34`), so the lane's
  rewrite is inherited rather than re-authored.
- The DLQ promotion is not rebound. `sufficient-promotions.v1.json` still pins
  `owner_page_sha256` `6c0525ee32f7875d9bb3e350bbbaafe5e2673e4625757616eae21098eac3337b`
  from the 2026-10-30 review, and `validate_pattern_owner_units.py` reports
  `owner-units-promotion-owner-hash: tycho.pattern.dead-letter-channel-dlq` by design
  until the owner rebinds it.

## Azure Service Bus lane evidence (already in the lane)

- `sources/register.json`: `src.azure-service-bus` admitted, documentation page,
  live page read 2026-11-01.
- `edition/patterns/reading-ledger.v1.json`:
  `read.azure-service-bus-messages.2026-11-01` with content SHA-256
  `1eb90aff576f436387bea36245c4111684dd000685ee06b5163e51ca6771cdcc` and section
  `Message properties`.
- `edition/patterns/source-plan.v1.json`: one read unit for the entry.
- `edition/patterns/registry.v1.json`: one read source unit; the registry file itself
  is unchanged by this integration.
- The integration adds one `source_support.auxiliary` entry for
  `src.azure-service-bus` to the correlation owner unit, so preflight sees every
  binding source in the support list.

## Zero-trust metadata-only repair (commit d743ebf6)

Authorized by the delegating owner because the invalid frontmatter blocked
`canonical_scan` and therefore the mandated refresh. No zero-trust content or claim
is changed.

- Zero Trust Architecture
  - old file: `4e3f19c5203bc5ad097681d60f464961114c7ce886f74b1fda5d67cb5bd9a6a3`
  - new file: `e229d4ee2060f1099c1331facb0396e2c75c83bdc247de57645d3f10e88b6b04`
  - body, unchanged:
    `a516c62da251e14b8b860d47bcd5c9f3e25b55f58174a745421c46fc430d5c2f`
- Least Privilege
  - old file: `eab7e8f716954b46ce9c0991381d9d52a20ec05cd297e6877c0d00b42d7178e4`
  - new file: `6d897b106dc5c38f0a08b121396392f5d9fa34c1addcaf5bdbe0bc1460ef7337`
  - body, unchanged:
    `2a242d018b9861640976b9b70202dbf1d8f6eb4b2553b42ac71e5f717332938d`

- The bodies are byte-identical before and after (the body SHA-256 is the same in both
  states). Only `content_review.proof_uri` and the least-privilege
  `content_verified_at` placement change.
- `proof_uri` now points at the saved report at commit `612599a4` under
  `authoring/ai-reviews/2026-11-01-zero-trust-least-privilege-deepseek.md`. The URI is
  wrapped with a YAML escaped line break to keep the 100-character prose limit.
- `sufficient-promotions.v1.json` updates only the two `card_sha256` values. Reviewer,
  report path, report SHA-256, `reviewed_head` and acceptance state are unchanged.
  This is a metadata-only rebind, not a new review or promotion.

## Registrations

- `edition/atlas-manifest.json`: 105 -> 106 documents; the new V11/C03 page carries
  its id, parent, title and hash. README and the two repaired cards also take current
  hashes.
- `edition/directory-migration.json`: `canonical_documents` 528 -> 529; one document
  record (identity, parent, reversible path, baseline SHA-256
  `785a9c20c1209bc024835fb17eaffb115598e68aa279810ac2ac020e23f0359d`) and one
  `added_documents` record for issue 540.
- `sources/document-identities.json`: 559 -> 560 entries; origin commit `fe7fea2f`,
  authored 2026-11-01, migration body SHA-256
  `2fb3d5504b043d872ae130207ea5092780b37979f54df7823bda3baa46d0b18d`.
- `edition/patterns/semantic-audit.v1.json`: 528 -> 529 pages; the page is
  `tier: atlas`, `phase4_disposition: atlas-decision`, disposition `sound`,
  self-checked 2026-11-01. Summary: 529 pages, 106 atlas pages, 0 findings.
- `edition/patterns/card-batches.v1.json`: the correlation entry gains
  `card_path`; the 2026-10-21 ledger record and enterprise source citation stay.
- `edition/patterns/owner-units.v1.json`: Azure auxiliary entry; the stale
  Dead Letter Channel-DLQ coordinate moves 199 -> 207 (the lane lengthened the
  preceding Correlation section) and the stale Least Privilege coordinate moves
  92 -> 97. No unit text, quote, binding or coverage value changes.
- `edition/content-revisions.json`: one issue-540 authorization records the README
  historical-view change (482 -> 452 lines) and the inherited least-privilege
  enrichment baseline.
- `edition/enrichment-manifest.json`: the least-privilege page baseline repairs the
  inherited zero-trust lane drift; no new source inspection is claimed.

## Refresh

- Interpreter: `python3` 3.15.0 (Homebrew, arm64).
- Command: `python3 scripts/refresh_atlas_artifacts.py --authorize ...` with the
  reason "Integrate the Correlation Identifier card split, register the Azure Service
  Bus identity evidence and repair inherited zero-trust card metadata."
- Refreshed: route index, section FTS index, pattern census, coverage, phase 4,
  atlas hashes and registry hash, semantic-audit hashes and summary, delivery
  evidence, corpus and agentic qrels snapshots, inventory, sufficient candidates,
  review reconciliation, re-review scope and packets, content revisions.
- Mechanical schema updates required by the page count: `maxItems` 528 -> 529 in
  `schemas/pattern-semantic-audit.v1.schema.json` and
  `schemas/pattern-phase4.v1.schema.json`; delivery-evidence summary and schema
  `ledger_records` 359 -> 361 and `sources` 348 -> 350.
- Source-plan summary rebinds to the derived values: 399 required units, 398 read,
  0 planned, 1 blocked, 361 ledger records. The refresh writes the full V1-V12 route
  snapshot; the source-plan validator requires the legacy V1-V11 view, so the legacy
  snapshot `1b9b0481f58761b3eb34910a0a01136eaca3db4af98b66307a97d3e3292a7b37` is
  stored instead.
- `edition/v12/protected-baseline.json`: all 467 page hashes and 5 promotion-record
  hashes rebind mechanically. Six of the nine drifts already existed at `fe7fea2f`
  (owner page, least-privilege owner page and cards, promotions and registry from the
  lane and zero-trust work); three are caused by this integration (README, atlas
  manifest, re-review packets). This is a hash refresh, not a V12 review.
- Counts after refresh: 12 volumes, 89 chapters, 529 canonical documents, 106 atlas
  documents, 145 cards, 361 ledger records, 359 sources (350 outside V12), 91
  promotions and 7 owner-accepted entries.

## Verification

- `python3 scripts/preflight_sufficient.py --pattern
  tycho.pattern.correlation-identifier`: PASS, 1/1 clean.
- PASS: atlas (106 documents), cards (145 entries), registry (145/11), semantic audit
  (529 pages), coverage (145/89), phase 4 (529 pages, 538 routes), delivery evidence
  (145/145), directory migration (529 documents), book metadata (560 documents),
  edition inventory, enrichment, V12 structure and hashes, sufficient owner acceptance
  (7), sufficient pilot inputs, lexical boundary checks and V11 line length (145
  exact owner-link exceptions).
- FAIL by design: `validate_pattern_owner_units.py` reports only
  `owner-units-promotion-owner-hash: tycho.pattern.dead-letter-channel-dlq`; the DLQ
  rebind is deferred by instruction.
- FAIL inherited from the zero-trust lane and unchanged at `fe7fea2f`:
  `validate_sources.py` rejects `src.nist-sp-800-207` `reading_status`
  `full-public-document-inspected`; `validate_pattern_sources.py` rejects unit type
  `standard` in the zero-trust source plan (entry 133); `validate_sufficient_promotions.py`
  reports `promotions-head-not-ancestor: tycho.pattern.least-privilege`;
  `validate_corpus_qrels.py` reports a stale qrels snapshot; `validate_book_navigation.py`
  reports the same four pre-existing missing-local-anchor issues as the base (two in
  dark-launching-shadow-traffic, two in rbac-abac). None is caused by this
  integration.
- Not run, per owner instruction: the full unit suite and V12 review. Tests are
  unchanged.

## Limits

- Partial-bounded coverage only; no promotion, sufficient coverage, independent
  review, CI result, production observation or owner acceptance.
- The AI review gate for book and atlas changes is outstanding for this branch. This
  record is self-checked integration evidence, not a review.
- The inherited validators listed above stay red until the owning lanes repair them.

## Deviations

- One four-line Azure source citation is added to the moved card.
- The least-privilege owner-unit coordinate (92 -> 97) is repaired without a separate
  instruction; it is a mechanical coordinate refresh from the zero-trust lane and
  changes no unit text.
- The zero-trust repair commit carries only the two cards and the two promotion
  hashes; the derived artifacts that depend on it land in the integration commit.
- Source-plan legacy route snapshot and schema count caps are restored after the
  refresh, following the house refresh convention.
