"""Note di rilascio: la pagina esiste, è nell'indice e ha una sezione per la versione attuale.

Copia identica nei tre volumi (Teoria, Pratica, Repertorio). Quando cambia ``VERSIONE`` in
conf.py, aggiungere in ``src/docs/note-di-rilascio.rst`` la sezione «X.Y (dal …)».
"""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / 'src/docs'


class NoteDiRilascioTest(unittest.TestCase):
    def setUp(self):
        self.page = (DOCS / 'note-di-rilascio.rst').read_text(encoding='utf-8')

    def test_in_toctree_and_footer(self):
        index = (DOCS / 'index.rst').read_text(encoding='utf-8')
        self.assertRegex(index, r'(?m)^  note-di-rilascio$')
        self.assertIn(':doc:`note di rilascio <note-di-rilascio>`', index)

    def test_section_for_current_version(self):
        conf = (DOCS / 'conf.py').read_text(encoding='utf-8')
        version = re.search(r'^VERSIONE = "([0-9]+\.[0-9]+)"', conf, re.M).group(1)
        lines = self.page.splitlines()
        headings = [a for a, b in zip(lines, lines[1:]) if b and set(b) == {'-'} and len(b) >= len(a)]
        versions = [h.split(' ')[0] for h in headings if re.match(r'^[0-9]+\.[0-9]+ ', h)]
        self.assertTrue(versions, 'nessuna sezione di versione')
        self.assertEqual(versions[0], version, 'la prima sezione di versione deve essere quella attuale')
        # Versioni dalla più recente.
        key = [tuple(map(int, v.split('.'))) for v in versions]
        self.assertEqual(key, sorted(key, reverse=True))

    def test_dates_newest_first(self):
        months = ['gennaio', 'febbraio', 'marzo', 'aprile', 'maggio', 'giugno', 'luglio', 'agosto',
                  'settembre', 'ottobre', 'novembre', 'dicembre']
        lines = self.page.splitlines()
        dates = []
        for a, b in zip(lines, lines[1:]):
            m = re.match(r'^(\d{1,2}) (\w+) (\d{4})$', a)
            if m and b and set(b) == {'~'}:
                dates.append((int(m.group(3)), months.index(m.group(2)) + 1, int(m.group(1))))
        self.assertEqual(dates, sorted(dates, reverse=True))


if __name__ == '__main__':
    unittest.main()
