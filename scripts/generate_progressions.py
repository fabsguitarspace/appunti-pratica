#!/usr/bin/env python3
"""Original progression studies. Run this script, then build progressioni-* sources.

Explicit strings, pitches, rhythms and chord symbols share one definition for
notation, tablature and MIDI. Shells use only strings 6-4-3 or 5-4-3. Complete
altered chords and modal voicings are explicitly identified as such in the text.
"""
from pathlib import Path
from math import ceil
ROOT=Path(__file__).resolve().parents[1]
OPEN={6:40,5:45,4:50,3:55,2:59,1:64}
NAMES={0:'c',1:'df',2:'d',3:'ef',4:'e',5:'f',6:'gf',7:'g',8:'af',9:'a',10:'bf',11:'b'}
MELODY_STRINGS={59:3,60:3,61:3,62:3,64:2,65:2,67:2,69:1,71:1,72:1}

def chord(label,frets,spell=None,shell=True):
 if shell:assert tuple(s for s,f in frets) in ((6,4,3),(5,4,3))
 voices=tuple((s,f,OPEN[s]+f) for s,f in frets)
 assert all(f>0 for s,f,p in voices)
 assert [p for s,f,p in voices]==sorted(p for s,f,p in voices)
 return dict(label=label,voices=voices,spell=spell or {},shell=shell)

CHORDS={
 'Cmaj7':chord('Cmaj7',[(5,3),(4,2),(3,4)]),
 'C7':chord('C7',[(6,8),(4,8),(3,9)]),
 'Cm7':chord('Cm7',[(5,3),(4,1),(3,3)]),
 'Cm6':chord('Cm6',[(5,3),(4,1),(3,2)]),
 'CmMaj7':chord('Cm(maj7)',[(5,3),(4,1),(3,4)]),
 'Dm7':chord('Dm7',[(5,5),(4,3),(3,5)]),
 'G7':chord('G7',[(6,3),(4,3),(3,4)]),
 'Am7':chord('Am7',[(6,5),(4,5),(3,5)]),
 'A7':chord('A7',[(6,5),(4,5),(3,6)],{61:"cs'"}),
 'Em7':chord('Em7',[(5,7),(4,5),(3,7)]),
 'E7':chord('E7',[(5,7),(4,6),(3,7)],{56:'gs'}),
 'D7':chord('D7',[(5,5),(4,4),(3,5)],{54:'fs'}),
 'F7':chord('F7',[(5,8),(4,7),(3,8)]),
 'Fm7':chord('Fm7',[(5,8),(4,6),(3,8)]),
 'Bb7':chord('Bb7',[(6,6),(4,6),(3,7)]),
 'Ab7':chord('Ab7',[(6,4),(4,4),(3,5)]),
 'Bbmaj7':chord('Bbmaj7',[(6,6),(4,7),(3,7)]),
 'Gmaj7':chord('Gmaj7',[(6,3),(4,4),(3,4)],{54:'fs'}),
 'Db7':chord('Db7',[(5,4),(4,3),(3,4)],{59:"cf'"}),
 'Dhalf':chord('Dm7(b5)',[(5,5),(4,6),(3,5),(2,6)],shell=False),
 'G7b9':chord('G7(b9), senza R',[(5,2),(4,3),(3,1),(2,3)],shell=False),
 'Csdim':chord('C#dim7',[(5,4),(4,5),(3,3),(2,5)],{49:'cs'},shell=False),
 'Fsdim':chord('F#dim7',[(6,2),(5,3),(4,1),(3,2)],{42:'fs,'},shell=False),
 'DmPedal':chord('Dm7',[(5,5),(4,7),(3,5),(2,6)],shell=False),
 'EmD':chord('Em7/D',[(5,5),(4,5),(3,4),(2,5)],shell=False),
}

def whole(*keys):return [[(key,1)] for key in keys]
MAJOR=whole('Dm7','G7','Cmaj7','Cmaj7')
MINOR=whole('Dhalf','G7b9','Cm6','CmMaj7')
BLUES=whole('C7','C7','C7','C7','F7','F7','C7','C7','G7','F7','C7','G7')
A=whole('Cmaj7','Am7','Dm7','G7','Em7','A7','Dm7','G7')
B=whole('D7','D7','Gmaj7','Gmaj7','Em7','A7','Dm7','G7')
JAZZ=whole('C7','F7','C7','C7','F7','Fsdim','C7','A7','Dm7','G7')+[[('C7',2),('A7',2)],[('Dm7',2),('G7',2)]]

