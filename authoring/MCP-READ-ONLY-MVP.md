# Read-only MCP stdio adapter — local candidate

> Issue [#57](https://github.com/rouslanbaranov/tycho/issues/57), E09-02, M5.
> 2026-10-23. **Status:** local implementation and offline tests; not merged,
> not independently reviewed, not a pinned-SDK conformance run and not a
> hosted service. No live external client, authentication or deployment is
> claimed.

## Scope and non-goals

[scripts/mcp_server.py](../scripts/mcp_server.py) is a stdlib-only MCP adapter
over the existing snapshot-bound section index. It exposes bounded retrieval
and registered evidence; it does not generate answers, rank with vectors,
reformulate queries, fetch sources, rebuild indexes or write the book.

The adapter is deliberately separate from the retrieval core:

- [section_search.py](../scripts/section_search.py) owns search, section
  reads and snapshot refusal;
- [section_evidence.py](../scripts/section_evidence.py) owns registered
  evidence resolution;
- [section_fts_index.py](../scripts/section_fts_index.py) owns the published
  SQLite snapshot;
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
| `tycho_describe` | Collection identity, snapshot, counts and limits | No book text |
| `tycho_search` | Lexical BM25 over indexed sections | `limit` 1–20 |
| `tycho_read` | Bounded read from one section | 1–5,000 codepoints |
| `tycho_page` | Bounded page body plus section map | 1–5,000 codepoints |
| `tycho_evidence` | Registered document/claim/source metadata | One ID only |

`tycho_search` returns the best section per document by default;
`all_sections=true` returns every matching section. The response carries the
snapshot; each result carries `path`, `anchor`, `title`, `snippet`, `excerpt`,
`score`, `score_kind`, `section_key`, `section_id`, `citation` and
`matched_terms`.
`anchor` and `snippet` are aliases for `section_id` and `excerpt`.

`tycho_read` returns a codepoint range, `next_offset`, `truncated`,
`document_char_start`, `document_char_end`, the document hash and the
citation. `tycho_page` returns the page body slice, a section map with body
offsets, the page-level citation and the same continuation fields.

All successful tool results also carry `content_trust:
"untrusted-evidence"`. Book text is data; the adapter does not follow
instructions found inside it.

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

- **Read-only:** the process opens the published SQLite index in read-only
  mode and never writes the book, metadata, index or evidence.
- **No arbitrary paths:** `tycho_page` accepts only a relative canonical
  `book/...md` path without `..`, backslashes, absolute prefixes or empty
  segments. The page must be present in the snapshot; the file must stay
  under `book/`, must not be a symlink and must match its recorded SHA-256.
- **No SSRF or shell:** there is no URL fetch, subprocess, shell, write,
  embedding, model call or outbound network operation.
- **Snapshot refusal:** a stale route snapshot, a changed document or a
  caller-supplied `snapshot_id` mismatch returns `snapshot-mismatch` rather
  than mixing bytes from different book states.
- **Content is not authority:** returned text is tagged untrusted evidence
  and must not be treated as instructions or permission.
- **Local transport only:** stdio has no authentication, TLS, rate limiting
  or tenancy. It is not a hosted endpoint and must not be exposed as one.

Input limits are enforced before retrieval: search `limit` 1–20, read/page
budget 1–5,000 codepoints, query 2,000 characters, path 500 characters and
message size 1,000,000 characters.

## Tests

Run the offline suite from the repository root:

~~~sh
.venv/bin/python -m unittest discover -s tests \
  -p 'test_tycho_mcp_server.py' -v
~~~

The suite builds a synthetic three-page book with strict metadata, publishes
a real FTS5 section index and exercises 16 cases: modern discovery and cache
fields, legacy initialization, tool listing, search citations, zero results,
bounded section reads, page maps, traversal refusal, snapshot pinning,
unsupported versions, missing metadata, unknown tools and arguments, ping era
behavior, evidence argument validation, collection counts and a stdio
subprocess roundtrip.

## Measured local evidence — 2026-10-23

| Observation | Value |
|---|---|
| Indexed documents and sections | 423 and 2,753 |
| Route snapshot | `4232fead4319c7161ca23ea9994ffbf9fced055e48246539071b3485c1a84279` |
| Section snapshot | `4d2391ee8ba90de07d29ea3554061bea299df6661498f394471ab694a800ec0a` |
| Offline tests | 16 passed, about 0.4 s |
| `server/discover` | about 0.03 s |
| `tycho_search` warm local run | about 1.0–1.2 s end to end |
| `tycho_read` warm local run | about 1.0 s end to end |
| `tycho_page` warm local run | about 1.0 s end to end |
| `tycho_describe` warm local run | about 1.2 s end to end |
| Runtime | Python 3.9.6, SQLite 3.54.0 |

Timings are single-machine observations that include interpreter startup and
route-snapshot revalidation. They are not a latency SLO, a capacity forecast
or a client benchmark.

## Limitations and next gates

- No official MCP SDK is installed or pinned. This adapter is a direct
  stdlib implementation of the documented wire shape, not an SDK
  conformance run. A pinned SDK and an independent client version matrix
  remain required before claiming interoperability.
- No hosted Streamable HTTP endpoint, authentication, authorization,
  observability, load test or deployment exists.
- No query logging exists yet; the future opt-in design must state privacy,
  retention and redaction rules before collecting real queries.
- No calibrated answerability or refusal metric exists; the five
  unanswerable qrels items still have no refusal score.
- Pattern and decision-method lookup is not in this adapter; it belongs to
  the bounded #58 work.
- The open #51 evidence-quality measurement remains separate. Evidence
  resolution works locally, but it is not a completed #51 acceptance.
- No independent review, human acceptance, CI result or merge is claimed.
  Pattern sufficiency remains 0; this adapter does not change it.

## Sources

- MCP [Discovery](https://modelcontextprotocol.io/specification/2026-07-28/server/discover)
- MCP [Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools)
- MCP [stdio](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/stdio)
- MCP [Versioning](https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning)
- MCP [Changelog](https://modelcontextprotocol.io/specification/2026-07-28/changelog)
- Tycho [protocol and transport decision](MCP-PROTOCOL-COMPATIBILITY.md)
- Tycho [section search contract](SECTION-SEARCH.md)
