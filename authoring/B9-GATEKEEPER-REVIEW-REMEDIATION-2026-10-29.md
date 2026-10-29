# B9 Gatekeeper mechanism review remediation — 2026-10-29

Status: remediation applied. Gatekeeper remains `partial-bounded`; no promotion,
sufficient-coverage claim, independent review, owner acceptance or merge
permission is added. A fresh external review is still required at the review HEAD.

## Trigger

A separate read-only review of the B9 Gatekeeper card reported one minor finding:
the owner-unit mechanism quote claimed the gatekeeper "authenticates the caller
and evaluates coarse authorization", while its bound source passage only
described validation and sanitization. The raw report remains with the reviewing
session and is not reproduced here.

## Correction

- The mechanism quote is now: "A gatekeeper is a dedicated request-validation
  boundary that validates and sanitizes requests before forwarding them to the
  protected service; it can also centralize authentication initiation and
  authorization checks." It no longer says the gatekeeper authenticates the
  caller or evaluates "coarse" authorization.
- The primary binding is `Solution`, quoting the passage that requires the
  gatekeeper to validate and sanitize request content and says gatekeepers might
  authorize the request.
- A `supporting_bindings` entry uses `Workload design`, quoting the sentence
  that names authentication initiation and authorization checks.
- Both bindings use the admitted `read.microsoft-gatekeeper.2026-10-21` record
  and its recorded revision.
- The card good-fit condition now says the gatekeeper can centralize
  authentication initiation and authorization checks; its Sources note names the
  two bound sections.
- The owner Gatekeeper note uses the same narrowed mechanism sentence, the Limits
  wording says "only initiates authentication", and the Source boundary names the
  two sections.
- The owner-unit `notes` field records the new bindings.

## Source verification

- The public page was fetched on 2026-10-29. Its canonical article text SHA-256
  under `scripts/source_content_hash.py` is
  `d7c92cbbce501ce13865c0250593e92f7d68aa4c1a64240597ef11ca006d8151`; all three
  quoted passages are present verbatim.
- The ledger record's revision `5af11b96...` was recorded on 2026-10-21, before
  the committed canonical extractor existed. This remediation retains that
  revision and does not substitute the 2026-10-29 hash into the ledger.
- The page's `updated_at` value (2026-09-25) predates the 2026-10-21 read, and
  the record lists `Solution` and `Workload design` in `sections_read`. The
  new bindings therefore stay on the admitted record without asserting a fresh
  revision identity.
- Linked pages, figures and executable behavior remain outside scope.

## Artifact hashes after remediation

- Card: `809e11c39e1b634b05be40ef94fd88387b649275879de5e034d5296b42a25f2f`
- Owner page: `459e7c7b14e7a11c5e6ff58d029cbcfbb390dd267bdb4847affcb556a7ad5e0f`
- Owner units: `00bacb5a32bf55b32a7d8da61c917d2d711b406cbf1b1f7963bf7946f2feb665`
- Regression test: `dfdd43e44633b3e05e0e36ce6ea554cd9ccc1aac3ebcdb6d8393167da5a4583f`

## Verification

- `python3 scripts/preflight_sufficient.py --pattern tycho.pattern.gatekeeper`:
  PASS, 1/1 entries preflight clean. This is the pre-review gate and does not
  replace review.
- One authorized refresh rebuilt the route index, section index, census,
  coverage, phase 4, inventory, source plan, candidates, reconciliation, review
  scope and packets.
- Target validators pass: atlas, cards, coverage, owner units, phase 4, registry,
  semantic audit, pattern sources, sources, delivery, directory, edition,
  enrichment, promotions, owner acceptance, pilot, metadata schema examples,
  corpus qrels, claim references, book metadata and decomposition.
- `python3 scripts/book_change.py --plan`: clean.
- `python3 scripts/check_boundary.py`: pass.
- `python3 scripts/check_markdown_line_length.py`: pass; 145 exact owner-link
  exceptions.
- `python3 scripts/validate_book_navigation.py`: the same four pre-existing
  missing-local-anchor findings in the dark-launching and RBAC/ABAC pages.
- Full suite: `python3 -m unittest discover -s tests`, 702 tests, OK
  (run once at remediation end).
- `tests/test_tycho_b9_gatekeeper_review_remediation.py` guards the correction.

## Limits

- No entry reaches `sufficient`; the 22 existing promotions are unchanged and
  Gatekeeper is not one of them.
- The Gatekeeper review packet remains `page-changed-since-review` with the
  historical 2026-10-23 page hash pinned; its pass fields describe that historical
  review and do not cover the current bytes. No promotion record or owner
  acceptance exists, and none is claimed.
- The 2026-10-21 revision hash is not recomputable with the current extractor.
  The 2026-10-29 canonical hash in this record is verification evidence only.
- This record is remediation evidence, not independent review, owner acceptance,
  CI or proof of source truth.
