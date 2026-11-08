# Pipeline musicale — correzioni e sostituzione di pdfcrop

Data: 2026-11-08. Implementazione applicata a entrambi i progetti.

## Uso

Installare nell'ambiente Python locale le dipendenze di `requirements-music.txt` (`python -m pip install -r requirements-music.txt`). Servono inoltre LilyPond, Ghostscript (`gs`), pdf2svg, FluidSynth e LAME nel PATH. Non occorrono pdfcrop o una distribuzione TeX per questa pipeline.

- Tutti i sorgenti: `sh build-lilypond.sh`.
- Output isolato: `sh build-lilypond.sh --output-dir /percorso/temporaneo`.
- Singolo sorgente: aggiungere `--source nome-senza-estensione`, ripetibile.
- Rigenerazione forzata: aggiungere `--force`.

Il comando funziona anche fuori dalla radice. Il primo avvio non ha un manifest e rigenera tutte le unità selezionate: per questo i controlli sono stati eseguiti con destinazioni temporanee. Nessun media esistente è stato sovrascritto durante la verifica.

## Correzioni

Il wrapper shell richiama `scripts/build_music.py`. La firma di aggiornamento considera contenuto del sorgente, include locali `.ly`/`.ily` sotto directory, soundfont, eseguibili, versione del ritagliatore e PyMuPDF e contenuto del builder. L'invalidazione è conservativa: un cambio agli include o al soundfont rigenera l'intera unità, anche se solo una fase ne ha bisogno. Le impronte degli output riconoscono file mancanti o alterati, incluso il MIDI quando prodotto dall'ultima compilazione riuscita.

Ogni unità è lavorata in una directory temporanea nella destinazione. Solo dopo il successo di tutte le fasi e il controllo dei file non vuoti si promuovono gli output. Il manifest viene invalidato prima della promozione e scritto a fine operazione: un'interruzione richiede una nuova build. La sostituzione è atomica per file, non per l'intero insieme; la pubblicazione non deve leggere una build in corso. Un lock impedisce due scrittori sulla stessa destinazione. Le unità già riuscite restano disponibili se una successiva fallisce.

Stato e log sono in `.music-build/`, ignorata da Git. Gli asset pregressi non vengono cancellati. Gli output prima gestiti ma non più prodotti e i sorgenti rimossi sono segnalati per revisione.

## Ritaglio

`pdfcrop` è stato sostituito esplicitamente da pdfCropMargins 2.2.1: bounding box mediante Ghostscript (`-c gb`), margine residuo percentuale zero (`-p 0`) e ampliamento di 10 punti (`-a -10`). Si scrive un PDF separato prima di sostituire il PDF temporaneo. Il rendering usato per individuare i limiti non implica rasterizzare la partitura di uscita.

Riferimento: https://github.com/abarker/pdfCropMargins . È un cambiamento dello strumento, non un'installazione del comando TeX pdfcrop. La variante SVG nativa di LilyPond resta una valutazione futura.

## Verifiche eseguite

- Test isolato con strumenti simulati: generazione, salto invariato, MIDI mancante, modifica include, modifica soundfont, SVG alterato, fallimento conversione con conservazione degli output, recupero e percorsi con spazi. Eseguibile con `.venv/bin/python tests/test_music_pipeline.py`.
- Conversione reale completa di `scala-maggiore-verticale-c1` in Pratica e `scala-c-maggiore` in Teoria, in `/private/tmp/appunti-crop-pratica` e `/private/tmp/appunti-crop-teoria`; secondo avvio senza conversioni superflue.
- Ispezione visiva dei PDF renderizzati: pentagrammi, diteggiature e tablatura integri nei campioni. Verifica strutturale: nessuna immagine raster incorporata e presenza di tracciati vettoriali. Generati anche SVG, MIDI e MP3; non effettuato ascolto audio.

## Limiti e lavoro residuo

Non eseguita ancora una nuova rigenerazione completa dei 257 sorgenti con il ritagliatore sostituito. Il contratto resta un PDF e un SVG omonimi e al massimo un MIDI; nomi multipli non supportati vengono respinti. La gestione di un PDF multipagina resta quella preesistente: pdf2svg senza numero di pagina converte la prima pagina; prima di usare partiture multipagina occorre estendere il contratto. Non sono controllati gli include esterni al repository né tutte le librerie di sistema degli eseguibili. Le dipendenze transitive Python non sono completamente bloccate. Lock tramite `fcntl`: supportati macOS/Linux, non Windows. Nessuna eliminazione automatica di asset senza sorgente o audio non più previsto. Le dipendenze musicali sono separate da quelle Sphinx e non vengono installate su Read the Docs dalla configurazione corrente.
