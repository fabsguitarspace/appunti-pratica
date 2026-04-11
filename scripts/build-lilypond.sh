#!/bin/sh

set -eu

SRC_DIR="src/lilypond"
OUT_DIR="src/docs/_static/music"

if ! command -v lilypond >/dev/null 2>&1; then
  echo "Errore: lilypond non trovato nel PATH." >&2
  exit 1
fi

if [ ! -d "$SRC_DIR" ]; then
  echo "Errore: cartella sorgente '$SRC_DIR' non trovata." >&2
  exit 1
fi

find "$SRC_DIR" -maxdepth 1 -type f -name '*.ly' | while IFS= read -r src; do
  rel="${src#$SRC_DIR/}"
  rel_dir=$(dirname "$rel")
  base=$(basename "$src" .ly)

  target_dir="$OUT_DIR/$rel_dir"
  pdf_out="$target_dir/$base.pdf"
  svg_out="$target_dir/$base.svg"

  mkdir -p "$target_dir"

  needs_build=0

  if [ ! -f "$pdf_out" ] || [ "$src" -nt "$pdf_out" ]; then
    needs_build=1
  fi

  if [ ! -f "$svg_out" ] || [ "$src" -nt "$svg_out" ]; then
    needs_build=1
  fi

  if [ "$needs_build" -eq 1 ]; then
    echo "Compilo: $src"

    # PDF
    lilypond \
      -o "$target_dir/temp" \
      -dcrop \
      "$src"
    mv "$target_dir/temp.cropped.pdf" "$target_dir/$base.pdf"

    # SVG
    lilypond \
      --svg \
      -o "$target_dir/temp" \
      -dcrop \
      "$src"
    mv "$target_dir/temp.cropped.svg" "$target_dir/$base.svg"
  else
    echo "Salto: $src (già aggiornato)"
  fi
done

find "$OUT_DIR" -maxdepth 1 -type f -name '*.midi' | while IFS= read -r src; do
  base=$(basename "$src" .midi)

  target_dir="$OUT_DIR"
  wav_out="$target_dir/$base.wav"
  mp3_out="$target_dir/$base.mp3"
  needs_build=0

  if [ ! -f "$mp3_out" ] || [ "$src" -nt "$mp3_out" ]; then
    needs_build=1
  fi
  if [ "$needs_build" -eq 1 ]; then
    echo "Compilo: $src"
    fluidsynth -F $wav_out -ni src/lilypond/sf/Jazzernaut.sf2 $src
    lame $wav_out $mp3_out
    rm -f $wav_out
  else
    echo "Salto: $src (già aggiornato)"
  fi
done
