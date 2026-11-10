# Analisi — Licks bebop e collegamento con Progressioni

- Data: 2026-11-10
- Stato: completato; commit e push autorizzati dall’utente.
- Perimetro chiarito dall’utente: cinquanta licks totali, non cinquanta per categoria.

## Risultato

Capitolo Licks sviluppato con dieci frasi per ciascuna categoria: maggiori (M01–M10), minori (N01–N10), dominanti (D01–D10), progressioni bebop (P01–P10), blues (B01–B10). Cinquanta melodie distinte, composte per gli appunti, non trascrizioni attribuite al repertorio e non semplici trasposizioni di una stessa frase.

Ogni esempio ha griglia armonica, durata, ultima nota, spiegazione della cellula, rimando alla sezione pertinente di Progressioni, pentagramma ottavizzato, TAB e audio con accompagnamento più piano. I licks statici durano due battute; quelli su progressioni e blues quattro. Per i blues sono precisate le finestre nel chorus o la variante didattica, senza confonderle con una forma completa.

## Collegamento didattico

Aggiunte ancore stabili alle sezioni del capitolo Progressioni, una tabella di ingresso in Licks e un percorso di uscita da Progressioni verso specifiche frasi. Nessuna modifica alle griglie o ai materiali musicali del capitolo Progressioni.

Esercizi concreti: prime due battute di P01 più M01 sul II–V–I maggiore; prime due di P03 più N03, prolungando Cm6, nel minore; cellula di D02 sulla mezza battuta finale di G7; B01, B03 e B04 sulle finestre 1–4, 5–8 e 9–12 del blues di base. Il testo verifica esplicitamente le durate: una frase di due battute su un accordo non va sovrapposta automaticamente a un accordo della durata di una sola battuta.

## Materiale musicale

Arpeggi, note d’approccio cromatiche, enclosure, discesa bebop dominante, seste/noni, cromatismi blues, dominanti secondarie, tritono, backdoor, diminuito e cambi di centro. Le tre sonorità minori m7, m6 e m(maj7) restano distinte.

Riferimento audio a 90 BPM con swing regolare 2:1, quattro impulsi iniziali e un solo passaggio per file. La notazione conserva gli ottavi convenzionali. Una mappa razionale degli attacchi riproduce il primo ottavo su due terzi di movimento e il secondo su un terzo; mantiene durata di ogni battuta e sincronizzazione con gli accordi. Il testo dichiara il rapporto come riferimento di studio, non come descrizione di qualsiasi esecuzione jazz.

La TAB usa una posizione di riferimento coerente per le medesime altezze e prosegue sulla prima corda nel registro acuto, fino al ventesimo tasto. Le grafie funzionali dei cromatismi, della nona aumentata e del sostituto di tritono sono controllate; Mi doppio bemolle nel lick P07 è spiegato nel testo.

## Produzione

`scripts/generate_bebop_licks.py` contiene cinquanta melodie scritte esplicitamente con durate, sigle e analisi; non usa generazione casuale. Eseguire `python3 scripts/generate_bebop_licks.py`, poi `./build-lilypond.sh --source NOME` per i cinquanta nomi licks-* restituiti da catalogue(). Il generatore aggiorna soltanto il catalogo fra i marcatori BEGIN/END del capitolo, preservando introduzione e metodo di studio scritti fuori da quei marcatori.

I file .ly generati non vanno modificati a mano. Un’unica definizione alimenta note e TAB, playback swing e accompagnamento. Il MIDI ha due parti sonore, melodia e accordi; la TAB non raddoppia la riproduzione. Riutilizzati i voicing di `generate_progressions.py`, aggiunto soltanto C6. Prodotti cinquanta PDF, cinquanta SVG, cinquanta MIDI e cinquanta MP3 mediante la pipeline esistente. Nessun link «Scarica…» aggiunto.

## Fonti consultate

Jazz Lesson Videos, Approach Note and Enclosure Exercises: https://www.jazzlessonvideos.com/post/15-approach-note-and-enclosure-exercises-that-every-jazz-musician-should-know — riferimento sul lessico di approccio/enclosure, citato per approfondimento. Nessun loro esercizio o spartito è stato riprodotto. Le frasi degli appunti sono originali e seguono i contesti armonici già sviluppati nel progetto.

## Verifiche

- Cinque test in tests/test_bebop_licks.py: conteggio e unicità, note/TAB e grafia, swing e durata delle battute, note finali/enclosure, collegamenti e finestre del blues.
- Cinquanta sorgenti compilati. Tutti i PDF hanno una pagina; ispezionati visivamente attraverso nove fogli di contatto, verificando anche leggibilità di alterazioni e numeri di tasto.
- Confrontati tutti i cinquanta MIDI con i dati musicali: altezze, attacchi swing, durate, accordi, conteggio e tempo di 90 BPM. Nessun raddoppio dovuto alla tablatura.
- MP3 controllati con ffprobe e decodifica PCM: durate coerenti, segnale presente e nessun campione al limite di saturazione. Nessun ascolto umano certificato.
- Build HTML con avvisi trattati come errori, cinquanta immagini e cinquanta audio risolti, ancore e rimandi reciproci tra i due capitoli verificati.

## Copertura del volume

Licks era l’ultimo capitolo di Pratica rimasto al solo titolo. Nel controllo richiesto dall’utente è stato segnalato un completamento puntuale ancora aperto nel vocabolario maggiore di Accordi: 13 e Δ7 al canto sulla prima corda. Non aggiunti in questa lavorazione, dedicata a Licks. La presenza dei capitoli sviluppati non sostituisce una revisione musicale ed esecutiva integrale del volume.
