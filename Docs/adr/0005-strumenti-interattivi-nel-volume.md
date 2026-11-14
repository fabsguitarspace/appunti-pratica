# ADR 0005 — Strumenti interattivi nel volume

- Stato: Accettato
- Data: 2026-11-12
- Decisore: utente responsabile del progetto, nella conversazione di lavoro del 2026-11-12
- Ambito: questo progetto; appunti-strumenti (ex Guitar-Scale-Practice)
- Analisi collegata: [019 — Capitolo di strumenti interattivi](../analisi/019-capitolo-strumenti-interattivi.md)

## Contesto ed evidenze

Il volume ha esempi fissi (LilyPond → SVG/MP3, ADR 0001). Guitar Scale Practice (GSP) è un'app web statica, senza build e funzionante da `file://`, che genera esercizi sulle scale con audio, tablatura e metronomo. L'utente chiede un capitolo che porti nel volume GSP e strumenti analoghi per Arpeggi, Accordi e Progressioni. La build Sphinx è `-W`; RTD produce anche PDF ed ePub; finora RTD non dipende da altri repository (ADR 0004, punto 5).

## Opzioni considerate

Stato attuale (nessun capitolo); GitHub Pages con link; sottomodulo copiato nell'output Sphinx; riscrittura in `_static`. Presentazione: link a schermo intero, `<iframe>`, link ora e vista incorporabile dopo. Confronto nell'analisi 019.

## Decisione

1. Gli strumenti restano nel repository GSP, che diventa una suite multipagina (Scale, Arpeggi, Accordi, Progressioni) con nucleo comune — ADR 0010 di GSP.
2. Pubblicazione (punto **deciso dall'utente il 2026-11-12**, opzione A1 dell'analisi 019): gli strumenti si pubblicano con **GitHub Pages** dal loro repository `fabsguitarspace/appunti-strumenti` (rinomina di Guitar-Scale-Practice decisa dall'utente il 2026-11-12), all'indirizzo `https://fabsguitarspace.github.io/appunti-strumenti/`, con un ciclo di vita indipendente dal volume. Il volume vi rimanda con link; l'indirizzo base è definito una sola volta in `conf.py` (sostituzione o `extlinks`), così un cambio di dominio tocca un solo punto. Nessun sottomodulo, nessuna modifica a `.readthedocs.yaml`.
3. Nuovo capitolo **«Strumenti per la pratica»**, ultimo nel toctree dopo Percorsi d'autore (titolo e posizione decisi dall'utente il 2026-11-12), una pagina per strumento: scopo, rimando al capitolo, figura, pulsante «Apri lo strumento» a schermo intero, esercizi pronti come deep link. Niente `<iframe>` nella prima versione.
4. Una riga di rimando in fondo alle sezioni Esercizi dei capitoli 4–7 (deciso dall'utente il 2026-11-12), aggiunta man mano che ciascuno strumento è pubblicato.
5. Contenuto interattivo sotto `.. only:: html`; nei formati PDF/ePub un testo alternativo con indirizzo pubblico.
6. Coerenza visiva (opzione D1 dell'analisi 019): GSP adotta ovunque, anche fuori dal volume, un tema «Appunti» (neutri e accento rosso del volume, stessi caratteri di sistema), mostra una testata con logo e ritorno al capitolo.
7. Chiaro/scuro: con domini diversi lo strumento non vede la scelta salvata da Shibuya. Mitigazione proposta: un piccolo script del volume (`html_js_files`) aggiunge ai link verso gli strumenti il tema corrente (`&theme=dark|light`); lo strumento lo applica come `data-theme` e altrimenti segue `prefers-color-scheme`.
8. Uscita per fasi: capitolo con il solo strumento Scale, poi una pagina per strumento completato, nell'ordine Arpeggi → Accordi → Progressioni. La prima uscita del capitolo porta il volume alla versione 1.1 (`release` in `conf.py`).

Motivazione: aggiornare gli strumenti senza ricostruire il volume; indirizzo autonomo utilizzabile anche nei video e dagli altri due volumi; build RTD invariata; nessuna duplicazione di codice; l'app resta mobile-first a pagina intera.

## Conseguenze

- Editoriale: un capitolo nuovo e quattro righe nei capitoli esistenti; nessun impatto su LilyPond e MP3.
- Tecnico: la build del volume non cambia; serve attivare GitHub Pages sul repository degli strumenti.
- Stabilità dei link: le versioni pubblicate del volume restano online mentre gli strumenti evolvono. Lo schema dei deep link è quindi un'interfaccia pubblica: versionato (`v=1`), retrocompatibile, coperto da test in GSP; i link del capitolo vanno controllati prima di ogni rilascio del volume.
- GSP: chiavi `localStorage` con prefisso per strumento (più pagine sulla stessa origine Pages).
- Reversibile: si può passare in seguito al sottomodulo sul dominio RTD (opzione A2) cambiando l'indirizzo base in `conf.py`.

## Verifica

- `./build.sh` pulito con `-W`.
- Strumenti raggiungibili su GitHub Pages; ogni deep link del capitolo apre lo strumento con la configurazione attesa (controllo automatizzabile con un elenco dei link).
- PDF ed ePub senza riferimenti rotti e con l'alternativa testuale.
- Prova su iPhone e Android: audio, wake lock, layout.
- Passando dal volume allo strumento e ritorno: stesso tema chiaro/scuro (tramite il parametro `theme`), stesso accento, contrasti WCAG AA su tastiera e tablatura in entrambi i temi.

Decisioni dell'utente (2026-11-12): tema visivo D1; pubblicazione su GitHub Pages (A1); nome del repository `appunti-strumenti`; capitolo «Strumenti per la pratica» in ultima posizione; rimandi nei capitoli 4–7; ordine Arpeggi → Accordi → Progressioni; versione 1.1 alla prima uscita. Nessuna questione aperta; ADR accettato lo stesso giorno.

## Note di attuazione

2026-11-12, strumento Scale: capitolo `11-strumenti-per-la-pratica.rst` con **una sezione per strumento** nella stessa pagina (punto 3: le pagine separate si valuteranno quando gli strumenti saranno più di uno) e senza schermata per ora; link aperti in una nuova scheda da `strumenti.js`. Dettagli e verifiche nell'analisi 019, «Esito dell'attuazione».

2026-11-14, strumento Arpeggi: sezione «Arpeggi» nel capitolo 11 con nove esercizi pronti, rimando in fondo agli esercizi di `5-arpeggi.rst`, `arpeggi.html` nel test dei link. La pagina unica del capitolo resta adeguata con due strumenti. Dettagli nell'analisi 019, «Esito dell'attuazione (Arpeggi)».

2026-11-14, strumento Accordi: sezione «Accordi» nel capitolo 11 con nove esercizi pronti, rimando in fondo a «Una routine breve» degli shell voicing in `6-accordi.rst`, `accordi.html` nel test dei link. Con tre strumenti la pagina unica resta leggibile; da rivalutare con Progressioni. Dettagli nell'analisi 019, «Esito dell'attuazione (Accordi)».

## Collegamenti

- [ADR 0001](0001-lilypond-diretto-e-generazione-python.md) e [ADR 0004](0004-libreria-musicale-comune.md): invariati; RTD continua a non dipendere da altri repository.
- GSP: `Docs/ADR-0010-suite-di-strumenti.md`, `Docs/plans/0002-suite-pratica.md`.
- Il numero 0005 è libero in tutti e tre i progetti di appunti.
