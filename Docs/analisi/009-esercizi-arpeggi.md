# Analisi — Esercizi sugli arpeggi

- Data: 2026-11-10
- Stato: realizzato su richiesta dell’utente di sviluppare la sezione Esercizi.
- Ambito: solo sezione Esercizi del capitolo Arpeggi e relativi nuovi materiali.

## Problema e obiettivi

La sezione conteneva soltanto il titolo. Collegare le mappe degli arpeggi a un percorso di studio che integri riconoscimento delle note, ritmo, spostamenti sulla tastiera e cambi di accordo.

## Struttura attuata

Quattro studi di base: salita/discesa, partenze da terza/quinta/settima, confronto C6/C7/Cmaj7, confronto Cm6/Cm7/Cm(maj7). Sei avanzati: ordine delle note e posizioni, none, dominante aumentata e diminuito completo, fraseggio, II–V–I maggiore e minore. Schede con scopo, procedura, ascolto, varianti e verifica; indicazioni per trasporto e sessione breve.

Ogni esempio ha pentagramma ottavizzato e tablatura con corde esplicite in accordatura standard, più audio a 60/90 BPM con quattro impulsi iniziali sul Do acuto. Quattro oppure otto battute, una sola parte melodica nel MIDI, nessun accompagnamento. Rispettata la preferenza espressa dall’utente: nessun link «Scarica…» aggiunto alla pagina.

Nel minore sono introdotte esplicitamente le note del semidiminuito e della dominante con nona minore; sul diminuito completo Si doppio bemolle conserva la grafia funzionale pur suonando come La nel temperamento equabile. Le note dei II–V–I rispettano le sigle di ogni battuta; i confini sono collegati da movimenti di semitono spiegati nel testo.

## Produzione e dipendenze

Applicato ADR 0001. `scripts/generate_arpeggio_exercises.py` è la fonte delle definizioni musicali e genera i venti file `src/lilypond/arpeggi-esercizioNN[-90].ly` (NN da 01 a 10). Non modificare manualmente i file generati. Eseguire `python3 scripts/generate_arpeggio_exercises.py`, poi `./build-lilypond.sh` con `--source` ripetuto per i venti nomi base. Il generatore usa soltanto la libreria standard Python; le risorse sono prodotte dalla pipeline musicale già presente.

Spartito, tablatura e MIDI condividono una sola definizione della melodia; la tablatura non raddoppia le note riprodotte. La pipeline produce PDF/SVG/MIDI/MP3 per ciascuna velocità. Nella pagina si mostrano gli SVG a 60 BPM e i due lettori audio. Non modificati catalogo precedente degli arpeggi, pipeline o progetto Teoria.

## Verifiche eseguite

- Compilazione dei venti sorgenti con produzione delle ottanta risorse.
- Ispezione visiva dei dieci spartiti a 60 BPM, tutti di una pagina; gli studi di otto battute sono disposti su due sistemi.
- Quattro test musicali senza dipendenze esterne in `tests/test_arpeggio_exercises.py`: appartenenza delle note agli accordi delle singole battute; conservazione delle altezze nel cambio di posizione; note guida ai confini armonici; grafia della quinta aumentata e della settima diminuita.
- Confronto MIDI mediante mido per tutte le venti versioni: altezze, attacchi, durate, tempo, conteggio e accenti. Verificata l’assenza di raddoppi dovuti alla tablatura.
- MP3 controllati con ffprobe e decodifica PCM: durata coerente, segnale presente, nessun campione al limite di saturazione. Non effettuato ascolto umano dei venti audio.
- Build HTML con avvisi trattati come errori: riuscita. Verificati dieci riferimenti immagine e venti riferimenti audio nella pagina generata, tutti risolti; nessun link di download.

Restano nei log gli avvisi ambientali Fontconfig e sul preset percussivo del canale 9 non usato dalla parte melodica; compilazione e sintesi riuscite. La verifica strutturale e visiva non sostituisce una revisione esecutiva sulla chitarra.
