// Actual Mermaid syntax parsing. This does not exercise browser SVG layout.
import fs from 'node:fs';
import path from 'node:path';
import {JSDOM} from 'jsdom';
const args = process.argv.slice(2);
const option = (name, fallback) => {
  const i = args.indexOf(name);
  if (i < 0) return fallback;
  if (!args[i + 1] || args[i + 1].startsWith('--')) throw Error('Missing ' + name);
  return args[i + 1];
};
const root = path.resolve(option('--root', '.'));
const dom = new JSDOM('<!doctype html><html><body></body></html>');
globalThis.window = dom.window;
globalThis.document = dom.window.document;
const {default: mermaid} = await import('mermaid');
mermaid.initialize({startOnLoad: false, securityLevel: 'strict'});
function* markdown(dir) {
  for (const entry of fs.readdirSync(dir, {withFileTypes: true}).sort((a,b) => a.name.localeCompare(b.name))) {
    const p = path.join(dir, entry.name);
    if (entry.isSymbolicLink()) throw Error('Refuse symlink: ' + path.relative(root, p));
    if (entry.isDirectory()) yield* markdown(p);
    else if (entry.isFile() && p.endsWith('.md')) yield p;
  }
}
const results = [];
for (const file of markdown(path.join(root, 'book'))) {
  let fence = null, source = [], lineNumber = 0, openingLine = 0;
  for (const line of fs.readFileSync(file, 'utf8').split(/\r?\n/)) {
    lineNumber++;
    const match = line.match(/^\s{0,3}(`{3,}|~{3,})(.*)$/);
    if (!fence && match) {
      fence = {marker: match[1][0], length: match[1].length, diagram: match[2].trim() === 'mermaid'};
      openingLine = lineNumber;
      source = [];
    } else if (fence && match && match[1][0] === fence.marker &&
               match[1].length >= fence.length && !match[2].trim()) {
      if (fence.diagram) {
        const row = {path: path.relative(root, file).split(path.sep).join('/'), line: openingLine};
        try {
          const parsed = await mermaid.parse(source.join('\n'));
          results.push({...row, status: 'passed', diagramType: parsed.diagramType});
        } catch (e) {
          results.push({...row, status: 'failed', error: String(e.message || e)});
        }
      }
      fence = null;
    } else if (fence?.diagram) source.push(line);
  }
  if (fence) throw Error('Unclosed code fence: ' + path.relative(root, file));
}
if (!results.length) throw Error('No Mermaid diagrams checked');
const version = JSON.parse(fs.readFileSync(new URL('./node_modules/mermaid/package.json', import.meta.url))).version;
const report = {engine: 'mermaid ' + version, scope: 'syntax parser only; browser rendering not executed',
  total: results.length, passed: results.filter(r => r.status === 'passed').length, results};
const reportPath = option('--report', null);
if (reportPath) fs.writeFileSync(path.resolve(reportPath), JSON.stringify(report, null, 2) + '\n');
console.log(JSON.stringify({...report, results: results.filter(r => r.status === 'failed')}, null, 2));
process.exitCode = results.some(r => r.status === 'failed') ? 1 : 0;
