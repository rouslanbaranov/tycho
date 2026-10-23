# Independent agent review — MCP read-only MVP

> Issue [#57](https://github.com/rouslanbaranov/tycho/issues/57), E09-02, M5.
> Reviewer preset: `reviewer` (DeepSeek Harness). Three independent child
> batches: `b11c723b-a42b-4491-95f8-12c9ecf8bca9` (code, protocol, security),
> `18c9b948-d7b8-4b6c-89ef-497d168e09f8` (documentation and evidence), and
> `71cd778e-1e50-4b9e-8c2f-460dce380530` (focused delta).
> Initial reviews completed by 2026-10-23T15:34Z; delta by 15:41Z.
>
> **Status:** independent agent audit only. It is not named human review,
> owner acceptance, CI, sufficiency, deployment approval or permission to
> merge. Reviewers wrote no repository files; the final `git status` was
> clean except the unrelated untracked `deliverables/`.
> `human_review: not-performed`; `sufficient: 0`.

## Reviewed revision

| Item | Value |
|---|---|
| Review HEAD | `fae2043bbc4c3c19a064b482c1fb8b0acab91889` |
| Code commit | `7b9f49322d478053d905c858308427fa4c0bcc1a` |
| Base | `origin/main` `5018fda9b30456271fb80cf8a38a67f45380d5d3` |
| Server SHA-256 | `79879040fca80e24c003cbef3ea4d1fb0dd48359b5521e2d9ba7be5dd62686e2` |
| Tests SHA-256 | `98047b019f318819026f2ed9697ee5b57490ea3e1b3fc5cc9db4263f911a7ed1` |
| Smoke client SHA-256 | `c929086d2f2576271df876a5cc16c54eea6912d70369d37c75a3a55dd1c13cc3` |
| SDK wheel SHA-256 | `dd0c44c089d16453e8ae31a3877a0054d7a2314caaa81f5e0541b9b1734b2377` |

Both reviewers reproduced the 23-test suite, the section and registry
snapshots, the SDK versions and the modern/legacy smoke outputs. The working
tree had only the unrelated untracked `deliverables/` before and after both
audits.

## Verdicts

| Batch | Verdict | Findings |
|---|---|---|
| Code, protocol and security | ACCEPT-WITH-FINDINGS | 3 medium, 5 low |
| Documentation and evidence | ACCEPT-WITH-FINDINGS | 3 medium, 2 low |
| Focused delta | ACCEPT-WITH-FINDINGS | residuals M1, L4, D3; no regressions |

No blocker or high severity finding was raised. The code review supported the
bounded local acceptance case only if the medium findings were fixed or
explicitly accepted. The documentation review supported the factual core but
not issue acceptance as written.

## Code and protocol findings

**M1 — medium: query-log boundary.**
The denylist did not cover root files, `.git` or other control paths, and
hard links plus check/open races remained. The resolved log path must now be
outside the checkout; final symlinks, non-regular files and multiply-linked
files are refused; writes use `O_NOFOLLOW` and verify the opened descriptor.
Tests cover root files, `.git`, directories, symlinks, hard links and FIFOs.
Residual LOW: the parent-directory symlink swap between the predicate and
`os.open` is not covered; the write remains outside the checkout by design.

**M2 — medium: legacy era detection.**
Era detection keyed on `_meta` presence and rejected legacy progress-token
metadata. Modern era now requires
`_meta.io.modelcontextprotocol/protocolVersion`; legacy requests with
progress metadata remain legacy. A legacy progress-token test was added.

**M3 — medium: failure-path coverage.**
Integrity, notification, envelope and evidence paths were untested. The suite
now has 30 tests covering page hash/reconstruction/symlink refusal,
notification silence, modern envelopes, legacy progress metadata, registry
failure, cursor/version rejection and the evidence wrapper. After the delta,
test-only assertions added root-level log refusal, oversized-message handling,
page-offset refusal, evidence snapshot mismatch and legacy version data; the
server code did not change.

**L1 — low: error text could expose absolute paths.**
Raw `str(exc)` is replaced with path-free client messages for retrieval,
page and pattern failures. A missing-registry test asserts the checkout path
is absent.

**L2 — low: inconsistent sufficiency fields.**
`tycho_patterns` now returns `sufficient_entries` and
`registry_status`; `tycho_pattern` returns boolean `sufficient` and
`coverage_state`.

**L3 — low: past-end pattern offset.**
A past-end offset returned `no-results` although matches existed. The status
is now `ok` when the filtered total is non-zero; the test covers an empty
past-end page.

**L4 — low: query-log side effect versus `readOnlyHint`.**
The tool description and MVP security note now state the local JSONL side
effect when query logging is enabled. The annotation remains
`readOnlyHint: true` because the domain is read-only by default; the
conditional write is a residual LOW limitation.

**L5 — low: minor protocol details.**
Notifications are ignored before parameter validation; missing log parents are
refused; legacy version errors remain explicit `-32602` with
supported/requested data; the test now asserts that data.

## Documentation findings

**D1 — medium: source-unit overclaim.**
`tycho_patterns` was said to return source-unit identifiers but omitted
them. Summaries now include `source_units`; tests assert the field.

**D2 — medium: absolute path in an error payload.**
A missing-registry error exposed the checkout path. The error is now
path-free; a test asserts the checkout path is absent.

**D3 — medium: 419 versus 423 pages.**
STATE now explains the 419-page cut, the 423-page current tree and the four
pages added by the #228 deep-source splits. The book and edition landings still
record 419; they were not rewritten because they are outside this MCP slice and
changing an indexed book page would invalidate the pinned section index and
qrels. The residual is tracked under #228.

**D4 — low: README and STATE disagreed on PR #222.**
GitHub confirms #222 merged on 2026-10-20; README now says merged.

**D5 — low: symlink wording.**
The record now says the log file itself must not be a symlink, parent symlinks
are resolved, and the resolved location must be outside the checkout.

## Corrections and delta review

| Item | Value |
|---|---|
| Correction commit | `39bbaa28d88bdea86cd8e8683990ff0b01597535` |
| Final test and wording commit | `1a63d4351d7d1a8ad466a47a53c9f82ff9ba3077` |
| Server after correction | `cd89a36e4b4ae7bcb85b2ecb8d8f0ecfa3c00be1c8605a798582db73f104b296` |
| Tests after correction | `ffb7658a45c7ba2595250429cee1a8a6cfc7170884a3abceed2bcd6d45d631ec` |
| Focused MCP tests | 30 passed |
| Pre-merge tests | 446 methods; 467 total methods including non-premerge files |
| SDK smoke | mcp 2.3.0, modern and legacy reruns passed |
| Boundary and whitespace | passed |
| Line length | V11 checker passed; new and edited MCP docs checked locally |

The delta reviewed `87d85b5` and code commit `39bbaa2`. It found no
regressions and resolved M2, L1, L2, L3, D1, D2, D4 and D5. Residuals are M1
(parent-symlink race, LOW), L4 (`readOnlyHint`, LOW), and D3 (landing counts,
MEDIUM). Test-only coverage additions in `1a63d43` close the root, message,
page-offset, evidence and legacy-data gaps noted by the delta; they were not
separately re-reviewed.

## Limits

- No named human review, owner acceptance, CI run, deployment, HTTP transport,
  authorization, concurrency, cancellation, load test or full client matrix.
- The SDK smoke is one machine, one SDK version and one process lifecycle; its
  client makes no assertions and is not a conformance suite.
- The pre-merge subset (446 test methods) was run locally by the authoring
  session, not by CI; 467 total test methods exist. The reviewers ran the
  focused MCP suite.
- No independent verification of the 419/423 landing-page count was performed
  beyond the current index and the recorded #228 split.
- Pattern coverage remains 145 entries, all `partial-bounded`, 0
  `sufficient`. This review does not change that.
- This record is a post-review synthesis by the authoring session, not a
  second independent report.
