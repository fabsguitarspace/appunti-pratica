# Analisi — Vocabolario avanzato: accordi minori e dominanti

- Data: 2026-11-10
- Stato: realizzato su richiesta esplicita dell’utente.
- Ambito: prosecuzione del modello degli accordi maggiori nella sezione Vocabolario avanzato di Pratica.

## Problema e obiettivi

Il vocabolario avanzato conteneva soltanto i maggiori. Estendere il criterio della nota al canto fissa agli accordi minori e dominanti, con Do sulla seconda corda e Fa sulla prima, conservando il materiale precedente.

## Struttura attuata

- Minori: R, 9, ♭3, 11, 5, 6/13, ♭7, Δ7 su entrambe le corde previste: 16 gruppi.
- Dominanti: R, ♭9, 9, ♯9, 3, 11/sus4, ♯11, 5, ♭13, 13, ♭7 su entrambe le corde: 22 gruppi.
- Tre voicing di quattro note per gruppo, totale 114. Ciascun gruppo ha diagrammi delle corde, pentagramma ottavizzato, tablatura e audio a 60 BPM con quattro impulsi iniziali. Nessun nuovo link «Scarica…».
- Spiegazioni per minore sesta, minore settima e minore con settima maggiore, tensioni naturali/alterate, sospensioni e omissioni. Le forme senza fondamentale sono indicate nel testo; la sigla descrive l’armonia di riferimento, non il basso del voicing.

## Scelte musicali e alternative

Preferita una raccolta mirata di tre disposizioni per nota al canto anziché un catalogo combinatorio completo. I voicing possono omettere fondamentale, quinta ed estensioni non essenziali; tutte le note effettivamente suonate appartengono alla sonorità dichiarata. Il generatore richiede terza minore più sesta o settima appropriata per i minori, terza maggiore e settima minore per le dominanti non sospese, quarta e settima minore senza terza per i sus4.

La 13 naturale e la settima maggiore del minore sono confronti di colori specifici, non prescrizioni per ogni m7. L’11 naturale delle dominanti è sviluppata come sus4 e distinta dalla ♯11. La ♯9 è scritta Re♯ su C e Sol♯ su F.

Le forme usano quattro corde distinte, nessuna corda a vuoto, note in ordine ascendente e massimo quattro tasti di differenza fra il minimo e il massimo. Su indicazione successiva dell’utente, il basso dei nuovi voicing è limitato a fondamentale, terza, quinta o settima, escludendo nona, undicesima e tredicesima (anche la sesta naturale viene tenuta fuori dal basso). La selezione deterministica preferisce forme compatte, con pochi salti di corda e fondamentale quando possibile. Tali vincoli non sostituiscono una verifica esecutiva personale sulla chitarra.

## Fonti consultate

- Wayne Naus, Berklee Today, «Creating melody-driven chord progressions»: https://college.berklee.edu/berklee-today-55 — rapporto fra nota melodica, tono cordale e tensione; ripreso come riferimento di approfondimento nel capitolo.
- Berklee Online / Randy Felts, «Chord Substitution and Reharmonization»: https://online.berklee.edu/takenote/reharmonization-simple-substitution/ — riferimento sul contesto funzionale; nessuna trascrizione di esempi o diagrammi delle fonti.

Le forme della raccolta sono originali, generate e controllate in questo progetto.

## Produzione e dipendenze

Applicato ADR 0001. `scripts/generate_chord_vocabulary.py` contiene profili armonici, vincoli chitarristici e selezione delle forme. Eseguire `python3 scripts/generate_chord_vocabulary.py` per generare i 38 sorgenti `accordi-{c,f}-{minore,dominante}-GRADO[-1].ly`. I nomi esatti sono restituiti da `catalogue()` nel generatore. Compilare con `./build-lilypond.sh --source NOME` ripetuto per i nomi base interessati. Non modificare manualmente i file generati.

Corde e tasti selezionati definiscono sia note del pentagramma, sia diagrammi e TAB, sia MIDI. Nel MIDI suona una sola parte di accordi, senza raddoppio dovuto alla tablatura. Il generatore usa solo la libreria standard Python e non modifica la pipeline esistente. Ogni sorgente produce PDF/SVG/MIDI/MP3; nella pagina sono incorporati SVG e MP3.

## Verifiche eseguite

- Compilazione dei 38 sorgenti con produzione delle 152 risorse musicali.
- Ispezione visiva dei 38 PDF, ciascuno di una pagina, mediante cinque fogli di contatto. Allargata la spaziatura per evitare sovrapposizioni fra diagrammi e sigle.
- Cinque test in `tests/test_chord_vocabulary.py`: copertura/nota al canto, corde/tasti e profili armonici, terze/settime/sus4, assenza di estensioni al basso, corrispondenza fra grafia delle note e tasti compresa la ♯9.
- Verifica MIDI con mido per i 38 esempi: quattro note di conteggio e tre accordi di quattro note, altezze/attacchi/durate esatti e tempo di 60 BPM; nessun raddoppio della tablatura.
- MP3: durata coerente, decodifica PCM riuscita, segnale presente e nessun campione al limite di saturazione. Non effettuato ascolto umano dei 38 audio.
- Build HTML con avvisi trattati come errori; 38 nuove immagini e 38 nuovi audio risolti nella pagina.
- Confronto con HEAD: contenuti essenziali e maggiori preesistenti conservati, al netto dei terminatori di riga e degli spazi finali.

Non modificati gli altri capitoli, il progetto Teoria o le risorse musicali dei maggiori. Restano nei log musicali gli avvisi ambientali Fontconfig e sul preset percussivo non usato del canale 9; compilazione e sintesi riuscite.

## Revisione successiva del basso

Su richiesta dell’utente sono stati sostituiti 17 dei 114 voicing per evitare tensioni al basso, mantenendo copertura, note al canto e tre forme per gruppo. Nel gruppo con fondamentale al canto delle dominanti la nona è stata sostituita da una seconda disposizione di settima, più compatta con il nuovo vincolo. Aggiornati testo, figure e audio, e ripetuti i controlli. Vedi anche [uniformazione grafica](011-stile-spartiti-accordi.md).
