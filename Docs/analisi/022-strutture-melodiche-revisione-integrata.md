# Analisi — Correzioni concettuali e sezione sulle strutture melodiche

- Data: 14 novembre 2026.
- Stato: fase A approvata e applicata ai sorgenti di Teoria il 14 novembre 2026; pagina melodica scritta il 14 novembre 2026 senza la sezione Famiglie, per decisione dell’autore; classificazione da verificare. Completamento della fase A sul minore (M1–M7) approvato e applicato a Teoria il 14 novembre 2026. Fase B: classificazione da Bergonzi, voll. 1–2, e ripartizione Teoria/Pratica approvate; testi di Teoria (BT1–BT4) applicati il 14 novembre 2026; Pratica attuata lo stesso giorno (sezione Famiglie e pagina Pentatoniche).
- Ambito: Teoria e Pratica, con ricadute future sugli Strumenti.
- Riferimento: [Proposta di revisione integrata](022-revisione-integrata-quadro-generale.md).
- Sorgenti verificati: Teoria `a420e05`, Pratica `9c83ab7`.

## Problema e risultato atteso

Rendere coerenti le definizioni di materiale, tensione e funzione prima di ampliare la classificazione delle strutture melodiche e delle pentatoniche. Il lavoro richiesto in questa fase produce testi prima/dopo e un progetto di pagina concreto. I blocchi “Dopo” sono redazione originale pronta per il confronto con l’autore.

## Evidenze e correzioni proposte

Le righe qui indicate sono quelle verificate durante la stesura; i testi citati identificano i passaggi anche dopo futuri spostamenti. Le sostituzioni possono essere valutate singolarmente. Per il gruppo A4, l’applicazione è coordinata: non lasciare affermazioni generali incompatibili nei paragrafi successivi.

### A1 — Simmetria: accordo e scala sono oggetti diversi

Fonte: `appunti-teoria/src/docs/8-armonia-diminuita.rst:189`.

Correzione certa: la simmetria di un sottoinsieme non si trasferisce alla sua unione con C6. Il testo proposto non aggiunge una digressione sulle trasposizioni limitate.

**Prima**

```rst
Un accordo °7 è simmetrico (è fatto di terze minori sovrapposte). Per questo:

D°7 = F°7 = A♭°7 = B°7 (stesso insieme di suoni, cambia solo quale nota consideri “radice”).

Questa simmetria spiega due cose importanti:

* la scala ha pochissime “trasposizioni davvero diverse”
* il diminuito funziona perfettamente come materiale di collegamento: non introduce un nuovo mondo, introduce un meccanismo
```

**Dopo**

```rst
Un accordo °7 è simmetrico: le sue note dividono l'ottava in quattro terze minori. Per questo D°7, F°7, A♭°7 e B°7 contengono gli stessi suoni, scritti qui con gli enarmonici più semplici. Cambiano il nome e la lettura nel contesto.

Questa proprietà riguarda il diminuito, non l'intera scala sesta diminuita. Do–Re–Mi–Fa–Sol–La♭–La–Si non conserva lo stesso insieme di note se la trasporti per terze minori.

Il movimento che ci interessa nasce dall'alternanza: i quattro rivolti di C6 si intrecciano con i quattro rivolti di D°7. Puoi così far muovere le voci mantenendo riconoscibile il centro di Do.
```

### A2a — Seconda minore: attrito e destinazione

Fonte: `appunti-teoria/src/docs/3-intervalli.rst:123`.

La tendenza cromatica è utile; l’obbligo universale contraddice i campi modali descritti più avanti, incluso il frigio.

**Prima**

```rst
- Non vive mai da solo... chiede sempre una risoluzione.
```

**Dopo**

```rst
- Spesso conduce per semitono a una nota d'arrivo. Può anche restare come colore, se il contesto la sostiene.
```

### A2b — Quarta giusta: sospensione e struttura

Fonte: `appunti-teoria/src/docs/3-intervalli.rst:198`.

La quarta non è intrinsecamente un passaggio. Il confronto usa contesti già presenti nei volumi, senza introdurre un nuovo argomento.

**Prima**

```rst
- Stabilità apparente
- Leggera sospensione
- Orizzontalità
- Non spinge forte, ma non riposa del tutto.
- È un intervallo di passaggio mascherato da stabilità.
```

**Dopo**

```rst
- Apertura
- Possibile sospensione
- Sopra la fondamentale di un accordo maggiore può creare attrito con la terza.
- In un accordo sus o in una struttura per quarte può invece essere parte del suono che vuoi mantenere.
```

### A2c — Tritono: direzione contestuale

Fonte: `appunti-teoria/src/docs/3-intervalli.rst:218`.

Collega la funzione tonale all’esempio reale. Una distanza di sei semitoni non impone da sola una destinazione.

**Prima**

```rst
- Massima ambiguità
- Tensione strutturale
- Direzione obbligata
- Non è “brutto”. È instabile per natura.
- Proprio per questo è uno dei motori principali dell'armonia.
```

**Dopo**

```rst
- Tensione e ambiguità
- Fra terza e settima di V7 rende riconoscibile la spinta verso il I.
- In altri contesti può restare parte del colore, come la quarta aumentata sopra un accordo maggiore.
- Ascolta dove vanno le due note: la distanza da sola non decide la risoluzione.
```

### A2d — Settima maggiore: conservare il colore senza imporre una risoluzione

Fonte: `appunti-teoria/src/docs/3-intervalli.rst:314`.

Elimina la contraddizione con l’impiego di maj7 come accordo di riposo. Mantiene gli stessi riferimenti a spartito e audio; le due prove nuove sono istruzioni da eseguire, non descrizioni del file audio esistente.

**Prima**

```rst
- Tensione raffinata
- Fragilità
- Sospensione intensa
- Non urla. Sussurra, ma non riposa.

.. image:: 
   _static/music/intervallo-maj7.*
   :width: 300px

.. raw:: html

   <audio controls class="audio-controls">
      <source src="_static/music/intervallo-maj7.mp3" type="audio/mp3">
   </audio>

La settima maggiore è un intervallo strano.

Non è violento come il tritono, non è ruvido come la seconda minore. Eppure è profondamente instabile.

È una tensione che non chiede di muoversi subito.

Resta lì, sospesa, come qualcosa che non si chiude.

Quando la ascolti, non senti un'urgenza fisica di risoluzione. Senti piuttosto una fragilità. È come se la nota fosse troppo vicina a qualcosa di stabile per potersi rilassare davvero, ma non abbastanza lontana da creare conflitto.
Questa è la sua forza.

Dal punto di vista percettivo, la settima maggiore è quasi un unisono mancato.

È a un passo dall'ottava, che invece rappresenta il ritorno, la conferma.
Proprio questa vicinanza crea la tensione.

L'orecchio sente che “manca pochissimo”, ma quel pochissimo è decisivo. Non è una distanza che puoi ignorare. È una distanza che senti sempre.

Per questo la settima maggiore non è mai neutra. Anche quando è suonata piano, anche quando è immersa in un contesto morbido, rimane irrisolta.
```

**Dopo**

```rst
- Vicinanza all'ottava
- Colore riconoscibile negli accordi maj7
- Può cercare l'ottava oppure restare parte dell'accordo.

.. image::
   _static/music/intervallo-maj7.*
   :width: 300px

.. raw:: html

   <audio controls class="audio-controls">
      <source src="_static/music/intervallo-maj7.mp3" type="audio/mp3">
   </audio>

La settima maggiore è a un semitono dall'ottava. Prova Si–Do sopra un basso Do: il movimento è breve e ben riconoscibile.

Ora tieni il Si dentro Cmaj7, senza farlo salire. L'accordo può sostenere una conclusione proprio con quel colore. La vicinanza all'ottava resta, ma non ti obbliga a raggiungerla.
```

### A3 — Aree funzionali: criteri leggibili e coerenti

Fonte: `appunti-teoria/src/docs/6-armonia-funzionale.rst:179`.

La formulazione attuale attribuisce IV e VII anche al V triadico e fa dipendere la funzione dalla sola presenza della sensibile, presente però anche in Em. La sostituzione distingue triadi, settime e contesto senza eliminare la mappa delle tre aree.

**Prima**

```rst
Nella tonalità maggiore esistono due gradi strutturalmente instabili che organizzano tutto il campo armonico:

- IV grado (la quarta rispetto alla tonica)
- VII grado (la settima maggiore, la sensibile)

Questi due gradi non sono instabili “per convenzione”, ma perché creano attrito diretto con la tonica e generano direzione.

.. important::

   La presenza o assenza di questi gradi negli accordi è ciò che determina il tipo di funzione e quindi l'area tonale.

Area di tonica
^^^^^^^^^^^^^^

Gli accordi di tonica non contengono il IV grado della scala maggiore.

Accordi: I, IIIm, VIm

- nessun semitono che “spinga” verso la tonica
- nessuna gravità sottodominante
- nessuna sensibile attiva

Risultato percettivo: stabilità.

Questi accordi:

- possono durare a lungo
- non creano attesa
- non chiedono risoluzione

Sono “dentro casa”.

Area di sottodominante
^^^^^^^^^^^^^^^^^^^^^^

Gli accordi sottodominanti contengono il IV grado, ma non il VII.

Accordi: IIm, IV

Il IV grado:

- è instabile rispetto alla tonica
- tende a scendere verso la terza
- crea un allontanamento morbido


Risultato percettivo: movimento senza urgenza.

Questi accordi:

- non risolvono
- non spingono forte
- aprono lo spazio armonico

Sono il passaggio.

Area di dominante
^^^^^^^^^^^^^^^^^

Qui compare sia il IV sia il VII grado (la sensibile).

Accordi tipici: V, VII∅

La sensibile:

- è a semitono dalla tonica
- crea attrito massimo
- ha direzione obbligata
- spesso è accompagnata anche dal IV grado (es. nel V7), ma è il VII a determinare la funzione dominante

Risultato percettivo: tensione narrativa.

Questi accordi:

- non possono restare fermi
- chiedono risoluzione
- generano attesa

Sono il viaggio.

Questo modello funziona perché:

- IV e VII sono gli unici gradi che formano semitoni strutturali con le note di stabilità
- sono le note che “non si appoggiano”
- l'orecchio li riconosce immediatamente
```

