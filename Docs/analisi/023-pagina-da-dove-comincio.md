# Analisi — Pagina «Da dove comincio» (INT-10)

- Data: 2026-11-14
- Stato: approvato dall’autore e attuato il 14 novembre 2026.
- Ambito e richiesta: INT-10 del `PIANO_MIGLIORAMENTO.md` e §8 della [proposta di revisione integrata](022-revisione-integrata-quadro-generale.md): una pagina che orienti fra obiettivi, con tre ingressi e un percorso minimo fatto di materiale esistente. Solo Pratica e Teoria; il rimando da Repertorio (R1) previsto dal piano resta fuori, perché Repertorio è fuori ambito.

## Problema e risultato atteso

Il volume offre molto materiale e nessuna indicazione di cosa basta per cominciare. L’audit del lettore lo segnalava come causa di abbandono a metà Pratica. In Teoria 1 la frase «Non c’è un ordine obbligato» è stata tolta con il taglio B2 di INT-07, rinviando la questione a questa pagina.

Risultato atteso: il lettore sceglie un obiettivo, sa quali sezioni studiare e in che ordine, e sa riconoscere quando ha finito il primo giro. Non deve leggere i capitoli per intero né in sequenza.

## Evidenze

- **Ingressi già decisi** (proposta integrata, §8): costruire una frase, accompagnare una progressione, sostenere una melodia con gli accordi.
- **Materiale disponibile per ciascun ingresso**, con etichette o titoli verificati nei sorgenti:
  - frase: Scale, «Scala maggiore» e «Dal pattern a una frase»; Arpeggi, esercizio 8 «Dall’arpeggio alla frase»; `strutture-melodiche` (percorso essenziale); `progressioni-ii-v-i`, «Improvvisare: scegliere note bersaglio»;
  - accompagnamento: `shell-voicings`; `progressioni-ii-v-i`, «Accompagnare: attacchi e silenzi»; `progressioni-blues`; `strumenti-progressioni`;
  - melodia con accordi: `shell-voicings`; «Vocabolario avanzato» (nota al canto), `vocabolario-accordi-minori` e `vocabolario-accordi-dominanti`; `chord-melody-voicings`; `progressioni-aaba`.
- **Base comune**: Le basi, sezione `basi-musica` («Il tempo prima delle note»); pagina `leggere-gli-esempi`.
- **Già presenti**: la mappa del capitolo Le basi in tre parti; il brano guida AABA con i riquadri «Brano guida»; «Come usare la pagina» in Strutture melodiche. La nuova pagina li richiama, non li ripete.
- **Teoria 1**, «Come leggerli… e quando chiuderli per prendere la chitarra»: dopo il taglio B2 non dà più indicazioni d’ordine. È il punto naturale per il rimando.

## Dipendenze e impatto

| Sede | Intervento |
|---|---|
| `src/docs/da-dove-comincio.rst` (nuovo) | La pagina, testo sotto |
| `src/docs/index.rst` | Toctree: subito dopo `1-introduzione`, prima di `leggere-gli-esempi` |
| Pratica 1, fine di «Perché questi appunti esistono» | Una frase di rimando, accanto al glossario |
| Teoria 1, «Come leggerli» | Una frase di rimando con URL del sito di Pratica |

Nessun materiale musicale, nessun generatore, nessuna etichetta esistente modificata. Il titolo della pagina non entra in conflitto con etichette esistenti (`da-dove-comincio` non è usata).

## Alternative e criteri di confronto

| Alternativa | Vantaggio | Limite | Valutazione |
|---|---|---|---|
| Lasciare l’orientamento all’Introduzione | Nessuna pagina in più | L’Introduzione è già lunga e parla di metodo, non di percorsi | Non risolve |
| Sezione in fondo all’Introduzione | Un solo file | Si perde fra prefazione e patto; non è raggiungibile dall’indice come voce propria | Possibile, meno visibile |
| Pagina autonoma breve | Voce propria nell’indice, raggiungibile da Teoria | Una pagina in più da mantenere quando cambiano i capitoli | Raccomandata |

## Raccomandazione

Pagina autonoma breve, circa 500 parole, con il testo proposto sotto. Ogni ingresso ha quattro tappe, un criterio per dire «basta» e un’indicazione su dove proseguire. I rimandi puntano a etichette e titoli esistenti; nessun contenuto assente.

### Testo proposto per `src/docs/da-dove-comincio.rst`

