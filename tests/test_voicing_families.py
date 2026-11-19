"""Musical invariants of the voicing-family examples (analysis 024) and coherence with the
Accordi tool: every example must be one of the voicings that js/voicings.js generates."""
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import unittest

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT.parent / 'appunti-strumenti'
spec = importlib.util.spec_from_file_location('vf', ROOT / 'scripts/generate_voicing_families.py')
vf = importlib.util.module_from_spec(spec)
spec.loader.exec_module(vf)
cm = vf.cm
SHEETS = {stem: events for stem, title, events in vf.SHEETS}
TOOL_QUALITY = {'maj7': 'maj7', '6': '6', '7': '7', 'm7': 'm7', 'm7(b5)': 'm7b5', 'maj': 'maj', 'm': 'm'}


COLOR = ('ust', 'quartal', 'cluster')


def pitches(event):
    return [v['pitch'] for v in event['voices']]


class VoicingFamiliesTest(unittest.TestCase):
    def test_playable_and_spelled(self):
        for stem, events in SHEETS.items():
            for e in events:
                strings = [v['string'] for v in e['voices']]
                self.assertEqual(strings, sorted(set(strings), reverse=True), (stem, e['label']))
                self.assertEqual(pitches(e), sorted(set(pitches(e))), (stem, e['label']))
                frets = [v['fret'] for v in e['voices']]
                self.assertTrue(all(1 <= f <= 17 for f in frets), (stem, e['label']))
                self.assertLessEqual(max(frets) - min(frets), 4, (stem, e['label']))
                for v in e['voices']:
                    name = v['name'].rstrip("',")
                    alter = name[1:].count('s') - name[1:].count('f')
                    self.assertEqual((cm.NATURAL[name[0]] + alter) % 12, v['pitch'] % 12, (stem, v))

    def test_chord_tones_no_tension_in_bass(self):
        for stem, events in SHEETS.items():
            for e in events:
                _, _, root = cm.parse_root(e['root'])
                tones = dict((s, d) for d, s in e['tones'])
                pcs = [(p - root) % 12 for p in pitches(e)]
                self.assertLessEqual(set(pcs), set(tones), (stem, e['label']))
                self.assertLessEqual(tones[pcs[0]], 7, (stem, e['label'], 'tensione al basso'))

    def test_rootless(self):
        for stem in ('vf-senza-fondamentale', 'vf-senza-fondamentale-ii-v-i'):
            for e in SHEETS[stem]:
                self.assertEqual(e['family'], 'rootless')
                _, _, root = cm.parse_root(e['root'])
                tones = dict((s, d) for d, s in e['tones'])
                degrees = [tones[(p - root) % 12] for p in pitches(e)]
                self.assertNotIn(1, degrees, (stem, e['label']))
                self.assertIn(3, degrees, (stem, e['label']))
                self.assertIn(degrees[0], (3, 7), (stem, e['label'], 'nota guida al basso'))
        # Two forms: third in the bass on 5-4-3-2, seventh in the bass on 4-3-2-1.
        rows = SHEETS['vf-senza-fondamentale']
        bass = [dict((s, d) for d, s in e['tones'])[(pitches(e)[0] - cm.parse_root(e['root'])[2]) % 12]
                for e in rows]
        self.assertEqual(bass, [3] * 4 + [7] * 4)
        # II-V-I: the guide tone in the bass alternates 3-7-3 (form A) and 7-3-7 (form B).
        seq = SHEETS['vf-senza-fondamentale-ii-v-i']
        bass = [dict((s, d) for d, s in e['tones'])[(pitches(e)[0] - cm.parse_root(e['root'])[2]) % 12]
                for e in seq]
        self.assertEqual(bass, [3, 7, 3, 3, 7, 3, 7, 7])

    def test_drop_structures(self):
        expected = {'drop2': [2], 'drop3': [3], 'drop24': [2, 4], 'triad': [], 'spread': [2],
                    'rootless': [2]}
        for stem, events in SHEETS.items():
            for e in events:
                if e['family'] == 'shell':
                    self.assertEqual(len(e['voices']), 3)
                    continue
                if e['family'] in COLOR:
                    continue
                n = len(e['tones'])
                self.assertEqual(len(e['voices']), n)
                self.assertEqual(len({p % 12 for p in pitches(e)}), n, (stem, e['label']))
                # Raise the lowered voices back: the chord is in close position.
                p = pitches(e)
                ranks = expected[e['family']]
                close = sorted(p)
                for _ in ranks:
                    close = sorted(close[1:] + [close[0] + 12])
                self.assertLess(close[-1] - close[0], 12, (stem, e['label']))
                top = sorted(close, reverse=True)
                raised = [top.index(x + 12) + 1 for x in p if x + 12 in top and x not in top]
                self.assertEqual(sorted(raised), ranks, (stem, e['label']))

    def test_root_in_bass_where_stated(self):
        for stem in ('vf-confronto', 'vf-drop2-gruppi', 'vf-drop24'):
            for e in SHEETS[stem]:
                self.assertEqual(pitches(e)[0] % 12, cm.parse_root(e['root'])[2], (stem, e['label']))

    def test_comping_voice_leading(self):
        self.assertEqual([e['label'] for e in SHEETS['vf-drop2-ii-v-i']], ['Dm7', 'G7', 'Cmaj7', 'C6'])
        self.assertEqual([e['label'] for e in SHEETS['vf-triadi-ii-v-i']], ['Dm', 'G', 'C', 'C'])
        rootless = SHEETS['vf-senza-fondamentale-ii-v-i']
        for seq in (SHEETS['vf-drop2-ii-v-i'], SHEETS['vf-triadi-ii-v-i'][:3], rootless[:4], rootless[4:]):
            for a, b in zip(seq, seq[1:]):
                self.assertLessEqual(max(abs(x - y) for x, y in zip(pitches(a), pitches(b))), 2,
                                     (a['label'], b['label']))

    def test_triads(self):
        for stem, family in (('vf-triadi-strette', 'triad'), ('vf-triadi-late', 'spread')):
            events = SHEETS[stem]
            for row in (events[:3], events[3:]):
                # Three inversions per string set: a different note on top each time.
                self.assertEqual(len({pitches(e)[-1] % 12 for e in row}), 3, stem)
                self.assertEqual(len({tuple(v['string'] for v in e['voices']) for e in row}), 1, stem)
            for e in events:
                self.assertEqual(e['family'], family)
                span = pitches(e)[-1] - pitches(e)[0]
                self.assertTrue(span < 12 if family == 'triad' else span > 12, (stem, e['label']))

    def degrees(self, e):
        return [d for d, _ in e['tones']]

    def test_upper_structures(self):
        for stem in ('vf-strutture-superiori', 'vf-strutture-superiori-alterate'):
            for e in SHEETS[stem]:
                if e['family'] != 'ust':
                    continue
                self.assertIn(self.degrees(e)[0], (3, 7), (stem, e['label'], 'nota guida al basso'))
                p = pitches(e)
                upper = sorted((x - p[1]) % 12 for x in p[1:])
                self.assertIn(upper, ([0, 4, 7], [0, 3, 8], [0, 5, 9]), (stem, e['label'], 'triade maggiore'))
                self.assertLess(p[3] - p[1], 12, (stem, e['label'], 'triade stretta'))
        # Alterate: risoluzione su Fmaj9 per semitono o nota comune.
        seq = SHEETS['vf-strutture-superiori-alterate']
        self.assertLessEqual(max(abs(x - y) for x, y in zip(pitches(seq[2]), pitches(seq[3]))), 1)

    def test_fourths(self):
        for stem in ('vf-quarte', 'vf-quarte-modale'):
            for e in SHEETS[stem]:
                p = pitches(e)
                steps = [b - a for a, b in zip(p, p[1:])]
                self.assertEqual(steps, [5, 5, 5, 4] if len(p) == 5 else [5] * len(steps), (stem, e['label']))
                self.assertLessEqual(self.degrees(e)[0], 7, (stem, e['label']))

    def test_clusters(self):
        for e in SHEETS['vf-cluster']:
            p = pitches(e)
            steps = [b - a for a, b in zip(p, p[1:])]
            self.assertTrue(any(d <= 2 for d in steps), e['label'])
            self.assertTrue({3} & set(self.degrees(e)), e['label'])
            # Niente corde a vuoto (decisione dell'utente, analisi 024).
            self.assertTrue(all(v['fret'] >= 1 for v in e['voices']))

    @unittest.skipUnless(shutil.which('node') and (TOOLS / 'js/voicings.js').is_file(),
                         'manca node o ../appunti-strumenti')
    def test_examples_are_tool_voicings(self):
        jobs = []
        for stem, events in SHEETS.items():
            for e in events:
                jobs.append(dict(stem=stem, label=e['label'], family=e['family'],
                                 quality=TOOL_QUALITY[e['quality']], root=cm.parse_root(e['root'])[2],
                                 shape=[[6 - v['string'], v['fret']] for v in e['voices']]))
        script = r"""
const V = require(process.argv[1] + '/js/voicings.js');
const C = require(process.argv[1] + '/js/chords.js');
const jobs = JSON.parse(require('fs').readFileSync(0, 'utf8'));
const missing = jobs.filter((j) => {
  const q = C.catalog().find((x) => x.id === j.quality);
  const all = V.voicings(q, j.root, [j.family], { alt: true }).flatMap(V.octaves);
  const key = (notes) => JSON.stringify(notes.map((n) => [n.string, n.fret]));
  return !all.some((v) => key(v.notes) === JSON.stringify(j.shape));
}).map((j) => `${j.stem} ${j.label} ${j.family}`);
process.stdout.write(JSON.stringify(missing));
"""
        out = subprocess.run([shutil.which('node'), '-e', script, str(TOOLS)], input=json.dumps(jobs),
                             capture_output=True, text=True, check=True)
        self.assertEqual(json.loads(out.stdout), [])


if __name__ == '__main__':
    unittest.main()
