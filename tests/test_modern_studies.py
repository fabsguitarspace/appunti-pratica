"""Musical invariants and generated MIDI roles for modern/fusion studies.
Run with the music environment (mido required), after generating the assets.
"""
from pathlib import Path
from fractions import Fraction
import importlib.util
import mido
ROOT=Path(__file__).resolve().parents[1]
def module(name):
 spec=importlib.util.spec_from_file_location(name,ROOT/'scripts'/f'{name}.py')
 loaded=importlib.util.module_from_spec(spec);spec.loader.exec_module(loaded);return loaded

g=module('generate_modern_studies')
assert (ROOT/'src/lilypond/sf/PracticeRhythm.sf2').read_bytes()==module('generate_rhythm_soundfont').build()
assert len(g.STUDIES)==12
for study in g.STUDIES:
 beats=Fraction(study['meter'][0]*4,study['meter'][1])
 for index,events in enumerate(study['bars']):
  for part in [events,g.bass(study,index),g.drums(study,index)]:
   assert sum(Fraction(units,4) for pitch,units in part)==beats
  for pitch,units in events:
   if isinstance(pitch,tuple):
    for string,fret,note in pitch:assert g.OPEN[string]+fret==note
 for base in [False,True]:
  stem=study['stem']+('-base' if base else '')
  assert (ROOT/f'src/lilypond/{stem}.ly').read_text()==g.source(study,base=base)
  midi=mido.MidiFile(ROOT/f'src/docs/_static/music/{stem}.midi')
  programs={x.channel:x.program for tr in midi.tracks for x in tr if x.type=='program_change'}
  bass_channels={c for c,p in programs.items() if p==33};assert len(bass_channels)==1
  sounding=[x for tr in midi.tracks for x in tr if x.type=='note_on' and x.velocity>0]
  assert any(x.channel==9 for x in sounding)
  assert any(x.channel in bass_channels for x in sounding)
  assert len({x.channel for x in sounding if x.channel!=9})==(2 if base else 3)
  tempos=[x.tempo for tr in midi.tracks for x in tr if x.type=='set_tempo']
  expected=[750000,500000] if study['number']==10 else [mido.bpm2tempo(study['bpm'])]
  assert len(tempos)==len(expected) and all(abs(a-b)<=1 for a,b in zip(tempos,expected))
  assert max(sum(x.time for x in tr) for tr in midi.tracks)==int((len(study['bars'])+1)*beats*midi.ticks_per_beat)
  # Verify each lead onset, duration and pitch against the common score data.
  if not base:
   lead=next(tr for tr in midi.tracks if any(x.type=='program_change' and x.channel==1 for x in tr))
   clock=0;onsets={};actual=[]
   for x in lead:
    clock+=x.time
    if x.type=='note_on' and x.velocity>0:onsets[x.note]=clock
    elif x.type=='note_off' or (x.type=='note_on' and x.velocity==0):
     actual.append((onsets.pop(x.note),clock,x.note))
   expected_notes=[];position=beats
   for events in study['bars']:
    for pitch,units in events:
     length=Fraction(units,4)
     notes=[] if pitch is None else ([note for string,fret,note in pitch] if isinstance(pitch,tuple) else [pitch])
     for note in notes:expected_notes.append((int(position*midi.ticks_per_beat),int((position+length)*midi.ticks_per_beat),note))
     position+=length
   # LilyPond shortens notes slightly for MIDI articulation; starts and pitches must coincide.
   assert sorted((start,note) for start,end,note in actual)==sorted((start,note) for start,end,note in expected_notes),stem
   for got,want in zip(sorted(actual),sorted(expected_notes)):
    assert 0<=want[1]-got[1]<=midi.ticks_per_beat/8,(stem,got,want)
print('PASS: deterministic samples; 12 studies/12 bases; measures, tuning, source reproducibility, lead notes, rhythm-section roles, count-in and tempo maps')
