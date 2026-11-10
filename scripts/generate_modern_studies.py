#!/usr/bin/env python3
"""Twelve original modern/fusion studies and rhythm-section practice versions.

Run this script, then build modern-* with:
./build-lilypond.sh --soundfont-overlay src/lilypond/sf/PracticeRhythm.sf2 --source NAME
Generate the original rhythm SoundFont using generate_rhythm_soundfont.py first.
Notation, guitar TAB, bass and drums derive from the same rational event data.
"""
from pathlib import Path
from fractions import Fraction as F
from math import ceil
ROOT=Path(__file__).resolve().parents[1]
OPEN={6:40,5:45,4:50,3:55,2:59,1:64}
NAMES={0:'c',1:'df',2:'d',3:'ef',4:'e',5:'f',6:'fs',7:'g',8:'af',9:'a',10:'bf',11:'b'}
Q0=((5,5,50),(4,5,55),(3,5,60),(2,6,65))
Q1=((5,5,50),(4,7,57),(3,7,62),(2,8,67))
PADS={
 'Dm7':(38,(50,53,60),'Dm7'),
 'Dm11':(38,(50,53,60),'Dm11'),
 'EmD':(38,(50,55,59,64),'Em7/D'),
 'Clyd':(36,(48,52,59),'Cmaj7(#11)'),
 'Eblyd':(39,(51,55,62),'Ebmaj7(#11)'),
 'Ablyd':(44,(44,55,60),'Abmaj7(#11)'),
 'Dblyd':(37,(49,53,60),'Dbmaj7(#11)'),
}

def bar(*items):return [(x,2) if not isinstance(x,tuple) else x for x in items]
def held(p,u):return (p,u)
def study(n,title,keys,bars,style='modern',meter=(4,4),groups=None,bpm=80,tempo_change=None,accents=False):
 length=F(meter[0]*4,meter[1])
 for i,events in enumerate(bars):
  assert sum(F(u,4) for p,u in events)==length,(n,i,events)
 return dict(number=n,stem=f'modern-{n:02}',title=title,keys=keys,bars=bars,style=style,meter=meter,
             groups=groups,bpm=bpm,tempo_change=tempo_change,accents=accents)

MODAL=[bar(64,67,71,74,72,71,69,67),bar(65,64,62,60,59,60,(62,4)),
       bar(64,67,71,74,71,69,67,64),bar(65,64,(62,8),(None,4))]
FUSION=[bar((None,1),(64,1),67,71,74,72,(71,1),(69,1),67,64),
        bar(65,(64,1),(62,1),60,62,64,67,(62,4)),
        bar((None,2),(64,1),(67,1),71,74,(72,1),(71,1),69,67,64),
        bar(65,64,(62,8),(None,4))]
STUDIES=[
 study(1,'Dal bebop al vamp dorico',['Dm7','EmD','Dm7','EmD'],MODAL),
 study(2,'Stessa cellula: sedicesimi e groove',['Dm7']*4,FUSION,style='fusion'),
 study(3,'Strutture per quarte sul pedale di Re',['Dm11']*4,
       [[held(Q0,16)],[held(Q1,16)],[held(Q0,16)],[held(Q1,8),held(Q0,8)]]),
 study(4,'Triade di Re sopra Do: 9, #11, 13',['Clyd']*4,
       [bar(62,66,69,74,71,69,66,64),bar(62,66,69,72,71,67,64,60),[(62,4),(66,4),(69,4),(74,4)],bar(64,67,71,72,71,69,66,64)]),
 study(5,'Pentatonica di Mi minore sopra Re minore',['Dm7']*4,
       [bar(64,67,69,71,74,71,69,67),bar(62,64,67,69,71,69,67,64),bar(74,71,69,67,64,67,69,71),bar(67,64,(62,8),(None,4))]),
 study(6,'Side-slip: una cellula fuori e ritorno',['Dm7']*4,
       [bar(64,67,69,71,74,71,69,67),bar(64,67,69,71,65,68,70,72),bar(64,67,69,71,74,71,69,67),bar(65,64,(62,8),(None,4))]),
 study(7,'Gruppi di tre dentro quattro',['Dm7']*4,
       [bar(*[ [64,67,71][(i*8+j)%3] for j in range(8)]) for i in range(3)]+[[held(62,16)]],accents=True),
 study(8,'Cinque quarti: tre piu due',['Dm7']*4,
       [bar(64,67,71,74,72,69,67,64,65,62),bar(62,64,65,69,71,72,71,69,67,64),
        bar(64,67,71,74,71,69,67,65,64,62),[(64,4),(67,4),(71,4),(69,4),(62,4)]],
       style='five',meter=(5,4),groups=(3,2)),
 study(9,'Sette ottavi: due piu due piu tre',['Dm7']*4,
       [bar(64,67,71,74,72,69,62),bar(65,64,62,60,59,60,62),bar(64,67,71,74,71,67,64),[(62,4),(65,4),(64,2),(62,4)]],
       style='seven',meter=(7,8),groups=(2,2,3),bpm=84),
 study(10,'Modulazione metrica: la terzina diventa pulsazione',['Dm7']*4,
       [[(p,F(8,3)) for p in [64,67,71,74,71,67]],[(p,F(8,3)) for p in [65,69,72,76,74,72]],
        [(p,4) for p in [64,67,71,74]],[(65,4),(64,4),(62,8)]],tempo_change=(2,120)),
 study(11,'Studio fusion: forma di otto battute',['Dm7','Dm7','EmD','EmD','Dm7','Dm7','EmD','Dm7'],
       FUSION[:3]+[bar(64,67,71,74,72,71,67,64)]+[FUSION[0],
       bar(64,67,71,74,72,69,(65,1),(68,1),(70,1),(75,1)),bar(64,67,71,74,71,69,67,64),FUSION[3]],style='fusion'),
 study(12,'Strutture superiori su centri diversi',['Clyd','Eblyd','Ablyd','Dblyd'],
       [bar(62,66,69,74,72,69,67,64),bar(65,69,72,77,75,72,70,67),
        bar(58,62,65,70,68,65,63,60),bar(63,67,70,75,73,70,68,65)]),
]
DRUM_NAMES={36:'bd',38:'sn',42:'hh',51:'cymr'}

