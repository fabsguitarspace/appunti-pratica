"""Musical checks for «Ritmo melodico» (R1–R10): bars, register, attack positions."""
from fractions import Fraction as F
import importlib.util
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    'melodic_rhythms', ROOT / 'scripts/generate_melodic_rhythms.py')
gen = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gen)
EXAMPLES = {label: (stem, chords, bars) for label, stem, _, chords, bars in gen.EXAMPLES}
CHORD_PCS = {'Dm7': {2, 5, 9, 0}, 'G7': {7, 11, 2, 5}, 'Cmaj7': {0, 4, 7, 11}}
PAGE = ROOT / 'src/docs/ritmo-melodico.rst'


def attacks(bar):
    """[(onset in quarters from the bar start, event)] for the notes of a bar, ties excluded."""
    out, t = [], F(0)

    def walk(events, scale):
        nonlocal t
        for e in events:
            if e['kind'] == 'tuplet':
                walk(e['items'], scale * F(e['den'], e['num']))
                continue
            if e['kind'] == 'note':
                out.append((t, e))
            t += gen.LENGTHS[e['dur']] * scale
    walk(bar, F(1))
    return out


def tied_heads(bars):
    """Bar-by-bar attacks, without the notes that continue a tie."""
    result, tied = [], False
    for bar in bars:
        current = []
        for onset, e in attacks(bar):
            if not tied:
                current.append((onset, e))
            tied = e['tie']
        result.append(current)
    return result


class MelodicRhythmsTest(unittest.TestCase):
    def test_bars_register_and_frets(self):
        for label, (stem, chords, bars) in EXAMPLES.items():
            with self.subTest(example=label):
                self.assertEqual(len(bars), len(chords))
                for bar in bars:
                    self.assertEqual(sum(gen.length(e) for e in bar), gen.BAR)
                notes = [e for bar in bars for e in gen.notes_of(bar)]
                self.assertGreaterEqual(min(e['pitch'] for e in notes), 55)
                self.assertLessEqual(max(e['pitch'] for e in notes), 76)
                for e in notes:
                    self.assertEqual(gen.OPEN[e['string']] + e['fret'], e['pitch'])

    def test_r1_same_rhythm_r2_three_notes_different_rhythms(self):
        r1 = [[o for o, _ in bar] for bar in tied_heads(EXAMPLES['R1'][2])]
        self.assertTrue(all(b == r1[0] for b in r1))
        self.assertEqual(r1[0], [0, F(3, 2), 2])
        r2 = [[o for o, _ in bar] for bar in tied_heads(EXAMPLES['R2'][2])]
        self.assertTrue(all(len(b) == 3 for b in r2))
        self.assertEqual(len({tuple(b) for b in r2}), 4)

    def test_r3_same_cell_from_four_positions(self):
        bars = tied_heads(EXAMPLES['R3'][2])
        self.assertEqual([b[0][0] for b in bars], [0, F(1, 2), F(3, 2), 2])
        for bar in bars:
            self.assertEqual([e['pitch'] for _, e in bar], gen.CELL)
            onsets = [o for o, _ in bar]
            self.assertEqual([y - x for x, y in zip(onsets, onsets[1:])], [F(1, 2)] * 3)

    def test_r4_anticipations_belong_to_the_next_chord(self):
        _, chords, bars = EXAMPLES['R4']
        for b in (0, 1):
            onset, e = attacks(bars[b])[-1]
            self.assertEqual(onset, F(7, 2))
            self.assertIn(e['pitch'] % 12, CHORD_PCS[chords[b + 1]])
            self.assertNotIn(e['pitch'] % 12, CHORD_PCS[chords[b]] - CHORD_PCS[chords[b + 1]])

    def test_r5_four_of_six_triplets(self):
        for bar in tied_heads(EXAMPLES['R5'][2])[:3]:
            self.assertEqual(len(bar), 4)
            onsets = [o for o, _ in bar]
            self.assertTrue(all((o * 3).denominator == 1 for o in onsets))

    def test_r6_three_beat_cycle_returns_on_one(self):
        bars = EXAMPLES['R6'][2]
        accents = [4 * b + o for b, bar in enumerate(bars) for o, e in attacks(bar) if e['accent']]
        self.assertEqual(accents, [0, 3, 6, 9, 12])
        # Ogni ciclo: quattro crome e una pausa di semiminima.
        heads = [4 * b + o for b, bar in enumerate(bars) for o, _ in attacks(bar)]
        for start in accents[:4]:
            self.assertEqual([h for h in heads if start <= h < start + 3],
                             [start, start + F(1, 2), start + 1, start + F(3, 2)])

    def test_r7_one_line_four_gears(self):
        bars = EXAMPLES['R7'][2]
        line = gen.DORIAN_LINE
        played = lambda bs: [e['pitch'] for bar in bs for e in gen.notes_of(bar)]
        self.assertEqual(played(bars[0:2]), line)   # terzine di semiminima: due battute
        self.assertEqual(played(bars[2:4]), line)   # crome
        self.assertEqual(played(bars[4:5]), line)   # terzine di croma
        self.assertEqual(played(bars[5:6]), line)   # semicrome
        self.assertEqual([o for o, _ in attacks(bars[0])][:3], [0, F(2, 3), F(4, 3)])

    def test_r8_sequence_order_is_kept_when_notes_are_left_out(self):
        bars = EXAMPLES['R8'][2]
        scale = [62, 64, 65, 67, 69, 71, 72, 74, 76]
        played = [e['pitch'] for e in gen.notes_of(bars[0] + bars[1])]
        full = [scale[g + k] for g in range(4) for k in range(4)]
        it = iter(full)
        self.assertTrue(all(p in it for p in played), 'le note restano nell\'ordine della sequenza')
        self.assertLess(len(played), len(full))

    def test_r9_anticipation_and_late_resolution(self):
        _, chords, bars = EXAMPLES['R9']
        onset, e = attacks(bars[1])[-1]
        self.assertEqual((onset, e['pitch'], e['tie']), (F(7, 2), 64, True))
        late = attacks(bars[6])
        self.assertEqual([(o, x['pitch']) for o, x in late], [(0, 65), (1, 64)])

    def test_r10_downbeats_then_upbeats(self):
        bars = tied_heads(EXAMPLES['R10'][2])
        for bar in bars[:2]:
            self.assertTrue(all(o.denominator == 1 for o, _ in bar))
        for bar in bars[2:]:
            self.assertTrue(bar and all(o.denominator == 2 for o, _ in bar))

    def test_sources_and_page(self):
        text = PAGE.read_text()
        for label, (stem, _, _) in EXAMPLES.items():
            with self.subTest(example=label):
                for suffix in ('', '-90'):
                    ly = ROOT / f'src/lilypond/{stem}{suffix}.ly'
                    self.assertTrue(ly.is_file(), ly)
                    src = ly.read_text()
                    self.assertIn('Generated by scripts/generate_melodic_rhythms.py', src)
                    self.assertIn('hhc4', src)
                    self.assertIn(f'_static/music/{stem}{suffix}.mp3', text)
                self.assertIn(f'_static/music/{stem}.*', text)
                self.assertTrue(re.search(rf'\*\*{label}\.', text), f'{label} non citato nella pagina')


if __name__ == '__main__':
    unittest.main()