**Dopo**

```rst
Nelle cadenze maggiori, due movimenti aiutano a sentire l'arrivo: il VII grado sale al I e il IV scende al III. In Do maggiore sono Si–Do e Fa–Mi. Li senti insieme nel passaggio da G7 a C.

La presenza di Si o Fa è un indizio, ma non basta da sola ad assegnare una funzione. Em contiene Si e può prolungare l'area di tonica; la triade G non contiene Fa e può già preparare C. Conta il percorso in cui l'accordo entra.

Area di tonica
^^^^^^^^^^^^^^

Il I è il riferimento principale. IIIm e VIm possono prolungarne il campo grazie alle note condivise, quando il contesto conferma quella lettura.

In Do maggiore Em condivide Mi e Sol con C; Am condivide Do e Mi con C. Questo permette di variare il basso e il colore senza allontanarsi necessariamente dal centro. Non significa che ogni Em o Am abbia sempre la stessa funzione.

Area di sottodominante
^^^^^^^^^^^^^^^^^^^^^^

IIm e IV preparano spesso la dominante. Nel II–V–I in Do, Dm7 porta verso G7: Fa resta comune e Do può scendere a Si. Il movimento comincia prima dell'arrivo sul V.

Nelle triadi Dm e F compare Fa, il IV grado della tonalità. Passando alle settime trovi Dm7 e Fmaj7: il colore si amplia, ma in una cadenza possono continuare a preparare il V. Osserva il movimento delle voci, non soltanto la presenza di Fa.

Area di dominante
^^^^^^^^^^^^^^^^^

V e VII° preparano tipicamente il I; con le settime diventano V7 e VII∅7. In Do maggiore, G7 contiene Si e Fa: nel passaggio a C, Si può salire a Do e Fa scendere a Mi. B∅7 contiene lo stesso tritono e può partecipare alla stessa preparazione.

La triade G contiene già Si, pur senza Fa. Aggiungere la settima rende esplicito il tritono; non crea da zero ogni possibilità di funzione dominante.

.. important::

   Queste aree sono una mappa per leggere i movimenti tonali. Verifica accordi precedenti e successivi, melodia e punti d'arrivo: la stessa sigla può assumere un ruolo diverso in un altro percorso.
```

### A4a — Pentatonica: definizione e prime famiglie

Fonte: `appunti-teoria/src/docs/4-scale.rst:785`.

La definizione generale resta distinta dalle proprietà delle due famiglie che seguono.

**Prima**

```rst
È una scala di **5 note**. Sembra poco. In realtà è un set di note **stabili, cantabili, resistenti**: funziona su tanti accordi, regge il tempo, e soprattutto si presta a quel tipo di fraseggio “parlato” che fa subito musica.
```

**Dopo**

```rst
È una scala di **cinque note per ottava**. Le pentatoniche maggiore e minore che vediamo qui permettono di costruire frasi riconoscibili con poco materiale. Il loro effetto cambia però con l'accordo, il ritmo e le note su cui ti fermi.
```

### A4b — Pentatoniche senza semitoni e rapporto con l’accordo

Fonte: `appunti-teoria/src/docs/4-scale.rst:818`.

Corregge sia “suona bene quasi sempre” sia “note dell’accordo o vicinissime”, che senza un accordo specificato non sono criteri verificabili.

**Prima**

```rst
La cosa importante non è la formula... è l'effetto: togliendo due gradi della scala diatonica, elimini molte frizioni “automatiche” e ottieni una tavolozza che suona bene anche quando l'armonia sotto si muove.

Perché suona bene quasi sempre
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

La pentatonica contiene soprattutto:

- note dell'accordo (o note vicinissime)
- intervalli molto cantabili
- poche “spine” che ti costringono a risolvere subito

Ecco perché la senti ovunque: folk, rock, blues, pop, jazz... è una lingua trasversale.
```

**Dopo**

```rst
Nella maggiore pentatonica togliamo quarto e settimo grado dalla scala maggiore. Restano cinque note senza semitoni fra loro. La relativa minore usa gli stessi suoni con un centro diverso.

Poche note, relazioni diverse
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

L'assenza di semitoni dentro queste due pentatoniche non elimina gli attriti con l'accompagnamento. Do–Re–Mi–Sol–La sopra Cmaj7 dà 1–9–3–5–13; sopra Dm7 le stesse note danno ♭7–1–9–11–5.

Il materiale è identico, ma cambiano gli appoggi. Prima scegli il sostegno armonico, poi ascolta dove vuoi fermarti. Altre pentatoniche possono contenere semitoni: il nome indica cinque note, non un unico comportamento.
```

### A4c — Pila di quinte: circoscrivere la conclusione

Fonte: `appunti-teoria/src/docs/4-scale.rst:848`.

La costruzione per quinte è valida per la famiglia mostrata, non è la definizione di tutte le pentatoniche.

**Prima**

```rst
Quindi la pentatonica non è solo “una scala di 5 note”... è un frammento del giro delle quinte, cioè una porzione di armonia naturale.
```

**Dopo**

```rst
Questa costruzione spiega la relazione fra i suoni della pentatonica maggiore e della relativa minore. Non descrive ogni possibile scala di cinque note.
```

### A4d — Cinque note non assegnano un genere

Fonte: `appunti-teoria/src/docs/4-scale.rst:914`.

Conserva la distinzione fra materiale e linguaggio, evitando di definire tutte le pentatoniche “molto stabili”.

**Prima**

```rst
La pentatonica non è un genere. È un insieme di cinque gradi molto stabile, presente in tantissime culture musicali. Il blues, invece, è una lingua storica e sonora specifica. Può usare la pentatonica come materiale... ma non coincide con essa.
```

**Dopo**

```rst
Una scala di cinque note non determina da sola un genere. Le pentatoniche maggiore e minore compaiono in linguaggi diversi; il blues ne usa il materiale con una pronuncia e un comportamento armonico riconoscibili.
```

### A4e — Evitare una categoria implicita di pentatonica pura

Fonte: `appunti-teoria/src/docs/4-scale.rst:926`.

La parola “pura” non identifica una famiglia. Il nuovo testo mantiene un esempio concreto e controllabile.

**Prima**

```rst
La pentatonica “pura” è neutra nel senso migliore del termine: non impone una grammatica armonica rigida.

Prendiamo la pentatonica maggiore: 1 2 3 5 6. Se la confronti con la scala maggiore completa (1 2 3 4 5 6 7), noti che mancano 4 e 7... proprio i due gradi che, nella tonalità europea, creano le tensioni più direzionali (la 4 verso la 3, la 7 verso la 1). Togliendo quelle due calamite, ottieni un suono aperto, “senza spigoli”, che non ti costringe a risolvere in modo specifico.
```

**Dopo**

```rst
La maggiore pentatonica omette Fa e Si rispetto a Do maggiore: non contiene il semitono Mi–Fa né Si–Do. Questo le dà un profilo diverso dalla scala completa, ma non decide da solo come debba essere usata. Sopra un accordo diverso anche gli stessi cinque suoni possono creare tensioni.
```

### A4f — Timbro, intonazione e contesto non assegnano automaticamente lo stile

Fonte: `appunti-teoria/src/docs/4-scale.rst:932`.

Il temperamento non impedisce il fraseggio blues: serve evitare un’altra regola assoluta mentre si circoscrive il termine pentatonica.

**Prima**

```rst
Quindi: una pentatonica suonata in modo perfettamente temperato e “pulito” tende a evocare un colore folk, arcaico, universale... non necessariamente blues.
```

**Dopo**

```rst
Anche con note perfettamente temperate puoi far riconoscere una frase blues attraverso ritmo, articolazione e rapporto con gli accordi. Le inflessioni di intonazione ampliano queste possibilità.
```

### A5 — Qualità di settima di dominante e funzione

Fonte: `appunti-teoria/src/docs/5-accordi.rst:714`.

Allinea questo passaggio con il paragrafo successivo che ammette già il G7 statico e blues. Non richiede una nuova sezione di eccezioni.

**Prima**

```rst
La **dominante** è diversa.
Non sta ferma nemmeno quando è ferma.

Un accordo dominante contiene al suo interno una tensione strutturale che spinge in avanti: il tritono tra la terza maggiore e la settima minore. 

Questa tensione non avviene per convenzione, ma per attrito percettivo: alcune delle sue note non si appoggiano bene sul centro e cercano una risoluzione.

Per questo la dominante è narrativa.

Non descrive un luogo, ma un momento di passaggio.

Quando compare, l'orecchio sa che qualcosa deve succedere. Anche se non sai perché, lo senti. E quando la risoluzione arriva, il sollievo non è intellettuale. È fisico.
```

**Dopo**

```rst
Un accordo di **settima di dominante** contiene il tritono fra terza maggiore e settima minore. In G7 sono Si e Fa.

Quando G7 prepara C, quelle due voci possono andare a Do e Mi: senti il movimento verso la tonica. È una delle direzioni fondamentali dell'armonia tonale.

Ma G7 può anche restare fermo in un vamp o essere il I7 di un blues in Sol. La struttura è la stessa; il ruolo cambia con il contesto. Distingui quindi la qualità dell'accordo dalla funzione di dominante che può assumere.
```

### A6 — Il diminuito di passaggio: circoscrivere l’affermazione

Fonte: `appunti-teoria/src/docs/8-armonia-diminuita.rst:15`.

Evita di dedurre dal solo intervallo un obbligo di movimento, mantenendo il perimetro del capitolo.

