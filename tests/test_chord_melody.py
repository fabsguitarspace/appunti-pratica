"""Musical invariants of the chord-melody voicings in the Accordi chapter."""
import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('cm', ROOT / 'scripts/generate_chord_melody.py')
cm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cm)
SHEETS = {stem: events for stem, title, events in cm.SHEETS}
EXTRA = {'A7(♭9)': {1}, 'G7(♭13)': {8}}  # tensions allowed beyond the seventh chord


def chords(stem):
    return [e for e in SHEETS[stem] if e['kind'] == 'chord']


def pitches(event):
    return [v['pitch'] for v in event['voices']]


def allowed_pcs(event):
    _, _, root = cm.parse_root(event['root'])
    tones = {s for d, s in cm.QUALITIES[event['quality']]} | EXTRA.get(event['label'], set())
    return root, tones


class ChordMelodyTest(unittest.TestCase):
    def test_every_voicing_is_playable_and_spelled(self):
        for stem, events in SHEETS.items():
            for e in events:
                strings = [v['string'] for v in e['voices']]
                self.assertEqual(len(set(strings)), len(strings), (stem, e['label']))
                self.assertEqual(pitches(e), sorted(set(pitches(e))), (stem, e['label']))
                self.assertEqual(strings, sorted(strings, reverse=True))
                frets = [v['fret'] for v in e['voices']]
                self.assertTrue(all(1 <= f <= 17 for f in frets), (stem, e['label']))
                if e['kind'] == 'chord':
                    self.assertLessEqual(max(frets) - min(frets), 4, (stem, e['label']))
                for v in e['voices']:
                    name = v['name'].rstrip("',")
                    alter = name[1:].count('s') - name[1:].count('f')
                    pc = (cm.NATURAL[name[0]] + alter) % 12
                    self.assertEqual(pc, v['pitch'] % 12, (stem, v))

    def test_chord_tones_and_bass(self):
        for stem, events in SHEETS.items():
            for e in chords(stem):
                root, tones = allowed_pcs(e)
                pcs = {(p - root) % 12 for p in pitches(e)}
                self.assertLessEqual(pcs, tones, (stem, e['label']))
                guide = {s for d, s in cm.QUALITIES[e['quality']] if d in (3, 6, 7)}
                self.assertTrue(pcs & guide, (stem, e['label']))
                self.assertIn((pitches(e)[0] - root) % 12,
                              {s for d, s in cm.QUALITIES[e['quality']]}, (stem, e['label']))

    def drop_index(self, event):
        """Raise the lowest voice an octave: close position, and its rank from the top."""
        p = pitches(event)
        raised = p[0] + 12
        close = sorted(p[1:] + [raised])
        self.assertLess(close[-1] - close[0], 12)
        return list(reversed(close)).index(raised) + 1

    def test_drop_structures(self):
        for stem in SHEETS:
            if stem.startswith('cm-drop2') or stem in ('cm-diminuiti-passaggio', 'cm-sesta-diminuita'):
                for e in chords(stem):
                    self.assertEqual(self.drop_index(e), 2, (stem, e['label']))
                    self.assertEqual([v['string'] for v in e['voices']], [4, 3, 2, 1])
        for e in chords('cm-drop3'):
            self.assertEqual(self.drop_index(e), 3, e['label'])
            root = cm.parse_root(e['root'])[2]
            self.assertEqual(pitches(e)[0] % 12, root)

    def test_four_melody_notes_per_drop2_quality(self):
        for stem in ('cm-drop2-maj7', 'cm-drop2-6', 'cm-drop2-7', 'cm-drop2-m7', 'cm-drop2-m7b5'):
            tops = [pitches(e)[-1] % 12 for e in chords(stem)]
            self.assertEqual(len(set(tops)), 4, stem)
            self.assertEqual(sorted(pitches(e)[-1] for e in chords(stem)),
                             [pitches(e)[-1] for e in chords(stem)])

    def test_smooth_voice_leading(self):
        for stem in ('cm-drop2-ii-v-i', 'cm-diminuiti-passaggio'):
            seq = chords(stem)
            for a, b in zip(seq, seq[1:]):
                moves = [abs(x - y) for x, y in zip(pitches(a), pitches(b))]
                self.assertLessEqual(max(moves), 2, (stem, a['label'], b['label']))

    def test_sixth_diminished_alternation(self):
        seq = chords('cm-sesta-diminuita')
        self.assertEqual([e['quality'] for e in seq], ['6', 'dim7'] * 4 + ['6'])
        tops = [pitches(e)[-1] for e in seq]
        self.assertEqual(tops, [67, 68, 69, 71, 72, 74, 76, 77, 79])

    def test_three_voices_bass_guide_melody(self):
        for e in chords('cm-tre-voci'):
            self.assertEqual(len(e['voices']), 3)
            root, _ = allowed_pcs(e)
            self.assertEqual((pitches(e)[0] - root) % 12, 0)
            self.assertIn((pitches(e)[1] - root) % 12, {3, 4, 10, 11})

    def test_arrangement_melody_and_form(self):
        events = SHEETS['cm-arrangiamento']
        self.assertEqual([pitches(e)[-1] for e in events], cm.ARRANGEMENT_MELODY)
        self.assertEqual(sum(cm.BEATS[e['dur']] for e in events), 32)
        self.assertEqual([e['label'] for e in chords('cm-arrangiamento')],
                         ['Cmaj7', 'A7', 'Dm7', 'G7', 'Em7', 'A7(♭9)', 'Dm7', 'G7(♭13)', 'C6'])


if __name__ == '__main__':
    unittest.main()
