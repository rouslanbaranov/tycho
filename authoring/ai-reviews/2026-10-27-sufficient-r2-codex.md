# Independent AI re-review — Tycho #540 sufficient-pilot remediation

**Verdict: pass-with-findings for the bounded remediation.**
The six original technical promotion verdicts remain **reject**. No entry qualifies for
promotion. This report accepts the correction of inflated support labels and the safe
rejection state; it does **not** declare every prior finding fully resolved.
`ai_review: performed`; `sufficient: 0`.

## Identity and revisions

- Harness / vendor: Codex desktop app / OpenAI.
- Model: GPT-6 family per session context; exact model name and version are not exposed.
- Session ID: `01a17a03-0b7c-7513-87fe-1f3994862b1d`.
- Timestamp: `2026-10-27T00:53:57+01:00`, Europe/Zurich.
- Repository: `/Users/rbaranov/Projects/tycho`.
- Review HEAD: `55649c3a2541e81a5672cf887f1d45853e10823e`.
- Prior review HEAD: `cf9e02f261d3eeeddd2e3541a5746e5a61500d12`.
- Evidence baseline: `6ff461e73675db642990b55e97df66b26e26bcea`.
- Remediation commit: `a9279b74848d57ecd8f98b255b561b10e151e650`.
- Handoff: `authoring/AI-REVIEW-HANDOFF-SUFFICIENT-R2_2026-10-26.md`, at review HEAD;
  its latest modifying commit is also the review HEAD.
- Original report: `authoring/ai-reviews/2026-10-26-sufficient-pilot-codex.md`.
  Recomputed SHA-256:
  `b755e412cf6de44e58d111448dd2595a228dbd4a133d20087f65ffccd13faaa9`.

I am continuing my own external review, without authoring involvement. OpenAI/Codex is
separate from the DeepSeek authoring harness identified in the request. This is an AI
review, not human owner acceptance.

## Scope and counts

Focused delta review of P540-01 through P540-04 for the same six entries. Inspected the
changed owner-unit evidence, corresponding owner/card passages, manifest, source-plan
bindings, five corrected ledger records, RFC 9700 hash record, outcome and coverage policy.
Compared the prior reviewed snapshot with this HEAD for these artifacts. Extra acceptance
and review-index tooling, the remaining atlas, batch plans and the 155-unit reading were
outside scope.

Counts below were derived from JSON artifacts, not copied from the handoff:

| Artifact / state | Count |
|---|---:|
| Pilot entries, rejected and blocked | 6 |
| Owner-page/card hash checks matching | 12 / 12 |
| Distinct files covered by those hashes | 7 |
| Registry and owner technical: partial-bounded | 141 |
| Registry and owner technical: partial | 4 |
| Registry decision: partial-bounded | 145 |
| Registry overall: partial-bounded / partial | 141 / 4 |
| Promotions allowlist records | 0 |
| Technical / decision / overall sufficient | 0 / 0 / 0 |

These 145-entry counts are mechanical enumeration, not 145 semantic assessments.

## Per-entry verdicts

Dimension order is mechanism, invariant, failure/recovery, alternative. S = supported;
P = partial. These are the corrected artifact labels, read and assessed in this delta
review. They do not mean every possible clause in an S dimension was revalidated anew.
Technical and decision verdicts below concern promotion, separately from remediation.

| Entry | Dimensions | Technical | Decision |
|---|---|---|---|
| Workload Identity / mTLS | S / S / P / P | reject | pass-with-findings |
| Dark Launching / Shadow Traffic | S / P / P / S | reject | pass |
| RBAC / ABAC | S / P / P / P | reject | pass-with-findings |
| Federated Identity | S / S / P / P | reject | pass |
| Controlled Cutover | P / P / P / P | reject | pass |
| Parallel Run | S / P / S / P | reject | pass |

- **Workload Identity / mTLS:** complete recovery/revocation and comparative alternatives
  remain partly synthetic. Technical coverage remains partial-bounded.
- **Dark Launching:** the complete side-effect, measurement and containment rules are
  not established by the admitted source. Technical coverage is now partial.