**Prima**

```rst
Un accordo di settima diminuita contiene **due tritoni** (in C°7: Do–Sol♭ e Mi♭–La); la triade diminuita ne ha uno solo. Con due tensioni di quel tipo dentro, l'accordo non trova mai un punto di riposo: chiede sempre di muoversi.
```

**Dopo**

```rst
Un accordo di settima diminuita contiene **due tritoni** (in C°7: Do–Sol♭ e Mi♭–La); la triade diminuita ne ha uno solo. Nei collegamenti che studiamo qui, il diminuito prepara l'accordo vicino: segui dove vanno le singole voci per sentire la risoluzione.
```

## Limite della fase A

Questi interventi correggono i passaggi prioritari; non certificano che tutti gli assoluti dei volumi siano risolti. Restano da valutare insieme i paragrafi sul minore in Teoria 4 e 6, che lo descrivono come mai definitivo o mai stabilizzato: l’esistenza di più forme del minore non implica che una tonica minore sia instabile. La revisione di quei paragrafi richiede un intervento unitario per evitare correzioni isolate contraddette poche righe dopo. Non è un prerequisito per verificare le formule del nuovo catalogo.

## Nuova pagina: obiettivo e collocazione

Titolo proposto: **Strutture melodiche e costruzione della frase**. File proposto: `src/docs/strutture-melodiche.rst`; etichetta generale: `strutture-melodiche`. Inserimento nel toctree di Pratica dopo `5-arpeggi`, senza rinominare capitoli esistenti. È un percorso per il lavoro melodico; il lettore interessato all’accompagnamento può passare direttamente ad Accordi.

Risultato atteso: scegliere una struttura, riconoscerne gli intervalli, organizzarla in una frase breve e modificarla mantenendo pulsazione e punto d’arrivo. Non serve conoscere tutte le famiglie per iniziare.

### Struttura della pagina

| Sezione | Cosa deve permettere di fare | Materiale da recuperare o aggiungere |
|---|---|---|
| Poche note, una scelta precisa | Distinguere la collezione da una frase | Introduzione e confronto originale di quattro note |
| Formula e riferimenti | Nominare gradi della struttura e dell’accordo senza confonderli | Esempio su due bassi; rimandi a Teoria 3–5 |
| Famiglie di strutture | Consultare la classificazione rigorosa | Tabella da completare dopo verifica sul riferimento richiesto |
| Cambiare ordine e registro | Conservare l’identità del materiale trasformando il percorso | Due ordini e uno spostamento d’ottava; evitare tavole esaustive nell’ingresso |
| Dare tempo alle note | Usare pause, durate e accenti prima di aggiungere altezze | Raccordo a Teoria 12 e agli studi di Pratica 4–5 |
| Collegare due accordi | Scegliere l’arrivo prima del riempimento | Una cadenza di quattro battute su Progressioni |
| Organizzare le pentatoniche | Distinguere salto nella collezione da intervallo risultante | Riutilizzo di Pratica 4, poi rimando agli studi 05–06 di Pratica 9 |
| Una frase tua | Inventare una risposta e verificarla | Registrazione breve con stessi accordi, tempo e punto d’arrivo |

### Apertura proposta, già redatta

> Una scala ti mostra un insieme di suoni. Una frase sceglie quali usare, in quale ordine e con quali durate. Fra le due cose puoi lavorare con una struttura più piccola: poche note di cui riconosci gli intervalli e il rapporto con l’accordo.
>
> Prendi Do–Re–Mi–Sol. Rispetto a Do sono 1–2–3–5. Se le suoni Mi–Sol–Re–Do, il materiale resta lo stesso; cambia il percorso. Se lasci una pausa dopo Mi–Sol, cambia anche l’attesa di chi ascolta.
>
> Canta i due ordini prima di cercarli sulla tastiera. Poi scegline uno, suonalo sopra Cmaj7 e inventa una risposta più corta. Cominciamo da qui: riconoscere una scelta e riuscire a trasformarla.

Questa apertura dimostra una procedura; non dichiara che 1–2–3–5 sia la prima o unica famiglia della classificazione di riferimento. La posizione definitiva dell’esempio dipende dalla verifica di quel catalogo.

### Distinzioni da rendere esplicite

| Livello | Esempio | Cosa cambia |
|---|---|---|
| Materiale | Do–Re–Mi–Sol, formula 1–2–3–5 da Do | Le altezze scelte |
| Ordine | Mi–Sol–Re–Do, gradi 3–5–2–1 | La successione, non la collezione |
| Registro | Stesse classi di altezza in ottave diverse | Distanze effettive e profilo |
| Ritmo | Quattro crome seguite da una pausa di minima | Attacchi, durate e spazio |
| Applicazione | Do–Re–Mi–Sol su Dm7: ♭7–1–9–11 | Il riferimento armonico |
| Diteggiatura | Stesse altezze e durate su altre corde | Il percorso fisico |

Quattro note di un accordo, quattro note selezionate da una scala e quattro note cromatiche non diventano automaticamente la stessa famiglia solo perché hanno la stessa cardinalità. La cellula Mi–Sol–Si–Re già usata nei volumi rimane: è una struttura accordale di Em7 e su Cmaj7 dà 3–5–7–9. Può essere confrontata con Do–Re–Mi–Sol senza essere sostituita o rinominata.

### Esempio originale: dalla struttura alla cadenza

Bozza musicale da notare e diteggiare nella successiva attuazione. Metro 4/4, crome regolari, semiminima = 60. Una sigla per battuta. Il registro proposto è Do4–Si4 in altezze reali, con Do4 come Do centrale; la notazione per chitarra dovrà rispettare la consueta trasposizione d’ottava. Non avviare due lettori audio insieme.

| Battuta | Accordo | Struttura di riferimento | Linea | Durate |
|---|---|---|---|---|
| 1 | Dm7 | Re–Mi–Fa–La: 1–2–♭3–5 da Re | Re4–Mi4–Fa4–La4 | Quattro crome + pausa di minima |
| 2 | G7 | Sol–La–Si–Re: 1–2–3–5 da Sol | Sol4–La4–Si4–Re4 | Quattro crome + pausa di minima |
| 3 | Cmaj7 | Do–Re–Mi–Sol: 1–2–3–5 da Do | Mi4–Sol4–Re4–Do4 | Quattro crome + pausa di minima |
| 4 | Cmaj7 | Stessa struttura | Do4 | Minima + pausa di minima |

Il primo arrivo sul I è Mi, la terza: la linea non ricomincia dalla fondamentale a ogni accordo. Le strutture delle prime due battute evidenziano qualità diverse mediante Fa naturale e Si naturale. Sono frammenti di frase con uno spazio deliberato, non arpeggi completi degli accordi.

**Percorso di studio proposto:** canta Fa, Si e Mi sulle prime tre battute; esegui la linea completa; conserva la terza battuta e cambia soltanto l’ordine delle note nella seconda; inventa infine una risposta alternativa nella quarta. Registra due giri sulla stessa base. Verifica se ritrovi il Mi sul I e se conti le pause senza accelerare.

**Esito atteso:** sai cantare il materiale, indicare la struttura di ogni battuta e produrre una variante mantenendo forma e arrivo. Una maggiore velocità non è il criterio di completamento.

### Pentatoniche: un esempio del problema di notazione

Do maggiore pentatonica è Do–Re–Mi–Sol–La. Partendo da Do, passare alla terza nota della collezione porta a Mi: una terza maggiore. Partendo da Mi e avanzando ancora di due posizioni arrivi a La: una quarta giusta. La stessa operazione sugli indici non produce sempre lo stesso intervallo diatonico.

La futura pagina deve mostrare insieme ordine nella collezione, gradi rispetto alla sua fondamentale e intervalli effettivi quando necessario. Il software deve usare la stessa convenzione: “una nota sì e una no” è più preciso di “terze” se si intende un’operazione su qualsiasi collezione.

### Contenuti da verificare prima della stesura del catalogo

- Famiglie e criteri di classificazione delle strutture melodiche richiesti dall’autore.
- Tipi pentatonici, equivalenze, trasformazioni e ordine della presentazione.
- Distinzione fra rotazione della stessa collezione, trasposizione e famiglia con formula differente.

L’indice editoriale di un metodo non basta a ricostruire questi dettagli. Gli esempi sopra sono proposte originali e verificabili: non certificano la corrispondenza a quella classificazione. Nel testo rivolto al lettore si useranno formulazione autonoma ed esempi originali.

## Schema editoriale dettagliato — proposta del 14 novembre 2026

Sviluppa la tabella «Struttura della pagina» in un progetto redigibile sezione per sezione. Stato: **proposto**, da confermare con l’autore prima della stesura in `src/docs`. Nessun sorgente del volume è stato modificato.

### Impianto

- File `src/docs/strutture-melodiche.rst`, titolo di livello `=`, sezioni `-`, sottosezioni `~`, esercizi `^`, come in `4-scale.rst` e `5-arpeggi.rst`.
- Toctree di `index.rst`: fra `5-arpeggi` e `6-accordi`. Nessun capitolo rinominato.
- Etichette: `strutture-melodiche` per la pagina e una per ogni sezione, indicate sotto; servono ai rimandi in entrata e non vanno cambiate dopo la pubblicazione.
- Esercizi nel formato già usato in Pratica 4 e 5: **Scopo**, **Procedura**, **Ascolto**, **Varianti**, **Verifica**. Nessun nuovo formato di riquadro.
- Rimandi a Teoria con URL completi del sito pubblicato, come negli altri capitoli; non esiste intersphinx fra i volumi.
- Esempi musicali: nuovo generatore `scripts/generate_melodic_structures.py` sul modello di `generate_arpeggio_exercises.py`, file `_static/music/strutture-NN.*`, spartito e TAB allineati secondo `leggere-gli-esempi`, audio a 60 e 90 BPM come negli esercizi di Arpeggi (ADR 0001).
- Estensione indicativa: paragonabile a una sezione maggiore di Arpeggi. La pagina è un ingresso, non un catalogo: le tabelle complete restano in fondo alla sezione Famiglie.

