"""Verify the 60 artist studies and ten practice bases after the music build."""
from pathlib import Path
from fractions import Fraction as F
import sys
import mido
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
import generate_artist_studies as g
from artist_profiles import PROFILES
assert len(PROFILES)==10 and len(g.STUDIES)==60
assert all(len(group)==6 and [s['number'] for s in group]==list(range(1,7)) for group in g.GROUPS)

def pitches(p):return [] if p is None else [n for string,fret,n in p] if isinstance(p,tuple) else [p]
def fingerings(p):return [] if p is None else list(p) if isinstance(p,tuple) else [g.single_finger(p)]
def timeline(s,bars):
 result=[];position=F(0)
 for events in bars:
  for pitch,units in events:
   a=g.swing_position(position) if s['swing'] else position
   b=g.swing_position(position+units) if s['swing'] else position+units
   result.extend((a,b,n) for n in pitches(pitch));position+=units
 return result
for s in g.STUDIES:
 units=F(s['meter'][0]*16,s['meter'][1]);beats=units/4
 for i,bar in enumerate(s['bars']):
  assert sum(u for p,u in bar)==units
  assert sum(u for p,u in g.music.bass(s,i))==units
  assert sum(u for p,u in g.music.drums(s,i))==units
  for p,u in bar:
   g.guitar_pitch(p,s['keys'][i]) if p is not None else None
  if s['lower']:assert sum(u for p,u in s['lower'][i])==units
  # Simultaneous guitar notes use distinct strings, with at most four frets of span.
  voices=[bar]+([s['lower'][i]] if s['lower'] else [])
  moments=[]
  for voice in voices:
   position=0
   for pitch,u in voice:
    moments.append((position,position+u,fingerings(pitch)));position+=u
  for point in sorted({x for start,end,notes in moments for x in (start,end)}):
   active=[note for start,end,notes in moments if start<=point<end for note in notes]
   strings=[st for st,fret,n in active];frets=[f for st,f,n in active if f]
   assert len(strings)==len(set(strings)),(s['stem'],i,point,'string collision')
   assert not frets or max(frets)-min(frets)<=4,(s['stem'],i,point,active)
 for base in ([False,True] if s['number']==6 else [False]):
  stem=s['stem']+('-base' if base else '')
  assert (ROOT/f'src/lilypond/{stem}.ly').read_text()==g.source(s,base)
  m=mido.MidiFile(ROOT/f'src/docs/_static/music/{stem}.midi');ticks=m.ticks_per_beat
  assert max(sum(x.time for x in tr) for tr in m.tracks)==int((len(s['bars'])+1)*beats*ticks),stem
  sounding=[x for tr in m.tracks for x in tr if x.type=='note_on' and x.velocity]
  channels={x.channel for x in sounding if x.channel!=9}
  assert len(channels)==(0 if base and s['solo'] else 1 if s['solo'] else 2 if base else 3),(stem,channels)
  tempos=[x.tempo for tr in m.tracks for x in tr if x.type=='set_tempo']
  assert len(tempos)==1 and abs(tempos[0]-mido.bpm2tempo(s['bpm']))<=1
  if not base:
   lead=next(tr for tr in m.tracks if any(x.type=='program_change' and x.channel==1 for x in tr))
   clock=0;active={};actual=[]
   for msg in lead:
    clock+=msg.time
    if msg.type=='note_on' and msg.velocity:
     assert msg.note not in active,(stem,'overlapping MIDI pitch',msg.note)
     active[msg.note]=clock
    elif msg.type=='note_off' or (msg.type=='note_on' and not msg.velocity):
     actual.append((active.pop(msg.note),clock,msg.note))
   expected=timeline(s,s['bars'])+(timeline(s,s['lower']) if s['lower'] else [])
   expected=sorted((int((a/4+beats)*ticks),int((b/4+beats)*ticks),n) for a,b,n in expected)
   assert sorted((a,n) for a,b,n in actual)==[(a,n) for a,b,n in expected],stem
   for got,want in zip(sorted(actual),expected):
    assert 0<=want[1]-got[1]<=ticks/8,(stem,got,want)
  # Verify that solo audio has no rhythm events after the count-in; its base has clicks throughout.
  drum_onsets=[]
  for tr in m.tracks:
   clock=0
   for msg in tr:
    clock+=msg.time
    if msg.type=='note_on' and msg.velocity and msg.channel==9:drum_onsets.append(clock)
  assert len([t for t in drum_onsets if t<beats*ticks])==s['meter'][0]
  assert any(t>=beats*ticks for t in drum_onsets)==(not s['solo'] or base)
print('PASS: 60 studies/10 bases; measures, string tuning, playable spans, simultaneous voices, exact lead onsets/pitches, swing maps, MIDI roles, count-ins and solo backing behavior')
