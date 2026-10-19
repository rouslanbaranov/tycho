# Unified knowledge validation — E04-06

> Tycho [issue #37](https://github.com/rouslanbaranov/tycho/issues/37), 2026-10-19. A read-only orchestration command for *implemented* knowledge checks, **not** a full semantic, security, copyright, search-quality or human review certificate. Do not infer a CI result from a submitted PR.

## Implementation

[validate_knowledge.py](../scripts/validate_knowledge.py) checks the canonical versioned source/inventory formats and composes these existing read-only validators in one fail-fast operation:

1. Source register validation and source catalogue freshness.
2. Pinned public Git repository lock and catalogue freshness.
3. Typed claim/provenance structure and admission-boundary checks.
4. Public document observation ledger and research checkpoint freshness.
5. Strict metadata JSON Schema fixture validation (requires the already declared external Python `jsonschema` dependency).
6. Existing book navigation/link validation.
7. Validated route index freshness when its generated artifact exists. A missing required route index is explicitly returned as `incomplete`. Curated graph validation is **not a Tycho requirement**.

The validator does **not** run `checkout`, `acquire`, `build`, `frontmatter apply`, embedding generation, chapter enrichment or a scheduled GitHub workflow. The new command itself doesn't create any generated artifacts.

## Invocation and exit states

~~~sh
python3 scripts/validate_knowledge.py --mode available --json
python3 scripts/validate_knowledge.py --mode strict --json
python3 -m unittest discover -s tests -p 'test_tycho_validate_knowledge.py' -v
~~~

- **`passed`, exit 0:** all required checks and the generated routing index passed; proves ONLY mechanical validation across their explicitly bounded scopes.
- **`incomplete`, exit 2:** required checker outcomes have not failed, but a capability is not implemented or an expected generated index has not been built. This is *not* CI green or readiness to close a milestone.
- **`failed`, exit 1:** actual checker failure, mismatched contract version, missing scripts/dependency, malformed JSON or mismatched/stale generated outputs. Stop immediately; preserve offending evidence for diagnosis.

`--mode strict` fails up front when the required routing-index gate is missing. Absence of graph tooling never blocks acceptance. `--mode available` runs implemented checks but still produces nonzero `incomplete` rather than silently waiving missing coverage.

The CLI also checks currently declared source contract versions and JSON Schema dialects. To adopt future versions, update the declared contract in a dedicated reviewed migration and test the old/new compatibility; do not modify expected constants merely to silence a mismatch.

## Milestone-only CI and handoff

Tycho's existing GitHub Actions policy triggers validation **only on milestone closure**. This PR adds no push/PR trigger, workflow rerun or new automatic milestone-closing action. The command can be used *locally* in an authorized checkout during review; the former optional graph hook is retired from this Tycho validator; code-relationship experiments may have independent validation but cannot become an implicit release prerequisite. An exit code or metadata/date field cannot establish independent technical fact-checking.

When a check fails, record the exact checker name, schema/source/index revision, error, relevant original source and owner, and a bounded corrective issue. Never auto-reset a pinned Git checkout or regenerate whole-book content. A stale route index is repaired by deliberate index rebuild only after checking its metadata and canonical source changes, not by re-enriching chapters. A curated graph is explicitly **out of Tycho scope**; its absence is neither a failed gate nor a reason to generate graph artifacts.

## Evidence and implementation limits

Seven isolated tests exercise current version contracts, deliberate drift, optional hook detection, strict-vs-available semantics, fail-fast behavior and forbidden modes using temporary fixtures and mocked subprocess results. They do not prove that a complete real checkout passed every validator. Source claim support, code-symbol existence, independent domain review, network access rights, licensing and performance evaluations remain separate, substantive quality obligations.

**Status:** bounded orchestration and tests supplied; full M1–M8 knowledge delivery and milestone acceptance are not implied.
