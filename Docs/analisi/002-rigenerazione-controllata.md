# Rigenerazione controllata — prima misura

Data: 2026-11-08. Esecuzione sequenziale dei 257 sorgenti al primo livello, da destinazioni vuote sotto `/private/tmp/appunti-pipeline-benchmark`, senza alterare media o script dei progetti. Compilazione di ogni sorgente e conversione di ogni MIDI prodotto con il soundfont del rispettivo repository. Dati grezzi: [benchmark-risultati.json](benchmark-risultati.json).

| Progetto | Sorgenti | LilyPond (s) | Sintesi ed encoding (s) | Totale fasi eseguite (s) | PDF prodotti | MP3 prodotti |
|---|---:|---:|---:|---:|---:|---:|
| Pratica | 118 | 126.1 | 111.6 | 237.8 | 118 | 107 |
| Teoria | 139 | 166.6 | 25.4 | 192.0 | 139 | 120 |

Tutti i processi eseguiti sono terminati con codice zero. Strumenti: LilyPond 2.26.0, FluidSynth 2.6.1, LAME 4.0 (versioni riportate dai programmi). I tempi sono somme delle durate misurate per unità e non includono la successiva revisione o una build Sphinx.

## Limiti della prova

`pdfcrop` non è disponibile nei percorsi verificati né nel PATH. Non sono stati eseguiti ritaglio e conversione PDF→SVG: questa è una misura parziale, non il tempo della pipeline completa. Nessun confronto visivo o ascolto effettuato. Avvisi Fontconfig segnalano cache non scrivibili nell'ambiente di esecuzione: i tempi possono risentirne. Non si deduce equivalenza grafica dalla sola uscita zero.

Log per partitura e output temporanei restano in `/private/tmp/appunti-pipeline-benchmark/{pratica,teoria}`; questa posizione è temporanea, mentre i risultati numerici sono conservati nella KB. Il benchmark non ricopia asset pregressi: misura quanto viene prodotto dai sorgenti attuali.

## Valutazione

L'ordine di grandezza misurato non giustifica da solo l'introduzione immediata di una cache complessa. Prima completare il confronto grafico, stabilire l'ambiente dei font e misurare la fase SVG. La compilazione completa è praticabile come riferimento locale; la frequenza di rigenerazione e il tempo accettabile restano scelte operative.

## Evoluzione proposta, da verificare

Prima di installare ulteriori convertitori valutare l'SVG nativo di LilyPond, mantenendo una produzione PDF separata ove necessaria. La documentazione ufficiale descrive gli output alternativi: https://lilypond.org/doc/v2.26/Documentation/notation/alternative-output-formats . Verificare ritaglio, margini, font, multipagina e macro su campioni prima di eliminare `pdfcrop` e `pdf2svg`. Nessuna modifica alla pipeline è stata eseguita.
