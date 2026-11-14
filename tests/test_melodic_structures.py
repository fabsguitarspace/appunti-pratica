"""Musical checks for «Strutture melodiche» (S1–S12) and «Pentatoniche» (P1–P3)."""
import importlib.util
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    'melodic_structures', ROOT / 'scripts/generate_melodic_structures.py')
gen = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gen)
EXAMPLES = {label: (chords, events) for label, _, _, chords, events, _ in gen.EXAMPLES}
ROOTS = {'Cmaj7': 0, 'Cm7': 0, 'Dm7': 2, 'G7': 7, 'C6': 0, 'Am7': 9}
DEGREES = {0: '1', 1: '♭9', 2: '9', 3: '♭3', 4: '3', 5: '11', 6: '♯11', 7: '5',
           8: '♭13', 9: '13', 10: '♭7', 11: '7'}


def bars(events):
    result, current, length = [], [], 0
    for event in events:
        length += 8 // event['duration']
        if event['pitch'] is not None:
            current.append(event)
        if length > 8:
            raise AssertionError('Event crosses a bar line')
        if length == 8:
            result.append(current)
            current, length = [], 0
    if length:
        raise AssertionError('Incomplete final bar')
    return result


def pitches(measure):
    return [e['pitch'] for e in measure]


def degrees(measure, chord):
    return [DEGREES[(e['pitch'] - ROOTS[chord]) % 12] for e in measure]


def classes(measure):
    return {p % 12 for p in pitches(measure)}


