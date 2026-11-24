# KB ARCHITECT — Appunti di Pratica

Aggiornamento: 13 novembre 2026. Questa KB descrive i sorgenti presenti; non certifica lo stato dei siti pubblicati.

Versione: **1.2** (`VERSIONE` in `src/docs/conf.py`) dal 19 novembre 2026, con tutte le famiglie di voicing nel capitolo Accordi (analisi 024); 1.1 dal 12 novembre 2026, con il capitolo «Strumenti per la pratica» (ADR 0005); 1.0 dall'11 novembre 2026, per decisione dell'utente: il volume è considerato sostanzialmente completo. Nessun tag git di versione. Dal 14 novembre 2026, su richiesta dell'utente, la versione completa è **MAJOR.MINOR.PATCH**: MAJOR.MINOR si scrive a mano nella riga `VERSIONE = "X.Y"` di `src/docs/conf.py`; la patch conta i commit successivi all'ultimo cambio di quella riga, quindi avanza a ogni push su main e riparte da 0 quando si cambia MAJOR.MINOR. La data di aggiornamento è quella dell'ultimo commit. Entrambe compaiono in fondo alla homepage e nel frontespizio del PDF ed ePub; il calcolo è in `src/docs/versione_git.py`, copia identica nei tre volumi, e `.readthedocs.yaml` completa la storia git prima della build.

## Modalità di lavoro

Leggere questa pagina e [architettura](architettura.md) prima di proporre interventi. In modalità ARCHITECT produrre analisi, mappe di dipendenze, alternative e ADR dentro `Docs`. La scrittura assistita e la possibile ristrutturazione dei contenuti sono state richieste esplicitamente dall’utente. Nella fase ARCHITECT elaborare prima struttura e obiettivi; passare alla redazione nel perimetro concordato. Una proposta non equivale a una decisione approvata.

Per ogni richiesta: chiarire problema e risultato atteso; rileggere i sorgenti coinvolti; distinguere fatti, inferenze e punti aperti; valutare impatto su entrambi i progetti; documentare opzioni e criteri di verifica. Usare il [modello di analisi](analisi/TEMPLATE.md) e il [modello ADR](adr/TEMPLATE.md).

## Identità e perimetro

Percorso operativo sulla chitarra: basi, conoscenza della tastiera, scale, arpeggi, accordi, progressioni e licks. Il capitolo scale privilegia otto sonorità e la costruzione autonoma delle diteggiature, con estensione a ottave e tonalità diverse; pentatoniche, scala blues e scale bebop hanno mappe proprie come materiali derivati.

Il progetto fratello è `../appunti-teoria`. Teoria spiega strutture e relazioni; Pratica le applica alla tastiera. Questa distinzione è una lettura del materiale, non una decisione storica documentata. Prima di spostare contenuti verificare prerequisiti, duplicazioni utili e collegamenti tra i due percorsi.

## Mappa dei capitoli

- `src/docs/1-introduzione.rst`: Introduzione
- `src/docs/da-dove-comincio.rst`: Da dove comincio (dal 14 novembre 2026, analisi 023)
- `src/docs/2-basi.rst`: Le basi che nessuno vede
- `src/docs/3-conoscere-la-tastiera.rst`: Conoscere la tastiera
- `src/docs/4-scale.rst`: Scale
- `src/docs/5-arpeggi.rst`: Arpeggi
- `src/docs/strutture-melodiche.rst`: Strutture melodiche e costruzione della frase (dal 14 novembre 2026, analisi 022)
- `src/docs/pentatoniche.rst`: Pentatoniche (dal 14 novembre 2026, analisi 022, fase B)
- `src/docs/ritmo-melodico.rst`: Ritmo melodico (dal 22 novembre 2026, analisi 025; esempi R1–R10 da `scripts/generate_melodic_rhythms.py`)
- `src/docs/6-accordi.rst`: Accordi
- `src/docs/7-progressioni.rst`: Progressioni
- `src/docs/8-licks.rst`: Licks
- `src/docs/9-modern-jazz-fusion.rst`: Modern jazz e fusion
- `src/docs/10-percorsi-autore.rst` e `src/docs/autori/`: Percorsi d’autore

## Gestione delle decisioni

