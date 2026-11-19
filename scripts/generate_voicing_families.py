#!/usr/bin/env python3
"""Generate the voicing-family examples of the Accordi chapter (analysis 024).

Run python3 scripts/generate_voicing_families.py, then build the vf-* sources with
build-lilypond.sh --source NAME (repeatable). Generated .ly must not be edited.

Four-voice families come from a close-position chord under a melody note: drop 2
lowers the second voice from the top by an octave, drop 3 the third, drop 2 and 4
the second and the fourth. Spelling, diagrams, TAB and MIDI reuse the helpers of
generate_chord_melody.py, so both scripts share one notation.
"""
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location('cm', ROOT / 'scripts/generate_chord_melody.py')
cm = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(cm)

# Family -> voices lowered by an octave, counted from the top. Triads: close (`triad`) or with
# the middle voice lowered (`spread`); rootless voicings are drop 2 of four colour tones.
DROPPED = {'drop2': (2,), 'drop3': (3,), 'drop24': (2, 4), 'triad': (), 'spread': (2,),
           'rootless': (2,)}

# Triads are not in the chord-melody catalogue: add them here (same notation helpers).
cm.QUALITIES.setdefault('maj', [(1, 0), (3, 4), (5, 7)])
cm.QUALITIES.setdefault('m', [(1, 0), (3, 3), (5, 7)])
cm.SUFFIX.setdefault('maj', '')
cm.SUFFIX.setdefault('m', 'm')

# Rootless voicings (analysis 024, ADR 0015 of appunti-strumenti): guide tones plus two colours;
# on the dominant the 13th replaces the 5th, on m7(b5) the natural 9th replaces the root.
# Same notes as ROOTLESS in appunti-strumenti/js/voicings.js.
ROOTLESS = {
    'maj7': [(3, 4), (5, 7), (7, 11), (9, 2)],
    '6': [(3, 4), (5, 7), (6, 9), (9, 2)],
    '7': [(3, 4), (13, 9), (7, 10), (9, 2)],
    'm7': [(3, 3), (5, 7), (7, 10), (9, 2)],
    'm7(b5)': [(3, 3), (5, 6), (7, 10), (9, 2)],
}


def drop(root, quality, top_pitch, family, strings, dur='1', label=None):
    """Close position under top_pitch, then lower the voices of the family."""
    _, _, root_pc = cm.parse_root(root)
    tones = ROOTLESS[quality] if family == 'rootless' else cm.QUALITIES[quality]
    degree_of = {(root_pc + s) % 12: (d, s) for d, s in tones}
    assert top_pitch % 12 in degree_of, (root, quality, top_pitch)
    close = [top_pitch]
    while len(close) < len(tones):
        p = close[-1] - 1
        while p % 12 not in degree_of or p % 12 in {q % 12 for q in close}:
            p -= 1
        close.append(p)
    for rank in DROPPED[family]:
        close[rank - 1] -= 12
    voices = []
    for string, pitch in zip(strings, sorted(close)):
        fret = pitch - cm.OPEN[string]
        assert 1 <= fret <= 17, (root, quality, top_pitch, string, fret)
        d, s = degree_of[pitch % 12]
        voices.append(cm.voice(string, fret, cm.spell(root, d, s, pitch)))
    frets = [v['fret'] for v in voices]
    assert max(frets) - min(frets) <= 4, (root, quality, top_pitch, frets)
    event = cm.chord(root, quality, voices, dur, label)
    event['family'] = family
    event['tones'] = tones
    return event


def shell(root, quality, frets, degrees, dur='1', label=None):
    event = cm.explicit(root, quality, frets, degrees, dur, label)
    event['family'] = 'shell'
    event['tones'] = cm.QUALITIES[quality]
    return event


def fixed(root, quality, family, shape, degrees, label=None, dur='1'):
    """Explicit (string, fret) shape spelled by degree: upper structures, fourths, clusters.

    Tensions (9, 11, 13 and their alterations) are spelled from the degree, like the tool
    (♯9 is D♯ on C). `tones` keeps (degree, semitones) for the tests."""
    event = cm.explicit(root, quality, shape, degrees, dur, label)
    _, _, root_pc = cm.parse_root(root)
    event['family'] = family
    event['tones'] = [(d, (v['pitch'] - root_pc) % 12) for d, v in zip(degrees, event['voices'])]
    return event


QUALITIES = ('maj7', '7', 'm7', 'm7(b5)')


