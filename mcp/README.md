# MCP sources

This directory owns the read-only Tycho MCP server, HTTP wrapper, shared
tool contract, launchable client CLI and MCP-specific smokes/benchmarks.

- `mcp_server.py` - thin stdio protocol/composition facade.
- `mcp_*_tools.py` - feature mixins for search, reads, context, patterns and
  describe.
- `mcp_protocol.py` - JSON-RPC errors, argument validation and stdio loop.
- `mcp_shared.py` - shared evidence and frontmatter helpers.
- `mcp_contract.py` - constants, enums, tool metadata and schema loaders.
- `schemas/input/*.json`, `schemas/output/*.json` - one schema per tool.
- `INSTRUCTIONS.md` - spec-aligned high-level onboarding, loaded by discover.
- `mcp_http_server.py` - authenticated HTTP MCP and book/search wrapper.
- `agent_session_cli.py` - small read-only CLI drill-down entry point.
- `tests/` - MCP unit tests, CLI tests and page/diagram tests.
- `tests/smoke/` - stdlib and optional official-SDK transport smokes.
- `mcp_multi_process_benchmark.py` - MCP process benchmark.
- `benchmark_mcp_default.py`, `evaluate_mcp_default*.py` - MCP-specific
  retrieval diagnostics.

Shared retrieval implementation remains in `scripts/section_search.py`.
The folder is intentionally a namespace directory, not an initialized Python
package, so the installed official `mcp` SDK is not shadowed.

Run from the repository root:

```sh
python3 mcp/mcp_server.py --root .
python3 mcp/mcp_http_server.py --root . --port 8000
```
