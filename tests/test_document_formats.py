"""Regression: score alternatives select SVG for web and PDF for LaTeX.
No ImageMagick or TeX executable is needed: exercise the failing Sphinx stage.
"""
from pathlib import Path
import tempfile,subprocess,sys,re,shutil
ROOT=Path(__file__).resolve().parents[1]
# Check the real directives, including pages nested under autori/.
for root in [ROOT,ROOT.parent/'appunti-teoria']:
 for path in (root/'src/docs').rglob('*.rst'):
  for target in re.findall(r'^\.\. image::\s+([^\n]+)',path.read_text(),re.MULTILINE):
   if '_static/music/' not in target:continue
   if target.endswith(('.png','.jpg','.jpeg','.gif')):continue
   assert target.endswith('.*'),(path,target)
   base=path.parent/target[:-2]
   assert base.with_suffix('.svg').is_file() and base.with_suffix('.pdf').is_file(),(path,target)
with tempfile.TemporaryDirectory(prefix='sphinx-score-formats-') as tmp:
 root=Path(tmp);src=root/'source';src.mkdir();(src/'autori').mkdir()
 (src/'conf.py').write_text('''project = 'Score formats'
author = 'Test'
copyright = 'Test'
version = release = '1.0'
extensions = ['sphinx.ext.imgconverter']
image_converter = 'converter-must-not-be-invoked'
epub_publisher = 'Test'
epub_identifier = 'https://example.invalid/score-formats'
epub_scheme = 'URL'
''')
 assets=ROOT/'src/docs/_static/music'
 for ext in ['svg','pdf']:shutil.copyfile(assets/f'modern-groove-44.{ext}',src/f'score.{ext}')
 (src/'index.rst').write_text('Score formats\n=============\n\n.. image:: score.*\n\n.. toctree::\n\n   autori/example\n')
 (src/'autori/example.rst').write_text('Nested score\n============\n\n.. image:: ../score.*\n')
 for builder in ['html','latex','epub']:
  out=root/builder
  result=subprocess.run([sys.executable,'-m','sphinx','-E','-b',builder,'-W','-d',str(root/'doctrees'/builder),str(src),str(out)],capture_output=True,text=True)
  assert result.returncode==0,(builder,result.stdout,result.stderr)
  if builder=='latex':
   tex=''.join(p.read_text() for p in out.glob('*.tex'))
   assert '{score}.pdf' in tex and '{score}.png' not in tex and '{score}.svg' not in tex
  else:assert (out/'_images/score.svg').is_file(),builder
print('PASS: real score pairs exist; HTML/EPUB select SVG and LaTeX selects existing PDF without a converter, including nested pages')
