# Analisi — Capitolo di strumenti interattivi (scale, arpeggi, accordi, progressioni)

- Data: 2026-11-12
- Stato: decisa — tutte le decisioni prese dall'utente il 2026-11-12; ADR 0005 e ADR 0010 di GSP Accettati; attuata per lo strumento Scale il 2026-11-12 e per lo strumento Arpeggi il 2026-11-14 (vedi Esito dell'attuazione). Decisioni: coerenza visiva D1; pubblicazione A1 (GitHub Pages); rinomina del repository in `appunti-strumenti`; capitolo «Strumenti per la pratica», ultimo nel volume; rimandi nei capitoli 4–7; ordine Arpeggi → Accordi → Progressioni; versione 1.1.
- Ambito e richiesta: appunti-pratica e appunti-strumenti, ex Guitar-Scale-Practice (`../../appunti-strumenti`; cartella spostata e rinominata il 2026-11-12). Richiesta dell'utente: «creare un capitolo dentro il progetto Pratica che riporti questo tool [Guitar Scale Practice] e altri simili applicati anche ad Arpeggi, Accordi, Progressioni».
- ADR collegato: [0005 — Strumenti interattivi nel volume](../adr/0005-strumenti-interattivi-nel-volume.md) (Accettato). Lato strumento: `appunti-strumenti/Docs/ADR-0010-suite-di-strumenti.md` (Accettato) e `Docs/plans/0002-suite-pratica.md` (Approvato).

## Problema e risultato atteso

Il volume offre esempi fissi (spartito, TAB, MP3 a due velocità). Guitar Scale Practice (GSP) offre invece pratica generativa: scala e tonica casuali, esercizi combinabili Cosa × Come × Dove, audio sintetizzato, tablatura, metronomo e trainer di velocità. Risultato atteso: un capitolo del volume da cui aprire quattro strumenti — Scale (esistente), Arpeggi, Accordi, Progressioni — collegati ai capitoli 4–7, senza degradare la build Sphinx, il PDF e l'ePub.

## Evidenze

Fatti osservati:

- Pratica: Sphinx 8.2.3 + Shibuya, solo `.rst` (`src/docs/conf.py`), build `-W --keep-going`, RTD con PDF ed ePub (`.readthedocs.yaml`). Il volume usa già `raw:: html` per audio e per `<iframe>` YouTube (`3-conoscere-la-tastiera.rst:51`). Nessun `html_extra_path`, nessun sottomodulo. Versione 1.0 dall'11 novembre 2026.
- Capitoli coinvolti e sezioni «Esercizi»: `4-scale.rst` (otto sonorità, Esercizi di base/avanzati, Trasportare), `5-arpeggi.rst` (a 4 note, estesi, m6/9, Esercizi), `6-accordi.rst` (essenziali, shell, vocabolario con nota al canto, chord melody: drop 2, drop 3, tre voci), `7-progressioni.rst` (II–V–I maggiore e minore, turnaround, dominanti secondarie, tritono, blues, blues minore, vamp modale, AABA, rhythm changes, basi).
- GSP (`fabsguitarspace/Guitar-Scale-Practice`, ora `appunti-strumenti`, titolo «Strumenti per la pratica»): pagina statica senza build né dipendenze, funziona da `file://` (ADR 0001), script classici con namespace globali (ADR 0002), moduli puri testati in Node, ~3 450 righe. Persistenza `localStorage` con chiavi `interval-master:v1` e `gsp:practice:v1`.
- Moduli GSP riusabili senza modifiche: `exercises/rhythm.js` (celle, swing, accenti), `exercises/melodic.js` (motivi su indici di un insieme di altezze), `exercises/fingering.js` (Viterbi corda/tasto), `audio/*` (Karplus-Strong, scheduler lookahead, smorzamento per corda), `tab/*`, `fretboard.js`.
- Accoppiamenti alla scala: `theory.js` (catalogo delle 33 scale), `guitar.js` (diteggiature 3NPS), `app.js` (estrazione e rendering di una scala), `practice.js` (pannello e trasporto nello stesso modulo).
- Gli eventi sono monofonici: `{i, beat, dur, string, fret, accent, rest}` (ADR 0009 di GSP). Il motore audio smorza per corda, quindi suona già note simultanee su corde diverse.

Inferenze:

