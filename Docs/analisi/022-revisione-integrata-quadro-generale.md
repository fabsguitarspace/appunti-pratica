# Proposta di revisione integrata: Teoria, Pratica e Strumenti

Data: 14 novembre 2026. Documento di decisione editoriale, a seguito della lettura dei due volumi e della valutazione discussa con l’autore. Nessuna modifica ai contenuti pubblicati o al software in questa fase.

## 1. Decisione centrale

Conservare l’impianto dei due volumi, rendere esplicito il percorso di costruzione melodica e adeguare gli strumenti alle attività effettivamente proposte. Strutture melodiche e pentatoniche si inseriscono in questa revisione complessiva: non costituiscono due aggiunte indipendenti né giustificano automaticamente due nuove applicazioni.

La catena da rendere riconoscibile è: **materiale → organizzazione delle note → frase ritmica → contesto armonico → variazione personale**. Il lettore deve poterla percorrere anche con pochissimo materiale e senza studiare preventivamente ogni catalogo.

Giudizio editoriale: **8/10 per la coerenza complessiva dei due volumi**. La distinzione fra spiegazione delle relazioni e lavoro sulla chitarra funziona; le applicazioni musicali sono numerose. Rimangono dispersione dei procedimenti melodici, alcune definizioni eccessivamente assolute e una gerarchia non sempre evidente fra materiale essenziale e approfondimento.

Per gli strumenti, il precedente **7/10 sulla copertura didattica era riferito allo stato senza Progressioni**. La sua implementazione migliora concretamente la copertura di forma, accompagnamento e bersagli. Non assegno un nuovo voto alla qualità dell’applicazione senza una prova d’uso: la verifica di questa sessione riguarda sorgenti e documentazione, non l’esperienza audio e interattiva completa. Non è dimostrabile che siano gli strumenti “migliori” in assoluto; sono pertinenti agli Appunti, con lacune specifiche correggibili.

## 2. Base della valutazione e aggiornamenti

La lettura testuale ha compreso i capitoli di Teoria e Pratica, il glossario e i dieci percorsi d’autore. Non comprende una verifica integrale degli spartiti resi, delle diteggiature e degli audio. Gli audit precedenti sono materiale di confronto, non una fotografia automaticamente valida del presente.

Snapshot dei repository al consolidamento: Teoria `a420e05`, Pratica `9c83ab7`, Strumenti `3a1ba8d`; nessuna modifica locale segnalata nei tre repository. Il documento resta nella cartella di coordinamento esterna ai repository.

**Correzione rispetto alla prima proposta in conversazione:** Progressioni è implementato. Il README descrive quattordici griglie, accompagnamento, basso, note guida e modalità “suona tu”; l’ADR 0013 riporta i passi 4.0–4.4 implementati e l’accettazione dopo la prova dell’utente ancora da completare. Non va riproposto come sviluppo da iniziare.

Il `PIANO_MIGLIORAMENTO.md`, aggiornato il 14 novembre, conserva decisioni e interventi già eseguiti. Questa proposta lo integra per l’architettura melodica e gli strumenti, senza riaprire automaticamente interventi chiusi. In particolare: ordine dei capitoli di Teoria intenzionale, pagina “Come leggere gli esempi” già presente, interventi sulla chord-scale già effettuati, Repertorio fuori ambito.

## 3. Cosa esiste già e cosa manca davvero

| Area | Presenza nei volumi | Decisione |
|---|---|---|
| Ascolto, canto, ritmo e pause | Basi di Pratica; esercizi applicativi; percorsi d’autore | Conservare e usare come criteri di riuscita, evitando nuove prefazioni ripetitive |
| Scale e arpeggi trasformati in frasi | Pratica 4, “Dal pattern a una frase”; Pratica 5, “Dall’arpeggio alla frase” | Collegare a una sede comune per i procedimenti, mantenendo gli esercizi locali |
| Bersagli e collegamenti | Pratica 7; licks su progressioni; Christian, Hall e Martino | Rendere esplicito il rapporto fra struttura scelta e nota d’arrivo |
| Sviluppo motivico | Teoria 12; Pratica 9; Hall, Metheny, Scofield e McLaughlin | Riutilizzare questi esempi come applicazioni, non riscriverli in un percorso parallelo |
| Pentatoniche | Teoria 4 e 10; Pratica 4 e studi 05–06 di Pratica 9 | Sistemazione delle famiglie e dei procedimenti, non introduzione da zero |
| Accompagnamento e canto superiore | Pratica 6; Hall, Pass e Wes | Integrare la scelta della nota al canto negli strumenti per gli accordi |
| Forma e pratica contestuale | Pratica 7, brano guida AABA e studi conclusivi | Sfruttare Progressioni come ambiente comune di applicazione |

