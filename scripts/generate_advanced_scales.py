#!/usr/bin/env python3
"""Generate the eight advanced scale studies and two studies on derived scales.

Run from any directory: python3 scripts/generate_advanced_scales.py
After building the assets, run with --collect-pdf to assemble the PDF booklet.
Generated scale-avanzati-01..08[-90].ly and scale-derivate-01..02[-90].ly
must not be edited by hand.
Pitch, rhythm, strings and accents share one definition for Staff/Tab/MIDI.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAJOR = [60, 62, 64, 65, 67, 69, 71, 72, 74, 76]
OPEN = {1: 64, 2: 59, 3: 55, 4: 50, 5: 45, 6: 40}
# Strings selected explicitly, rather than relying on automatic tablature.
STRINGS = {60: 3, 62: 3, 63: 3, 64: 2, 65: 2, 66: 2, 67: 2, 68: 2, 69: 1, 70: 1, 71: 1, 72: 1, 74: 1, 76: 1}
UPPER = {60: 4, 62: 4, 64: 3, 65: 3, 67: 2, 69: 2, 71: 2, 72: 1}
NAMES = {0: 'c', 2: 'd', 3: 'ef', 4: 'e', 5: 'f', 6: 'gf', 7: 'g', 8: 'gs', 9: 'a', 10: 'bf', 11: 'b'}


def note(pitch, duration=8, *, accent=False, mark='', upper=False):
    string = (UPPER if upper else STRINGS)[pitch]
    fret = pitch - OPEN[string]
    assert 5 <= fret <= 12, (pitch, string, fret)
    return dict(pitch=pitch, duration=duration, string=string, accent=accent, mark=mark)


def rest(duration):
    return dict(pitch=None, duration=duration)


def run(indices, **kwargs):
    return [note(MAJOR[i], **kwargs) for i in indices]


def end():
    return [note(60, 1)]


STUDIES = [
    ('Direzioni alternate',
     run([0,1,2,3,4,3,2,1, 2,3,4,5,6,5,4,3, 4,5,6,7,6,5,4,1]) + end()),
    ('Terze a direzione alternata',
     run([0,2,3,1,2,4,5,3, 4,6,7,5,6,8,7,5, 6,4,3,5,4,2,1,3]) + end()),
    ('Quarte e seste nella scala',
     run([0,3,1,4,2,5,3,6], mark='')
     + run([4,7,3,6,2,5,1,4, 0,3,1,4,2,5,1,3]) + end()
     + run([0,5,1,6,2,7,1,6, 2,7,1,6,0,5,1,6, 2,7,1,6,0,5,1,3]) + end()),
    ('Gruppi di tre in ottavi',
     [note(MAJOR[i+j], mark='inizio cellula' if k == 0 else '', accent=False)
      for k,(i,j) in enumerate((i,j) for i in range(8) for j in range(3))] + end()),
    ('Accenti ogni tre note',
     [note(MAJOR[i], accent=k % 3 == 0)
      for k,i in enumerate([0,1,2,3,4,5,6,7,6,5,4,3,2,1,0,1,2,3,4,3,2,1,2,1])] + end()),
    ('Collegare due posizioni',
     run([0,1,2,3,4,5,6,7], mark='')
     + run([6,5,4,3,2,1,0,1])
     + [note(MAJOR[i], upper=True, mark='VIII posizione' if k == 0 else '')
        for k,i in enumerate([2,3,4,5,6,7,6,5])]
     + [note(MAJOR[4],4,upper=True),note(MAJOR[2],4,upper=True),note(MAJOR[1],4,upper=True),note(MAJOR[0],4,upper=True)]),
    ('Una cellula, tre colori',
     [note(p, mark=label if k == 0 else '')
      for label, pitches in [
          ('Do maggiore',[60,64,67,69,71,69,67,64]),
          ('Do minore melodica',[60,63,67,69,71,69,67,63]),
          ('Do dorico',[60,63,67,69,70,69,67,63])]
      for k,p in enumerate(pitches)] + end()),
    ('Dalla sequenza alla frase',
     [rest(8)] + run([0,2,1,3,2,4,3])
     + [note(67,4),note(64,8),note(62,8),note(60,4),rest(4)]
     + [rest(8)] + run([4,6,5,7,6,4,2])
     + [note(62,4),note(60,2),rest(4)]
     + [rest(4)] + run([0,2,1,3,4,2])
     + [note(62,8),note(64,4,accent=True),note(60,8),rest(2)]
     + [note(67,8),note(69,8),note(71,4),note(69,8),note(67,8),note(64,4)]
     + [note(62,4),note(60,2),rest(4)]),
]
# Derived scales (pentatonic/blues and bebop), on C7 / C6 in the same V–VIII position.
DERIVED = [
    ('Pentatonica minore e blues su C7',
     [rest(8), note(63, mark='terza blues'), note(64), note(67), note(70, 4), note(67), note(63)]
     + [note(60, 4), rest(4), rest(2)]
     + [rest(8), note(65), note(66, mark='quinta diminuita'), note(67), note(70), note(72, 4), note(70)]
     + [note(67), note(66), note(65), note(63), note(60, 2)]),
    ('Discesa bebop: note dell\'accordo sui movimenti',
     [note(p, mark='bebop di dominante, C7' if k == 0 else '')
      for k, p in enumerate([72, 71, 70, 69, 67, 65, 64, 62])]
     + [note(p) for p in [60, 64, 67, 70, 72, 71, 70, 69]]
     + [note(67), note(65), note(64), note(62), note(60, 4), rest(4)]
     + [note(p, mark='bebop maggiore, C6' if k == 0 else '')
        for k, p in enumerate([72, 71, 69, 68, 67, 65, 64, 62])]
     + end()),
]
STUDIES[2][1][0]['mark'] = 'Quarte'
STUDIES[2][1][25]['mark'] = 'Seste'
STUDIES[5][1][0]['mark'] = 'V posizione'


def lily_pitch(pitch):
    return NAMES[pitch % 12] + "'" * (pitch // 12 - 4)


def music(events):
    tokens, beat = [], 0
    for event in events:
        duration = event['duration']
        length = 8 // duration if duration <= 8 else 0
        assert length and beat + length <= 8, (event, beat)
        if event['pitch'] is None:
            token = f'r{duration}'
        else:
            token = f"{lily_pitch(event['pitch'])}{duration}\\{event['string']}"
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
    assert 4 <= bars <= 8
    return rf"""% Generated by scripts/generate_advanced_scales.py; edit the generator.
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
  \layout {{ indent = 0 system-count = #{2 if bars == 8 else 1} \context {{ \Score \omit StringNumber }} }}
}}
% One audible voice only: tablature must not double the MIDI notes.
% Four high C pulses precede the study, but do not appear in the printed bars.
\score {{
  \new Staff {{ \tempo 4 = {tempo} c'''4\p c''' c''' c''' \melody }}
  \midi {{ }}
}}
"""


def collect_pdf():
    import pymupdf  # Installed with the optional music pipeline dependencies.
    base = ROOT / 'src/docs/_static/music'
    collection = pymupdf.open()
    for number in range(1, 9):
        with pymupdf.open(base / f'scale-avanzati-{number:02}.pdf') as score:
            assert len(score) == 1
            page = collection.new_page(width=842, height=595)
            height = min(475, 794 * score[0].rect.height / score[0].rect.width)
            page.show_pdf_page(pymupdf.Rect(24, 30, 818, 30 + height), score, 0)
    collection.set_metadata({
        'title': 'Scale — otto esercizi avanzati con tablatura',
        'author': 'Appunti di Pratica per Chitarra Jazz',
    })
    collection.save(base / 'scale-avanzati-raccolta.pdf', garbage=4, deflate=True)
    collection.close()
    print('Assembled eight score pages in scale-avanzati-raccolta.pdf.')


def main():
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--collect-pdf', action='store_true')
    args = parser.parse_args()
    if args.collect_pdf:
        collect_pdf()
        return
    for number, (title, events) in enumerate(STUDIES, 1):
        for tempo, suffix in [(60, ''), (90, '-90')]:
            path = ROOT / f'src/lilypond/scale-avanzati-{number:02}{suffix}.ly'
            path.write_text(source(number, title, events, tempo))
    for number, (title, events) in enumerate(DERIVED, 1):
        for tempo, suffix in [(60, ''), (90, '-90')]:
            path = ROOT / f'src/lilypond/scale-derivate-{number:02}{suffix}.ly'
            path.write_text(source(number, title, events, tempo))
    print('Generated 20 LilyPond sources; validated bar lengths and string/fret ranges.')


if __name__ == '__main__':
    main()
