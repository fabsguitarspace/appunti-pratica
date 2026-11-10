"""Musical invariants of the three-voice shell collection."""
import importlib.util
from pathlib import Path
import unittest
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('shells',ROOT/'scripts/generate_shell_voicings.py')
shells=importlib.util.module_from_spec(spec);spec.loader.exec_module(shells)

class ShellVoicingsTest(unittest.TestCase):
 def test_three_voices_and_chord_tone_basses(self):
  self.assertEqual(len(shells.SHEETS),7)
  for stem,title,chords in shells.SHEETS:
   for chord in chords:
    voices=chord['voices'];label=chord['label']
    self.assertEqual(len(voices),3,(stem,label))
    self.assertEqual(len({s for s,f,p in voices}),3)
    self.assertEqual([p for s,f,p in voices],sorted(p for s,f,p in voices))
    self.assertTrue(all(f>0 and p==shells.OPEN[s]+f for s,f,p in voices))
    root=2 if label.startswith('D') else 7 if label.startswith('G') else 0
    bass=(voices[0][2]-root)%12
    allowed={0,3,7} if label.startswith(('Cm','Dm')) and not label.startswith('Cmaj') else {0,4,7}
    if 'b5' in label:allowed={0,3,6}
    self.assertIn(bass,allowed,(stem,label))

 def test_only_the_two_requested_string_sets(self):
  for stem,title,chords in shells.SHEETS:
   for chord in chords:
    self.assertIn(tuple(s for s,f,p in chord['voices']),((6,4,3),(5,4,3)),(stem,chord))
  for frets in [[(4,2),(3,4),(2,1)],[(6,3),(3,4),(2,5)]]:
   with self.assertRaises(AssertionError):shells.chord('invalid',frets)

 def test_guide_tones_in_major_cadence(self):
  chords=next(c for stem,title,c in shells.SHEETS if stem=='shell-ii-v-i-maggiore')
  self.assertEqual([[p for s,f,p in c['voices']][1:] for c in chords[:3]],[[53,60],[53,59],[52,59]])

 def test_half_diminished_ambiguity_and_fifth(self):
  chords=next(c for stem,title,c in shells.SHEETS if stem=='shell-semidiminuito')
  self.assertEqual(chords[0]['voices'],chords[1]['voices'])
  pcs={p%12 for s,f,p in chords[2]['voices']}
  self.assertEqual(pcs,{8,0,5})
  self.assertNotIn(2,pcs)

if __name__=='__main__':unittest.main()
