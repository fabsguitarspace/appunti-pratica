"""Musical and guitar constraints for the advanced chord vocabulary."""
import importlib.util
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('chord_vocabulary',ROOT/'scripts/generate_chord_vocabulary.py')
vocab = importlib.util.module_from_spec(spec)
spec.loader.exec_module(vocab)


class ChordVocabularyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entries=vocab.catalogue()

    def test_coverage_and_fixed_soprano(self):
        self.assertEqual(len(self.entries),38)
        self.assertEqual(len({e['stem'] for e in self.entries}),38)
        for e in self.entries:
            self.assertEqual(len(e['shapes']),3)
            for shape in e['shapes']:
                self.assertEqual(shape['voices'][-1],
                                 (e['top_string'],e['top_pitch']-vocab.OPEN[e['top_string']],e['top_pitch']))
                self.assertTrue(all(p<e['top_pitch'] for s,f,p in shape['voices'][:-1]))

    def test_shapes_are_valid_four_note_guitar_voicings(self):
        for e in self.entries:
            with self.subTest(stem=e['stem']):
                for shape in e['shapes']:
                    voices=shape['voices']
                    self.assertEqual(len(voices),4)
                    self.assertEqual(len({s for s,f,p in voices}),4)
                    frets=[f for s,f,p in voices]
                    self.assertGreaterEqual(min(frets),1)
                    self.assertLessEqual(max(frets)-min(frets),4)
                    self.assertTrue(all(p==vocab.OPEN[s]+f for s,f,p in voices))
                    allowed,required=shape['chord'][1:]
                    pcs={(p-e['root'])%12 for s,f,p in voices}
                    self.assertLessEqual(pcs,allowed)
                    self.assertLessEqual(required,pcs)

    def test_thirds_sevenths_and_suspensions(self):
        for e in self.entries:
            for shape in e['shapes']:
                suffix=shape['chord'][0]
                pcs={(p-e['root'])%12 for s,f,p in shape['voices']}
                if e['family']=='minore':
                    self.assertIn(3,pcs)
                    self.assertNotIn(4,pcs)
                    self.assertIn(11 if 'maj' in suffix else 9 if suffix.startswith('m6') else 10,pcs)
                else:
                    self.assertIn(10,pcs)
                    if 'sus4' in suffix:
                        self.assertIn(5,pcs)
                        self.assertNotIn(4,pcs)
                    else:
                        self.assertIn(4,pcs)

    def test_extensions_do_not_appear_in_the_bass(self):
        for entry in self.entries:
            allowed = {0, 3, 7, 10, 11} if entry['family'] == 'minore' else {0, 4, 7, 10}
            for shape in entry['shapes']:
                interval = (shape['voices'][0][2] - entry['root']) % 12
                self.assertIn(interval, allowed, (entry['stem'], shape))

    def test_notated_pitches_match_frets_including_alterations(self):
        natural={'c':0,'d':2,'e':4,'f':5,'g':7,'a':9,'b':11}
        for e in self.entries:
            for shape in e['shapes']:
                for voice in shape['voices']:
                    text=vocab.lily_note(e,voice)
                    match=re.fullmatch(r"([a-g])(f|s)?([',]*)\\([1-6])",text)
                    self.assertIsNotNone(match,text)
                    letter,accidental,octaves,string=match.groups()
                    pitch=48+natural[letter]+(1 if accidental=='s' else -1 if accidental=='f' else 0)
                    pitch+=12*(octaves.count("'")-octaves.count(','))
                    self.assertEqual(pitch,voice[2],text)
                    self.assertEqual(int(string),voice[0])
                    if e['family']=='dominante' and (pitch-e['root'])%12==3:
                        self.assertEqual(letter,'d' if e['root_name']=='c' else 'g')
                        self.assertEqual(accidental,'s')


if __name__=='__main__':
    unittest.main()
