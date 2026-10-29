# B7 — Service Discovery split, 2026-10-29

Status: split complete and review-ready. No external review, promotion or owner
acceptance was performed in this batch.

## Parent and scope

- Parent HEAD: `a51015ad77ee1f9884ac982134f87f30c1c79160`.
- One accelerated batch covering the C02 residual in
  `authoring/FROZEN-SPLIT-INVENTORY-2026-10-29.md`.
- Two pages were added: one atlas card and one dedicated owner note.
- The Service Discovery promotion and owner acceptance are suspended; all four
  technical dimensions remain supported and coverage is `partial-bounded`.

## Move

- Source card: `book/volumes/v11-pattern-atlas/c02-api-communication/README.md`,
  section `### Service Discovery` (lines 325-351 at the parent HEAD).
- New card page:
  `book/volumes/v11-pattern-atlas/c02-api-communication/service-discovery.md`.
- Source owner section: `discovery-balancing.md` in the V08/C08 chapter
  (`c08-network-request-paths-routing-and-edge-delivery`), section
  `### Service Discovery` (lines 212-222 at the parent HEAD).
- New owner page: `service-discovery.md` in the same V08/C08 chapter.
- Both source sections keep their `#service-discovery` anchors as one-line index
  links.
- The Client-Side Discovery, Server-Side Discovery and Load Balancing sections
  remain on the original owner page; only their line coordinates changed.

## Reciprocal links

- The new card's technical-owner link points to the new owner page.
- The original owner page's atlas link points to the new card page.
- The V08/C08 chapter landing lists the new owner note.
- The C02 chapter keeps `### Service Discovery` as an index link to the card.

## Verbatim check

- Owner moved body SHA-256:
  `b60e1af59584ce638f52e5528f3d2017cebf81a0f9fb6c20f37e42b4b44b2319`.
  The same bytes are a contiguous substring of the new owner page.
- Card moved body SHA-256 before the link update:
  `664b316950cbf14153d21a4665fc5e03b671e177a9efdf68ce3f04410a434b60`.
- Card moved body SHA-256 after normalizing only the technical-owner link path:
  `1d78d0ce27e854d76381815d2f4ced8519d47e22c9d139fb688a8df529359f3c`.
  That normalized body is a contiguous substring of the new card page.
- No other card or owner sentence changed in the move.

## Registration

- Atlas manifest: 43 documents; registry unchanged at 145 patterns.
- Directory migration: two records and two canonical additions; 461 canonical
  documents.
- Document identities and semantic audit: two pages; 461 semantic pages.
- Enrichment manifest: the new owner page is registered with `origin_page` and
  `origin_heading`; no new source inspection is claimed.
- Card batches: `card_path` and the owner path are rebound for Service Discovery.
- Owner units: 76 owner pages and 30 shared pages; the original page now owns three
  discovery and balancing units.
- Registry, owner-unit, ready-plan and delivery-evidence coverage is
  `partial-bounded` for Service Discovery.
- Promotions: 20 remain; Service Discovery is removed from the promotion list.
- Owner acceptance: 8 entries remain; Service Discovery is removed from the
  accepted entries and review-report list.
- The saved Service Discovery review report remains on disk and is not reused.
- Qrels Q109 is retargeted to the new owner page; Q110 remains on the original
  page for Server-Side Discovery.

## Post-split hashes

- C02 chapter README SHA-256:
  `e89715b94c87a103b38c257fbcf9b17fa5d599761c27a9d0e84166186c637c7f`
- New card page SHA-256:
  `0485d5067d81f0ae0b634f42d9289f0fa04623aa20f6ae74d446b153d6490337`
- New card page body SHA-256:
  `6db75a4302acbc3387c5ffea63775eff822ee0bfd472a0cfebbdfad345703408`
- New owner page SHA-256:
  `fc5b99e5b1d86d82e060bb5d05267c32ec548567545b6aba2bc5c2e0e5d671b5`
- Original owner page SHA-256:
  `06793f0c4ec2e190b98add3171847cd71aa215904da7aa9306a4c9969e630cef`
- V08/C08 chapter README SHA-256:
  `53cf9e8532be7eda7f44b3ddae44117533635358704e0854e3a4a457d29b6174`
- New card migration baseline SHA-256:
  `ad1f2ab201a252b448c4af03a300882aaea189e5a0c5c632dd51f6c6a03a3c70`
- New owner migration baseline SHA-256:
  `20d9b649f4ed41c929a0e1690e835c04e7e4eb38c8de3970162be5a38a1dbb72`

## Verification

- `python3 scripts/book_change.py --plan`: clean after refresh.
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
- Full suite at batch end: `python3 -m unittest discover -s tests`, 627 tests, OK.
- No test was run during editing; the full suite ran once at the batch end.

## Review packet needed

One fresh external AI review for Service Discovery at the review HEAD:

- Card: `book/volumes/v11-pattern-atlas/c02-api-communication/service-discovery.md`,
  SHA-256 `0485d5067d81f0ae0b634f42d9289f0fa04623aa20f6ae74d446b153d6490337`.
- Owner: `service-discovery.md` in the V08/C08 chapter
  (`c08-network-request-paths-routing-and-edge-delivery`), SHA-256
  `fc5b99e5b1d86d82e060bb5d05267c32ec548567545b6aba2bc5c2e0e5d671b5`.
- Owner moved-body SHA-256:
  `b60e1af59584ce638f52e5528f3d2017cebf81a0f9fb6c20f37e42b4b44b2319`.
- Read the exact source units bound in the owner unit: `src.envoy` record
  `read.envoy-service-discovery.2026-10-21`, sections listed in
  `edition/patterns/owner-units.v1.json`.
- Verify byte-level movement, all four technical dimensions, alternatives, limits
  and both reciprocal links.
- Use a different vendor/harness, or a fresh read-only DeepSeek Reviewer that is not
  a fork of this conversation. Work read-only; do not edit, commit, push, open a PR
  or change configuration.
- Do not run tests; the authoring parent already ran the suite once.
- Return a verdict, evidence, findings by severity with exact paths and limits;
  state `sufficient: 0` until a separate promotion commit exists. Do not claim
  owner acceptance.
- Save the raw report under `authoring/ai-reviews/`, add its SHA-256 to the index,
  and rebind the promotion and acceptance only after a pass. Owner acceptance is
  recorded once after all planned batches, not per batch.

## Limits

- This record does not prove correctness, sufficient coverage, independent review,
  CI or merge readiness. It records a structural split and its review hand-off.
- The moved owner paragraph keeps its original line breaks, including one
  123-character line; the line-length checker covers V11 only.
- Review HEAD is the commit that contains this record; run `git rev-parse HEAD`.