def top_for(root, quality, degree):
    """Pitch of `degree` of the chord inside the octave above G3 (55)."""
    _, _, root_pc = cm.parse_root(root)
    semis = dict(cm.QUALITIES[quality])[degree]
    pc = (root_pc + semis) % 12
    return next(p for p in range(55, 80) if p % 12 == pc)


SHEETS = [
    ('vf-confronto', 'Cmaj7 con il Do all’VIII tasto: shell, drop 2, drop 3, drop 2 e 4',
     [shell('c', 'maj7', [(6, 8), (4, 9), (3, 9)], [1, 7, 3], label='Shell'),
      drop('c', 'maj7', 64, 'drop2', (6, 5, 4, 3), label='Drop 2'),
      drop('c', 'maj7', 67, 'drop3', (6, 4, 3, 2), label='Drop 3'),
      drop('c', 'maj7', 71, 'drop24', (6, 5, 3, 2), label='Drop 2 e 4')]),
    ('vf-drop2-gruppi', 'Drop 2 con la fondamentale al basso sulle corde 5–4–3–2 e 6–5–4–3',
     [drop('c', q, top_for('c', q, 3), 'drop2', (5, 4, 3, 2)) for q in QUALITIES]
     + [drop('g', q, top_for('g', q, 3), 'drop2', (6, 5, 4, 3)) for q in QUALITIES]),
    ('vf-drop2-ii-v-i', 'Drop 2 sulle corde 5–4–3–2: II–V–I d’accompagnamento',
     [drop('d', 'm7', 65, 'drop2', (5, 4, 3, 2)),
      drop('g', '7', 65, 'drop2', (5, 4, 3, 2)),
      drop('c', 'maj7', 64, 'drop2', (5, 4, 3, 2)),
      drop('c', '6', 64, 'drop2', (5, 4, 3, 2))]),
    ('vf-drop24', 'Drop 2 e 4 con la fondamentale al basso',
     [drop('c', q, top_for('c', q, 7) + 12, 'drop24', (6, 5, 3, 2)) for q in QUALITIES]
     + [drop('f', q, top_for('f', q, 7) + 12, 'drop24', (5, 4, 2, 1)) for q in QUALITIES]),
    ('vf-triadi-strette', 'Triadi strette: Do maggiore sulle corde 3–2–1, Do minore sulle corde 4–3–2',
     [drop('c', 'maj', p, 'triad', (3, 2, 1)) for p in (67, 72, 76)]
     + [drop('c', 'm', p, 'triad', (4, 3, 2)) for p in (63, 67, 72)]),
    ('vf-triadi-late', 'Triadi late: Do maggiore sulle corde 6–4–3 e 4–2–1',
     [drop('c', 'maj', p, 'spread', (6, 4, 3)) for p in (60, 64, 67)]
     + [drop('c', 'maj', p, 'spread', (4, 2, 1)) for p in (67, 72, 76)]),
    ('vf-triadi-ii-v-i', 'Triadi strette sulle corde 3–2–1: II–V–I',
     [drop('d', 'm', 65, 'triad', (3, 2, 1)), drop('g', 'maj', 67, 'triad', (3, 2, 1)),
      drop('c', 'maj', 67, 'triad', (3, 2, 1)), drop('c', 'maj', 72, 'triad', (3, 2, 1))]),
    ('vf-senza-fondamentale', 'Senza fondamentale: terza al basso (5–4–3–2), settima al basso (4–3–2–1)',
     [drop('c', 'maj7', 67, 'rootless', (5, 4, 3, 2)), drop('c', '7', 69, 'rootless', (5, 4, 3, 2)),
      drop('c', 'm7', 67, 'rootless', (5, 4, 3, 2)), drop('c', 'm7(b5)', 66, 'rootless', (5, 4, 3, 2))]
     + [drop('c', q, 74, 'rootless', (4, 3, 2, 1)) for q in QUALITIES]),
    ('vf-senza-fondamentale-ii-v-i', 'Senza fondamentale sulle corde 4–3–2–1: II–V–I nelle due forme',
     [drop('d', 'm7', 69, 'rootless', (4, 3, 2, 1)), drop('g', '7', 69, 'rootless', (4, 3, 2, 1)),
      drop('c', 'maj7', 67, 'rootless', (4, 3, 2, 1)), drop('c', 'maj7', 67, 'rootless', (4, 3, 2, 1)),
      drop('d', 'm7', 76, 'rootless', (4, 3, 2, 1)), drop('g', '7', 76, 'rootless', (4, 3, 2, 1)),
      drop('c', 'maj7', 74, 'rootless', (4, 3, 2, 1)), drop('c', 'maj7', 74, 'rootless', (4, 3, 2, 1))]),
    ('vf-strutture-superiori', 'Strutture superiori: una triade maggiore sopra la nota guida',
     [fixed('c', 'maj7', 'ust', [(5, 7), (4, 5), (3, 4), (2, 3)], [3, 5, 7, 9], 'Cmaj9'),
      fixed('c', 'maj7', 'ust', [(4, 2), (3, 2), (2, 3), (1, 2)], [3, 13, 9, 11], 'Cmaj7(♯11)'),
      fixed('c', 'm7', 'ust', [(5, 6), (4, 8), (3, 7), (2, 6)], [3, 7, 9, 11], 'Cm11'),
      fixed('c', '7', 'ust', [(4, 8), (3, 7), (2, 7), (1, 5)], [7, 9, 11, 13], 'C13(♯11)')]),
    ('vf-strutture-superiori-alterate', 'Strutture superiori alterate sul dominante e risoluzione',
     [fixed('c', '7', 'ust', [(4, 8), (3, 6), (2, 5), (1, 5)], [7, 9, 3, 13], 'C13(♭9)'),
      fixed('c', '7', 'ust', [(4, 8), (3, 5), (2, 4), (1, 4)], [7, 1, 9, 13], 'C7(♯9♭13)'),
      fixed('c', '7', 'ust', [(4, 2), (3, 3), (2, 2), (1, 2)], [3, 7, 9, 11], 'C7(♭9♯11)'),
      drop('f', 'maj7', 67, 'rootless', (4, 3, 2, 1), label='Fmaj9')]),
    ('vf-quarte', 'Voicing per quarte',
     [fixed('c', 'm7', 'quartal', [(5, 3), (4, 3), (3, 3), (2, 4), (1, 3)], [1, 11, 7, 3, 5], 'Cm11'),
      fixed('c', 'm7', 'quartal', [(4, 5), (3, 5), (2, 6), (1, 6)], [5, 1, 11, 7], 'Cm11'),
      fixed('c', 'maj7', 'quartal', [(5, 2), (4, 2), (3, 2), (2, 3)], [7, 3, 13, 9], 'Cmaj13'),
      fixed('c', '7', 'quartal', [(4, 2), (3, 2), (2, 3)], [3, 13, 9], 'C13')]),
    ('vf-quarte-modale', 'Quarte in Re dorico: Dm7 ed Em7 con il voicing So What',
     [fixed('d', 'm7', 'quartal', [(5, 5), (4, 5), (3, 5), (2, 6), (1, 5)], [1, 11, 7, 3, 5], 'Dm11'),
      fixed('e', 'm7', 'quartal', [(5, 7), (4, 7), (3, 7), (2, 8), (1, 7)], [1, 11, 7, 3, 5], 'Em11'),
      fixed('d', 'm7', 'quartal', [(5, 5), (4, 5), (3, 5), (2, 6), (1, 5)], [1, 11, 7, 3, 5], 'Dm11'),
      fixed('d', 'm7', 'quartal', [(5, 5), (4, 5), (3, 5), (2, 6), (1, 5)], [1, 11, 7, 3, 5], 'Dm11')]),
    ('vf-cluster', 'Cluster: seconde fra le voci',
     [fixed('c', 'maj7', 'cluster', [(4, 5), (3, 7), (2, 5), (1, 7)], [5, 9, 3, 7], 'Cmaj9'),
      fixed('c', '6', 'cluster', [(4, 5), (3, 7), (2, 5), (1, 5)], [5, 9, 3, 6], 'C6/9'),
      fixed('c', '7', 'cluster', [(4, 8), (3, 5), (2, 5), (1, 5)], [7, 1, 3, 13], 'C13'),
      fixed('c', 'm7', 'cluster', [(5, 6), (4, 3), (3, 3), (2, 3)], [3, 11, 7, 9], 'Cm11')]),
]


def main():
    for stem, title, events in SHEETS:
        text = cm.source(stem, title, events).replace(
            'generate_chord_melody.py', 'generate_voicing_families.py', 1)
        (ROOT / 'src/lilypond' / f'{stem}.ly').write_text(text)
    total = sum(len(events) for _, _, events in SHEETS)
    print(f'Generated {len(SHEETS)} voicing-family sources, {total} voicings.')


if __name__ == '__main__':
    main()
