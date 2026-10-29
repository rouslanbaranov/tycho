# Top-1 agent audit — 2026-10-29

Status: **session subagent audit**, not human review, independent review, CI or
owner acceptance.

## Scope

The 20 items in
[TOP1-ADJUDICATION-PACKET-2026-10-29.md](TOP1-ADJUDICATION-PACKET-2026-10-29.md)
were read at HEAD 94244ba4. Every top-1 and accepted path resolved. The
reviewer judged only whether the returned section answers its query; it did not
assess technical truth or coverage sufficiency.

## Counts

| Split | Valid | Invalid | Uncertain |
|---|---:|---:|---:|
| v2 | 7 | 5 | 0 |
| phase3 | 1 | 3 | 0 |
| V12 | 1 | 3 | 0 |
| **Total** | **9** | **11** | **0** |

Nine of the 20 strict top-1 misses were judged defensible answers outside the
accepted set. Strict hit@1 therefore undercounts useful top-1 results on this
sample; the sample is not a replacement for full adjudication.

## Patterns

- **Adjacent section, same page:** Q010, T1-A01, Q606. This is a section
  granularity/indexing issue, not a topic miss.
- **Landing, routing or capability section:** Q014, Q015, Q601, Q602. The
  section names the topic but does not answer the mechanism question.
- **Wrong topic:** Q001, Q016, T1-A04, T2-A05.
- The remaining items are valid but often summary-level.

## Decision

- Do not edit qrels from this audit.
- Do not claim production top-1 quality from 9/20.
- Keep the adjudication packet as the owner-facing form; this audit is a
  separate diagnostic.
- The adjacent-section pattern supports section-level reranking/H3 work, not a
  larger embedding model alone.

## Limits

- One reviewer subagent from the same vendor; not independent review.
- 20 items, selected as strict misses; not a random sample of all queries.
- Reasons are summaries; the full reviewer response is in the session record.
- No tests were run by the reviewer; no files were written by it.
