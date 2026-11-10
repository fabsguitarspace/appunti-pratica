"""Count, musical context, fingering, timing and linkage invariants for 50 licks."""
import importlib.util
from pathlib import Path
from fractions import Fraction
from collections import Counter
import re
import unittest
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('bebop',ROOT/'scripts/generate_bebop_licks.py')
b=importlib.util.module_from_spec(spec);spec.loader.exec_module(b)

class BebopLicksTest(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.licks=b.catalogue()

 def test_fifty_distinct_authored_phrases(self):
  self.assertEqual(len(self.licks),50)
  self.assertEqual(Counter(l['category'] for l in self.licks),dict.fromkeys('MNDPB',10))
  self.assertEqual(len({l['id'] for l in self.licks}),50)
  self.assertEqual(len({tuple(tuple(bar) for bar in l['bars']) for l in self.licks}),50)
  for lick in self.licks:
   self.assertEqual(len(lick['bars']),2 if lick['category'] in 'MND' else 4)
   self.assertEqual(len(lick['keys']),len(lick['bars']))
   for key,bar in zip(lick['keys'],lick['bars']):
    self.assertIn(key,b.BACKING);self.assertEqual(sum(u for p,u in bar),8)

 def test_explicit_tablature_and_notation_pitch(self):
  natural={'c':0,'d':2,'e':4,'f':5,'g':7,'a':9,'b':11}
  for lick in self.licks:
   for key,bar in zip(lick['keys'],lick['bars']):
    for pitch,units in bar:
     if pitch is None:continue
     string,fret=b.finger(pitch)
     self.assertEqual(b.OPEN[string]+fret,pitch)
     self.assertTrue(2<=fret<=20)
     spelling=b.spelling(lick,pitch,key)
     m=re.fullmatch(r"([a-g])((?:f|s){0,2})([',]*)",spelling)
     self.assertIsNotNone(m,spelling)
     letter,accidentals,octave=m.groups()
     actual=48+natural[letter]+accidentals.count('s')-accidentals.count('f')+12*(octave.count("'")-octave.count(','))
     self.assertEqual(actual,pitch,(lick['id'],spelling,pitch))

 def test_swing_preserves_bars_and_two_to_one_ratio(self):
  self.assertEqual(b.swing_position(1),Fraction(2,3))
  self.assertEqual(b.swing_position(2),1)
  self.assertEqual(b.swing_position(8),4)
  self.assertEqual(b.swing_position(1)/(b.swing_position(2)-b.swing_position(1)),2)
  for lick in self.licks:
   for bar in lick['bars']:
    slot=0;total=Fraction(0)
    for pitch,units in bar:
     delta=b.swing_position(slot+units)-b.swing_position(slot)
     self.assertGreater(delta,0);total+=delta;slot+=units
    self.assertEqual(total,4)

 def test_final_targets_and_enclosures(self):
  tones={'Cmaj7':{0,4,7,11},'C6':{0,4,7,9},'Cm7':{0,3,7,10},'Cm6':{0,3,7,9},
         'CmMaj7':{0,3,7,11},'G7':{7,11,2,5},'G7b9':{7,11,2,5,8},'A7':{9,1,4,7},
         'Fm7':{5,8,0,3},'Bbmaj7':{10,2,5,9},'C7':{0,4,7,10}}
  for lick in self.licks:
   last=next(p for p,u in reversed(lick['bars'][-1]) if p is not None)
   self.assertIn(last%12,tones[lick['keys'][-1]],lick['id'])
  by_id={l['id']:l for l in self.licks}
  self.assertEqual([p for p,u in by_id['M02']['bars'][0][:3]],[65,63,64])
  self.assertEqual([p for p,u in by_id['D02']['bars'][0][:3]],[72,70,71])
  self.assertEqual(b.spelling(by_id['P07'],71,'Db7'),"cf''")

 def test_progression_routes_and_blues_windows(self):
  progress=(ROOT/'src/docs/7-progressioni.rst').read_text()
  chapter=(ROOT/'src/docs/8-licks.rst').read_text()
  for lick in self.licks:
   self.assertIn(f".. _{lick['link']}:",progress)
   self.assertIn(f".. _lick-{lick['id'].lower()}:",chapter)
  by_id={l['id']:l for l in self.licks}
  self.assertEqual(by_id['P01']['keys'],['Dm7','G7','Cmaj7','Cmaj7'])
  self.assertEqual(by_id['B01']['keys']+by_id['B03']['keys']+by_id['B04']['keys'],
                   ['C7']*4+['F7','F7','C7','C7','G7','F7','C7','G7'])
  self.assertEqual(by_id['N03']['keys'],['Cm6','Cm6'])
  self.assertEqual(by_id['P03']['keys'][2:],by_id['N03']['keys'])

if __name__=='__main__':unittest.main()
