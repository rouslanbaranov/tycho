# B59 Backup, PITR and Restore lane integration

Status: integrated and self-checked on 2026-10-31. Coverage remains
partial-bounded; no promotion, sufficient coverage, owner acceptance or
independent AI review is claimed.

## Commit chain

- Parent: `b4b66090994486785f6033f34b899aeb1c7148fd` (`b4b66090`).
- Lane commit cherry-picked: `bef8ca5cfaf31736f234bb641ff2d5178402da77`
  (`docs(book): bind backup PITR and restore dimensions`).
- Cherry-pick on this branch: `7f8877e9` with the same content.
- This integration commit applies the shared metadata, dedicated card split,
  counters, revisions and generated artifacts. It does not change the lane's
  book argument.

The lane edited the V05/C07 owner section and an inline card in the V11/C06
chapter landing. The task requires a dedicated page, so the card moves
verbatim and the chapter keeps its stable anchor and a link to the page.

## Card split

- Dedicated page:
  `book/volumes/v11-pattern-atlas/c06-database-storage/backup-pitr-and-restore.md`.
- Page identity: `tycho.page.1daaed0aff5964fb0e79ca3397b8e5b8`.
- Page raw SHA-256:

      c12c94d6b453f44d3fcb32ac433c579227dfb2746deb0ae214a1f535fb8926ea4

- Page historical-view SHA-256:

      954c4895c4cc44113548f1e6eae23bd0b6c693f5e900ed8b58e8bf8bd9bdbeb6

- Page body SHA-256:

      c6bf5bb29c95f4190704eef8d65d8f04a49b7279e1cc90aba038291b87b19e34

- README raw SHA-256:

      962ea787e3b8726f19719d45153397a42bf6ef9868809afed8a6b2388a0339d0

- README historical-view SHA-256:

      8d34adfebaabe1f425b40b1b0ce4c2736bc04c890915e6849f65d6ca0663f297

- Owner page raw SHA-256:

      c369ef443787d1fbd02abfe3eb19dbd7fe1d41c0563e92522a233d93e9a10466

- Owner page historical-view SHA-256:

      960fdbae205c9af22d557829430ea41d1a874f8deb1a3bd33bee4a6c78f33d9d

- The card moved verbatim from the shared chapter page; the section heading
  becomes the page H1. The README keeps `### Backup, PITR and Restore` and
  points to the dedicated card, so the owner backlink
  (`README.md#backup-pitr-and-restore`) and the card owner link both resolve.
  The chapter page drops the three card-only source ids, which now belong to
  the dedicated page; `src.postgresql` remains because other C06 cards cite
  it.
- The card section is 51 body lines and 428 words; the page is 107 lines with
  frontmatter and 572 words. The owner page is 163 lines and 1,141 words; the
  owner heading is line 104.

## Applied metadata

- `sources/register.json`: 324 -> 326 sources. Added `src.aws-backup` and
  `src.azure-backup`; `src.postgresql` gains the PostgreSQL 17
  continuous-archiving representation and verification scope, and `src.sre`
  gains the Data Integrity chapter representation. The source catalogue was
  regenerated.
- `edition/patterns/reading-ledger.v1.json`: 281 -> 286 records. The five new
  records are `read.pg-pitr.2026-10-31`, `read.aws-backup.2026-10-31`,
  `read.aws-backup-restore-testing.2026-10-31`,
  `read.azure-backup.2026-10-31` and
  `read.sre-data-integrity.2026-10-31`. The retained
  `read.batch3-pg-archiving.2026-10-21` is marked
  `intentionally-unused` and added to the plan's foundation records, because
  the rebinding removes it from the plan and card citations.
- `edition/patterns/source-plan.v1.json`: the backup/PITR entry takes R1-R5
  in lane order with the exact sections, URLs and record ids; the PostgreSQL
  unit is rebound to the PostgreSQL 17 page. Summary: 325/324/281 ->
  329/328/286 required/read/ledger; planned stays 0 and blocked stays 1.
- `edition/patterns/registry.v1.json`: source units 325 -> 329. The entry
  gains five read units; technical owner, technical coverage and overall
  coverage move from partial to partial-bounded; decision stays
  partial-bounded. Notes name the five units.
- `edition/patterns/owner-units.v1.json`: mechanism, invariant,
  failure/recovery and alternative are `supported`, each with one primary
  binding and supporting bindings. The owner line moves 91 -> 104. Primary
  records are `read.pg-pitr.2026-10-31` (three times) and
  `read.sre-data-integrity.2026-10-31`. Coverage stays partial-bounded.
  Counters: mechanism 123 (unchanged), invariant 89 -> 90, failure/recovery
  84 -> 85, alternative 89 -> 90, technical partial-bounded 15 -> 16 and
  technical partial 58 -> 57. Technical sufficient stays 72 and decision
  partial-bounded stays 73.
