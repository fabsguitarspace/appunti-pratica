"""Musical checks for the new original arpeggio studies (no external tools)."""
import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('arpeggio_studies', ROOT / 'scripts/generate_arpeggio_exercises.py')
studies = importlib.util.module_from_spec(spec)
spec.loader.exec_module(studies)


def bars(events):
    result, current, length = [], [], 0
    for event in events:
        length += 8 // event['duration']
        if event['pitch'] is not None:
            current.append(event)
        if length > 8:
            raise AssertionError('Event crosses a bar without notation for a tie')
        if length == 8:
            result.append(current)
            current, length = [], 0
    if length:
        raise AssertionError('Incomplete final bar')
    return result


class ArpeggioStudiesTest(unittest.TestCase):
    def test_notes_belong_to_the_indicated_chord(self):
        cmaj = {0,4,7,11}
        c6, c7 = {0,4,7,9}, {0,4,7,10}
        cm6, cm7, cmmaj = {0,3,7,9}, {0,3,7,10}, {0,3,7,11}
        major_progression = [{2,5,9,0}, {7,11,2,5}, cmaj, cmaj]
        minor_progression = [{2,5,8,0}, {7,11,2,5,8}, cm6, cm6]
        allowed = [
            [cmaj]*4, [cmaj]*4, [c6,c7,cmaj,c6], [cm6,cm7,cmmaj,cm6],
            [cmaj]*4, [{0,4,7,11,2},{0,4,7,10,2},{0,3,7,10,2},{0,3,7,11,2}],
            [{0,4,8,10}]*2 + [{0,3,6,9}]*2, [cmaj]*8,
            major_progression*2, minor_progression*2,
        ]
        for number, ((title,events), chords) in enumerate(zip(studies.STUDIES, allowed), 1):
            with self.subTest(study=number, title=title):
                measures = bars(events)
                self.assertEqual(len(measures),len(chords))
                for measure,chord in zip(measures,chords):
                    self.assertLessEqual({e['pitch'] % 12 for e in measure},chord)

    def test_repeated_line_preserves_actual_pitches_across_positions(self):
        measures = bars(studies.STUDIES[4][1])
        self.assertEqual([e['pitch'] for e in measures[0]], [e['pitch'] for e in measures[2]])
        self.assertNotEqual([e['string'] for e in measures[0]], [e['string'] for e in measures[2]])
        # The transition uses the same C4 on two strings, as described in the text.
        self.assertEqual(measures[1][-1]['pitch'],60)
        self.assertEqual(measures[2][0]['pitch'],60)

    def test_guide_tones_at_harmonic_boundaries(self):
        for number, expected in [(8,[(72,71),(65,64)]),(9,[(72,71),(71,72)])]:
            measures = bars(studies.STUDIES[number][1])
            for offset in (0,4):
                for boundary,pair in enumerate(expected):
                    self.assertEqual((measures[offset+boundary][-1]['pitch'],
                                      measures[offset+boundary+1][0]['pitch']), pair)

    def test_altered_fifth_and_diminished_seventh_spelling(self):
        measures = bars(studies.STUDIES[6][1])
        for measure in measures[:2]:
            self.assertTrue(all(e['name']=="gs'" for e in measure if e['pitch']==68))
        for measure in measures[2:]:
            self.assertTrue(all(e['name']=="bff'" for e in measure if e['pitch']==69))


if __name__ == '__main__':
    unittest.main()
