# ADR 0006 — Piano elettrico al posto della chitarra negli esempi audio

- Stato: Accettato
- Data: 2026-11-24
- Decisore: utente responsabile dei progetti, nella conversazione di lavoro
- Ambito: progetti fratelli (appunti-teoria, appunti-pratica, appunti-repertorio) e libreria appunti-musica

## Contesto ed evidenze

Gli MP3 dei tre volumi si ottengono dai MIDI di LilyPond con FluidSynth. Accordi e linee usano il programma 0 («acoustic grand»), che il soundfont predefinito `Jazzernaut.sf2` suona come una chitarra campionata. Basso e batteria vengono dall'overlay `PracticeRhythm.sf2`, sintetizzato senza campioni di terzi. L'utente ha giudicato poco gradevole il suono della chitarra sintetizzata.

Il 24 novembre 2026 sono stati confrontati, sugli stessi MIDI di Repertorio e Pratica, la chitarra attuale e tre varianti di un piano elettrico tipo Rhodes sintetizzato in FM: morbido, brillante, con tremolo. Un soundfont Rhodes già presente sul computer (iReal Pro) è stato escluso perché contiene campioni commerciali non ridistribuibili.

## Opzioni considerate

| Opzione | Benefici | Costi e rischi |
|---|---|---|
| Mantenere la chitarra | Nessun lavoro | Suono giudicato poco gradevole |
| Soundfont di piano elettrico di terzi | Suono campionato realistico | Licenze da verificare; file grandi |
| **Piano elettrico originale sintetizzato (FM), variante morbida** | Nessun campione di terzi; generatore deterministico; il programma 0 resta invariato e i sorgenti `.ly` non cambiano | Suono meno realistico di un campionamento; tutti gli MP3 vanno ricompilati |

## Decisione

1. Il soundfont predefinito diventa `AppuntiEPiano.sf2`, generato da `appunti_musica/epiano_soundfont.py` nella libreria comune: preset 0, banco 0, un campione ogni sei semitoni da La1 a Do7, FM 1:1 con indice che cala dopo l'attacco, variante «morbido» scelta dall'utente.
2. `PracticeRhythm.sf2` resta l'overlay di basso e batteria.
3. I builder (`build.py` della libreria; `scripts/build_music.py` di Teoria e Pratica, finché non migrano alla libreria) cercano `sf/AppuntiEPiano.sf2` al posto di `sf/Jazzernaut.sf2`. Teoria e Pratica ne tengono una copia identica in `src/lilypond/sf/`.

## Conseguenze

- **Media.** Tutti gli MP3 dei tre volumi sono ricompilati; anche PDF e SVG vengono riscritti, perché il soundfont entra nell'impronta di ogni sorgente. Spartiti e MIDI non cambiano nel contenuto.
- **Editoriali.** Dove il testo parla del suono degli esempi come di una chitarra, va adeguato. Le note di rilascio di ogni volume annotano il cambio.
- **Reversibilità.** Ripristinare `Jazzernaut.sf2` dalla storia git, il suo nome nei builder e ricompilare riporta la chitarra. Il file, non più usato, è stato rimosso dalla libreria e dai volumi il 24 novembre 2026.
- **Fuori ambito.** appunti-strumenti ha un proprio motore audio nel browser e non cambia.

## Verifica

- Test della pipeline aggiornati e superati in tutti i progetti.
- Ascolto a campione degli MP3 ricompilati in ogni volume.

## Collegamenti

- [ADR 0004 — Libreria musicale comune ai tre progetti](0004-libreria-musicale-comune.md).