### Tre modi di usare la pagina

Da dichiarare nel paragrafo «Come usare la pagina», dopo l’apertura:

| Ingresso | Sezioni | Per chi |
|---|---|---|
| Essenziale | 1, 2, 4, 5, 6, 8 | Chi vuole costruire una frase con poco materiale |
| Consultazione | 3, 7 | Chi cerca formule, famiglie e organizzazioni |
| Prosecuzioni | 9 | Chi ha completato la sezione 8 e vuole materiali avanzati |

Prerequisiti dichiarati: scala maggiore in una posizione (Pratica 4), arpeggio di Cmaj7 (Pratica 5), capacità di cantare una linea di quattro note. Non servono le famiglie complete né le pentatoniche.

### Sezioni

**0. Apertura e «Come usare la pagina»** — etichetta `strutture-melodiche`.
Testo: l’apertura già redatta sopra, poi la tabella dei tre ingressi e i prerequisiti. Nessun esempio musicale oltre a quello citato nell’apertura, che coincide con S1.

**1. Poche note, una scelta precisa** — `strutture-poche-note`.
Obiettivo: distinguere collezione, struttura e frase.
Esempio **S1** (2 battute, Cmaj7): Do–Re–Mi–Sol in salita, pausa; Mi–Sol–Re–Do, pausa. Stesso materiale, percorso diverso.
Esercizio: cantare entrambi gli ordini, suonarli, inventare una risposta di due o tre note.
Stato: redigibile subito.

**2. Formula e riferimenti** — `strutture-riferimenti`.
Obiettivo: separare tre riferimenti: grado rispetto alla fondamentale della struttura, grado rispetto all’accordo, posizione nella collezione.
Contenuto: la tabella «Distinzioni da rendere esplicite», ridotta a materiale, applicazione e diteggiatura; ordine, registro e ritmo passano alle sezioni 4 e 5.
Esempio **S2** (2 battute): la stessa linea Do–Re–Mi–Sol su Cmaj7 (1–2–3–5) e su Dm7 (♭7–1–9–11), con il basso nella base.
Raccordo: la cellula Mi–Sol–Si–Re dell’Introduzione, su Cmaj7 3–5–7–9, come struttura accordale da confrontare con quella selettiva di S1. Rimandi a Teoria 3, 4 e 5.
Stato: redigibile subito.

**3. Famiglie di strutture** — `strutture-famiglie`.
Obiettivo: consultazione rigorosa.
Forma fissata per ogni famiglia: criterio di inclusione, formula, esempio da Do, un’applicazione su accordo, rimando a una sezione dove viene usata.
Tabella completa in fondo alla sezione, non all’inizio.
Stato: **bloccata** dalla verifica della classificazione di riferimento (vedi «Contenuti da verificare»). Proposta: la prima pubblicazione omette la sezione, senza segnaposto visibile; la si aggiunge dopo la verifica, con etichetta già riservata.

**4. Cambiare ordine e registro** — `strutture-ordine-registro`.
Obiettivo: trasformare il percorso mantenendo il materiale.
Esempio **S3** (4 battute, Cmaj7): ordine 1–2–3–5; ordine 3–5–2–1; stesso ordine con Re e Do all’ottava superiore; le stesse altezze della battuta 3 in una seconda diteggiatura fra l’VIII e il XII tasto, raccordo a Pratica 3. In attuazione la quarta battuta sostituisce il ritorno al registro iniziale, per mostrare la diteggiatura nello spartito.
Raccordo: le Varianti di «Dall’arpeggio alla frase» in Pratica 5, che chiedono già di cambiare l’ordine delle note dell’accordo; qui lo stesso procedimento si applica a una struttura selettiva.
Stato: redigibile subito. Non includere tavole di tutte le permutazioni.

**5. Dare tempo alle note** — `strutture-ritmo`.
Obiettivo: cambiare pause, durate e accenti prima di cambiare le altezze.
Esempio **S4** (3 battute): la linea Mi–Sol–Re–Do in crome con pausa; con le prime due note lunghe; con partenza in levare. Altezze invariate.
Raccordi: «Dal pattern a una frase» in Pratica 4; Teoria 12, «Sviluppare una cellula», senza ripeterne la spiegazione.
Stato: redigibile subito.

**6. Collegare due accordi** — `strutture-due-accordi`.
Obiettivo: scegliere l’arrivo prima del riempimento.
Esempio **S5**: l’esempio originale già redatto (Dm7–G7–Cmaj7–Cmaj7, arrivo su Mi), con base senza chitarra e il percorso di studio già scritto.
Raccordi: `progressioni-ii-v-i`, sottosezione «Improvvisare: scegliere note bersaglio»; `strumenti-progressioni` per suonare la stessa cadenza in altre tonalità.
Stato: redigibile subito.

**7. Organizzare le pentatoniche** — `strutture-pentatoniche`.
Obiettivo: distinguere il salto nella collezione dall’intervallo che ne risulta.
Contenuto: il paragrafo «Pentatoniche: un esempio del problema di notazione» e la convenzione «una nota sì e una no».
Esempio **S6** (2 battute, C6): Do pentatonica maggiore a coppie Do–Mi, Re–Sol, Mi–La, Sol–Do, La–Re. Una terza maggiore e quattro quarte giuste: lo stesso passo produce intervalli diversi.
Raccordi: `scala-pentatonica-maggiore` e `scala-pentatonica-minore` per le mappe; `modern-05` e `modern-06` per sovrapposizione e side-slip.
Stato: parte su maggiore e minore redigibile subito; altre famiglie pentatoniche **bloccate** come la sezione 3.

**8. Una frase tua** — `strutture-frase-tua`.
Obiettivo: produrre e verificare una frase propria.
Consegna: sulla base di S5, due giri registrati con una struttura per accordo scelta dal lettore; arrivo deciso prima di suonare.
Verifica: stessa pulsazione nei due giri, pause contate, arrivo previsto raggiunto, seconda versione riconoscibile come variante della prima.
Riquadro «Brano guida», secondo la convenzione dell’Introduzione: portare una struttura nello studio `progressioni-aaba`.
Stato: redigibile subito.

**9. Dove proseguire** — senza etichetta propria.
Rimandi brevi: `licks-progressioni`; `modern-01` per la cellula Mi–Sol–Si–Re; Percorsi d’autore; `strumenti-scale` e `strumenti-arpeggi` per esercitare ordine e registro. Nessun nuovo contenuto.

### Esempi musicali da produrre

| Id | Sezione | Battute | Accordi | Base |
|---|---|---|---|---|
| S1 | 1 | 2 | Cmaj7 | No |
| S2 | 2 | 2 | Cmaj7, Dm7 | Sì, per sentire il basso |
| S3 | 4 | 4 | Cmaj7 | No |
| S4 | 5 | 3 | Cmaj7 | No |
| S5 | 6 | 4 | Dm7–G7–Cmaj7 | Sì |
| S6 | 7 | 2 | C6 | No |

Le altezze dei sei esempi rientrano in Do4–Re5 reali. Prima della generazione verificare con un controllo automatico appartenenza delle note alle strutture dichiarate, gradi rispetto agli accordi e durata delle battute, come per l’esempio S5.

### Rimandi in entrata

Una frase per sede, nel punto indicato; nessuna riscrittura dei testi esistenti.

| Sede | Punto |
|---|---|
| Pratica 4 | Fine di «Dal pattern a una frase», dopo **Verifica** |
| Pratica 5 | Fine dell’esercizio 8, «Dall’arpeggio alla frase» |
| Pratica 7 | «Improvvisare: scegliere note bersaglio» nel II–V–I maggiore |
| Pratica 1 | Paragrafo dei due fili, accanto alla cellula Mi–Sol–Si–Re |
| Teoria 12 | Fine di «Sviluppare una cellula» |

Pratica 11 e gli Strumenti restano esclusi fino alla definizione delle famiglie (fase D).

### Ordine di stesura proposto

1. Sezioni 0, 1, 2, 4, 5, 6, 8, 9 e parte di 7, con S1–S6.
2. Generatore, build HTML con `-W --keep-going`, test dei collegamenti, ascolto degli audio.
3. Rimandi in entrata.
4. Sezione 3 e famiglie pentatoniche aggiuntive, dopo la verifica della classificazione.

### Decisioni richieste all’autore

- ~~Pubblicare la pagina senza la sezione 3 oppure attendere la classificazione completa.~~ **Deciso dall’autore il 14 novembre 2026:** la prima pubblicazione esce senza la sezione 3 e senza segnaposto visibile; l’etichetta `strutture-famiglie` resta riservata.
- ~~Audio a una velocità o a due.~~ **Deciso il 14 novembre 2026:** due velocità, 60 e 90 BPM, come negli esercizi di Arpeggi.
- ~~Conferma dei sei esempi e della loro collocazione.~~ **Confermati il 14 novembre 2026**; stesura autorizzata nel perimetro dello schema.

## Dipendenze e impatto

| Sede esistente | Intervento successivo proposto |
|---|---|
| Teoria 3–5 | Applicare le correzioni condivise e spiegare i riferimenti intervallari nella sede pertinente |
| Teoria 6 e 8 | Correggere A1/A3/A6; conservare esempi e impianto dei capitoli |
| Teoria 12 | Inserire un rimando alla pratica delle trasformazioni, evitando di duplicarne la spiegazione |
| Pratica 4, “Dal pattern a una frase” | Conservare lo studio locale e aggiungere un rinvio al procedimento generale |
| Pratica 5, “Dall’arpeggio alla frase” | Conservare l’esercizio; collegare strutture accordali e nuove strutture selettive |
| Pratica 7 | Usare il II–V–I già presente come contesto dell’esempio originale |
| Pratica 8 | Collegare la nuova pagina al lavoro su bersagli e trasformazioni; conservare il catalogo originale |
| Pratica 9 e percorsi d’autore | Usare i casi avanzati già disponibili come prosecuzioni facoltative |
| Pratica 11 e Strumenti | Aggiungere i nuovi ingressi solo quando materiali e trasformazioni saranno definiti |

