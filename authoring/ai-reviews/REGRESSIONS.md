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
  and binding to cover all five named cases.
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

A future finding without a guard is not closed. If the guard cannot be mechanical,
record the exact manual check and the review that performed it.