def bass(study,index):
 root=PADS[study['keys'][index]][0]
 if study['style']=='five':return [(root,4),(root+7,2),(root+10,2),(root+12,4),(root,4),(root+7,4)]
 if study['style']=='seven':return [(root,4),(root+7,4),(root+10,2),(root+12,4)]
 if study['style']=='fusion':return [(root,2),(None,1),(root,1),(root+7,2),(root+12,2),(None,2),(root,2),(root+7,2),(root+12,2)]
 return [(root,4),(root+7,4),(root+12,4),(root+7,4)]

def drums(study,index):
 units=int(F(study['meter'][0]*16,study['meter'][1]));style=study['style'];events=[]
 for slot in range(units):
  notes=[]
  if style=='fusion':
   notes.append(42)
   if slot in (0,3,8,10):notes.append(36)
   if slot in (4,12):notes.append(38)
  elif style=='five':
   if slot%2==0:notes.append(42)
   if slot in (0,12):notes.append(36)
   if slot in (8,16):notes.append(38)
  elif style=='seven':
   if slot%2==0:notes.append(42)
   if slot in (0,8):notes.append(36)
   if slot==4:notes.append(38)
  else:
   if slot%2==0:notes.append(51)
   if slot in (0,8):notes.append(36)
   if slot in (4,12):notes.append(38)
  if not notes and events and slot%4:
   previous,units=events[-1];events[-1]=(previous,units+1)
  else:events.append((tuple(sorted(notes)) if notes else None,1))
 return events

def pname(p):
 shift=p//12-4
 return NAMES[p%12]+("'"*shift if shift>=0 else ','*(-shift))
def duration(u):
 names={1:'16',2:'8',3:'8.',4:'4',6:'4.',8:'2',12:'2.',14:'2..',16:'1',20:'1*5/4'}
 return names[u]
def guitar_note(p):
 if isinstance(p,tuple):return '<'+' '.join(pname(n)+f'\\{s}' for s,f,n in p)+'>'
 if p<55:s=5
 elif p<60:s=4
 elif p<=63:s=3
 elif p<=68:s=2
 else:s=1
 fret=p-OPEN[s];assert 1<=fret<=20,(p,s,fret)
 return pname(p)+f'\\{s}'
def with_duration(token,u):
 if token.startswith('<'):return token+duration(u)
 if '\\' in token:
  pitch,string=token.split('\\');return pitch+duration(u)+'\\'+string
 return token+duration(u)

def melody(study):
 lines=[];count=0
 for index,events in enumerate(study['bars']):
  tokens=[];triplet=study['number']==10 and index<2
  if triplet:
   for offset in (0,3):
    tokens.append('\\tuplet 3/2 { '+' '.join(with_duration(guitar_note(p),4) for p,u in events[offset:offset+3])+' }')
  else:
   for j,(p,u) in enumerate(events):
    token=with_duration('r' if p is None else guitar_note(p),u)
    if study['accents'] and count%3==0 and p is not None:token+='->'
    tokens.append(token);count+=1
  # Attach chord labels to the first event/tuplet group without changing note timing.
  label=PADS[study['keys'][index]][2]
  tokens[0]+=f'^\\markup {{ \\small "{label}" }}'
  lines.append(' '.join(tokens)+' |'+(' \\break' if (index+1)%4==0 and index+1<len(study['bars']) else ''))
 return '\n'.join(lines)

