# Modern jazz e fusion nei due volumi

Data: 10 novembre 2026. Perimetro approvato dall'utente: ampliare il percorso di Teoria e aggiungere gli studi corrispondenti in Pratica. Il successivo elenco di dieci artisti ha ricevuto una proposta di struttura separata; i percorsi d'autore non sono implementati in questo intervento.

## Obiettivi e scelte

Collegare Progressioni e Licks a vamps, quarte, triadi superiori, pentatoniche sovrapposte, side-slip, sviluppo ritmico, 5/4, 7/8 e modulazione metrica. Evitare che modern jazz e fusion vengano presentati come un unico vocabolario obbligatorio. Conservare la definizione di shell a tre sole voci sulle corde 6–4–3 o 5–4–3.

Pratica aggiunge `9-modern-jazz-fusion.rst`: 12 studi originali con pentagramma/TAB, audio completo e base senza la parte di chitarra; tre partiture di basso e batteria spiegano gli accompagnamenti. Gli studi 01–02 trasformano il nucleo Mi–Sol–Si del lick M01. Le basi contengono realmente basso, batteria e sostegno armonico. Non sono introdotti collegamenti «Scarica».

Teoria amplia il capitolo 10 e introduce `12-ritmo-sviluppo.rst` prima delle letture conclusive del capitolo 11. Il nome 12 preserva gli URL esistenti; l'ordine didattico è stabilito dall'indice. Quattro esempi strumentali generici (tre groove e modulazione metrica) sono condivisi con Teoria.

## Fonti musicali e riproduzione

Fonte autorevole: `scripts/generate_modern_studies.py`; genera 28 sorgenti LilyPond (12 studi, 12 basi, tre groove, un esempio ritmico). I dati condivisi descrivono durate razionali, altezze, corde, basso, batteria e cambi di tempo. Le parti MIDI e scritte derivano dagli stessi eventi. Lo studio 10 passa da semiminima 80 a 120 mantenendo la vecchia semiminima in terzina come nuova semiminima.

`generate_rhythm_soundfont.py` sintetizza campioni originali di basso, cassa, rullante, charleston e ride, senza campioni esterni. `PracticeRhythm.sf2` fornisce programma 33/banco 0 e programma 0/banco 128. Jazzernaut continua a fornire il timbro della chitarra. I timbri sono riferimenti sintetici, non esecuzioni umane.

La pipeline supporta `--soundfont-overlay` e la dichiarazione `% soundfont-overlay: percorso-relativo-al-sorgente` nei file LilyPond. Gli studi dichiarano la loro dipendenza: anche la normale compilazione selezionata o completa usa i campioni corretti senza opzioni aggiuntive. Ogni SoundFont partecipa all'impronta di aggiornamento; una risorsa mancante arresta il processo prima della promozione degli output. Gli altri sorgenti conservano il comportamento precedente.

Rigenerazione dalla radice:

```sh
.venv/bin/python scripts/generate_rhythm_soundfont.py
.venv/bin/python scripts/generate_modern_studies.py
./build-lilypond.sh --source modern-01 --source modern-01-base
```

Ripetere `--source` per gli altri nomi modern-* oppure compilare l'intero repertorio quando necessario. Copiare PDF/SVG/MIDI/MP3 di `modern-groove-44`, `modern-groove-54`, `modern-groove-78`, `modern-metric` nel progetto Teoria dopo la rigenerazione. Queste copie sono pubblicate con il libro; i sorgenti rimangono in Pratica.

## Criteri di verifica

- Build HTML con avvisi trattati come errori in entrambi i progetti.
- Test di regressione della pipeline: invalidazione per SoundFont esplicito e dichiarato, percorsi con spazi, arresto per overlay mancante e conservazione degli output.
- Test degli studi: durata di ciascuna battuta e parte, accordatura, riproducibilità sorgenti/campioni, note della chitarra nel MIDI, ruoli, conteggio e tempi; tolleranza di un microsecondo nel tempo 84 BPM per arrotondamento LilyPond.
- Apertura e rasterizzazione dei PDF; controllo visivo delle 16 partiture distinte. Le basi ripetono il medesimo spartito della chitarra, con titolo differente.
- Decodifica dei 24 MP3 degli studi/basi: presenza di segnale e assenza di clipping; verifica separata della percussione sintetica. Il messaggio iniziale FluidSynth di preset percussivo mancante proviene dal caricamento del primo SoundFont, prima dell'overlay; il banco percussivo dell'overlay è presente e produce segnale.
- Rimandi e risorse locali controllati sulle pagine generate. I link tra libri puntano agli URL pubblici, che mostreranno i nuovi contenuti dopo la rispettiva pubblicazione.

## Limiti

Nessuna dichiarazione di completezza musicologica dei due libri. Non include nuovi percorsi d'autore o trascrizioni. Restano fuori perimetro i due gruppi mancanti del vocabolario maggiore già segnalati. Le verifiche HTML non certificano l'impaginazione dell'intero libro PDF/ePub.
