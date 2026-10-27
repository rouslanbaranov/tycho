# Independent AI re-review — Tycho #540 sufficient R3

**Verdict: pass-with-findings for the focused remediation.**
R2-01 through R2-04 are addressed for the six pilot entries. One non-blocking shared-source
citation defect remains in three other cards on the same chapter page. All six technical
promotion verdicts remain **reject**. `ai_review: performed`; `sufficient: 0`.

## Identity and snapshot

- Harness / vendor: Codex desktop app / OpenAI.
- Model: GPT-6 family per session context; exact deployed model/version not exposed.
- Session ID: `01a17a03-0b7c-7513-87fe-1f3994862b1d`.
- Review timestamp: `2026-10-27T01:12:00+01:00`, Europe/Zurich.
- Repository: `/Users/rbaranov/Projects/tycho`.
- Actual review HEAD: `7482e650e0628e6d62096cdc50ede9519c4175d3`.
- Prior reviewed HEAD: `55649c3a2541e81a5672cf887f1d45853e10823e`.
- Named remediation commit: `eea4d89169a320a685567fbd7cc13305fb0b48ca`.
- Handoff: `authoring/AI-REVIEW-HANDOFF-SUFFICIENT-R3_2026-10-27.md`, at review HEAD.
  Last modifying commit: `a891d95efba8833b1260b679e792dced6433883b`.
- Policy: `governance/SUFFICIENT-COVERAGE.md`, at review HEAD.
- Prior report: `authoring/ai-reviews/2026-10-27-sufficient-r2-codex.md`.
  Recomputed SHA-256:
  `3997c55722125ca28477b4a0e07feb57437710ed334708595187effb1ded5278`.

This is the same independent external reviewer continuing its own earlier reviews.
I did not author the remediation. OpenAI/Codex is separate from the DeepSeek authoring
harness identified in the handoff. This is an AI review, not human owner acceptance.

## Exact scope

Reviewed only R2-01 through R2-04 and the required preservation checks for the same six
pilot entries. Compared the prior reviewed snapshot with pinned current HEAD. Read the
changed manifest, ledger, card note, hash script, pilot-validator changes and focused tests;
compared source-plan bindings and current owner/registry coverage mechanically.

Freshly retrieved three public sources: Spanner cutover HTML, ASVS 5.0.0 PDF and Istio
Security HTML. Reproduced the canonical Spanner digest using both the script's URL mode
and its local-file mode. Checked the eight named Istio headings and their relevant content.
Checked ASVS PDF identity and targeted verification-level/authorization passages.

The other three ASVS card notes were encountered on the shared chapter page while checking
the changed citation. Only their explicit source-record mismatch is assessed here; their
technical or decision sufficiency was not reviewed. No full 155-unit rereading, new
six-entry qualification, remaining-atlas assessment, full-suite review or owner-acceptance
review was performed.

## Counts derived from artifacts

Counts were independently enumerated from the pilot manifest, owner units, registry and
promotion allowlist. They were not copied from the handoff.

| State | Count |
|---|---:|
| Pilot entries rejected / blocked | 6 / 6 |
| Matching owner-page/card hash checks | 12 / 12 |
| Distinct owner/card files hashed | 7 |
| Manifest/source-plan field mismatches | 0 |
| Manifest/current owner-coverage mismatches | 0 |
| Technical coverage: partial-bounded / partial | 141 / 4 |
| Decision coverage: partial-bounded | 145 |
| Overall coverage: partial-bounded / partial | 141 / 4 |
| Promotions | 0 |
| Technical / decision / overall sufficient | 0 / 0 / 0 |

The 145-entry coverage enumeration is mechanical, not 145 substantive reviews.

## Per-entry verdicts

These verdicts concern promotion. The remediation verdict above has a different scope.
S = supported; P = partial. Dimension order: mechanism, invariant, failure/recovery,
alternative. Owner-unit dimension labels are unchanged since R2.

| Entry | Dimensions | Technical | Decision |
|---|---|---|---|
| Workload Identity / mTLS | S / S / P / P | reject | pass |
| Dark Launching / Shadow Traffic | S / P / P / S | reject | pass |
| RBAC / ABAC | S / P / P / P | reject | pass |
| Federated Identity | S / S / P / P | reject | pass |
| Controlled Cutover | P / P / P / P | reject | pass |
| Parallel Run | S / P / S / P | reject | pass |

The mTLS and RBAC decision assessments improve from pass-with-findings to pass on new
evidence: the previously ambiguous heading subset and the pilot ASVS binding are now
correct. The other four decision passes are retained from the prior review. These are
bounded delta conclusions, not fresh complete technical reviews. Every entry still has
partial required technical dimensions, so none has both promotion passes.

## Disposition of R2-01 through R2-04

