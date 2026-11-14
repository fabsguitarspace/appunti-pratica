#!/usr/bin/env python3
"""Generate the examples of «Strutture melodiche» (S1–S12) and «Pentatoniche»
(P1–P3) at 60 and 90 BPM.

Run python3 scripts/generate_melodic_structures.py, then build_music.py with
--source for every strutture-* and pentatoniche-* stem it writes (each at 60
and 90 BPM; examples with a backing track also get <stem>-base[-90]).
Generated .ly files are not edited manually. No third-party Python dependencies.
Pitches are MIDI numbers at sounding pitch: 60 is the middle C (Do4).
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OPEN = {1: 64, 2: 59, 3: 55, 4: 50, 5: 45, 6: 40}
# Default fingering: fifth position, frets 5–10.
STRINGS = {60: 3, 62: 3, 63: 3, 64: 2, 65: 2, 66: 2, 67: 2, 69: 1, 70: 1,
           71: 1, 72: 1, 74: 1, 76: 1}
NAMES = {0: 'c', 2: 'd', 3: 'ef', 4: 'e', 5: 'f', 6: 'fs', 7: 'g', 9: 'a', 10: 'bf', 11: 'b'}
TEMPI = [(60, ''), (90, '-90')]

# Root of the bass and a two-note shell (third and seventh, or third and sixth).
CHORDS = {'Cmaj7': (48, (52, 59)), 'Dm7': (50, (53, 60)),
          'G7': (43, (53, 59)), 'C6': (48, (52, 57)), 'Cm7': (48, (51, 58)),
          'Am7': (45, (48, 55))}


def pname(pitch):
    octave = pitch // 12 - 4
    return NAMES[pitch % 12] + ("'" * octave if octave >= 0 else ',' * -octave)


def note(pitch, duration=8, *, string=None, mark=''):
    string = string or STRINGS[pitch]
    fret = pitch - OPEN[string]
    assert 0 <= fret <= 12, (pitch, string)
    return dict(pitch=pitch, duration=duration, string=string, fret=fret, mark=mark)


def rest(duration):
    return dict(pitch=None, duration=duration)


def cell(pitches, chord='', strings=None):
    """Four eighth notes followed by a half rest: the shape used in S1–S5."""
    assert len(pitches) == 4
    strings = strings or [None] * 4
    return [note(p, string=s, mark=chord if i == 0 else '')
            for i, (p, s) in enumerate(zip(pitches, strings))] + [rest(2)]


DO_RE_MI_SOL = [60, 62, 64, 67]
MI_SOL_RE_DO = [64, 67, 62, 60]

def run(pitches, chord=''):
    """Eighth notes; the first carries the mark."""
    return [note(p, mark=chord if i == 0 else '') for i, p in enumerate(pitches)]


A_MINOR_PENT = [60, 62, 64, 67, 69, 72, 74, 76]   # Do4–Mi5, collection of La minore


def formula(start):
    """Passo su, salto su, passo giù: indexes i, i+1, i+3, i+2 in the collection."""
    return [A_MINOR_PENT[start + k] for k in (0, 1, 3, 2)]


# label, stem, title, chords per bar, events, backing track
EXAMPLES = [
    ('S1', 'strutture-01', 'Stesso materiale, due ordini', ['Cmaj7'] * 2,
     cell(DO_RE_MI_SOL, 'Cmaj7') + cell(MI_SOL_RE_DO), False),
    ('S2', 'strutture-02', 'La stessa linea su due accordi', ['Cmaj7', 'Dm7'],
     cell(DO_RE_MI_SOL, 'Cmaj7') + cell(DO_RE_MI_SOL, 'Dm7'), True),
    ('S3', 'strutture-03', 'Ordine, registro e posizione', ['Cmaj7'] * 4,
     cell(DO_RE_MI_SOL, 'Cmaj7') + cell(MI_SOL_RE_DO)
     + cell([64, 67, 74, 72], 'V posizione')
     + cell([64, 67, 74, 72], 'VIII–XII tasto', strings=[3, 3, 1, 1]), False),
    ('S4', 'strutture-04', 'Stesse note, tre ritmi', ['Cmaj7'] * 3,
     cell(MI_SOL_RE_DO, 'Cmaj7')
     + [note(64, 4), note(67, 4), note(62, 8), note(60, 8), rest(4)]
     + [rest(8), note(64, 8), note(67, 8), note(62, 8), note(60, 4), rest(4)], False),
    ('S5', 'strutture-05', 'Dalla struttura alla cadenza', ['Dm7', 'G7', 'Cmaj7', 'Cmaj7'],
     cell([62, 64, 65, 69], 'Dm7') + cell([67, 69, 71, 62], 'G7')
     + cell(MI_SOL_RE_DO, 'Cmaj7') + [note(60, 2), rest(2)], True),
    ('S6', 'strutture-06', 'Una nota sì e una no', ['C6'] * 2,
     [note(p, mark='C6' if i == 0 else '') for i, p in enumerate([60, 64, 62, 67, 64, 69])]
     + [rest(4)] + [note(p) for p in [67, 72, 69, 74]] + [rest(2)], False),
    ('S7', 'strutture-07', 'Tre strutture su Cmaj7', ['Cmaj7'] * 3,
     cell([60, 62, 64, 67], 'Cmaj7: 1–5') + cell([67, 69, 71, 74], '5–9')
     + cell([62, 64, 66, 69], '9–13'), False),
    ('S8', 'strutture-08', 'Tre strutture su Cm7', ['Cm7'] * 3,
     cell([60, 63, 65, 67], 'Cm7: 1–5') + cell([67, 70, 72, 74], '5–9')
     + cell([62, 65, 67, 69], '9–13'), False),
    ('S9', 'strutture-09', 'Quattro permutazioni', ['Cmaj7'] * 4,
     cell([60, 64, 62, 67], 'Cmaj7: 1–3–2–5') + cell([62, 67, 64, 60], '2–5–3–1')
     + cell([64, 60, 62, 67], '3–1–2–5') + cell([67, 62, 64, 60], '5–2–3–1'), False),
    ('S10', 'strutture-10', 'Rivolti lineari', ['Cmaj7'] * 4,
     cell([62, 67, 64, 60], 'Cmaj7: Do in basso') + cell([62, 67, 64, 72], 'Re in basso')
     + cell([74, 67, 64, 72], 'Mi in basso') + cell([74, 67, 76, 72], 'Sol in basso'), False),
    ('S11', 'strutture-11', 'Mescolare le strutture', ['Dm7', 'G7', 'Cmaj7', 'Cmaj7'],
     cell([69, 67, 65, 62], 'Dm7') + cell([62, 64, 65, 69], 'G7')
     + cell([69, 67, 71, 74], 'Cmaj7') + [note(64, 2), rest(2)], True),
    ('S12', 'strutture-12', 'La struttura delle note guida', ['Cmaj7', 'Cm7'],
     cell([64, 67, 69, 71], 'Cmaj7: 3–5–6–7') + cell([63, 65, 67, 70], 'Cm7: 3–4–5–7'), False),
    ('P1', 'pentatoniche-01', 'Una formula di quattro note', ['Am7'] * 3,
     run(formula(4) + formula(3), 'Am7') + run(formula(2) + formula(1))
     + run(formula(0)) + [note(60, 2)], False),
    ('P2', 'pentatoniche-02', 'Tre pentatoniche su Dm7', ['Dm7'] * 3,
     run([62, 65, 67, 69, 72, 69], 'Dm7: Re minore') + [rest(4)]
     + run([69, 72, 74, 76, 74, 72], 'La minore') + [rest(4)]
     + run([64, 67, 69, 71, 74, 71], 'Mi minore') + [rest(4)], True),
    ('P3', 'pentatoniche-03', 'Una pentatonica alterata sulla dominante',
     ['Dm7', 'G7', 'Cmaj7', 'Cmaj7'],
     run([62, 65, 67, 69, 72, 69, 67, 65], 'Dm7: Re minore')
     + run([67, 70, 71, 74, 71, 70, 67, 65], 'G7: pentatonica alterata')
     + run([64, 67, 69, 72, 74, 72, 69, 67], 'Cmaj7: La minore')
     + [note(64, 2), rest(2)], True),
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
            token = f"{pname(event['pitch'])}{duration}\\{event['string']}"
            if event['mark']:
                token += f'^\\markup {{ \\small "{event["mark"]}" }}'
        tokens.append(token)
        beat += length
        if beat == 8:
            tokens.append('|\n')
            beat = 0
    assert beat == 0
    return ' '.join(tokens)


def bars(events):
    return sum(8 // e['duration'] for e in events) // 8


def bassline(chords):
    return ' '.join(f'{pname(CHORDS[c][0])}1' for c in chords)


def padline(chords):
    return ' '.join('<' + ' '.join(pname(p) for p in CHORDS[c][1]) + '>1' for c in chords)


HEADER = r'''% Generated by scripts/generate_melodic_structures.py; edit the generator.
\version "2.26.0"
\language "english"
'''


OVERLAY = '% soundfont-overlay: sf/PracticeRhythm.sf2\n'
COUNT = r"c'''4\p c''' c''' c'''"


def source(label, title, chords, events, tempo, base):
    accompaniment = ''
    if base:
        accompaniment = rf'''
  \new Staff {{ \set Staff.midiInstrument = "acoustic grand" r1 \pp \pad }}
  \new Staff {{ \set Staff.midiInstrument = "electric bass (finger)" r1 \mf \bassline }}'''
    head = HEADER + (OVERLAY if base else '')
    return head + rf'''\header {{ title = "{label}. {title}" tagline = ##f }}
\paper {{ page-breaking = #ly:one-page-breaking }}
melody = \absolute {{
  \time 4/4 \key c \major
  {music(events)}
  \bar "|."
}}
pad = \absolute {{ {padline(chords)} }}
bassline = \absolute {{ {bassline(chords)} }}
\score {{
  \new StaffGroup <<
    \new Staff {{ \clef "treble_8" \tempo 4 = {tempo} \melody }}
    \new TabStaff {{ \set TabStaff.stringTunings = #guitar-tuning \omit TextScript \melody }}
  >>
  \layout {{ indent = 0 system-count = #1
    \context {{ \Score \omit StringNumber }} }}
}}
% MIDI: four high C pulses precede the printed example.
\score {{
  <<
  \new Staff {{ \tempo 4 = {tempo} {COUNT} \melody }}{accompaniment}
  >>
  \midi {{ }}
}}
'''


def base_source(label, title, chords, tempo):
    marks = ' '.join(f'{pname(CHORDS[c][0])}1^\\markup {{ \\small "{c}" }}' for c in chords)
    return HEADER + OVERLAY + rf'''\header {{ title = "{label}. {title} - base" tagline = ##f }}
\paper {{ page-breaking = #ly:one-page-breaking }}
pad = \absolute {{ {padline(chords)} }}
bassline = \absolute {{ {bassline(chords)} }}
\score {{
  \new Staff {{ \clef bass \time 4/4 \key c \major \tempo 4 = {tempo} \absolute {{ {marks} }} \bar "|." }}
  \layout {{ indent = 0 system-count = #1 }}
}}
% MIDI: four high C pulses, then bass and chords without the guitar part.
\score {{
  <<
  \new Staff {{ \tempo 4 = {tempo} {COUNT} }}
  \new Staff {{ \set Staff.midiInstrument = "acoustic grand" r1 \pp \pad }}
  \new Staff {{ \set Staff.midiInstrument = "electric bass (finger)" r1 \mf \bassline }}
  >>
  \midi {{ }}
}}
'''


def main():
    count = 0
    for label, stem, title, chords, events, base in EXAMPLES:
        assert bars(events) == len(chords), label
        for tempo, suffix in TEMPI:
            (ROOT / f'src/lilypond/{stem}{suffix}.ly').write_text(
                source(label, title, chords, events, tempo, base))
            count += 1
            if base:
                (ROOT / f'src/lilypond/{stem}-base{suffix}.ly').write_text(
                    base_source(label, title, chords, tempo))
                count += 1
    print(f'Generated {count} sources; bar lengths and fret ranges validated.')


if __name__ == '__main__':
    main()
