# V12 artifact qrels v1

Reviewer: OpenAI Codex / model exposed by harness. Date: 2026-10-30.

- Content HEAD: `448a65574c3cd9f86d8ddf02963308f431c11756`
- Section index snapshot: `e7496a664281afd4a1fff483f68780107a9541e3771a44741322751322dfe8fa`
- Questions: 30; target artifact types: model 7, scenario 8, run 8, decision 7.
- Candidate judgments: 150 total, five per question; model 25, scenario 62, run 49, decision 14.
- Grades: 30 direct (2), 39 partial (1), 81 not relevant (0). The pools contain 25 distinct artifact IDs, of which 21 are direct answers for at least one question.
- Validation: `python3 scripts/validate_v12_artifact_qrels.py --file evaluation/v12-artifact-qrels.v1.json` passed. The final HEAD and snapshot were checked again after construction.

Questions were newly worded to request a model, scenario, run, or decision for a specific information need. Candidate IDs came from the V12 index. Adjudication used index metadata and the relevant model scopes and equations, scenario input fields, run result and provenance fields, or decision context, constraints and candidate references. Related artifacts of a different type provide partial context; contrasting artifacts supply distractors. The `target_type` field records the requested type for each query. No v3/v4 page qrels or current search rankings were consulted, and decision outcome fields were not used to choose labels.

The pools are not exhaustive, and a single AI reviewer made the judgments without an independent disagreement assessment. The index has only three models and two decision artifacts, so several questions share a direct artifact. V12 inputs and outputs are synthetic; these judgments do not establish production validity. Passing the validator checks internal structure and references, not the correctness or completeness of relevance labels. No question was rejected during construction.

**AI-adjudicated only; not human review, CI, owner acceptance, or sufficient coverage.**