- **RBAC / ABAC:** the complete invariant, failure/recovery and alternative are partial;
  source-binding contradictions remain below. Technical coverage is now partial.
- **Federated Identity:** stale-key/wrong-issuer recovery and the local-account lifecycle
  comparison are not fully bound. Technical coverage remains partial-bounded.
- **Controlled Cutover:** the general observed-gate mechanism, invariant, recovery and
  alternative are partial; product-specific Spanner steps do not establish the general
  rule. Technical coverage is now partial.
- **Parallel Run:** the full divergence-owner/commit rule and canary/shadow comparison
  remain unsupported in part. Technical coverage is now partial.

No original promotion verdict was upgraded. Decision findings for mTLS and RBAC remain;
new evidence improves their source notes but does not remove all ambiguity.

## Disposition of the original findings

| Finding | Re-review disposition |
|---|---|
| P540-01 | Support-label remediation verified; all six still fail technical promotion. |
| P540-02 | Mostly repaired; residual ASVS contradictions remain in R2-01. |
| P540-03 | ASVS and RFC hashes reproduced; Spanner pin remains unreproduced, R2-02. |
| P540-04 | RBAC note and duplicate fixed; mTLS subset still unspecified, R2-04. |

The explicit rejected/blocked state and zero allowlist remove the immediate risk of
these residual defects being presented as an approved promotion. Consequently, the
remaining defects are non-blocking for retaining this rejected pilot. They must not be
silently carried into a future promotion review.

## Findings

Paths below are relative to the repository root given above; line numbers refer to
review HEAD.

### R2-01 — ASVS still mixes two different source units

Severity: **non-blocking for this remediation; unresolved source-binding defect**.
Affected entry: `tycho.pattern.rbac-abac`. Original findings: P540-02 / P540-03.

Locations:

- `research/sufficient-pilot-540/manifest.json:155–158`, ASVS source unit.
- `edition/patterns/reading-ledger.v1.json:4545–4603`, ASVS record;
  contradictory assertion specifically at line 4588.
- `edition/patterns/source-plan.v1.json:3911` and corresponding ASVS bindings.

The manifest still identifies the OWASP project overview URL. The source plan and
ledger identify the versioned ASVS 5.0.0 PDF. Worse, the PDF record retains this assertion:
“The page is an overview landing page, not the requirement catalogue; it does not define
verification levels.” That assertion contradicts its own full-PDF scope and the document.
The freshly fetched matching PDF defines verification levels on printed page 12 and
contains V8 authorization requirements on printed page 57. A short source quote is:
“The ASVS defines three security verification levels”.

Required action: replace or remove the stale overview assertion in the PDF record and
align the pilot ASVS URL/unit label with the source plan. If the overview remains useful,
keep it as a separately identified source, rather than attributing its scope to the PDF.
The corrected RBAC card itself now correctly names the full PDF; duplicate prose is gone.

### R2-02 — Spanner's refreshed raw HTML hash is not reproducible in this review

Severity: **non-blocking for retaining rejection; source-revision verification gap**.
Affected entry: `tycho.pattern.controlled-cutover`. Original finding: P540-03.

Location: `edition/patterns/reading-ledger.v1.json:5360–5404`, especially line 5402.

A fresh HTTP 200 response from the recorded public URL produces a different SHA-256:

- Recorded: `3e74ffaada1f38992f31b36a199441ff49cffe827c33f7c0ad02aa9e20a335f8`
- Retrieved: `aceba5e262282dda94ac4bde4a902196807b14d93eba73886e356360363b07a4`

The ledger now explicitly warns that the page is mutable and chrome can change bytes.
The retrieved article contains all ten listed headings and supports the bounded
pause/drain/verify/switch sequence. For example, under “Pause application writes”:
“Pause all database write traffic on your application.”

This establishes current passage support, not equality with the author's recorded
representation. I cannot determine whether the byte difference is only site chrome
without the original captured representation.

Required action before using the revision as promotion evidence: make the reviewed
representation reproducible, or provide an independently checkable capture and defined
content-extraction/hash procedure. Merely refreshing a raw HTML hash is insufficient to
prove which representation was read. Do not describe this pin as verified by this review.

