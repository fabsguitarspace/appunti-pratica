"""Note, posizioni e collegamenti dei materiali aggiunti a Scale, Arpeggi e Accordi."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
LY = ROOT / 'src/lilypond'
DOCS = ROOT / 'src/docs'
MUSIC = DOCS / '_static/music'
OPEN = {6: 40, 5: 45, 4: 50, 3: 55, 2: 59, 1: 64}
PC = {'c': 0, 'd': 2, 'e': 4, 'f': 5, 'g': 7, 'a': 9, 'b': 11}

# Sorgente -> (classi di altezza in salita da Do, documento che la usa)
SCALES = {
    'scala-pentatonica-maggiore-verticale-c1': ([0, 2, 4, 7, 9], '4-scale.rst'),
    'scala-pentatonica-minore-verticale-c1': ([0, 3, 5, 7, 10], '4-scale.rst'),
    'scala-blues-verticale-c1': ([0, 3, 5, 6, 7, 10], '4-scale.rst'),
    'scala-bebop-dominante-verticale-c1': ([0, 2, 4, 5, 7, 9, 10, 11], '4-scale.rst'),
    'scala-bebop-maggiore-verticale-c1': ([0, 2, 4, 5, 7, 8, 9, 11], '4-scale.rst'),
    **{k[:-1] + '2': v for k, v in {
        'scala-pentatonica-maggiore-verticale-c1': ([0, 2, 4, 7, 9], '4-scale.rst'),
        'scala-pentatonica-minore-verticale-c1': ([0, 3, 5, 7, 10], '4-scale.rst'),
        'scala-blues-verticale-c1': ([0, 3, 5, 6, 7, 10], '4-scale.rst'),
        'scala-bebop-dominante-verticale-c1': ([0, 2, 4, 5, 7, 9, 10, 11], '4-scale.rst'),
        'scala-bebop-maggiore-verticale-c1': ([0, 2, 4, 5, 7, 8, 9, 11], '4-scale.rst'),
    }.items()},
    'arpeggio-cm7f5-1': ([0, 3, 6, 10], '5-arpeggi.rst'),
    'arpeggio-cm7f5-2': ([0, 3, 6, 10], '5-arpeggi.rst'),
}
CHORDS = {
    'accordi-f-maggiore-13-1': 74,   # Re al canto, prima corda decimo tasto
    'accordi-f-maggiore-maj7-1': 76,  # Mi al canto, prima corda dodicesimo tasto
}
F_MAJOR_PCS = {5, 9, 0, 4, 2, 7, 11}  # F A C E D G B (6, 9, 13, ♯11)


def pitch_class(token):
    name = token.rstrip("',0123456789-")
    base = PC[name[0]]
    rest = name[1:]
    return (base + rest.count('s') - rest.count('f')) % 12


def lines(stem):
    text = (LY / f'{stem}.ly').read_text(encoding='utf-8')
    body = text[text.index('musica ='):text.index('\\score')]
    return [l.strip() for l in body.splitlines() if re.match(r'\s*c', l)]


class MaterialiAggiuntiTest(unittest.TestCase):
    def test_scales_and_arpeggios_have_expected_notes(self):
        for stem, (pcs, _) in SCALES.items():
            with self.subTest(stem=stem):
                rows = lines(stem)
                self.assertTrue(rows)
                for row in rows:
                    notes = [t for t in row.split() if t[0] in PC]
                    ascending = []
                    for t in notes:
                        p = pitch_class(t)
                        if ascending and p == ascending[0]:
                            break
                        ascending.append(p)
                    self.assertEqual(ascending, pcs)
                    self.assertEqual({pitch_class(t) for t in notes}, set(pcs))

    def test_positions_are_distinct(self):
        for stem in SCALES:
            text = (LY / f'{stem}.ly').read_text(encoding='utf-8')
            frets = re.findall(r'minimumFret = #(\d+)', text)
            self.assertEqual(len(frets), len(set(frets)), stem)

    def test_major_voicings_keep_soprano_and_span(self):
        for stem, top in CHORDS.items():
            with self.subTest(stem=stem):
                text = (LY / f'{stem}.ly').read_text(encoding='utf-8')
                diagrams = re.findall(r"diag[A-Z] = \\markup \\fret-diagram-verbose #'\((.*?)\)\n\s*\)",
                                      text, re.S)
                self.assertGreaterEqual(len(diagrams), 4)
                for d in diagrams:
                    voices = [(int(s), int(f)) for s, f in re.findall(r'place-fret (\d) (\d+)', d)]
                    pitches = [OPEN[s] + f for s, f in voices]
                    self.assertEqual(pitches, sorted(pitches))
                    self.assertEqual(max(pitches), top)
                    self.assertEqual(voices[-1][0], 1)
                    frets = [f for s, f in voices]
                    self.assertLessEqual(max(frets) - min(frets), 4)
                    self.assertTrue({p % 12 for p in pitches} <= F_MAJOR_PCS)
                    self.assertIn(9, {p % 12 for p in pitches})  # la terza La

    def test_documents_reference_built_media(self):
        stems = list(SCALES) + list(CHORDS)
        docs = {'4-scale.rst', '5-arpeggi.rst', '6-accordi.rst'}
        text = {d: (DOCS / d).read_text(encoding='utf-8') for d in docs}
        for stem in stems:
            with self.subTest(stem=stem):
                self.assertTrue(any(f'_static/music/{stem}.' in t for t in text.values()))
                for ext in ('svg', 'pdf', 'mp3'):
                    self.assertTrue((MUSIC / f'{stem}.{ext}').is_file(), f'{stem}.{ext}')


class StudiScaleDerivateTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import importlib.util
        spec = importlib.util.spec_from_file_location(
            'advanced_scales', ROOT / 'scripts/generate_advanced_scales.py')
        cls.gen = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.gen)

    def test_bebop_descents_put_chord_tones_on_beats(self):
        events = self.gen.DERIVED[1][1]
        pitches = [e['pitch'] for e in events]
        for start, chord in [(0, {0, 4, 7, 10}), (24, {0, 4, 7, 9})]:
            bar = pitches[start:start + 8]
            self.assertTrue(all(p % 12 in chord for p in bar[0::2]), bar)
            self.assertFalse(any(p % 12 in chord for p in bar[1::2]), bar)

    def test_blues_study_uses_blues_scale_and_major_third(self):
        pcs = {e['pitch'] % 12 for e in self.gen.DERIVED[0][1] if e['pitch'] is not None}
        self.assertEqual(pcs, {0, 3, 4, 5, 6, 7, 10})

    def test_studies_are_generated_built_and_referenced(self):
        doc = (DOCS / '4-scale.rst').read_text(encoding='utf-8')
        for n in ('01', '02'):
            for suffix in ('', '-90'):
                stem = f'scale-derivate-{n}{suffix}'
                self.assertTrue((LY / f'{stem}.ly').is_file(), stem)
                self.assertTrue((MUSIC / f'{stem}.mp3').is_file(), stem)
                self.assertIn(f'_static/music/{stem}.mp3', doc)
            self.assertTrue((MUSIC / f'scale-derivate-{n}.svg').is_file())


if __name__ == '__main__':
    unittest.main()