La lacuna principale è una **classificazione riconoscibile e riutilizzabile delle strutture e delle trasformazioni**. Non manca il fraseggio; manca una sede che ne renda leggibili i procedimenti trasversali.

## 4. Strutture melodiche: collocazione e perimetro

In Pratica, introdurre una pagina autonoma “Strutture melodiche e costruzione della frase”, nell’indice dopo Arpeggi. Conservare gli indirizzi dei capitoli esistenti: la posizione nell’indice non richiede di rinominare tutti i file. La pagina rappresenta un ingresso al lavoro melodico, non un prerequisito obbligatorio per leggere Accordi.

Contenuto proposto:

1. Definizione della struttura come materiale selezionato e identificato tramite intervalli.
2. Classificazione delle famiglie, con formule esplicite e criterio di inclusione.
3. Distinzione fra formula, ordine delle note, registro e ritmo.
4. Due o tre organizzazioni esemplificative prima delle tavole di consultazione.
5. Applicazione su un accordo e collegamento a una nota d’arrivo sul successivo.
6. Frase breve, pausa, risposta e variante personale sopra una griglia già disponibile.

In Teoria inserire soltanto il supporto concettuale necessario, raccordando Intervalli, Scale, Accordi e “Ritmo e sviluppo del materiale”. La descrizione operativa estesa appartiene a Pratica.

La classificazione precisa richiesta dall’autore **non è ancora verificata sulle pagine dei due volumi di riferimento**. Prima di redigere il catalogo occorrono gli estratti pertinenti o un accesso verificabile alle sezioni: indici e presentazioni editoriali non bastano. Non attribuire a quella classificazione formule ricostruite a memoria. Usare testo ed esempi originali e una presentazione autonoma, senza impostare i capitoli come esposizione di un metodo nominato.

Conservare la cellula Mi–Sol–Si–Re già impiegata: su Cmaj7 vale 3–5–7–9. È un utile raccordo, ma non deve essere confusa con una struttura 1–2–3–5. Il criterio comune è la relazione intervallare, non l’identità di tutte le cellule.

## 5. Pentatoniche: classificare senza duplicare

| Sede | Responsabilità |
|---|---|
| Teoria, Scale | Formule, intervalli, relazioni fra collezioni e differenze fra famiglie |
| Pratica, Scale | Visualizzazione e percorsi sulla tastiera, collegati alle mappe esistenti |
| Nuova pagina melodica | Ordini, salti, registri, ritmo e costruzione di frasi |
| Modern jazz e fusion | Sovrapposizioni, spostamenti e rientri, sviluppando gli studi già presenti |

La maggiore e la minore pentatonica senza semitoni non rappresentano le proprietà di ogni collezione pentatonica. Evitare che “pentatonica” diventi sinonimo universale di materiale senza attriti. Ogni applicazione deve indicare il basso o accordo reale e i gradi prodotti.

Separare tre riferimenti: grado rispetto alla fondamentale della struttura; grado rispetto all’accordo; posizione della nota nella collezione. Un salto di due posizioni in una pentatonica non è automaticamente una terza diatonica. Questa distinzione deve essere condivisa da testo, esempi e generatore.

Il catalogo può essere preciso senza imporre lo studio di tutte le combinazioni. Presentare pochi ingressi musicalmente utili e lasciare le tabelle complete alla consultazione.

## 6. Decisioni sugli strumenti

| Strumento | Conservare | Intervento motivato |
|---|---|---|
| Scale | Catalogo, ritmi, accenti, vincoli di zona, link agli esercizi | Integrare pentatoniche, blues e bebop già trattati nei volumi; verificare nomi degli intervalli e percorsi per cardinalità diverse; offrire ingressi per obiettivo |
| Arpeggi | Partenze da note diverse, organizzazioni, ritmi e posizioni | Collegare gli esercizi ai bersagli e alle applicazioni su Progressioni; non duplicare funzioni esistenti |
| Accordi | Shell, drop, triadi e conduzione delle voci | Aggiungere vincolo o filtro della nota al canto, con esempi coerenti con Pratica 6 |
| Progressioni | Implementazione corrente di griglie, forma, basso, accompagnamento e note guida | Verificare l’esperienza d’uso e collegare le attività melodiche al contesto; non rifare l’applicazione |
| Strutture melodiche | Nessuna nuova pagina software decisa in anticipo | Definire prima il modello editoriale; solo dopo scegliere modalità condivisa o strumento autonomo |

