# Audit dei file musicali non referenziati

Data: 2026-11-08. Analisi statica dei sorgenti locali; nessun file eliminato.

## Metodo e limiti

Esaminati RST, configurazioni Python e CSS sotto `src/docs`; risolti riferimenti locali espliciti e wildcard di immagini. Un riferimento immagine `nome.*` copre PDF/SVG/immagini, non rende automaticamente utilizzato un MP3. Per i `.ly`, utilizzo editoriale inferito da output omonimi referenziati nelle pagine, anche SVG, e propagato transitivamente tramite `\include`. Gli script di build compilano tutti i sorgenti: essere compilato non equivale a essere richiamato nei contenuti.

La relazione sorgente→output omonimo è una convenzione dei progetti, non una prova per output personalizzati o multipli. Non analizzati utilizzi esterni, storia Git o riferimenti creati dinamicamente. Non referenziato non significa eliminabile: alcuni esempi possono essere riservati a sviluppi futuri. I PDF sono conservativamente considerati utilizzati anche se la wildcard in HTML seleziona uno SVG.

Sono esclusi `out`, `.venv`, `.git` e `Docs`: il perimetro dei file candidati è `src`.

## Riepilogo

| Tipo | Totale | Non referenziati nel percorso editoriale |
|---|---:|---:|
| `.mp3` | 119 | 17 |
| `.pdf` | 191 | 87 |
| `.ly` | 120 | 16 |

## File .mp3 non referenziati

- `src/docs/_static/music/accordi-c-maggiore-11-1.mp3`
- `src/docs/_static/music/accordi-c-maggiore-3-1.mp3`
- `src/docs/_static/music/accordi-c-maggiore-7.mp3`
- `src/docs/_static/music/accordi-c-maggiore-9-1.mp3`
- `src/docs/_static/music/accordi-c-maggiore-r-1.mp3`
- `src/docs/_static/music/accordi-c-maggiore.mp3`
- `src/docs/_static/music/accordi-f-maggiore-5.mp3`
- `src/docs/_static/music/arpeggio-c69-1.mp3`
- `src/docs/_static/music/arpeggio-c69-2.mp3`
- `src/docs/_static/music/scala-cromatica-verticale2.mp3`
- `src/docs/_static/music/scala-maggiore-5V2-tab.mp3`
- `src/docs/_static/music/scala-maggiore-5V4-tab.mp3`
- `src/docs/_static/music/scala-maggiore-6V2-tab.mp3`
- `src/docs/_static/music/scala-maggiore-6V4-tab.mp3`
- `src/docs/_static/music/scala-maggiore-orizzontale1.mp3`
- `src/docs/_static/music/scale.mp3`
- `src/docs/_static/music/triade-armonica-minore-c-2.mp3`

## File .pdf non referenziati

