# V12 search integration — 2026-10-29

Issue: #598. Parent: #587.

## Purpose

Close the search-layer gap left by the V12 volume: expose V12 artifacts and their pattern
links through the section search layer without editing any existing card, book page or
promotion record.

## What changed

- Section FTS schema v5 adds nullable `artifact_type` and `volume` columns and the
  `section_patterns` table.
- Facets are derived from `generated/v12-index.v1.json` and
  `edition/v12/reverse-index.v1.json`; the canonical route index remains authoritative.
- `section_search.search` accepts `artifact_type`, `volume` and `pattern_ids` filters and
  returns channel facets plus a bounded `artifacts` lookup.
- `section_search.py v12` returns model, scenario, run and decision contracts for a
  pattern, type or volume without requiring a text query.
- `tycho_search` exposes the same filters. `tycho_pattern` now includes a
  `v12_artifacts` block for the selected pattern.
- `evaluation/v12-simulation-qrels.v1.json` adds 15 author-labelled V12 queries;
  `validate_corpus_qrels.py --scope v12` validates them against the full route.
- `evaluate_corpus_qrels.py --volume v12` evaluates the V12 qrels against the section
  index.

## Agent route

1. Resolve the architecture question to a `tycho.pattern.*` ID.
2. Call `section_search.py v12 --pattern-id tycho.pattern.timeout` or the
   `tycho_pattern` tool. The result lists linked models, scenarios, runs and decisions.
3. Read `model.dynamics.kind` to choose the simulation family: stock-flow,
   discrete-event or hybrid.
4. Read the scenario contract, then the run provenance and decision constraints.
5. Reproduce with `scripts/v12_engine.py`; verify with
   `scripts/validate_v12.py`.

Example:

~~~text
python3 scripts/section_search.py v12 --pattern-id tycho.pattern.timeout
python3 scripts/section_search.py search --query "queue timeout" \
  --volume v12 --pattern-id tycho.pattern.timeout --include-artifacts
~~~

## Limits

- The lookup is a provenance table, not a semantic graph.
- V12 models are uncalibrated; search discovery does not validate a model.
- V12 qrels are author-labelled, not independently adjudicated.
- The SQLite index stays gitignored and must be rebuilt locally.
- No existing pattern is promoted, demoted or re-reviewed.

## Local verification

- Full unit suite: 714 tests, OK.
- V12 qrels: 15 items, 28 accepted pages; page hit@5 0.929, MRR 0.598 (author-labelled).
- V12, edition, source, metadata, AI-review and Phase 4 validators: pass.
- Section index: 498 documents, 3,075 sections, 268 V12 sections.
- Mermaid diagrams are unchanged; the checker was not rerun in this fresh clone because
  its Node dependencies are not installed.
