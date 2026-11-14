"""Musical checks for the examples of «Strutture melodiche» (no external tools)."""
import importlib.util
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    'melodic_structures', ROOT / 'scripts/generate_melodic_structures.py')
gen = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gen)
EXAMPLES = {number: (chords, events) for number, _, chords, events in gen.EXAMPLES}
ROOTS = {'Cmaj7': 0, 'Dm7': 2, 'G7': 7, 'C6': 0}
DEGREES = {0: '1', 2: '9', 3: '♭3', 4: '3', 5: '11', 7: '5', 9: '13', 10: '♭7', 11: '7'}


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


class MelodicStructuresTest(unittest.TestCase):
    def test_bar_count_matches_chords_and_register(self):
        for number, (chords, events) in EXAMPLES.items():
            with self.subTest(example=number):
                self.assertEqual(len(bars(events)), len(chords))
                notes = [e['pitch'] for e in events if e['pitch'] is not None]
                self.assertGreaterEqual(min(notes), 60)
                self.assertLessEqual(max(notes), 74)

    def test_s1_same_material_two_orders(self):
        first, second = bars(EXAMPLES[1][1])
        self.assertEqual(pitches(first), [60, 62, 64, 67])
        self.assertEqual(pitches(second), [64, 67, 62, 60])
        self.assertEqual(set(pitches(first)), set(pitches(second)))

    def test_s2_degrees_on_two_chords(self):
        chords, events = EXAMPLES[2]
        first, second = bars(events)
        self.assertEqual(degrees(first, chords[0]), ['1', '9', '3', '5'])
        self.assertEqual(degrees(second, chords[1]), ['♭7', '1', '9', '11'])

    def test_s3_octave_shift_and_second_fingering(self):
        measures = bars(EXAMPLES[3][1])
        self.assertEqual([p % 12 for p in pitches(measures[1])],
                         [p % 12 for p in pitches(measures[2])])
        self.assertEqual(pitches(measures[2]), pitches(measures[3]))
        self.assertNotEqual([e['string'] for e in measures[2]],
                            [e['string'] for e in measures[3]])
        # Second bar descends a fourth to Re, third bar leaps a fifth.
        self.assertEqual(pitches(measures[1])[2] - pitches(measures[1])[1], -5)
        self.assertEqual(pitches(measures[2])[2] - pitches(measures[2])[1], 7)

    def test_s4_same_pitches_different_rhythms(self):
        events = EXAMPLES[4][1]
        measures = bars(events)
        self.assertTrue(all(pitches(m) == [64, 67, 62, 60] for m in measures))
        rhythms = [tuple(e['duration'] if e['pitch'] else -e['duration'] for e in chunk)
                   for chunk in (events[0:5], events[5:10], events[10:16])]
        self.assertEqual(len(set(rhythms)), 3)
        self.assertEqual(rhythms[2][0], -8)  # third bar enters after an eighth rest

    def test_s5_structures_and_arrival_on_the_third(self):
        chords, events = EXAMPLES[5]
        measures = bars(events)
        self.assertEqual(degrees(measures[0], 'Dm7'), ['1', '9', '♭3', '5'])
        self.assertEqual(degrees(measures[1], 'G7'), ['1', '9', '3', '5'])
        self.assertEqual(degrees(measures[2], 'Cmaj7'), ['3', '5', '9', '1'])
        self.assertEqual(measures[2][0]['pitch'] % 12, 4)
        self.assertIn(65, pitches(measures[0]))
        self.assertIn(71, pitches(measures[1]))

    def test_s6_every_other_note_gives_one_third_and_four_fourths(self):
        notes = [e['pitch'] for e in EXAMPLES[6][1] if e['pitch'] is not None]
        pairs = list(zip(notes[0::2], notes[1::2]))
        self.assertEqual([b - a for a, b in pairs], [4, 5, 5, 5, 5])
        self.assertTrue({p % 12 for p in notes} <= {0, 2, 4, 7, 9})

    def test_page_references_every_generated_asset(self):
        page = (ROOT / 'src/docs/strutture-melodiche.rst').read_text()
        referenced = set(re.findall(r'_static/music/(strutture-[0-9a-z-]+)\.(?:mp3|\*)', page))
        expected = set()
        for number in EXAMPLES:
            for _, suffix in gen.TEMPI:
                expected.add(f'strutture-{number:02}{suffix}')
                if number in gen.WITH_BASE:
                    expected.add(f'strutture-{number:02}-base{suffix}')
        images = {name for name in expected if '-90' not in name and 'base' not in name}
        self.assertEqual(referenced, expected | images)
        for name in expected:
            self.assertTrue((ROOT / f'src/lilypond/{name}.ly').is_file(), name)


if __name__ == '__main__':
    unittest.main()
