"""Validate source inventory structure, topic references and catalogue freshness.

This is a targeted Python validator, not a JSON Schema engine or proof that a
source supports a technical claim. It performs no network requests.
"""
from datetime import date
from pathlib import Path
from urllib.parse import urlsplit
import importlib.util
import json
import re

ROOT = Path(__file__).resolve().parents[1]
FIELDS = {
    'id', 'title', 'category', 'publisher', 'kind', 'url', 'resolved_url',
    'topics', 'priority', 'planned_use', 'admission', 'access',
    'reading_status', 'version', 'access_checked', 'content_verified',
    'license_notes', 'verification_scope', 'observed_title',
}
ADMISSION = {'admitted-for-research', 'bibliography-only', 'pending-content-access'}
ACCESS = {'bibliographic-page-and-preview', 'free-personalized-download', 'public-web-or-author-download'}
READING = {'fetch-incomplete', 'landing-or-abstract-inspected', 'full-public-page-inspected'}
MANDATORY = {
    'src.kafka', 'src.kafka-design', 'src.postgresql', 'src.postgres-concurrency',
    'src.reactor', 'src.reactive-streams', 'src.jep444', 'src.jep491',
    'src.jdk25-virtual-threads', 'src.continuous-delivery-book', 'src.argocd',
    'src.argo-rollouts', 'src.citus', 'src.pgbouncer', 'src.k8s-hpa',
    'src.tail-at-scale', 'src.little-law', 'src.k6',
    'src.otel-metrics-model', 'src.prometheus-storage',
}

def require(condition, message):
    if not condition:
        raise ValueError(message)

def public_url(value):
    parsed = urlsplit(value)
    return (parsed.scheme == 'https' and bool(parsed.hostname)
            and parsed.hostname not in {'localhost', '127.0.0.1', '::1'}
            and not parsed.username and not parsed.password)

def validate(data):
    require(set(data) == {'schema_version', 'updated', 'scope', 'sources'}, 'Unexpected inventory fields')
    require(type(data['schema_version']) is int and data['schema_version'] == 2, 'Unsupported inventory version')
    require(isinstance(data['scope'], str) and bool(data['scope'].strip()), 'Missing inventory scope')
    date.fromisoformat(data['updated'])
    require(isinstance(data['sources'], list) and bool(data['sources']), 'Empty source inventory')
    ids, urls = set(), set()
    for entry in data['sources']:
        require(isinstance(entry, dict) and set(entry) == FIELDS, 'Unexpected source fields')
        sid = entry['id']
        require(isinstance(sid, str) and re.fullmatch(r'src\.[a-z0-9]+(?:-[a-z0-9]+)*', sid), 'Invalid source ID')
        require(sid not in ids, 'Duplicate source ID'); ids.add(sid)
        for field in FIELDS - {'topics', 'content_verified'}:
            require(isinstance(entry[field], str) and bool(entry[field].strip()), f'{sid}: missing {field}')
        require(public_url(entry['url']) and public_url(entry['resolved_url']), f'{sid}: invalid public URL')
        require(entry['url'] not in urls, f'{sid}: duplicate canonical URL'); urls.add(entry['url'])
        require(isinstance(entry['topics'], list) and bool(entry['topics']), f'{sid}: missing topics')
        require(all(isinstance(t, str) and re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', t) for t in entry['topics']), f'{sid}: invalid topic')
        require(len(entry['topics']) == len(set(entry['topics'])), f'{sid}: duplicate topic')
        require(entry['priority'] in {'core', 'supporting'}, f'{sid}: invalid priority')
        require(entry['admission'] in ADMISSION, f'{sid}: invalid admission')
        require(entry['access'] in ACCESS, f'{sid}: invalid access')
        require(entry['reading_status'] in READING, f'{sid}: invalid reading status')
        checked = date.fromisoformat(entry['access_checked'])
        require(checked <= date.fromisoformat(data['updated']), f'{sid}: check date later than inventory')
        if entry['content_verified'] is not None:
            date.fromisoformat(entry['content_verified'])
        if entry['kind'] == 'commercial-book':
            require(entry['admission'] == 'bibliography-only', f'{sid}: commercial book requires lawful content admission')
        if entry['admission'] == 'pending-content-access':
            require(entry['reading_status'] == 'fetch-incomplete', f'{sid}: inconsistent pending status')
    require(MANDATORY <= ids, 'Mandatory source coverage is missing')
    return ids

def main():
    data = json.loads((ROOT / 'sources/register.json').read_text())
    ids = validate(data)
    for folder in ['sources', 'authoring']:
        for path in (ROOT / folder).glob('*.md'):
            refs = set(re.findall(r'\bsrc\.[a-z0-9]+(?:-[a-z0-9]+)*', path.read_text()))
            require(refs <= ids, f'Unknown source reference in {path.relative_to(ROOT)}')
    spec = importlib.util.spec_from_file_location('source_catalog', ROOT / 'scripts/source_catalog.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    require((ROOT / 'sources/CATALOG.md').read_text() == module.render(), 'Source catalogue is stale')
    print(f'PASS: {len(ids)} source records, mandatory IDs, cross-references and catalogue freshness')

if __name__ == '__main__':
    main()
