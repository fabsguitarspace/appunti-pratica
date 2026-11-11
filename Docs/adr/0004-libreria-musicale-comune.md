# ADR 0004 — Libreria musicale comune ai tre progetti

- Stato: Accettato
- Data: 2026-11-11
- Decisore: utente responsabile dei progetti, nella conversazione di lavoro
- Ambito: appunti-repertorio, appunti-pratica, appunti-teoria
- Analisi collegata: [002 — Libreria musicale comune](https://github.com/fabsguitarspace/appunti-repertorio/blob/main/Docs/analisi/002-libreria-musicale-comune.md) (in locale: `appunti-repertorio/Docs/analisi/002-libreria-musicale-comune.md`)

## Contesto ed evidenze

Pratica e Teoria hanno copie separate e già divergenti di `build_music.py`, `my-scales.ly` e del soundfont. Repertorio richiederebbe una terza copia. L'ADR 0001 stabilisce LilyPond con generatori Python, ma non dice dove debbano risiedere gli strumenti comuni. I dettagli delle differenze sono nell'analisi 002.

Il numero 0004 è lo stesso in tutti e tre i repository, per riconoscere la decisione comune. In Pratica e Teoria i numeri 0002 e 0003 non sono usati: in Repertorio corrispondono a decisioni proprie di quel progetto.

## Opzioni considerate

Copie separate (stato attuale), sottomodulo git, pacchetto pip da tag git, subtree git. Il confronto è nell'analisi 002.

## Decisione

1. Gli strumenti musicali comuni vivono in un repository dedicato, [`fabsguitarspace/appunti-musica`](https://github.com/fabsguitarspace/appunti-musica), creato il 2026-11-11 e ancora vuoto.
2. La libreria comprende:
   - lo script di build (ricavato da quello di Pratica, sovrainsieme di quello di Teoria);
   - le macro LilyPond;
   - i soundfont;
   - i moduli Python condivisi dai generatori (voicing, basi, scrittura LilyPond e MIDI);
   - i test della pipeline.
3. **Tutti e tre i progetti** la usano come sottomodulo git in `tools/appunti-musica/`, bloccato a un commit preciso. Aggiornare la versione è un'operazione esplicita, seguita da una rigenerazione controllata.
4. Restano nei progetti i sorgenti `.ly`, i generatori dei contenuti e le risorse generate e versionate. Al posto dei link simbolici previsti all'inizio, la build passa a LilyPond la cartella delle macro della libreria con `-I` e cerca i soundfont prima nel progetto e poi nella libreria (aggiornamento del 2026-11-11, in fase di implementazione). I sorgenti esistenti restano invariati.
5. Read the Docs non dipende dalla libreria: la pipeline gira solo in locale.

## Conseguenze

- Migrazione in quest'ordine: creazione della libreria, Repertorio, Pratica, Teoria. Le copie si eliminano solo dopo il confronto degli output.
- Per Teoria la versione di `my-scales.ly` passa a quella di Pratica. In Teoria nessun sorgente include questa macro.
- Clonare un progetto richiede `git clone --recurse-submodules` oppure `git submodule update --init`. Va documentato nei README.
- Le correzioni alla pipeline si fanno una sola volta nella libreria, e ogni progetto le adotta aggiornando il proprio sottomodulo.
- Si estende l'ambito dell'ADR 0001 ad appunti-repertorio.
- Reversibile: si può tornare alle copie copiando i file dal commit bloccato.

## Verifica

Criteri dell'analisi 002:

- build musicale completa senza errori nei tre progetti;
- confronto degli output prima e dopo la migrazione di Pratica e Teoria;
- `pytest` e build HTML con `-W` puliti;
- build RTD non alterata.

## Collegamenti

- [ADR 0001 — LilyPond diretto e generazione Python](0001-lilypond-diretto-e-generazione-python.md): questa decisione ne organizza l'attuazione e non lo sostituisce.
- Copia identica di questo ADR in ciascuno dei tre progetti. Le modifiche vanno riportate in tutte le copie.
