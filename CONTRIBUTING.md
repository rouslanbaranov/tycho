# Contributing to Tycho

Tycho is an independent, source-grounded system-design project. Contributions
are welcome when they preserve the repository's evidence, independence and
editorial rules.

## Before you start

Read these documents first:

- [AGENTS.md](AGENTS.md) — mandatory contributor rules.
- [Governance index](governance/README.md) and
  [independence and source admissibility](governance/INDEPENDENCE.md).
- [Authoring methodology](authoring/METHODOLOGY.md).
- [Current state and next action](authoring/STATE.md).

Use public sources only. Do not include restricted-origin material, private
data, proprietary code or unlicensed third-party assets. Synthetic examples must
be clearly labelled and must not be based on restricted systems.

## Pick a bounded task

Work from an executable GitHub issue with an `[E##-##]` title. Keep the change
within that issue's acceptance criteria.

Each issue has one primary development branch, created from `main`:

```text
feature/TYCHO-<issue-number>-<task-slug>
```

Use the issue number, not the epic code. Derive the slug from the issue title
after the `[E##-##]` prefix: lowercase ASCII words separated by single hyphens.
Do not mix unrelated issues in one branch.

## Local workflow

1. Create or reuse the issue branch.
2. Make one bounded change and update the relevant documentation, evidence and
   links.
3. Run targeted validators while editing. Save the full premerge run for the
   review-ready state of the batch.
4. Run the lexical boundary check:

   ```text
   python3 scripts/check_boundary.py
   ```

5. Before requesting merge, run:

   ```text
   python3 scripts/premerge_check.py \
     --branch <branch> \
     --issue-title '<exact GitHub issue title>'
   ```

   Record any command that could not run and why.

6. Commit with a focused message and open a pull request against `main`. Use
   `Refs #<issue-number>`; avoid automatic-closing keywords. Include the
   bounded scope, evidence, local checks and remaining limitations.

Do not claim that CI ran. The repository's single verification workflow runs
only when an intentionally closed milestone has no open issues.

## Content rules

- Write repository content in English.
- Keep every Markdown line at or below 100 characters.
- Cite public sources and keep claims within what those sources support.
- Use Mermaid for architecture, flow, sequence, state or recovery diagrams when
  they make the explanation clearer. Explain the diagram in prose.
- Keep one canonical owner for each explanation and derive indexes from
  metadata instead of duplicating them.
- Label synthetic versus documented behavior and state applicability limits.
- Do not copy prose, code, schemas, diagrams or examples from another source.

## Review and acceptance

Book-content and atlas-structure changes require an independent AI review under
[the AI review policy](governance/AI-INDEPENDENT-REVIEW.md). Tooling, tests,
generated indexes, workflow configuration, scripts and documentation do not
require that gate.

A review pass is not owner acceptance, CI status, sufficient coverage or
permission to merge. The owner decides whether to apply the verdict and when the
issue is complete.

## License

Repository contributions are distributed under the [MIT License](LICENSE).
Third-party sources remain subject to their own terms; see the
[source register](sources/register.json).
