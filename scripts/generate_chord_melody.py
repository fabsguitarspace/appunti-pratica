#!/usr/bin/env python3
"""Generate the chord-melody voicing examples of the Accordi chapter.

Run python3 scripts/generate_chord_melody.py, then build the cm-* sources with
build-lilypond.sh --source NAME (repeatable). Generated .ly must not be edited.

Drop 2 and drop 3 voicings are computed from the chord tones and the melody
note; three-voice shapes and the short arrangement are written as explicit
strings and frets. Each note keeps its spelling from the chord degree, so
notation, diagrams, TAB and MIDI share the same data.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OPEN = {6: 40, 5: 45, 4: 50, 3: 55, 2: 59, 1: 64}
LETTERS = 'cdefgab'
NATURAL = {'c': 0, 'd': 2, 'e': 4, 'f': 5, 'g': 7, 'a': 9, 'b': 11}
ACCIDENTAL = {-2: 'ff', -1: 'f', 0: '', 1: 's', 2: 'ss'}
PRINTED = {-2: '𝄫', -1: '♭', 0: '', 1: '♯', 2: '𝄪'}

# Chord qualities: (degree, semitones above the root).
QUALITIES = {
    'maj7': [(1, 0), (3, 4), (5, 7), (7, 11)],
    '6': [(1, 0), (3, 4), (5, 7), (6, 9)],
    '7': [(1, 0), (3, 4), (5, 7), (7, 10)],
    'm7': [(1, 0), (3, 3), (5, 7), (7, 10)],
    'm7(b5)': [(1, 0), (3, 3), (5, 6), (7, 10)],
    'dim7': [(1, 0), (3, 3), (5, 6), (7, 9)],
}
SUFFIX = {'maj7': 'maj7', '6': '6', '7': '7', 'm7': 'm7', 'm7(b5)': 'm7(♭5)', 'dim7': '°7'}


def parse_root(name):
    """'c', 'cs', 'bf' -> (letter, alteration, pitch class)."""
    letter, rest = name[0], name[1:]
    alter = {'': 0, 's': 1, 'f': -1}[rest]
    return letter, alter, (NATURAL[letter] + alter) % 12


def root_label(name):
    letter, alter, _ = parse_root(name)
    return letter.upper() + PRINTED[alter]


def spell(root, degree, semis, pitch):
    """LilyPond absolute name of pitch, spelled as degree of root."""
    letter, _, root_pc = parse_root(root)
    target = LETTERS[(LETTERS.index(letter) + degree - 1) % 7]
    alter = ((root_pc + semis - NATURAL[target] + 6) % 12) - 6
    assert (NATURAL[target] + alter - pitch) % 12 == 0, (root, degree, pitch)
    octave = (pitch - alter) // 12 - 1
    shift = octave - 3
    return target + ACCIDENTAL[alter] + ("'" * shift if shift >= 0 else ',' * -shift)


def voice(string, fret, name):
    return dict(string=string, fret=fret, pitch=OPEN[string] + fret, name=name)


def drop(root, quality, top_pitch, dropped, strings):
    """Close position under top_pitch, then lower voice `dropped` (2 or 3 from the top)."""
    _, _, root_pc = parse_root(root)
    tones = QUALITIES[quality]
    degree_of = {(root_pc + s) % 12: (d, s) for d, s in tones}
    assert top_pitch % 12 in degree_of, (root, quality, top_pitch)
    close = [top_pitch]
    while len(close) < 4:
        p = close[-1] - 1
        while p % 12 not in degree_of or p % 12 in {q % 12 for q in close}:
            p -= 1
        close.append(p)
    close[dropped - 1] -= 12
    pitches = sorted(close)
    voices = []
    for string, pitch in zip(strings, pitches):
        fret = pitch - OPEN[string]
        assert 1 <= fret <= 17, (root, quality, top_pitch, string, fret)
        d, s = degree_of[pitch % 12]
        voices.append(voice(string, fret, spell(root, d, s, pitch)))
    frets = [v['fret'] for v in voices]
    assert max(frets) - min(frets) <= 4, (root, quality, top_pitch, frets)
    return voices


def chord(root, quality, voices, dur='1', label=None, kind='chord'):
    return dict(root=root, quality=quality, voices=voices, dur=dur, kind=kind,
                label=label or root_label(root) + SUFFIX[quality])


def drop2(root, quality, top, dur='1', label=None):
    return chord(root, quality, drop(root, quality, top, 2, (4, 3, 2, 1)), dur, label)


def drop3(root, quality, top, strings, dur='1', label=None):
    return chord(root, quality, drop(root, quality, top, 3, strings), dur, label)


def explicit(root, quality, frets, degrees, dur='1', label=None):
    """Explicit (string, fret) shape; degrees spell each voice from the root."""
    _, _, root_pc = parse_root(root)
    tones = dict(QUALITIES.get(quality, []))
    voices = []
    for (string, fret), degree in zip(frets, degrees):
        pitch = OPEN[string] + fret
        semis = (pitch - root_pc) % 12
        voices.append(voice(string, fret, spell(root, degree, semis, pitch)))
    return chord(root, quality, voices, dur, label)


def note(string, fret, name, dur='4'):
    return dict(kind='note', voices=[voice(string, fret, name)], dur=dur, label=None,
                root=None, quality=None)


G4, A4, B4, C5, E5 = 67, 69, 71, 72, 76

SHEETS = [
    ('cm-drop2-maj7', 'Drop 2 sulle corde 4–3–2–1: Cmaj7',
     [drop2('c', 'maj7', p) for p in (G4, B4, C5, E5)]),
    ('cm-drop2-6', 'Drop 2 sulle corde 4–3–2–1: C6',
     [drop2('c', '6', p) for p in (G4, A4, C5, E5)]),
    ('cm-drop2-7', 'Drop 2 sulle corde 4–3–2–1: C7',
     [drop2('c', '7', p) for p in (G4, 70, C5, E5)]),
    ('cm-drop2-m7', 'Drop 2 sulle corde 4–3–2–1: Cm7',
     [drop2('c', 'm7', p) for p in (G4, 70, C5, 75)]),
    ('cm-drop2-m7b5', 'Drop 2 sulle corde 4–3–2–1: Cm7(♭5)',
     [drop2('c', 'm7(b5)', p) for p in (66, 70, C5, 75)]),
    ('cm-drop2-ii-v-i', 'Drop 2: II–V–I con la melodia al canto',
     [drop2('d', 'm7', C5), drop2('g', '7', B4), drop2('c', 'maj7', B4), drop2('c', '6', A4)]),
    ('cm-drop3', 'Drop 3 con la fondamentale al basso',
     [drop3('c', q, (67 if q in ('maj7', '7', 'm7') else 66), (6, 4, 3, 2))
      for q in ('maj7', '7', 'm7', 'm7(b5)')]
     + [drop3('f', q, (72 if q in ('maj7', '7', 'm7') else 71), (5, 3, 2, 1))
        for q in ('maj7', '7', 'm7', 'm7(b5)')]),
    ('cm-tre-voci', 'Tre voci: basso, nota guida e melodia',
     [explicit('d', 'm7', [(5, 5), (3, 5), (2, 6)], [1, 7, 3]),
      explicit('g', '7', [(6, 3), (3, 4), (2, 6)], [1, 3, 7]),
      explicit('c', 'maj7', [(5, 3), (3, 4), (2, 5)], [1, 7, 3]),
      explicit('c', 'maj7', [(5, 3), (3, 4), (1, 3)], [1, 7, 5])]),
    ('cm-diminuiti-passaggio', 'Diminuiti di passaggio con nota comune al canto',
     [drop2('c', '6', G4, '2'), drop2('cs', 'dim7', G4, '2'),
      drop2('d', 'm7', A4, '2'), drop2('ds', 'dim7', A4, '2'), drop2('e', 'm7', B4)]),
    ('cm-sesta-diminuita', 'Scala di sesta diminuita armonizzata in drop 2',
     [drop2('c', '6', p, '2') if i % 2 == 0 else drop2('b', 'dim7', p, '2')
      for i, p in enumerate((67, 68, 69, 71, 72, 74, 76, 77))]
     + [drop2('c', '6', 79)]),
    ('cm-arrangiamento', 'Chord melody: otto battute originali',
     [explicit('c', 'maj7', [(5, 3), (3, 4), (2, 5)], [1, 7, 3], '2'),
      note(1, 3, "g'"), note(2, 5, "e'"),
      explicit('a', '7', [(6, 5), (5, 4), (1, 3)], [1, 3, 7], '2'),
      note(2, 6, "f'"), note(2, 5, "e'"),
      explicit('d', 'm7', [(5, 5), (3, 5), (2, 6)], [1, 7, 3], '2'),
      note(1, 5, "a'"), note(2, 6, "f'"),
      explicit('g', '7', [(6, 3), (3, 4), (2, 6)], [1, 3, 7], '1'),
      explicit('e', 'm7', [(5, 7), (3, 7), (2, 8)], [1, 7, 3], '2'),
      note(1, 7, "b'"), note(2, 8, "g'"),
      explicit('a', '7', [(6, 5), (4, 5), (3, 6), (1, 6)], [1, 7, 3, 9], '2',
               label='A7(♭9)'),
      note(1, 5, "a'"), note(1, 3, "g'"),
      explicit('d', 'm7', [(5, 5), (3, 5), (2, 6), (1, 5)], [1, 7, 3, 5], '2'),
      explicit('g', '7', [(6, 3), (4, 3), (3, 4), (2, 4)], [1, 7, 3, 13], '2',
               label='G7(♭13)'),
      explicit('c', '6', [(5, 3), (4, 5), (3, 2), (2, 5)], [1, 5, 6, 3], '1')]),
]

# Melody of the arrangement, one entry per event (top voice).
ARRANGEMENT_MELODY = [64, 67, 64, 67, 65, 64, 65, 69, 65, 65, 67, 71, 67, 70, 69, 67, 69, 63, 64]

BEATS = {'1': 4, '2': 2, '4': 1}


def lily_event(event, tag):
    tag_mark = f'^\\{tag}' if tag else ''
    if event['kind'] == 'note':  # duration must precede the string number
        v = event['voices'][0]
        return f"{v['name']}{event['dur']}\\{v['string']}"
    names = ' '.join(f"{v['name']}\\{v['string']}" for v in event['voices'])
    return f'<{names}>' + event['dur'] + tag_mark


def bars(events):
    out, current, count = [], [], 0
    for text, event in events:
        current.append(text)
        count += BEATS[event['dur']]
        if count == 4:
            out.append(' '.join(current))
            current, count = [], 0
    assert not current, 'Incomplete bar'
    return out


def source(stem, title, events):
    diagrams, tokens = [], []
    for i, event in enumerate(events):
        tag = None
        if event['kind'] == 'chord':
            tag = f'diag{chr(65 + len(diagrams))}'
            frets = {v['string']: v['fret'] for v in event['voices']}
            items = ' '.join(f'(place-fret {s} {frets[s]})' if s in frets else f'(mute {s})'
                             for s in range(6, 0, -1))
            diagrams.append(rf'''{tag} = \markup \center-column {{ \small "{event['label']}"
  \fret-diagram-verbose #'({items}) }}''')
        tokens.append((lily_event(event, tag), event))
    measures = bars(tokens)
    systems = max(1, -(-len(measures) // 4))
    return rf"""% Generated by scripts/generate_chord_melody.py; edit the generator.
