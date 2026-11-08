from pathlib import Path
import tempfile, shutil, subprocess, os, json, sys
with tempfile.TemporaryDirectory(prefix='music-check-') as tmp:
 r=Path(tmp);(r/'scripts').mkdir();shutil.copy(str(Path(__file__).resolve().parents[1] / 'scripts/build_music.py'),r/'scripts/build_music.py')
 src=r/'src/lilypond';(src/'sf').mkdir(parents=True);(src/'include').mkdir();(src/'include/common.ly').write_text('macro');(src/'sf/Jazzernaut.sf2').write_text('font');(src/'sample.ly').write_text('music')
 tools=r/'bin';tools.mkdir(); fake='''#!/usr/bin/env python3
import sys,os
from pathlib import Path
n=Path(sys.argv[0]).name;a=sys.argv[1:]
if n=='lilypond':
 p=Path(a[a.index('-o')+1]);p.with_suffix('.pdf').write_text('pdf');p.with_suffix('.midi').write_text('midi')
elif n=='pdf2svg':
 if Path(os.environ['FAIL_FILE']).exists():sys.exit(1)
 Path(a[1]).write_text('svg')
elif n=='fluidsynth':Path(a[a.index('-F')+1]).write_text('wav')
elif n=='lame':Path(a[1]).write_text('mp3')
'''
 for n in ['lilypond','gs','pdf2svg','fluidsynth','lame']:
  p=tools/n;p.write_text(fake);p.chmod(0o755)
 (tools/'pdfCropMargins.py').write_text("import sys,shutil\na=sys.argv[1:];shutil.copyfile(a[-1],a[a.index('-o')+1])\n")
 env=dict(os.environ,PYTHONPATH=str(tools),PATH=str(tools)+os.pathsep+os.environ['PATH'],FAIL_FILE=str(r/'fail'));out=r/'output with spaces';cmd=[sys.executable,str(r/'scripts/build_music.py'),'--output-dir',str(out)]
 def run(ok=True):
  x=subprocess.run(cmd,env=env,capture_output=True,text=True);assert (x.returncode==0)==ok,x.stderr;return x.stdout
 assert 'Compilo' in run();assert 'Aggiornato' in run()
 (out/'sample.midi').unlink();assert 'Compilo' in run()
 (src/'include/common.ly').write_text('changed');assert 'Compilo' in run()
 (src/'sf/Jazzernaut.sf2').write_text('changed font');assert 'Compilo' in run()
 (out/'sample.svg').write_text('damaged');assert 'Compilo' in run()
 before=(out/'sample.pdf').read_bytes();(src/'sample.ly').write_text('new');(r/'fail').touch();run(False);assert (out/'sample.pdf').read_bytes()==before
 (r/'fail').unlink();assert 'Compilo' in run();assert 'Aggiornato' in run()
 print('PASS: initial build, skip, missing MIDI, include, soundfont, damaged output, failed conversion preserves outputs, recovery, spaces')
