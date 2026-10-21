"""Explicit directory remapping and reversible historical views.

Only directory names and local link path segments change. Public URLs, query
strings, fragments, prose, code and evidence metadata retain their exact bytes.
The separate migration validator enforces baseline hashes and path coverage.
"""
import hashlib
import json
from pathlib import Path
import posixpath
import re
from urllib.parse import unquote, urlsplit

MANIFEST = 'edition/directory-migration.json'
LINK = re.compile(r'(!?\[[^\]\n]*\]\()([^\s)]+)([^)\n]*\))')


def sha(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def remap(path, directories):
    for old in sorted(directories, key=len, reverse=True):
        if path == old or path.startswith(old + '/'):
            return directories[old] + path[len(old):]
    return path


def rewrite(text, source, directories):
    """Preserve relative spelling, changing only the traversed named segments."""
    def link(match):
        raw = match.group(2)
        u = urlsplit(raw)
        if u.scheme or u.netloc or raw.startswith('/') or not u.path:
            return match.group(0)
        cursor = posixpath.dirname(source)
        parts = []
        for token in u.path.split('/'):
            cursor = posixpath.normpath(posixpath.join(cursor, unquote(token)))
            mapped = remap(cursor, directories)
            if token not in ('', '.', '..') and mapped != cursor:
                # A renamed ancestor is insufficient: only replace this token
                # if this exact path is itself one of the moved directories.
                parts.append(posixpath.basename(mapped) if cursor in directories else token)
            else:
                parts.append(token)
        path = '/'.join(parts)
        value = path + raw[len(u.path):]
        return match.group(1) + value + match.group(3)
    text = LINK.sub(link, text)
    if not directories:
        return text
    # Explicit repository paths in frontmatter, inline code and prose. A path
    # inside an HTTP URL is excluded by the preceding slash/word boundary.
    alternatives = '|'.join(re.escape(p) for p in sorted(directories, key=len, reverse=True))
    pattern = re.compile(r'https?://[^\s<>\"\x27]+|(?<![\w/])(' + alternatives + r')(?=/|[\s\"\x27`]|$)')
    return pattern.sub(lambda m: directories[m.group(1)] if m.group(1) else m.group(0), text)


class HistoricalView:
    """Read earlier manifests against today's paths without changing history.

    Reads intentionally do not enforce whole-file baseline hashes: the original
    decomposition/enrichment validators retain their specific negative oracles.
    validate_directory_migration enforces the complete migration boundary.
    """
    def __init__(self, root):
        self.root = Path(root)
        path = self.root / MANIFEST
        self.manifest = json.loads(path.read_text()) if path.exists() else None
        self.directories = {r['old']: r['new'] for r in self.manifest['directories']} if self.manifest else {}
        self.inverse = {v: k for k, v in self.directories.items()}

    def current(self, path):
        return remap(path, self.directories)

    def original(self, path):
        return remap(path, self.inverse)

    def path(self, path):
        return self.root / self.current(path)

    def read_text(self, path):
        current = self.current(path)
        return rewrite((self.root / current).read_text(), current, self.inverse)
