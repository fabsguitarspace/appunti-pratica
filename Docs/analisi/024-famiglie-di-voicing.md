# Analisi — Famiglie di voicing: copertura coerente nel capitolo Accordi e nello strumento

- Data: 2026-11-19
- Stato: decisa con l'utente il 2026-11-19 (alternativa D e quattro decisioni sotto); attuata in
  tre fasi il 2026-11-19 (vedi «Attuazione»)
- Ambito e richiesta: l'utente chiede che nella sezione Accordi di Appunti di Pratica e nello
  strumento Accordi di appunti-strumenti «siano trattate in modo coerente tutte queste forme»:
  shell, drop 2, drop 3, drop 2&4, voicing senza fondamentale, voicing per quarte, strutture
  superiori, triadi strette e late, cluster. Ha scelto di avere prima l'analisi e un ADR, poi
  l'attuazione a fasi. Lo strumento è trattato in
  [ADR 0015 di appunti-strumenti](../../../appunti-strumenti/Docs/ADR-0015-famiglie-di-voicing.md).
  Repertorio è fuori dal perimetro.

## Problema e risultato atteso

Il capitolo 6 tratta bene tre famiglie (shell, drop 2, drop 3), ma le altre sono assenti, sparse
in altri capitoli o presenti di fatto senza un nome. Lo strumento genera soltanto shell, drop 2,
drop 3 e triadi strette. Il lettore non trova un quadro d'insieme e, passando dal volume allo
strumento, incontra famiglie e nomi diversi.

Risultato atteso:

1. ogni famiglia ha nel capitolo 6 **una sola sezione di riferimento**, con definizione,
   costruzione, insiemi di corde, uso musicale ed esempi con diagramma, pentagramma, TAB e audio;
2. una **mappa delle famiglie** all'inizio del capitolo collega sezioni, capitoli d'applicazione
   (7, 9, chord melody) e famiglia dello strumento;
3. **un solo nome** per famiglia, uguale nel volume, nel glossario di Teoria e nelle etichette
   dello strumento;
4. le stesse convenzioni (niente corde a vuoto, nessuna tensione al basso, cinque tasti) in volume
   e strumento, con le eccezioni dichiarate nei due posti.

## Evidenze

### Copertura attuale

| Famiglia | Capitolo 6 (`src/docs/6-accordi.rst`) | Altrove nel volume | Strumento (`js/voicings.js`) |
|---|---|---|---|
| Shell | sezione `shell-voicings` (r. 109–300): 6–4–3 e 5–4–3, bassi di tonica, terza, quinta | cap. 7, studi II–V–I | `shell`, stesse cinque disposizioni |
| Drop 2 | solo dentro «Voicing per il chord melody» (r. 1245), corde 4–3–2–1, definito come strumento per la melodia | cap. 11, esercizi 5, 6, 9 | `drop2` su 4321 e 5432 |
| Drop 3 | solo nel chord melody (r. 1323), fondamentale al basso | cap. 11, esercizio 7 | `drop3` su 6432 e 5321 |
| Drop 2&4 | assente; l'analisi 018 lo elenca fra gli ampliamenti possibili | — | assente |
| Senza fondamentale | di fatto: shell con basso di quinta (r. 191–205), semidiminuito essenziale (r. 76), tre voci del chord melody; manca una sezione con il nome | cap. 7 r. 129 (G7♭9 con Si al basso) | di fatto: negli accordi di nona i drop usano 3 5 7 9 (ADR 0012, punto 1), senza dirlo all'utente |
| Per quarte | assente | cap. 9, studio 03 «Quarte sopra il pedale» | assente |
| Strutture superiori | un cenno nel Vocabolario avanzato (r. 505) | cap. 9, studio 04 «Una triade come struttura superiore» | assente |
| Triadi strette | assenti come voicing d'accompagnamento | cap. 3, triadi come arpeggi sulla tastiera | `triad` su 321, 432, 543, 654 |
| Triadi late | assenti come voicing | cap. 3 r. 757, «Triadi a parti late maggiori» (come arpeggi) | assenti |
| Cluster | assente | — | assente |

