# KB ARCHITECT — Appunti di Pratica

Aggiornamento: 12 novembre 2026. Questa KB descrive i sorgenti presenti; non certifica lo stato dei siti pubblicati.

Versione: **1.1** (`release` in `src/docs/conf.py`) dal 12 novembre 2026, con il capitolo «Strumenti per la pratica» (ADR 0005); 1.0 dall'11 novembre 2026, per decisione dell'utente: il volume è considerato sostanzialmente completo. Nessun tag git di versione.

## Modalità di lavoro

Leggere questa pagina e [architettura](architettura.md) prima di proporre interventi. In modalità ARCHITECT produrre analisi, mappe di dipendenze, alternative e ADR dentro `Docs`. La scrittura assistita e la possibile ristrutturazione dei contenuti sono state richieste esplicitamente dall’utente. Nella fase ARCHITECT elaborare prima struttura e obiettivi; passare alla redazione nel perimetro concordato. Una proposta non equivale a una decisione approvata.

Per ogni richiesta: chiarire problema e risultato atteso; rileggere i sorgenti coinvolti; distinguere fatti, inferenze e punti aperti; valutare impatto su entrambi i progetti; documentare opzioni e criteri di verifica. Usare il [modello di analisi](analisi/TEMPLATE.md) e il [modello ADR](adr/TEMPLATE.md).

## Identità e perimetro

Percorso operativo sulla chitarra: basi, conoscenza della tastiera, scale, arpeggi, accordi, progressioni e licks. Il capitolo scale privilegia otto sonorità e la costruzione autonoma delle diteggiature, con estensione a ottave e tonalità diverse.

Il progetto fratello è `../appunti-teoria`. Teoria spiega strutture e relazioni; Pratica le applica alla tastiera. Questa distinzione è una lettura del materiale, non una decisione storica documentata. Prima di spostare contenuti verificare prerequisiti, duplicazioni utili e collegamenti tra i due percorsi.

## Mappa dei capitoli

- `src/docs/1-introduzione.rst`: Introduzione
- `src/docs/2-basi.rst`: Le basi che nessuno vede
- `src/docs/3-conoscere-la-tastiera.rst`: Conoscere la tastiera
- `src/docs/4-scale.rst`: Scale
- `src/docs/5-arpeggi.rst`: Arpeggi
- `src/docs/6-accordi.rst`: Accordi
- `src/docs/7-progressioni.rst`: Progressioni
- `src/docs/8-licks.rst`: Licks
- `src/docs/9-modern-jazz-fusion.rst`: Modern jazz e fusion
- `src/docs/10-percorsi-autore.rst` e `src/docs/autori/`: Percorsi d’autore

## Gestione delle decisioni

Le scelte storiche osservate nei sorgenti non sono considerate approvate retroattivamente. Per nuove decisioni usare `adr/NNNN-titolo.md`, numero progressivo libero, stato iniziale Proposto. Stati: Proposto, Accettato, Respinto, Superato. Registrare autore della decisione e data quando disponibili; non inventarli. Un ADR superato resta consultabile e rimanda al successore.

## Manutenzione

I sorgenti prevalgono sulla KB. Dopo cambiamenti rilevanti aggiornare evidenze e data; verificare sempre percorsi e riferimenti prima di riutilizzare una conclusione. `Docs` è distinta da `src/docs` e non entra nella build Sphinx corrente.

## Analisi disponibili

- [Pipeline musicale: dipendenze, aggiornamento e alternative](analisi/001-pipeline-musicale.md) — analisi congiunta dei due repository; raccomandazioni da decidere.

- [Rigenerazione controllata: prima misura](analisi/002-rigenerazione-controllata.md) — risultati delle fasi eseguibili e limiti.

## ADR disponibili

- [ADR 0001 — LilyPond diretto e generazione Python](adr/0001-lilypond-diretto-e-generazione-python.md) — Accettato, 2026-11-08.

- [ADR 0004 — Libreria musicale comune ai tre progetti](adr/0004-libreria-musicale-comune.md) — Accettato, 2026-11-11. Copia comune con appunti-repertorio e il progetto fratello; migrazione non avviata. I numeri 0002–0003 sono usati solo in appunti-repertorio.

