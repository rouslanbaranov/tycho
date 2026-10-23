# Read-only MCP stdio adapter — local candidate

> Issue [#57](https://github.com/rouslanbaranov/tycho/issues/57), E09-02, M5.
> 2026-10-23. **Status:** local implementation, offline tests and a one-off
> official-SDK 2.3.0 smoke; not merged, not independently reviewed, not a
> pinned-dependency conformance matrix and not a hosted service. No
> authentication or deployment is claimed.

## Scope and non-goals

[scripts/mcp_server.py](../scripts/mcp_server.py) is a stdlib-only MCP adapter
over the snapshot-bound section index and the draft pattern registry. It
exposes bounded retrieval, pattern lookup and registered evidence; it does not
generate answers, rank with vectors, reformulate queries, fetch sources,
rebuild indexes or rewrite the book.

The adapter is deliberately separate from the canonical stores:

- [section_search.py](../scripts/section_search.py) owns search, section
  reads and snapshot refusal;
- [section_evidence.py](../scripts/section_evidence.py) owns registered
  evidence resolution;
- [section_fts_index.py](../scripts/section_fts_index.py) owns the published
  SQLite section snapshot;
- [registry.v1.json](../edition/patterns/registry.v1.json) owns pattern
  identity, family, coverage and owner citations;
- [card-batches.v1.json](../edition/patterns/card-batches.v1.json) supplies
  optional card and ledger references;
- the MCP module only validates protocol messages, tool arguments and
  response envelopes.

The book and its frontmatter remain canonical. The adapter never exposes an
absolute filesystem path, a caller-chosen file path outside `book/`, a URL
fetch or an executable operation.

## Protocol behavior

### Modern 2026-07-28

The adapter follows the public
[2026-07-28 specification](https://modelcontextprotocol.io/specification/2026-07-28):

- every modern request carries `_meta` with
  `io.modelcontextprotocol/protocolVersion` and
  `io.modelcontextprotocol/clientCapabilities`;
- `server/discover` is implemented and returns supported versions,
  capabilities, server identity, `ttlMs`, `cacheScope` and instructions;
- `tools/list` returns a deterministic tool set with `ttlMs` and
  `cacheScope`;
- `tools/call` returns `resultType: "complete"`, `content`,
  `structuredContent` and `isError`;
- an unsupported version returns error code `-32022`
  (`UnsupportedProtocolVersion`) with `supported` and `requested`;
- `ping`, `initialize` and `notifications/initialized` are not modern
  methods.

The stdio binding uses newline-delimited JSON-RPC over standard input and
output, with diagnostics reserved for standard error. See the
[stdio binding](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/stdio)
and [versioning rules](https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning).

### Legacy 2025-11-25

A bounded legacy path exists for clients that still open with `initialize`:

- only protocol version `2025-11-25` is accepted;
- `initialize` returns `protocolVersion`, `capabilities.tools`, `serverInfo`
  and `instructions`;
- `notifications/initialized` is accepted and ignored;
- `ping` returns an empty result after initialization;
- `tools/list` and `tools/call` use the legacy result shape without
  `resultType` or server `_meta`.

Unknown methods return `-32601`; malformed parameters return `-32602`; parse
failures return `-32700`. Batch requests are rejected explicitly.

## Tools

| Tool | Operation | Hard bounds |
|---|---|---|
| `tycho_describe` | Collection, snapshot, pattern registry and limits | No book text |
| `tycho_search` | Lexical BM25 over indexed sections | `limit` 1–20 |
| `tycho_read` | Bounded read from one section | 1–5,000 codepoints |
| `tycho_page` | Bounded page body plus section map | 1–5,000 codepoints |
| `tycho_patterns` | Draft pattern summaries and registry snapshot | `limit` 1–50 |
| `tycho_pattern` | One draft pattern, family, card and owner citation | One ID |
| `tycho_evidence` | Registered document/claim/source metadata | One ID only |

`tycho_search` returns the best section per document by default;
`all_sections=true` returns every matching section. The response carries the
snapshot; each result carries `path`, `anchor`, `title`, `snippet`, `excerpt`,
`score`, `score_kind`, `section_key`, `section_id`, `citation` and
`matched_terms`. `anchor` and `snippet` are aliases for `section_id` and
`excerpt`.

`tycho_read` returns a codepoint range, `next_offset`, `truncated`,
`document_char_start`, `document_char_end`, the document hash and the
citation. `tycho_page` returns the page body slice, a section map with body
offsets, the page-level citation and the same continuation fields.

All successful tool results also carry `content_trust:
"untrusted-evidence"`. Book text is data; the adapter does not follow
instructions found inside it.

## Pattern registry

`tycho_patterns` and `tycho_pattern` read the draft pattern registry and,
when available, the card batches. They return identity, family, coverage,
confidence, review status, source-unit identifiers and owner citations. They
do not return book text; use `tycho_page` or `tycho_read` for the owner
section.

The registry snapshot is the SHA-256 of the exact registry bytes. A caller can
pin it with `registry_snapshot_id`; a mismatch returns
`snapshot-mismatch`. The tools report the registry status and a derived
coverage summary. They do not infer that `partial-bounded` entries are
sufficient, and they do not claim independent review.

Pattern owner citations use `tycho.markdown-heading-anchor.v1`, not
`tycho.section-key.v2`. An anchor can point at an H3 that is not a citable
section. Use `tycho_page` with the owner path and then choose a section from
its map for `tycho_read`.

## Query logging

Search queries are **not logged by default**. The operator can opt in with
`--query-log PATH`; the server then appends one JSON object per successful
search call to that file. Each record contains the schema version, UTC
timestamp, tool name, query, filters, limit, section snapshot, status,
returned count and at most 20 result citations.

The log deliberately excludes client identity, request IDs, IP addresses,
read/page/evidence calls and book text. Query text can contain user data, so
enabling the log is a privacy decision: the operator must control the path,
access, retention and deletion. The adapter does not rotate, redact or encrypt
the file. A write failure is reported as `query_log: "not-available"` and does
not break retrieval.

The path must be a regular file outside the canonical stores (`book/`,
`generated/`, `edition/`, `sources/`, `schemas/`, `authoring/`, `tests/` and
`scripts/`). Symlinks, directories and special files are refused; a refused
path is reported as `query_log: "not-available"` and writes nothing.

## Answerability

No calibrated abstention or answer-correctness metric exists yet. The adapter
therefore does not claim that a result is answerable:

| Field | Value | Meaning |
|---|---|---|
| `answerable` | `null` | Not assessed |
| `no_confident_answer` | `true` or `null` | True only for zero lexical results |
| `state` | `no-results` or `not-assessed` | Retrieval state |
| `confident` | `false` | No confidence model |
| `basis` | `zero-results` or `uncalibrated` | Why the state was set |

Zero results mean only that this index, snapshot, filter and query returned
no match. They are not proof that the corpus lacks the concept. A separate
refusal metric and independent labels remain future work.

## Security and trust boundary

- **Read-only book access:** the process opens the published SQLite index in
  read-only mode and never writes the book, metadata, index or evidence. The
  optional query log is the only write path; it is disabled by default and must
  be a regular file outside the canonical stores.
- **No arbitrary paths:** `tycho_page` accepts only a relative canonical
  `book/...md` path without `..`, backslashes, absolute prefixes or empty
  segments. The page must be present in the snapshot; the file must stay
  under `book/`, must not be a symlink and must match its recorded SHA-256.
- **No SSRF or shell:** there is no URL fetch, subprocess, shell, embedding,
  model call or outbound network operation.
- **Snapshot refusal:** a stale route snapshot, a changed document, a
  caller-supplied `snapshot_id` mismatch or a pattern-registry mismatch
  returns `snapshot-mismatch` rather than mixing states.
- **Content is not authority:** returned text is tagged untrusted evidence
  and must not be treated as instructions or permission.
- **Local transport only:** stdio has no authentication, TLS, rate limiting
  or tenancy. It is not a hosted endpoint and must not be exposed as one.

Input limits are enforced before retrieval: search `limit` 1–20, pattern
`limit` 1–50, read/page budget 1–5,000 codepoints, pattern `offset` at most
10,000, query 2,000 characters, path 500 characters and message size
1,000,000 characters.

## Tests

Run the offline suite from the repository root:

~~~sh
.venv/bin/python -m unittest discover -s tests \
  -p 'test_tycho_mcp_server.py' -v
~~~

The suite builds a synthetic three-page book with strict metadata, publishes
a real FTS5 section index, writes a synthetic pattern registry and card batch,
and exercises 23 cases: modern discovery and cache fields, legacy
initialization, tool listing, search citations, zero results, bounded section
reads, page maps, traversal refusal, retrieval and registry snapshot pinning,
unsupported versions, missing metadata, unknown tools and arguments, ping era
behavior, pattern filters and pagination, pattern card lookup, pattern
citation scheme, query-log opt-in, failure and protected-path refusal,
malformed-message handling, evidence argument validation, collection counts
and a stdio subprocess roundtrip.

A separate manual smoke runs the same server through the official SDK
2.3.0 client in modern and legacy modes; it is recorded in
[the SDK smoke note](MCP-SDK-SMOKE_2026-10-23.md) and is not part of the
offline suite.

## Measured local evidence — 2026-10-23

| Observation | Value |
|---|---|
| Indexed documents and sections | 423 and 2,753 |
| Route snapshot | `4232fead4319c7161ca23ea9994ffbf9fced055e48246539071b3485c1a84279` |
| Section snapshot | `4d2391ee8ba90de07d29ea3554061bea299df6661498f394471ab694a800ec0a` |
| Pattern registry | 145 entries, all `partial-bounded`, 0 `sufficient` |
| Pattern registry snapshot | `d63969cf650d7acb174fa1570085b8854c0a28c8470a7918ecd4523470d73814` |
| Offline tests | 23 passed, about 0.5–1.5 s |
| `server/discover` | about 0.03 s |
| `tycho_search` warm local run | about 1.0–1.2 s end to end |
| `tycho_read` warm local run | about 1.0 s end to end |
| `tycho_page` warm local run | about 1.0 s end to end |
| `tycho_describe` warm local run | about 1.2 s end to end |
| `tycho_patterns` warm local run | about 0.03 s |
| `tycho_pattern` warm local run | under 0.01 s |
| Official SDK smoke | `mcp` 2.3.0, modern and legacy roundtrip |
| Runtime | Python 3.9.6, SQLite 3.54.0 |

Timings are single-machine observations that include interpreter startup and
route-snapshot revalidation where applicable. They are not a latency SLO, a
capacity forecast or a client benchmark.

## Limitations and next gates

- The official SDK was exercised only as a one-off smoke: `mcp` 2.3.0
  under Python 3.15.0 in a temporary environment. It is not a repository
  dependency pin, not a full client matrix and not an SDK conformance
  suite.
- No hosted Streamable HTTP endpoint, authentication, authorization,
  observability, load test or deployment exists.
- Query logging is opt-in, requires a regular non-symlink file outside the
  canonical stores, and has no rotation, retention enforcement, redaction or
  encryption. It must not be enabled without an explicit privacy decision.
- No calibrated answerability or refusal metric exists; the five
  unanswerable qrels items still have no refusal score.
- Pattern lookup reads a draft registry. All 145 entries remain
  `partial-bounded`; 0 are sufficient, and this adapter does not change
  that. Decision-method lookup remains outside this slice.
- The open #51 evidence-quality measurement remains separate. Evidence
  resolution works locally, but it is not a completed #51 acceptance.
- No independent review, human acceptance, CI result or merge is claimed.

## Sources

- MCP [Discovery](https://modelcontextprotocol.io/specification/2026-07-28/server/discover)
- MCP [Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools)
- MCP [stdio](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/stdio)
- MCP [Versioning](https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning)
- MCP [Changelog](https://modelcontextprotocol.io/specification/2026-07-28/changelog)
- Tycho [protocol and transport decision](MCP-PROTOCOL-COMPATIBILITY.md)
- Tycho [section search contract](SECTION-SEARCH.md)
- Tycho [pattern registry](../edition/patterns/registry.v1.json)
- [MCP Python SDK](https://py.sdk.modelcontextprotocol.io/get-started/installation/)
