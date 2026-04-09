#!/bin/sh

set -eu

SRC_DIR="notation"
OUT_DIR="docs/_static/notation"

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
      --output="$target_dir/$base" \
      "$src"

    # SVG
    lilypond \
      --svg \
      --output="$target_dir/$base" \
      "$src"
  else
    echo "Salto: $src (già aggiornato)"
  fi
done