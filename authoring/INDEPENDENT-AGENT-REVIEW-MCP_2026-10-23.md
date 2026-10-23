# Independent agent review — MCP read-only MVP

> Issue [#57](https://github.com/rouslanbaranov/tycho/issues/57), E09-02, M5.
> Reviewer preset: `reviewer` (DeepSeek Harness). Two independent child
> batches: `b11c723b-a42b-4491-95f8-12c9ecf8bca9` (code, protocol, security)
> and `18c9b948-d7b8-4b6c-89ef-497d168e09f8` (documentation and evidence).
> Review completed by 2026-10-23T15:34Z.
>
> **Status:** independent agent audit only. It is not named human review,
> owner acceptance, CI, sufficiency, deployment approval or permission to
> merge. Reviewers wrote no repository files; `git status` stayed unchanged.
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

**M2 — medium: legacy era detection.**
Era detection keyed on `_meta` presence and rejected legacy progress-token
metadata. Modern era now requires
`_meta.io.modelcontextprotocol/protocolVersion`; legacy requests with
progress metadata remain legacy. A legacy progress-token test was added.

**M3 — medium: failure-path coverage.**
Integrity, notification, envelope and evidence paths were untested. The suite
now has 30 tests covering page hash/reconstruction/symlink refusal,
notification silence, modern envelopes, legacy progress metadata, registry
failure, cursor/version rejection and the evidence wrapper.

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
The tool description now states the local JSONL side effect when query logging
is enabled.

**L5 — low: minor protocol details.**
Notifications are ignored before parameter validation; missing log parents are
refused; legacy version errors remain explicit `-32602` with
supported/requested data and are tested.

## Documentation findings

**D1 — medium: source-unit overclaim.**
`tycho_patterns` was said to return source-unit identifiers but omitted
them. Summaries now include `source_units`; tests assert the field.

**D2 — medium: absolute path in an error payload.**
A missing-registry error exposed the checkout path. The error is now
path-free; a test asserts the checkout path is absent.

**D3 — medium: 419 versus 423 pages.**
STATE now labels 423 as the post-#228 current count and 419 as the earlier cut.
The book and edition landing counts were not rewritten because they are outside
this MCP slice and changing an indexed book page would invalidate the pinned
section index and qrels. The residual landing-count inconsistency is recorded
as a pre-existing editorial and index task.

**D4 — low: README and STATE disagreed on PR #222.**
GitHub confirms #222 merged on 2026-10-20; README now says merged.

**D5 — low: symlink wording.**
The record now says the log file itself must not be a symlink, parent symlinks
are resolved, and the resolved location must be outside the checkout.

## Post-review verification

| Item | Value |
|---|---|
| Correction commit | `39bbaa28d88bdea86cd8e8683990ff0b01597535` |
| Server after correction | `cd89a36e4b4ae7bcb85b2ecb8d8f0ecfa3c00be1c8605a798582db73f104b296` |
| Focused MCP tests | 30 passed |
| Repository tests | 446 passed in the local pre-merge gate |
| SDK smoke | mcp 2.3.0, modern and legacy reruns passed |
| Boundary, line length, whitespace | passed |

The correction changed the code and tests after the reviewed revision. A
separate delta review is the remaining review step; this record does not
claim that delta review has already passed.

## Limits

- No named human review, owner acceptance, CI run, deployment, HTTP transport,
  authorization, concurrency, cancellation, load test or full client matrix.
- The SDK smoke is one machine, one SDK version and one process lifecycle; its
  client makes no assertions and is not a conformance suite.
- The full repository suite was run locally by the authoring session, not by
  CI; the reviewers ran the focused MCP suite.
- No independent verification of the 419/423 landing-page count was performed
  beyond the current index and the recorded #228 split.
- Pattern coverage remains 145 entries, all `partial-bounded`, 0
  `sufficient`. This review does not change that.
- This record is a post-review synthesis by the authoring session, not a
  second independent report.
