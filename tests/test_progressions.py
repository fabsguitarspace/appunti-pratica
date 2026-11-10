"""Independent musical checks for the Progressioni chapter."""
import importlib.util
from pathlib import Path
import unittest
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('progressions',ROOT/'scripts/generate_progressions.py')
p=importlib.util.module_from_spec(spec);spec.loader.exec_module(p)

class ProgressionsTest(unittest.TestCase):
 def test_form_and_rhythm_lengths(self):
  self.assertEqual(len(p.STUDIES),20)
  self.assertEqual(len({s['stem'] for s in p.STUDIES}),20)
  for study in p.STUDIES:
   for bar in study['bars']:self.assertEqual(sum(8//d for key,d in bar),8)
   if 'melody' in study:
    self.assertEqual(len(study['melody']),len(study['bars']))
    for bar in study['melody']:self.assertEqual(sum(8//d for pitch,d in bar),8)
  for number in ['10','11','12']:
   self.assertEqual(len(next(s for s in p.STUDIES if s['stem'].startswith('progressioni-'+number))['bars']),12)
  aaba=next(s for s in p.STUDIES if s['stem']=='progressioni-15-aaba')['bars']
  self.assertEqual(len(aaba),32)
  self.assertEqual(aaba[:8],aaba[8:16]);self.assertEqual(aaba[:8],aaba[24:])
  self.assertNotEqual(aaba[:8],aaba[16:24])

 def test_chord_notes_and_shell_strings(self):
  expected={
   'Cmaj7':{0,4,7,11},'C7':{0,4,7,10},'Cm7':{0,3,7,10},'Cm6':{0,3,7,9},'CmMaj7':{0,3,7,11},
   'Dm7':{2,5,9,0},'G7':{7,11,2,5},'Am7':{9,0,4,7},'A7':{9,1,4,7},'Em7':{4,7,11,2},
   'E7':{4,8,11,2},'D7':{2,6,9,0},'F7':{5,9,0,3},'Fm7':{5,8,0,3},'Bb7':{10,2,5,8},
   'Ab7':{8,0,3,6},'Bbmaj7':{10,2,5,9},'Gmaj7':{7,11,2,6},'Db7':{1,5,8,11},
   'Dhalf':{2,5,8,0},'G7b9':{7,11,2,5,8},'Csdim':{1,4,7,10},'Fsdim':{6,9,0,3},
   'DmPedal':{2,5,9,0},'EmD':{4,7,11,2},
  }
  self.assertEqual(set(p.CHORDS),set(expected))
  for key,chord in p.CHORDS.items():
   with self.subTest(chord=key):
    self.assertLessEqual({v[2]%12 for v in chord['voices']},expected[key])
    self.assertEqual(len({s for s,f,n in chord['voices']}),len(chord['voices']))
    self.assertTrue(all(n==p.OPEN[s]+f for s,f,n in chord['voices']))
    if chord['shell']:
     self.assertEqual(len(chord['voices']),3)
     self.assertIn(tuple(s for s,f,n in chord['voices']),((6,4,3),(5,4,3)))

 def test_guide_tones_and_pedal(self):
  g={n%12 for s,f,n in p.CHORDS['G7']['voices']};db={n%12 for s,f,n in p.CHORDS['Db7']['voices']}
  self.assertEqual(g&db,{5,11})
  self.assertEqual(p.CHORDS['Db7']['spell'][59],"cf'")
  for key in ['DmPedal','EmD']:self.assertEqual(p.CHORDS[key]['voices'][0][2],50)
  self.assertIn(59,[n for s,f,n in p.CHORDS['EmD']['voices']])

 def test_melody_respects_current_chord_except_declared_ninth(self):
  allowed={key:{n%12 for s,f,n in chord['voices']} for key,chord in p.CHORDS.items()}
  # Include omitted chord tones, independently of the chosen shell.
  allowed.update({'Cmaj7':{0,4,7,11},'Am7':{9,0,4,7},'Dm7':{2,5,9,0},'G7':{7,11,2,5},'Em7':{4,7,11,2},'A7':{9,1,4,7}})
  for study in p.STUDIES:
   if 'melody' not in study:continue
   for bar_index,(melody,chords) in enumerate(zip(study['melody'],study['bars'])):
    schedule=[]
    for key,duration in chords:schedule.extend([key]*(8//duration))
    clock=0
    for pitch,duration in melody:
     if pitch is not None:
      if study['stem']=='progressioni-16-frase' and bar_index==2 and clock==7:
       self.assertEqual(pitch,64)  # The explicitly explained ninth of Dm7.
      else:self.assertIn(pitch%12,allowed[schedule[clock]],(study['stem'],bar_index,clock,pitch))
     clock+=8//duration

if __name__=='__main__':unittest.main()
