#!/usr/bin/env python3
"""Generate the examples of «Ritmo melodico» (R1–R10) at 60 and 90 BPM.

Run python3 scripts/generate_melodic_rhythms.py, then build_music.py with --source
for every ritmo-* stem it writes (each at 60 and 90 BPM). Generated .ly files are
not edited manually. No third-party Python dependencies.

Every example has the guitar part (staff and TAB) and, in the MIDI only, a soft pad,
a bass on the roots and a closed hi-hat on beats 2 and 4, so that the position of
each attack in the bar can be heard. Pitches are MIDI numbers at sounding pitch:
60 is the middle C (Do4). Durations are fractions of a quarter note.
"""
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OPEN = {1: 64, 2: 59, 3: 55, 4: 50, 5: 45, 6: 40}
# Fifth position (frets 5–9), with the first string up to the 12th fret.
STRINGS = {55: 4, 57: 4, 58: 4, 59: 4, 60: 3, 61: 3, 62: 3, 63: 3, 64: 2, 65: 2, 66: 2,
           67: 2, 69: 1, 70: 1, 71: 1, 72: 1, 74: 1, 76: 1}
NAMES = {0: 'c', 1: 'cs', 2: 'd', 3: 'ef', 4: 'e', 5: 'f', 6: 'fs', 7: 'g', 8: 'af',
         9: 'a', 10: 'bf', 11: 'b'}
TEMPI = [(60, ''), (90, '-90')]
BAR = F(4)

# Root of the bass and a two-note shell (third and seventh).
CHORDS = {'Cmaj7': (48, (52, 59)), 'Dm7': (50, (53, 60)), 'G7': (43, (53, 59))}

LENGTHS = {'1': F(4), '2.': F(3), '2': F(2), '4.': F(3, 2), '4': F(1), '8.': F(3, 4),
           '8': F(1, 2), '16': F(1, 4)}


def pname(pitch):
    octave = pitch // 12 - 4
    return NAMES[pitch % 12] + ("'" * octave if octave >= 0 else ',' * -octave)


def n(pitch, dur='8', *, mark='', accent=False, tie=False):
    """A note: written duration, optional text above, accent, tie to the next note."""
    string = STRINGS[pitch]
    fret = pitch - OPEN[string]
    assert 0 <= fret <= 12, (pitch, string)
    return dict(kind='note', pitch=pitch, dur=dur, string=string, fret=fret,
                mark=mark, accent=accent, tie=tie)


def r(dur='8'):
    return dict(kind='rest', dur=dur)


def tup(num, den, *items):
    """Tuplet: `num` written notes in the time of `den` (3, 2 = triplet)."""
    return dict(kind='tuplet', num=num, den=den, items=list(items))


def length(event, scale=F(1)):
    if event['kind'] == 'tuplet':
        inner = F(event['den'], event['num'])
        return sum(length(e, scale * inner) for e in event['items'])
    return LENGTHS[event['dur']] * scale


def eighths(pitches, **first):
    """Consecutive eighth notes; keyword arguments go to the first one."""
    return [n(p, '8', **(first if i == 0 else {})) for i, p in enumerate(pitches)]


def notes_of(events):
    for e in events:
        if e['kind'] == 'tuplet':
            yield from notes_of(e['items'])
        elif e['kind'] == 'note':
            yield e


# Lines used by more than one example.
CELL = [64, 67, 71, 74]                                     # Mi–Sol–Si–Re: Em7, 3–5–7–9 di Cmaj7
DORIAN_LINE = [62, 65, 69, 72, 71, 69, 67, 65, 64, 62, 60, 57]  # dodici note su Dm7
CADENCE = ['Dm7', 'G7', 'Cmaj7', 'Cmaj7']

