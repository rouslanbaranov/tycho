# Official MCP SDK client smoke — 2026-10-23

> Issue [#57](https://github.com/rouslanbaranov/tycho/issues/57), E09-02, M5.
> **Status:** one-off local client smoke, not CI, not a compatibility matrix,
> not a hosted endpoint and not independent review. It proves only that the
> exact files and versions below interoperated once on this machine.

## Environment

| Item | Value |
|---|---|
| Official SDK | `mcp==2.3.0` from PyPI |
| SDK wheel SHA-256 | `dd0c44c089d16453e8ae31a3877a0054d7a2314caaa81f5e0541b9b1734b2377` |
| Client interpreter | Python 3.15.0 in a temporary virtual environment |
| Server interpreter | Python 3.9.6 in the repository virtual environment |
| Transport | stdio, newline-delimited JSON-RPC |
| Repo HEAD at smoke | `87a34f7f62121930723656981e73641a81af8bd6` |
| Server file SHA-256 | `261626d49dd4e9ae5b65e498effc649069eff46c8eb3a7424e924f38366f1adf` |
| Smoke client SHA-256 | `c929086d2f2576271df876a5cc16c54eea6912d70369d37c75a3a55dd1c13cc3` |

The SDK was installed only in `/tmp/tycho-mcp-sdk-2.3.0`. It is not a
repository dependency, and no runtime package was added to the server
environment. The wheel hash above covers `mcp` itself; transitive
dependencies were not locked.

## Commands

~~~sh
/tmp/tycho-mcp-sdk-2.3.0/bin/python scripts/mcp_sdk_smoke.py \
  --server-python .venv/bin/python

/tmp/tycho-mcp-sdk-2.3.0/bin/python scripts/mcp_sdk_smoke.py \
  --server-python .venv/bin/python --mode legacy
~~~

[scripts/mcp_sdk_smoke.py](../scripts/mcp_sdk_smoke.py) starts the local server
over stdio and calls `tycho_search`, `tycho_page`, `tycho_patterns` and
`tycho_pattern`. It uses no hosted model or answer generator.

## Observed

| Observation | Modern run | Legacy run |
|---|---|---|
| Negotiated protocol | `2026-07-28` | `2025-11-25` |
| Server identity | `tycho-mcp` 0.1.0 | `tycho-mcp` 0.1.0 |
| Listed tools | 7 | 7 |
| Search status | `ok`, 2 results | `ok`, 2 results |
| Page status | `ok`, 80 chars | `ok`, 80 chars |
| Pattern list | `ok`, 145 total, 2 returned | `ok`, 145 total, 2 returned |
| Pattern lookup | Layered Architecture | Layered Architecture |
| Client exit | 0 | 0 |

The modern run exercised `server/discover` and per-request `_meta`. The
legacy run exercised `initialize` and the legacy tool result shape. Both
runs listed the same seven tool names and returned the same first search
citation for the same query.

## Limits

- This is one machine, one SDK version, one server revision and one process
  lifecycle. It is not a supported-client matrix or a conformance suite.
- Concurrency, cancellation, malformed-header behavior, HTTP transport,
  authentication, authorization, TLS, rate limiting, load and deployment were
  not exercised.
- The SDK's transitive dependencies are not pinned or hashed here, and the
  temporary environment is not part of the repository.
- No independent reviewer or human acceptance has examined this smoke.
- A future SDK release may change client behavior; re-run the commands against
  the exact versions when the server or SDK changes.

## Sources

- [MCP Python SDK installation](https://py.sdk.modelcontextprotocol.io/get-started/installation/)
- [MCP Python SDK v2 notes](https://py.sdk.modelcontextprotocol.io/whats-new/)
- [MCP 2026-07-28 specification](https://modelcontextprotocol.io/specification/2026-07-28)
- [Read-only MCP MVP record](MCP-READ-ONLY-MVP.md)
