# B8 — five messaging owner splits, 2026-10-29

Status: split complete and review-ready. No external review, promotion or owner
acceptance was performed in this batch.

## Parent and scope

- Batch base HEAD: `fbe9b7899f6b6aab50959c374851003457f0b2d0`.
- Direct commit parent: `33dc0be964623515c00ae06050dc8b88d907a3df` (a
  governance-only AGENTS change that landed during the batch; no book or edition
  artifact changed).
- One accelerated batch covering five owner sections on three V04/C06 pages.
- Five dedicated owner pages were added; the five atlas cards were already
  dedicated and only their technical-owner links changed.
- Five promotions and the one affected owner acceptance are suspended. All four
  technical dimensions remain supported and coverage is `partial-bounded`.
- Paths below use the readable chapter directory
  `book/volumes/v04-distributed-coordination-and-events/`
  `c06-messaging-families-and-delivery-contracts/`.

## Moves

| Entry | Originating page | New owner page |
|---|---|---|
| Resequencer | `message-selection.md#resequencer` | `resequencer.md` |
| Pipes and Filters | `message-selection.md#pipes-and-filters` | `pipes-and-filters.md` |
| Claim Check | `workflow-failure.md#claim-check` | `claim-check.md` |
| Request-Reply | `workflow-failure.md#request-reply-messaging` | `request-reply-messaging.md` |
| Splitter | `messaging-families-and-durable-workflows.md#splitter` | `splitter.md` |

Each originating heading remains as a stable page anchor and is followed by one
index link to the dedicated owner page. All other sections and anchors on the
three pages are intact; only their line coordinates changed. The two preambles
that described the moved notes as source-bound exceptions were corrected so the
remaining notes keep their synthetic-guidance status.

## Reciprocal links

- Each new owner page opens with a pattern-atlas link to its dedicated card.
- Each dedicated card's `**Technical owner.**` link now resolves to the new owner
  page and its existing anchor.
- Each originating page links to its dedicated owner page.
- The V04/C06 chapter landing lists the five new owner notes.

## Verbatim check

Every moved body is a byte-for-byte substring of its new owner page and is absent
from the originating page. SHA-256 values below cover the moved body only.

- Resequencer: `6de14005d1777baa4a2e3df2a9e73fcd8a2229833212278c0211deb7a6b9ff58`
- Pipes and Filters: `41c282bba3cc46b849682a8c2d5b5054e65b8b7012a4a3f946bb797db532ed95`
- Claim Check: `70e0134dc7280ff343cb4f3e57605c68d3e5f8c0755b78907c71555c42cab9b9`
- Request-Reply Messaging: `28aca80af7d42869ab90862b7f26bd8e0837fa761ccfab5ad9a61fc0e369f6bd`
- Splitter: `276c1d83db1db4d43ad18453a287ad1dffc4aa384d7e152fcf2ae5ac70fdca38`

## Registration

- Atlas manifest: unchanged at 43 V11 documents; registry unchanged at 145
  patterns.
- Directory migration, document identities and semantic audit: five new pages;
  466 canonical documents and 466 semantic pages.
- Enrichment manifest: five split owner pages registered with `origin_page` and
  `origin_heading`; no new source inspection is claimed.
- Card batches, owner units and registry: owner paths, document IDs and anchors
  rebound to the dedicated pages; shared-page inventories now record nine
  message-selection units, two workflow-failure units and two messaging-family
  units.
- Owner units: 81 owner pages and 30 shared pages; 145 entries remain.
- Registry, owner-unit and delivery-evidence coverage is `partial-bounded` for
  the five entries; sufficient counts fall from 21 to 16.
- Promotions: 16 remain; Resequencer, Pipes and Filters, Claim Check, Request-Reply
  Messaging and Splitter are removed from the promotion list.
- Owner acceptance: 7 entries remain; Request-Reply Messaging is removed from the
  accepted entries and the shared Claim Check/Request-Reply report is no longer
  listed as an acceptance report.
- Review records for the five entries now carry
  `awaiting-current-external-review` with pinned historical passes; reconciliation
  reports 10 awaiting and 135 historical promoted labels, not current promotions.
- Qrels Q115 is retargeted to the Splitter owner page with section `splitter`.

## Post-split hashes