- `src/docs/_static/music/16-bar-blues-my-babe.pdf`
- `src/docs/_static/music/8-bar-blues-how-long.pdf`
- `src/docs/_static/music/8-bar-blues-key-to-the-highway.pdf`
- `src/docs/_static/music/accordi-c-maggiore-11-1.pdf`
- `src/docs/_static/music/accordi-c-maggiore-3-1.pdf`
- `src/docs/_static/music/accordi-c-maggiore-7.pdf`
- `src/docs/_static/music/accordi-c-maggiore-9-1.pdf`
- `src/docs/_static/music/accordi-c-maggiore-r-1.pdf`
- `src/docs/_static/music/accordi-c-maggiore.pdf`
- `src/docs/_static/music/accordi-f-maggiore-5.pdf`
- `src/docs/_static/music/arpeggio-c69-1.pdf`
- `src/docs/_static/music/arpeggio-c69-2.pdf`
- `src/docs/_static/music/blues-simple.pdf`
- `src/docs/_static/music/blues_grid.pdf`
- `src/docs/_static/music/scala-diminuita-1.pdf`
- `src/docs/_static/music/scala-diminuita-2.pdf`
- `src/docs/_static/music/scala-dorica-5H.pdf`
- `src/docs/_static/music/scala-dorica-5H2.pdf`
- `src/docs/_static/music/scala-dorica-5V2.pdf`
- `src/docs/_static/music/scala-dorica-6H.pdf`
- `src/docs/_static/music/scala-dorica-6H2.pdf`
- `src/docs/_static/music/scala-dorica-6V2.pdf`
- `src/docs/_static/music/scala-dorica-6V4-bis.pdf`
- `src/docs/_static/music/scala-dorica-6V4.pdf`
- `src/docs/_static/music/scala-maggiore-5H2.pdf`
- `src/docs/_static/music/scala-maggiore-5V2-tab.pdf`
- `src/docs/_static/music/scala-maggiore-5V2.pdf`
- `src/docs/_static/music/scala-maggiore-5V4-tab.pdf`
- `src/docs/_static/music/scala-maggiore-5V4.pdf`
- `src/docs/_static/music/scala-maggiore-6H2.pdf`
- `src/docs/_static/music/scala-maggiore-6V2-tab.pdf`
- `src/docs/_static/music/scala-maggiore-6V2.pdf`
- `src/docs/_static/music/scala-maggiore-6V4-tab.pdf`
- `src/docs/_static/music/scala-maggiore-6V4.pdf`
- `src/docs/_static/music/scala-maggiore-orizzontale1.pdf`
- `src/docs/_static/music/scala-melodica-5H.pdf`
- `src/docs/_static/music/scala-melodica-5H2.pdf`
- `src/docs/_static/music/scala-melodica-5V2.pdf`
- `src/docs/_static/music/scala-melodica-6H.pdf`
- `src/docs/_static/music/scala-melodica-6H2.pdf`
- `src/docs/_static/music/scala-melodica-6V2.pdf`
- `src/docs/_static/music/scala-melodica-6V4-bis.pdf`
- `src/docs/_static/music/scala-melodica-6V4.pdf`
- `src/docs/_static/music/scala-minore-armonica-5H.pdf`
- `src/docs/_static/music/scala-minore-armonica-5V2.pdf`
- `src/docs/_static/music/scala-minore-armonica-5V4.pdf`
- `src/docs/_static/music/scala-minore-armonica-6H.pdf`
- `src/docs/_static/music/scala-minore-armonica-6H2.pdf`
- `src/docs/_static/music/scala-minore-armonica-6V4.pdf`
- `src/docs/_static/music/scala-minore-naturale-5H.pdf`
- `src/docs/_static/music/scala-minore-naturale-5V2.pdf`
- `src/docs/_static/music/scala-minore-naturale-5V4.pdf`
- `src/docs/_static/music/scala-minore-naturale-6H.pdf`
- `src/docs/_static/music/scala-minore-naturale-6H2.pdf`
- `src/docs/_static/music/scala-minore-naturale-6V4.pdf`
- `src/docs/_static/music/scala-misolidia-5H2-bis.pdf`
- `src/docs/_static/music/scala-misolidia-5H2.pdf`
- `src/docs/_static/music/scala-misolidia-5V2.pdf`
- `src/docs/_static/music/scala-misolidia-5V4.pdf`
- `src/docs/_static/music/scala-misolidia-6H2.pdf`
- `src/docs/_static/music/scala-misolidia-6V2.pdf`
- `src/docs/_static/music/scala-misolidia-b9b13-5H.pdf`
- `src/docs/_static/music/scala-misolidia-b9b13-5V4.pdf`
- `src/docs/_static/music/scala-misolidia-b9b13-6H2.pdf`
- `src/docs/_static/music/scala-misolidia-b9b13-6V4.pdf`
- `src/docs/_static/music/scala-superlocria-5H.pdf`
- `src/docs/_static/music/scala-superlocria-5H2.pdf`
- `src/docs/_static/music/scala-superlocria-5V2.pdf`
- `src/docs/_static/music/scala-superlocria-6H.pdf`
- `src/docs/_static/music/scala-superlocria-6H2.pdf`
- `src/docs/_static/music/scala-superlocria-6V2.pdf`
- `src/docs/_static/music/scala-superlocria-6V4.pdf`
- `src/docs/_static/music/scala-toni-diminuita-1.pdf`
- `src/docs/_static/music/scala-toni-diminuita-2.pdf`
- `src/docs/_static/music/scala-toni-interi-1.pdf`
- `src/docs/_static/music/scala-toni-interi-2.pdf`
- `src/docs/_static/music/scala-toni-interi-3.pdf`
- `src/docs/_static/music/scala-toni-interi-4.pdf`
- `src/docs/_static/music/scale-riepilogo-5H2.pdf`
- `src/docs/_static/music/scale-riepilogo-5V2.pdf`
- `src/docs/_static/music/scale-riepilogo-5V4.pdf`
- `src/docs/_static/music/scale-riepilogo-6H2.pdf`
- `src/docs/_static/music/scale-riepilogo-6V2.pdf`
- `src/docs/_static/music/scale-riepilogo-6V4.pdf`
- `src/docs/_static/music/scale.pdf`
- `src/docs/_static/music/scale2.pdf`
- `src/lilypond/8-bar-blues-key-to-the-highway.pdf`

## File .ly non referenziati

- `src/lilypond/16-bar-blues-my-babe.ly`
- `src/lilypond/8-bar-blues-how-long.ly`
- `src/lilypond/8-bar-blues-key-to-the-highway.ly`
- `src/lilypond/arpeggio-c69-1.ly`
- `src/lilypond/arpeggio-c69-2.ly`
- `src/lilypond/blues-simple.ly`
- `src/lilypond/blues_grid.ly`
- `src/lilypond/include/my-chart.ly` — incluso soltanto da sorgenti non utilizzati nelle pagine
- `src/lilypond/include/my-scales.ly` — incluso soltanto da sorgenti non utilizzati nelle pagine
- `src/lilypond/scala-diminuita-1.ly`
- `src/lilypond/scala-diminuita-2.ly`
- `src/lilypond/scala-toni-interi-1.ly`
- `src/lilypond/scala-toni-interi-2.ly`
- `src/lilypond/scala-toni-interi-3.ly`
- `src/lilypond/scala-toni-interi-4.ly`
- `src/lilypond/scale.ly`

## Evidenze dei riferimenti

Il file JSON allegato contiene, per ogni candidato, i riferimenti rilevati e la classificazione. Per i `.ly` è distinto il raggiungimento dai contenuti dalla sola presenza di un include.