### R2-03 — Four manifest current-coverage fields are stale

Severity: **non-blocking metadata inconsistency**.
Affected entries: dark launching, RBAC/ABAC, controlled cutover, parallel run.

Location: `research/sufficient-pilot-540/manifest.json:92,146,303,362`,
`current_coverage`; compare their owner-unit and registry records.

All four manifest fields still say partial-bounded, while both current canonical
artifacts say partial. Rejected/blocked flags are correct, so this does not create a
sufficient entry.

Required action: synchronize the four current-coverage values, or explicitly identify
this field as a historical pre-review snapshot and record current coverage separately.
The current field name and handoff do not establish that historical interpretation.

### R2-04 — The mTLS card still does not identify its cited eight-heading subset

Severity: **non-blocking citation precision issue**.
Affected entry: `tycho.pattern.workload-identity-mtls`. Original finding: P540-04.

Location: `book/volumes/v11-pattern-atlas/c11-security-operations/README.md:244–248`.

The note correctly says all thirty-four served headings were read, but then says
“The eight cited headings support workload identity binding” without identifying those
specific eight. The manifest enumerates thirty-four headings; the note provides no
mapping to an eight-heading subset.

Required action: name or link the actual supporting headings, or remove the unexplained
count and cite the relevant named sections directly. Keep the synthetic limitations.

## Ledger-scope checks

| Record | What was verified in the artifacts | Result |
|---|---|---|
| NIST SP 800-162 | Full 47-page scope; appendices A–B included, not excluded | reconciled |
| OpenID Federation | 21 sections and appendices; no earlier five-section exclusion | reconciled |
| Spanner cutover | Ten headings, including What's next; linked pages excluded | scope reconciled |
| MinimumCD Parallel Run | Eight headings, including Next step and Related content | reconciled |
| ASVS 5.0.0 | Full PDF URL, V1–V17, appendices A–E, correct PDF hash | residual R2-01 |

These checks verify internal read/scope consistency. They do not independently prove
that the author read every page, figure or example.

## Public sources and hashes actually checked

Fresh retrievals all returned HTTP 200. Source bytes were saved only in reviewer scratch
space. The ASVS request redirected to raw.githubusercontent.com at the same tagged file.