Le 33 scale attuali non comprendono le pentatoniche, blues e bebop: c’è un disallineamento concreto rispetto ai volumi. Aggiungerle non significa applicare indiscriminatamente la visualizzazione a tre note per corda: serve verificare che i percorsi risultino leggibili e utili per ciascun materiale.

Il generatore distingue già cosa, come e dove suonare. Non serve riscoprire il ritmo: serve collegare questi controlli a compiti musicali riconoscibili. Analogamente, le partenze dalla terza o settima degli arpeggi sono già disponibili.

Una sequenza che scorre sui gradi di una scala e una struttura selezionata che conserva la propria identità sono operazioni diverse. Un eventuale modello comune deve distinguere materiale, trasformazione, applicazione armonica e diteggiatura. Non basta aggiungere una sequenza numerica ai preset esistenti.

## 7. Correzioni concettuali preliminari

Prima di estendere la classificazione, correggere localmente i passaggi che renderebbero ambigue le nuove spiegazioni.

- **Teoria 8, dopo l’armonizzazione della scala sesta diminuita:** la simmetria dell’accordo diminuito viene usata per sostenere che “la scala ha pochissime trasposizioni davvero diverse”. Il passaggio confonde l’accordo diminuito con la collezione appena descritta. Do–Re–Mi–Fa–Sol–La♭–La–Si ha dodici trasposizioni distinte come insieme di classi di altezza; l’accordo °7 ne ha tre. Correggere questo nesso senza riscrivere l’impianto del capitolo.
- **Stabilità e tensione:** rivedere gli assoluti sugli intervalli e sulla dominante alla luce dei contesti blues e modali già trattati. Descrivere la tendenza nello specifico contesto, senza aggiungere avvertenze ripetitive in ogni pagina.
- **Aree funzionali:** distinguere la descrizione semplificata delle funzioni dalla presenza effettiva delle note nelle triadi e nelle settime. Evitare criteri che producano contraddizioni fra gli esempi elencati.
- **Pentatoniche:** circoscrivere le proprietà delle famiglie senza semitoni quando si ampliano i tipi trattati.

Queste correzioni hanno precedenza sulla nuova pagina: una tassonomia più ricca deve poggiare su definizioni coerenti. Non sono una richiesta di uniformare la voce personale dell’autore.

## 8. Ordine di lavoro e criteri di completamento

| Fase | Risultato concreto | Verifica |
|---|---|---|
| A — Fondamenti | Proposte puntuali di correzione dei passaggi sopra indicati | Confronto prima/dopo, formule e controesempi verificabili |
| B — Classificazione | Tabella delle famiglie e delle trasformazioni, verificata sul riferimento richiesto | Nessuna confusione fra gradi, indici della collezione, registro e applicazione |
| C — Integrazione editoriale | Nuova sede melodica, raccordi e riuso degli esempi esistenti | Ogni aggiunta copre una funzione non già spiegata altrove; accesso essenziale distinto dalla consultazione |
| D — Strumenti | Estensioni mirate a Scale e Accordi; collegamenti con Progressioni | Corrispondenza fra formule, testo, note generate, nomi e diteggiature |
| E — Verifica completa | Build e controllo di esempi, collegamenti e interazione | Build HTML con avvisi come errori, test pertinenti e controllo visivo/audio dei materiali modificati |

La pagina “Da dove comincio” già prevista da INT-10 resta utile: deve orientare fra obiettivi, non imporre la lettura lineare di tutti i capitoli. Può introdurre tre ingressi essenziali: costruire una frase, accompagnare una progressione, sostenere una melodia con gli accordi.

Prima di modificare i progetti leggere le rispettive `Docs`. Per i contenuti generati intervenire negli script o nei dati autorevoli: `generate_artist_paths.py` per i percorsi d’autore e `generate_bebop_licks.py` per il catalogo dei licks. Conservare URL, etichette e link pubblicati; verificare la rigenerazione prima di applicare modifiche.

**Prossima attività concreta:** preparare i testi prima/dopo della fase A e lo schema editoriale della nuova pagina. La verifica della classificazione specifica della fase B resta un requisito aperto prima della stesura del catalogo. Non occorre attendere quel materiale per lavorare sulle correzioni certe.