# label, stem, title, chords per bar, bars (lists of events)
EXAMPLES = [
    ('R1', 'ritmo-01', 'Tre note per battuta, lo stesso ritmo', CADENCE, [
        [n(65, '4', mark='Dm7'), r('8'), n(69), n(72, '4'), r('4')],
        [n(71, '4', mark='G7'), r('8'), n(67), n(65, '4'), r('4')],
        [n(64, '4', mark='Cmaj7'), r('8'), n(67), n(71, '4'), r('4')],
        [n(72, '4'), r('8'), n(71), n(67, '4'), r('4')],
    ]),
    ('R2', 'ritmo-02', 'Tre note per battuta, ritmi diversi', CADENCE, [
        [r('8'), n(65, mark='Dm7'), n(69), n(72), r('2')],
        [r('4'), r('8'), n(71, mark='G7'), n(67, '4'), n(65, '4')],
        [n(64, '4.', mark='Cmaj7'), n(67), n(71, '2')],
        [r('4'), n(72, '4'), r('8'), n(71), n(67, '4')],
    ]),
    ('R3', 'ritmo-03', 'Quattro crome da quattro punti della battuta', ['Cmaj7'] * 4, [
        eighths(CELL, mark='sull\'1') + [r('2')],
        [r('8')] + eighths(CELL, mark='«e» dell\'1') + [r('8'), r('4')],
        [r('4'), r('8')] + eighths(CELL, mark='«e» del 2') + [r('8')],
        [r('2')] + eighths(CELL, mark='sul 3'),
    ]),
    ('R4', 'ritmo-04', 'Partenza sull\'«e» del 4: l\'accordo arriva prima', CADENCE, [
        [n(69, '4', mark='Dm7'), n(65, '4'), r('4'), r('8'), n(71, mark='anticipo')],
        [n(67, mark='G7'), n(65), n(62), r('8'), r('4'), r('8'), n(64, mark='anticipo')],
        [n(67, mark='Cmaj7'), n(71), n(72), r('8'), r('2')],
        [n(64, '2'), r('2')],
    ]),
    ('R5', 'ritmo-05', 'Terzine: quattro note su sei', CADENCE, [
        [tup(3, 2, n(62, mark='Dm7'), n(65), n(69)), tup(3, 2, n(72), r(), r()), r('2')],
        [r('4'), tup(3, 2, r(), n(71, mark='G7'), n(69)), tup(3, 2, n(67), n(65), r()), r('4')],
        [r('2'), tup(3, 2, n(64, mark='Cmaj7'), n(67), n(71)), tup(3, 2, n(69), r(), r())],
        [n(67, '2'), r('2')],
    ]),
    ('R6', 'ritmo-06', 'Un ciclo di tre pulsazioni sopra il 4/4', CADENCE, [
        eighths([72, 69, 65, 62], accent=True, mark='Dm7') + [r('4'), n(71, accent=True), n(67)],
        [n(65, mark='G7'), n(62), r('4')] + eighths([69, 65, 62, 59], accent=True),
        [r('4')] + eighths([71, 67, 64, 60], accent=True, mark='Cmaj7') + [r('4')],
        eighths([72, 71, 67, 64], accent=True, mark='di nuovo sull\'1') + [r('2')],
    ]),
    ('R7', 'ritmo-07', 'La stessa linea in quattro marce', ['Dm7'] * 6, [
        [tup(3, 2, *[n(p, '4', mark='terzine di semiminima' if i == 0 else '') for i, p in enumerate(DORIAN_LINE[:3])]),
         tup(3, 2, *[n(p, '4') for p in DORIAN_LINE[3:6]])],
        [tup(3, 2, *[n(p, '4') for p in DORIAN_LINE[6:9]]), tup(3, 2, *[n(p, '4') for p in DORIAN_LINE[9:]])],
        eighths(DORIAN_LINE[:8], mark='crome'),
        eighths(DORIAN_LINE[8:]) + [r('2')],
        [tup(3, 2, *eighths(DORIAN_LINE[k:k + 3], **({'mark': 'terzine'} if k == 0 else {}))) for k in range(0, 12, 3)],
        [n(p, '16', mark='semicrome' if i == 0 else '') for i, p in enumerate(DORIAN_LINE)] + [r('4')],
    ]),
    ('R8', 'ritmo-08', 'Una sequenza di scala con note tolte e pause', ['Dm7'] * 4, [
        eighths([62, 64, 65, 67, 64, 65, 67, 69], mark='sequenza intera'),
        [n(65, mark='note tolte'), r('8'), n(69), n(71), n(67), r('8'), n(71), n(72)],
        [n(69, '4', mark='note lunghe'), n(72), n(74), r('8'), n(72), n(74), n(76)],
        [n(74), n(72), n(69, '4'), r('2')],
    ]),
    ('R9', 'ritmo-09', 'Anticipare e ritardare la risoluzione', CADENCE * 2, [
        eighths([65, 69, 72, 69], mark='Dm7') + [n(65, '4'), r('4')],
        eighths([71, 67, 65, 62], mark='G7') + [r('4'), r('8'), n(64, mark='anticipo', tie=True)],
        [n(64, '2.', mark='Cmaj7'), r('4')],
        [r('1')],
        eighths([62, 65, 69, 72], mark='Dm7') + [n(71, '4'), r('4')],
        eighths([71, 69, 67, 65, 62, 65, 67, 69], mark='G7'),
        [n(65, '4', mark='Cmaj7: ritardo'), n(64, '2.')],
        [r('1')],
    ]),
    ('R10', 'ritmo-10', 'Semiminime in battere e in levare', CADENCE, [
        [n(62, '4', mark='Dm7: in battere'), n(65, '4'), r('4'), n(69, '4')],
        [n(71, '4', mark='G7'), r('4'), n(67, '4'), n(65, '4')],
        [r('8'), n(64, '4', mark='Cmaj7: in levare'), n(67, '4'), n(71, '4'), n(69, tie=True)],
        [n(69), n(67, '4'), n(64, '4'), r('8'), r('4')],
    ]),
]


