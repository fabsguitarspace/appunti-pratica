# Analisi — Sezione dedicata agli shell voicings

- Data: 2026-11-10
- Stato: realizzata.
- Richiesta: aggiungere la sezione Shell voicings; sviluppare tre voci sulle corde centrali e varianti con nota su sesta/quinta corda; usare bassi di tonica, quinta o terza.

## Struttura e scelte

Sezione inserita tra Accordi essenziali e Vocabolario avanzato. Dieci esempi con diagrammi, pentagramma ottavizzato, TAB e audio a 60 BPM con quattro impulsi iniziali. Tutte le forme hanno esattamente tre note, su tre corde distinte e senza corde a vuoto.

- Corde quarta–terza–seconda con basso di tonica, terza e quinta: tre gruppi di Cmaj7, Cm7 e C7.
- Fondamentale sulla sesta e quinta corda: sei forme.
- Terza sulla quinta corda: tre forme in primo rivolto.
- Quinta sulla sesta e quinta corda: sei forme senza fondamentale.
- Confronto C6, Cm6 e Cm(maj7) sui due bassi di riferimento.
- Collegamenti II–V–I maggiore e minore.
- Confronto tra shell m7, riduzione m7♭5 senza quinta e riduzione semidiminuita senza fondamentale che conserva la quinta diminuita.

Con basso di tonica o terza le note sono fondamentale, terza e settima, oppure sesta al posto della settima per gli accordi di sesta. Con basso di quinta si omette la fondamentale per conservare terza e settima nelle tre voci. La sigla indica l’armonia di riferimento; le forme senza fondamentale sono dichiarate come tali. Per il semidiminuito la quinta al basso è diminuita, non un’estensione.

Non sviluppati esempi autonomi a due o quattro voci, seguendo la precisazione dell’utente. La versione iniziale con un esempio di sole note guida è stata sostituita prima della consegna finale. Il materiale storico dei maggiori e degli essenziali è conservato, tranne due paragrafi sui semidiminuiti che attribuivano scarsa importanza alla quinta alterata: corretti per coerenza con la nuova spiegazione. Aggiunto il rimando alla sezione dedicata dal primo richiamo agli shell.

## Fonti

Tom Lippincott, Shell Voicings: https://tomlippincott.com/shell-voicings — riferimento sul nucleo fondamentale/terza/settima, varianti con sesta e ruolo della quinta nelle qualità diminuite. Citato come approfondimento nel testo. Esempi e disposizione delle note della nuova sezione sono originali.

## Produzione

`scripts/generate_shell_voicings.py` definisce corde e tasti di ogni forma e genera i dieci sorgenti `shell-*.ly` elencati in `SHEETS`. Eseguire `python3 scripts/generate_shell_voicings.py`, poi `./build-lilypond.sh --source NOME` ripetuto per i dieci nomi base. Non modificare a mano i sorgenti generati.

Un’unica definizione musicale alimenta diagrammi, pentagramma, tablatura e MIDI. Il MIDI contiene una sola parte sonora, senza raddoppio della TAB. Prodotte quaranta risorse PDF/SVG/MIDI/MP3. Nessun nuovo link di download, nessuna modifica alla pipeline o a Teoria.

## Verifiche

- Ispezione visiva di tutti i dieci spartiti, ciascuno di una pagina.
- Quattro test in `tests/test_shell_voicings.py`: esattamente tre voci, bassi ammessi, intervalli e rivolti sulle corde centrali, note guida del II–V–I, distinzione del semidiminuito tramite la quinta.
- Confronto con mido dei dieci MIDI: tre note per accordo, altezze, attacchi, durate, conteggio e tempo coerenti; nessun raddoppio.
- MP3 controllati con ffprobe e decodifica PCM: durata coerente, segnale presente, nessun campione al limite di saturazione. Non effettuato ascolto umano dei dieci audio.
- Build HTML con avvisi trattati come errori e verifica dei riferimenti immagine/audio e dell’ancora `shell-voicings`.

Le forme in primo rivolto con terza sulla quinta corda sono più aperte: il testo propone la disposizione sulle corde centrali come alternativa quando risultano scomode.
