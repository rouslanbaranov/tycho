# External-agent benchmark prompt v3-concise

You are an independent external agent. Answer one question from evidence only.
This is prompt v3 with a strict concise answer target after the length-controlled
A/B showed that detailed v3 answers win but cost too many words.

## 0. Onboarding (mandatory)

Run:

```bash
.venv/bin/python mcp/agent_session_cli.py describe
```

Read metadata.layers, tool descriptions, pagination/errors and examples. Canonical
layers are book, atlas and modeling-and-simulation; v11/v12 are aliases.

## 1. Facet matrix

Decompose the question into 3-6 decision-relevant facets. Track:

| Facet | Query formulations | Evidence |
|---|---|---|
| ... | ... | section_key |

Do not stop at two facets when the question has independent parts.

## 2. Search broadly

For every facet:

1. Use 2-3 distinct formulations (exact terms, synonyms, layer aliases,
   conceptual query).
2. Use outline when structure is unclear; follow next_actions and related_ids.
3. Search the relevant layer; use more than one layer for cross-layer questions.
4. Continue until every facet has evidence and two consecutive searches add no
   new evidence. There is no fixed maximum number of calls.
5. Do not cite a snippet instead of the section you need.

## 3. Evidence ledger

For each core claim record claim -> section_key -> short quote/note, and mark
observed evidence versus inference. Every substantive claim needs a section key.
Preserve gaps; do not invent.

## 4. Answer shape: concise but complete

Target 150-220 words. Include:

1. Direct answer.
2. Mechanism and justification.
3. Boundaries, trade-offs, alternatives and failure modes that change the
   decision.
4. Compact evidence map.
5. Unknowns and confidence.

Do not pad, repeat the question or list every citation as prose. Keep the full
evidence array in JSON so detail remains auditable.

## 5. CLI

```bash
.venv/bin/python mcp/agent_session_cli.py describe
.venv/bin/python mcp/agent_session_cli.py search "query" --limit 5 --log LOG
.venv/bin/python mcp/agent_session_cli.py page "book/..." --max-chars 5000 --log LOG
.venv/bin/python mcp/agent_session_cli.py read "section_key" --max-chars 5000 --log LOG
.venv/bin/python mcp/agent_session_cli.py outline "topic" --limit 4 --log LOG
```

Default budget is 4500; maximum 6000. Continue with offset=next_offset when
truncated. Search has no offset; refine the query.

## 6. Output

```json
{
  "task_id": "Q000",
  "answer": "150-220 words with direct answer, mechanism, boundaries and evidence map",
  "citations": ["section_key"],
  "evidence": [{"claim": "...", "section_key": "...", "note": "..."}],
  "abstain": false,
  "token_usage": {"total": null, "estimated": true}
}
```

Do not read corpus/qrels/labels/answers/rankings/reports. Do not edit
book/atlas/indexes. Do not commit.
