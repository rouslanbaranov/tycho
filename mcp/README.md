# MCP sources

This directory owns the read-only Tycho MCP server, HTTP wrapper, shared
tool contract, launchable client CLI and MCP-specific smokes/benchmarks.

- `mcp_server.py` - stdio MCP adapter.
- `mcp_http_server.py` - authenticated HTTP MCP and book/search wrapper.
- `mcp_contract.py` - input/output schema and tool catalog metadata.
- `agent_session_cli.py` - small read-only CLI drill-down entry point.
- `*_smoke.py` - stdlib and optional official-SDK transport smokes.
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
