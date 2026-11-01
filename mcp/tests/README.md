# MCP tests

This directory owns MCP-specific unit and integration tests.

Run from the repository root:

~~~sh
python3 -m unittest discover -s mcp/tests -p 'test_*.py' -v
~~~

Smoke/transport scripts are under `smoke/`. Shared non-MCP tests remain in the
top-level `tests/` directory. MCP tests compute the repository root from
`parents[2]` and add `mcp/` plus `scripts/` to `sys.path`.
