#!/usr/bin/env python3
"""Generate ten original arpeggio studies with staff, TAB and 60/90 BPM MIDI.

Run python3 scripts/generate_arpeggio_exercises.py, then build_music.py with
--source arpeggi-esercizio-NN and --source arpeggi-esercizio-NN-90 (01..10).
Generated .ly files are not edited manually. No third-party Python dependencies.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OPEN = {1: 64, 2: 59, 3: 55, 4: 50, 5: 45, 6: 40}
STRINGS = {60:3, 62:3, 63:3, 64:2, 65:2, 66:2, 67:2, 68:2,
           69:1, 70:1, 71:1, 72:1, 74:1, 76:1}
UPPER = {60:4, 62:4, 64:3, 67:2, 71:2, 72:1, 76:1}
NAMES = {0:'c', 2:'d', 3:'ef', 4:'e', 5:'f', 6:'gf', 7:'g', 8:'af', 9:'a', 10:'bf', 11:'b'}


def note(pitch, duration=8, *, mark='', upper=False, spelling=None, accent=False):
    string = (UPPER if upper else STRINGS)[pitch]
    assert 5 <= pitch - OPEN[string] <= 12
    name = NAMES[pitch % 12] + "'" * (pitch // 12 - 4)
    return dict(pitch=pitch, duration=duration, string=string,
                name=spelling or name, mark=mark, accent=accent)


def rest(duration):
    return dict(pitch=None, duration=duration)


def bar(pitches, mark='', *, upper=False, spelling=None):
    assert len(pitches) == 8
    return [note(p, mark=mark if i == 0 else '', upper=upper,
                 spelling=(spelling or {}).get(p)) for i,p in enumerate(pitches)]


def quarters(pitches, mark='', upper=False):
    assert len(pitches) == 4
    return [note(p, 4, mark=mark if i == 0 else '', upper=upper) for i,p in enumerate(pitches)]


C_UP = [60,64,67,71,72,71,67,64]
C_SKIP = [60,67,64,71,67,72,71,64]
D_MINOR = [62,65,69,72,69,65,69,72]
G_DOM = [71,67,65,62,65,67,62,65]
C_RESOLVE = [64,67,71,72,71,67,64,60]
D_HALF = [62,65,68,72,68,65,68,72]
G_FLAT9 = [71,74,68,65,67,65,62,71]
CM6 = [72,69,67,63,60,63,67,69]

STUDIES = [
 ('Salita, discesa e ritorno',
  quarters([60,64,67,71],'Cmaj7') + quarters([72,71,67,64])
  + bar(C_UP) + [note(60,1)]),
 ('Partire da terza, quinta e settima',
  bar([64,67,71,72,71,67,64,60],'Cmaj7: dalla terza')
  + bar([67,71,72,76,72,71,67,64],'dalla quinta')
  + bar([71,67,64,60,64,67,71,72],'dalla settima') + [note(60,1)]),
 ('Sesta, settima minore e settima maggiore',
  bar([60,64,67,69,72,69,67,64],'C6')
  + bar([60,64,67,70,72,70,67,64],'C7')
  + bar(C_UP,'Cmaj7') + bar([60,64,67,69,72,69,67,60],'C6')),
 ('Tre colori della triade minore',
  bar([60,63,67,69,72,69,67,63],'Cm6')
  + bar([60,63,67,70,72,70,67,63],'Cm7')
  + bar([60,63,67,71,72,71,67,63],'Cm(maj7)')
  + bar([60,63,67,69,72,69,67,60],'Cm6')),
 ('Cambiare ordine e posizione',
  bar(C_SKIP,'Cmaj7: V posizione')
  + bar([72,67,71,64,67,71,64,60])
  + bar(C_SKIP,'VIII posizione',upper=True)
  + quarters([67,71,64,60],upper=True)),
 ('La nona dentro la linea',
  bar([60,64,67,71,74,71,67,64],'Cmaj9')
  + bar([60,64,67,70,74,70,67,64],'C9')
  + bar([60,63,67,70,74,70,67,63],'Cm9')
  + bar([60,63,67,71,74,71,67,60],'Cm(maj9)')),
 ('Quinta aumentata e settima diminuita',
  bar([60,64,68,70,72,70,68,64],'C7(#5)',spelling={68:"gs'"})
  + bar([72,70,68,64,60,64,68,70],spelling={68:"gs'"})
  + bar([60,63,66,69,72,69,66,63],'Cdim7',spelling={69:"bff'"})
  + bar([72,69,66,63,60,63,66,60],spelling={69:"bff'"})),
 ('Dall’arpeggio alla frase',
  [rest(8),note(60,8,mark='Cmaj7'),note(64,8),note(67,8),note(71,4),note(67,4)]
  + [note(64,4),note(60,2),rest(4)]
  + [rest(8),note(67,8),note(71,8),note(72,8),note(76,4),note(71,4)]
  + [note(67,4),note(64,2),rest(4)]
  + [rest(4),note(60,8),note(64,8),note(67,4),note(71,8),note(67,8)]
  + [note(64,8),note(67,4,accent=True),note(60,8),rest(2)]
  + bar([67,71,72,76,72,71,67,64])
  + [note(71,4),note(72,2),rest(4)]),
 ('Collegare II-V-I in maggiore',
  bar(D_MINOR,'Dm7') + bar(G_DOM,'G7') + bar(C_RESOLVE,'Cmaj7')
  + quarters([67,71,64,60])
  + bar([65,69,72,74,72,69,65,72],'Dm7')
  + bar([71,67,65,62,67,71,62,65],'G7')
  + [note(64,4,mark='Cmaj7'),note(67,8),note(71,8),note(72,4),note(67,4)]
  + [note(64,4),note(60,2),rest(4)]),
 ('Collegare II-V-I in minore',
  bar(D_HALF,'Dm7(b5)') + bar(G_FLAT9,'G7(b9)') + bar(CM6,'Cm6')
  + quarters([67,63,69,60])
  + bar([65,68,72,74,72,68,65,72],'Dm7(b5)')
  + bar([71,68,67,65,62,65,68,71],'G7(b9)')
  + [note(72,4,mark='Cm6'),note(69,8),note(67,8),note(63,4),note(60,4)]
  + [note(63,4),note(60,2),rest(4)]),
]


def music(events):
    tokens, beat = [], 0
    for event in events:
        duration = event['duration']
        length = 8 // duration
        assert length and beat + length <= 8
        if event['pitch'] is None:
            token = f'r{duration}'
        else:
            token = f"{event['name']}{duration}\\{event['string']}"
            if event['accent']:
                token += '->'
            if event['mark']:
                token += f'^\\markup {{ \\small "{event["mark"]}" }}'
        tokens.append(token)
        beat += length
        if beat == 8:
            tokens.append('|\n')
            beat = 0
    assert beat == 0
    return ' '.join(tokens)


def source(number, title, events, tempo):
    bars = sum(8 // e['duration'] for e in events) // 8
    assert bars in (4,8)
    return rf"""% Generated by scripts/generate_arpeggio_exercises.py; edit the generator.