- [ASVS 5.0.0 PDF](https://github.com/OWASP/ASVS/raw/v5.0.0/5.0/OWASP_Application_Security_Verification_Standard_5.0.0_en.pdf):
  514,062 bytes, SHA-256
  `a2fa1bbe38f12cac86d3a0f0023327e9772201f65a7f741f282f5e785d268fc5`, matches.
  Extracted the PDF text and inspected structure, verification levels and V8 passages.
- [RFC 9700 HTML](https://www.rfc-editor.org/rfc/rfc9700.html):
  261,599 bytes, SHA-256
  `c00e2234fcd79581bc29669c60d693afaa42f67d9205bddee848f757ae975419`, matches.
  Hash verification only in this round; no complete RFC rereading.
- [Spanner cutover](https://docs.cloud.google.com/spanner/docs/mysql-perform-cutover):
  249,261 bytes; SHA-256 shown in R2-02, does not match.
  Opened and inspected the extracted article and all ten named headings.

NIST, OpenID Federation, MinimumCD and the remaining unchanged pilot source passages
were inspected in my previous review; their public representations were not freshly
retrieved in this round. Their revised ledger scopes were read directly here.

All twelve owner/card SHA-256 comparisons matched their manifest values. Full files,
not individual sections, are hashed. Results are listed below; repeated paths represent
separate manifest checks.

| Entry | File kind | SHA-256 |
|---|---|---|
| workload-identity-mtls | owner | `41462a8c2c148e93cd602b969b0021113263ffb434243218a5c53c0792461bbd` |
| workload-identity-mtls | card | `7f93dcb4dce62fee761fff5db5db6b9289b6a47c668596acc7e7b3a8640a427b` |
| dark-launching-shadow-traffic | owner | `5c95bf668a8c503a5308b1b218950038082a5a5a78ec9a047e424475481f9b91` |
| dark-launching-shadow-traffic | card | `db101e283a93ae0e56276d146f3faeffe1d443e683b40c2367f2cd426393f665` |
| rbac-abac | owner | `26eb70ddf183185cc1cf48ca5f8b23017d652d1c8c5b16342fa2efe0a62b447d` |
| rbac-abac | card | `7f93dcb4dce62fee761fff5db5db6b9289b6a47c668596acc7e7b3a8640a427b` |
| federated-identity | owner | `41462a8c2c148e93cd602b969b0021113263ffb434243218a5c53c0792461bbd` |
| federated-identity | card | `7f93dcb4dce62fee761fff5db5db6b9289b6a47c668596acc7e7b3a8640a427b` |
| controlled-cutover | owner | `c9dc734d942a08082c0e739586337b3ec847b8c9728d3be249d59642c25844d3` |
| controlled-cutover | card | `db101e283a93ae0e56276d146f3faeffe1d443e683b40c2367f2cd426393f665` |
| parallel-run | owner | `5e9c621043bed2fc250d9c8c254b1161beb20f7d820b8cca7fc43b5e637552bb` |
| parallel-run | card | `db101e283a93ae0e56276d146f3faeffe1d443e683b40c2367f2cd426393f665` |

## Checks actually run

Validators ran against an isolated tracked snapshot exported from review HEAD, with a
copied Git database, at `/tmp/tycho-540-sufficient-r2-55649c3a/tree`.
The original checkout was never used as a validator output directory.

In the command table, `PY` means this exact executable:
`/Users/rbaranov/Documents/Codex/2026-10-26/human-reviewer-human-review-private-tmp/work/venv/bin/python`.

| Command, from isolated tree | Exit |
|---|---:|
| `PY -B scripts/validate_sufficient_pilot.py` | 0 |
| `PY -B scripts/validate_sufficient_promotions.py` | 0 |
| `PY -B scripts/validate_pattern_owner_units.py` | 0 |
| `PY -B scripts/validate_pattern_registry.py` | 0 |
| `PY -B scripts/validate_pattern_sources.py` | 0 |
| `PY -B scripts/validate_pattern_cards.py` | 0 |
| `PY -B scripts/validate_delivery_evidence.py` | 0 |
| `PY -B scripts/check_boundary.py` | 0 |
| `PY -B -m unittest discover -s tests -p test_tycho_sufficient_pilot.py` | 0 |

The unit-test command ran one test, successfully. Validators reported 145 owner units,
145 registry entries, 154 read source-plan units, 126 ledger records and three existing
open delivery gaps. Those diagnostics are validator output, not additional substantive
source-reading claims. A validator pass did not detect R2-01 or R2-03.

Other substantive checks: `git rev-parse HEAD`, `git status --short`, targeted
`git diff`/`git log`, JSON enumeration and cross-artifact comparison, SHA-256 recomputation,
three public HTTPS GETs, PDF text extraction with `pdftotext -layout`, and HTML article
extraction. The HTTP/hash script and PDF extraction exited 0; byte inequality was recorded
as a failed comparison, not a subprocess failure.

Two exploratory path probes failed: a shell glob for `tools/validate*` exited 1, and
an `rg` call using the nonexistent `source-reading-ledger.v1.json` exited 2. They were
corrected to `scripts/` and `edition/patterns/reading-ledger.v1.json`. No validator was
omitted because of those probes.

The handoff requests validators but supplies no explicit command list. I used the eight
relevant validators and the focused pilot test from the prior review. New acceptance/
review-index tooling and the full test suite were not run; they are outside this scope.
No requested in-scope validator was unavailable.

Original-checkout verification after checks: HEAD unchanged; status remained the
pre-existing `?? deliverables/`. SHA-256 comparison of all 1,987 initially enumerated
non-Git files found zero changed/deleted files and zero additions. No repository edits,
commits, PRs or configuration changes were made.

## Limits and authority

This is a partial review of a bounded remediation, not renewed full-source coverage.
I challenge treating a disclosed mutable-page hash as a reproduced revision, the stale
ASVS assertion as valid PDF evidence, or synthetic required dimensions as sufficient.
No new source was inaccessible in the three retrievals; the exact recorded Spanner
representation was unavailable for comparison. Unchanged public sources were not all
reopened. No production behavior, security implementation, benchmark or author reading
activity was independently reproduced.

The accepted state is six rejected/blocked proposals, with the residual findings above.
The previous promotion rejection is unchanged. A future promotion needs its own evidence
and review; this report grants no owner acceptance, CI status or merge permission.

## review-manifest

```json
{
  "reviewer": {
    "harness": "Codex desktop app",
    "vendor": "OpenAI",
    "model": "GPT-6 family per session context",
    "exact_model_version": "not available; not exposed",
    "session_id": "01a17a03-0b7c-7513-87fe-1f3994862b1d"
  },
  "timestamp": "2026-10-27T00:53:57+01:00",
  "repository": "/Users/rbaranov/Projects/tycho",
  "review_head": "55649c3a2541e81a5672cf887f1d45853e10823e",
  "prior_review_head": "cf9e02f261d3eeeddd2e3541a5746e5a61500d12",
  "evidence_baseline": "6ff461e73675db642990b55e97df66b26e26bcea",
  "remediation_commit": "a9279b74848d57ecd8f98b255b561b10e151e650",
  "verdict": "pass-with-findings",
  "verdict_scope": "bounded remediation with all six promotion rejections retained",
  "ai_review": "performed",
  "sufficient": 0,
  "counts": {
    "pilot_entries": 6,
    "rejected": 6,
    "blocked": 6,
    "hash_checks": 12,
    "matching_hash_checks": 12,
    "technical_partial_bounded": 141,
    "technical_partial": 4,
    "decision_partial_bounded": 145,
    "promotion_records": 0
  },
  "sampled_units": [
    "tycho.pattern.workload-identity-mtls",
    "tycho.pattern.dark-launching-shadow-traffic",
    "tycho.pattern.rbac-abac",
    "tycho.pattern.federated-identity",
    "tycho.pattern.controlled-cutover",
    "tycho.pattern.parallel-run"
  ],
  "checked_findings": [
    "P540-01",
    "P540-02",
    "P540-03",
    "P540-04"
  ],
  "residual_findings": [
    "R2-01",
    "R2-02",
    "R2-03",
    "R2-04"
  ],
  "technical_promotion_verdict": "reject for all six entries",
  "decision_verdicts": {
    "workload-identity-mtls": "pass-with-findings",
    "dark-launching-shadow-traffic": "pass",
    "rbac-abac": "pass-with-findings",
    "federated-identity": "pass",
    "controlled-cutover": "pass",
    "parallel-run": "pass"
  },
  "validator_exit_statuses": [
    {
      "script": "-B scripts/validate_sufficient_pilot.py",
      "exit_status": 0
    },
    {
      "script": "-B scripts/validate_sufficient_promotions.py",
      "exit_status": 0
    },
    {
      "script": "-B scripts/validate_pattern_owner_units.py",
      "exit_status": 0
    },
    {
      "script": "-B scripts/validate_pattern_registry.py",
      "exit_status": 0
    },
    {
      "script": "-B scripts/validate_pattern_sources.py",
      "exit_status": 0
    },
    {
      "script": "-B scripts/validate_pattern_cards.py",
      "exit_status": 0
    },
    {
      "script": "-B scripts/validate_delivery_evidence.py",
      "exit_status": 0
    },
    {
      "script": "-B scripts/check_boundary.py",
      "exit_status": 0
    },
    {
      "script": "-B -m unittest discover -s tests -p test_tycho_sufficient_pilot.py",
      "exit_status": 0
    }
  ],
  "limits": [
    "Focused remediation, not full 155-unit rereading",
    "Extra acceptance/index tooling and full test suite excluded",
    "Three fresh source retrievals only",
    "Recorded Spanner bytes not reproduced",
    "No owner acceptance, CI or merge permission"
  ],
  "repository_unchanged": true
}
```
