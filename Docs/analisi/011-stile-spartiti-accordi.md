# Analisi — Uniformazione grafica degli spartiti del capitolo Accordi

- Data: 2026-11-10
- Stato: attuato.
- Richiesta: rifare solo lo stile degli spartiti di Accordi essenziali e degli Accordi maggiori nel Vocabolario avanzato, conservandone il contenuto. Successiva preferenza dell’utente: evitare nona, undicesima e tredicesima al basso nei nuovi voicing.

## Ambito grafico

Uniformati 17 sorgenti LilyPond: cinque raccolte di accordi essenziali e dodici raccolte dei maggiori (Do sulla seconda corda e Fa sulla prima). Titoli, larghezza di riga di 160 mm, dimensioni dei diagrammi, distanza dal pentagramma e raggruppamento pentagramma/TAB riprendono lo stile dei nuovi minori/dominanti. Gli esempi più numerosi sono disposti su due sistemi; il diagramma compare una sola volta, sopra il pentagramma. Visualizzati tempo di 60 BPM e metro 4/4 già presenti nei dati musicali.

## Conservazione del contenuto

Confronto prima/dopo dei blocchi `music` e, dove presenti, `accordi`: identici. Confrontati in ordine tutti i comandi place-fret/open/mute dei diagrammi: identici. I MIDI generati dai sorgenti aggiornati sono semanticamente uguali a quelli originali per note, attacchi, durate, dinamiche e tempo.

Compilazione eseguita in una cartella temporanea con la pipeline esistente. Promossi soltanto PDF e SVG. I 34 file MIDI/MP3 dei 17 esempi preesistenti sono rimasti identici byte per byte, verificati mediante SHA-256. Non modificati testo, ordine delle forme, note o posizioni dei maggiori e degli essenziali. Nessuna modifica alla pipeline.

## Preferenza sul basso dei nuovi voicing

Applicata alla raccolta originale di minori/dominanti introdotta nella lavorazione precedente: basso su fondamentale, terza, quinta o settima. La nona aumentata non può diventare una terza minore al basso nelle dominanti; nei sus4 la quarta rimane nelle voci superiori. Esclusa dal basso anche la sesta dei minori sesta per mantenere il criterio operativo coerente. I maggiori e gli essenziali storici mantengono il contenuto, come richiesto per il lavoro grafico.

Sostituiti 17 voicing, conservando 38 gruppi e 114 forme. Nel gruppo con fondamentale al canto delle dominanti si confrontano ora due disposizioni di settima e una tredicesima. Aggiornati il generatore, le sigle nel testo e i materiali grafici/sonori delle forme cambiate. Aggiunto il test relativo al basso ai controlli già esistenti.

## Verifiche

- Controlli di identità musicale e degli hash dei 17 esempi storici.
- Ispezione visiva di tutti i 17 spartiti uniformati e dei gruppi minori/dominanti modificati.
- Cinque test musicali sul nuovo vocabolario, inclusa l’esclusione delle tensioni dal basso.
- Confronto dei 38 MIDI con le definizioni delle nuove forme; controllo MP3 per durata, decodifica, segnale presente e assenza di saturazione. Nessun ascolto umano certificato.
- Build HTML con avvisi trattati come errori; verifica dei riferimenti a immagini e audio.

Il cambiamento grafico non è una revisione teorica degli esempi storici. Non applicata una selezione diversa dei loro voicing né corretti eventuali contenuti preesistenti. Non modificato il progetto Teoria.
