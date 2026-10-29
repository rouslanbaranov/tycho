# Owner acceptance of AI labels — 2026-10-29

Status: **owner-accepted evidence for AI labels**. This is not human review,
independent review, CI or a sufficient-coverage claim.

## Owner instruction

The owner authorized using AI-adjudicated labels as owner-accepted evidence and
asked to treat them as human review. The first part is recorded. The second part
is **not** recorded: no human reviewer or human evidence exists, so the artifact
remains `human_review: not-claimed`.

## Scope

- `evaluation/corpus-qrels.v3.json`
- `evaluation/section-qrels.v3.json`
- derived uncertainty, split and guarded analyses
- production default decision

## Record

- `owner_acceptance: granted`
- `acceptance_basis: AI-adjudicated labels`
- `human_review: not-claimed`
- `independent_review: not-claimed`
- `ci: not-run`
- `sufficient: 0`

## Decision

- BM25 remains the default.
- Best mode remains optional; its v3 gain is not significant and is
  prior-accepted-page driven.
- Section rerank remains optional; guarded all/v2 gains are significant, but
  phase3 page top-1 still regresses .895 -> .842.
- V12 guards remain in force.

## Limits

- This acceptance does not convert AI labels into human judgments.
- It does not establish production quality or sufficient coverage.
- Phase3 needs a guard or dedicated review before a default section-rerank
  switch.
