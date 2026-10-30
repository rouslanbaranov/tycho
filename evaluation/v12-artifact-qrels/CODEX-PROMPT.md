# Codex prompt — V12 artifact qrels

Work only in the isolated clone:

```sh
cd ~/Projects/tycho-index-and-search
```

Read:

- `authoring/V12-ARTIFACT-QRELS-HANDOFF-2026-10-30.md`
- `generated/v12-index.v1.json` read-only.

Do not read v3/v4 page qrels, current search rankings or author conclusions.

## Task

Create `evaluation/v12-artifact-qrels.v1.json` with exactly 30 fresh
artifact-selection questions.

- IDs V12A-001–V12A-030.
- 4–10 artifact candidates per query from the V12 index.
- At least one direct grade 2.
- Cover model, scenario, run and decision artifacts; no type over 10 queries.
- Fresh wording; do not copy the artifact question strings verbatim.
- accepted = grade >=1; direct = grade 2.
- Record HEAD and section snapshot.

Do not edit book/atlas/edition/generated/production configuration. Do not merge
page or section qrels.

Validate:

```sh
python3 scripts/validate_v12_artifact_qrels.py \
  --file evaluation/v12-artifact-qrels.v1.json
```

Write `evaluation/v12-artifact-qrels/REPORT.md` with counts by artifact type,
candidate totals, method and limitations. State AI-adjudicated only; not human
review, CI, owner acceptance or sufficient coverage.