- Resequencer owner: `a686c031a1a889e397356f9cce9d9854e1c764cb04b68e232c989fc372dbd3c3`
- Resequencer card: `e23a4c9403153c7a44e64271a11289a6a487a583bcebfc62c8ff272fb72547f6`
- Pipes and Filters owner: `5626343a2414b52d7c59c5aa5f5d59a27c6f2734fce965698bec87abc0b34e32`
- Pipes and Filters card: `e77be08363654b7dac5afddab3663223790fa1d277b7348a54c767516743a4cb`
- Claim Check owner: `b6901b448b3c7c4c74b4cfc918a9841b7f7bd36bd23bcb33a3e368b161e85c50`
- Claim Check card: `d2e20b22f12c53c36d258666c0aa8b884a125930470ebfa4715ed38e8168b58e`
- Request-Reply Messaging owner: `15e485c75976d0cbdb441a5f435397e6f5f271b2d7942e9fefce4e15e936c482`
- Request-Reply Messaging card: `b4350b59d1c9c671c66197182b0e7a36d4742c2e22df38ef38f32d60b612d960`
- Splitter owner: `da1fa7e4176b6e2c868366fe52dacebc1d622ead96e36c9355fc58c803f4bcdd`
- Splitter card: `129b64d154c06d640a45e6c64c6d240e90d16c26f520dcd1d25544319f1bdc8e`
- Originating pages:
  - `message-selection.md`: `2894a8b6c4cac1c22f46d2d54c5248fa7ce16a3d1a2562e275ca9f10883211f9`
  - `workflow-failure.md`: `efc999753ebeee48cdcefb9add28b156f50c914af8a51f0837106e242a78b9a5`
  - `messaging-families-and-durable-workflows.md`:
    `e045c5fccb1778afbded8e8faa1b32042504432845ed2a5051b3b60317749881`
- V04/C06 chapter README: `9ca4498224f32a16c7d3626211b4922fb1ccd590fbde2802253a630f69593443`

## Verification

- `python3 scripts/book_change.py --plan`: clean.
- Targeted structural validators pass: atlas, cards, coverage, owner units, phase 4,
  registry, semantic audit, sources, delivery evidence, directory migration,
  edition, enrichment, promotions, acceptance, pilot inputs, book metadata and
  corpus qrels.
- `python3 scripts/validate_book_navigation.py` reports the same four
  pre-existing missing-local-anchor issues at the parent HEAD in the B5/B6 pages;
  it reports no new issue at this HEAD.
- `python3 scripts/check_boundary.py`: pass.
- `python3 scripts/check_markdown_line_length.py`: the same two pre-existing V11
  failures remain (c01 anti-corruption-layer line 46 and c11 rbac-abac line 58).
- Full suite at batch end: `python3 -m unittest discover -s tests`, 627 tests, OK
  after updating guards for the new 466-page, 81-owner-page, 16-promotion and
  7-acceptance counts.
- Targeted structural validators ran during editing. The batch-end suite first
  exposed two stale count guards; both were updated and the rerun passed.

## Review packet needed

One fresh external AI review per suspended entry at the review HEAD, using the
card and owner hashes above and the moved-body hashes.

- Card: `book/volumes/v11-pattern-atlas/c03-messaging-integration/<entry>.md`.
- Owner: `book/volumes/v04-distributed-coordination-and-events/`
  `c06-messaging-families-and-delivery-contracts/<entry>.md`.
- Read the exact source units bound in each owner unit, verify byte-level movement,
  all four technical dimensions, alternatives, limits and both reciprocal links.
- Use a different vendor/harness, or a fresh read-only DeepSeek Reviewer that is not
  a fork of this conversation. Work read-only; do not edit, commit, push, open a PR
  or change configuration.
- Do not run tests; the authoring parent already ran the suite once.
- Return a verdict, evidence, findings by severity with exact paths and limits;
  state `sufficient: 0` until a separate promotion commit exists. Do not claim
  owner acceptance.
- Save the raw report under `authoring/ai-reviews/`, add its SHA-256 to the index,
  and rebind a promotion and acceptance only after a pass. Owner acceptance is
  recorded once after all planned batches, not per batch.

## Limits

- This record does not prove correctness, sufficient coverage, independent review,
  CI or merge readiness. It records a structural split and its review hand-off.
- The moved bodies keep their original line breaks, including lines over 100
  characters; the line-length checker covers V11 only.
- Review HEAD is the commit that contains this record; run `git rev-parse HEAD`.