All locations below refer to review HEAD, relative to the repository root above.

### R2-01 — Addressed for the pilot ASVS binding

Evidence:

- `research/sufficient-pilot-540/manifest.json:155–183` now identifies
  ASVS 5.0.0 and the versioned PDF URL, matching its source-plan unit and ledger record.
- `edition/patterns/reading-ledger.v1.json:4545–4602` no longer contains the stale
  overview/no-verification-levels assertion in this record.
- Fresh retrieval of the recorded PDF returned HTTP 200, 514,062 bytes, with SHA-256
  `a2fa1bbe38f12cac86d3a0f0023327e9772201f65a7f741f282f5e785d268fc5`.
  This equals the ledger hash.
- The PDF contains verification-level definitions on printed page 12 and authorization
  requirements in V8 on printed pages 56–57. Its targeted passages agree with a full
  requirement-catalogue source, rather than an overview-only representation.

The RBAC card at chapter lines 208 onward already names the full PDF. Its citation is
consistent after this change. Broader shared-card fan-out is addressed separately below.

### R2-02 — Addressed by reproducible canonical article hashing

Evidence:

- `edition/patterns/reading-ledger.v1.json:5364–5403` identifies the extraction method
  and records this canonical-text SHA-256:
  `aa3be8892206c03c58a52f97a163a7f6dd23e30a3715ccdd88c062cba5cc75dc`.
- `scripts/source_content_hash.py:14–66` extracts the selected article text,
  normalizes whitespace, and hashes its UTF-8 encoding.
- Running the committed script against the public URL returned the exact recorded hash.
- Running the same script against a separately fetched local HTML representation returned
  that same hash. Both commands exited 0.
- The extracted text has 9,191 characters and contains all ten ledger-listed headings,
  from “Before you begin” through “What's next”. The article text includes the bounded
  pause/drain/verify/switch sequence.

An independent BeautifulSoup extraction of the article produced the same sequence of
whitespace-separated tokens. Its initial string comparison differed only in whitespace;
that is not a substantive extraction discrepancy.

Fresh raw HTML SHA-256 was
`f56586d14d43716bc884af53684cc7a541fd8ee03b55cb9b85259eaf23ab0f76`.
It is now correctly distinct from the ledger's canonical-text hash domain. The script's
SHA-256 is recorded in the machine-readable manifest below.

The canonical digest establishes equality of the extracted representation at retrieval,
not an immutable upstream revision, proof of past reading or product-behavior validation.

### R2-03 — Addressed

`research/sufficient-pilot-540/manifest.json:92,146,303,362` now says partial for dark
launching, RBAC, controlled cutover and parallel run. All six manifest current-coverage
fields match owner units; owner technical coverage agrees with the registry. All checked
source-unit fields also match the source plan.

The updated pilot validator checks these cross-artifact fields at
`scripts/validate_sufficient_pilot.py:35–45,88–90`. Its focused stale-source-URL test passes.
This verifies the exercised guard, not every possible stale-field scenario.

### R2-04 — Addressed

`book/volumes/v11-pattern-atlas/c11-security-operations/README.md:244–251` now names:

1. Istio identity.
2. Identity and certificate management.
3. Authentication.
4. Mutual TLS authentication.
5. Secure naming.
6. Peer authentication.
7. Authorization.
8. Authorization policies.

All eight are actual headings in the freshly retrieved public page. Their passages
support the bounded identity, rotation, mTLS and policy subjects named by the card.
The card retains its explicit synthetic limits for certificate revocation, trust-root
bootstrapping, key storage and lifetime policy. It continues to label the source as
unmeasured official documentation. This closes the unexplained-eight-heading finding.

## Remaining finding

### R3-01 — Shared ASVS citation fan-out remains incomplete

Severity: **non-blocking for the six rejected pilot entries**.
Affected cards outside the pilot: Zero Trust Architecture, Least Privilege,
Multitenant Isolation. This is a citation-consistency observation, not a sufficiency
verdict for those cards.

Exact repository-relative file:
`book/volumes/v11-pattern-atlas/c11-security-operations/README.md`.
Locations: lines 143–147, 176–180 and 311–315, each card's Sources paragraph.

All three still cite `read.batch6-asvs.2026-10-21` while describing fourteen headings
and an overview page without verification-requirement/level headings. That read record
now identifies the 120-page ASVS 5.0.0 PDF with V1–V17 and appendices. The freshly
retrieved PDF contains both requirement material and verification levels.

These stale paragraphs predate this round; they were observed while checking the shared
card file. Their persistence prevents a claim that the shared ASVS correction has been
propagated everywhere, as required by
`governance/SUFFICIENT-COVERAGE.md:61–66`. The six-entry pilot's ASVS binding is repaired.

