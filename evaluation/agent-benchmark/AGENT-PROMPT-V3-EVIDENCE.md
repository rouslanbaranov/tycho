# External-agent benchmark prompt v3-evidence

You are an independent external agent. Answer one question from evidence only.
This is full v3 with no answer-length or claim-count cap, plus the v2 evidence
contract. Read this entire prompt before acting.

## 0. Onboarding (mandatory)

Run:

```bash
.venv/bin/python mcp/agent_session_cli.py describe
```

Read `metadata.layers`, tool descriptions, pagination/error rules and examples.
State which layers the question needs. Canonical layers are `book`, `atlas`
and `modeling-and-simulation`.

## 1. Facet matrix

Decompose the question into 3-6 decision-relevant facets. Write:

| Facet | Query formulations | Evidence |
|---|---|---|
| ... | ... | section_key |

Do not stop at 2-5 facets if the question has more independent parts.

## 2. Search broadly

For every facet:

1. Use 2-3 distinct formulations: exact terms, synonyms, layer aliases and a
   conceptual query.
2. Use `outline` when the structure is unclear.
3. Follow `next_actions`, `related_ids` and page section maps.
4. Search the relevant layer with
   `--volume book|atlas|modeling-and-simulation`. Atlas and modeling questions
   must use their own volume, not only book results.
5. Continue until every facet has evidence and two consecutive searches add no
   new evidence. There is no fixed call limit.
6. Never cite a snippet as a section; read the section you cite.

## 3. Evidence ledger (mandatory)

Before writing the answer, build a claim-to-evidence ledger. Every core claim
must have at least one evidence entry read through the CLI:

```json
{
  "claim_id": "C1",
  "text": "atomic answer claim",
  "evidence": [
    {
      "section_key": "tycho.page...#anchor",
      "quote": "verbatim fragment read from the section",
      "supports": "C1",
      "status": "observed"
    }
  ]
}
```

Rules:

- `status` is `observed` or `inference`; inference is not a source claim.
- `quote` is a real fragment, not a paraphrase.
- `supports` must equal the claim id.
- No claim without evidence. If evidence cannot be found, write an explicit
  unknown or abstain.
- No citation without a claim. No orphan citations.
- Do not use E1/E2 labels unless the same object also gives the section_key.

## 4. Answer JSON v2

Write exactly this shape:

```json
{
  "task_id": "Q250",
  "answer": "full v3 answer with facet matrix, mechanism, boundaries, evidence map and unknowns",
  "claims": [{"claim_id": "C1", "text": "...", "evidence": [{"section_key": "...", "quote": "...", "supports": "C1", "status": "observed"}]}],
  "citations": ["tycho.page...#anchor"],
  "missing_required_anchors": ["required key not found"],
  "abstain": false
}
```

- `citations` must equal the unique section keys in the evidence ledger.
- `missing_required_anchors` is computed honestly against the question's
  `required_evidence`; do not invent coverage.
- There is no word limit. Keep the full reasoning and all decision-relevant
  nuance.

## 5. Self-check before finishing

Run on your answer file:

```bash
.venv/bin/python scripts/validate_agent_answer.py ANSWER.json --corpus CORPUS.json
```

It must print `PASS` for the mechanical contract. Fix unresolved keys,
citations not present in evidence, claims without evidence or a wrong
missing-anchor list. A PASS does not prove semantic support; it proves the
contract is coherent.

## 6. CLI

```bash
.venv/bin/python mcp/agent_session_cli.py describe
.venv/bin/python mcp/agent_session_cli.py search "query" --limit 5 --volume atlas --log LOG
.venv/bin/python mcp/agent_session_cli.py page "book/..." --max-chars 5000 --log LOG
.venv/bin/python mcp/agent_session_cli.py read "section_key" --max-chars 5000 --log LOG
.venv/bin/python mcp/agent_session_cli.py outline "topic" --limit 4 --log LOG
```

Default budget is 4500; maximum 6000. Use `offset=next_offset` when truncated.

## 7. Honesty

Record unknowns, contradictions and unverified claims. Do not invent citations,
measurements, review, production observations or coverage. Missing evidence is
a result, not permission to guess.
