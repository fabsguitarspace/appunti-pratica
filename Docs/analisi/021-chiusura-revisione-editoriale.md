# Analisi — Chiusura dei punti della revisione editoriale

- Data: 2026-11-13
- Stato: implementato su richiesta dell'utente («fai tutto»).
- Ambito e richiesta: completare i punti rimasti aperti della revisione editoriale dell'11 novembre 2026. La parte di Teoria è in `../appunti-teoria/Docs/analisi/012-chiusura-revisione-editoriale.md`.

## Interventi in Pratica

| Punto della revisione | Intervento |
|---|---|
| Testi duplicati nel vocabolario | In Accordi, i commenti della prima corda per minori (8 gruppi) e dominanti (11 gruppi) sono riscritti con dettagli propri delle forme in Fa (corde, bassi, dita), verificati sul catalogo di `generate_chord_vocabulary.py`. Nessun paragrafo lungo del capitolo è più ripetuto. |
| Bebop minore senza mappa | `scala-bebop-minore-verticale-c1` (dorica con settima maggiore) e `scala-bebop-dorica-verticale-c1` (dorica con terza maggiore), sei posizioni distinte ciascuna. |
| Esercizi solo in Do | Sottosezione `esercizi-fuori-da-do` con lo studio `scale-trasposte-01` (gruppi di quattro in Fa e in Sol, stessa posizione), generato da `generate_advanced_scales.py` (lista `TRANSPOSED`; aggiunto il parametro `spell` per scrivere Fa♯ invece di Sol♭). |
| Glossario | Collegamento al glossario comune di Teoria dall'introduzione. |
| Brano guida | Etichetta `progressioni-aaba` sullo studio AABA del capitolo 7, dichiarato brano guida; riquadri «Brano guida» nei capitoli Scale, Arpeggi, Accordi e Licks con un compito sulla stessa forma. |
| Cellula guida | Paragrafo nell'introduzione che presenta la cellula Mi–Sol–Si–Re e il brano guida. |
| Capitolo 2 troppo lungo | Riquadro «Come è organizzato il capitolo» e tre etichette (`basi-strumento`, `basi-musica`, `basi-tecnica`) che dividono il capitolo in strumento, principi musicali e tecnica, senza cambiare URL né livelli dei titoli. |

## Verifica

Build HTML con `-W` riuscita; `tests/test_materiali_aggiunti.py` esteso (mappe del bebop minore, studio trasposto: note nella tonalità, grafia Fa♯, file e riferimenti); suite completa 38 test OK. Spartiti controllati visivamente; audio sintetizzato non certificato da ascolto umano.
