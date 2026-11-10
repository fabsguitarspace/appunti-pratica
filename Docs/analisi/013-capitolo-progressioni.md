# Analisi — Capitolo Progressioni

- Data: 2026-11-10
- Stato: realizzato; commit e push autorizzati dall’utente al termine del lavoro.
- Ambito: capitolo Progressioni, materiali originali, rimandi ai capitoli precedenti. Inclusa nella consegna la correzione esplicita del perimetro degli shell richiesta durante il lavoro.

## Problema e risultato

Il capitolo conteneva soltanto il titolo. Costruito un percorso operativo che collega accompagnamento, ascolto delle voci, fraseggio, lettura della griglia e mantenimento della forma.

## Struttura

Lettura della griglia e ritmo armonico; metodo di studio; II–V–I maggiore; ritmo dell’accompagnamento; note bersaglio; II–V–I minore; turnaround diatonico e con dominante secondaria; dominanti secondarie; sostituzione di tritono; backdoor; diminuito di passaggio; blues maggiore, jazz e minore; vamp dorico; due centri tonali; studio AABA originale; schema di rhythm changes distinto dall’AABA originale; studio melodico di sintesi; basi, trasporto e verifica della sessione.

Diciassette esempi grafici con pentagramma ottavizzato e tablatura, venti audio inclusi tre riferimenti di accompagnamento senza melodia. Quattro impulsi iniziali, 60 BPM, ottavi regolari. Due esempi melodici comprendono anche accordi più piano. Le basi eseguono due giri del II–V–I maggiore/minore oppure un chorus del blues di base, senza cicli automatici.

Lo studio AABA contiene trentadue battute ed è scritto integralmente. Lo schema rhythm changes contiene invece A e bridge, otto battute ciascuno: il testo spiega esplicitamente come costruire A–A–B–A e non presenta le sedici battute dell’audio come un chorus completo. Tutte le linee e gli arrangiamenti sono originali; non sono trascrizioni delle melodie del repertorio.

## Vincoli musicali

Gli accompagnamenti indicati come shell usano soltanto tre note sulle corde 6–4–3 oppure 5–4–3, secondo la definizione esplicita dell’utente. I voicing a quattro note di semidiminuiti, dominante con nona minore, diminuiti completi e vamp sono dichiarati separatamente e non chiamati shell. Le tensioni non sono al basso; il pedale Re di Em7/D è la settima dell’accordo superiore, non un’estensione.

Le note effettive di ogni accordo sono verificate. Si mantiene la grafia Do♭ su D♭7 e la grafia di sensibile su E7/A7/D7. L’esempio melodico finale include una nona di Dm7 dichiarata come nota di collegamento; l’arrivo conclusivo su Do coincide con il cambio G7–Cmaj7 al terzo movimento dell’ultima battuta.

Non confusi accordi e ritmo degli attacchi; precisati i punti in cui due accordi occupano mezza battuta. Distinti il finale e il ritorno ciclico nei blues e nello studio AABA. Nessun nuovo link «Scarica…».

## Fonti

- Open Music Theory, Blues Harmony: https://viva.pressbooks.pub/openmusictheory/chapter/blues-harmony/
- Music Theory for the 21st-Century Classroom, Standard Chord Progressions: https://musictheory.pugetsound.edu/mt21c/StandardChordProgressions.html

Consultate per confronto sul lessico e sulle famiglie di progressioni; riferimenti di approfondimento nel capitolo. Non copiate le loro figure, trascrizioni o spiegazioni.

## Produzione e manutenzione

`scripts/generate_progressions.py` definisce corde/tasti, sigle, durate e linee melodiche; genera i venti sorgenti progressioni-*.ly elencati in STUDIES. Non editarli a mano. Eseguire `python3 scripts/generate_progressions.py`, poi `./build-lilypond.sh --source NOME` ripetuto per i nomi base. Prodotte ottanta risorse PDF/SVG/MIDI/MP3 tramite la pipeline esistente.

La definizione delle note e dei ritmi è condivisa fra spartito, TAB e MIDI. Negli esempi melodici il MIDI ha una parte di melodia e una di accompagnamento; la TAB non crea raddoppi. Le figure di accompagnamento non duplicano i diagrammi delle forme già presenti nel capitolo Accordi. Lo spartito di trentadue battute usa una singola pagina più alta per evitare troncamenti della conversione SVG, mantenendo larghezza di riga coerente con gli altri esempi.

## Verifiche

- Venti sorgenti compilati; PDF tutti di una pagina, ispezionati visivamente attraverso quattro fogli di contatto e controllo separato dello studio AABA.
- Quattro test in tests/test_progressions.py: durata di ogni battuta e forme, note dei voicing e corde degli shell, tritono/pedale, note melodiche rispetto all’accordo presente con l’eccezione della nona dichiarata.
- MIDI confrontati con le definizioni per tutti i venti esempi: note, attacchi, durate, conteggio e tempo; gestite separatamente le parti di melodia e accompagnamento, senza raddoppio della TAB.
- MP3 controllati tramite ffprobe e decodifica PCM: durate coerenti, segnale presente, nessun campione al limite di saturazione. Nessun ascolto umano certificato.
- Build HTML con avvisi trattati come errori; diciassette riferimenti immagine e venti riferimenti audio risolti.
- Ricontrollati i sette esempi shell corretti, con test che rifiuta tutte le combinazioni diverse da 6–4–3 e 5–4–3.

Non modificati pipeline, altri capitoli didattici o progetto Teoria oltre alla correzione di Shell voicings nel capitolo Accordi. Conservate le risorse storiche del blues già presenti e non collegate: i nuovi esempi hanno nomi dedicati e non sovrascrivono il lavoro precedente.