def rhythmic_part(study,kind):
 lines=[]
 for i,key in enumerate(study['keys']):
  if kind=='pad':
   token='<'+ ' '.join(pname(p) for p in PADS[key][1])+'>'
   units=F(study['meter'][0]*16,study['meter'][1]);lines.append(token+'1*'+str(units/16)+' |');continue
  events=bass(study,i) if kind=='bass' else drums(study,i);tokens=[]
  for p,u in events:
   if p is None:token='r'
   elif kind=='bass':token=pname(p)
   else:token='<'+ ' '.join(DRUM_NAMES[n] for n in p)+'>'
   tokens.append(with_duration(token,u))
  lines.append(' '.join(tokens)+' |'+(' \\break' if (i+1)%4==0 and i+1<len(study['bars']) else ''))
 return '\n'.join(lines)

def global_music(study,countin=False):
 beats=F(study['meter'][0]*4,study['meter'][1]);commands=[f"\\time {study['meter'][0]}/{study['meter'][1]}",f"\\tempo 4 = {study['bpm']}"]
 if study['groups']:
  base='1/8' if study['style']=='seven' else '1/4'
  commands.extend([f'\\set Timing.baseMoment = #(ly:make-moment {base.replace("/"," ")})',"\\set Timing.beatStructure = #'("+' '.join(map(str,study['groups']))+')'])
 if countin:commands.append('s1*'+str(beats/4))
 for i in range(len(study['bars'])):
  if study['tempo_change'] and i==study['tempo_change'][0]:commands.append(f"\\tempo 4 = {study['tempo_change'][1]}")
  commands.append('s1*'+str(beats/4))
 return ' '.join(commands)

def source(study,base=False,groove=False,theory=False):
 beats=F(study['meter'][0]*4,study['meter'][1]);skip='r1*'+str(beats/4)
 count=('hh8 '*7) if study['style']=='seven' else ('hh4 '*int(beats))
 systems=ceil(len(study['bars'])/4)
 if theory:
  layout=r'''\new StaffGroup <<
   \new Staff { \clef treble << \global \guitar >> }
   \new DrumStaff { << \global \drumline >> }
  >>'''
 elif groove:
  layout=r'''\new StaffGroup <<
   \new Staff { \clef bass << \global \bassline >> }
   \new DrumStaff { << \global \drumline >> }
  >>'''
 else:
  layout=r'''\new StaffGroup <<
   \new Staff { \clef "treble_8" << \global \guitar >> }
   \new TabStaff { \set TabStaff.stringTunings = #guitar-tuning \omit TextScript << \global \guitar >> }
  >>'''
 guitar_midi='' if base or groove else rf'\new Staff {{ \set Staff.midiInstrument = "acoustic grand" {skip} \mf \guitar }}'
 return rf'''% Generated by scripts/generate_modern_studies.py; edit the generator.
% soundfont-overlay: sf/PracticeRhythm.sf2
\version "2.26.0"
\language "english"
\header {{ title = "{study['number']:02} - {study['title']}{' - base' if base else ' - groove' if groove else ''}" tagline = ##f }}
\paper {{ page-breaking = #ly:one-page-breaking line-width = 160\mm ragged-right = ##f }}
global = {{ {global_music(study)} }}
control = {{ {global_music(study,True)} }}
guitar = \absolute {{ {melody(study)} \bar "|." }}
pad = \absolute {{ {rhythmic_part(study,'pad')} }}
bassline = \absolute {{ {rhythmic_part(study,'bass')} }}
drumline = \drummode {{ {rhythmic_part(study,'drums')} }}
\score {{ {layout}
 \layout {{ indent = 0 system-count = #{systems}
  \context {{ \Voice \override TextScript.staff-padding = #2 }}
  \context {{ \Score \omit StringNumber }} }} }}
\score {{
 <<
  \new Staff {{ \control }}
  {guitar_midi}
  \new Staff {{ \set Staff.midiInstrument = "acoustic grand" {skip} \pp \pad }}
  \new Staff {{ \set Staff.midiInstrument = "electric bass (finger)" {skip} \mf \bassline }}
  \new DrumStaff {{ \drummode {{ {count} }} \p \drumline }}
 >>
 \midi {{ }}
}}
'''

def main():
 for s in STUDIES:
  for base in (False,True):
   (ROOT/'src/lilypond'/f"{s['stem']}{'-base' if base else ''}.ly").write_text(source(s,base=base))
 for number,suffix in [(2,'44'),(8,'54'),(9,'78')]:
  s=STUDIES[number-1]
  (ROOT/'src/lilypond'/f'modern-groove-{suffix}.ly').write_text(source(s,groove=True))
 (ROOT/'src/lilypond/modern-metric.ly').write_text(source(STUDIES[9],theory=True))
 print('Generated twelve studies, twelve bases, three grooves and one metric score.')
if __name__=='__main__':main()
