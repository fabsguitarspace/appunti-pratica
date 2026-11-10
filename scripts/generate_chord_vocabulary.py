#!/usr/bin/env python3
"""Generate minor/dominant chord vocabulary, organized by a fixed soprano.

Run python3 scripts/generate_chord_vocabulary.py, then build the listed sources
with build-lilypond.sh --source NAME (repeatable). Generated .ly are not edited.
Four explicit strings/frets define notation, diagrams, TAB and a single MIDI part.
Voicings are selected deterministically with a four-fret maximum hand span.
"""
from itertools import combinations, product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OPEN = {6:40,5:45,4:50,3:55,2:59,1:64}
# Profiles: chord suffix, permitted pitch classes relative to the root, required ones.
def profile(suffix, allowed, required):
    return (suffix, frozenset(allowed), frozenset(required))

M7 = profile('m7',[0,3,7,10],[3,10])
M6 = profile('m6',[0,3,7,9],[3,9])
MM = profile('m(maj7)',[0,3,7,11],[3,11])
M9 = profile('m9',[0,2,3,7,10],[2,3,10])
M69 = profile('m6/9',[0,2,3,7,9],[2,3,9])
MM9 = profile('m(maj9)',[0,2,3,7,11],[2,3,11])
M11 = profile('m11',[0,2,3,5,7,10],[3,5,10])
MM11 = profile('m(maj11)',[0,2,3,5,7,11],[3,5,11])
M13 = profile('m13',[0,2,3,5,7,9,10],[3,9,10])
MM13 = profile('m(maj13)',[0,2,3,5,7,9,11],[3,9,11])
D7 = profile('7',[0,4,7,10],[4,10])
D9 = profile('9',[0,2,4,7,10],[2,4,10])
D13 = profile('13',[0,2,4,7,9,10],[4,9,10])
DB9 = profile('7(b9)',[0,1,4,7,10],[1,4,10])
D13B9 = profile('13(b9)',[0,1,4,7,9,10],[1,4,9,10])
DB9B13 = profile('7(b9,b13)',[0,1,4,8,10],[1,4,8,10])
DS9 = profile('7(#9)',[0,3,4,7,10],[3,4,10])
DS9B13 = profile('7(#9,b13)',[0,3,4,8,10],[3,4,8,10])
DS9S11 = profile('7(#9,#11)',[0,3,4,6,10],[3,4,6,10])
DS11 = profile('7(#11)',[0,4,6,7,10],[4,6,10])
D9S11 = profile('9(#11)',[0,2,4,6,7,10],[2,4,6,10])
D13S11 = profile('13(#11)',[0,2,4,6,7,9,10],[4,6,9,10])
DB13 = profile('7(b13)',[0,4,7,8,10],[4,8,10])
SUS = profile('7sus4',[0,5,7,10],[5,10])
SUS9 = profile('9sus4',[0,2,5,7,10],[2,5,10])
SUS13 = profile('13sus4',[0,2,5,7,9,10],[5,9,10])

# The third entry repeats m11 with a different shape: same chord, different voicing.
MINOR = [
 ('r','R',0,[M7,M6,MM]),('9','9',2,[M9,M69,MM9]),
 ('b3','♭3',3,[M7,M6,MM]),('11','11',5,[M11,M11,MM11]),
 ('5','5',7,[M7,M6,MM]),('13','6 / 13',9,[M6,M13,MM13]),
 ('b7','♭7',10,[M7,M9,M11]),('maj7','Δ7',11,[MM,MM9,MM11]),
]
DOMINANT = [
 ('r','R',0,[D7,D7,D13]),('b9','♭9',1,[DB9,D13B9,DB9B13]),
 ('9','9',2,[D9,D13,D9S11]),('s9','♯9',3,[DS9,DS9B13,DS9S11]),
 ('3','3',4,[D7,D9,D13]),('11','11 / sus4',5,[SUS,SUS9,SUS13]),
 ('s11','♯11',6,[DS11,D9S11,D13S11]),('5','5',7,[D7,D9,D13]),
 ('b13','♭13',8,[DB13,DB9B13,DS9B13]),
 ('13','13',9,[D13,D13B9,D13S11]),('b7','♭7',10,[D7,D9,D13]),
]


def choose_voicing(root, top_string, top_pitch, chord, exclude=()):
    suffix,allowed,required = chord
    top_fret = top_pitch-OPEN[top_string]
    candidates=[]
    for lower_strings in combinations(range(6,top_string,-1),3):
        options=[]
        for string in lower_strings:
            options.append([(string,fret,OPEN[string]+fret)
                            for fret in range(max(1,top_fret-4),min(20,top_fret+4)+1)
                            if OPEN[string]+fret<top_pitch
                            and (OPEN[string]+fret-root)%12 in allowed])
        for lower in product(*options):
            voices=lower+((top_string,top_fret,top_pitch),)
            if tuple(v[2] for v in voices)!=tuple(sorted(set(v[2] for v in voices))):
                continue
            frets=[v[1] for v in voices]
            span=max(frets)-min(frets)
            if span>4 or voices in exclude:
                continue
            pcs={(v[2]-root)%12 for v in voices}
            if not required<=pcs:
                continue
            # Keep extensions out of the bass (also the natural sixth of m6).
            bass_interval = (voices[0][2] - root) % 12
            chord_tone_basses = {0, 3, 7, 10, 11} if suffix.startswith('m') else {0, 4, 7, 10}
            if bass_interval not in chord_tone_basses:
                continue
            # Prefer compact four-note shapes; roots when space permits; few skipped strings.
            gaps=voices[0][0]-top_string+1-len(voices)
            score=(span*3 + gaps*2 + (0 if 0 in pcs else 3)
                   + (0 if (voices[0][2]-root)%12==0 else 1)
                   + (4-len(pcs))*2)
            candidates.append((score,voices))
    if not candidates:
        raise ValueError((root,top_string,top_pitch,suffix))
    return min(candidates)[1]


