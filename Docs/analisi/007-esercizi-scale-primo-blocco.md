# Scale: ampliamento del primo blocco di esercizi

Data: 2026-11-08. Stesura autorizzata dall’utente dopo il confronto sul perimetro.

Modificata soltanto la sezione Esercizi di `src/docs/4-scale.rst`: schede con scopo, procedura, ascolto, varianti e verifica per i quattro esempi esistenti; aggiunti terze diatoniche, variazioni ritmiche e costruzione di una frase. Chiariti il superamento della tonica prima dell’inversione nei primi due esempi, l’adattamento a scale di sei/otto suoni, la forma della minore melodica usata nell’esercitazione e una routine breve.

Nuovi sorgenti diretti LilyPond: `scale-esercizio05.ly`, `06` e `07`, ciascuno in 4/4 a 72 BPM, con PDF/SVG/MIDI/MP3 omonimi. I quattro esempi precedenti sono conservati. Non modificato l’indice generale del percorso; restano aperte le due ipotesi di ristrutturazione.

Verifiche: conversione completa dei tre esempi; ispezione visiva dei PDF; build HTML pulita con avvisi trattati come errori, riuscita senza avvisi; presenza di tutti e sette i riferimenti grafici e audio nell’HTML; MP3 riconosciuti da ffprobe con durata positiva. Eliminata una selezione iniziale di timbro non disponibile nel soundfont: usato il programma predefinito coerente con i vecchi esempi. I log continuano a contenere gli avvisi ambientali Fontconfig e quello sul preset percussion channel 9, non usato dalle parti melodiche. Nessun ascolto diretto certificato; revisione musicale all’ascolto da completare.

Possibili estensioni successive, non ancora sviluppate: gruppi di tre, direzioni alternate, quarte/seste, continuità fra posizioni e ulteriori famiglie di varianti. Nessuna necessità di generare subito tutte le combinazioni.
