# Analisi — Correzioni concettuali e sezione sulle strutture melodiche

- Data: 14 novembre 2026.
- Stato: fase A approvata e applicata ai sorgenti di Teoria il 14 novembre 2026; schema della pagina melodica proposto, classificazione da verificare.
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

Attuazione di Teoria registrata su `main` nel commit `223ad65`. Documentazione predisposta per commit su `main` di Pratica. Il push di Teoria è stato tentato il 14 novembre 2026 ed è bloccato dalla mancata risoluzione di `github.com`; lo stato di sincronizzazione va verificato con Git prima di considerare pubblicate le modifiche.