\version "2.26.0"
\language "english"
\header {{ title = "{number}. {title}" tagline = ##f }}
\paper {{ page-breaking = #ly:one-page-breaking }}
melody = \absolute {{
  \time 4/4 \key c \major
  {music(events)}
  \bar "|."
}}
\score {{
  \new StaffGroup <<
    \new Staff {{ \clef "treble_8" \tempo 4 = {tempo} \melody }}
    \new TabStaff {{ \set TabStaff.stringTunings = #guitar-tuning \melody }}
  >>
  \layout {{ indent = 0 system-count = #{2 if bars == 8 else 1}
    \context {{ \Score \omit StringNumber }} }}
}}
% MIDI: one sounding voice; four high C pulses precede the printed study.
\score {{
  \new Staff {{ \tempo 4 = {tempo} c'''4\p c''' c''' c''' \melody }}
  \midi {{ }}
}}
"""


def main():
    for number,(title,events) in enumerate(STUDIES,1):
        for tempo,suffix in [(60,''),(90,'-90')]:
            (ROOT / f'src/lilypond/arpeggi-esercizio{number:02}{suffix}.ly').write_text(
                source(number,title,events,tempo))
    print('Generated twenty sources; bar lengths and fret ranges validated.')


if __name__ == '__main__':
    main()