def catalogue():
    entries=[]
    for family,degrees in [('minore',MINOR),('dominante',DOMINANT)]:
        for root_name,root,top_string in [('c',48,2),('f',53,1)]:
            for key,label,offset,profiles in degrees:
                top_pitch=root+12+offset
                shapes=[]
                for chord in profiles:
                    voices=choose_voicing(root,top_string,top_pitch,chord,
                                          exclude=[v['voices'] for v in shapes])
                    shapes.append(dict(chord=chord,voices=voices))
                entries.append(dict(family=family,root_name=root_name,root=root,
                                    top_string=top_string,top_pitch=top_pitch,
                                    degree=label,key=key,shapes=shapes,
                                    stem=f'accordi-{root_name}-{family}-{key}'
                                         + ('-1' if top_string==1 else '')))
    return entries


# Interval spellings: letter name relative to each root, including #9 and b13.
SPELLINGS = {
 'c': {0:'c',1:'df',2:'d',3:'ef',4:'e',5:'f',6:'fs',7:'g',8:'af',9:'a',10:'bf',11:'b'},
 'f': {0:'f',1:'gf',2:'g',3:'af',4:'a',5:'bf',6:'b',7:'c',8:'df',9:'d',10:'ef',11:'e'},
}
NATURAL_PCS={'c':0,'d':2,'e':4,'f':5,'g':7,'a':9,'b':11}


def lily_note(entry,voice):
    pitch=voice[2]
    interval=(pitch-entry['root'])%12
    name=SPELLINGS[entry['root_name']][interval]
    if entry['family']=='dominante' and interval==3:
        name='ds' if entry['root_name']=='c' else 'gs'
    natural=NATURAL_PCS[name[0]]
    alteration=1 if name.endswith('s') else -1 if len(name)>1 and name.endswith('f') else 0
    octave=(pitch-natural-alteration)//12-1
    shift=octave-3
    marks="'"*shift if shift>=0 else ','*(-shift)
    return f'{name}{marks}\\{voice[0]}'


def source(entry):
    diagrams=[];notes=[]
    root_name=entry['root_name'].upper()
    for index,shape in enumerate(entry['shapes']):
        tag=f'diag{chr(65+index)}'
        items=[]
        by_string={s:f for s,f,p in shape['voices']}
        for string in range(6,0,-1):
            items.append(f'(place-fret {string} {by_string[string]})' if string in by_string else f'(mute {string})')
        suffix=shape['chord'][0]
        pcs={(p-entry['root'])%12 for s,f,p in shape['voices']}
        label=root_name+suffix
        diagrams.append(rf'''{tag} = \markup \center-column {{
  \small "{label}"
  \fret-diagram-verbose #'({' '.join(items)})
}}''')
        notes.append('<'+' '.join(lily_note(entry,v) for v in shape['voices'])+f'>1^\\{tag}')
    family='minore' if entry['family']=='minore' else 'dominante'
    title=f"{root_name} {family}: {entry['degree']} sulla {entry['top_string']}a corda"
    return rf"""% Generated by scripts/generate_chord_vocabulary.py; edit the generator.
\version "2.26.0"
\language "english"
\header {{ title = "{title}" tagline = ##f }}
\paper {{ page-breaking = #ly:one-page-breaking
  line-width = 160\mm ragged-right = ##f }}
{chr(10).join(diagrams)}
melody = \absolute {{
  \time 4/4 \key c \major
  {' | '.join(notes)} \bar "|."
}}
\score {{
  \new StaffGroup <<
    \new Staff {{ \clef "treble_8" \tempo 4 = 60 \melody }}
    \new TabStaff {{ \set TabStaff.stringTunings = #guitar-tuning
      \omit TextScript \melody }}
  >>
  \layout {{ indent = 0 system-count = #1
    \context {{ \Voice \override TextScript.staff-padding = #4 }}
    \context {{ \Score \omit StringNumber }} }}
}}
% MIDI has one sounding chord part, without the TAB doubling.
\score {{
  \new Staff {{ \tempo 4 = 60 c'''4\p c''' c''' c''' \melody }}
  \midi {{ }}
}}
"""


def main():
    entries=catalogue()
    for entry in entries:
        (ROOT/'src/lilypond'/f"{entry['stem']}.ly").write_text(source(entry))
    print(f"Generated {len(entries)} sources, {sum(len(e['shapes']) for e in entries)} voicings.")


if __name__=='__main__':
    main()
