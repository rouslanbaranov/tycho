#!/usr/bin/env python3
"""Hash canonical visible article text for a public source representation."""
import argparse
import hashlib
from html.parser import HTMLParser
from pathlib import Path
import re
import sys
import urllib.request

MARKERS = ("devsite-article-body", "markdown-body", "article-body")
SKIP = {"script", "style", "noscript", "svg", "nav", "footer"}
SPACE = re.compile(r"\s+")


class ArticleText(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.depth = 0
        self.capture = False
        self.skip = 0
        self.parts = []
        self.fallback = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in SKIP:
            self.skip += 1
            return
        if tag == "div" and self.depth:
            self.depth += 1
        elif tag == "div" and any(marker in attrs.get("class", "")
                                  for marker in MARKERS):
            self.capture = True
            self.depth = 1

    def handle_endtag(self, tag):
        if tag in SKIP and self.skip:
            self.skip -= 1
            return
        if self.capture and tag == "div":
            self.depth -= 1
            if self.depth == 0:
                self.capture = False

    def handle_data(self, data):
        if self.skip:
            return
        if self.capture:
            self.parts.append(data)
        else:
            self.fallback.append(data)

    def text(self):
        value = "\n".join(self.parts or self.fallback)
        return SPACE.sub(" ", value).strip()


def canonical_text(html):
    parser = ArticleText()
    parser.feed(html)
    return parser.text()


def digest(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", help="HTTP(S) URL or local HTML file")
    parser.add_argument("--file", action="store_true", help="treat source as a file")
    args = parser.parse_args()
    if args.file:
        html = Path(args.source).read_text(encoding="utf-8")
    else:
        request = urllib.request.Request(args.source, headers={"User-Agent": "Tycho/1"})
        with urllib.request.urlopen(request, timeout=30) as response:
            html = response.read().decode("utf-8", "replace")
    text = canonical_text(html)
    if len(text) < 100:
        print("FAIL: extracted text too short", file=sys.stderr)
        return 1
    print(digest(text))
    return 0


if __name__ == "__main__":
    sys.exit(main())