# Melody/rest events: sounding MIDI pitch (None for rest), denominator.
TARGETS=[[(65,2),(69,4),(72,4)],[(65,2),(62,4),(59,4)],[(64,2),(67,4),(71,4)],[(72,2),(None,2)]]
PHRASE=[[(None,4),(64,8),(67,8),(71,4),(67,4)],[(69,4),(64,4),(60,2)],
 [(None,8),(62,8),(65,8),(69,8),(72,8),(69,8),(65,8),(64,8)],
 [(65,4),(62,4),(59,2)],[(64,4),(67,4),(71,2)],[(67,4),(64,4),(61,2)],
 [(62,4),(65,8),(69,8),(72,4),(69,4)],[(65,8),(62,8),(59,4),(60,2)]]
PHRASE_CHORDS=A[:7]+[[('G7',2),('Cmaj7',2)]]

STUDIES=[
 dict(stem='progressioni-01-ii-v-i',title='II-V-I: collegare gli shell',bars=MAJOR),
 dict(stem='progressioni-02-ritmo',title='II-V-I: due ritmi di accompagnamento',bars=MAJOR,rhythm=True),
 dict(stem='progressioni-03-note-bersaglio',title='II-V-I: note bersaglio',bars=MAJOR,melody=TARGETS),
 dict(stem='progressioni-04-minore',title='II-V-I in minore',bars=MINOR),
 dict(stem='progressioni-05-turnaround',title='Turnaround: Am7 oppure A7',bars=whole('Cmaj7','Am7','Dm7','G7','Cmaj7','A7','Dm7','G7')),
 dict(stem='progressioni-06-dominanti',title='Dominanti secondarie: raggiungere un accordo',bars=whole('Cmaj7','E7','Am7','A7','Dm7','G7','Cmaj7','Cmaj7')),
 dict(stem='progressioni-07-tritono',title='G7 e Db7: due percorsi verso Do',bars=MAJOR+whole('Dm7','Db7','Cmaj7','Cmaj7')),
 dict(stem='progressioni-08-backdoor',title='Interscambio: Fm7-Bb7-Cmaj7',bars=whole('Cmaj7','Fm7','Bb7','Cmaj7')),
 dict(stem='progressioni-09-diminuito',title='Un diminuito di passaggio',bars=whole('Cmaj7','Csdim','Dm7','G7')),
 dict(stem='progressioni-10-blues',title='Blues in Do: dodici battute',bars=BLUES),
 dict(stem='progressioni-11-jazz-blues',title='Blues in Do: una variante jazz',bars=JAZZ),
 dict(stem='progressioni-12-blues-minore',title='Blues minore in Do: una variante',bars=whole('Cm6','Cm6','Cm6','Cm6','Fm7','Fm7','Cm6','Cm6','Ab7','G7','Cm6','G7')),
 dict(stem='progressioni-13-vamp',title='Vamp dorico: pedale di Re',bars=whole(*(['DmPedal','EmD']*4))),
 dict(stem='progressioni-14-centri',title='Due centri: Do maggiore e Sib maggiore',bars=MAJOR+whole('Cm7','F7','Bbmaj7','Bbmaj7')),
 dict(stem='progressioni-15-aaba',title='Studio originale: forma AABA di 32 battute',bars=A+A+B+A),
 dict(stem='progressioni-16-frase',title='Studio originale: accompagnamento e frase',bars=PHRASE_CHORDS,melody=PHRASE),
 dict(stem='progressioni-17-rhythm-changes',title='Rhythm changes: una sezione A e un bridge',bars=[
  [('Cmaj7',2),('A7',2)],[('Dm7',2),('G7',2)],[('Em7',2),('A7',2)],[('Dm7',2),('G7',2)],
  [('C7',1)],[('F7',2),('Fsdim',2)],[('Cmaj7',2),('A7',2)],[('Dm7',2),('G7',2)],
 ]+whole('E7','E7','A7','A7','D7','D7','G7','G7')),
 dict(stem='progressioni-base-ii-v-i',title='Base: II-V-I in Do, due giri',bars=MAJOR+MAJOR),
 dict(stem='progressioni-base-minore',title='Base: II-V-I minore, due giri',bars=MINOR+MINOR),
 dict(stem='progressioni-base-blues',title='Base: blues in Do, un chorus',bars=BLUES),
]