Non occorre spostare o riscrivere i cinquanta licks, i dodici studi modern/fusion o i sessanta esempi d’autore. Per eventuali modifiche future alle parti generate si interviene nei generatori, verificando prima la rigenerazione a vuoto.

## Alternative e criteri di confronto

| Alternativa | Vantaggio | Limite | Valutazione |
|---|---|---|---|
| Lasciare i procedimenti nelle sedi attuali | Nessuna crescita del volume | Il raccordo e la classificazione restano impliciti | Non risolve la richiesta |
| Ampliare soltanto Licks | Recupera una sede melodica esistente | La costruzione da poche note arriva dopo le progressioni ed è legata alla raccolta bebop | Possibile, meno chiaro come ingresso generale |
| Pagina autonoma dopo Arpeggi | Una sede comune raggiungibile da più percorsi | Richiede rimandi e una gerarchia per non diventare un altro catalogo | Raccomandata |
| Nuovi capitoli e applicazioni per ogni famiglia | Ampia separazione dei materiali | Frammentazione e duplicazione del percorso | Da evitare in questa fase |

## Raccomandazione e verifiche eseguite

Valutare i blocchi A come interventi circoscritti; usare l’apertura e l’esempio per giudicare tono, difficoltà e utilità della nuova pagina prima di sviluppare tutte le famiglie. La classificazione richiesta resta da verificare prima della redazione completa.

Controllati automaticamente: presenza univoca di ogni citazione nei sorgenti; classi di altezza e trasposizioni di accordo diminuito e scala sesta diminuita; gradi delle sovrapposizioni usate nelle proposte; appartenenza delle note dell’esempio alle strutture dichiarate; durata di quattro semiminime per ogni battuta.

Nella preparazione della proposta non erano state eseguite build Sphinx; l’attuazione della fase A e la relativa verifica sono registrate sotto. Spartito, TAB e audio del nuovo esempio non sono ancora prodotti. Nell’attuazione occorreranno controllo della notazione e della diteggiatura, ascolto dell’audio, build HTML con avvisi come errori e test pertinenti; la build HTML da sola non verifica la correttezza musicale.


## Attuazione della fase A — 14 novembre 2026

Dopo la conferma dell’autore sono stati applicati tutti i quattordici blocchi nei cinque capitoli di Teoria, sul branch `revisione-strutture-fase-a`. La nuova pagina melodica resta alla fase di schema: la classificazione completa richiede il confronto con il riferimento richiesto.

Durante l’applicazione sono state apportate due precisazioni tecniche ai testi proposti: lunghezza della sottolineatura RST del titolo “Poche note, relazioni diverse”; confronto fra triadi in A3, esplicitando che Em e Am condividono ciascuno due note con C, senza attribuire due note comuni a ogni coppia. I blocchi “Dopo” riportati sopra sono allineati ai sorgenti.

Verifiche eseguite: corrispondenza dei quattordici blocchi con i sorgenti finali; controllo delle note comuni e dei rapporti intervallari; build HTML di Teoria mediante `./build.sh` con `-W --keep-going`, conclusa con successo; `git diff --check`. Nessuna rigenerazione dei materiali musicali, che restano quelli esistenti. Il controllo HTML è strutturale; non costituisce ascolto degli audio o verifica dei formati PDF/ePub.

Attuazione di Teoria registrata su `main` nel commit `223ad65`. Documentazione predisposta per commit su `main` di Pratica. Il primo push di Teoria, il 14 novembre 2026, era bloccato dalla mancata risoluzione di `github.com`; ripetuto lo stesso giorno, ha portato `origin/main` di Teoria a `223ad65` e quello di Pratica a `7e776af`.

## Attuazione della pagina melodica — 14 novembre 2026

Dopo le decisioni dell’autore (pubblicazione senza sezione 3, audio a 60 e 90 BPM, esempi confermati) è stata scritta la pagina secondo lo schema.

- `src/docs/strutture-melodiche.rst`, nel toctree fra `5-arpeggi` e `6-accordi`. Sezioni e etichette come nello schema; `strutture-famiglie` non compare ed è riservata. La sezione «Come usare la pagina» indica tre ingressi; con la sezione 3 assente l’approfondimento coincide con la sezione 7.
- `scripts/generate_melodic_structures.py` genera sedici sorgenti LilyPond: S1–S6 a 60 e 90 BPM e le basi di S2 e S5 alle due velocità (`strutture-NN[-base][-90].ly`). Esempi e basi con accompagnamento usano basso elettrico e accordi a due voci, con l’overlay `sf/PracticeRhythm.sf2` come gli studi modern jazz. Conteggio di quattro Do acuti, come negli esercizi di Arpeggi.
- Rimandi in entrata: Pratica 1 (paragrafo dei due fili), 4 (dopo «Dal pattern a una frase»), 5 (dopo l’esercizio 8), 7 (dopo le note bersaglio del II–V–I); Teoria 12, fine di «Sviluppare una cellula», con URL del sito di Pratica.
- Test `tests/test_melodic_structures.py`: lunghezza delle battute e registro Do4–Re5; ordini di S1; gradi di S2 su Cmaj7 e Dm7; spostamento d’ottava, intervalli e seconda diteggiatura di S3; altezze invariate e tre ritmi distinti in S4; strutture e arrivo sulla terza in S5; una terza e quattro quarte in S6; corrispondenza fra risorse generate e riferimenti della pagina.

Verifiche eseguite: generazione e compilazione delle sedici partiture con `build-lilypond.sh` (nessun avviso LilyPond; avvisi FluidSynth sul canale 9 identici a quelli degli esercizi esistenti); controllo visivo degli spartiti S3–S6 e della base di S5; suite `unittest` di Pratica (46 test, inclusi gli 8 nuovi) superata; build HTML di Pratica e Teoria con `-W --keep-going` concluse con successo; presenza di tutte le risorse SVG e MP3 referenziate nell’HTML. Non verificati: ascolto completo degli audio, formati PDF ed ePub, pagina pubblicata su Read the Docs.

## Fase A, completamento: la tonica minore — proposta del 14 novembre 2026

Stato: **approvato dall’autore e applicato** il 14 novembre 2026 (vedi «Attuazione» in fondo). Riprende il punto lasciato aperto in «Limite della fase A».

### Problema

Teoria 4 e 6 descrivono il minore come «instabile», «mai definitivo», con una gravità «mai completamente stabilizzata». Le stesse pagine mostrano però che una cadenza V7–Im chiude con fermezza, e l’elenco delle aree tonali di Teoria 6 mette V7 come dominante «fondamentale». La contraddizione nasce dal confondere due cose:

- **il centro**: la tonica minore, preparata da una dominante con la sensibile, conclude quanto quella maggiore;
- **i gradi mobili**: sesto e settimo grado hanno due forme, e la musica sceglie fra le due a seconda della direzione.

La mobilità riguarda i secondi, non il primo. Le sostituzioni seguenti lo dicono in ogni punto in cui compare l’affermazione assoluta e lasciano invariato il resto: le quattro scale, gli esempi, il discorso sul carattere e sull’ambiguità come risorsa. Vanno applicate insieme, per non lasciare affermazioni contraddette poche righe dopo.

Ricerca eseguita in entrambi i volumi su «instabil», «mai definit» e «stabilizzat» accanto a «minore»: gli unici casi sono quelli elencati. Nessun riferimento interno punta ai titoli che cambiano; per conservare gli indirizzi già pubblicati, ogni titolo modificato riceve un’etichetta con l’identificatore precedente.

### M1 — Teoria 4, differenze percettive

Prima:

```rst
Nel maggiore:

- la tonica è chiara
- le tensioni sono ordinate
- il sistema tende alla stabilità

Nel minore:

- il centro è meno definitivo
- le tensioni sono più ambigue
- il sistema è mobile: 
   - alcuni gradi cambiano identità
   - la scala non è mai una sola
   - le tensioni si adattano al contesto
   - l'orecchio accetta più versioni dello stesso suono
```

Dopo:

```rst
Nel maggiore:

- la tonica è chiara
- le tensioni sono ordinate
- sesto e settimo grado hanno una sola forma

Nel minore:

- la tonica può essere altrettanto conclusiva, se la prepara una dominante con la sensibile
- le tensioni sono più ambigue
- il sistema è mobile:
   - sesto e settimo grado cambiano identità
   - la scala non è una sola
   - le tensioni si adattano al contesto
   - l'orecchio accetta più versioni dello stesso suono
```

### M2 — Teoria 4, «Tristezza, dramma, instabilità»

Titolo nuovo: **Tristezza, dramma, mobilità**, con etichetta `.. _tristezza-dramma-instabilita:` per conservare l’ancora. La prima frase, con la sua punteggiatura, resta dell’autore.

Prima (dopo la prima frase):

```rst
Il mondo minore non è semplicemente “più scuro” del maggiore. **È instabile, mobile, ambiguo**.

Dove il maggiore tende a dichiarare un centro, il minore lo *mette in discussione*.

Dove il maggiore organizza, il minore *oscilla*.

Dove il maggiore afferma, il minore *interroga*.

Per questo il minore è spesso associato a:

* dramma
* tensione irrisolta
* introspezione
* conflitto emotivo

Non perché sia debole, ma perché **non è mai definitivo**.
```

Dopo:

