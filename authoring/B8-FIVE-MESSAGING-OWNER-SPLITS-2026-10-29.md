# B8 — five messaging owner splits, 2026-10-29

Status: split complete and review-ready. Review remediation for all five entries was
applied on 2026-10-29. No promotion or owner acceptance is claimed, and the remediated
bytes still need a current external review.

## Parent and scope

- Batch base HEAD: `fbe9b7899f6b6aab50959c374851003457f0b2d0`.
- Split commit direct parent: `33dc0be964623515c00ae06050dc8b88d907a3df` (a
  governance-only AGENTS change that landed during the batch; no book or edition
  artifact changed).
- Two documentation-only follow-up commits corrected this record; use
  `git rev-parse HEAD` for the review HEAD.
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

At the split, every moved body was a byte-for-byte substring of its new owner page and
was absent from the originating page. SHA-256 values below cover the moved body only
and describe the split state; the review remediation changed the bodies, so they are
historical, not current-page checks.

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

These are the hashes at the split state. They are historical after the review
remediation in the next section.

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

## Review remediation — 2026-10-29

A separate read-only DeepSeek review recorded at
`authoring/ai-reviews/2026-10-29-resequencer-pipes-deepseek.md` returned a pass with
five minor findings, pinned to `a66d8534`. The findings were rechecked against the
split pages and fixed forward under rule 33; no promotion or acceptance was restored.

- Resequencer: the owner decision no longer treats an unbounded buffer as a reason to
  partition by key. An unbounded buffer now rejects the resequencer or fails the
  ordering scope, and the card failure path names the same disposition. The card and
  owner decision, alternative and failure now agree.
- Pipes and Filters: the invariant is bound only to the ordering claim at
  `Parallel Processing (p.74)`; the filter-interface and port claim moved to
  Mechanism under the `Solution (p.71)` quote. The in-process fallback is labeled as
  Tycho guidance in both owner and card, and the card reversal matches the owner
  wording. The card `content_review.reviewed_at` and `updated_at` are `2026-10-29`.
- Both entries remain `partial-bounded`; no promotion, owner acceptance or sufficient
  coverage is claimed.
- Guard: `tests/test_tycho_b8_review_remediation.py`.
- Remediated hashes:
  - Resequencer owner: `731af4b2b51b919b3703e7ef554be0983b5347846a04b1c9f905fc88e24098e4`
  - Resequencer card: `0c33b4fd1f074ef0d7838216ec32f7d3b67ae521505f032e897ab64227b744d3`
  - Pipes owner: `45b03be36f7f65cbff3eb28137c5768502716b4b1db8b18170f8564880156059`
  - Pipes card: `a3b30a356ec6c29780c924e140841343b994830d1bf30f472412741c82c1e929`

### Claim Check, Request-Reply Messaging and Splitter

The same B8 review returned separate findings on these three entries. The raw report is
retained by the reviewing session and is not reproduced or rewritten here. The findings
were fixed forward under rule 33; all three remain `partial-bounded`, awaiting a current
external review, with no promotion or owner acceptance restored.

- Request-Reply: the owner page gained an explicit Limits component for the
  correlation/private reply channel, one outstanding request, timeouts, duplicate replies,
  the callback contract and the publisher-abridged source. The card gained a Decision
  component and distinguishes messaging Request-Reply from direct synchronous RPC; the
  Correlation Identifier relation is scoped to multiple outstanding requests as Tycho
  guidance; the blocking-call contraindication is replaced; the RPC alternative is labeled
  Tycho synthesis; and both card dates are `2026-10-29`. The alternative binding moved from
  `Solution (unheaded)` to `Request-Reply`: the sentence sits in the Request-Reply body
  before the Synchronous Block approach, not inside that bullet.
- Claim Check: the invariant now binds the source's payload-lifecycle ownership and
  independent-authorization text. Owner and card separate payload-deletion ownership from
  authorization as an independent interaction with the data store.
- Splitter: the invariant now binds the Spring Integration Iterators paragraph for
  unknown-size `SEQUENCE_SIZE`, release strategy and expiry. Card and owner failure text
  state the source's incomplete-aggregate consequence and the required release or expiry.
- Guard: `tests/test_tycho_b8_review_remediation.py` (both remediation groups).
- Remediated hashes:
  - Claim Check owner: `fa30b4b0d3285011af535070730f72b7092663986baaa32e54bfe4976c8cb552`
  - Claim Check card: `bbdc786487f100ac64547b5896e5538c9943cd17d321c3a04267290807e0f549`
  - Request-Reply Messaging owner:
    `5eca88a08da75da896ff152f059d5d817567dc274e645f1aa58ae267ede4fc85`
  - Request-Reply Messaging card: `d30687d3215c2d5d2a41b5334bd9ec10519a1a06db323c5a3ab15967eed98299`
  - Splitter owner: `4a3d29b1e7cdda3b3a73ef7260ebbfe0dd3d704bab795a90321b0c396687c773`
  - Splitter card: `ca3cb782815465f811aa06b1876094147b13bd1ddf021aa22970cdb7ddd466e1`

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
- Full suite at batch end: `python3 -m unittest discover -s tests`, 639 tests, OK.
  The pre-remediation baseline was 627 tests; the B8 remediation guard adds 12 tests
  (five for Resequencer/Pipes and seven for Claim Check/Request-Reply/Splitter).
- Targeted structural validators ran during editing. The batch-end suite first
  exposed two stale count guards; both were updated and the rerun passed.

## Review packet needed

One fresh external AI review per suspended entry at the review HEAD, using the
current card and owner hashes in the review-remediation section. The post-split
and moved-body hashes are historical and do not describe the remediated bytes.

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