def pitch_name(pitch):
 shift=pitch//12-4
 return NAMES[pitch%12]+("'"*shift if shift>=0 else ','*(-shift))

def chord_token(key,duration,mark=True):
 c=CHORDS[key]
 notes=' '.join((c['spell'].get(p) or pitch_name(p))+f'\\{s}' for s,f,p in c['voices'])
 result=f'<{notes}>{duration}'
 if mark:result+=f'^\\markup {{ \\small "{c["label"]}" }}'
 return result

def accompaniment(study):
 lines=[]
 for i,bar in enumerate(study['bars']):
  assert sum(8//d for key,d in bar)==8
  if study.get('rhythm'):
   key=bar[0][0]
   if i<2:line='r4 '+chord_token(key,4)+' r4 '+chord_token(key,4,False)
   else:line='r8 '+chord_token(key,8)+' r4 '+chord_token(key,4,False)+' r4'
  else:line=' '.join(chord_token(key,d) for key,d in bar)
  lines.append(line+' |'+(' \\break' if (i+1)%4==0 and i+1<len(study['bars']) else ''))
 return '\n'.join(lines)

def melody(study):
 lines=[]
 for i,(bar,chords) in enumerate(zip(study['melody'],study['bars'])):
  assert sum(8//d for p,d in bar)==8
  chord_times={};t=0
  for key,d in chords:chord_times[t]=CHORDS[key]['label'];t+=8//d
  pending=None;tokens=[];t=0
  for pitch,duration in bar:
   if t in chord_times:pending=chord_times[t]
   token=f'r{duration}' if pitch is None else f'{pitch_name(pitch) if pitch!=61 else "cs"+chr(39)}{duration}\\{MELODY_STRINGS[pitch]}'
   if pending:
    token+=f'^\\markup {{ \\small "{pending}" }}';pending=None
   tokens.append(token);t+=8//duration
  lines.append(' '.join(tokens)+' |'+(' \\break' if (i+1)%4==0 and i+1<len(study['bars']) else ''))
 return '\n'.join(lines)

def source(study):
 n=len(study['bars']);systems=ceil(n/4);height=max(297,75+systems*40)
 backing=accompaniment(study)
 tune=melody(study) if 'melody' in study else backing
 midi = r"\new Staff { \tempo 4 = 60 c'''4\p c''' c''' c''' \mf \music }"
 if 'melody' in study:
  midi=rf'''<<
   {midi}
   \new Staff {{ \tempo 4 = 60 r1 \p \backing }}
  >>'''
 return rf'''% Generated by scripts/generate_progressions.py; edit the generator.
\version "2.26.0"
\language "english"
\header {{ title = "{study['title']}" tagline = ##f }}
\paper {{ page-breaking = #ly:one-page-breaking line-width = 160\mm
 paper-height = {height}\mm ragged-right = ##f }}
music = \absolute {{ \time 4/4 \key c \major
 {tune} \bar "|." }}
backing = \absolute {{ \time 4/4 \key c \major
 {backing} \bar "|." }}
\score {{
 \new StaffGroup <<
  \new Staff {{ \clef "treble_8" \tempo 4 = 60 \music }}
  \new TabStaff {{ \set TabStaff.stringTunings = #guitar-tuning \omit TextScript \music }}
 >>
 \layout {{ indent = 0 system-count = #{systems}
  \context {{ \Voice \override TextScript.staff-padding = #2 }}
  \context {{ \Score \omit StringNumber }} }}
}}
\score {{ {midi} \midi {{ }} }}
'''

def main():
 for s in STUDIES:(ROOT/'src/lilypond'/f"{s['stem']}.ly").write_text(source(s))
 print(f'Generated {len(STUDIES)} original progression studies and bases.')
if __name__=='__main__':main()
