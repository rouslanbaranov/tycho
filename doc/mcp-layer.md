# MCP layer

The MCP layer exposes Tycho as a read-only, snapshot-bound knowledge service.
It is not a chat agent and does not produce final answers. Its job is to return
bounded, attributable sections, evidence and pattern metadata to a calling
client.

The implementation is under [`mcp/`](../mcp/). The human onboarding entry
point is [INTEGRATION.md](../INTEGRATION.md).

## Tool surface

The current server exposes 11 tools:

| Tool | Purpose |
|---|---|
| `tycho_describe` | Snapshot, counts, limits, catalog and tool list |
| `tycho_search` | Ranked bounded search over sections |
| `tycho_outline` | Topic or path-prefix reading plan |
| `tycho_page` | Page section map, frontmatter and bounded body |
| `tycho_read` | Bounded read of a known section |
| `tycho_context` | Question-driven bundle of cited sections |
| `tycho_compare` | Extractive comparison of two to five options |
| `tycho_batch` | Up to eight bounded reads or evidence resolutions |
| `tycho_patterns` | Draft pattern-family and entry discovery |
| `tycho_pattern` | One draft pattern entry |
| `tycho_evidence` | Registered evidence metadata, not source text |

Each tool has an input and output JSON Schema under
[`mcp/schemas/`](../mcp/schemas/). The schemas are the machine-readable contract;
this table is only a summary.

## Transport model

The server supports:

- **stdio** for harness sessions and local clients;
- **HTTP** for a local or trusted network endpoint.

The HTTP implementation targets the stateless `2026-07-28` MCP revision.
Legacy clients that require the older handshake should use stdio.

Typical endpoints are:

| Endpoint | Purpose |
|---|---|
| `/mcp` | MCP JSON-RPC transport |
| `/health` | Liveness |
| `/ready` | Readiness and snapshot state |

The HTTP server uses a bearer token. The token is generated into a local file by
the control script, with restrictive permissions. The token is not a substitute
for network controls.

## Starting the server

From the repository root:

```sh
python3 mcp/mcp_server.py --root .
python3 mcp/mcp_http_server.py --root . --port 8000
```

For the managed HTTP path:

```sh
python3 integration/mcp_server_ctl.py start --port 8765
python3 integration/mcp_server_ctl.py status --port 8765
python3 integration/mcp_server_ctl.py stop
```

The verifier starts its own server instance and checks both transports:

```sh
python3 integration/verify.py --http-port 8765
```

The expected check count is six. A skipped HTTP check must be reported as
skipped, not as a pass.

## Read-only guarantees

- No tool edits the book, metadata, index or repository.
- No tool fetches arbitrary external URLs.
- No tool executes user-provided code.
- Paths must resolve inside the indexed corpus.
- Reads are bounded by explicit character and result limits.
- Snapshot mismatches fail closed.

The model can still produce a misleading synthesis; the server's read-only
property is not a correctness guarantee.

## Evidence semantics

The MCP server returns evidence, not instructions. Returned text is untrusted
input to the calling agent. The caller must:

- preserve the snapshot ID;
- cite `path#section_id`;
- state missing evidence;
- avoid treating a zero-hit result as proof of absence;
- avoid treating pattern metadata as a recommendation.

Pattern endpoints currently expose draft registry metadata. They do not claim
that every pattern is independently reviewed.

## Authentication and exposure

Current HTTP authentication is a shared bearer token. There is:

- no OAuth;
- no per-client authorization;
- no rate limiting;
- no multi-tenant quota isolation;
- no public production SLA.

Run the HTTP server only on a trusted boundary and rotate the token if it is
exposed. A public deployment requires additional work.

## Tests

The MCP test suite has 123 test definitions across 10 files. It covers:

- protocol and schema contracts;
- stdio and HTTP behavior;
- search/read/page/outline/context/pattern tools;
- snapshot and index freshness;
- negative inputs and limits;
- client interoperability fixtures.

The general test strategy is in [Tests and coverage](tests-and-coverage.md).

## Limits

- The MCP layer is a local candidate, not a hardened production service.
- The default search is lexical; no semantic ranker is required.
- One snapshot is served at a time.
- No final answer, recommendation or decision is generated.
- No OAuth, per-client authorization or rate limiting is implemented.
- A passing verifier is not a security audit.
