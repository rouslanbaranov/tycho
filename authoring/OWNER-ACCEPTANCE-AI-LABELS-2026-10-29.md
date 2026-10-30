# Owner acceptance of AI labels — 2026-10-29

Status: **owner-accepted evidence for AI labels**. This is not human review,
independent review, CI or a sufficient-coverage claim.

Update 2026-10-29: the owner approved the MCP production default
`section_rerank=true, section_rerank_margin=0.15`, with no separate
section/phase3 review and no production-client benchmark. See
[MCP-MARGIN-DEFAULT-2026-10-29.md](MCP-MARGIN-DEFAULT-2026-10-29.md).

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

- MCP default was margin-gated at .15; qrels v4 reversed it to BM25 on
  2026-10-30. Margin gate remains opt-in.
- Best mode remains optional; its v3 gain is not significant and is
  prior-accepted-page driven.
- Global section rerank remains optional; phase3 page top-1 regresses .895 ->
  .842 without the margin gate.
- V12 guards remain in force.

## Limits

- This acceptance does not convert AI labels into human judgments.
- It does not establish production quality or sufficient coverage.
- Phase3 needs a guard or dedicated review before a default section-rerank
  switch.