class MelodicStructuresTest(unittest.TestCase):
    def test_bar_count_matches_chords_and_register(self):
        for label, (chords, events) in EXAMPLES.items():
            with self.subTest(example=label):
                self.assertEqual(len(bars(events)), len(chords))
                notes = [e['pitch'] for e in events if e['pitch'] is not None]
                self.assertGreaterEqual(min(notes), 60)
                self.assertLessEqual(max(notes), 76)

    def test_s1_same_material_two_orders(self):
        first, second = bars(EXAMPLES['S1'][1])
        self.assertEqual(pitches(first), [60, 62, 64, 67])
        self.assertEqual(pitches(second), [64, 67, 62, 60])

    def test_s2_degrees_on_two_chords(self):
        chords, events = EXAMPLES['S2']
        first, second = bars(events)
        self.assertEqual(degrees(first, chords[0]), ['1', '9', '3', '5'])
        self.assertEqual(degrees(second, chords[1]), ['♭7', '1', '9', '11'])

    def test_s3_octave_shift_and_second_fingering(self):
        measures = bars(EXAMPLES['S3'][1])
        self.assertEqual([p % 12 for p in pitches(measures[1])],
                         [p % 12 for p in pitches(measures[2])])
        self.assertEqual(pitches(measures[2]), pitches(measures[3]))
        self.assertNotEqual([e['string'] for e in measures[2]],
                            [e['string'] for e in measures[3]])
        self.assertEqual(pitches(measures[1])[2] - pitches(measures[1])[1], -5)
        self.assertEqual(pitches(measures[2])[2] - pitches(measures[2])[1], 7)

    def test_s4_same_pitches_different_rhythms(self):
        events = EXAMPLES['S4'][1]
        self.assertTrue(all(pitches(m) == [64, 67, 62, 60] for m in bars(events)))
        rhythms = [tuple(e['duration'] if e['pitch'] else -e['duration'] for e in chunk)
                   for chunk in (events[0:5], events[5:10], events[10:16])]
        self.assertEqual(len(set(rhythms)), 3)
        self.assertEqual(rhythms[2][0], -8)

    def test_s5_structures_and_arrival_on_the_third(self):
        measures = bars(EXAMPLES['S5'][1])
        self.assertEqual(degrees(measures[0], 'Dm7'), ['1', '9', '♭3', '5'])
        self.assertEqual(degrees(measures[1], 'G7'), ['1', '9', '3', '5'])
        self.assertEqual(degrees(measures[2], 'Cmaj7'), ['3', '5', '9', '1'])

    def test_s6_skips_give_one_third_and_four_fourths(self):
        notes = [e['pitch'] for e in EXAMPLES['S6'][1] if e['pitch'] is not None]
        pairs = list(zip(notes[0::2], notes[1::2]))
        self.assertEqual([b - a for a, b in pairs], [4, 5, 5, 5, 5])

    def test_s7_s8_three_structures_a_fifth_apart(self):
        expected = {'S7': ('Cmaj7', [['1', '9', '3', '5'], ['5', '13', '7', '9'],
                                     ['9', '3', '♯11', '13']]),
                    'S8': ('Cm7', [['1', '♭3', '11', '5'], ['5', '♭7', '1', '9'],
                                   ['9', '11', '5', '13']])}
        for label, (chord, rows) in expected.items():
            measures = bars(EXAMPLES[label][1])
            with self.subTest(example=label):
                self.assertEqual([degrees(m, chord) for m in measures], rows)
                base = pitches(measures[0])
                # 5–9 is the 1–5 shape transposed up a fifth.
                self.assertEqual([p - base[0] for p in base],
                                 [p - pitches(measures[1])[0] for p in pitches(measures[1])])

    def test_s9_four_permutations_one_per_starting_note(self):
        measures = bars(EXAMPLES['S9'][1])
        self.assertTrue(all(classes(m) == {0, 2, 4, 7} for m in measures))
        self.assertEqual({m[0]['pitch'] % 12 for m in measures}, {0, 2, 4, 7})

    def test_s10_linear_inversions(self):
        measures = bars(EXAMPLES['S10'][1])
        lowest = [min(pitches(m)) % 12 for m in measures]
        self.assertEqual(lowest, [0, 2, 4, 7])
        for m in measures:
            self.assertEqual(degrees(m, 'Cmaj7'), ['9', '5', '3', '1'])

    def test_s11_common_tones_between_chords(self):
        measures = bars(EXAMPLES['S11'][1])
        self.assertEqual(measures[0][-1]['pitch'], measures[1][0]['pitch'])
        self.assertEqual(measures[1][-1]['pitch'], measures[2][0]['pitch'])
        self.assertEqual(sorted(degrees(measures[1], 'G7')), sorted(['5', '13', '♭7', '9']))
        self.assertEqual(measures[3][0]['pitch'] % 12, 4)

    def test_s12_guide_tone_structure(self):
        first, second = bars(EXAMPLES['S12'][1])
        self.assertEqual(degrees(first, 'Cmaj7'), ['3', '5', '13', '7'])
        self.assertEqual(degrees(second, 'Cm7'), ['♭3', '11', '5', '♭7'])

    def test_p1_formula_on_a_minor_pentatonic(self):
        notes = [e['pitch'] for e in EXAMPLES['P1'][1] if e['pitch'] is not None]
        self.assertTrue({p % 12 for p in notes} <= {9, 0, 2, 4, 7})
        groups = [notes[i:i + 4] for i in range(0, 20, 4)]
        coll = gen.A_MINOR_PENT
        for g in groups:
            idx = [coll.index(p) for p in g]
            self.assertEqual([i - idx[0] for i in idx], [0, 1, 3, 2])
        self.assertEqual([coll.index(g[0]) for g in groups], [4, 3, 2, 1, 0])
        self.assertEqual(notes[-1], 60)

    def test_p2_three_minor_pentatonics_on_dm7(self):
        measures = bars(EXAMPLES['P2'][1])
        roots = [2, 9, 4]
        for m, r in zip(measures, roots):
            self.assertTrue(classes(m) <= {(r + i) % 12 for i in (0, 3, 5, 7, 10)})
        self.assertIn('13', degrees(measures[2], 'Dm7'))

    def test_p3_altered_pentatonic_on_the_dominant(self):
        measures = bars(EXAMPLES['P3'][1])
        b_flat_major_flat2 = {10, 11, 2, 5, 7}
        self.assertTrue(classes(measures[1]) <= b_flat_major_flat2)
        self.assertEqual(set(degrees(measures[1], 'G7')), {'1', '♭3', '3', '5', '♭7'})
        self.assertEqual(measures[1][-1]['pitch'], 65)   # Fa, the seventh of G7 ...
        self.assertEqual(measures[2][0]['pitch'], 64)    # ... resolves to Mi
        self.assertEqual(measures[3][0]['pitch'] % 12, 4)

    def test_pages_reference_every_generated_asset(self):
        pages = ''.join((ROOT / f'src/docs/{name}.rst').read_text()
                        for name in ('strutture-melodiche', 'pentatoniche'))
        referenced = set(re.findall(r'_static/music/((?:strutture|pentatoniche)-[0-9a-z-]+)\.(?:mp3|\*)', pages))
        expected = set()
        for _, stem, _, _, _, base in gen.EXAMPLES:
            for _, suffix in gen.TEMPI:
                expected.add(f'{stem}{suffix}')
                if base:
                    expected.add(f'{stem}-base{suffix}')
        self.assertEqual(referenced, expected)
        for name in expected:
            self.assertTrue((ROOT / f'src/lilypond/{name}.ly').is_file(), name)
            self.assertTrue((ROOT / f'src/docs/_static/music/{name}.mp3').is_file(), name)


if __name__ == '__main__':
    unittest.main()
