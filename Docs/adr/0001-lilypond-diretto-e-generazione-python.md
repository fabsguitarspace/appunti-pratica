# ADR 0001 — LilyPond diretto e generazione Python per famiglie di esercizi

- Stato: Accettato
- Data: 2026-11-08
- Decisore: utente responsabile dei progetti, nella conversazione di lavoro
- Ambito: appunti-pratica e appunti-teoria; esteso ad appunti-repertorio il 2026-11-11 (vedi ADR 0004)
- Analisi collegate: [pipeline musicale](../analisi/001-pipeline-musicale.md), [prima rigenerazione controllata](../analisi/002-rigenerazione-controllata.md)

## Contesto ed evidenze

I progetti devono consentire di creare partiture di qualità mediante programmazione automatica, senza costruzione manuale in editor visuali, e ottenere risorse grafiche e audio coerenti.

Sono presenti complessivamente 257 sorgenti LilyPond al primo livello, oltre a macro e diagrammi personalizzati per chitarra. La prima prova isolata con LilyPond 2.26.0 ha compilato tutti i sorgenti senza errori di processo. Tale prova non certifica la qualità visiva o musicale: ritaglio e conversione SVG non sono stati eseguiti e non è stato effettuato ascolto.

La scelta riguarda il modo di descrivere e generare musica. È distinta dalla scelta della strategia di aggiornamento degli output e dall'eventuale semplificazione della pipeline grafica.

## Opzioni considerate

| Opzione | Benefici | Costi e limiti |
|---|---|---|
| Solo LilyPond scritto direttamente, stato attuale | Riutilizzo completo dei sorgenti e controllo delle personalizzazioni | Ripetizioni e manutenzione manuale quando aumentano le varianti |
| LilyPond diretto con generatori Python mirati | Riutilizzo delle macro; automazione progressiva di tonalità, ritmi, corde e diteggiature | Occorre definire modelli, validare la logica musicale e distinguere sorgenti generati e manuali |
| Abjad come livello di costruzione delle partiture | API Python per strutture di notazione e trasformazioni complesse | Nuova dipendenza e astrazione; adattamento delle personalizzazioni da valutare; LilyPond resta necessario |

Abjad non è stato provato sui progetti: il maggior costo rispetto ai modelli diretti è una valutazione architetturale contestuale, non il risultato di un confronto sperimentale.

## Decisione

Adottare LilyPond come formato di descrizione delle partiture e motore tipografico. Scrivere direttamente i file `.ly` per esempi singoli e impaginazioni particolari. Per famiglie di esercizi ripetitive usare Python per generare sorgenti `.ly` da modelli piccoli e riutilizzabili, mantenendo le convenzioni grafiche nelle macro e nei modelli LilyPond.

Non introdurre Abjad come dipendenza predefinita. Rivalutarlo se la manipolazione strutturata di voci, durate, raggruppamenti o strutture ritmiche rende i generatori diretti difficili da mantenere.

La generazione deve partire da una definizione musicale condivisa fra notazione e riproduzione. Il percorso previsto resta sorgente LilyPond → output grafici e MIDI → sintesi e codifica audio. L'uso di Python non implica la generazione separata e indipendente di uno spartito e di un audio potenzialmente divergenti.

## Conseguenze

- Nessuna migrazione complessiva dei 257 sorgenti esistenti; introduzione dei generatori per esigenze concrete.
- Nessun editor visuale richiesto nel flusso di produzione; ispezione degli output e ascolto restano controlli di qualità.
- I generatori devono gestire correttamente ortografia musicale, trasposizione, durate e vincoli chitarristici; una compilazione riuscita non ne dimostra la correttezza.
- Prima del primo generatore definire quali file siano generati, da quale input e con quale comando. Evitare correzioni manuali degli output generati che andrebbero perse al successivo avvio.
- Riutilizzare le macro esistenti dopo averne verificato le differenze tra i repository; questa decisione non ne impone la centralizzazione.
- Python diventa dipendenza del processo solo per le famiglie effettivamente generate. Versioni e dipendenze dovranno essere dichiarate nella successiva implementazione.
- Scelta reversibile: un eventuale futuro generatore Abjad potrà produrre LilyPond, previa verifica della compatibilità con le convenzioni adottate.

## Verifica e attuazione

Primo caso pilota suggerito: una famiglia di scale con varianti di tonalità e diteggiatura, pentagramma, tablatura e audio, senza ampliamento automatico dei contenuti pubblicati.

Criteri di accettazione del pilota:

1. Generazione ripetibile dagli input dichiarati, senza interventi in editor visuali.
2. Compilazione dei `.ly` prodotti e corrispondenza fra definizione musicale, notazione e MIDI.
3. Verifica di alterazioni, durate, corde, tasti e diteggiature; controllo visivo di PDF/SVG e ascolto dei campioni.
4. Modifica del modello comune propagata alle varianti, senza modifiche agli esempi scritti manualmente.
5. Origine e procedura di rigenerazione documentate; gestione delle dipendenze coerente con la futura strategia della pipeline.

L'ADR registra la scelta architetturale. Non implementa generatori, non modifica la pipeline e non decide la migrazione a SVG nativo o l'introduzione di una cache incrementale.

## Collegamenti

- [LilyPond: input testuale](https://lilypond.org/text-input.html)
- [Abjad: API Python per costruire file LilyPond](https://github.com/abjad/abjad)
- Nessun ADR precedente superato.

Una copia di questo ADR è mantenuta in ciascun progetto; modifiche alla decisione comune devono essere riportate in entrambe. Cambiamenti sostanziali futuri vanno documentati con un nuovo ADR che richiami questo.
