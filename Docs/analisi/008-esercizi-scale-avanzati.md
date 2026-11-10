# Analisi — Raccolta di esercizi avanzati sulle scale

- Data: 2026-11-10
- Stato: realizzata su approvazione dell’utente alla proposta degli otto studi.
- Ambito: Pratica, capitolo Scale, sottosezione Esercizi avanzati.

## Obiettivi e struttura

Proseguire gli esercizi di base con direzioni alternate, terze alternate, quarte/seste, cellule di tre in ottavi, accenti ogni tre note, collegamento fra posizioni, confronto maggiore/minore melodica/dorico e frase conclusiva di otto battute. Ogni scheda comprende scopo, procedura, ascolto, varianti e verifica.

## Attuazione e dipendenze

Pentagramma ottavizzato e tablatura in accordatura standard, con corde esplicite. Ogni studio dura quattro oppure otto battute. PDF scaricabile, SVG incorporato e audio a 60/90 BPM con quattro impulsi di conteggio sul Do acuto. Nessun accompagnamento o conversione swing. Disponibile anche un PDF complessivo di otto pagine.

Applicato ADR 0001: `scripts/generate_advanced_scales.py` contiene le definizioni musicali e genera sedici file `src/lilypond/scale-avanzati-NN[-90].ly`. Non modificarli a mano. Eseguire `python3 scripts/generate_advanced_scales.py`, quindi `./build-lilypond.sh` con `--source` ripetuto per i sedici nomi base. Infine eseguire `.venv/bin/python scripts/generate_advanced_scales.py --collect-pdf` per ricomporre il PDF complessivo. La definizione della melodia è condivisa fra pentagramma, TAB e MIDI. Nel MIDI suona una sola parte, evitando il raddoppio della tablatura.

La variante a 90 BPM produce anch’essa PDF/SVG per rispettare il contratto esistente della pipeline; nella pagina si mostra la partitura a 60 BPM. Non modificati gli esercizi di base, la pipeline o il progetto Teoria.

## Verifiche

- Generatore: battute complete, estensione fra quattro e otto battute, corde esplicite e tasti fra 5 e 12.
- Compilazione selettiva dei sedici sorgenti e generazione di PDF/SVG/MIDI/MP3.
- Ispezione visiva di tutti gli otto spartiti a 60 BPM; studi di otto battute distribuiti su due sistemi.
- Verifica MIDI indipendente con mido: altezze, attacchi, durate, conteggio iniziale, tempo e accenti confrontati con gli eventi sorgente; nessun raddoppio di note.
- Verifica MP3 con ffprobe e decodifica PCM: durate coerenti con conteggio/esecuzione/coda del sintetizzatore, segnale presente e nessun campione al limite di saturazione.
- Build HTML con avvisi trattati come errori; controllo dei riferimenti grafici, audio e download.

Limite: questi controlli non costituiscono un ascolto umano dei sedici audio. Rimane utile la revisione esecutiva sulla chitarra delle diteggiature proposte. Nei log musicali restano gli avvisi ambientali Fontconfig e il preset del canale percussivo 9 non usato; la compilazione e la sintesi sono riuscite.