```rst
Il mondo minore non è semplicemente “più scuro” del maggiore. **È mobile e ambiguo**.

Mobile non vuol dire instabile. La tonica minore può chiudere un brano con la stessa fermezza della maggiore. A muoversi sono i gradi che la circondano: sesto e settimo hanno due forme, e la musica sceglie a seconda della direzione.

Dove il maggiore offre una sola strada verso la tonica, il minore ne offre diverse: con la sensibile o senza, con la sesta maggiore o minore.

Per questo il minore è spesso associato a:

* dramma
* tensione prolungata
* introspezione
* conflitto emotivo

Non perché sia debole, ma perché **lascia aperte più strade**. Lo stesso materiale può suonare sereno, come nel dorico, o deciso, come in una cadenza con V7: il carattere dipende da come lo usi.
```

### M3 — Teoria 4, «Perché la musica non sceglie mai una sola versione»

Titolo invariato: «mai» si riferisce alla pratica di scegliere fra le versioni, non al centro.

Prima:

```rst
Nella musica reale, soprattutto quella viva, improvvisata o cantabile, il **minore non si presenta mai in forma pura**.
```

Dopo:

```rst
Nella musica reale, soprattutto quella viva, improvvisata o cantabile, il **minore resta raramente in una sola forma** per tutto il brano.
```

### M4 — Teoria 6, titolo della sezione

Titolo nuovo: **Tonalità minore: un centro, più scale**, con etichetta `.. _tonalita-minore-un-sistema-non-stabile:` per conservare l’ancora.

### M5 — Teoria 6, «Il minore non è una tonalità, è una famiglia»

Prima:

```rst
Questa pluralità non è un problema teorico. È la descrizione di un fatto musicale: nel minore, la gravità non è mai completamente stabilizzata.

Per questo gli accordi che nascono dal minore non sono mai oggetti fissi.
Sono **adattamenti locali** a un contesto in movimento.
```

Dopo:

```rst
Questa pluralità non è un problema teorico. È la descrizione di un fatto musicale: nel minore la tonica resta ferma, mentre sesto e settimo grado cambiano forma a seconda della direzione.

Per questo molti accordi del minore non hanno una qualità fissa.
Sono **adattamenti locali**: lo stesso grado prende la forma che serve in quel punto.
```

### M6 — Teoria 6, funzione e qualità

Prima:

```rst
Nel maggiore, un accordo diatonico tende a mantenere una funzione abbastanza stabile. Nel minore, no.
```

Dopo:

```rst
Nel maggiore, un accordo diatonico tende a mantenere una qualità fissa. Nel minore la funzione resta riconoscibile, ma la qualità cambia più spesso.
```

L’elenco successivo («Lo stesso grado può apparire con qualità diverse») resta invariato e ora segue senza contraddizione.

### M7 — Teoria 6, la dominante nel minore

Prima:

```rst
La dominante minore “diatonica” esiste, ma spesso non basta. La dominante maggiore è un evento narrativo, non un dato strutturale.
```

Dopo:

```rst
La dominante minore “diatonica” esiste, ma per una cadenza conclusiva spesso non basta: lì si usa quasi sempre V7, con la sensibile. Vm7 resta utile quando la linea scende verso il sesto grado o quando non si vuole chiudere.
```

La seconda frase originale contraddiceva l’elenco delle aree tonali, che indica V7 come dominante fondamentale del minore.

### Verifiche previste dopo l’applicazione

Corrispondenza dei sette blocchi con i sorgenti; ricerca di nuovo dei termini assoluti nei due volumi; presenza delle due etichette e delle ancore precedenti nell’HTML; build di Teoria con `-W --keep-going`. Nessun materiale musicale coinvolto.

### Attuazione — 14 novembre 2026

Applicati i sette blocchi senza variazioni ai testi «Dopo»: M1–M3 in `src/docs/4-scale.rst`, M4–M7 in `src/docs/6-armonia-funzionale.rst`. I due titoli modificati hanno le etichette `tristezza-dramma-instabilita` e `tonalita-minore-un-sistema-non-stabile`.

Verifiche eseguite: ogni testo «Prima» trovato una sola volta e sostituito; build HTML di Teoria con `-W --keep-going` conclusa con successo; nell’HTML sono presenti sia le ancore nuove sia quelle precedenti; nuova ricerca di «instabil», «mai definit» e «stabilizzat» accanto a «minore» nei due volumi, senza affermazioni assolute residue (resta solo la frase nuova «Mobile non vuol dire instabile»); `git diff --check`. Non verificati i formati PDF ed ePub.

## Fase B — classificazione ricavata dal riferimento — 14 novembre 2026

Stato: **proposta**, da confermare con l’autore. Nessun sorgente modificato.

Fonte: J. Bergonzi, *Inside Improvisation*, vol. 1 *Melodic Structures* (Advance Music, 1994) e vol. 2 *Pentatonics* (Advance Music), copie dell’autore, lette il 14 novembre 2026. I numeri di pagina sono quelli stampati. Da qui si ricavano **criteri, formule e procedimenti**: testo, esempi, esercizi e tabelle dei volumi non si riproducono. Nei capitoli si citerà la fonte come riferimento della suddivisione.

Le formule e le compatibilità accordali riportate sotto sono state ricontrollate con un calcolo sulle classi di altezza; tutte coincidono con la fonte.

### Vol. 1 — Strutture di quattro note

**Criterio.** Una struttura è un segmento di quattro note della scala dell’accordo, nominato con i gradi rispetto alla fondamentale dell’accordo (pp. 7–8). I numeri seguono la scala implicita: «3» e «7» di un minore sono ♭3 e ♭7; le alterazioni dell’accordo (♭9, ♭5, ♭13) si applicano ai numeri (pp. 12, 58).

**Tre strutture principali**, ciascuna è la precedente spostata di una quinta; insieme coprono l’accordo di tredicesima (pp. 58–59, 69–71, 74):

| Nome | Maggiore e dominante | Minore | Equivalenza |
|---|---|---|---|
| 1–5 | 1–2–3–5 | 1–3–4–5 | — |
| 5–9 | 5–6–7–9 (7 maggiore o minore secondo l’accordo) | 5–7–8–9 | 1–2–3–5 / 1–3–4–5 una quinta sopra |
| 9–13 | 9–10–♯11–13 | 9–11–12–13 | 1–2–3–5 / 1–3–4–5 due quinte sopra |

Varianti alterate citate: m7♭5 1–3–4–♭5 e ♭5–7–8–♭9; dominante ♭9♭13 5–♭6–7–♭9 e ♭9–10–♯11–♭13; alterato ♭5–♭6–7–♭9 (pp. 12–13, 58, 70).

**Origine.** 1–2–3–5 e 1–3–4–5 sono le due letture della stessa pila di quinte, cioè della pentatonica maggiore e della relativa minore; hanno gli stessi intervalli, una terza minore e due seconde maggiori, in ordine speculare (p. 8). È il punto di contatto fra i due volumi.

**Note da trattare.** Il 4 di maggiore e dominante e il 6 del minore sono gli unici gradi della scala esclusi da 1–5 e 5–9. Bergonzi li chiama *avoid notes* precisando che il nome è improprio: il 4 si risolve sul 3 o sul 5; il 6 del minore non richiede risoluzione ma ha un suono marcato ed è frequente sulla tonica minore (pp. 64–65).

**Strutture aggiuntive** (pp. 74–79), ciascuna con le sue 24 permutazioni:

| Nome | Maggiore e dominante | Minore | Nota |
|---|---|---|---|
| 3–7 | 3–5–6–7 | 3–4–5–7 | contiene le note guida |
| 7–11 | 7–9–10–♯11 | 7–8–9–11 | — |
| 4–8 | ♯4–6–7–8 | 4–5–6–8 | equivale a ♯11–13–14–15 / 11–12–13–15 |
| 6–3 | 6–7–1–3 | 6–1–2–3 | — |

Sono ammessi anche gli scambi 1–2–3–5 sul minore e 1–3–4–5 sul maggiore, e altre quattro note entro una quinta giusta («raggruppamenti intervallari alternativi», p. 79).

**Un segmento, molti accordi** (pp. 77–78). Do–Re–Mi–Sol è 1–2–3–5 su Cmaj7, ♭3–4–5–♭7 su Am7, ♭7–1–2–4 su Dm7, 2–5–6–7 su Fmaj7, 2–3–♭5–6 su B♭7, e così via fino agli alterati. È la generalizzazione dell’esempio S2 già pubblicato.

**Procedimenti**, nell’ordine del volume:

1. Permutazioni: 24 per struttura; si comincia da quattro, una per ciascuna nota iniziale (pp. 10–11, 63).
2. Mescolare le permutazioni pensando alla forma; evitare di partire sempre da 1 o da 5 (pp. 25–26).
3. Visualizzazione: prima l’accordo come blocco, poi la linea (pp. 31–32).
4. Immaginazione del suono (p. 37).
5. *Editing*: togliere da una a quattro note per accordo, ripetere note, per passare dalle crome continue al ritmo (pp. 39–40).
6. Centri tonali: un accordo per volta nelle progressioni dense; variare le permutazioni sugli accordi lunghi (p. 43).
7. Rivolti lineari: ogni permutazione suonata con ciascuna delle quattro note come la più grave (pp. 47–48).
8. Mescolare le strutture per ottenere una condotta più liscia, scegliendo quella che parte più vicino alla nota precedente (p. 80).

### Vol. 2 — Pentatoniche

**Definizione.** Una pentatonica è una qualsiasi scala di cinque note (pp. 9, 113). Il punto di partenza è la minore, equivalente alla relativa maggiore e generata da una pila di quinte; dal capitolo 1 in poi Bergonzi nomina le pentatoniche con il nome minore (pp. 9–11).

**Movimento nella collezione** (pp. 10–11): *step* è il passaggio alla nota successiva della collezione, qualunque sia l’intervallo; *skip* salta una nota; *double skip* e *triple skip* ne saltano due e tre. È la stessa distinzione che il nostro schema chiama «posizione nella collezione» e che l’esempio S6 descrive come «una nota sì e una no».

