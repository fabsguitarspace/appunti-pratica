# Percorsi d'autore

Data: 10 novembre 2026. L'utente ha richiesto di completare i dieci percorsi proposti, mantenendo la richiesta di commit e push al termine.

## Obiettivo e struttura approvata

Django Reinhardt, Charlie Christian, Wes Montgomery, Jim Hall, Pat Metheny, Joe Pass, George Benson, Pat Martino, John Scofield e John McLaughlin. Un capitolo introduttivo e dieci pagine in Pratica; cinque esercizi progressivi e uno studio conclusivo per artista, con pentagramma/TAB e audio. Ascolti guidati, fonti riconoscibili, analisi di elementi precisi, applicazioni e criteri di autovalutazione. In Teoria un percorso di analisi collegato ai capitoli pertinenti e agli esempi pratici.

## Scelte editoriali e musicali

Gli studi sono originali: illustrano tecniche da confrontare con registrazioni documentate, senza presentarsi come trascrizioni o repliche delle esecuzioni degli artisti. Ogni autore è affrontato attraverso alcuni ingressi didattici; non si attribuisce un unico vocabolario all'intera carriera. Gli ascolti indicano versioni/album e compiti concreti, evitando minutaggi che cambiano fra edizioni.

Famiglie distinte: arpeggi e diminuiti; riff swing; ottave e accordi; sviluppo motivico e spazio; melodia modale; chitarra sola con basso e voci superiori; blues/bebop e canto; linee minori rilette sulle dominanti; groove e tensione; raggruppamenti e metri dispari. Gli shell conservano esclusivamente le corde 6–4–3 e 5–4–3; negli accordi completi il basso è tonica, terza o quinta. Nessun link «Scarica».

## Dipendenze e verifiche previste

LilyPond resta la fonte degli spartiti. Un nuovo generatore raccoglie gli eventi comuni a notazione/TAB/MIDI e le spiegazioni degli esercizi, riutilizzando il timbro ritmico originale e la pipeline già verificata. Le basi degli studi finali omettono la chitarra; per la chitarra sola la base è un riferimento ritmico e non aggiunge accordi che altererebbero il compito.

Verificare note e accordatura, totali ritmici, swing esplicito rispetto alla notazione convenzionale, voci indipendenti negli studi di chitarra sola, presenza delle parti nelle basi, tempo e conteggio; generare/renderizzare gli spartiti e controllare le pagine HTML con avvisi come errori e i rimandi fra i volumi. Confermare i contenuti degli ascolti attraverso discografie degli artisti, etichette e istituzioni prima della redazione definitiva.

## Implementazione e risultati

Completati `src/docs/10-percorsi-autore.rst` e dieci pagine in `src/docs/autori/`, con 20 ascolti guidati, fonti discografiche, analisi, prerequisiti e autovalutazione. Collegati i capitoli Accordi, Licks e Modern jazz/fusion. Il nuovo capitolo 13 di Teoria comprende dieci analisi e confronti e rimanda agli studi; collegamenti di ritorno da armonia funzionale, non funzionale e ritmo.

Fonti editoriali canoniche: `scripts/artist_profiles.py` per presentazioni/ascolti/analisi; `scripts/generate_artist_studies.py` per 60 esempi musicali e relative consegne; `scripts/generate_artist_paths.py` per le pagine dei due volumi. Il generatore delle pagine richiede entrambi i repository affiancati con i nomi correnti. Genera file editoriali dichiaratamente derivati: modificare le fonti negli script e rigenerare per non perdere le correzioni.

Settanta sorgenti LilyPond e famiglie PDF/SVG/MIDI/MP3: 60 esempi completi e dieci basi degli studi finali. La dipendenza dal SoundFont di basso/batteria è dichiarata nei sorgenti e gestita dalla pipeline esistente. Le crome swing sono notate convenzionalmente e mappate a 2:1 sia per chitarra sia per ride; gli esempi regolari non subiscono questa trasformazione. Le versioni solo di Joe Pass non aggiungono sezione ritmica dopo il conteggio; la loro base finale è un riferimento di quattro impulsi per battuta.

Nel basso della chitarra sola si usano tonica, terza e quinta. Il generatore sceglie corde alternative in funzione delle note superiori tenute, evitando collisioni di corde e aperture simultanee superiori a quattro tasti (corde a vuoto escluse dal calcolo dell'apertura). È un controllo di compatibilità geometrica, non una garanzia di comodità per qualunque mano. I voicing completi degli altri esempi hanno la tonica al basso. Le doppie note melodiche sono distinte dai voicing completi e dagli shell.

Rigenerazione:

```sh
.venv/bin/python scripts/generate_artist_studies.py
.venv/bin/python scripts/generate_artist_paths.py
./build-lilypond.sh --source autori-django-01
.venv/bin/python tests/test_artist_studies.py
```

Ripetere `--source` per gli altri nomi `autori-*` quando necessario. Per il test completo gli output delle 70 sorgenti devono essere presenti. I test MIDI richiedono `mido` nell'ambiente musicale.

Verifiche eseguite:

- Build HTML di Pratica e Teoria con avvisi trattati come errori, entrambe riuscite.
- `tests/test_artist_studies.py`: 60 esempi/10 basi, totali ritmici, accordatura, corde e aperture, voci simultanee, altezze e attacchi MIDI, trasformazione swing, ruoli strumentali, conteggi iniziali, tempi e comportamento della base solo.
- Regressioni `tests/test_modern_studies.py` e `tests/test_music_pipeline.py`, riuscite.
- Aperte e rasterizzate tutte le 60 partiture distinte; controllate visivamente in dieci tavole per artista. Verificato il contratto di pagina singola anche nei dieci PDF delle basi. Corretto Sol♯ nelle dominanti di Mi mantenendo La♭ dove richiesto dal contesto.
- Decodificati tutti i 70 MP3: segnale presente e assenza di clipping.
- Verificate le 12 nuove pagine, i 70 lettori audio, le risorse e i collegamenti interni; le destinazioni dei rimandi fra i libri sono state confrontate con entrambi gli output locali, inclusi gli identificatori di sezione.

I collegamenti pubblici ai nuovi capitoli dipendono dalla pubblicazione dei due repository. Le verifiche non certificano l'impaginazione dell'intero libro PDF/ePub né la resa espressiva dei timbri sintetici. Non sono state aggiunte trascrizioni del repertorio né collegamenti «Scarica».

Gli attributi Git marcano PDF, MIDI, MP3 e SoundFont come binari, evitando conversioni di fine riga nei file musicali. La pulizia degli spazi nei sorgenti derivati è stata verificata confrontando gli SVG con quelli già controllati visivamente.