```rst
.. _da-dove-comincio:

Da dove comincio
================

Questo volume non va letto dall'inizio alla fine. Scegli che cosa vuoi saper fare fra qualche settimana e segui uno dei tre percorsi qui sotto. Ognuno usa poche sezioni, in un ordine preciso, e finisce con una verifica: quando la superi, il primo giro è fatto.

Prima di tutto, per ogni percorso
---------------------------------

- Leggi :doc:`leggere-gli-esempi`: le convenzioni di spartiti, tablature e audio valgono per tutto il volume.
- Studia :ref:`i principi musicali <basi-musica>` del capitolo Le basi, a partire da «Il tempo prima delle note». Tornaci quando un esercizio ti sembra corretto ma non suona.

Il resto del capitolo Le basi si consulta quando serve: la mappa all'inizio del capitolo ti dice come.

Costruire una frase
-------------------

#. :doc:`4-scale`: la scala maggiore in una posizione, poi l'esercizio «Dal pattern a una frase».
#. :doc:`5-arpeggi`: l'arpeggio di Cmaj7 e l'esercizio 8, «Dall'arpeggio alla frase».
#. :doc:`strutture-melodiche`: il percorso essenziale indicato all'inizio della pagina.
#. :ref:`progressioni-ii-v-i`: «Improvvisare: scegliere note bersaglio».

**Basta quando** sai suonare due giri di II–V–I in Do sulla base di :ref:`strutture-due-accordi`, arrivando sulla nota che avevi scelto e lasciando almeno una pausa per giro.

**Poi:** :doc:`8-licks`, a partire dalle frasi sulle progressioni.

Accompagnare una progressione
-----------------------------

#. :ref:`shell-voicings`: fondamentale, terza e settima sulle corde 6–4–3 e 5–4–3.
#. :ref:`progressioni-ii-v-i`: «Accompagnare: attacchi e silenzi».
#. :ref:`progressioni-blues`: dodici battute con gli stessi voicing.
#. Lo strumento :ref:`Progressioni <strumenti-progressioni>`, per ripetere le griglie in altre tonalità.

**Basta quando** accompagni il blues in Do per tre giri senza fermarti, con le terze e le settime che si muovono il meno possibile fra un accordo e l'altro.

**Poi:** le altre griglie di :doc:`7-progressioni` e lo :ref:`studio in AABA <progressioni-aaba>`.

Sostenere una melodia con gli accordi
-------------------------------------

#. :ref:`shell-voicings`, come nel percorso precedente.
#. «Vocabolario avanzato» in :doc:`6-accordi`: scegli una sola famiglia, per esempio :ref:`vocabolario-accordi-minori`, e lavora sulla nota al canto.
#. :ref:`chord-melody-voicings`: drop 2, drop 3 e voicing a tre voci sotto una melodia.
#. «Mettere tutto insieme: otto battute», alla fine di :ref:`chord-melody-voicings`: un piccolo arrangiamento completo.

**Basta quando** suoni le otto battute dell'arrangiamento senza fermarti, con la melodia che si sente sopra gli altri suoni.

**Poi:** :ref:`vocabolario-accordi-dominanti`; quindi la sezione A dello :ref:`studio in AABA <progressioni-aaba>`, scegliendo tu una melodia di una nota per battuta, come propone il riquadro «Brano guida» del capitolo Accordi.

Dopo il primo giro
------------------

Puoi cambiare percorso o fare il secondo: i tre si incrociano su Progressioni e sullo studio in AABA. :doc:`9-modern-jazz-fusion` e :doc:`10-percorsi-autore` presuppongono almeno uno dei tre percorsi completato.

Se vuoi capire perché qualcosa funziona, nel volume di Teoria i capitoli Intervalli, Scale e Accordi accompagnano il primo percorso, Armonia funzionale il secondo e il terzo.
```

### Rimandi proposti

**Pratica 1**, dopo il paragrafo del glossario:

```rst
Se non sai da quale capitolo partire, :doc:`da-dove-comincio` propone tre percorsi brevi, ciascuno con una verifica finale.
```

**Teoria 1**, in «Come leggerli», dopo l’elenco «prima il suono, poi le parole, poi di nuovo il suono»:

```rst
Se cerchi un ordine per cominciare a suonare, la pagina `Da dove comincio <https://appunti-pratica-per-chitarra-jazz.readthedocs.io/it/latest/da-dove-comincio.html>`__ del volume di Pratica propone tre percorsi brevi.
```

### Punti verificati nei sorgenti

- `progressioni-blues` è in **Do** (C7, F7, G7): il criterio del secondo percorso usa Do. Gli shell coprono C7 e le altre dominanti (tabella «Le note che definiscono la sonorità»).
- Lo studio in AABA (`progressioni-15-aaba`) contiene **solo shell voicing**, senza melodia scritta; la sezione A dura otto battute. Il terzo percorso non lo usa come verifica: lo propone come prosecuzione, con una melodia scelta dal lettore, come già fa il riquadro «Brano guida» di Accordi.
- «Mettere tutto insieme: otto battute» è l’ultima sottosezione di `chord-melody-voicings` (`cm-arrangiamento`, con spartito e audio): diventa la quarta tappa e la verifica del terzo percorso.

### Decisioni richieste all’autore

- Collocazione nell’indice: dopo l’Introduzione (proposta) oppure prima.
- I tre criteri «Basta quando»: livello di richiesta adeguato o da alleggerire.
- Tono: la pagina usa la seconda persona e frasi brevi, come le parti riscritte del volume.

## Piano di verifica ed eventuale attuazione

Dopo la conferma: scrivere la pagina e i due rimandi; build di Pratica e Teoria con `-W --keep-going`; controllo che ogni `:ref:` e `:doc:` risolva e che la pagina compaia nell’indice. Criterio di accettazione dal piano: la pagina esiste, è raggiungibile dall’indice di Pratica e da Teoria 1, e non rimanda a contenuti assenti.

## Attuazione — 14 novembre 2026

Confermata dall’autore la proposta così com’è, inclusa la collocazione dopo l’Introduzione.

- `src/docs/da-dove-comincio.rst` con il testo proposto, senza variazioni; voce nel toctree fra `1-introduzione` e `leggere-gli-esempi`.
- Rimando in Pratica 1, dopo il paragrafo del glossario; rimando in Teoria 1, «Come leggerli», dopo l’elenco «prima il suono…».

Verifiche eseguite: tutti i `:ref:` e `:doc:` della pagina risolti (build di Pratica con `-W --keep-going` conclusa con successo); pagina presente nell’indice e collegata da Pratica 1; build di Teoria con `-W --keep-going` conclusa con successo; suite `unittest` di Pratica (46 test) superata; `git diff --check`. Criterio di accettazione INT-10 soddisfatto per Pratica e Teoria; il rimando da Repertorio resta fuori ambito. Non verificati PDF ed ePub.
