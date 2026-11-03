#!/usr/bin/env python3
"""Read-only queries over the derived structural graph."""
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import book_graph  # noqa: E402


def emit(value, as_json):
    if as_json:
        print(json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False))
    else:
        if value.get("query") == "backlinks":
            print(book_graph.format_backlinks(value))
        elif value.get("query") == "path":
            print(book_graph.format_path(value))
        else:
            print(book_graph.format_audit(value))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--graph", type=Path,
                        default=ROOT / "generated/book-graph.v1.json")
    parser.add_argument("--json", action="store_true",
                        help="emit the full bounded JSON result")
    commands = parser.add_subparsers(dest="command", required=True)

    backlinks = commands.add_parser("backlinks",
                                    help="incoming links for one node")
    backlinks.add_argument("--id", required=True)
    backlinks.add_argument("--kind", action="append",
                           choices=book_graph.EDGE_KINDS)
    backlinks.add_argument("--limit", type=int, default=50)

    path = commands.add_parser("path", help="shortest structural path")
    path.add_argument("--from", dest="start", required=True)
    path.add_argument("--to", dest="goal", required=True)
    path.add_argument("--max-hops", type=int, default=4)
    path.add_argument("--edge-kind", action="append",
                      choices=book_graph.EDGE_KINDS)
    path.add_argument("--undirected", action="store_true")

    commands.add_parser("audit", help="structural findings and counts")

    args = parser.parse_args()
    graph = book_graph.load_graph(args.graph)
    if args.command == "backlinks":
        if not 1 <= args.limit <= 200:
            parser.error("--limit must be 1..200")
        result = book_graph.backlinks(graph, args.id,
                                      kinds=tuple(args.kind) if args.kind else None,
                                      limit=args.limit)
        result["query"] = "backlinks"
    elif args.command == "path":
        kinds = (tuple(args.edge_kind) if args.edge_kind
                 else book_graph.DOCUMENT_PATH_KINDS)
        result = book_graph.shortest_path(graph, args.start, args.goal,
                                          max_hops=args.max_hops, kinds=kinds,
                                          directed=not args.undirected)
        result["query"] = "path"
    else:
        result = book_graph.audit_graph(graph)
        result["query"] = "audit"
    emit(result, args.json)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (book_graph.GraphError, OSError, json.JSONDecodeError) as exc:
        print("FAIL: " + str(exc), file=sys.stderr)
        sys.exit(1)
