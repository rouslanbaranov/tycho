# B4 review remediation — 2026-10-29

Status: remediation applied. Self-Contained Service, Sidecar and Ambassador remain
`partial-bounded` and are explicitly awaiting a current external review. No promotion,
owner acceptance, CI result or merge permission is claimed.

## Trigger

A separate read-only DeepSeek review of the B4 trio failed with three majors: the
reconciliation, rereview-packet and review-record artifacts still implied current
pass/promotion states after the 2026-10-29 split changed the card and owner-page hashes.
The raw review report is retained by the reviewing session and is not reproduced or
rewritten here.

## Current states

- **Self-Contained Service** — `awaiting-current-external-review`;
  `partial-bounded`; pass pinned to the 2026-10-23 phase-B report and page hash.
- **Sidecar** — `awaiting-current-external-review`; `partial-bounded`; pass pinned to
  the 2026-10-28 report and page/card hashes, with earlier reject and passes also pinned.
- **Ambassador** — `awaiting-current-external-review`; `partial-bounded`; passes pinned
  to the 2026-10-28 reports and page/card hashes, with earlier passes also pinned.

The records carry no top-level current `verdict`. Earlier passes live only in
`historical_reviews`, each with a report SHA-256, review date and page/card hashes where
known. A historical pass does not cover the current bytes.

## Review artifacts

- `edition/patterns/sufficient-review-records.v1.json`: three records replaced with
  explicit current states and pinned `historical_reviews`.
- `edition/patterns/sufficient-review-reconciliation.v1.json`: the same three rows derive
  `awaiting-current-external-review`; no `promoted-after-remediation` label remains for
  them. Historical passes are carried in the row.
- `edition/patterns/sufficient-rereview-packets.v1.json`: the same three packets have
  status and current verdict `awaiting-current-external-review`, blank verdict templates
  and the current page/card SHA-256 values.
- `edition/patterns/independent-rereview-scope-2026-10-22.v2.json` and
  `authoring/SUFFICIENT-REREVIEW-PACKETS_2026-10-22.md` were regenerated.

The state note in both machine-readable artifacts records that the remaining
`promoted-after-remediation` value is a historical agent-review label, not a promotion
record. Promotions remain only in `edition/patterns/sufficient-promotions.v1.json`.

## Minor findings

- Ambassador card priority changed from `core` to `advanced`, matching the registry and
  source plan.
- Ambassador mechanism binding now names the page introduction
  (`Ambassador pattern`) rather than `Solution`. The invariant binding was extended with
  the introduction passage listing the offloaded connectivity capabilities.
- The static-stability shared-page rationale now records two colocated-helper patterns and
  the 2026-10-29 removal of the Immutable Infrastructure owner note. The page front
  matter records `updated_at: 2026-10-29` and `content_review.reviewed_at: 2026-10-29`.
- The Static Content Hosting alternative quote was rebound to the committed owner page
  only; its coverage remains `partial-bounded`.

## Hashes at the B4 state remediation

- Static-stability owner page:
  `2264dc48b01da7eeab3970ce6cf518e8f9a05c5f671fe680f24cb554f229935a`
- Ambassador card:
  `09641386ebe9650028c6ae30bd2342f06790b38fa8fe15797b9ca01ed663d508`
- Sidecar card:
  `d2169cf74651eac88b0a169f144a6a16bcfbc057778e81f798c4cca565112d7a`
- Self-Contained Service card:
  `1b7839e0a8ac2993cbfdd451fa7cf58bd1511dd1f731a949cb56dc3ae3f333c7`
- Self-Contained Service owner page:
  `f343e82b6b2fb24904176c2652dfabfbc4c92aecb3e91feb478d3fc35e07fd48`

## Final review remediation hashes (2026-10-29)

These are the raw page hashes after the final review corrections and refresh.
Use them for the next bounded review; they do not supersede a fresh review at
the actual review HEAD.

- Static-stability owner page:
  `df04214db202ee955cedd9960f76e53d24463e1ea64e7e4ff409f6986d269006`
- Ambassador card:
  `92c94ca49e8fdc4b1957426ab54ca4e3031352ddb8c91f83f2ee40f46a4c7414`
- Sidecar card:
  `0bda31b15bb32b344b3fd4d93812785509d11dd057c0891e8c1fcbb97a398f62`
- Self-Contained Service card:
  `5fa28c2c6898babeae6cb2a7cf731cc0e345a00717e539fddb54c045accea4e0`
- Self-Contained Service owner page:
  `078a010f10488fa95087e3f3a6ed775a11828e726dbe23e85ac24808783342a3`

## Verification

- `python3 scripts/book_change.py --plan`: clean.
- `python3 scripts/refresh_atlas_artifacts.py --authorize ...`: completed; derived
  artifacts and authorized revisions refreshed.
- Structural validators: pattern registry, cards, owner units, sufficient promotions and
  sufficient owner acceptance pass.
- `python3 scripts/check_boundary.py`: pass.
- `python3 scripts/check_markdown_line_length.py`: the same three pre-existing V11
  failures remain.
- `python3 -m unittest discover -s tests`: 617 tests, OK (run once at batch end).

## Final review remediation (2026-10-29)

A later read-only DeepSeek review of the same three entries returned two major and
five minor findings. The raw report remains with the reviewing session. This
remediation does not promote an entry or restore owner acceptance.

- **Self-Contained Service:** the owner-page link now targets the dedicated card;
  the chapter README keeps only a pointer and no duplicate body. The mechanism
  quote uses the exact binding wording, failure/recovery binds the pattern's
  recovery outcome instead of the baseline problem, and the route exclusion is a
  scope limit rather than a coverage disclaimer.
- **Ambassador:** the owner note and card restore the source hedge ("might not be
  safe", "all operations") and narrow the hard contraindication to
  ambassador-managed retries on non-idempotent operations; other offload uses
  remain viable. The definition is attributed as the source's analogy and the
  invariant uses binding wording instead of "remote services".
- **Sidecar:** the route question matches the full decision question. The
  static-stability Ambassador pattern-atlas link is separated from the Sidecar
  link.

All three remain `partial-bounded` and `awaiting-current-external-review`.
`tests/test_tycho_b4_review_remediation.py` guards these corrections.

## Review needs

A fresh external review is required for each of the three entries at the review HEAD.
Reviewers must use the current owner/card hashes above, verify every historical pass is
labelled historical, and return a bounded verdict with findings by severity. Do not infer
owner acceptance and do not restore a promotion from a historical pass.

## Limits

This record is remediation evidence. It does not prove correctness, sufficient coverage,
independent review, CI or merge readiness. Review HEAD is the commit that contains this
record; run `git rev-parse HEAD`.

The standalone `validate_book_navigation.py` reports two pre-existing missing local
anchors in B5/B6 split owner pages (Dark Launching and RBAC/ABAC); this change does not
edit those pages. The full suite remains green.
