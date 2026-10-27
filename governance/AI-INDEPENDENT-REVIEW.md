# Independent AI review

Status: mandatory. Effective: 2026-10-26. Supersedes the human-review gate for all
future reviews and acceptance decisions.

## Purpose

Tycho accepts an independent review performed by a different AI harness from a different
vendor as the independent review gate. A review by the authoring agent, the same harness,
the same vendor or a subagent of the authoring session does not satisfy this rule.

Permitted examples when the authoring session is DeepSeek Harness:

- ChatGPT (OpenAI) in a fresh session;
- Claude Code (Anthropic) in a fresh checkout;
- another external harness from a third vendor, used read-only.

A DeepSeek `reviewer` subagent does **not** qualify. The reviewer must be a separate
product and a separate vendor from the authoring harness.

## Reviewer discovery and selection

The authoring agent must locate a qualifying local CLI before preparing a hand-off.

1. Search `PATH` and installed application bundles for CLIs from vendors other than the
   authoring vendor, for example `codex` (OpenAI), `claude` (Anthropic) or `gemini`
   (Google). Verify that the CLI starts, is authenticated and offers a non-interactive
   read-only mode.
2. If more than one qualifying CLI is available, ask the user which CLI to use. Do not
   choose silently.
3. If the selected CLI supports model selection, obtain its available model list, give
   that list to the user, and ask which model to use. Record the chosen model. Once the
   user has selected a CLI and/or model, remember the choice for the current session and
   reuse it for later reviews; ask again only if it becomes unavailable, fails, or the
   user requests a change.
4. If no qualifying CLI is available, use a manual hand-off through the user: provide the
   exact self-contained prompt and receive the reviewer's raw report. If the user cannot
   supply a qualifying review, mark the gate blocked; never substitute a same-vendor
   model, a subagent or a self-review.
5. Record the discovered CLI, selection source (the user), vendor, model, version,
   session and read-only invocation in the review record.

## Independence requirements

1. The reviewer must not see the author's conversation, conclusions or desired verdict.
2. Start from the exact HEAD and content commit supplied in the hand-off, in a read-only
   checkout or read-only repository access.
3. The reviewer must not write to the repository, change configuration, commit, open a PR
   or modify canonical artifacts.
4. Use public sources only. Never supply restricted, employer-specific or private material.
5. For each source, pin the URL, revision or content hash and access date.
6. Review one bounded scope per run. Large scopes are split into non-overlapping batches.

## Hand-off prompt

When the owner asks for a hand-off document for an external AI reviewer, the hand-off must
contain an exact, copy-paste prompt for that reviewer. A summary, checklist or link alone is
not sufficient. The prompt must be self-contained: reviewer role, repository path, pinned
commit, read-only rule, scope, required checks, source rules, report schema and the rule
that the reviewer must not claim owner acceptance, CI or sufficient coverage.

## Required record

Every review must leave a report containing:

- review harness and vendor;
- model name and version, when exposed;
- session or run identifier;
- review timestamp;
- repository path, branch, HEAD and content commit;
- exact scope: artifact paths, page hashes, source URLs and hashes;
- the prompt or instruction set used, or a stable link to it;
- verdict (`pass`, `pass-with-findings` or `reject`);
- findings by severity with exact paths and evidence;
- limits, unresolved questions and any source unavailable;
- a statement that the review is not owner acceptance or sufficient coverage by itself.

Store the raw report in the repository for every completed review. The reviewer remains
read-only; the author saves the reviewer output verbatim. If the reviewer wrote to the
repository, stop, quarantine the changes and treat the review as contaminated.

## Preservation of reports

Every completed external AI review must be preserved in the repository.

- Directory: `authoring/ai-reviews/`.
- File name: `YYYY-MM-DD-<scope-slug>-<reviewer-slug>.md`.
- Content: the reviewer output verbatim, including identity fields, scope, evidence,
  findings, verdict and limits. Do not edit the report. Add corrections as a separate
  addendum file.
- Hash: record the SHA-256 of the saved file in `authoring/ai-reviews/README.md`.
- Index: add one row per review with date, reviewer harness/vendor, scope, verdict, path
  and SHA-256.
- The hand-off or acceptance record must link the saved report. A review with no saved
  report is not a completed review.

If a report contains restricted or private material, do not commit it; quarantine it and
follow the contamination procedure. Public-source reviews only.

## What the verdict means

- `pass`: no blocking finding in the reviewed scope.
- `pass-with-findings`: actionable findings remain; the owner decides whether to remediate
  before acceptance.
- `reject`: blocking finding; the artifact cannot be accepted in the reviewed state.

An AI review pass satisfies the independent review gate. It does **not** by itself grant
owner acceptance, sufficient coverage, CI status or permission to merge. Those remain
separate decisions unless the owner explicitly records otherwise.

## Failure and unavailability

If no qualifying CLI is available, prepare a manual hand-off through the user using the
same prompt, scope and report requirements. If the user cannot provide a qualifying review,
the gate is `blocked`. It is never waived, replaced by self-review or satisfied by the
authoring agent's own harness. Do not claim a review that did not run.

## Historical records

Human-review records created before 2026-10-26 remain historical evidence. They are not
retroactively invalidated, and they are not a template for new reviews. See
[the owner acceptance record](../authoring/OWNER-ACCEPTANCE-2026-10-26.md) and
[the historical human review](../authoring/HUMAN-REVIEW_2026-10-21.md).
