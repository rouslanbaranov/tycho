# Bounded public research workflow and immutable checkpoints

> E03-05 [issue #31](https://github.com/rouslanbaranov/tycho/issues/31). This is an **implemented local event and checkpoint model**, not a source-verification oracle or AI agent that has read every entry in the public inventory. It integrates exact source/claim IDs with chapter-level research tasks without modifying the global source register when a section is inspected.

## What is actually implemented

- [research-events.json](research-events.json) is an append-preserving stream of public bounded slice events. It has concrete examples for landing/entry observation, named section read, contested interpretation and a source-access blocker. Its `events` list is authoritative; there is **no mutable `currentStatus` field** which can erase history.
- [research_checkpoints.py](../scripts/research_checkpoints.py) enforces stable event and slice IDs, registered public source ID, exact HTTP publisher host, named technical section for section-read claims, source admission and valid claim IDs from [claim-references.json](claim-references.json). It refuses to promote an entry-page inspection or a blocked JEP to verified reading.
- [RESEARCH-CHECKPOINTS.md](RESEARCH-CHECKPOINTS.md) is a deterministic human route to the latest event of each slice. It is derived from event order and can be regenerated and compared; history lives only in JSON.
- [test_tycho_research_checkpoints.py](../tests/test_tycho_research_checkpoints.py) contains ten local tests of source/claim admission, entry-vs-section distinction, blockers, contradiction notes, deterministic report and append preservation.

## Reading scope is more precise than inventory discovery

| Research event | What it proves | What it does not prove |
|---|---|---|
| `entry-inspected` | Title, landing page or summary was encountered with declared source version and date | A material technical claim, performance result or cited section was independently verified |
| `section-inspected` | An operator explicitly asserts having read the named section; can become **ready for review** | Automated tool cannot prove reading occurred, the assertion is correct, or independent review was obtained |
| `dispute-recorded` | A claim/inference was challenged against an admitted section | This alone does not establish that two primary sources contradict each other |
| `blocked` | Exact obstacle and an actionable next step recorded without hiding the history | Source has been inspected or technical behavior established |
| `checkpoint` | A bounded research action/hold state and next action were recorded | Production implementation or human approval |

An offline validation PASS is a **structural state**. Only exact inspected passages, actual experiment reports and named reviewers establish evidence quality. A source catalogue may correctly say `landing-or-abstract-inspected` while one **specific** research slice records a named section reading: do not silently broaden that result to the whole publication.

## CLI, deterministic current state and historical preservation

~~~sh
python3 scripts/research_checkpoints.py validate
python3 scripts/research_checkpoints.py status
python3 scripts/research_checkpoints.py check
python3 -m unittest discover -s tests -p 'test_tycho_research_checkpoints.py' -v

# Only when source/read review actually changes; never invent evidence:
python3 scripts/research_checkpoints.py append --event-json path/to/new-event.json
python3 scripts/research_checkpoints.py regenerate
~~~

The event supplied to `append` must be fully specified, source/claim-valid and in date order within its slice. The CLI refuses a duplicate event ID or stale file write and preserves earlier events. Append/rebuild are **explicit** actions; they do not fetch sources, run enrichments, reset clones, update an index, revalidate the entire book, or activate CI.

## Actual research slices included

1. **Idempotency** — first landing then specific sections of [AWS Builders' Library](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/), including semantic equivalence; latest state is `ready-for-review`, NOT human-approved or independently reproduced.
2. **HTTP scope challenge** — the overbroad inference that method-level idempotence guarantees global external effects is kept `blocked` / disputed, and the exact RFC 9110 §9.2.2 is identified. This is a contradiction between a proposed inference and source scope, **not** between AWS and RFC.
3. **JEP 491** — canonical full text not retrievable (HTTP 403), kept `blocked`, with explicit official-companion research task; no invented source passages.

All three slices reference existing public source IDs and claim IDs. The optional [access and licensing ledger](ACCESS-LICENSING-RESOLUTION.md) explains why source access and lawful third-party reuse must not be conflated.

## Checkpoint and re-review discipline

For any material disputed claim or refreshed source, append an event with exact section/snapshot, `finding`, `claim_ids`, `next_action` and a status. If a digest/revision changes in the [document observations workflow, pending PR #155](https://github.com/rouslanbaranov/tycho/pull/155), treat it as a candidate for targeted re-review, **not** a reason to reconstruct old research records or regenerate unrelated pages. The latest event may move from ready-for-review back to blocked when contrary evidence or missing access emerges; the earlier source reading remains historically visible.

**Not delivered here:** a deployed source crawler, provenance truth engine, automated expert sign-off, semantic graph/index, full Markdown/frontmatter schema, or a means to inspect private employer documents. No M9 case-study files or lock are modified.
