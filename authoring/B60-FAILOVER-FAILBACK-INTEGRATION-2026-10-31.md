# B60 Failover/Failback lane integration

Status: integrated and self-checked on 2026-10-31. Coverage remains
partial-bounded; no promotion, sufficient coverage, owner acceptance or
independent AI review is claimed.

## Commit chain

- Parent: `f99e21e78d6239d3573f846cc1ca4e627a3e69f9` (`f99e21e7`).
- Lane commit cherry-picked: `b0edf9648b95c1d7b03f4ad533a94ce7e6922045`
  (`docs(book): bind failover/failback dimensions`).
- Cherry-pick on this branch: `020e9ff8` with the same content.
- This integration commit applies the shared metadata, dedicated card split,
  counters, revisions and generated artifacts. It does not change the lane's
  book argument.

The lane edited the V08/C07 owner section and an inline card in the V11/C07
chapter landing. The task requires a dedicated page, so the card moves and the
chapter keeps its stable anchor and a link to the page.

## Card split

- Dedicated page:
  `book/volumes/v11-pattern-atlas/c07-resilience/failover-failback.md`.
- Page identity: `tycho.page.36bfc8635514db33025afd706a6b4c85`.
- Page raw SHA-256:

      2fc3ad31c830f08d5211040410367b10515b4037da6b5c24acdb819fb3ebb83a

- Page historical-view SHA-256:

      afb62a56f0fac62973f3344d2551569c551ef1b76d037749d696a06a3df1fe15

- Page body SHA-256:

      e63bcc876bb60592801cfe379fbf921d20c2abc00a4174210f1504123990dfa0

- README raw SHA-256:

      ae058acde4a072e2df94841acba6f8d6238b3b1178820aa6f68400d62600cf5a

- README historical-view SHA-256:

      803c512eca400151529ce81c4244d21da8c08cbe382e6b9008dc3c5648b24388

- Owner page raw SHA-256:

      5ff92e9bb78e932f4d44fea4ca5f0b40dde6375e51e511e1f95a8987391b9554

- Owner page historical-view SHA-256:

      545fd1388657446a13bfde22a20015f3cb26a27fddce96ec66f489c7adb398fd

- The card moved from the shared chapter page; the section heading becomes the
  page H1. The README keeps `### Failover / Failback` and points to the
  dedicated card, so the owner backlink
  (`README.md#failover--failback`) and the card owner link both resolve. The
  chapter page drops the three card-only source ids; they now belong to the
  dedicated page.
- The card section is 56 body lines and 464 words; the page is 114 lines with
  frontmatter and 468 body words. The owner page is 231 lines and 1,835 body
  words; the owner heading is line 166.

## Applied metadata

- `sources/register.json`: 326 -> 328 sources. Added `src.aws-route53` and
  `src.azure-site-recovery`; `src.postgresql` gains the PostgreSQL 17 26.3
  Failover representation and verification scope, and `src.sre` gains the
  Testing for Reliability / Testing Disaster representation. The source
  catalogue was regenerated.
- `edition/patterns/reading-ledger.v1.json`: 286 -> 291 records. The five new
  records are `read.aws-route53-failover.2026-10-31`,
  `read.azure-asr-failover.2026-10-31`, `read.azure-asr-failback.2026-10-31`,
  `read.pg-failover.2026-10-31` and `read.sre-testing-disaster.2026-10-31`.
  The retained `read.batch3-pg-warm.2026-10-21` stays historical evidence.
- `edition/patterns/source-plan.v1.json`: the failover entry takes R4, R1,
  R2, R3 and R5 with their exact sections, URLs and record ids, plus the
  retained PostgreSQL log-shipping unit. Summary: 329/328/286 ->
  334/333/291 required/read/ledger; planned stays 0 and blocked stays 1.
- `edition/patterns/registry.v1.json`: six read source units for the entry;
  technical owner, technical coverage and overall coverage move from partial
  to partial-bounded; decision stays partial-bounded.