- `edition/patterns/card-batches.v1.json`: the entry gains the dedicated
  `card_path` and cites `read.pg-pitr.2026-10-31`.
- `edition/content-revisions.json`: one issue-540 revision authorizes the
  owner-page evidence-scope binding and the corrected 2026-10-31
  evidence-bound banner from the decomposition baseline; a second authorizes
  the owner-page and chapter historical-view changes. The historical-view
  hashes are `960fdbae...` for the owner page and `8d34adfe...` for the
  chapter. The new page baseline is its historical-view hash, so it needs no
  separate authorization.
- `edition/atlas-manifest.json`, `edition/directory-migration.json`,
  `sources/document-identities.json` and
  `edition/patterns/semantic-audit.v1.json`: register the page, identity,
  baseline and atlas review entry. Atlas documents move 87 -> 88; directory
  documents move 510 -> 511.
- Route index, section index, census, coverage/reverse maps, phase 4,
  semantic summary, qrels, inventory, sufficient candidates, review
  reconciliation and re-review packets were refreshed. Test guards move to
  511 pages, 88 V11 documents, 329 registry units, 328 read units and 286
  ledger records. Delivery counters move to 57 technical partial and 16
  technical partial-bounded; decision partial-bounded stays 73.

## Deviations from the lane note

- The lane leaves the card inline at V11/C06. The task and the card
  granularity policy require a dedicated page, so the card moves verbatim
  and the chapter keeps a stub link at the stable anchor.
- The lane advances the owner `content_review` to `self-checked` and
  `source_inspection_date` to 2026-10-31. The page is a decomposition
  question page, and `validate_decomposition.py` requires the original
  draft review fields and a null inspection date for pages without
  `fresh_source_ids`. The integration restores them; the 2026-10-31 binding
  remains in the shared ledger, the owner units and the dedicated card, and
  the banner states that the binding is self-checked, not independently
  reviewed.
- The lane proposes registering the card with no `card_path` because it
  remained inline. The integration adds the path, as the task requires.
- The lane marks the new source ids as proposed pending registration. The
  integration registers them and removes the "proposed" wording from the
  owner and card metadata and prose.
- The note's owner-unit quotes for invariant, failure/recovery and
  alternative are already verbatim in the edited owner section and are kept.
  The decision-evidence fields are rebased to the edited card's question and
  competing alternative; the old values no longer match the card.
- The retained PostgreSQL record is not reused as the current plan unit.
  It stays historical evidence and is marked intentionally unused rather
  than silently dropped.

## Validation

- `python3 scripts/preflight_sufficient.py --pattern
  tycho.pattern.backup-pitr-and-restore`: PASS, 1/1.
- PASS: sources (326), source catalogue, source plan (328 read, 286
  records), registry (329 units), owner units, cards, atlas (88 documents),
  coverage, phase 4 (511 pages), semantic audit (511 pages), delivery
  evidence, edition, directory migration (511 documents), decomposition,
  book metadata, claim references, metadata schemas and page census.
- PASS: V11 prose line length, 145 exact owner-link exceptions.
- PASS: configured lexical boundary checks; independent-origin review
  remains required.
- PASS: `git diff --check`.
- `book_change.py --plan`: clean, no changed pages, missing revisions or
  stale artifacts.
- Full suite: 688 tests pass (688 OK, 45.438 s), run once on the integrated
  tree.
- `validate_book_navigation.py` still reports the four missing local anchors
  in untouched dark-launching and RBAC/ABAC pages, as recorded in the B50,
  B51, B53 and B58 notes.

## Limits

- Partial-bounded coverage only; no Backup/PITR promotion, sufficient
  coverage or owner acceptance.
- No external AI content review was run for this integration; the book and
  atlas review gate remains outstanding.
- The integrator applied the lane's recorded revisions. No source was
  re-fetched, and no database, backup set, archive, restore, failover or
  disaster-recovery exercise was created or run.
- The PostgreSQL, AWS and Azure pages are living documentation; the SRE
  chapter is a book chapter. Their digests pin the 2026-10-31
  representations, not future revisions.
- The chain-completeness check, application-validation rule, runbook order
  and choice rule remain Tycho guidance, not source claims. The owner
  section and card are self-checked, not independently reviewed.