Le scelte storiche osservate nei sorgenti non sono considerate approvate retroattivamente. Per nuove decisioni usare `adr/NNNN-titolo.md`, numero progressivo libero, stato iniziale Proposto. Stati: Proposto, Accettato, Respinto, Superato. Registrare autore della decisione e data quando disponibili; non inventarli. Un ADR superato resta consultabile e rimanda al successore.

## Manutenzione

I sorgenti prevalgono sulla KB. Dopo cambiamenti rilevanti aggiornare evidenze e data; verificare sempre percorsi e riferimenti prima di riutilizzare una conclusione. `Docs` è distinta da `src/docs` e non entra nella build Sphinx corrente.

**Note di rilascio** (dal 19 novembre 2026, su richiesta dell'utente): `src/docs/note-di-rilascio.rst`, ultima voce dell'indice e collegata dal piè di pagina della homepage. A ogni modifica dei contenuti pubblicata (ogni push su main fa avanzare la PATCH) aggiungere una voce, scritta per il lettore, nella sezione «Prossimo aggiornamento»; alla pubblicazione la sezione diventa una sottosezione datata («19 novembre 2026») sotto la versione MAJOR.MINOR corrente. Quando cambia `VERSIONE` in `src/docs/conf.py` aprire una nuova sezione «X.Y (dal …)» in cima. `tests/test_note_di_rilascio.py` (copia identica nei tre volumi) controlla pagina, indice, sezione della versione attuale e ordine delle date.

## Analisi disponibili

- [Pipeline musicale: dipendenze, aggiornamento e alternative](analisi/001-pipeline-musicale.md) — analisi congiunta dei due repository; raccomandazioni da decidere.

- [Rigenerazione controllata: prima misura](analisi/002-rigenerazione-controllata.md) — risultati delle fasi eseguibili e limiti.

## ADR disponibili

- [ADR 0001 — LilyPond diretto e generazione Python](adr/0001-lilypond-diretto-e-generazione-python.md) — Accettato, 2026-11-08.

- [ADR 0004 — Libreria musicale comune ai tre progetti](adr/0004-libreria-musicale-comune.md) — Accettato, 2026-11-11. Copia comune con appunti-repertorio e il progetto fratello; migrazione non avviata. I numeri 0002–0003 sono usati solo in appunti-repertorio.

- [ADR 0005 — Strumenti interattivi nel volume](adr/0005-strumenti-interattivi-nel-volume.md) — Accettato, 2026-11-12. Capitolo «Strumenti per la pratica», strumenti su GitHub Pages dal repository `appunti-strumenti` (ex Guitar-Scale-Practice, in locale `../appunti-strumenti`), titolo dell'app «Strumenti per la pratica». Attuato per lo strumento Scale il 2026-11-12 (capitolo 11, rimando nel capitolo 4, test `tests/test_strumenti_links.py`) per lo strumento Arpeggi il 2026-11-14 (sezione nel capitolo 11, rimando nel capitolo 5) e per lo strumento Accordi il 2026-11-14 (sezione nel capitolo 11, rimando nel capitolo 6); Progressioni da aggiungere. Il 2026-11-22 lo strumento Ritmi (ADR 0016 di appunti-strumenti) con la sezione «Ritmi» del capitolo 11 e quattordici esercizi pronti (analisi 025). Il 2026-11-15 lo strumento Scale passa a 45 scale con pentatoniche, blues e bebop (ADR 0014 di appunti-strumenti): quattro esercizi pronti nuovi nel capitolo 11.
- [ADR 0006 — Piano elettrico al posto della chitarra negli esempi audio](adr/0006-piano-elettrico-negli-esempi-audio.md) — Accettato, 2026-11-24. Copia comune ai tre volumi: soundfont predefinito `AppuntiEPiano.sf2` (piano elettrico originale in FM, variante morbida) generato dalla libreria appunti-musica; tutti gli MP3 ricompilati.

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

- [Contenuti mancanti segnalati dalla revisione](analisi/020-contenuti-mancanti-revisione.md) — pentatoniche, scala blues e scale bebop nel capitolo Scale, arpeggio m7♭5, gruppi 13 e Δ7 della famiglia maggiore sulla prima corda; poi commenti di tutta la famiglia maggiore, mappe dal Do superiore e due studi sulle scale derivate; test `tests/test_materiali_aggiunti.py`, 13 novembre 2026.

- Introduzione riscritta da zero nelle sezioni «Iniziamo bene» e «Studia in modo consapevole» (voce da manuale tradotto, fonte non identificata); dettagli in `../appunti-teoria/Docs/analisi/011-riscrittura-passaggi-tradotti.md`, 13 novembre 2026.

- [Chiusura dei punti della revisione editoriale](analisi/021-chiusura-revisione-editoriale.md) — commenti differenziati nel vocabolario, bebop minore, studio in Fa e in Sol, brano guida, mappa del capitolo Le basi, 13 novembre 2026.

- [Capitolo di strumenti interattivi](analisi/019-capitolo-strumenti-interattivi.md) — lo strumento Scale (ex Guitar Scale Practice) e strumenti analoghi per Arpeggi, Accordi e Progressioni nel volume; 12 novembre 2026; decisa con l'utente, attuata per Scale, Arpeggi e Accordi, manca Progressioni. ADR [0005](adr/0005-strumenti-interattivi-nel-volume.md) Accettato.

- [Strutture melodiche e revisione integrata](analisi/022-strutture-melodiche-revisione-integrata.md) — proposta del 14 novembre 2026: quattordici blocchi prima/dopo per Teoria, schema della nuova pagina di Pratica ed esempio originale; fase A applicata a Teoria; pagina `strutture-melodiche.rst` scritta il 14 novembre 2026 senza la sezione Famiglie, con esempi S1–S6, generatore `generate_melodic_structures.py`, test e rimandi in entrata; il 14 novembre 2026 fase B: classificazione da Bergonzi, voll. 1–2, sezione Famiglie (S7–S12) e nuova pagina Pentatoniche (P1–P3).

- [Pagina «Da dove comincio» (INT-10)](analisi/023-pagina-da-dove-comincio.md) — proposta del 14 novembre 2026: tre percorsi (frase, accompagnamento, melodia con accordi) con verifica finale, testo completo della pagina e rimandi da Pratica 1 e Teoria 1; attuata il 14 novembre 2026 (`src/docs/da-dove-comincio.rst`).

- [Famiglie di voicing nel capitolo Accordi e nello strumento](analisi/024-famiglie-di-voicing.md) — proposta del 19 novembre 2026: mappa delle famiglie, sei sezioni nuove nel capitolo 6 (triadi, drop 2/3/2 e 4, senza fondamentale, strutture superiori, quarte, cluster), nomi unici per volume, glossario di Teoria e strumento, attuazione in tre fasi. Decisa con l'utente il 19 novembre 2026: definizioni dei drop spostate fuori dal chord melody, strutture superiori naturali e alterate, cluster senza corde a vuoto, nomi italiani con l'inglese citato una volta. Fase 1 attuata il 19 novembre 2026: mappa delle famiglie e sezione «Quattro voci: drop 2, drop 3, drop 2 e 4» con quattro esempi `vf-*`, generatore `generate_voicing_families.py` e test di coerenza con lo strumento. Fase 2 lo stesso giorno: sezioni «Triadi strette e late» e «Voicing senza fondamentale», cinque esempi, glossario di Teoria. Fase 3 lo stesso giorno: «Strutture superiori», «Voicing per quarte», «Cluster», cinque esempi; il capitolo 6 copre tutte le famiglie. Strumento: ADR 0015 di appunti-strumenti, Accettato il 19 novembre 2026.

- [Ritmo melodico: pagina del volume e strumento Ritmi](analisi/025-ritmo-melodico.md) — 22 novembre 2026, su richiesta dell'utente: pagina `ritmo-melodico.rst` ispirata a Bergonzi, *Inside Improvisation*, vol. 4 (procedimenti per capitolo, figure ed esempi originali), dieci esempi R1–R10 con charleston sul 2 e sul 4 nell'audio, generatore e test; strumento Ritmi (ADR 0016 di appunti-strumenti) con quattordici esercizi pronti nel capitolo 11; rimandi da Le basi, Strutture melodiche, Da dove comincio e Teoria 12. Attuata sui rami `ritmo-melodico` e `strumento-ritmi`, da approvare; versione da decidere.