**Formule di quattro note** (pp. 13–14): una successione di quattro movimenti (per esempio salto giù, passo giù, salto su, passo giù) ripetuta partendo dalle note successive. Dalle rotazioni del disegno e dalla sua inversione si ottengono otto formule; la linea torna alla nota di partenza dopo cinque gruppi. Altre formule con salti doppi nel cap. 7 (pp. 73–75).

**Variazione ritmica** (pp. 27–28): le stesse linee con figure ritmiche diverse, pause e sincopi.

**Pentatoniche sugli accordi** (pp. 29–31): la pentatonica minore di Do si usa su Cm7, E♭maj7, Fm7, A♭maj7, B♭m7, D♭maj7, A7alt, E♭7. Su un m7 dorico tre scelte: pentatonica minore sulla fondamentale, sulla quinta, sulla seconda; analogamente su maj7. Non valgono su m7♭5 e dominante, che richiedono altri tipi.

**Tipi**, tutti ottenuti dalla minore cambiando una nota (capp. 6, 8–11):

| Tipo | Formula | Esempio | Accordi indicati (selezione) | Pagine |
|---|---|---|---|---|
| Minore 7 | 1–♭3–4–5–♭7 | Do–Mi♭–Fa–Sol–Si♭ | Cm7, E♭maj7, Fm7, A7alt | 29 |
| Minore 6 | 1–♭3–4–5–6 | Do–Mi♭–Fa–Sol–La | C-6, F7, Aø, B7alt, E♭maj7♯11 | 53 |
| Maggiore ♭6 | 1–2–3–5–♭6 | Mi♭–Fa–Sol–Si♭–Do♭ | A♭m(maj7), G7alt, D♭7♯11, Fø♮9 | 79 |
| Minore 7♭5 | 1–♭3–4–♭5–♭7 | Do–Mi♭–Fa–Sol♭–Si♭ | Cø, E♭-6, A♭7, D7alt | 87 |
| Maggiore ♭2 | 1–♭2–3–5–6 | Do–Re♭–Mi–Sol–La | C7, E♭7, F♯7, A7 (dominanti a distanza di terza minore) | 95 |
| Esatonale | 1–3–♯4–♯5–♭7 | Si–Mi♭–Fa–Sol–La, cioè la minore 6 di Do con la fondamentale abbassata di un semitono | Cm(maj7), F7♯11, B7alt | 105 |

Il cap. 12 aggiunge altre collezioni di cinque note senza nome, a conferma della definizione generale (p. 113).

**Poli-pentatoniche** (pp. 115–117): rispetto a una pentatonica «madre», il grado di uscita dipende dal numero di note comuni. Per la minore di Do: nessuna nota comune con Si, Do♯, Fa♯ minore; una con La♭ e Mi; due con Mi♭ e La; tre con Si♭ e Re; quattro con Fa e Sol. Esercizio: alternare gruppi di quattro note fra madre e pentatonica esterna, collegandoli con la nota più vicina. Gli studi `modern-05` e `modern-06` già pubblicati ne sono un caso particolare.

### Ripartizione proposta fra Teoria e Pratica

Criterio già in uso nei due volumi: Teoria spiega formule e relazioni; Pratica le porta sulla tastiera con esempi, procedure e verifiche. Ogni concetto ha una sola sede principale; l’altra rimanda.

**Teoria**

| Sede | Contenuto nuovo |
|---|---|
| T4, «Scala pentatonica» | Definizione generale (cinque note qualsiasi); pila di quinte; i sei tipi come alterazioni di una nota della minore, con formule; quali hanno semitoni; le due letture maggiore/minore della stessa collezione |
| T5, estensioni | I gradi dell’accordo di tredicesima come tre segmenti di quattro note sovrapposti per quinte (1–5, 5–9, 9–13); equivalenze per trasposizione |
| T5 o T6 | Le note «da trattare»: 4 su maggiore e dominante, 6 sul minore, con il motivo intervallare (semitono dal 3, tritono dal ♭3) |
| T10, «Pentatoniche sovrapposte» | Compatibilità pentatonica–accordo come lettura dei gradi; poli-pentatoniche e grado di uscita misurato in note comuni |
| T12 | Rimando: l’*editing* coincide con la frammentazione già trattata; nessun testo nuovo |

**Pratica**

| Sede | Contenuto nuovo |
|---|---|
| Strutture melodiche, sezione 3 «Famiglie di strutture» | Le tre strutture principali e le aggiuntive, con esempi originali su Do; scelta di quattro permutazioni; rivolti lineari; mescolare strutture per condotta; un segmento su molti accordi (sviluppo di S2) |
| Strutture melodiche, sezioni 4–5 | Restano; si aggiunge il rimando all’*editing* come procedimento esplicito |
| **Nuova pagina «Pentatoniche»** dopo Strutture melodiche | Passo e salto (anche doppio e triplo) come notazione; formule di quattro movimenti; variazione ritmica; scelta della pentatonica sull’accordo; i tipi alterati sulla tastiera; poli-pentatoniche come prosecuzione verso `modern-05` e `modern-06` |
| Strutture melodiche, sezione 7 | Si sposta nella nuova pagina con l’esempio S6; resta un rimando |
| Scale, mappe delle pentatoniche | Restano; rimando alla nuova pagina |
| Strumenti (fase D) | Pentatoniche e strutture come nuovi materiali dello strumento Scale; da valutare dopo la stesura |

### Terminologia proposta

- *grouping* → **struttura** (già in uso nel volume); le tre principali **1–5**, **5–9**, **9–13**.
- *avoid note* → **nota da trattare**, seguendo la precisazione della fonte.
- *step*, *skip*, *double skip* → **passo**, **salto**, **salto doppio**.
- *editing* → **togliere note**, senza termine inglese.
- *poly-pentatonics* → **poli-pentatoniche**; *parent* → **pentatonica di partenza**.
- Nomi dei tipi: proposta di usare la formula (minore 6, maggiore ♭6, minore 7♭5, maggiore ♭2, esatonale), come nella fonte.

### Decisioni richieste all’autore

1. ~~La ripartizione Teoria/Pratica sopra.~~ **Approvata dall’autore il 14 novembre 2026.**
2. ~~Nuova pagina «Pentatoniche» in Pratica, dopo Strutture melodiche, con la sezione 7 spostata.~~ **Approvata con la ripartizione.**
3. ~~Nome delle pentatoniche.~~ **Deciso:** entrambi i nomi alla prima occorrenza, poi il nome minore.
4. ~~Strutture aggiuntive.~~ **Deciso:** tutte e quattro in tabella di consultazione; esempio solo per 3–7.
5. ~~Ordine di lavoro.~~ **Deciso:** prima Teoria, poi Pratica.

### Fase B — testi proposti per Teoria

Stato: **approvato dall’autore e applicato** il 14 novembre 2026 (vedi «Attuazione in Teoria» in fondo). Gli esempi sono originali; formule, gradi e note comuni sono stati ricontrollati con un calcolo sulle classi di altezza. T12 non cambia: «togliere note» coincide con la frammentazione già spiegata in «Sviluppare una cellula», e il rimando verso Pratica esiste già.

#### BT1 — T4, «Che cos’è davvero»: definizione generale

Prima:

```rst
“Pentatonica” significa semplicemente “a cinque suoni”. Le due famiglie più usate sono:
```

Dopo:

```rst
“Pentatonica” significa semplicemente “a cinque suoni”: qualsiasi scala di cinque note è una pentatonica. Le due più usate, e il punto di partenza per tutte le altre, sono:
```

#### BT2 — T4, dopo «Maggiore e minore… e il trucco più utile»: nomi e pentatoniche alterate

Aggiunta dopo il paragrafo che termina con «è il centro che ci metti tu.»:

```rst
Nei due volumi useremo entrambi i nomi alla prima occorrenza, per esempio «La minore pentatonica (= Do maggiore pentatonica)», e poi il nome minore. Il motivo è pratico: le altre pentatoniche si descrivono più facilmente come modifiche della minore.

Altre pentatoniche: cambiare una nota
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Se nella minore pentatonica cambi una sola nota, ottieni collezioni nuove, ciascuna con un suono proprio. Partendo da Do minore pentatonica, Do–Mi♭–Fa–Sol–Si♭:

.. list-table::
   :header-rows: 1

   * - Nome
     - Cosa cambia
     - Note
     - Formula
   * - Minore 6
     - Si♭ diventa La
     - Do–Mi♭–Fa–Sol–La
     - 1–♭3–4–5–6
   * - Minore 7♭5
     - Sol diventa Sol♭
     - Do–Mi♭–Fa–Sol♭–Si♭
     - 1–♭3–4–♭5–♭7
   * - Maggiore ♭6
     - Do diventa Do♭
     - Mi♭–Fa–Sol–Si♭–Do♭
     - 1–2–3–5–♭6 da Mi♭
   * - Maggiore ♭2
     - Fa diventa Mi
     - Mi♭–Mi–Sol–Si♭–Do
     - 1–♭2–3–5–6 da Mi♭
   * - Esatonale
     - nella minore 6, Do scende a Si
     - Si–Mi♭–Fa–Sol–La
     - 1–3–♯4–♯5–♭7 da Si

La minore 6 e l'esatonale restano senza semitoni; minore 7♭5, maggiore ♭6 e maggiore ♭2 ne contengono uno. È la conferma pratica di quanto detto sopra: il nome indica cinque note, non un unico comportamento.

Questa classificazione segue quella di Jerry Bergonzi, *Inside Improvisation*, vol. 2, *Pentatonics*. Su quali accordi si usano queste collezioni lo vediamo in :doc:`10-armonia-non-funzionale`; sulla chitarra, nella pagina «Pentatoniche» del volume di Pratica.
```

