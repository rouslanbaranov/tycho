# MCP smoke scripts

Transport-level checks that are not part of the unit-test suite:

- `mcp_sdk_smoke.py` - official SDK over stdio.
- `mcp_http_client_smoke.py` - stdlib HTTP client.
- `mcp_http_sdk_smoke.py` - official SDK over authenticated HTTP.
- `mcp_end_to_end_smoke.py` - end-to-end stdio checks.

Run from the repository root; the scripts compute the repository root from
`parents[2]` and accept explicit `--root` where applicable.