### Terminologia osservata

- «parti strette / parti late» (Pratica cap. 3, Teoria cap. 5) contro «posizione stretta» (ADR
  0012) e «Triadi strette» (etichetta dello strumento); Teoria usa anche «posizione chiusa».
- «note guida» (Pratica cap. 6, glossario di Teoria) con «guide tones» come sinonimo: coerente.
- «strutture superiori» (Teoria cap. 5 e 10, Pratica cap. 9): coerente, ma solo in italiano.
- «quartali» (Teoria cap. 5) contro «quarte» (Pratica cap. 9): da uniformare.
- «senza fondamentale» (Pratica e Teoria): coerente; *rootless* non compare.
- Il glossario di Teoria (`appunti-teoria/src/docs/glossario.rst`) definisce drop 2, note guida e
  shell voicing; mancano drop 3, drop 2&4, senza fondamentale, per quarte, struttura superiore,
  cluster.

### Vincoli dello strumento (da ADR 0012)

- Le qualità (`js/chords.js`, 19) arrivano alla nona: niente 11, 13, né tensioni alterate.
  Strutture superiori, voicing per quarte e senza fondamentale con la tredicesima richiedono
  quindi un insieme di **tensioni disponibili** per qualità (decisione dell'ADR 0015).
- Una nota per corda, al massimo cinque tasti, niente corde a vuoto: i cluster si possono generare
  solo con le seconde fra corde vicine. Sulla chitarra la seconda è comoda fra 3ª e 2ª corda
  (terza maggiore fra le corde vuote), stretta altrove.

### Inferenze

- Il drop 2 nasce nel volume come tecnica di chord melody e lo strumento lo usa come voicing
  d'accompagnamento (II–V–I, ciclo): definizione e uso andrebbero separati.
- Le convenzioni del capitolo (nota al canto, niente corde a vuoto, niente tensione al basso) sono
  compatibili con tutte le famiglie nuove, tranne le pile di quarte che partono da una tensione
  (es. Re–Sol–Do–Fa su Cm7): l'ADR 0015 le esclude dal capitolo 6 e dallo strumento. *Correzione
  del 2026-11-19 (fase 3):* una versione precedente citava come esempio lo studio 03 del cap. 9,
  ma lì il basso della chitarra è sempre Re, la fondamentale.

## Dipendenze e impatto

- `src/docs/6-accordi.rst`: nuove sezioni e mappa. Le etichette `shell-voicings` e
  `chord-melody-voicings` restano invariate (rimandi dai capitoli 7, 9, 11 e da «Da dove comincio»).
- `src/docs/9-modern-jazz-fusion.rst`: studi 03 e 04 rimandano alle nuove sezioni come
  applicazione, senza duplicarle.
- `src/docs/3-conoscere-la-tastiera.rst`: le triadi late restano arpeggi; il capitolo 6 rimanda
  al capitolo 3 per la costruzione e ne aggiunge l'uso come voicing.
- `src/docs/11-strumenti-per-la-pratica.rst`: elenco delle famiglie ed esercizi pronti per quelle
  nuove; `tests/test_strumenti_links.py` deve accettare i nuovi valori di `fam` e `set`.
- LilyPond: nuovi esempi generati da uno script (sul modello di `generate_shell_voicings.py` e
  `generate_chord_melody.py`), con test Python sul modello di `test_chord_melody.py`. Pipeline
  esistente: `build-lilypond.sh --source …`, audio 60 BPM con `Jazzernaut.sf2`.
- Teoria: voci nuove nel glossario e uniformazione «quartali» / «per quarte». Teoria è nel
  perimetro della revisione editoriale.
- appunti-strumenti: ADR 0015, `voicings.js`, `chords.js` (tensioni), `chordpractice.js`
  (etichette), `Docs/deep-link.md`, test.

## Alternative e criteri di confronto

Criteri: un solo punto di riferimento per famiglia, progressione didattica, costo (esempi da
generare e verificare), stabilità dei rimandi esistenti.

### A. Stato attuale

Nessun costo, ma la richiesta resta disattesa: sei famiglie mancano o sono senza nome, e volume e
strumento divergono.

### B. Solo una mappa, senza nuove sezioni

Una tabella all'inizio del capitolo che rimanda ai capitoli esistenti. Costo basso, ma drop 2&4,
senza fondamentale e cluster restano senza trattazione e le quarte e le strutture superiori senza
definizione (il cap. 9 le applica senza costruirle).

### C. Mappa e nuove sezioni nel capitolo 6, chord melody invariato

Aggiunge le famiglie mancanti dove servono, ma drop 2 e drop 3 restano definiti dentro il chord
melody mentre le altre famiglie a quattro voci starebbero fuori: incoerente.

### D. Mappa, sezione unica per le famiglie a quattro voci, nuove sezioni (raccomandata)

Il capitolo diventa un percorso per famiglie, dalla più leggera alla più colorata:

| # | Sezione | Contenuto | Etichetta |
|---|---|---|---|
| 1 | Accordi essenziali | invariata | — |
| 2 | **Le famiglie di voicing** (nuova) | mappa: costruzione, corde, uso, sezione, famiglia dello strumento | `famiglie-voicing` |
| 3 | Shell voicings | invariata; la frase finale rimanda alla mappa | `shell-voicings` |
| 4 | **Triadi strette e late come voicing** (nuova) | triadi su terne vicine e late; sopra il basso d'insieme; rimando al cap. 3 | `voicing-triadi` |
| 5 | **Quattro voci: drop 2, drop 3, drop 2&4** (nuova) | costruzione da posizione stretta; drop 2 su 4321, 5432, 6543; drop 3 su 6432, 5321; drop 2&4 su 6532, 5421; rivolti, II–V–I d'accompagnamento | `voicing-drop` |
| 6 | **Senza fondamentale** (nuova) | note guida + due colori (5, 9, 13); tipo con la terza e tipo con la settima al basso; perché con il bassista; legame con shell con basso di quinta e con i diminuiti | `voicing-senza-fondamentale` |
| 7 | Vocabolario avanzato | invariato; la frase introduttiva lo colloca nella mappa | — |
| 8 | **Strutture superiori** (nuova) | nota guida al basso + triade sopra (4321, 5432); tabella triadi → tensioni per maj7, m7, 7 naturale e alterato | `strutture-superiori` |
| 9 | **Voicing per quarte** (nuova) | tre e quattro quarte su corde vicine (stesso tasto tranne fra 3ª e 2ª); voicing «So What»; uso modale; rimando al cap. 9 studio 03 | `voicing-quarte` |
| 10 | **Cluster** (nuova) | seconde fra 3ª e 2ª corda; 6/9, m11, maj9 con seconda; quando usarli | `voicing-cluster` |
| 11 | Voicing per il chord melody | definizioni di drop 2 e drop 3 sostituite da un rimando alla sezione 5; restano gli esempi melodici | `chord-melody-voicings` |
| 12 | Percorsi d'autore | invariata | — |

Costo stimato: circa 14 esempi nuovi (2 triadi, 4 drop, 2 senza fondamentale, 2 strutture
superiori, 2 quarte, 2 cluster), generati da `scripts/generate_voicing_families.py` con test.
Nessuna etichetta esistente cambia.

### E. Capitolo nuovo «Famiglie di voicing» separato dal 6

Più pulito sulla carta, ma sposta shell e chord melody, rompe i rimandi e allunga il percorso.
Scartata.

## Raccomandazione

**Alternativa D**, in tre fasi, con lo strumento allineato secondo l'ADR 0015.

### Nomi unici (da applicare a volume, glossario e strumento)

| Famiglia | Nome nel testo | Sinonimo citato una volta | Id strumento |
|---|---|---|---|
| Shell | shell voicing | — | `shell` |
| Triadi strette | triadi strette | parti strette, posizione chiusa, *close* | `triad` |
| Triadi late | triadi late | parti late, *spread*, *open* | `spread` |
| Drop 2 | drop 2 | — | `drop2` |
| Drop 3 | drop 3 | — | `drop3` |
| Drop 2&4 | drop 2 e 4 | *drop 2&4* | `drop24` |
| Senza fondamentale | voicing senza fondamentale | *rootless* | `rootless` |
| Strutture superiori | strutture superiori | *upper structure* | `ust` |
| Per quarte | voicing per quarte | quartali | `quartal` |
| Cluster | cluster | voicing a grappolo | `cluster` |

«Parti strette / late» resta solo nel capitolo 3, dove descrive arpeggi; Teoria adotta «triadi
strette / late» con lo stesso sinonimo.

### Convenzioni comuni

- niente corde a vuoto; cinque tasti; una nota per corda;
- nessuna tensione al basso, senza eccezioni (ADR 0015, punto 4): una pila di quarte che parte
  da una tensione non entra nel capitolo 6 né nello strumento;
- nei voicing senza fondamentale e nelle strutture superiori il basso è una nota guida (terza o
  settima) oppure la quinta;
- sigle: stessa grafia del capitolo (Δ7, m7♭5, 7(♭9)).

### Decisioni dell'utente (2026-11-19)

1. **Drop 2 e drop 3**: le definizioni si spostano nella sezione 5 «Quattro voci: drop 2, drop 3,
   drop 2 e 4»; il chord melody conserva gli esempi melodici e rimanda lì, senza duplicati.
2. **Strutture superiori dei dominanti**: tensioni naturali e alterate già nella prima stesura
   della sezione 8 (II maggiore; VI, ♭VI e ♭V maggiore). Nello strumento le alterate restano
   dietro l'opzione «Tensioni alterate» (ADR 0015, punto 3).
3. **Cluster**: niente corde a vuoto, nessun riquadro d'ascolto con corde a vuoto; seconde fra
   3ª e 2ª corda, forme trasportabili.
4. **Termini**: nome italiano nel testo e nelle etichette dello strumento; il termine inglese tra
   parentesi alla prima occorrenza nel capitolo e nel glossario di Teoria, come nella tabella dei
   nomi.

## Piano di verifica ed eventuale attuazione

Ogni fase si attua solo dopo l'approvazione dell'utente.

**Fase 1 — struttura e famiglie a quattro voci.** Mappa (sezione 2), sezione 5 (drop) e
alleggerimento del chord melody; esempi drop 2 su 5432 e 6543, drop 2&4. Lo strumento aggiunge
`drop24` e il set 6543 di `drop2` nella stessa fase.

**Fase 2 — senza fondamentale e triadi.** Sezioni 4 e 6; strumento: `rootless`, `spread`.

**Fase 3 — colori.** Sezioni 8 (con tensioni naturali e alterate), 9, 10 (senza corde a vuoto); strumento: tensioni per qualità, `ust`, `quartal`,
`cluster`. Glossario di Teoria e rimandi dal cap. 9.

Criteri di accettazione:

- ogni famiglia della tabella dei nomi ha una sezione nel capitolo 6 e una riga nella mappa che
  indica la famiglia dello strumento;
- `tests/test_voicing_families.py`: struttura di ogni famiglia (posizione dell'ottava abbassata
  nei drop, assenza della fondamentale nei senza fondamentale, quarte giuste o eccedenti
  dichiarate nei voicing per quarte, almeno una seconda nei cluster), corde distinte, tasti 1–17,
  apertura ≤ 4, nessuna tensione al basso salvo le eccezioni dichiarate;
- test di coerenza volume/strumento: per ogni esempio del capitolo esiste lo stesso voicing (corde
  e tasti) fra quelli generati da `voicings.js` per la stessa famiglia;
- `tests/test_strumenti_links.py` passa con i nuovi valori di `fam`;
- build HTML con `-W` senza avvisi; spartiti controllati a campione; l'audio è sintetizzato e va
  ascoltato dall'utente.

Rischi:

- lunghezza del capitolo 6, già di circa 1.400 righe: tenere gli esempi nuovi a due per famiglia
  e lasciare le varianti allo strumento;
- divergenza fra esempi scritti e voicing generati: mitigata dal test di coerenza;
- le tensioni per qualità e le strutture superiori alterate estendono ADR 0012: l'ADR 0015 va
  approvato prima della fase 3.

## Attuazione

### Fase 1 (2026-11-19)

- `src/docs/6-accordi.rst`: nuova sezione «Le famiglie di voicing» (`famiglie-voicing`) dopo gli
  accordi essenziali, con la mappa delle famiglie già trattate nel volume; le righe per triadi,
  strutture superiori e quarte rimandano per ora al cap. 3 e agli studi 03–04 del cap. 9, e le
  famiglie delle fasi 2–3 senza materiale (senza fondamentale, cluster) non compaiono ancora.
  Nuova sezione «Quattro voci: drop 2, drop 3, drop 2 e 4» (`voicing-drop`) prima del Vocabolario
  avanzato (nuova etichetta `vocabolario-avanzato`), con quattro esempi. Nel chord melody le
  definizioni di drop 2 e drop 3 sono sostituite da rimandi; nuova etichetta `drop3-chord-melody`.
- Esempi: `vf-confronto` (Cmaj7 come shell, drop 2, drop 3, drop 2 e 4 con il Do all'VIII tasto),
  `vf-drop2-gruppi` (corde 5–4–3–2 e 6–5–4–3), `vf-drop2-ii-v-i` (Dm7–G7–Cmaj7–C6 sulle corde
  5–4–3–2), `vf-drop24` (corde 6–5–3–2 e 5–4–2–1); 24 voicing generati da
  `scripts/generate_voicing_families.py`, che riusa grafia e partitura di
  `generate_chord_melody.py`.
- `tests/test_voicing_families.py` (6 test): suonabilità e grafia, note dell'accordo, struttura dei
  drop (voci abbassate contate dall'alto), fondamentale al basso, conduzione delle voci ≤ 1 tono,
  e **coerenza con lo strumento**: ogni esempio è fra i voicing di `js/voicings.js` (via Node).
- `src/docs/11-strumenti-per-la-pratica.rst`: cinque famiglie, due esercizi pronti nuovi (drop 2
  II–V–I sulle corde 5–4–3–2, che riproduce l'esempio del capitolo; drop 2 e 4 sulle corde 6–5–3–2).
- Teoria, `glossario.rst`: voci «Drop 3» e «Drop 2 e 4».
- Strumento: ADR 0015, fase 1.

Verifiche: build HTML con `-W` di Pratica e Teoria senza avvisi; tutti i test di `tests/`
superati (compreso `test_strumenti_links.py`: 57 link); spartiti controllati a campione. L'audio è
sintetizzato e non è stato verificato all'ascolto.

### Fase 2 (2026-11-19)

- `src/docs/6-accordi.rst`: nuove sezioni «Triadi strette e late» (`voicing-triadi`, fra shell e
  drop) e «Voicing senza fondamentale» (`voicing-senza-fondamentale`, fra drop e Vocabolario
  avanzato); nella mappa la riga delle triadi rimanda alla nuova sezione e si aggiunge la riga dei
  senza fondamentale.
- Esempi: `vf-triadi-strette` (Do maggiore su 3–2–1, Do minore su 4–3–2), `vf-triadi-late` (Do
  maggiore su 6–4–3 e 4–2–1; contiene il Do–Sol–Mi del cap. 3), `vf-triadi-ii-v-i` (Dm–G–C su
  3–2–1), `vf-senza-fondamentale` (terza al basso su 5–4–3–2, settima al basso su 4–3–2–1, per
  maj7, 7, m7, m7♭5), `vf-senza-fondamentale-ii-v-i` (le due forme alternate); 32 voicing in più,
  56 in tutto.
- Note dei senza fondamentale, uguali nel generatore (`ROOTLESS`) e nello strumento: maj7 3 5 7 9,
  6 3 5 6 9, m7 ♭3 5 ♭7 9, 7 3 13 ♭7 9, m7♭5 ♭3 ♭5 ♭7 9. Sul semidiminuito la nona naturale e non
  l'undicesima, che non permette la forma con la settima al basso entro cinque tasti (ADR 0015,
  punto 10).
- `tests/test_voicing_families.py`: 8 test; nuovi controlli su triadi (tre rivolti per gruppo di
  corde, apertura stretta o lata), senza fondamentale (niente fondamentale, terza presente, nota
  guida al basso, alternanza 3–7–3 / 7–3–7 nel II–V–I) e conduzione delle voci.
- Capitolo 11: sette famiglie, due esercizi pronti nuovi (triadi late su 6–4–3; II–V–I senza
  fondamentale su 4–3–2–1, che riproduce la prima forma dell'esempio).
- Teoria: glossario («Senza fondamentale», «Triadi strette e late»); in `5-accordi.rst` il titolo
  «Triadi a parti late» diventa «Triadi late», con «a parti late» citato come sinonimo.

Verifiche: come nella fase 1 (build `-W` di Pratica e Teoria, tutti i test di Pratica e dello
strumento). L'audio è sintetizzato e non è stato verificato all'ascolto.

### Fase 3 (2026-11-19)

- `src/docs/6-accordi.rst`: sezioni «Strutture superiori» (`strutture-superiori`), «Voicing per
  quarte» (`voicing-quarte`) e «Cluster» (`voicing-cluster`) fra Vocabolario avanzato e chord
  melody; nella mappa tre righe al posto di quella che rimandava al cap. 9. Il capitolo 6 ha ora
  una sezione per ogni famiglia della tabella dei nomi.
- Esempi: `vf-strutture-superiori` (Cmaj9, Cmaj7(♯11), Cm11, C13(♯11)),
  `vf-strutture-superiori-alterate` (C13(♭9), C7(♯9♭13), C7(♭9♯11) → Fmaj9), `vf-quarte` (Cm11
  «So What» e a quattro voci, Cmaj13, C13 a tre voci), `vf-quarte-modale` (Dm11–Em11 in Re
  dorico), `vf-cluster` (Cmaj9, C6/9, C13, Cm11); 76 voicing in tutto. Le tensioni si scrivono
  secondo il grado, come nello strumento (♯9 = Re♯ su Do).
- Il semidiminuito non ha strutture superiori (ADR 0015, punto 11): il testo lo dice.
- `tests/test_voicing_families.py`: 11 test; nuovi controlli su strutture superiori (nota guida al
  basso, triade maggiore stretta, risoluzione per semitono), quarte (intervalli esatti, basso nota
  dell'accordo) e cluster (seconda, terza presente, niente corde a vuoto); il confronto con lo
  strumento usa anche le alterate.
- Capitolo 9: rimandi dagli studi 03 e 04 alle nuove sezioni. Capitolo 11: dieci famiglie, opzione
  «Tensioni alterate», tre esercizi pronti nuovi.
- Teoria, glossario: «Cluster», «Struttura superiore», «Voicing per quarte».
- Correzione: l'analisi diceva che lo studio 03 del cap. 9 metteva l'undicesima al basso; il basso
  della chitarra lì è sempre Re (vedi «Inferenze»).

Verifiche: build HTML con `-W` di Pratica e Teoria; tutti i test di Pratica e dello strumento;
strumento provato nel browser (famiglie nuove, etichette delle tensioni, `alt=1` dal link,
nessun errore in console). L'audio è sintetizzato e non è stato verificato all'ascolto.
