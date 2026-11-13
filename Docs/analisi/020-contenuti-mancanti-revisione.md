# Analisi — Contenuti mancanti segnalati dalla revisione editoriale

- Data: 2026-11-13
- Stato: implementato su richiesta dell'utente (scelta «Contenuti mancanti» dopo la verifica della revisione editoriale dell'11 novembre 2026).
- Ambito e richiesta: completare le lacune di contenuto di Pratica segnalate dalla revisione: pentatonica, scala blues e scale bebop (capitolo 4), arpeggio m7♭5 (capitolo 5), famiglia maggiore del vocabolario accordi sulla prima corda (capitolo 6).

## Problema e risultato atteso

- Il capitolo Scale presentava otto scale ma non la pentatonica né la scala blues, che Progressioni e Licks davano per note (blues di base, M08, B01), né le scale bebop, centrali per il capitolo Licks (D03).
- Le mappe degli arpeggi a quattro note non comprendevano il m7♭5, usato nell'esercizio 10 (II–V–I minore).
- Nel vocabolario avanzato la famiglia maggiore sulla prima corda si fermava alla quinta: mancavano i gruppi 13 e Δ7, presenti invece sulla seconda corda.

## Contenuto aggiunto

| Capitolo | Sezione / etichetta | Sorgenti LilyPond |
|---|---|---|
| 4-scale | «Pentatoniche, scala blues e scale bebop» (`scale-derivate`), con `scala-pentatonica-maggiore`, `scala-pentatonica-minore`, `scala-blues`, `scale-bebop` | `scala-pentatonica-maggiore-verticale-c1`, `scala-pentatonica-minore-verticale-c1`, `scala-blues-verticale-c1`, `scala-bebop-dominante-verticale-c1`, `scala-bebop-maggiore-verticale-c1` |
| 5-arpeggi | «m7♭5 (ø)» (`arpeggio-m7b5`), fra mΔ e 7♯5 | `arpeggio-cm7f5-1`, `arpeggio-cm7f5-2` |
| 6-accordi | «13 sulla 1ª corda» e «Δ7 sulla 1ª corda» nella famiglia maggiore | `accordi-f-maggiore-13-1` (5 voicing), `accordi-f-maggiore-maj7-1` (4 voicing) |

Le mappe di scala seguono il formato `…-verticale-c1` già usato: un Do di partenza, una riga per posizione impostata con `TabStaff.minimumFret`. Con cinque o sei note per ottava alcune partenze producevano la stessa diteggiatura: pentatonica minore e blues mostrano quattro posizioni, la pentatonica maggiore sei. Le scale bebop sono scritte in ottavi, in salita e discesa dal Do, per rendere udibile la proprietà che le definisce (note dell'accordo sui movimenti). Il bebop minore è descritto nelle due varianti (dorica con settima maggiore, dorica con terza maggiore) senza mappa, da costruire con il metodo del capitolo.

I voicing maggiori sono scritti a mano come gli altri file della famiglia maggiore (titolo, diagrammi, music), ma in `\absolute` con il numero di corda esplicito. Restano entro quattro tasti, senza corde a vuoto e con la nota al canto sulla prima corda. Il testo usa lo schema dei minori e dominanti («Nota al canto», «Voicing da sinistra»).

Collegamenti aggiornati: introduzione del capitolo 4 (rimando a `scale-derivate`), introduzione degli arpeggi a quattro note, rimando della pentatonica in `7-progressioni.rst` (ora verso le nuove sezioni di Pratica invece che verso Teoria).

## Verifica

- `build-lilypond.sh --source …` per i nove sorgenti; spartiti e TAB controllati visivamente sui PDF renderizzati.
- `build.sh` (Sphinx HTML con `-W`): riuscita, nessun avviso.
- Nuovo `tests/test_materiali_aggiunti.py` (4 test): note in salita di ogni scala e arpeggio, posizioni distinte, voicing maggiori (nota al canto, ordine delle voci, apertura ≤ 4 tasti, note di Fa maggiore con terza), presenza di SVG/PDF/MP3 e riferimento nei documenti.
- Suite completa con `unittest discover`: tutti i test OK. L'audio è sintetizzato e non è stato certificato da ascolto umano.

## Seconda fase (13 novembre 2026)

Su richiesta dell'utente sono stati chiusi i tre punti aperti della prima fase.

- **Commenti della famiglia maggiore.** I dodici gruppi preesistenti (sette sulla seconda corda, cinque sulla prima) hanno ora «Nota al canto», «Voicing da sinistra» e un commento. I nomi dei voicing sono stati ricavati dai diagrammi dei sorgenti, calcolando gli intervalli rispetto alla fondamentale. Due voicing del gruppo ♯11 sulla prima corda mettono la nona al basso, in deroga al criterio del capitolo: il testo li presenta come strutture superiori da usare sopra un basso di Fa.
- **Mappe dal Do superiore.** Aggiunte le versioni `-c2` delle cinque scale derivate (`scala-…-verticale-c2`). Pentatonica minore e blues mostrano cinque posizioni, perché due partenze duplicavano diteggiature già presenti.
- **Esercizi sulle scale derivate.** Nuova sottosezione `esercizi-scale-derivate` nel capitolo 4, dopo gli otto studi avanzati: `scale-derivate-01` (pentatonica minore e blues su C7) e `scale-derivate-02` (discesa bebop di dominante e maggiore), ciascuno a 60 e 90 BPM. Sono generati da `scripts/generate_advanced_scales.py` (lista `DERIVED`), che ora produce 20 sorgenti; gli otto studi preesistenti restano identici.

Verifica: build HTML con `-W` riuscita; `tests/test_materiali_aggiunti.py` esteso con le mappe `-c2` e con tre controlli sugli studi (note dell'accordo sui movimenti nelle discese bebop, note dello studio blues, sorgenti e audio presenti e richiamati); suite completa 37 test OK. Spartiti controllati visivamente; audio sintetizzato non certificato da ascolto umano.

## Punti aperti

- Gli esercizi del capitolo 4 restano in Do; il trasporto è lasciato allo studente come nelle altre sezioni.
- Il bebop minore è descritto senza mappa.
