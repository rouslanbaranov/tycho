# V12 artifact-level qrels — handoff

Status: handoff only. No artifact-level qrels exist.

## Goal

Create a separate 30-query artifact-level set. Do not mix it with page or section
qrels.

Candidate/relevance unit: `generated/v12-index.v1.json` artifact IDs
(`model`, `scenario`, `run`, `decision`). Book pages are not candidates here.

## Schema

`evaluation/v12-artifact-qrels.v1.json`:

```json
{
  "schema_version": 1,
  "status": "ai-adjudicated-not-human",
  "snapshot": "<section index snapshot>",
  "content_commit": "<git HEAD>",
  "query_count": 30,
  "items": [
    {
      "id": "V12A-001",
      "question": "Fresh artifact-selection question",
      "grades": {
        "tycho.model.example": 2,
        "tycho.run.example": 1,
        "tycho.scenario.example": 0
      },
      "accepted": ["tycho.model.example", "tycho.run.example"],
      "direct": ["tycho.model.example"]
    }
  ],
  "limits": "AI-adjudicated only; not human review, CI or sufficient coverage."
}
```

## Requirements

- Exactly 30 fresh questions, IDs `V12A-001`–`V12A-030`.
- 4–10 artifact candidates per query.
- Grades 0/1/2; at least one direct grade 2.
- accepted = grade >= 1; direct = grade 2.
- Cover models, scenarios, runs and decisions; no more than 10 queries from one
  artifact type.
- Use artifact metadata/questions/summaries; do not copy page/section qrels.
- Do not read v3/v4 page qrels or current search rankings.
- Do not edit book, atlas, edition, generated indexes or production config.
- Record HEAD and snapshot.

## Validate

```sh
python3 scripts/validate_v12_artifact_qrels.py \
  --file evaluation/v12-artifact-qrels.v1.json
```

## Limits

This is a new artifact retrieval set; page/section qrels cannot substitute.
AI-adjudicated labels are not human review, CI, owner acceptance or sufficient
coverage.
