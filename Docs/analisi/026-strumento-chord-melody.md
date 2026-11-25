# Analisi 026 — Strumento Chord melody

- Data: 25 novembre 2026.
- Stato: decisa con l'utente il 25 novembre 2026 (sotto, «Raccomandazione»); passo 1 (rilascio 1a
  dello strumento) attuato il 25 novembre 2026 sul ramo `strumento-chord-melody` di
  appunti-strumenti, da approvare; passi 2–4 da fare. Nessuna modifica al volume.
- Ambito e richiesta: l'utente chiede di valutare una sezione nuova in Strumenti dedicata al chord
  melody, con esercizi mirati. Ambito: appunti-strumenti (strumento nuovo,
  [ADR 0018](../../../appunti-strumenti/Docs/ADR-0018-strumento-chord-melody.md)), Pratica
  (capitolo 11, rimandi dal capitolo 6 e dal percorso Joe Pass), Teoria (solo note di rilascio, se
  si aggiunge un rimando dal capitolo 8). Repertorio escluso.

## Problema e risultato atteso

La sezione «Voicing per il chord melody» del capitolo 6 (`chord-melody-voicings`, analisi 018)
insegna a scegliere l'accordo **sotto la nota della melodia**, ma non ha uno strumento che la
accompagni: chi studia non può esercitarsi in ogni tonalità né su griglie diverse da quelle degli
esempi. Risultato atteso: uno strumento che generi melodie sulle griglie del volume, le armonizzi
con le famiglie del capitolo e guidi lo studio con le procedure del capitolo («prima la melodia,
poi il basso, poi gli accordi»).

## Evidenze

Fatti osservati:

- Capitolo 6, sezione `chord-melody-voicings`: undici esempi `cm-*` (drop 2 su 4–3–2–1 per maj7, 6,
  7, m7, m7♭5; II–V–I con melodia Do–Si–Si–La; drop 3; tre voci; diminuiti di passaggio; sesta
  diminuita; arrangiamento di otto battute) da `scripts/generate_chord_melody.py`, verificati da
  `tests/test_chord_melody.py`.
- Le tre voci di `cm-tre-voci` e `cm-arrangiamento` usano le corde 5-3-2, 6-3-2, 5-3-1 e 6-5-1:
  basso di fondamentale, nota guida nel mezzo, melodia sulla 2ª o 1ª corda.
- Lo strumento Accordi genera dieci famiglie (ADR 0015) ma non la forma a tre voci; l'ADR 0012
  rimanda «nota al canto fissa» e «tre voci del chord melody».
- Capitolo 11: nessun esercizio pronto sul chord melody.
- Nel codice degli strumenti: ogni voicing ha già il campo `top`; conduzione delle voci (Viterbi),
  griglie e linea del tempo, gironi di celle con seme, parti audio con volume proprio. La velocity
  è per evento.

Inferenze: circa due terzi del motore esistono; il lavoro nuovo è la sorgente della melodia,
l'armonizzazione nota per nota e la famiglia a tre voci.

Informazioni mancanti: la qualità musicale delle armonizzazioni generate si valuta solo
all'ascolto dell'utente.

## Dipendenze e impatto

- **appunti-strumenti**: pagina e moduli nuovi; `voicings.js` (filtro sulla nota al canto,
  famiglia `trio`, anche in Accordi), parte audio `melody`, link. Dettagli nell'ADR 0018.
- **Capitolo 6**: tabella delle famiglie (riga «Tre voci»); la frase «ogni forma degli esempi di
  questa pagina si ritrova fra quelle che lo strumento genera» diventa vera anche per `cm-tre-voci`;
  rimando allo strumento dalla sezione `chord-melody-voicings`.
- **Capitolo 11**: sezione «Chord melody» con esercizi pronti; nella sezione «Accordi» il conteggio
  passa da dieci a undici famiglie.
- **Percorso Joe Pass** (`autori/` e capitolo 10): rimando facoltativo.
- **Test del volume**: `tests/test_strumenti_links.py` per i link nuovi; un test di coerenza fra
  gli esempi `cm-*` e i voicing generati, come per le famiglie `vf-*` (analisi 024).
- **Nessun nuovo LilyPond** necessario: gli esempi esistono.
- **Note di rilascio**: i tre volumi e appunti-strumenti.

## Alternative e criteri di confronto

| Alternativa | Coerenza didattica | Costo | Esito |
|---|---|---|---|
| Stato attuale (nessuno strumento) | la sezione resta senza pratica guidata | nullo | scartata |
| Asse «nota al canto» in Accordi | copre la Verifica, non la melodia nel tempo | basso | scartata; il filtro va comunque nel nucleo |
| Strumento nuovo, melodie generate | ogni griglia e tonalità; melodie meno cantabili | alto, come Progressioni | **scelta** |
| Strumento nuovo, melodie originali scritte a mano | melodie migliori, poche | medio, più lavoro d'autore | rimandata |
| Melodia inserita dall'utente | la più vicina all'arrangiare un brano | il più alto (editor) | rimandata |
| Melodie degli standard | — | — | esclusa per i diritti |

## Raccomandazione

Decisioni dell'utente del 25 novembre 2026:

1. strumento nuovo della suite (`chord-melody.html`);
2. melodie generate sulle griglie (nota comune, note guida, toni dell'accordo, toni con passaggio,
   sesta diminuita), con ritmo da celle a gironi;
3. famiglia «Tre voci» anche nello strumento Accordi;
4. nella prima versione tutti i gruppi di esercizi (nota al canto, melodia su griglia, diminuiti,
   tre voci e arrangiamento), in due rilasci: 1a senza note di passaggio, 1b con diminuiti e
   arrangiamento.

Limiti: le melodie generate servono a esercitare la tecnica, non sostituiscono un tema; per il
passo «dal vocabolario al brano» il capitolo resta il riferimento.

## Piano di verifica ed eventuale attuazione

1. **Strumenti, rilascio 1a**: filtro sulla nota al canto e famiglia `trio` in `voicings.js` con
   test; linee `common`, `guide`, `tones`; armonizzatore; pagina, pannello, link; parte `melody`.
   Criteri: i casi di prova dell'ADR 0018 (punto 12), Accordi invariato tranne la famiglia nuova,
   verifica nel browser a 1280 e 375 px.
2. **Ascolto dell'utente** del rilascio 1a.
3. **Strumenti, rilascio 1b**: note di passaggio, diminuiti, famiglia «misto», arrangiamento.
4. **Volume**: sezione nel capitolo 11, rimandi nel capitolo 6, tabella delle famiglie, test dei
   link e di coerenza con gli esempi `cm-*`, note di rilascio dei tre volumi; build HTML con `-W`.

Rischi: armonizzazioni corrette ma poco musicali (mitigato dal rilascio in due tempi e
dall'ascolto); salti di corda scomodi nelle tre voci (costo di suonabilità, verifica a campione);
dimensione del lavoro, paragonabile a Progressioni.
