# Review finding regression guards

Every review finding must add a mechanical guard, or record why a semantic
guard is not yet possible. The guard is part of closing the finding.

- **P540-01 source-support overstatement:** `tests/test_tycho_pattern_owner_units.py`
  requires a nonempty reason for every supported dimension. A per-dimension source
  binding is still pending; this is the remaining semantic gap.
- **P540-02 ledger scope contradictions:** `tests/test_tycho_ledger_scope.py`
  rejects overlap between `sections_read` and `sections_not_read`.
- **P540-03 non-reproducible hashes:** `scripts/source_content_hash.py` and
  `tests/test_tycho_source_content_hash.py` define canonical text hashing; the pilot
  validator checks manifest/source-plan unit fields.
- **P540-04 stale card notes:** `tests/test_tycho_card_source_notes.py` rejects the
  old ASVS overview phrases and requires the named mTLS subset.
- **R2-01 stale ASVS manifest:** `scripts/validate_sufficient_pilot.py` compares every
  manifest source-unit field with the source plan.
- **R2-03 stale manifest coverage:** the pilot validator compares `current_coverage`
  with owner units.
- **R3-01 shared ASVS citation fan-out:** the card-source-note test rejects the stale
  overview wording on the shared C11 page.
- **Claim Check review 2026-10-29:** `tests/test_tycho_claim_check_review.py` requires
  payload-lifecycle wording in the card and owner, limits the owner-unit notes to the
  Microsoft bindings plus the stored-payload-only EIP role, and requires the failure quote
  and binding to cover all six named cases.
- **B4 review remediation 2026-10-29:** `tests/test_tycho_b4_review_remediation.py`
  requires Self-Contained Service, Sidecar and Ambassador to stay
  `awaiting-current-external-review` with pinned historical passes, no
  `promoted-after-remediation` row or packet, no promotion record and
  `partial-bounded` coverage. It also guards the Ambassador priority and binding
  labels and the static-stability two-pattern rationale and 2026-10-29 metadata.
- **B4 final review remediation 2026-10-29:** the same test module now guards the
  Self-Contained Service owner link to the dedicated card, the README pointer-only
  section, exact binding wording for the mechanism and recovery dimensions, a scope
  exclusion instead of a coverage disclaimer, the Sidecar route question matching its
  decision question, the separated static-stability Ambassador link, and the
  Ambassador retry hedge, analogy attribution and binding wording.

- **B8 review remediation 2026-10-29:** `tests/test_tycho_b8_review_remediation.py`
  guards the Resequencer alternative trigger and unbounded-buffer failure, the Pipes
  ordering-only invariant binding, the labeled in-process fallback and card alignment,
  the 2026-10-29 Pipes card date, and both entries remaining `partial-bounded` without
  promotion.
- **B8 Claim/Request-Reply/Splitter remediation 2026-10-29:** the same test module guards
  the Request-Reply Limits and Decision components, the removed blocking-call
  contraindication, the scoped Correlation Identifier guidance, the `Request-Reply`
  alternative binding, the 2026-10-29 card dates, Claim Check's separation of payload
  deletion ownership from independent authorization, Splitter's Iterators binding for
  unknown-size release and expiry, and all three entries remaining `partial-bounded`
  without promotion.
- **B8 Claim/Request-Reply/Splitter majors follow-up 2026-10-29:** the same test module now
  guards the Claim Check binding's own write-before-publish quote, its six failure cases and
  inline-alternative binding; the Request-Reply `private to the requesting thread` decision,
  Synchronous Block attribution and Tycho multiple-outstanding correlation path; and the
  Splitter identity/position/size invariant, Camel value-based watermark attribution,
  default-output binding, provider-documentation limits and Tycho ownership label.
- **B8 Claim/Request-Reply/Splitter C/R/S review 2026-10-29:** the same test module now
  guards Splitter's supporting `Programming Model` header binding, card header quote and
  Tycho inference/contraindication labels; Request-Reply's `Asynchronous Callback` supporting
  binding and RPC Tycho synthesis label; and Claim Check's `Alternatives` compression binding,
  Tycho reversal/expiry labels and defined tenant binding.
  `tests/test_tycho_pattern_owner_units.py` guards supporting-binding sections.
- **B8 final Claim/Request-Reply/Splitter C/R/S review 2026-10-29:** the same test module now
  guards Claim Check's inline-fit exception in card and owner, the source-stated
  sensitivity/repeated-serialization conditions with Tycho retention, the reversal
  precondition, and the write/transport/retrieval mechanism binding; Splitter's source
  incomplete-aggregate statement against Tycho partial-result or forced-closure guidance in
  card, owner and Limits, plus the narrowed Camel default-output mechanism claim; and
  Request-Reply's separated channel/invocation decision question, both-block statement, RPC
  synthesis label and partial alternative state.

- **B9 Gatekeeper mechanism review 2026-10-29:**
  `tests/test_tycho_b9_gatekeeper_review_remediation.py` rejects the
  "authenticates the caller" and "coarse authorization" mechanism wording, requires
  the `Solution` binding to name validation and authorization, requires the
  `Workload design` supporting binding to name authentication initiation, checks
  card/owner alignment, and pins `partial-bounded` coverage without promotion.

- **B47 Consistent Hashing reviews 2026-10-31:** `tests/test_tycho_b47_consistent_hashing_review.py`
  guards all four supported dimensions against read ledger records, the invariant quote and
  its expectation qualification, the Tycho synthesis labels, the corrected Dynamo 4.2
  supporting section, the 2026-10-31 register scopes, the historical 2026-10-23 page pin,
  the page-changed-since-review packet, and the promotion hashes. Codex recorded one minor
  formula note (B47-M1, join/leave denominator); a supplementary same-vendor review
  recorded nine provenance minors. Both found no blocking or major finding. B47-M1 and the
  content-level minors stay recorded, not silently closed; metadata minors were fixed
  forward.

A future finding without a guard is not closed. If the guard cannot be mechanical,
record the exact manual check and the review that performed it.