- Arpeggi: un arpeggio è un insieme di gradi come una scala; pool, melodia, ritmo e posizioni si riusano. Mancano il catalogo delle qualità e una diteggiatura diversa dal 3NPS (posizione di cinque tasti, una-due note per corda).
- Accordi e Progressioni richiedono eventi polifonici (più corde nello stesso evento) in tablatura, tastiera e scheduler, più tre moduli nuovi: voicing, conduzione delle voci, griglie armoniche.
- Il volume e gli strumenti hanno nomenclature compatibili (drop 2/3, shell, nota al canto, II–V–I): i cataloghi degli strumenti possono ricalcare le sezioni del volume.

Informazioni mancanti: comportamento di GSP dentro un `<iframe>` su iOS (sblocco audio, wake lock, scorciatoie); se RTD clona i sottomoduli con l'account attuale; nome e posizione desiderati del capitolo.

## Dipendenze e impatto

- **Editoriale**: un capitolo nuovo (`11-…rst` o una cartella `strumenti/` con una pagina per strumento) e un rimando breve in fondo alle sezioni Esercizi dei capitoli 4–7. Nessuna modifica agli esempi LilyPond, agli MP3 o alla pipeline musicale (ADR 0001, 0004 invariati).
- **Build**: dipende da dove si pubblicano gli strumenti (alternative sotto). PDF/ePub non possono eseguire JavaScript: serve un testo alternativo con indirizzo e una figura.
- **GSP**: da app per le scale a suite di quattro strumenti con un nucleo comune; nuove regole sulle chiavi `localStorage` (un'origine condivisa con il volume) e sui deep link.
- **Progetti fratelli**: Teoria e Repertorio non sono toccati; in futuro potrebbero rimandare agli stessi strumenti (es. Repertorio → Progressioni con la griglia di un brano). Da non anticipare.

## Alternative e criteri di confronto

### A. Dove vivono gli strumenti

| Opzione | Vantaggi | Costi e rischi |
|---|---|---|
| A0. Stato attuale: GSP separato, nessun capitolo | nessun lavoro | gli strumenti non fanno parte del percorso |
| A1. GSP su GitHub Pages, il volume rimanda con link | due cicli di vita indipendenti; aggiornare uno strumento non richiede ricostruire il volume | due domini; i deep link del volume possono rompersi con le versioni nuove; serve attivare Pages |
| **A2. GSP come sottomodulo di Pratica, copiato nell'output Sphinx (`out/strumenti/`)** | stesso dominio RTD; versione bloccata e coerente con il testo (stesso schema dell'ADR 0004); funziona anche nell'`out/` locale | RTD deve clonare il sottomodulo; aggiornare richiede bump del sottomodulo e nuova build; prima dipendenza esterna della build RTD |
| A3. Riscrivere gli strumenti dentro `_static` del volume | un solo repository | duplica GSP, perde test e autonomia; respinta |

### B. Come si presentano nel capitolo

| Opzione | Vantaggi | Costi e rischi |
|---|---|---|
| **B1. Scheda per strumento con figura, pulsante «Apri» a schermo intero e deep link agli esercizi del volume** | l'app resta mobile-first a pagina intera (drawer, scorciatoie, wake lock); semplice in PDF/ePub | si esce dalla pagina del volume |
| B2. `<iframe>` incorporato | pratica senza lasciare la pagina | layout a cassetti compresso, scorciatoie in conflitto, audio/wake lock da verificare su iOS, altezza da gestire; inutile su mobile |
| B3. B1 ora, B2 in seguito con una vista ridotta (`#embed=1`) | rimanda il rischio | lavoro aggiuntivo in GSP |

### C. Forma del capitolo

| Opzione | Vantaggi | Rischi |
|---|---|---|
| C1. Solo un capitolo finale «Strumenti per la pratica» | consultabile in un punto; nessun impatto sui capitoli esistenti | strumenti scollegati dagli esercizi |
| **C2. Capitolo finale + rimando di una riga in fondo agli Esercizi dei capitoli 4–7** | collega materiale fisso e pratica generativa; compatibile con entrambe le strutture ancora aperte nell'analisi 003 | quattro piccole modifiche a capitoli pubblicati |
| C3. Strumenti distribuiti dentro i capitoli, senza capitolo dedicato | massima contestualità | nessun punto d'ingresso; anticipa la scelta strutturale dell'analisi 003 |

