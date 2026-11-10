# Read the Docs: immagini dei nuovi spartiti nella build PDF

Data: 10 novembre 2026. Segnalazione dell'utente: build 35798005, commit ea4daa1.

## Diagnosi

L'HTML termina con successo (otto avvisi di titoli in Arpeggi); il comando `sphinx -b latex` fallisce nel convertire `modern-groove-44.svg` tramite ImageMagick. L'errore è `unbalanced graphic context push-pop`. I nuovi capitoli avevano fissato `.svg` nelle direttive immagine, obbligando LaTeX a convertire il formato; i PDF equivalenti erano già presenti. Le precedenti verifiche HTML non coprivano questa fase.

## Correzione

Le direttive immagine degli studi modern/fusion e dei percorsi d'autore usano `nome.*`, coerentemente con gli spartiti precedenti. Sphinx seleziona SVG per HTML e il PDF esistente per LaTeX. Aggiornato anche il generatore delle pagine dei percorsi d'autore, affinché la rigenerazione conservi la correzione. Applicata la stessa soluzione ai quattro esempi ritmici nel volume Teoria. Non sono modificati note, immagini, audio o dipendenze del sito.

Documentazione ufficiale: https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#images

Corretti inoltre i quattro titoli con sottolineatura troppo corta in `5-arpeggi.rst`, rilevati dalla build completa da zero e presenti nel log dell'utente.

## Verifiche

- Entrambi i repository: HTML da zero con `-E -a -W --keep-going`, riuscito senza avvisi.
- Entrambi i repository: generazione LaTeX da zero con `-E -W --keep-going`, riuscita senza avvisi. Il TeX risultante include `modern-groove-44.pdf` e gli altri PDF direttamente.
- Entrambi i repository: generazione ePub riuscita. Restano avvisi del builder sui tipi multimediali presenti nelle risorse statiche e sui metadati: non sono l'errore segnalato e non sono stati nascosti.
- `tests/test_document_formats.py`: controlla le coppie SVG/PDF referenziate nei due libri e costruisce un progetto Sphinx minimo, anche con pagina annidata. Verifica SVG per HTML/ePub e PDF per LaTeX mentre il convertitore esterno è deliberatamente indisponibile.

Non è installato un motore TeX locale: è verificata la preparazione LaTeX che falliva in Read the Docs, non la successiva compilazione dell'intero libro con LuaLaTeX. Il nuovo build remoto deve confermare anche quest'ultima fase.
