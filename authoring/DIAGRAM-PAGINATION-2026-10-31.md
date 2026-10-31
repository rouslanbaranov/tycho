# Diagram-safe page/read pagination — 2026-10-31

Status: implemented and tested. No book/atlas content change.

## Behavior

- fenced Mermaid blocks are detected by their opening and closing fences;
- if the requested budget would end inside a diagram, the slice extends to the
  closing fence, even above the soft budget;
- next_offset is set after the closing fence;
- sequential responses have no gaps or intersections.

## Response metadata

tycho_page and tycho_read add:

- budget_requested_chars;
- budget_overrun_chars;
- diagram_completed;
- exact next_offset.

The default soft budget is 2,500 codepoints; the request maximum is 6,000.

## Manual offset inside a diagram

The call returns a tool execution error with isError=true and this stable text:

offset-inside-diagram: requested_offset=...; diagram_start=...;
diagram_end=...; suggested_offset=...; retry with offset=... or offset=...

There is no structuredContent for this error. outputSchema remains success-only;
protocol errors remain JSON-RPC errors.

## Tests

tests/test_tycho_diagram_pagination.py covers:

- ranges and budget overrun;
- manual offset inside a diagram;
- sequential slices with no gap;
- complete diagram via tycho_page;
- text-only error envelope.

## Limits

- Diagrams longer than the maximum budget still require multiple calls.
- The detector recognizes fenced Mermaid blocks, not arbitrary diagrams.
- No human review or production benchmark.
