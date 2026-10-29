# B9 Health Readiness review remediation — 2026-10-29

Status: remediation applied. Health, Readiness and Liveness Checks remains
`partial-bounded`; no promotion, sufficient-coverage claim, independent review,
owner acceptance or merge permission is added. A fresh external review is still
required at the review HEAD.

## Trigger

A separate read-only review of the B9 Health card reported five bounded findings.
The raw report remains with the reviewing session and is not reproduced here.
The findings concerned card source scope, stale review/source dates, an
alternative binding that did not carry the telemetry sentence, a failure summary
that deferred to the owner without stating the path, and a truncated route
question that dropped startup completion.

## Corrections

1. **Source scope.** The card `evidence_scope.source_ids` now lists
   `src.kubernetes` and `src.microsoft-cloud-patterns`. The card Sources
   paragraph names the Microsoft ledger record
   `read.microsoft-health-endpoint.2026-10-29`. The owner unit adds an
   `auxiliary` declaration under `source_support` with the Microsoft source,
   ledger record and canonical revision
   `b5b302585c4e60a5d696b128b6a03d21c9629848e9fa2be23e6e1bc1751d1d61`;
   the owner-unit schema and validator check these auxiliaries against the
   source plan and reading ledger.
2. **Dates.** Card `content_review.reviewed_at`, `updated_at` and
   `source_inspection_date` are `2026-10-29`. The owner page review date and
   update date are `2026-10-29`; its `source_inspection_date` remains the
   decomposition-pinned `2026-10-20` for the inherited SRE source, and the
   source boundary records the Microsoft page update and 2026-10-29 access.
3. **Telemetry alternative.** The owner alternative keeps its transport-level
   primary binding and adds a `supporting_bindings` entry for the exact
   telemetry sentence in the actual `When to use this pattern` section. The
   binding revision matches the ledger record.
4. **Failure and recovery.** The card now summarizes the owner failure path
   (false restart or traffic to an unready instance), the cost of false
   positives and shared-dependency coupling, and the containment measures
   (bound probe timeouts, consecutive failures, no shared-dependency checks in
   liveness).
5. **Route question.** The card `route_hints` question is restored in full:
   "Should the runtime distinguish process liveness, traffic readiness and
   startup completion?" The route index derived from it matches the owner-unit
   decision question.

## Artifact hashes after refresh

- Card:
  `217eb5673c474bae25db9041ac0d167a27b4e4ec7c26acb9d45d0b8165aac83c`
- Owner page:
  `a6865e286768c612b758131b7ec1e99836975100269ea962fcd0b979028a0cb8`
- Owner units:
  `63b97e1d8abcdfc1b2d72638a9b189c690e56e5e3b954e85037666aa80938c33`
- Owner-unit schema:
  `e0d1718291f106a6ae7a12741f9df02a5de9aab196eea535b108acc5b650da23`
- Owner-unit validator:
  `b13d8308481cfa5fe0c27e338de8ada1db3235a8e6597eaabba47dd8973df9b8`
- Regression test:
  `fdc9ee5a7856fc33073eaeab17619fe211d68cd24bc394fa1c7614ef79a71154`

## Verification

- One authorized refresh rebuilt the route index, section index, census,
  coverage, phase 4, inventory, source plan, candidates, reconciliation, review
  scope and packets. A second authorized refresh recorded the correction that
  keeps the owner page's decomposition-pinned source date.
- Target validators pass: atlas, cards, coverage, owner units, phase 4,
  registry, semantic audit, sources, edition and inventory.
- `python3 scripts/book_change.py --plan`: clean.
- `python3 scripts/check_boundary.py`: pass.
- `python3 scripts/check_markdown_line_length.py`: pass; 145 exact owner-link
  exceptions.
- Targeted unit tests: 135 tests, OK.
- Full suite: run once at the batch end (result recorded in the session, not
  claimed here as CI).
- The new `tests/test_tycho_b9_health_remediation.py` guards these corrections.

## Limits

- No entry reaches `sufficient`; the 22 existing promotions are unchanged and
  Health is not one of them.
- The Microsoft binding covers only the named `When to use this pattern`
  section and page revision; linked pages and figures were not read.
- This record is remediation evidence, not independent review, owner
  acceptance, CI or proof of source truth.