\version "2.26.0"
\language "english"
\header {{ title = "{title}" tagline = ##f }}
\paper {{ page-breaking = #ly:one-page-breaking line-width = 160\mm ragged-right = ##f }}
{chr(10).join(diagrams)}
melody = \absolute {{ \time 4/4 \key c \major
 {' | '.join(measures)} \bar "|." }}
\score {{
 \new StaffGroup <<
  \new Staff {{ \clef "treble_8" \tempo 4 = 60 \melody }}
  \new TabStaff {{ \set TabStaff.stringTunings = #guitar-tuning \omit TextScript \melody }}
 >>
 \layout {{ indent = 0 system-count = #{systems}
  \context {{ \Voice \override TextScript.staff-padding = #4 }}
  \context {{ \Score \omit StringNumber }} }}
}}
\score {{ \new Staff {{ \tempo 4 = 60 c'''4\p c''' c''' c''' \melody }} \midi {{ }} }}
"""


def main():
    for stem, title, events in SHEETS:
        (ROOT / 'src/lilypond' / f'{stem}.ly').write_text(source(stem, title, events))
    total = sum(1 for _, _, e in SHEETS for x in e if x['kind'] == 'chord')
    print(f'Generated {len(SHEETS)} chord-melody sources, {total} voicings.')


if __name__ == '__main__':
    main()
