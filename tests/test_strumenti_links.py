"""Deep link verso gli Strumenti per la pratica (ADR 0005).

Controlla i link :strumento:`testo <pagina#v=1&...>` di tutti i capitoli (Scale, Arpeggi, Accordi,
Progressioni e Ritmi):
- pagina esistente fra quelle pubblicate, frammento versionato `v=1`;
- se il repository ../appunti-strumenti è presente e Node è installato, ogni parametro
  è riconosciuto dallo strumento: js/link.js lo decodifica e lo riscrive uguale, la scala
  esiste nel catalogo e la tonica è valida; negli Accordi e nelle Progressioni l'esercizio produce
  almeno un voicing;
- le griglie del catalogo di Progressioni (js/progressions.js) sono quelle del capitolo 7: stesse
  sigle e stesse battute, e ogni `ref` è un'etichetta del capitolo;
- nei Ritmi la figura esiste, la partenza sta nella griglia della figura, l'esercizio produce
  attacchi; le sezioni della pagina «Ritmo melodico» citate dallo strumento (js/ritmi.js) esistono.
  Senza il repository i controlli con Node sono saltati.
Da eseguire prima di ogni rilascio del volume.
"""
from pathlib import Path
import json, re, shutil, subprocess, sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / 'src/docs'
TOOLS = ROOT.parent / 'appunti-strumenti'
PAGES = {'index.html', 'scale.html', 'arpeggi.html', 'accordi.html', 'progressioni.html', 'ritmi.html'}
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
const X = require(tools + '/js/exercises/comping.js');
const V = require(tools + '/js/voicings.js');
const PG = require(tools + '/js/progression.js');
const PS = require(tools + '/js/progressions.js');
const PC = require(tools + '/js/exercises/progcomp.js');
const B = require(tools + '/js/exercises/bass.js');
const R = require(tools + '/js/rhythms.js');
const RL = require(tools + '/js/exercises/rhythmline.js');
// Impostazioni predefinite del pannello di Ritmi (js/rhythmpractice.js, defaults).
const RHYTHM_DEFAULTS = { ...RL.DEFAULTS, metroMode: 'two-four', bpm: 60 };
const METRO = ['all', 'two-four', 'one-three', 'downbeat', 'three', 'four', 'and-two-four'];
// Impostazioni predefinite del pannello di Progressioni (js/progpractice.js, defaults).
const PROG_DEFAULTS = { ...PC.DEFAULTS, study: 'grid', giri: 0, form: 'short', ending: 'loop', bpm: 60 };
const slugs = new Set(T.catalog().map((s) => L.slug(s.name)));
const chords = new Set(C.catalog().map((q) => q.id));
const SCOPE_KEYS = ['v', 'scale', 'chord', 'root', 'prog', 'key', 'rhythm'];
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
  if (page === 'accordi.html') {
    const q = C.catalog().find((x) => x.id === params.chord);
    if (params.chord && !q) errors.push('accordo sconosciuto ' + params.chord);
    if (params.root && !L.parseNote(params.root)) errors.push('fondamentale non valida ' + params.root);
    if (!!params.chord !== !!params.root) errors.push('chord e root vanno insieme');
    if (params.ex && !X.EXERCISES.some((e) => e.id === params.ex)) errors.push('esercizio sconosciuto ' + params.ex);
    if (params.rhythm && !X.RHYTHMS.some((r) => r.id === params.rhythm)) errors.push('ritmo sconosciuto ' + params.rhythm);
    if (params.attack && !X.ATTACKS.some(([id]) => id === params.attack)) errors.push('attacco sconosciuto ' + params.attack);
    if (params.dir && params.ex !== 'inv') errors.push('dir vale solo con ex=inv');
    if (params.bpm && !(+params.bpm >= 30 && +params.bpm <= 300)) errors.push('bpm fuori da 30–300');
    const fam = V.family(params.fam || X.DEFAULTS.family);
    if (!fam) errors.push('famiglia sconosciuta ' + params.fam);
    else if (params.set && params.set !== 'all' && !fam.sets.map(V.setLabel).includes(params.set)) errors.push('corde ' + params.set + ' fuori dalla famiglia ' + fam.id);
    if (q && fam && !V.familiesFor(q).includes(fam.id)) errors.push('la famiglia ' + fam.id + ' non prevede ' + q.id);
    const d = L.decodeChordExercise(params);
    const back = L.encodeChordExercise({ ...X.DEFAULTS, ...d });
    for (const [k, v] of Object.entries(params)) {
      if (SCOPE_KEYS.includes(k)) continue;
      if (String(back[k]) !== v) errors.push(k + '=' + v + ' ignorato (diventa ' + back[k] + ')');
    }
    if (q && params.root && fam && !errors.length) {
      const r = X.build(q, L.parseNote(params.root), d);
      if (r.error || !r.chords.length) errors.push('nessun voicing: ' + (r.error || 'sequenza vuota'));
    }
  }
  if (page === 'progressioni.html') {
    const prog = PS.catalog().find((x) => x.id === params.prog);
    if (params.prog && !prog) errors.push('progressione sconosciuta ' + params.prog);
    if (params.key && !L.parseNote(params.key)) errors.push('tonalità non valida ' + params.key);
    if (!!params.prog !== !!params.key) errors.push('prog e key vanno insieme');
    const fam = V.family(params.fam || PROG_DEFAULTS.family);
    if (!fam) errors.push('famiglia sconosciuta ' + params.fam);
    else if (params.set && params.set !== 'all' && !fam.sets.map(V.setLabel).includes(params.set)) errors.push('corde ' + params.set + ' fuori dalla famiglia ' + fam.id);
    const r = params.rhythm && X.PROG_RHYTHMS.find((x) => x.id === params.rhythm);
    if (params.rhythm && !r) errors.push('ritmo sconosciuto ' + params.rhythm);
    if (r && fam && r.families && !r.families.includes(fam.id)) errors.push('il ritmo ' + r.id + ' non vale con ' + fam.id);
    if (params.attack && !X.ATTACKS.some(([id]) => id === params.attack)) errors.push('attacco sconosciuto ' + params.attack);
    if (params.bass && !B.MODES.some((m) => m.id === params.bass)) errors.push('basso sconosciuto ' + params.bass);
    if (params.study && !['grid', 'guide', 'arp', 'play'].includes(params.study)) errors.push('studio sconosciuto ' + params.study);
    if (params.giri && !['0', '1', '2', '4'].includes(params.giri)) errors.push('giri non validi ' + params.giri);
    if (params.form && !(prog && prog.fullForm)) errors.push('form vale solo per aaba e rhythm-changes');
    if (params.end && !(prog && prog.ending && params.giri && params.giri !== '0')) errors.push('end vale solo con un finale nel catalogo e giri diversi da 0');
    if (params.bpm && !(+params.bpm >= 30 && +params.bpm <= 300)) errors.push('bpm fuori da 30–300');
    const d = L.decodeProgExercise(params);
    const s = { ...PROG_DEFAULTS, ...d };
    const back = L.encodeProgExercise(s);
    for (const [k, v] of Object.entries(params)) {
      if (SCOPE_KEYS.includes(k)) continue;
      if (String(back[k]) !== v) errors.push(k + '=' + v + ' ignorato (diventa ' + back[k] + ')');
    }
    if (prog && params.key && fam && !errors.length) {
      const real = PG.realize(prog, { key: L.parseNote(params.key), full: s.form === 'full',
        ending: s.ending === 'closed' && s.giri !== 0, giri: s.giri || 1 });
      const ex = PC.build(real, { ...s, fourVoices: prog.fourVoices, comp: s.study !== 'play', loop: s.giri === 0 });
      if (ex.error || !ex.events.length) errors.push('esercizio vuoto: ' + (ex.error || 'nessun evento'));
    }
  }
  if (page === 'ritmi.html') {
    const item = R.byId(params.rhythm);
    if (params.rhythm && !item) errors.push('figura sconosciuta ' + params.rhythm);
    if (params.key && !L.parseNote(params.key)) errors.push('tonalità non valida ' + params.key);
    if (!!params.rhythm !== !!params.key) errors.push('rhythm e key vanno insieme');
    if (params.start && !(item && item.kind === 'consecutive')) errors.push('start vale solo per le note consecutive');
    if (item && item.kind === 'consecutive' && /^\d+$/.test(params.start || '') && +params.start > R.METER * item.div) errors.push('partenza oltre la griglia della figura');
    if (params.vary && !(item && item.kind === 'perbar')) errors.push('vary vale solo per le note per battuta');
    if (params.notes && !RL.NOTES.some(([id]) => id === params.notes)) errors.push('altezze sconosciute ' + params.notes);
    if (params.omit && !R.OMIT.some(([id]) => id === params.omit)) errors.push('note tolte sconosciute ' + params.omit);
    if (params.accent && !R.ACCENTS.some(([id]) => id === params.accent)) errors.push('accento sconosciuto ' + params.accent);
    if (params.base && params.base !== 'none' && !PS.catalog().some((p) => p.id === params.base)) errors.push('base sconosciuta ' + params.base);
    if (params.bass && !RL.BASS.some(([id]) => id === params.bass)) errors.push('basso sconosciuto ' + params.bass);
    if (params.metro && !METRO.includes(params.metro)) errors.push('click sconosciuto ' + params.metro);
    if (params.bpm && !(+params.bpm >= 30 && +params.bpm <= 300)) errors.push('bpm fuori da 30–300');
    const d = L.decodeRhythmExercise(params);
    const s = { ...RHYTHM_DEFAULTS, ...d };
    // Come exerciseUrl in js/rhythmpractice.js.
    const random = !!item && (item.kind === 'perbar' || (item.kind === 'consecutive' && s.start === 'rand'));
    const back = L.encodeRhythmExercise({ ...s, random, start: item && item.kind === 'consecutive' ? s.start : null,
      vary: !!item && item.kind === 'perbar' && s.vary });
    for (const [k, v] of Object.entries(params)) {
      if (SCOPE_KEYS.includes(k)) continue;
      if (String(back[k]) !== v) errors.push(k + '=' + v + ' ignorato (diventa ' + back[k] + ')');
    }
    if (random && !params.seed) errors.push('figura casuale senza seed: il link non la riproduce');
    if (item && params.key && !errors.length) {
      const ex = RL.build(item, L.parseNote(params.key), s);
      if (ex.error || !RL.lineEvents(ex).length) errors.push('esercizio vuoto: ' + (ex.error || 'nessun attacco'));
    }
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

# ---------------------------------------------------------------- Griglie di Progressioni = capitolo 7

catalog = json.loads(subprocess.run(
    [node, '-e', "process.stdout.write(JSON.stringify(require(process.argv[1] + '/js/progressions.js').catalog()))", str(TOOLS)],
    capture_output=True, text=True, check=True).stdout)
chapter = (DOCS / '7-progressioni.rst').read_text().splitlines()
labels = {m.group(1): i for i, line in enumerate(chapter) if (m := re.match(r'\.\. _([\w-]+):\s*$', line))}

def bars(text):
    return [b.split() for b in text.split('|') if b.strip()]

def chapter_bars(start):
    """Battute del primo blocco letterale dopo l'etichetta (righe rientrate che contengono |)."""
    out, inside = [], False
    for line in chapter[start + 1:]:
        if line.startswith('.. _'):
            break
        if line.startswith('    ') and '|' in line:
            inside = True
            out += bars(line)
        elif inside and line.strip() and not line.startswith('    '):
            break
    return out

def table_rows(start):
    """Righe della tabella dell'AABA: sezione → sigle (una per battuta)."""
    rows, cells = {}, []
    for line in chapter[start + 1:]:
        if line.startswith('.. _') or (line and not line.startswith(' ') and cells):
            break
        m = re.match(r'\s+(\*)? ?- (.*)$', line)
        if m:
            if m.group(1):
                cells = []
            cells.append(m.group(2).strip())
            if len(cells) == 3:
                rows[cells[0]] = cells[2]
    return rows

grids = 0
for p in catalog:
    ref = p['ref']
    assert ref in labels, (p['id'], 'etichetta mancante nel capitolo 7', ref)
    order = list(dict.fromkeys(p['form']))
    mine = [b for sid in order for b in bars(p['sections'][sid])]
    if p['id'] == 'aaba':
        rows = table_rows(labels[ref])
        for sid, row in (('A', 'A1'), ('B', 'B')):
            assert [[c] for c in rows[row].split(', ')] == bars(p['sections'][sid]), (p['id'], sid, rows[row])
    else:
        assert chapter_bars(labels[ref]) == mine, (p['id'], chapter_bars(labels[ref]), mine)
    grids += 1

# ---------------------------------------------------------------- Sezioni della pagina citate dallo strumento Ritmi

ritmi = (TOOLS / 'js/ritmi.js').read_text()
anchors = set(re.findall(r"'(ritmo-[\w-]+)'", ritmi.split('ANCHORS =', 1)[1].split('};', 1)[0]))
page_labels = set(re.findall(r'^\.\. _([\w-]+):', (DOCS / 'ritmo-melodico.rst').read_text(), re.M))
assert anchors and anchors <= page_labels, ('sezioni mancanti in ritmo-melodico.rst', anchors - page_labels)

print(f'PASS: {len(links)} link verso gli strumenti, {len(fragments)} esercizi riconosciuti da appunti-strumenti, '
      f'{grids} griglie di Progressioni uguali al capitolo 7')