Il rimando a Pratica sarà aggiunto quando la pagina esisterà, per non puntare a contenuti assenti.

#### BT3 — T5, prima di «Una chiave di lettura»: tre segmenti e note da trattare

Aggiunta:

```rst
Tre segmenti di quattro note
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Le note di un accordo di tredicesima, ordinate per gradi, si possono dividere in tre gruppi di quattro note che si sovrappongono:

.. list-table::
   :header-rows: 1

   * - Segmento
     - Maggiore e dominante
     - Minore
   * - 1–5
     - 1–2–3–5
     - 1–3–4–5
   * - 5–9
     - 5–6–7–9
     - 5–7–8–9
   * - 9–13
     - 9–10–♯11–13
     - 9–11–12–13

I numeri seguono la scala dell'accordo: su un minore 3 e 7 sono ♭3 e ♭7, su un dominante 7 è ♭7. 8, 10 e 12 sono fondamentale, terza e quinta all'ottava superiore.

Ogni segmento è il precedente spostato di una quinta. Su Cmaj7, 5–6–7–9 è Sol–La–Si–Re, cioè 1–2–3–5 di Sol; 9–10–♯11–13 è Re–Mi–Fa♯–La, 1–2–3–5 di Re. Sul minore vale lo stesso con 1–3–4–5: su Cm7, 5–7–8–9 è Sol–Si♭–Do–Re, 1–3–4–5 di Sol minore.

1–2–3–5 e 1–3–4–5 hanno gli stessi intervalli in ordine rovesciato: due seconde maggiori e una terza minore, oppure una terza minore e due seconde maggiori. Sono le due letture della stessa pentatonica, maggiore e relativa minore (vedi :doc:`4-scale`).

**Note da trattare.** In maggiore e dominante l'unico grado della scala che resta fuori da 1–5 e 5–9 è il 4. Dista un semitono dalla terza: tenuto a lungo contrasta con l'accordo e di solito scende sul 3 o sale sul 5. La ♯11 non ha lo stesso problema, perché sopra la terza forma una nona maggiore, non minore. Nel minore il grado escluso è il 6 della scala dorica: forma un tritono con la ♭3 e richiama un colore di dominante, ma non chiede di risolvere ed è frequente sulla tonica minore, come in Cm6.

Questa divisione segue Jerry Bergonzi, *Inside Improvisation*, vol. 1, *Melodic Structures*. Come usarla sulla chitarra è spiegato nella pagina `Strutture melodiche e costruzione della frase <https://appunti-pratica-per-chitarra-jazz.readthedocs.io/it/latest/strutture-melodiche.html>`__ del volume di Pratica.
```

#### BT4 — T10, «Pentatoniche sovrapposte»: scelta sull’accordo e note comuni

Aggiunta dopo il paragrafo che termina con «Una diteggiatura familiare non rende automaticamente adatta una scala.»:

```rst
Su un accordo minore settima con funzione dorica hai almeno tre pentatoniche minori: sulla fondamentale, sulla quinta e sulla seconda. Su Dm7, Re minore pentatonica dà 1–♭3–4–5–♭7, La minore 5–♭7–1–9–11, Mi minore 9–11–5–13–1. La prima contiene la terza; le altre due la lasciano all'accompagnamento e aggiungono tensioni. Su un accordo maggiore settima vale lo stesso: su Cmaj7, La minore dà 6–1–2–3–5, Mi minore 3–5–6–7–9, Si minore 7–9–3–♯11–13, cioè il colore lidio.

Su semidiminuiti e dominanti questa scelta non basta: servono le pentatoniche alterate di :doc:`4-scale`. Alcuni esempi: Do minore 6 su F7 dà 5–♭7–1–9–3; Do minore 7♭5 su A♭7 dà 3–5–13–♭7–9; Mi♭ maggiore ♭2 su C7 dà ♯9–3–5–♭7–1; Si esatonale su F7♯11 dà ♯11–♭7–1–9–3.

Quanto una pentatonica suona lontana da un'altra si può misurare contando le note comuni. Rispetto a Mi minore pentatonica:

.. list-table::
   :header-rows: 1

   * - Note comuni
     - Pentatoniche minori
   * - 4
     - La, Si
   * - 3
     - Re, Fa♯
   * - 2
     - Do♯, Sol
   * - 1
     - Do, La♭
   * - 0
     - Mi♭, Fa, Si♭

Meno note comuni ci sono, più l'uscita è evidente. Il side-slip della sezione seguente passa da Mi minore a Fa minore pentatonica: nessuna nota in comune, ed è per questo che lo spostamento si riconosce subito. Alternare una pentatonica di partenza e una lontana si chiama a volte **poli-pentatonica**.
```

Verifiche già eseguite sulle proposte: tutte le formule e i gradi indicati; semitoni presenti o assenti nei cinque tipi; note comuni fra Mi minore pentatonica e le altre undici.

#### Attuazione in Teoria — 14 novembre 2026

Applicati BT1 e BT2 in `4-scale.rst`, BT3 in `5-accordi.rst`, BT4 in `10-armonia-non-funzionale.rst`, con i testi «Dopo» invariati salvo un punto: in BT2 è stata tolta la frase sul volume di Pratica («sulla chitarra, nella pagina “Pentatoniche”…»), perché la pagina non esiste ancora. Va aggiunta quando la pagina sarà scritta.

Verifiche eseguite: ogni punto di inserimento trovato una sola volta; build HTML di Teoria con `-W --keep-going` conclusa con successo; nell’HTML presenti le nuove sezioni «Altre pentatoniche: cambiare una nota» e «Tre segmenti di quattro note» con le loro tabelle e la tabella delle note comuni in T10; `git diff --check`. Non verificati PDF ed ePub.

Prossimo passo: Pratica, cioè la sezione 3 «Famiglie di strutture» di Strutture melodiche e la nuova pagina «Pentatoniche», con lo spostamento della sezione 7 e dell’esempio S6.

### Fase B — attuazione in Pratica — 14 novembre 2026

Dopo l’approvazione della ripartizione e delle tre scelte (nomi, strutture aggiuntive, ordine), scritta la parte di Pratica.

**Strutture melodiche** (`src/docs/strutture-melodiche.rst`)

- Nuova sezione 3 «Famiglie di strutture» (`strutture-famiglie`): tre strutture principali con tabella; «Scegliere le permutazioni»; «Rivolti lineari»; «Mescolare le strutture»; «Note da trattare»; «Una struttura, molti accordi» (Do–Re–Mi–Sol su sei accordi); «Strutture aggiuntive» con tabella di 3–7, 7–11, 4–8, 6–3 ed esempio solo per 3–7. Citazione di Bergonzi, vol. 1, e rimando a Teoria 5.
- Nuovi esempi: S7 (tre strutture su Cmaj7), S8 (su Cm7), S9 (quattro permutazioni), S10 (rivolti lineari di 2–5–3–1), S11 (strutture mescolate su II–V–I, con base), S12 (3–7 su Cmaj7 e Cm7).
- Sezione 5: aggiunto il paragrafo su «togliere note».
- Sezione 7 ridotta a «Le pentatoniche», con l’etichetta `strutture-pentatoniche` conservata e il rimando alla nuova pagina; il testo sul movimento nella collezione e l’esempio S6 sono passati alla pagina Pentatoniche.
- «Come usare la pagina» e «Dove proseguire» aggiornati.

**Nuova pagina** `src/docs/pentatoniche.rst`, nel toctree dopo `strutture-melodiche`

- Sezioni: «Passo e salto» (con S6), «Formule di quattro note» (P1: formula *passo su, salto su, passo giù* su La minore pentatonica), «Scegliere la pentatonica sull’accordo» (P2: Re, La, Mi minore su Dm7, con base), «Pentatoniche alterate» (tabella e P3: Si♭ maggiore ♭2 su G7 in un II–V–I, con base), «Poli-pentatoniche» (esercizio sulla base di P2, rimando a `modern-05` e `modern-06`), «Una frase tua», riquadro «Brano guida», «Dove proseguire». Citazione di Bergonzi, vol. 2.
- La formula di P1 è originale, diversa da quelle del volume di riferimento.
- Nello spartito di P3 la didascalia del G7 è «pentatonica alterata»: il segno ♭ nelle didascalie di LilyPond veniva spaziato male; il nome compare nel testo.

**Rimandi**: dal capitolo Scale di Pratica, prima delle mappe pentatoniche; da Teoria 4, «Altre pentatoniche: cambiare una nota» (la frase tolta in BT2 è stata ripristinata con l’URL della pagina).

**Generatore e test**: `generate_melodic_structures.py` descrive ora gli esempi con etichetta e nome file (`strutture-NN`, `pentatoniche-NN`); i sorgenti di S1–S6 sono rimasti identici. Ventiquattro nuovi sorgenti compilati. `tests/test_melodic_structures.py` riscritto: 16 test, fra cui gradi di S7–S8 e spostamento per quinta, una permutazione per nota iniziale in S9, nota più grave dei rivolti in S10, note comuni in S11, formula e collezione di P1, pentatoniche di P2, Si♭ maggiore ♭2 e risoluzione Fa–Mi in P3, corrispondenza fra risorse generate e riferimenti delle due pagine.

Verifiche eseguite: suite `unittest` di Pratica, 54 test superati; build HTML di Pratica e Teoria con `-W --keep-going` concluse con successo; presenza nell’HTML di tutte le risorse SVG e MP3 referenziate; controllo visivo degli spartiti S10, P1 e P3. Ricontrollati con un calcolo i gradi citati nel testo (fra cui Do–Re–Mi–Sol sui sei accordi, Re minore 6 e Si♭ maggiore ♭2 su G7, Mi minore 6 su A7, note comuni con Sol minore). Corretto prima della pubblicazione un rimando allo strumento Scale, che non contiene le pentatoniche. Non verificati: ascolto completo degli audio, PDF ed ePub.