def token(e):
    if e['kind'] == 'tuplet':
        inner = ' '.join(token(x) for x in e['items'])
        return f"\\tuplet {e['num']}/{e['den']} {{ {inner} }}"
    if e['kind'] == 'rest':
        return f"r{e['dur']}"
    t = f"{pname(e['pitch'])}{e['dur']}\\{e['string']}"
    if e['accent']:
        t += '->'
    if e['mark']:
        t += f'^\\markup {{ \\small "{e["mark"]}" }}'
    if e['tie']:
        t += '~'
    return t


def music(bars):
    lines = []
    for i, bar in enumerate(bars):
        total = sum(length(e) for e in bar)
        assert total == BAR, f'battuta {i + 1}: {total}'
        lines.append(' '.join(token(e) for e in bar) + ' |')
    return '\n  '.join(lines)


def bassline(chords):
    return ' '.join(f'{pname(CHORDS[c][0])}1' for c in chords)


def padline(chords):
    return ' '.join('<' + ' '.join(pname(p) for p in CHORDS[c][1]) + '>1' for c in chords)


HEADER = r'''% Generated by scripts/generate_melodic_rhythms.py; edit the generator.
\version "2.26.0"
\language "english"
% soundfont-overlay: sf/PracticeRhythm.sf2
'''
COUNT = r"c'''4\p c''' c''' c'''"


def source(label, title, chords, bars, tempo):
    hats = ' '.join(['r4 hhc4 r4 hhc4'] * len(chords))
    return HEADER + rf'''\header {{ title = "{label}. {title}" tagline = ##f }}
\paper {{ page-breaking = #ly:one-page-breaking }}
melody = \absolute {{
  \time 4/4 \key c \major
  {music(bars)}
  \bar "|."
}}
pad = \absolute {{ {padline(chords)} }}
bassline = \absolute {{ {bassline(chords)} }}
\score {{
  \new StaffGroup <<
    \new Staff {{ \clef "treble_8" \tempo 4 = {tempo} \melody }}
    \new TabStaff {{ \set TabStaff.stringTunings = #guitar-tuning \omit TextScript \melody }}
  >>
  \layout {{ indent = 0
    \context {{ \Score \omit StringNumber }} }}
}}
% MIDI: four high C pulses precede the printed example; pad, bass and hi-hat on 2 and 4.
\score {{
  <<
  \new Staff {{ \tempo 4 = {tempo} {COUNT} \melody }}
  \new Staff {{ \set Staff.midiInstrument = "acoustic grand" r1 \pp \pad }}
  \new Staff {{ \set Staff.midiInstrument = "electric bass (finger)" r1 \mf \bassline }}
  \new DrumStaff {{ \drummode {{ r1 \p {hats} }} }}
  >>
  \midi {{ }}
}}
'''


def main():
    count = 0
    for label, stem, title, chords, bars in EXAMPLES:
        assert len(bars) == len(chords), label
        music(bars)
        for tempo, suffix in TEMPI:
            (ROOT / f'src/lilypond/{stem}{suffix}.ly').write_text(source(label, title, chords, bars, tempo))
            count += 1
    print(f'Generated {count} sources; bar lengths and fret ranges validated.')


if __name__ == '__main__':
    main()