- `edition/patterns/owner-units.v1.json`: mechanism, invariant,
  failure/recovery and alternative are `supported`, each with one primary
  binding and supporting bindings. The owner line moves 157 -> 166. Primary
  records are `read.pg-failover.2026-10-31` and
  `read.aws-route53-failover.2026-10-31`. Coverage stays partial-bounded.
  Counters: mechanism 123 (unchanged), invariant 90 -> 91, failure/recovery
  85 -> 86, alternative 90 -> 91, technical partial-bounded 15 -> 16,
  technical partial 57 -> 56, sufficient 73 (unchanged).
- `edition/patterns/card-batches.v1.json`: the entry gains the dedicated
  `card_path` and cites `read.pg-failover.2026-10-31`.
- `edition/content-revisions.json`: one issue-540 revision authorizes the
  owner-page and chapter historical-view changes. The new page baseline is its
  historical-view hash, so it needs no separate authorization.
- `edition/atlas-manifest.json`, `edition/directory-migration.json`,
  `sources/document-identities.json` and
  `edition/patterns/semantic-audit.v1.json`: register the page, identity,
  baseline and atlas review entry. Atlas documents move 88 -> 89; directory
  documents move 511 -> 512; semantic-audit pages move 511 -> 512.
- Route index, section index, census, coverage/reverse maps, phase 4,
  semantic summary, qrels, inventory, sufficient candidates, review
  reconciliation and re-review packets were refreshed. Test guards move to
  512 pages, 89 V11 documents, 334 registry units, 333 read units and 291
  ledger records. Delivery counters move to 56 technical partial and 16
  technical partial-bounded; decision partial-bounded stays 72.

## Deviations from the lane note

- The lane leaves the card inline at V11/C07. The task and the card
  granularity policy require a dedicated page, so the card moves and the
  chapter keeps a stub link at the stable anchor.
- The lane sets the owner page `source_inspection_date` to 2026-10-31.
  The page is a decomposition question page, and `validate_decomposition.py`
  requires a null inspection date for pages without `fresh_source_ids`. The
  integration restores it; the binding remains in the shared ledger, owner
  units and dedicated card, and the evidence-scope notes state that it is
  self-checked. `content_review` stays self-checked as the lane sets it.
- The lane marks the new source ids as proposed pending registration. The
  integration registers them and removes the "proposed" wording from the owner
  page and card.
- The lane's counter target (334/333) and its `source_support` clause
  (auxiliary R1, R2, R3, R5 and the retained old record) require the retained
  PostgreSQL log-shipping unit to remain in the plan alongside the five new
  units. The old read record stays historical evidence and is not the current
  primary binding.
- The decision-evidence fields are rebased to the moved card's question and
  competing alternative.

## Validation

- `python3 scripts/preflight_sufficient.py --pattern
  tycho.pattern.failover-failback`: PASS, 1/1.
- PASS: sources (328), source catalogue, source plan (333 read, 291 records),
  registry (334 units), owner units, cards, atlas (89 documents), coverage,
  phase 4 (512 pages), semantic audit (512 pages), delivery evidence, edition,
  directory migration (512 documents), decomposition, book metadata, claim
  references and page census.
- PASS: V11 prose line length, 145 exact owner-link exceptions.
- PASS: configured lexical boundary checks; independent-origin review
  remains required.
- PASS: `git diff --check`.
- `book_change.py --plan`: clean, no changed pages, missing revisions or
  stale artifacts.
- Full suite: 688 tests OK (75.599 s), run once on the integrated tree.
- `validate_book_navigation.py` still reports four missing local anchors in
  untouched dark-launching and RBAC/ABAC pages, as recorded in earlier notes.

## Limits

- Partial-bounded coverage only; no Failover/Failback promotion, sufficient
  coverage or owner acceptance.
- No external AI content review was run for this integration; the book and
  atlas review gate remains outstanding and is not waived.
- The integrator applied the lane's recorded revisions. No source was
  re-fetched, and no database, DNS record, failover, failback, reprotect or
  disaster exercise was run.
- The AWS, Azure and PostgreSQL pages are living documentation; the SRE
  chapter is a 2017 book chapter. Their digests pin the 2026-10-31
  representations, not future revisions.
- The authority-epoch rule, reconciliation order, user-journey gate and choice
  rule remain Tycho guidance, not source claims.
