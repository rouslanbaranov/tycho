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

## Independence requirements

1. The reviewer must not see the author's conversation, conclusions or desired verdict.
2. Start from the exact HEAD and content commit supplied in the hand-off, in a read-only
   checkout or read-only repository access.
3. The reviewer must not write to the repository, change configuration, commit, open a PR
   or modify canonical artifacts.
4. Use public sources only. Never supply restricted, employer-specific or private material.
5. For each source, pin the URL, revision or content hash and access date.
6. Review one bounded scope per run. Large scopes are split into non-overlapping batches.

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

Store the raw report in the repository when the owner asks for it. If the reviewer wrote
to the repository, stop, quarantine the changes and treat the review as contaminated.

## What the verdict means

- `pass`: no blocking finding in the reviewed scope.
- `pass-with-findings`: actionable findings remain; the owner decides whether to remediate
  before acceptance.
- `reject`: blocking finding; the artifact cannot be accepted in the reviewed state.

An AI review pass satisfies the independent review gate. It does **not** by itself grant
owner acceptance, sufficient coverage, CI status or permission to merge. Those remain
separate decisions unless the owner explicitly records otherwise.

## Failure and unavailability

If no qualifying external reviewer is available, the gate is `blocked`. It is never waived,
replaced by self-review or satisfied by the authoring agent's own harness. Do not claim a
review that did not run.

## Historical records

Human-review records created before 2026-10-26 remain historical evidence. They are not
retroactively invalidated, and they are not a template for new reviews. See
[the owner acceptance record](../authoring/OWNER-ACCEPTANCE-2026-10-26.md) and
[the historical human review](../authoring/HUMAN-REVIEW_2026-10-21.md).
