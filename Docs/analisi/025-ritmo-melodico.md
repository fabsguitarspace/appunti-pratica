# Analisi 025 — Ritmo melodico: pagina del volume e strumento Ritmi

- Data: 22 novembre 2026.
- Stato: attuata il 22 novembre 2026 sui rami `ritmo-melodico` (Pratica e Teoria) e
  `strumento-ritmi` (appunti-strumenti); da approvare, niente commit né pubblicazione.
- Ambito: Pratica (pagina nuova, capitolo 11, rimandi), appunti-strumenti (strumento nuovo,
  [ADR 0016](../../../appunti-strumenti/Docs/ADR-0016-strumento-ritmi.md)), Teoria (rimandi).
- Fonte dei procedimenti: Jerry Bergonzi, *Inside Improvisation*, vol. 4, *Melodic Rhythms*
  (Advance Music), PDF dell'utente.

## Problema e risultato atteso

L'utente osserva che i volumi non hanno una trattazione approfondita e mirata sul ritmo applicato
alla melodia, non solo all'accompagnamento, e chiede di ispirarsi al metodo di Bergonzi per una
sezione del volume e per uno strumento dedicato, allo stesso livello di Scale, Arpeggi, Accordi e
Progressioni.

## Che cosa c'era

- Teoria, capitolo 12 «Ritmo e sviluppo del materiale»: definizioni (pulsazione, suddivisione,
  swing, groove, spostamento, gruppi di tre, metri dispari, poliritmia, modulazione metrica,
  sviluppo di una cellula). Concettuale, senza esercizi di fraseggio sistematici.
- Pratica, capitolo 2 «Il tempo prima delle note»: pulsazione, metronomo, backbeat, count-in.
- Pratica, «Strutture melodiche», sezione «Dare tempo alle note»: un esempio (S4) con tre ritmi
  sulle stesse note.
- Pratica, «Modern jazz e fusion», studi 07–10: gruppi di tre, metri dispari, modulazione metrica.
- Strumenti: il ritmo è un asse dell'esercizio (ottavi, terzine, swing…) o un ritmo d'attacco.

Mancava il lavoro sistematico sulla **figura ritmica della frase**: quante note per battuta, da
quale punto della battuta parte un gruppo, figure che attraversano la stanghetta, «marce»,
anticipi e ritardi della risoluzione.

## Il metodo di Bergonzi (vol. 4), per capitoli

1 note per battuta · 2 ventidue ritmi di una battuta · 3–8 gruppi di 2–7 crome consecutive dalle
otto posizioni della battuta, anche in 3/4, 5/4, 7/4 e 9/4 sopra il 4/4 · 9–13 gruppi di terzine
(quattro note su sei, ecc.) · 14 revisione · 15 semicrome (dimezzare i capitoli 3–8) ·
16 emiolie (3/4 sopra 4/4) · 17–18 5/4 e 7/4 sopra 4/4, ritmi speculari e retrogradi ·
19 4/4 sopra 3/4 · 20 «in the pocket» (terzine e triplet feel) · 21 terzine di semiminima a metà
tempo · 22–23 «time zones»: la stessa linea in 5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 20, 24 note per
battuta · 24 quintine, settimine e nonine spezzate · 25 cambi di marcia · 26 contrazione ed
espansione · 27 battere e levare in semiminime · 28 minime e semiminime · 29 accenti ·
30 sentire il brano in 1, 2 o 4 · 31 metronomo (sul 2 e 4, solo 4, «e» del 2 e del 4) ·
32 sequenze di scala ritmate (note tolte, pause, poliritmi) · 33 grammatica ritmica (non
cominciare né finire sull'uno, anticipare e ritardare).

## Decisioni

1. **Pagina nuova di Pratica** `src/docs/ritmo-melodico.rst`, dopo Pentatoniche e prima di
   Accordi: come Strutture melodiche e Pentatoniche, è materiale per costruire la frase. Il
   capitolo 12 di Teoria resta il riferimento per le definizioni; la pagina rimanda alle sue
   sezioni invece di ripeterle.
2. **Dieci esempi originali** (R1–R10), con la stessa forma di Strutture melodiche (Scopo,
   Procedura, Ascolto, Varianti, Verifica; pentagramma e TAB; audio a 60 e 90 BPM, crome
   regolari): note per battuta con lo stesso ritmo e con ritmi diversi (cap. 1), quattro crome da
   quattro posizioni con la cellula Mi–Sol–Si–Re (cap. 3), partenza sull'«e» del 4 come anticipo
   (capp. 3–4), quattro terzine su sei (cap. 9), ciclo di tre pulsazioni che torna sull'uno alla
   quarta battuta (cap. 16), la stessa linea in quattro marce (cap. 22), sequenza di scala con note
   tolte (cap. 32), anticipo e ritardo della risoluzione (cap. 33), semiminime in battere e in
   levare (cap. 27). I capitoli senza esempio (2, 15, 17–18, 20, 23–26, 28–31) sono trattati nel
   testo e nello strumento. Il metodo è citato come fonte dei procedimenti; nessuna figura è
   trascritta.
3. **Audio con riferimento metrico**: pad, basso sulle fondamentali e charleston chiuso sul 2 e sul
   4 (overlay `sf/PracticeRhythm.sf2`), solo nel MIDI. Senza il charleston gli spostamenti non si
   sentono.
4. **Generatore** `scripts/generate_melodic_rhythms.py`: eventi con durate razionali, terzine
   (`\tuplet`), legature oltre la stanghetta, accenti; controllo della lunghezza di ogni battuta e
   dei tasti. Test `tests/test_melodic_rhythms.py` sulle proprietà musicali (stesso ritmo in R1,
   tre attacchi per battuta in R2, stesse note da quattro posizioni in R3, anticipi che
   appartengono all'accordo seguente in R4, cicli di tre pulsazioni in R6, stessa linea nelle
   quattro marce in R7, ordine della sequenza in R8, anticipo e ritardo in R9, battere e levare in
   R10) e sulla presenza di sorgenti e audio nella pagina.
5. **Strumento Ritmi** in appunti-strumenti (ADR 0016): 64 figure originali in otto famiglie
   che seguono le sezioni della pagina; griglia ritmica; altezze dalla nota fissa alla sequenza di
   scala; base dal catalogo di Progressioni; click spostato. Capitolo 11: sezione «Ritmi» con
   quattordici esercizi pronti, verificati da `tests/test_strumenti_links.py` (che controlla
   anche che le sezioni citate da `js/ritmi.js` esistano nella pagina).
6. **Rimandi**: Pratica 2 («Il tempo prima delle note»), Strutture melodiche («Dare tempo alle
   note» e «Dove proseguire»), Da dove comincio (percorso «Costruire una frase»); Teoria 12
   («Dall'analisi alla pratica» e «Poliritmia e polimetria»).

## Punti aperti

- **Versione**: una pagina nuova è «un passo importante» secondo le note di rilascio (1.2 → 1.3?).
  Le voci sono in «Prossimo aggiornamento»; il cambio di `VERSIONE` spetta all'utente.
- **Ascolto**: gli audio sono stati generati e controllati come file (MP3 presenti, nessun errore
  di LilyPond o FluidSynth), non ascoltati.
- **Swing**: gli esempi usano crome regolari per rendere leggibili gli spostamenti; lo strumento
  permette lo swing.
