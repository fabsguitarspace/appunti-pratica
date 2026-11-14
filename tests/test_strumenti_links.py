"""Deep link verso gli Strumenti per la pratica (ADR 0005).

Controlla i link :strumento:`testo <pagina#v=1&...>` di tutti i capitoli (Scale e Arpeggi):
- pagina esistente fra quelle pubblicate, frammento versionato `v=1`;
- se il repository ../appunti-strumenti è presente e Node è installato, ogni parametro
  è riconosciuto dallo strumento: js/link.js lo decodifica e lo riscrive uguale, la scala
  esiste nel catalogo e la tonica è valida. Senza il repository il controllo è saltato.
Da eseguire prima di ogni rilascio del volume.
"""
from pathlib import Path
import json, re, shutil, subprocess, sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / 'src/docs'
TOOLS = ROOT.parent / 'appunti-strumenti'
PAGES = {'index.html', 'scale.html', 'arpeggi.html'}
ROLE = re.compile(r':strumento:`[^`<]*<([^>]+)>`', re.S)

links = []
for path in sorted(DOCS.rglob('*.rst')):
    for target in ROLE.findall(path.read_text()):
        links.append((path.name, re.sub(r'\s+', '', target)))
assert links, 'nessun link :strumento: trovato'

fragments = []
for name, target in links:
    page, _, frag = target.partition('#')
    assert page in PAGES, (name, target)
    if not frag:
        continue
    params = dict(p.split('=', 1) for p in frag.split('&'))
    assert params.get('v') == '1', (name, target)
    assert 'theme' not in params, ('il tema lo aggiunge _static/strumenti.js', name, target)
    fragments.append((name, page, {k: unquote(v) for k, v in params.items()}))

node = shutil.which('node')
if not (node and (TOOLS / 'js/link.js').is_file()):
    print(f'PASS (parziale): {len(links)} link; schema non verificato, manca node o {TOOLS}')
    sys.exit(0)

CHECK = r'''
const tools = process.argv[1];
const T = require(tools + '/js/theory.js');
const L = require(tools + '/js/link.js');
const P = require(tools + '/js/exercises/presets.js');
const C = require(tools + '/js/chords.js');
const slugs = new Set(T.catalog().map((s) => L.slug(s.name)));
const chords = new Set(C.catalog().map((q) => q.id));
const SCOPE_KEYS = ['v', 'scale', 'chord', 'root'];
/** Ogni parametro dell'esercizio deve sopravvivere a decodifica e ricodifica con il catalogo dato. */
function roundTrip(params, cat, errors) {
  if (params.preset && !cat.PRESETS.some((p) => p.id === params.preset)) errors.push('esercizio sconosciuto ' + params.preset);
  if (params.rhythm && !cat.RHYTHMS.some((r) => r.id === params.rhythm)) errors.push('ritmo sconosciuto ' + params.rhythm);
  if (params.bpm && !(+params.bpm >= 30 && +params.bpm <= 300)) errors.push('bpm fuori da 30–300');
  const d = L.decodeExercise(params);
  const s = { ...cat.DEFAULTS, ...cat.presetDefaults(d.presetId || cat.DEFAULTS.presetId), ...d,
    scope: { ...cat.DEFAULTS.scope, ...(d.scope || {}) } };
  const back = L.encodeExercise(s);
  for (const [k, v] of Object.entries(params)) {
    if (SCOPE_KEYS.includes(k)) continue;
    if (String(back[k]) !== v) errors.push(k + '=' + v + ' ignorato (diventa ' + back[k] + ')');
  }
}
const out = [];
for (const [name, page, params] of JSON.parse(require('fs').readFileSync(0, 'utf8'))) {
  const errors = [];
  if (page === 'scale.html') {
    if (params.scale && !slugs.has(params.scale)) errors.push('scala sconosciuta ' + params.scale);
    if (params.root && !L.parseNote(params.root)) errors.push('tonica non valida ' + params.root);
    if (!!params.scale !== !!params.root) errors.push('scale e root vanno insieme');
    if (params.start) errors.push('start vale solo negli arpeggi');
    // link.js lascia passare gli id; il pannello li scarterebbe se non sono nei cataloghi.
    roundTrip(params, P, errors);
  }
  if (page === 'arpeggi.html') {
    if (params.chord && !chords.has(params.chord)) errors.push('arpeggio sconosciuto ' + params.chord);
    if (params.root && !L.parseNote(params.root)) errors.push('fondamentale non valida ' + params.root);
    if (!!params.chord !== !!params.root) errors.push('chord e root vanno insieme');
    if (params.start && (params.ext === 'full' || params.scope === 'chain')) errors.push('start ignorato con ext=full o scope=chain');
    roundTrip(params, P.ARPEGGI, errors);
  }
  if (errors.length) out.push(name + ': ' + JSON.stringify(params) + ' → ' + errors.join('; '));
}
console.log(JSON.stringify(out));
'''
result = subprocess.run([node, '-e', CHECK, str(TOOLS)], input=json.dumps(fragments),
                        capture_output=True, text=True)
assert result.returncode == 0, result.stderr
problems = json.loads(result.stdout)
assert not problems, '\n'.join(problems)
print(f'PASS: {len(links)} link verso gli strumenti, {len(fragments)} esercizi riconosciuti da appunti-strumenti')