Criteri: coerenza didattica, resa su mobile, PDF/ePub, manutenzione, stabilità dei link, costo.

### D. Coerenza visiva

Fatti osservati (2026-11-12):

| Aspetto | Volume (Shibuya 2026.1.9) | GSP (`css/style.css`) |
|---|---|---|
| Carattere | `system-ui` / `ui-monospace` | `system-ui` / `ui-monospace` — già coerente |
| Neutri | grigi Radix freddi (`--gray-1` #fcfcfc, testo #202020) | crema caldo (`--bg` #f6f4ef, `--line` #d9d4ca) |
| Accento | `accent_color: "red"` (Radix red-9 #e5484d) | arancio #e8821e (tonica), blu #3f7fd8 (note) |
| Rosso già usato | link, accento | `--danger` #c4372b, `--playing` #ff6b6f (nota in riproduzione) |
| Tema chiaro/scuro | classe `html.dark`/`html.light`, scelta salvata in `localStorage._theme` (light/dark/auto) | `prefers-color-scheme` + `data-theme` su `:root` |
| Testata | logo del volume, barra con i tre progetti | titolo e link al canale, nessun ritorno al volume |

Senza interventi lo strumento apparirebbe come un sito diverso. Poiché GSP definisce già tutti i colori come token CSS e supporta `data-theme`, l'allineamento è un lavoro di soli token e testata, senza toccare il layout.

| Opzione | Vantaggi | Rischi |
|---|---|---|
| D0. Lasciare il tema di GSP | nessun lavoro | stacco visivo netto entrando dallo strumento |
| **D1. Tema «Appunti» come predefinito di GSP**: neutri e accento del volume, tonica sull'accento, nota in riproduzione su un colore distinto dal rosso | stessa identità ovunque, anche fuori dal volume; un solo tema da mantenere | l'accento rosso va separato da `--danger` e `--playing`; contrasti da riverificare sulla tastiera |
| D2. Due temi, scelti dall'hook di copia (file `css/skin.css` sostituito) | GSP standalone conserva il suo aspetto | due temi da testare; l'output dipende dalla build |

Comuni a D1/D2: sincronizzare chiaro/scuro leggendo `localStorage._theme` (stessa origine RTD) e applicandolo come `data-theme`, con fallback a `prefers-color-scheme` da `file://`; testata con logo del volume e link «← Appunti di Pratica» verso la pagina del capitolo. È un accoppiamento leggero con un dettaglio interno di Shibuya: va isolato in una funzione e coperto da una prova manuale a ogni aggiornamento del tema.

## Raccomandazione

**A2 + B1 (con B3 come evoluzione) + C2 + D1.**

1. GSP diventa una suite multipagina: `index.html` (scelta dello strumento), `scale.html`, `arpeggi.html`, `accordi.html`, `progressioni.html`, con nucleo comune. Dettaglio nel piano 0002 di GSP.
2. Pratica lo include come sottomodulo in `tools/guitar-practice/`, bloccato a un commit; un hook `build-finished` in `conf.py` copia solo i file pubblicabili (`*.html`, `css/`, `js/`) in `out/strumenti/`. `.readthedocs.yaml` dichiara il sottomodulo (`submodules: include: [tools/guitar-practice]`). Se il sottomodulo manca (clone senza `--recurse-submodules`), l'hook scrive un messaggio informativo e non un avviso, perché con `-W` gli avvisi bloccano la build; il resto del volume si costruisce comunque.
3. Nuovo capitolo, titolo di lavoro **«Strumenti per la pratica»**, ultimo nel toctree (dopo Percorsi d'autore), una pagina per strumento:
   - cosa allena e quando usarlo nel percorso (rimando al capitolo corrispondente);
   - figura (schermata) e pulsante «Apri lo strumento»;
   - 4–8 «esercizi pronti»: deep link che aprono lo strumento già configurato, ricalcati sulle sezioni del volume (es. «Scala dorica, terze, ottavi swing, posizione di 5 tasti»; «Drop 2 su 4–3–2–1, nota al canto fissa»; «Blues jazz in Fa, 120 BPM, note guida»);
   - nota d'uso: cuffie, modalità silenziosa iOS, Spazio/Invio.
   - PDF/ePub: `.. only:: html` attorno ai pulsanti e un'alternativa testuale con l'indirizzo per gli altri formati (verificare i tag del builder ePub, che è HTML).
4. Rimando di una riga in fondo agli Esercizi dei capitoli 4–7 (C2).
4bis. Tema «Appunti» come predefinito di GSP (D1), chiaro/scuro sincronizzato con il volume, testata con ritorno al capitolo.
5. Pubblicazione per fasi: il capitolo esce subito con il solo strumento Scale, poi si aggiunge una pagina per ogni strumento completato. Versione 1.1 alla prima uscita (decisione dell'utente).

Limiti: gli strumenti generano materiale non rivisto esempio per esempio; il capitolo deve dichiararlo e indicare criteri di ascolto. La correttezza musicale dei cataloghi (simboli, voicing, griglie) va verificata con test e revisione come per i generatori Python.

## Decisioni da prendere

1. ~~Pubblicazione: A2 o A1?~~ **Deciso dall'utente il 2026-11-12: A1, GitHub Pages**, per aggiornare gli strumenti indipendentemente dal volume. Conseguenza accettata: chiaro/scuro non sincronizzato automaticamente (mitigazione con parametro `theme` nei link, ADR 0005 punto 7). La raccomandazione A2 qui sopra resta come traccia del confronto.
2. ~~Titolo e posizione del capitolo?~~ **Deciso dall'utente il 2026-11-12: «Strumenti per la pratica», ultimo capitolo** (`11-strumenti-per-la-pratica.rst`, dopo Percorsi d'autore; nome del file indicativo).
3. ~~Rimandi nei capitoli 4–7?~~ **Deciso dall'utente il 2026-11-12: sì (C2)**, una riga in fondo alla sezione Esercizi di Scale, Arpeggi, Accordi e Progressioni, verso la pagina dello strumento nel capitolo «Strumenti per la pratica». Ogni rimando si aggiunge quando lo strumento corrispondente è pubblicato.
4. ~~Rinominare il repository GSP?~~ **Deciso dall'utente il 2026-11-12: rinomina** (non un repository nuovo) di `fabsguitarspace/Guitar-Scale-Practice` in **`fabsguitarspace/appunti-strumenti`**, da eseguire prima di attivare Pages. Indirizzo pubblico: `https://fabsguitarspace.github.io/appunti-strumenti/`. Motivi: conserva storia, ADR, issue e stelle; GitHub reindirizza web e git dal vecchio nome; l'URL Pages non sarebbe reindirizzato, ma non esiste ancora. Il nome colloca lo strumento nella famiglia degli appunti (`appunti-musica`, `appunti-pratica`, …), coerente con il tema D1.
5. ~~Ordine degli strumenti nuovi?~~ **Deciso dall'utente il 2026-11-12: Arpeggi → Accordi → Progressioni**; versione del volume 1.1 alla prima uscita del capitolo.
6. ~~Tema: D1 o D2?~~ **Deciso dall'utente il 2026-11-12: D1**, GSP adotta l'aspetto del volume ovunque, anche fuori dal volume. Nota: gli altri due volumi hanno accenti propri: se un giorno vi si rimanderà, l'accento può diventare un token scelto dalla pagina di provenienza.

## Piano di verifica ed eventuale attuazione

Nessuna implementazione implicita. Dopo le decisioni:

1. GSP fase 0 (suite e deep link, vedi piano 0002) con test verdi.
2. Pratica: sottomodulo, hook di copia, capitolo con lo strumento Scale. Verifiche: `./build.sh` pulito con `-W`; `out/strumenti/scale.html` apribile da `out/` e da `file://`; deep link funzionanti; build PDF/ePub locale o su RTD senza riferimenti rotti; prova su iPhone (audio, wake lock) dal dominio RTD.
3. Per ogni strumento nuovo: pagina del capitolo, esercizi pronti, rimando nel capitolo corrispondente, bump del sottomodulo, aggiornamento di questa KB.

Rischi: dipendenza della build RTD da un secondo repository; deriva tra testo del volume e versione dello strumento (mitigata dal commit bloccato e da deep link versionati `v=1`); `localStorage` condiviso sull'origine RTD (mitigato da chiavi con prefisso per strumento).

## Esito dell'attuazione (Scale, 2026-11-12)

- `src/docs/11-strumenti-per-la-pratica.rst`, ultimo nel toctree: introduzione, «Prima di iniziare» (audio e modalità silenziosa iOS, scorciatoie, tema, avvertenza sul materiale generato), sezione **Scale** con pulsante «Apri lo strumento» e otto esercizi pronti ricalcati su `4-scale.rst` (Do maggiore intorno al VII tasto a 72/60 BPM; Re dorico swing sulle corde 5 e 4; Do minore melodica in terze fino al XII tasto).
- Rimando di una riga in fondo agli Esercizi di `4-scale.rst` (riferimento `strumenti-scale`).
- `conf.py`: `release = "1.1"`, `strumenti_url`, `extlinks` con il ruolo `:strumento:`, `html_js_files` con `strumenti.js` (attributo `data-base`).
- Pulsante in `custom.css` con rosso fisso `#ce2c31` (5,2:1 con il bianco): il colore dei link di Shibuya in tema chiaro dà 4,4:1, sotto AA.
- Verifiche: build HTML pulita con `-W`; LaTeX e ePub senza avvisi nuovi, con l'indirizzo testuale nei formati non HTML; i dieci link si aprono in una nuova scheda con `theme` aggiornato anche cambiando tema; gli otto esercizi aperti sul sito pubblicato si configurano come atteso, senza errori; nessuno scorrimento orizzontale a 375 px. `tests/test_strumenti_links.py` controlla pagine, `v=1`, scala, tonica, esercizio, ritmo, BPM e che ogni parametro sia riconosciuto da `js/link.js`.
- Scostamenti dall'ADR 0005, punto 3: **una sezione per strumento nella pagina del capitolo** invece di pagine separate (con un solo strumento una sottopagina sarebbe vuota di contesto; si potrà dividere quando gli strumenti saranno quattro) e **nessuna schermata** per ora.
- Durante la verifica un esercizio previsto (Re dorico sulle corde 6 e 5 fino al XII tasto) generava solo nove note, perché in quell'ambito le due corde coprono da Re a La: sostituito con le corde 5 e 4. Gli esercizi pronti vanno ascoltati nello strumento, non solo decodificati.
- Da fare: prova su iPhone e Android dal volume pubblicato (audio, modalità silenziosa, wake lock).

## Esito dell'attuazione (Arpeggi, 2026-11-14)

- Strumento: `arpeggi.html` pubblicato su GitHub Pages (commit `64b749e` di appunti-strumenti; ADR 0011 di quel repository): 19 sonorità (4 triadi e le 15 del capitolo 5), diteggiature in posizione, esercizi propri, partenza da 3ª/5ª/7ª, parametri `chord` e `start` nei deep link.
- `src/docs/11-strumenti-per-la-pratica.rst`: sezione **Arpeggi** (riferimento `strumenti-arpeggi`) con pulsante e nove esercizi pronti ricalcati sugli studi di `5-arpeggi.rst` (Cmaj7 dall'VIII tasto in quarti; partenza dalla terza; confronto C6/C7/Cmaj7; Cm6; ordine 1–5–3–7 dello studio 5; Cmaj9; C7♯5 e C°7; Dm7♭5 sulle corde 5–4–3; Si♭7 swing). «Prima di iniziare»: Invio estrae anche un altro arpeggio.
- Rimando di una riga in fondo a «Una sessione breve» di `5-arpeggi.rst`.
- `tests/test_strumenti_links.py`: `arpeggi.html` tra le pagine; per gli arpeggi controlla sonorità, fondamentale, esercizio e ritmo nel catalogo `Presets.ARPEGGI`, andata e ritorno di ogni parametro con `js/link.js`; `start` ammesso solo negli arpeggi e non con `ext=full` o `scope=chain`. Verificato anche con link volutamente errati.
- Verifiche: ogni esercizio generato in Node con la pipeline dello strumento prima di scriverlo (nessun errore, nessuna estensione troncata: un primo Dm7♭5 sulle corde 4–3–2 e poi 5–4–3 su due ottave lo era, ridotto a un'ottava sulle corde 5–4–3); build HTML pulita con `-W`; i 12 test del volume verdi con `.venv`; nella pagina compilata 13 link verso gli strumenti con `theme` e nuova scheda; un esercizio aperto sul sito pubblicato si configura come atteso senza errori.
- Da fare: come per Scale, prova su iPhone e Android; LaTeX ed ePub non ricompilati (la sezione usa lo stesso schema `only:: html` / indirizzo testuale della sezione Scale).
