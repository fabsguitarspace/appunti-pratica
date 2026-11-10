# KB ARCHITECT — Appunti di Pratica

Rilevazione locale: 8 novembre 2026. Questa KB descrive i sorgenti presenti; non certifica lo stato dei siti pubblicati.

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

## Gestione delle decisioni

Le scelte storiche osservate nei sorgenti non sono considerate approvate retroattivamente. Per nuove decisioni usare `adr/NNNN-titolo.md`, numero progressivo libero, stato iniziale Proposto. Stati: Proposto, Accettato, Respinto, Superato. Registrare autore della decisione e data quando disponibili; non inventarli. Un ADR superato resta consultabile e rimanda al successore.

## Manutenzione

I sorgenti prevalgono sulla KB. Dopo cambiamenti rilevanti aggiornare evidenze e data; verificare sempre percorsi e riferimenti prima di riutilizzare una conclusione. `Docs` è distinta da `src/docs` e non entra nella build Sphinx corrente.

## Analisi disponibili

- [Pipeline musicale: dipendenze, aggiornamento e alternative](analisi/001-pipeline-musicale.md) — analisi congiunta dei due repository; raccomandazioni da decidere.

- [Rigenerazione controllata: prima misura](analisi/002-rigenerazione-controllata.md) — risultati delle fasi eseguibili e limiti.

## ADR disponibili

- [ADR 0001 — LilyPond diretto e generazione Python](adr/0001-lilypond-diretto-e-generazione-python.md) — Accettato, 2026-11-08.

- [Ristrutturazione editoriale e scrittura assistita](analisi/003-ristrutturazione-editoriale.md) — proposta aperta; i capitoli mancanti sono ipotesi.

- [Ripristino della build Sphinx](analisi/004-ripristino-build-sphinx.md) — modifiche e verifiche eseguite.

- [Correzioni pipeline musicale e ritaglio PDF](analisi/005-correzioni-pipeline-musicale.md) — implementazione, uso e verifiche.

- [Audit dei file musicali non referenziati](analisi/006-file-non-referenziati.md) — elenchi MP3, PDF e LilyPond con evidenze.

- [Scale: primo blocco di esercizi](analisi/007-esercizi-scale-primo-blocco.md) — stesura e verifiche.

- [Scale: esercizi avanzati](analisi/008-esercizi-scale-avanzati.md) — otto studi con pentagramma, tablatura e audio a due velocità, 10 novembre 2026.

- [Arpeggi: sezione Esercizi](analisi/009-esercizi-arpeggi.md) — dieci studi con pentagramma, tablatura e audio a due velocità, 10 novembre 2026.
