# Analisi — Voicing per il chord melody

- Data: 2026-11-11
- Stato: implementato su richiesta dell'utente («migliorare o ampliare la scelta dei voicing nella sezione accordi, privilegiando quelli più usati ed efficaci negli arrangiamenti chord melody»).

## Problema

Il capitolo Accordi conteneva forme essenziali, shell a tre voci e un vocabolario per nota al canto generato automaticamente, ma nessuna sezione sulle famiglie di voicing usate davvero per arrangiare una melodia per chitarra sola: drop 2 sulle corde alte, drop 3 con basso, tre voci basso–guida–melodia, diminuiti di passaggio e scala di sesta diminuita, né un esempio di arrangiamento completo.

## Contenuto aggiunto

Nuova sezione `Voicing per il chord melody` (`chord-melody-voicings`) in `src/docs/6-accordi.rst`, prima di «Percorsi d’autore». Undici esempi, 59 voicing, con diagrammi, pentagramma, TAB e audio:

| Sorgente | Contenuto |
|---|---|
| `cm-drop2-maj7`, `-6`, `-7`, `-m7`, `-m7b5` | Drop 2 su 4–3–2–1, quattro note al canto per qualità |
| `cm-drop2-ii-v-i` | Dm7–G7–Cmaj7–C6, melodia Do–Si–Si–La, voci interne ≤ 1 tono |
| `cm-drop3` | Drop 3 con fondamentale al basso: C su 6–4–3–2, F su 5–3–2–1 |
| `cm-tre-voci` | Basso, nota guida e melodia (stile Joe Pass) |
| `cm-diminuiti-passaggio` | C6–C♯°7–Dm7–D♯°7–Em7 con nota comune al canto |
| `cm-sesta-diminuita` | Scala di sesta diminuita (Barry Harris) armonizzata in drop 2 |
| `cm-arrangiamento` | Otto battute originali che combinano le tecniche |

Il testo segue la convenzione del capitolo (nota al canto, niente corde a vuoto, tensioni non al basso) e rimanda agli shell, al percorso Joe Pass e al capitolo Armonia diminuita di Teoria.

## Produzione e verifica

`scripts/generate_chord_melody.py` calcola drop 2 e drop 3 dalla nota al canto e dai gradi dell'accordo; le forme a tre voci e l'arrangiamento sono scritti come corde/tasti espliciti. La grafia delle note deriva dal grado (es. C♭ in Fm7(♭5), Si♭ in C♯°7). Rigenerare con Python, poi compilare con `build-lilypond.sh --source cm-…`.

`tests/test_chord_melody.py` (8 test) verifica: grafia coerente con l'altezza, corde distinte e voci ordinate, tasti 1–17 e apertura ≤ 4 negli accordi, toni dell'accordo e basso non di tensione, struttura drop 2/drop 3, quattro note al canto distinte per qualità, condotta delle voci ≤ 2 semitoni, alternanza C6/B°7, melodia e durata dell'arrangiamento. Build HTML con `-W` riuscita; suite completa: 30 test OK. Spartiti controllati visivamente a campione; l'audio è sintetizzato e non è stato certificato da ascolto umano.

## Punti aperti

- L'arrangiamento usa salti di corda (6–5–1, 6–4–3–1): il testo indica hybrid picking o dita; valutare con l'utente se aggiungere diteggiature della mano destra.
- Possibili ampliamenti: drop 2 sulle corde 5–4–3–2, drop 2+4, voicing con corde a vuoto nelle tonalità di chitarra (E, A, D, G), un secondo arrangiamento su forma AABA.
