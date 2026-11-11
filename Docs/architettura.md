# Architettura e punti di attenzione

## Fonti e flusso

- `README.md`: identità e indirizzo pubblico dichiarato.
- `src/docs/index.rst`: ordine del percorso e toctree con profondità 3.
- `src/docs/*.rst`: contenuti didattici reStructuredText.
- `src/docs/conf.py`: Sphinx, lingua italiana, release 0.1, tema Shibuya, CSS personalizzato, navigazione tra i progetti e LuaLaTeX.
- `src/docs/_static/custom.css`: presentazione; `_static/music`: risorse musicali utilizzate dalle pagine.
- `src/lilypond/*.ly`: sorgenti delle partiture; `include/`: macro condivise nel singolo repository; `sf/Jazzernaut.sf2`: soundfont.
- `build-lilypond.sh`: LilyPond → PDF → ritaglio con pdfcrop → SVG con pdf2svg; MIDI → WAV con FluidSynth → MP3 con LAME, eliminando il WAV intermedio.
- `build.sh`: `sphinx-build -b html src/docs out`; `out` è output, non fonte editoriale.
- `requirements.txt`: sphinx e shibuya senza versioni bloccate.
- `.readthedocs.yaml`: Ubuntu 24.04, Python 3.12, configurazione Sphinx e formati PDF/ePub.

Le pagine campionate usano immagini `_static/music/nome.*` e audio HTML con file MP3 omonimi. Il nome base collega RST, partitura e risorse: rinominarlo richiede analisi di tutti i riferimenti. Gli include LilyPond sono dipendenze trasversali interne.

## Vincoli osservati e rischi da analizzare

1. La build musicale controlla timestamp dei soli `.ly` al primo livello rispetto a PDF/SVG. Una modifica agli include non invalida automaticamente gli output; gli MP3 dipendono dal timestamp MIDI, non dal soundfont. Definire una strategia di invalidazione prima di intervenire sulla pipeline.
2. Lo script verifica esplicitamente solo LilyPond; servono anche pdfcrop, pdf2svg, fluidsynth e lame. Gli argomenti del ramo audio non sono quotati. Valutare riproducibilità e gestione degli errori.
3. La configurazione Read the Docs non richiama lo script musicale: verificare disponibilità e aggiornamento delle risorse prima della pubblicazione.
4. `source_suffix` dichiara Markdown, ma nelle estensioni non compare un parser Markdown. Non assumere che aggiungere `.md` sotto `src/docs` sia supportato.
5. Audio tramite `raw:: html`: verificare separatamente resa e alternative nei formati PDF/ePub. La presenza di `imgconverter` non dimostra che tutti i convertitori esterni siano installati.
6. I due repository hanno copie degli script e delle macro; le macro `my-scales.ly` differiscono. Non dedurre equivalenza dal nome, né centralizzare senza confronto e ADR. **Aggiornamento 2026-11-11:** l'ADR 0004 decide la centralizzazione in una libreria comune (sottomodulo `tools/appunti-musica`). Il confronto delle differenze e il piano di migrazione sono nell'analisi 002 di appunti-repertorio. Fino alla migrazione restano valide le copie attuali.
7. Dipendenze Python non fissate: una build futura potrebbe usare versioni diverse. La riproducibilità è un tema proposto, non un difetto dimostrato da esecuzione.

## Verifiche per future proposte

Per una sola analisi controllare fonti, riferimenti e coerenza delle conclusioni. Per modifiche implementative autorizzate, eseguire dalla radice la build pertinente, conservare avvisi ed errori e ispezionare pagine, immagini e audio interessati. Una build HTML non valida PDF/ePub né la correttezza musicale. Non rigenerare tutto per aggiornare questa KB.

## Limiti della rilevazione

Esaminati configurazioni, indici, script, inventario dei sorgenti e campioni del capitolo scale e delle macro. Non eseguite build, verifica dei siti remoti o revisione musicologica completa. Completezza dei media, riferimenti mancanti e compatibilità dei tool restano da verificare con analisi dedicate.
