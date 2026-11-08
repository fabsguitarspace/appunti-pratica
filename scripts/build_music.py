#!/usr/bin/env python3
"""Build musical assets in staging; commit fingerprints only after success."""
import argparse
import fcntl
import hashlib
import importlib.metadata
import sys
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ('lilypond', 'gs', 'pdf2svg', 'fluidsynth', 'lame')
RECIPE = 2


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def signature(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True).encode()).hexdigest()


def run(args, log):
    subprocess.run([str(x) for x in args], cwd=ROOT, stdout=log,
                   stderr=subprocess.STDOUT, check=True)


def save_manifest(path, data):
    pending = path.with_suffix('.pending')
    pending.write_text(json.dumps(data, indent=2, sort_keys=True) + '\n')
    os.replace(pending, path)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path, default=ROOT / 'src/docs/_static/music')
    parser.add_argument('--source', action='append', help='Source basename, repeatable (default: all)')
    parser.add_argument('--force', action='store_true')
    args = parser.parse_args()
    sources_dir = ROOT / 'src/lilypond'
    sources = sorted(sources_dir.glob('*.ly'))
    if args.source:
        requested = set(args.source)
        unknown = requested - {p.stem for p in sources}
        if unknown:
            parser.error('Unknown sources: ' + ', '.join(sorted(unknown)))
        sources = [p for p in sources if p.stem in requested]
    if not sources:
        parser.error('No LilyPond sources found')
    tools = {name: shutil.which(name) for name in TOOLS}
    missing = [name for name, path in tools.items() if path is None]
    if missing:
        parser.error('Missing required tools: ' + ', '.join(missing))
    try:
        crop_version = importlib.metadata.version('pdfCropMargins')
        mupdf_version = importlib.metadata.version('PyMuPDF')
    except importlib.metadata.PackageNotFoundError:
        parser.error('Missing cropping dependencies: install requirements-music.txt with this Python')
    soundfont = sources_dir / 'sf/Jazzernaut.sf2'
    if not soundfont.is_file():
        parser.error('Missing soundfont: ' + str(soundfont))
    # Hash executables rather than relying on inconsistent --version options.
    tool_hashes = {name: digest(Path(path)) for name, path in tools.items()}
    includes = {str(p.relative_to(sources_dir)): digest(p)
                for p in sorted(sources_dir.rglob('*'))
                if p.is_file() and p.suffix in ('.ly', '.ily') and p.parent != sources_dir}
    soundfont_hash = digest(soundfont)
    out = args.output_dir.resolve()
    out.mkdir(parents=True, exist_ok=True)
    state = out / '.music-build'
    state.mkdir(exist_ok=True)
    with (state / 'lock').open('w') as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            parser.error('Another build is using this output directory')
        manifest_path = state / 'manifest.json'
        manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else {}
        for src in sources:
            key = signature({'recipe': RECIPE, 'source': digest(src), 'includes': includes,
                             'tools': tool_hashes, 'crop': [crop_version, mupdf_version],
                             'builder': digest(Path(__file__)), 'soundfont': soundfont_hash})
            previous = manifest.get(src.name, {})
            products = previous.get('outputs', {})
            valid = (previous.get('signature') == key and products and
                     all((out / name).is_file() and digest(out / name) == value
                         for name, value in products.items()))
            if valid and not args.force:
                print('Aggiornato:', src.name, flush=True)
                continue
            print('Compilo:', src.name, flush=True)
            log_path = state / (src.stem + '.log')
            # Staging shares the destination filesystem, allowing atomic file replacement.
            with tempfile.TemporaryDirectory(prefix='stage-', dir=state) as folder:
                stage = Path(folder)
                base = stage / src.stem
                try:
                    with log_path.open('w') as log:
                        run([tools['lilypond'], '-o', base, src], log)
                        pdf = base.with_suffix('.pdf')
                        if not pdf.is_file() or not pdf.stat().st_size:
                            raise RuntimeError('Expected PDF missing: ' + str(pdf))
                        # Preserve the existing single-PDF/SVG contract; reject silent truncation.
                        pdfs = list(stage.glob('*.pdf'))
                        midis = list(stage.glob('*.midi'))
                        if len(pdfs) != 1 or len(midis) > 1 or any(p.stem != src.stem for p in midis):
                            raise RuntimeError('Multiple/nonnormal output names need an explicit output contract')
                        cropped = stage / 'cropped.pdf'
                        run([sys.executable, '-m', 'pdfCropMargins', '-p', '0', '-a', '-10',
                             '-c', 'gb', '-o', cropped, pdf], log)
                        os.replace(cropped, pdf)
                        run([tools['pdf2svg'], pdf, base.with_suffix('.svg')], log)
                        names = [src.stem + '.pdf', src.stem + '.svg']
                        if midis:
                            wav = base.with_suffix('.wav')
                            run([tools['fluidsynth'], '-F', wav, '-ni', soundfont, midis[0]], log)
                            run([tools['lame'], wav, base.with_suffix('.mp3')], log)
                            names += [src.stem + '.midi', src.stem + '.mp3']
                    for name in names:
                        if not (stage / name).is_file() or not (stage / name).stat().st_size:
                            raise RuntimeError('Empty or missing output: ' + name)
                    # Invalidate before promotion so interruption never leaves a success marker.
                    manifest.pop(src.name, None)
                    save_manifest(manifest_path, manifest)
                    for name in names:
                        os.replace(stage / name, out / name)
                    manifest[src.name] = {'signature': key,
                                          'outputs': {name: digest(out / name) for name in names}}
                    save_manifest(manifest_path, manifest)
                    leftovers = set(products) - set(names)
                    if leftovers:
                        print('Risorse precedenti conservate, da verificare:', ', '.join(sorted(leftovers)))
                except (subprocess.CalledProcessError, RuntimeError) as error:
                    raise RuntimeError(f'{src.name}: {error}. Log: {log_path}') from error
        removed = set(manifest) - {p.name for p in sources_dir.glob('*.ly')}
        if removed:
            print('Sorgenti rimossi; output conservati da verificare:', ', '.join(sorted(removed)))


if __name__ == '__main__':
    main()