Required action: align these three source notes with the actual PDF record and their
bounded source passages, or give the overview a separate source/read identity. Do not
reuse the PDF record to represent an overview-only read. Refresh affected hashes and
metadata after changing the shared file.

There are no new blocking findings within the requested six-entry remediation scope.

## Public sources actually opened

- [Spanner cutover](https://docs.cloud.google.com/spanner/docs/mysql-perform-cutover):
  HTTP 200; fresh raw HTML saved outside the repository; article and ten headings checked;
  canonical digest reproduced online and offline.
- [ASVS 5.0.0 PDF](https://github.com/OWASP/ASVS/raw/v5.0.0/5.0/OWASP_Application_Security_Verification_Standard_5.0.0_en.pdf):
  HTTP 200 after redirect to the same tagged file on raw.githubusercontent.com;
  hash matched; extracted text and targeted passages inspected.
- [Istio Security](https://istio.io/latest/docs/concepts/security/):
  HTTP 200; 158,607 bytes; eight named headings and passages inspected.
  Fresh raw SHA-256:
  `0291fb8211b0215a91fe1c2bf389db7b3cdb6fffd57605f13fb4e6b402eb66e4`.
  This capture hash records this retrieval; it does not assert equality with an older
  ledger representation of the mutable page.

Only public sources were used. Other unchanged external sources were not reopened.

## Checks actually run

All validators and tests ran in the isolated tracked snapshot:
`/tmp/tycho-540-sufficient-r3-7482e650/tree`.
It was exported from the pinned review HEAD and given a copied Git database. No validator
was run with the original repository as its output directory.

`PY` below denotes the existing review virtual environment's Python executable:
`/Users/rbaranov/Documents/Codex/2026-10-26/human-reviewer-human-review-private-tmp/work/venv/bin/python`.

| Command from isolated tree | Exit |
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
| `PY -B scripts/source_content_hash.py SPANNER_URL` | 0 |
| `PY -B scripts/source_content_hash.py LOCAL_HTML --file` | 0 |
| `PY -B -m unittest discover -s tests -p test_tycho_source_content_hash.py` | 0 |

`SPANNER_URL` is the exact public Spanner URL linked above.
`LOCAL_HTML` is `/tmp/tycho-540-sufficient-r3-7482e650/spanner.html`.
The pilot test command ran two tests; the hash-script test command ran one. All passed.
All eight validators passed; delivery evidence still reports three existing open gaps.
A passing validator does not detect or excuse the remaining semantic citation mismatch.

Other executed checks: pinned `git rev-parse`, `git status --short`, targeted `git diff`
and `git log`, JSON cross-artifact enumeration, twelve owner/card SHA-256 comparisons,
prior-report SHA-256, three public HTTPS retrievals, local HTML extraction, and
`pdftotext -layout` on the fresh ASVS PDF. All completed successfully. No required
in-scope command was unavailable. The handoff names no exact validator command list;
the eight validators retain the prior round's selection, plus the two focused test files.

No full test suite, broader promotion/acceptance program audit or CI was run.

## Limits, unchanged state and authority

This is a focused delta review. All six remain rejected and blocked in the manifest,
and no promotion record exists. Their unchanged partial technical dimensions retain
the prior technical rejections. Decision passes here do not establish technical
sufficiency or authorize promotion.

Hash reproduction proves equality of captured representations under the stated method.
It does not prove exhaustive source reading, implementation correctness, production
behavior, benchmark results or the semantic support of every unchanged sentence.
No fresh source used here was unavailable. The canonical hash method was inspected and
exercised for this Spanner representation, not certified for arbitrary websites.

The original checkout remains untouched. Final HEAD/status and file-integrity comparison
are recorded in the review manifest. No edits, commits, PRs or configuration changes were
made inside `/Users/rbaranov/Projects/tycho`.

This report grants no owner acceptance, CI status, merge permission or sufficient
coverage. `sufficient: 0`.

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
  "timestamp": "2026-10-27T01:12:00+01:00",
  "repository": "/Users/rbaranov/Projects/tycho",
  "review_head": "7482e650e0628e6d62096cdc50ede9519c4175d3",
  "prior_review_head": "55649c3a2541e81a5672cf887f1d45853e10823e",
  "remediation_commit": "eea4d89169a320a685567fbd7cc13305fb0b48ca",
  "handoff_commit": "a891d95efba8833b1260b679e792dced6433883b",
  "prior_report_sha256": "3997c55722125ca28477b4a0e07feb57437710ed334708595187effb1ded5278",
  "verdict": "pass-with-findings",
  "verdict_scope": "focused R2 residual remediation; six promotion rejections retained",
  "ai_review": "performed",
  "sufficient": 0,
  "counts": {
    "pilot_entries": 6,
    "rejected": 6,
    "blocked": 6,
    "owner_card_hash_checks": 12,
    "matches": 12,
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
    "R2-01",
    "R2-02",
    "R2-03",
    "R2-04"
  ],
  "dispositions": {
    "R2-01": "addressed for pilot; other cards have R3-01",
    "R2-02": "addressed",
    "R2-03": "addressed",
    "R2-04": "addressed"
  },
  "remaining_findings": [
    {
      "id": "R3-01",
      "severity": "non-blocking",
      "affected_cards": [
        "Zero Trust Architecture",
        "Least Privilege",
        "Multitenant Isolation"
      ]
    }
  ],
  "technical_verdicts": {
    "tycho.pattern.workload-identity-mtls": "reject",
    "tycho.pattern.dark-launching-shadow-traffic": "reject",
    "tycho.pattern.rbac-abac": "reject",
    "tycho.pattern.federated-identity": "reject",
    "tycho.pattern.controlled-cutover": "reject",
    "tycho.pattern.parallel-run": "reject"
  },
  "decision_verdicts": {
    "tycho.pattern.workload-identity-mtls": "pass",
    "tycho.pattern.dark-launching-shadow-traffic": "pass",
    "tycho.pattern.rbac-abac": "pass",
    "tycho.pattern.federated-identity": "pass",
    "tycho.pattern.controlled-cutover": "pass",
    "tycho.pattern.parallel-run": "pass"
  },
  "spanner_canonical_sha256": "aa3be8892206c03c58a52f97a163a7f6dd23e30a3715ccdd88c062cba5cc75dc",
  "hash_script_sha256": "94845a511b39f7f4f508fc9ed2b3316b08d77e603f12b2e55cf97e2efca9919f",
  "check_results": [
    {
      "command": [
        "PY",
        "-B",
        "scripts/validate_sufficient_pilot.py"
      ],
      "exit_status": 0
    },
    {
      "command": [
        "PY",
        "-B",
        "scripts/validate_sufficient_promotions.py"
      ],
      "exit_status": 0
    },
    {
      "command": [
        "PY",
        "-B",
        "scripts/validate_pattern_owner_units.py"
      ],
      "exit_status": 0
    },
    {
      "command": [
        "PY",
        "-B",
        "scripts/validate_pattern_registry.py"
      ],
      "exit_status": 0
    },
    {
      "command": [
        "PY",
        "-B",
        "scripts/validate_pattern_sources.py"
      ],
      "exit_status": 0
    },
    {
      "command": [
        "PY",
        "-B",
        "scripts/validate_pattern_cards.py"
      ],
      "exit_status": 0
    },
    {
      "command": [
        "PY",
        "-B",
        "scripts/validate_delivery_evidence.py"
      ],
      "exit_status": 0
    },
    {
      "command": [
        "PY",
        "-B",
        "scripts/check_boundary.py"
      ],
      "exit_status": 0
    },
    {
      "command": [
        "PY",
        "-B",
        "-m",
        "unittest",
        "discover",
        "-s",
        "tests",
        "-p",
        "test_tycho_sufficient_pilot.py"
      ],
      "exit_status": 0
    },
    {
      "command": [
        "PY",
        "-B",
        "scripts/source_content_hash.py",
        "https://docs.cloud.google.com/spanner/docs/mysql-perform-cutover"
      ],
      "exit_status": 0
    },
    {
      "command": [
        "PY",
        "-B",
        "scripts/source_content_hash.py",
        "/tmp/tycho-540-sufficient-r3-7482e650/spanner.html",
        "--file"
      ],
      "exit_status": 0
    },
    {
      "command": [
        "PY",
        "-B",
        "-m",
        "unittest",
        "discover",
        "-s",
        "tests",
        "-p",
        "test_tycho_source_content_hash.py"
      ],
      "exit_status": 0
    }
  ],
  "integrity": {
    "repository_unchanged": true,
    "files_checked": 1993,
    "head": "7482e650e0628e6d62096cdc50ede9519c4175d3",
    "status": "?? deliverables/\n",
    "asvs_pdf_pages": 120,
    "canonical_independent_tokens_equal": true,
    "canonical_chars": 9191,
    "canonical_sha256": "aa3be8892206c03c58a52f97a163a7f6dd23e30a3715ccdd88c062cba5cc75dc",
    "hash_script_sha256": "94845a511b39f7f4f508fc9ed2b3316b08d77e603f12b2e55cf97e2efca9919f"
  },
  "limits": [
    "Partial delta review, no complete 155-unit reading",
    "Other three ASVS cards assessed only for source-note consistency",
    "Three fresh public sources; unchanged sources not re-opened",
    "No general hash-tool certification or full test suite",
    "No owner acceptance, CI or merge permission"
  ]
}
```
