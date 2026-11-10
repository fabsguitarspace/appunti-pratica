# Analisi — Shell voicings

- Data: 2026-11-10
- Stato: corretto secondo la definizione esplicita dell’utente.

## Perimetro vincolante

Gli shell del progetto hanno esattamente tre note e soltanto i gruppi di corde 6–4–3 o 5–4–3. Non usare 4–3–2, 6–3–2 o altre combinazioni nella sezione Shell voicings. Il basso può essere tonica, terza o quinta; nel semidiminuito la quinta è diminuita. Le voci superiori restano sulle corde quarta e terza.

La prima versione aveva interpretato erroneamente «corde centrali» includendo 4–3–2. Rimossi i tre esempi relativi e corretti i bassi di quinta sulla sesta corda e il confronto del semidiminuito. Il generatore rifiuta ora direttamente tutte le altre combinazioni; il test copre anche i casi vietati.

## Contenuto attuale

Sette esempi con diagrammi, spartito, TAB e audio: forme base su quinta/sesta corda, terza al basso sulla quinta, quinta al basso su quinta/sesta, seste e settima maggiore nel minore, II–V–I maggiore/minore, confronto m7/semidiminuito. Con la quinta al basso le forme a tre note conservano terza e settima e omettono la fondamentale, come dichiarato nel testo.

Fonte di approfondimento: Tom Lippincott, https://tomlippincott.com/shell-voicings. Il perimetro delle corde è una scelta esplicita dell’utente e prevale su definizioni più generali.

## Produzione e verifica

`scripts/generate_shell_voicings.py` genera i sette sorgenti shell-* elencati in SHEETS. Rigenerare con Python, poi compilare i nomi base tramite build-lilypond.sh --source. Spartito, diagrammi, TAB e MIDI condividono corde e tasti. Audio a 60 BPM, quattro impulsi iniziali, una sola parte sonora.

Quattro test controllano tre voci, bassi ammessi, le sole due combinazioni di corde, note guida e semidiminuito. Verificati graficamente gli esempi corretti e confrontati MIDI e definizioni musicali; build HTML con avvisi trattati come errori. L’audio è sintetizzato e non è stato certificato da ascolto umano.