- [ADR 0005 — Strumenti interattivi nel volume](adr/0005-strumenti-interattivi-nel-volume.md) — Accettato, 2026-11-12. Capitolo «Strumenti per la pratica», strumenti su GitHub Pages dal repository `appunti-strumenti` (ex Guitar-Scale-Practice, in locale `../appunti-strumenti`), titolo dell'app «Strumenti per la pratica». Attuato per lo strumento Scale il 2026-11-12 (capitolo 11, rimando nel capitolo 4, test `tests/test_strumenti_links.py`); Arpeggi, Accordi e Progressioni da aggiungere man mano.

- [Ristrutturazione editoriale e scrittura assistita](analisi/003-ristrutturazione-editoriale.md) — proposta aperta; i capitoli mancanti sono ipotesi.

- [Ripristino della build Sphinx](analisi/004-ripristino-build-sphinx.md) — modifiche e verifiche eseguite.

- [Correzioni pipeline musicale e ritaglio PDF](analisi/005-correzioni-pipeline-musicale.md) — implementazione, uso e verifiche.

- [Audit dei file musicali non referenziati](analisi/006-file-non-referenziati.md) — elenchi MP3, PDF e LilyPond con evidenze.

- [Scale: primo blocco di esercizi](analisi/007-esercizi-scale-primo-blocco.md) — stesura e verifiche.

- [Scale: esercizi avanzati](analisi/008-esercizi-scale-avanzati.md) — otto studi con pentagramma, tablatura e audio a due velocità, 10 novembre 2026.

- [Arpeggi: sezione Esercizi](analisi/009-esercizi-arpeggi.md) — dieci studi con pentagramma, tablatura e audio a due velocità, 10 novembre 2026.

- [Vocabolario avanzato: minori e dominanti](analisi/010-vocabolario-minori-dominanti.md) — 38 gruppi con nota al canto fissa, 114 voicing, diagrammi, spartiti, TAB e audio, 10 novembre 2026.

- [Stile degli spartiti di Accordi e preferenza sul basso](analisi/011-stile-spartiti-accordi.md) — uniformati 17 spartiti preesistenti; aggiornati i nuovi voicing senza tensioni al basso, 10 novembre 2026.

- [Shell voicings](analisi/012-shell-voicings.md) — sette esempi a tre voci esclusivamente sulle corde 6–4–3 e 5–4–3, con bassi di tonica, terza e quinta, 10 novembre 2026.

- [Capitolo Progressioni](analisi/013-capitolo-progressioni.md) — percorso completo con diciassette esempi, tre basi e studio AABA, 10 novembre 2026.

- [Licks bebop e collegamento con Progressioni](analisi/014-licks-bebop.md) — cinquanta frasi originali in cinque categorie, spartiti/TAB/audio e rimandi reciproci, 10 novembre 2026.

- [Modern jazz e fusion](analisi/015-modern-jazz-fusion.md) — dodici studi, basi con basso/batteria, quarte, sovrapposizioni e ritmo, 10 novembre 2026.

- [Percorsi d’autore](analisi/016-percorsi-autore.md) — dieci artisti, venti ascolti guidati, sessanta studi con spartito/TAB/audio e dieci basi finali, 10 novembre 2026.

- [Read the Docs: formati degli spartiti](analisi/017-readthedocs-formati-spartiti.md) — risolto il passaggio SVG nella preparazione PDF e aggiunta regressione sui formati, 10 novembre 2026.

- [Voicing per il chord melody](analisi/018-voicing-chord-melody.md) — drop 2, drop 3, tre voci, diminuiti di passaggio, sesta diminuita e un arrangiamento di otto battute; 11 esempi, 59 voicing, 11 novembre 2026.

- [Capitolo di strumenti interattivi](analisi/019-capitolo-strumenti-interattivi.md) — lo strumento Scale (ex Guitar Scale Practice) e strumenti analoghi per Arpeggi, Accordi e Progressioni nel volume; 12 novembre 2026; decisa con l'utente, attuazione non avviata. ADR [0005](adr/0005-strumenti-interattivi-nel-volume.md) Accettato.
