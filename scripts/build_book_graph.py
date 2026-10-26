#!/usr/bin/env python3
"""Build or check the deterministic derived structural graph."""
import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import book_graph  # noqa: E402
import route_index  # noqa: E402


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("build", "check"))
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--output", type=Path,
                        default=ROOT / "generated/book-graph.v1.json")
    args = parser.parse_args()
    root = args.root.resolve()
    scan = route_index.canonical_scan(root)
    graph = book_graph.build_graph(root, scan=scan)
    data = book_graph.graph_bytes(graph)
    if args.action == "build":
        size = book_graph.write_graph(args.output, graph)
        print("Built " + str(len(graph["nodes"])) + " nodes, "
              + str(len(graph["edges"])) + " edges; "
              + str(size) + " bytes; " + graph["content_sha256"])
        return 0
    if not args.output.is_file():
        print("FAIL: graph missing: " + str(args.output), file=sys.stderr)
        return 1
    actual = args.output.read_text(encoding="utf-8")
    if actual != data:
        print("FAIL: graph stale or corrupted; rebuild deliberately",
              file=sys.stderr)
        return 1
    print("PASS: " + graph["source_snapshot_sha256"] + " "
          + graph["content_sha256"])
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (book_graph.GraphError, RuntimeError, OSError) as exc:
        print("FAIL: " + str(exc), file=sys.stderr)
        sys.exit(1)
