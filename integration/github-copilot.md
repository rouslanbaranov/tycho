# GitHub Copilot

**Status:** implemented. Configuration cross-checked against the published
VS Code MCP reference on 2026-11-02. A live Copilot session was not available
while this file was written; the MCP surface itself is covered by
`integration/verify.py`.

Complete Steps 0-6 of `instructions.md` first.

## Files

| Surface | File | Top-level key |
|---|---|---|
| Harness sessions and Copilot CLI | `.mcp.json` | `mcpServers` |
| VS Code chat UI | `.vscode/mcp.json` | `servers` |
| Custom agent | `.github/agents/<name>.agent.md` | frontmatter |

The two configuration files are not interchangeable. The chat UI reads its own
format; harness sessions read the portable format. If the owner is unsure
which surface applies, provide both entries; they do not conflict.

## 1. Add the server entry

Use the stdio entry from Step 6 as the default. Merge it into an existing file
instead of replacing other servers. The VS Code format for the chat UI:

```json
{
  "servers": {
    "tycho": {
      "type": "stdio",
      "command": "/ABS/PROJECT/.tycho/.venv/bin/python",
      "args": [
        "/ABS/PROJECT/.tycho/mcp/mcp_server.py",
        "--root",
        "/ABS/PROJECT/.tycho"
      ]
    }
  }
}
```

For HTTP, keep the server running with `integration/mcp_server_ctl.py`
and export the token before the harness starts.

Environment variables are a common failure: desktop applications on macOS and
Windows do not inherit variables exported in a terminal. If the HTTP entry
reports a missing token, start the harness from a shell that exports it, or set
the variable in the launcher environment.

## 2. Add the Tycho agent

Check for an existing agent with the same name:

```sh
mkdir -p .github/agents
grep -l '^name: Tycho' .github/agents/*.agent.md 2>/dev/null
ls .github/agents 2>/dev/null
```

If an agent named Tycho exists, ask:

> An agent named Tycho already exists at `<path>`. Choose another
> name for the Tycho agent, or confirm that I replace the existing file.

Then copy the template and, if the name changed, update both the file name and
the `name:` field:

```sh
cp "$INSTALL_DIR/.github/agents/tycho.agent.md" .github/agents/tycho.agent.md
```

The template restricts tools to `tycho/*`, `read` and
`search`. `tycho/*` requires the MCP server entry to be
named `tycho`. If the owner renamed the server, update the tools list
in the agent file.

## 3. Activate

1. Reload the VS Code window, or restart the Copilot session.
2. Approve the `tycho` server when the harness asks to start it.
3. Select the agent by name in the agents picker.
4. Ask: "Call tycho_describe and report the snapshot ID, document count and
   section count."
5. Ask: "Search Tycho for idempotency keys and cite one section as
   path#section_id."

Expected: the counts reported by Step 4, and at least one resolvable citation.

## 4. Verify

- The tools are visible for the `tycho` server.
- `tycho_describe` returns the snapshot from Step 4.
- A search returns `path#section_id` citations.
- The agent answers with an evidence map, not only prose.
- No tool call edits a file.

If tools do not appear, check the harness log, confirm absolute paths, confirm
the virtual environment exists, and run Step 5 of `instructions.md`.

## 5. Limits

- The Copilot coding agent in the cloud has no access to the local checkout or
  index. Use a local surface.
- The HTTP transport implements the stateless 2026-07-28 revision. A client
  limited to the older handshake must use stdio.
- There is no OAuth, per-client authorization or rate limiting. Keep the HTTP
  server on a trusted boundary.

