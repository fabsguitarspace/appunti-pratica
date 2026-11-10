#!/usr/bin/env python3
"""Sixty original artist-path studies; notation, TAB and audio share event data.

Durations are sixteenth-note units. The audio explicitly maps conventional
swing eighths to 2:1; even-eighth studies retain exact written timing.
Run with python3, then build autori-* with build-lilypond.sh.
"""
from pathlib import Path
from fractions import Fraction as F
from math import ceil
import generate_modern_studies as music
from artist_profiles import PROFILES
ARTISTS={p["id"]:p["name"] for p in PROFILES}
ROOT=Path(__file__).resolve().parents[1]
H={
 'C6':(36,(48,52,57),'C6'), 'Cmaj7':(36,(48,52,59),'Cmaj7'),
 'Dm7':(38,(50,53,60),'Dm7'), 'Dm6':(38,(50,53,59),'Dm6'),
 'G7':(31,(43,47,53),'G7'), 'G7b9':(31,(43,47,53,56),'G7(b9)'),
 'F7':(29,(41,45,51),'F7'), 'C7':(36,(48,52,58),'C7'),
 'Am6':(33,(45,48,54),'Am6'), 'Am7':(33,(45,48,55),'Am7'),
 'E7b9':(28,(40,44,50,53),'E7(b9)'),
 'EmD':(38,(50,55,59,64),'Em7/D'), 'Clyd':(36,(48,52,59),'Cmaj7(#11)'),
 'EbD':(38,(51,55,58,62),'Ebmaj7/D'),
}
music.PADS.update(H)
V={
 'C6':((5,3,48),(4,2,52),(3,2,57),(2,5,64)),
 'Cmaj7':((5,3,48),(4,2,52),(3,4,59),(2,5,64)),
 'Dm7':((5,5,50),(4,3,53),(3,5,60),(2,6,65)),
 'G7':((6,3,43),(4,3,53),(3,4,59),(2,3,62)),
 'C7':((5,3,48),(4,2,52),(3,3,58),(2,5,64)),
 'F7':((6,1,41),(4,1,51),(3,2,57),(2,1,60)),
 'Am7':((6,5,45),(4,5,55),(3,5,60),(2,5,64)),
}
def b(*values):return [(x,2) if not isinstance(x,tuple) else x for x in values]
def q(*values):return [(x,4) for x in values]
def h(*values):return [(x,8) for x in values]
def chord(key,units=8):return (V[key],units)
def octave(p):
 s=5 if p<55 else 4;t=s-2
 return ((s,p-music.OPEN[s],p),(t,p+12-music.OPEN[t],p+12))
def octbar(*pitches):return [(octave(p),2) for p in pitches]
def dyad(*pairs):return tuple((s,f,music.OPEN[s]+f) for s,f in pairs)
def S(artist,n,title,keys,bars,explain,task,*,swing=True,style='modern',meter=(4,4),groups=None,solo=False,lower=None,accents=False,bpm=76):
 assert len(keys)==len(bars)
 s=music.study(n,title,keys,bars,style=style,meter=meter,groups=groups,bpm=bpm,accents=accents)
 s.update(artist=artist,stem=f'autori-{artist}-{n:02}',swing=swing,solo=solo,lower=lower,explain=explain,task=task)
 if lower:
  assert len(lower)==len(bars)
  assert all(sum(F(u,4) for p,u in bar)==F(meter[0]*4,meter[1]) for bar in lower)
 return s

DJ=[
 S('django',1,'Arpeggi di sesta nel minore',['Am6']*4,
   [b(57,60,64,66,69,66,64,60),b(57,60,64,69,66,64,(60,4)),b(60,64,66,69,72,69,66,64),h(60,57)],
   'La–Do–Mi–Fa♯ mette in evidenza Am6: tonica, terza minore, quinta e sesta maggiore. I salti disegnano l’accordo senza riempire ogni spazio con una scala.',
   'Canta il Fa♯ prima della salita. Ripeti la seconda battuta con due diteggiature e conserva la durata delle note; poi cambia soltanto l’ultima risposta.'),
 S('django',2,'Diminuito sulla dominante',['E7b9','E7b9','Am6','Am6'],
   [b(56,59,62,65,68,65,62,59),b(65,62,59,56,53,56,59,62),b(60,64,66,69,66,64,60,59),h(60,57)],
   'Sol♯–Si–Re–Fa è il diminuito costruito dalla terza di E7: 3–5–♭7–♭9. Il Do della terza battuta chiarisce l’arrivo su La minore.',
   'Isola l’ultima nota di E7 e la prima di Am6: Re → Do. Trasporta il diminuito per terze minori e controlla quali note restano le stesse.'),
 S('django',3,'Approccio e cambio di registro',['Am6','Dm6','E7b9','Am6'],
   [b(59,60,64,66,69,72,71,69),b(65,69,71,74,72,71,69,65),b(68,65,62,59,56,55,56,59),b(60,64,66,69,(57,8))],
   'Si prepara Do all’inizio; Sol–Sol♯ riprende la terza della dominante. Gli arpeggi vengono collegati da pochi semitoni mirati.',
   'Suona prima solo l’inizio di ogni battuta. Aggiungi i collegamenti senza accentare automaticamente ogni cambio di corda.'),
 S('django',4,'Quattro attacchi di accompagnamento',['Am7','Dm7','G7','C6'],
   [[chord(k,4)]*4 for k in ['Am7','Dm7','G7','C6']],
   'Quattro accordi per battuta separano il lavoro della mano ritmica dalle linee solistiche. Sono voicing completi di quattro note con fondamentale al basso, non shell.',
   'Studia una durata breve e un rilascio coordinato delle dita, con secondo e quarto movimento leggermente in rilievo. L’audio tiene il valore scritto: il rilascio per la pompe è un lavoro manuale da confrontare con l’ascolto.'),
 S('django',5,'Domanda, pausa e risposta',['Am6','Am6','E7b9','Am6'],
   [b(60,64,66,69,(72,4),(None,4)),b((None,4),69,66,64,60,(57,4)),b(56,59,62,65,68,65,62,59),b(60,64,(57,8),(None,4))],
   'Il silenzio separa due registri prima della salita diminuita. La forma della frase conta quanto la velocità dell’arpeggio.',
   'Canta entrambe le frasi senza toccare lo strumento. Conserva le pause e inventa una risposta più corta.'),
]
DJ.append(S('django',6,'Studio: seste e dominante diminuita',['Am6','Am6','Dm6','Dm6','E7b9','E7b9','Am6','Am6'],
 [DJ[0]['bars'][0],DJ[4]['bars'][0],DJ[2]['bars'][1],b(74,71,69,65,62,65,(69,4)),DJ[1]['bars'][0],DJ[1]['bars'][1],DJ[2]['bars'][3],h(60,57)],
 'Otto battute originali: due di Am6, due di Dm6, due di E7(♭9), due di Am6. Il Fa♯ caratterizza il primo minore e il Si naturale la sesta di Dm6; Fa naturale appartiene alla dominante alterata.',
 'Sulla base alterna un giro scritto e un giro con risposte tue. Conserva l’arrivo su Do nella settima battuta e il riposo finale su La.'))

CC=[
 S('christian',1,'Riff di tre note',['C6']*4,
   [b(64,67,(69,4),67,64,(None,4)),b(64,67,(69,4),67,64,(None,4)),b(67,69,72,69,(67,4),(None,4)),h(64,60)],
   'Mi–Sol–La è un nucleo di 3–5–6 su C6. La ripetizione e la risposta più alta costruiscono una frase prima di introdurre cromatismi.',
   'Canta il riff e batti secondo e quarto movimento. Cambia una sola durata nella ripetizione mantenendo il punto d’arrivo.'),
 S('christian',2,'Anticipare la risposta',['C6']*4,
   [b((None,2),64,67,69,(72,4),69,67),b((64,4),(None,2),64,67,69,67,64),b((None,2),67,69,72,74,72,69,67),h(64,60)],
   'Gli ingressi sul levare lasciano spazio al primo movimento. La pulsazione non scompare durante la pausa.',
   'Segna i quattro quarti mentre canti gli attacchi. Mantieni la pausa iniziale anche quando riparti da una battuta interna.'),
 S('christian',3,'Terze e settime nei cambi',['Dm7','G7','C6','C6'],
   [q(65,69,72,65),q(65,62,59,62),q(64,67,69,67),h(64,60)],
   'Fa è terza di Dm7 e settima di G7; Si è terza di G7 e conduce al Mi della tonica. La linea in quarti rende chiari i bersagli.',
   'Suona soltanto Fa–Fa–Mi sul primo movimento delle prime tre battute, poi ripristina il resto senza perdere quel percorso.'),
 S('christian',4,'Un riff attraversa il blues',['C7','F7','C7','G7'],
   [b(64,67,70,69,67,64,(60,4)),b(69,72,75,74,72,69,(65,4)),b(64,67,70,69,67,64,(60,4)),b(59,62,65,64,62,59,(55,4))],
   'Il riff conserva 3–5–♭7–13–5–3–1 su ogni dominante, adattando le altezze a C7, F7 e G7. È una finestra di studio, non un blues completo di quattro battute.',
   'Riconosci prima le tre fondamentali, poi trasporta il riff senza cambiare ritmo. Collegalo alla forma di dodici battute in Progressioni.'),
 S('christian',5,'Collegare senza interrompere lo swing',['Dm7','G7','C6','C6'],
   [b(62,65,69,72,71,69,67,65),b(65,64,62,60,59,62,65,69),b(67,64,62,60,62,64,67,69),b(72,69,67,64,(60,8))],
   'La linea prolunga il Fa attraverso il II–V e riparte da Sol sul I. Le crome continue devono conservare gruppi e direzione.',
   'Suona una prima versione accentando solo l’inizio di ogni battuta e una seconda accentando le note di arrivo. Evita di rendere tutte le crome ugualmente forti.'),
]
CC.append(S('christian',6,'Studio: riff, risposta e cadenza',['C6','C6','Dm7','G7','C6','Am7','Dm7','G7'],
 [CC[0]['bars'][0],CC[1]['bars'][1],CC[4]['bars'][0],CC[4]['bars'][1],CC[0]['bars'][2],b(69,72,76,74,72,69,67,64),q(65,69,72,65),q(65,62,59,60)],
 'Forma di otto battute con turnaround finale. L’ultimo Do è un’anticipazione del ritorno a C6: se ripeti, fai sentire l’arrivo sul primo movimento successivo.',
 'Memorizza prima il riff iniziale e la risposta finale. Sul secondo giro sostituisci le battute centrali e conserva gli stessi bersagli.'))

WM=[
 S('wes',1,'Una melodia in due registri',['Dm7']*4,
   [b(50,53,57,60,62,60,57,53),b(62,65,69,72,74,72,69,65),q(62,60,57,53),h(50,62)],
   'Le prime due battute presentano lo stesso profilo a distanza di un’ottava, prima di chiedere la doppia nota simultanea.',
   'Confronta attacco e volume nei due registri. Prova il pollice senza irrigidire il polso, oppure mantieni il plettro e cerca un attacco rotondo.'),
 S('wes',2,'Ottave e corde intermedie mute',['Dm7']*4,
   [octbar(50,53,50,53,57,53,50,53),[(octave(50),8),(None,8)],octbar(53,50,53,50,53,50,53,50),[(octave(50),16)]],
   'Le ottave Re e Fa usano le corde 5–3; quella di La passa alle corde 4–2. La corda intermedia deve restare muta.',
   'Studia prima Re e Fa, poi il passaggio al La. Controlla che si sentano due note distanti dodici semitoni, senza risonanze della corda interna.'),
 S('wes',3,'Risposta in ottave e pause',['Dm7','Dm7','G7','G7'],
   [[(octave(50),4),(octave(53),2),(octave(57),2),(None,8)],[(None,4),(octave(57),4),(octave(53),4),(octave(50),4)],
    [(octave(55),4),(octave(59),2),(octave(62),2),(None,8)],[(octave(59),8),(octave(55),8)]],
   'La risposta passa da Re minore alla triade di Sol maggiore dentro G7. Le pause impediscono che la doppia nota diventi una corsa continua.',
   'Ascolta la nota superiore come melodia. Registra e verifica che la nota inferiore non la copra.'),
 S('wes',4,'Accordi come risposta',['Dm7','G7','Cmaj7','C6'],
   [[chord('Dm7',4),(None,4),chord('Dm7',8)],[chord('G7',8),(None,4),chord('G7',4)],
    [chord('Cmaj7',4),(None,4),chord('Cmaj7',8)],[chord('C6',8),(None,8)]],
   'Il passaggio dai suoni singoli agli accordi aumenta la densità mantenendo una frase corta. Nei quattro voicing il basso è la fondamentale.',
   'Ascolta il canto Fa–Re–Mi–Mi. Suona la melodia da sola, poi aggiungi le altre voci mantenendo il canto in evidenza.'),
 S('wes',5,'Costruire un crescendo di tessitura',['Dm7','G7','Cmaj7','C6'],
   [b(62,65,69,72,69,65,(62,4)),[(octave(55),4),(octave(59),4),(octave(62),4),(octave(59),4)],
    [chord('Cmaj7',4),(None,4),chord('Cmaj7',8)],[chord('C6',16)]],
   'Quattro battute organizzano linea singola, ottave e accordi: la crescita riguarda la tessitura e non richiede di accelerare.',
   'Mantieni il medesimo volume medio. Poi crea una crescita graduale di intensità, lasciando il metronomo invariato.'),
]
WM.append(S('wes',6,'Studio: linea, ottave, accordi',['Dm7','G7','Cmaj7','C6','Dm7','G7','Cmaj7','C6'],
 [WM[0]['bars'][1],b(65,62,59,62,65,69,67,65),b(64,67,71,72,71,67,64,62),q(60,64,67,69),
  [(octave(50),4),(octave(53),4),(octave(57),4),(octave(60),4)],WM[4]['bars'][1],WM[4]['bars'][2],WM[4]['bars'][3]],
 'Le prime quattro battute preparano il motivo; quinta e sesta lo ampliano in ottave; le ultime due chiudono con accordi. I materiali hanno densità diversa ma appartengono alla stessa forma.',
 'Esegui tre giri: tutto a note singole, tutto dove possibile in ottave, poi la versione scritta. Valuta se il cambio di tessitura sostiene una direzione.'))

JH=[
 S('hall',1,'Due note e silenzio',['Cmaj7']*4,
   [b((64,4),(67,4),(None,8)),b((None,8),(67,4),(64,4)),h(64,62),[(60,8),(None,8)]],
   'Mi–Sol viene proposto, lasciato risuonare e ripreso in ordine inverso. L’assenza di note occupa una durata precisa nella forma.',
   'Conta tutta la pausa senza aggiungere riempitivi. Canta la risposta prima di suonarla, poi cambia soltanto l’ultima altezza.'),
 S('hall',2,'Una nota comune, due armonie',['Dm7','G7','Cmaj7','Cmaj7'],
   [h(65,69),h(65,59),h(64,67),[(64,8),(None,8)]],
   'Il Fa rimane fra Dm7 e G7 cambiando funzione da terza a settima; Si conduce al Mi, terza di Cmaj7.',
   'Ascolta l’accordo mentre tieni il Fa, senza ripeterlo come automatismo. Poi inventa un’altra risposta che termini su Mi.'),
 S('hall',3,'Due voci che si avvicinano',['Dm7','G7','Cmaj7','Cmaj7'],
   [[(dyad((3,5),(2,6)),8),(dyad((3,7),(2,6)),8)],[(dyad((3,4),(2,6)),16)],
    [(dyad((3,4),(2,5)),8),(dyad((3,5),(2,5)),8)],[(dyad((3,4),(2,5)),8),(None,8)]],
   'Le coppie Do–Fa e Re–Fa arrivano a Si–Fa su G7 e a Si–Mi su Cmaj7. Una voce resta ferma mentre l’altra si muove.',
   'Canta prima la voce superiore, poi quella inferiore. Queste coppie non sono shell: il basso della base completa il contesto armonico.'),
 S('hall',4,'Domanda e risposta senza raddoppio',['Cmaj7','Am7','Dm7','G7'],
   [b((64,4),67,71,(None,8)),b((None,8),72,69,(64,4)),b((65,4),69,72,(None,8)),b((None,8),65,62,(59,4))],
   'Le battute dispari parlano nella prima metà; le pari rispondono nella seconda. Il dialogo nasce dall’alternanza, non da due linee sovrapposte.',
   'Con un compagno dividete le battute dispari e pari. Da solo canta una parte e suona l’altra, mantenendo le pause assegnate.'),
 S('hall',5,'Cambiare una sola cosa',['Cmaj7','Cmaj7','Dm7','G7'],
   [b((64,4),67,71,(None,8)),b((None,2),(64,4),67,71,(None,6)),b((65,4),69,72,(None,8)),b((65,4),62,59,(None,8))],
   'La seconda battuta sposta il motivo di una croma senza cambiarne altezze e durate interne; la pausa conclusiva si accorcia per rispettare il 4/4.',
   'Confronta le prime due battute sul metronomo. Mantieni riconoscibile il motivo anche quando la sua partenza si sposta.'),
]
JH.append(S('hall',6,'Studio: dialogo e voci vicine',['Cmaj7','Am7','Dm7','G7','Cmaj7','Am7','Dm7','G7'],
 [JH[3]['bars'][0],JH[3]['bars'][1],JH[2]['bars'][0],JH[2]['bars'][1],JH[2]['bars'][2],b((None,8),72,69,(64,4)),JH[3]['bars'][2],JH[3]['bars'][3]],
 'Otto battute alternano linea, coppie di note e silenzio. Il turnaround finale rimane aperto e prepara Cmaj7 al giro successivo.',
 'Sulla base dimezza gli attacchi senza cambiare la forma. Registra e ascolta se il silenzio prepara davvero la risposta invece di interrompere il discorso.'))

PM=[
 S('metheny',1,'Salti dentro una frase cantabile',['Dm7']*4,
   [b(62,69,(76,4),74,69,(65,4)),b(64,71,(77,4),76,71,(67,4)),q(69,65,64,62),h(65,62)],
   'Quinte e intervalli ampi aprono la linea, mentre la discesa riconduce al registro centrale. Le note appartengono a Re dorico.',
   'Canta i salti prima di cercare i tasti. Fai respirare le note lunghe, senza trasformare ogni cambio di corda in un accento.',swing=False),
 S('metheny',2,'Una cellula su un pedale',['Dm7','EmD','Dm7','EmD'],
   [b(64,67,71,74,(72,4),(69,4)),b(64,67,71,74,(76,4),(71,4)),b(65,69,72,76,(74,4),(69,4)),h(67,62)],
   'Mi–Sol–Si–Re assume il colore di 9–11–13–1 su Re. La permanenza del basso lega armonie superiori differenti.',
   'Suona prima la cellula sempre uguale, poi modifica l’ultima nota di ogni battuta in relazione all’accordo.',swing=False),
 S('metheny',3,'Il motivo diventa una frase lunga',['Dm7','Dm7','EmD','Dm7'],
   [b(62,69,76,74,72,69,67,65),b(64,67,71,74,76,74,71,67),b(64,71,76,79,77,76,74,71),b(69,67,65,64,(62,8))],
   'I salti iniziali ritornano in registri diversi; la risoluzione viene rimandata fino alla quarta battuta. Il registro acuto richiede un cambio di posizione preparato.',
   'Canta l’intera frase con un solo punto di arrivo sul Re finale. Studia separatamente la terza battuta e limita la pressione della mano sinistra.',swing=False),
 S('metheny',4,'Nona e undicesima aumentata',['Clyd']*4,
   [q(62,66,69,74),b(76,74,71,69,67,66,64,62),b(64,67,71,74,76,74,71,69),h(67,64)],
   'Re–Fa♯–La è la triade maggiore un tono sopra Do: 9–♯11–13. Il Mi finale riporta l’orecchio alla terza dell’accordo.',
   'Confronta prima Fa e Fa♯ sopra la base. Scegli poi due sole tensioni e costruisci una frase che torni al Mi.',swing=False),
 S('metheny',5,'Una risposta più ampia del motivo',['Dm7','EmD','Dm7','Dm7'],
   [b((62,4),69,76,(74,8)),b((71,4),76,79,(77,8)),b((76,4),72,69,67,65,64,62),h(65,62)],
   'Le prime due battute mantengono lo stesso ritmo in registri differenti; la terza sostituisce la nota lunga con una discesa di crome.',
   'Mantieni i due punti di respiro e inventa un’altra discesa senza anticipare il riposo conclusivo.',swing=False),
]
PM.append(S('metheny',6,'Studio: arco melodico sul pedale',['Dm7','EmD','Dm7','EmD','Dm7','EmD','Dm7','Dm7'],
 [PM[0]['bars'][0],PM[1]['bars'][1],PM[4]['bars'][0],PM[4]['bars'][1],PM[2]['bars'][0],PM[2]['bars'][2],PM[4]['bars'][2],h(65,62)],
 'Otto battute su Re organizzano esposizione, risposta più alta, espansione e chiusura. Il culmine arriva prima della discesa finale.',
 'Sulla base sostituisci quattro note mantenendo il profilo generale. Registra una versione più rarefatta: la cantabilità deve sopravvivere alla riduzione.',swing=False))

# In the solo studies the lower voice is played on the guitar, not by a separate bassist.
BASS={'Cmaj7':[48,52,55,52],'C6':[48,52,55,52],'Dm7':[50,53,45,53],'G7':[43,47,50,47],'Am7':[45,48,52,48]}
TOP={'Cmaj7':[dyad((2,5),(1,7)),dyad((2,8),(1,8))], 'C6':[dyad((2,5),(1,5)),dyad((2,8),(1,8))],
     'Dm7':[dyad((2,6),(1,8)),dyad((2,6),(1,5))], 'G7':[dyad((2,6),(1,7)),dyad((3,7),(2,8))],
     'Am7':[dyad((2,5),(1,8)),dyad((2,5),(1,7))]}
def single_finger(p):
 string=6 if p<45 else 5 if p<55 else 4 if p<60 else 3 if p<=63 else 2 if p<=68 else 1
 return (string,p-music.OPEN[string],p)
def upper(keys):return [[(TOP[k][0],8),(TOP[k][1],8)] for k in keys]
def lower(keys,upperbars=None):
 upperbars=upperbars or upper(keys);result=[]
 for key,events in zip(keys,upperbars):
  line=[]
  for beat,pitch in enumerate(BASS[key]):
   position=0
   for top,units in events:
    if position<=beat*4<position+units:break
    position+=units
   notes=[] if top is None else list(top) if isinstance(top,tuple) else [single_finger(top)]
   occupied={string for string,fret,note in notes};frets=[fret for string,fret,note in notes if fret]
   choices=[]
   for string in (6,5,4):
    fret=pitch-music.OPEN[string]
    if string not in occupied and 0<=fret<=15:
     pressed=frets+([fret] if fret else [])
     span=max(pressed)-min(pressed) if pressed else 0
     choices.append((span,abs(fret-(sum(frets)/len(frets) if frets else fret)),string,fret))
   span,distance,string,fret=min(choices);assert span<=4,(key,beat,notes,choices)
   line.append((((string,fret,pitch),),4))
  result.append(line)
 return result
SOLO_MELODY=[[(71,8),(72,8)],[(74,8),(72,8)],[(71,8),(67,8)],[(64,16)]]
JP=[
 S('pass',1,'Il basso tiene la forma',['Cmaj7','Am7','Dm7','G7'],[q(*BASS[k]) for k in ['Cmaj7','Am7','Dm7','G7']],
   'Le fondamentali, terze e quinte descrivono il giro senza una sezione ritmica esterna. Ogni nota di basso è una nota dell’accordo.',
   'Conta e canta la fondamentale di ogni battuta. Suona le quattro note senza affrettare il passaggio di corda.',solo=True),
 S('pass',2,'Basso e accordo alternati',['Cmaj7','Am7','Dm7','G7'],
   [[(BASS[k][0],4),(TOP[k][0],4),(BASS[k][2],4),(TOP[k][1],4)] for k in ['Cmaj7','Am7','Dm7','G7']],
   'Il basso occupa primo e terzo movimento, le coppie superiori secondo e quarto. I registri si rispondono senza suonare tutti insieme.',
   'Studia le due parti separatamente, poi alternale. I suoni bassi devono essere più leggeri del canto.',solo=True),
 S('pass',3,'Melodia sostenuta sopra il basso',['Cmaj7']*4,
   SOLO_MELODY,
   'La voce superiore procede per minime, con una semibreve finale e il basso continua in quarti: due durate indipendenti sulla stessa chitarra.',
   'Lascia risuonare le note alte mentre attacchi il basso. Le due voci del pentagramma e della TAB condividono il tempo, non la durata di ogni evento.',solo=True,lower=lower(['Cmaj7']*4,SOLO_MELODY)),
 S('pass',4,'Due voci alte e un basso mobile',['Dm7','G7','Cmaj7','C6'],upper(['Dm7','G7','Cmaj7','C6']),
   'Le coppie superiori durano due movimenti mentre il basso si muove ogni quarto. Il Fa e il Si di G7 trovano Mi e Si in Cmaj7.',
   'Canta il canto e suona solo il basso; poi aggiungi la voce interna. Evita che la nota di basso interrompa le due note tenute sopra.',solo=True,lower=lower(['Dm7','G7','Cmaj7','C6'])),
 S('pass',5,'Una linea fra gli accordi',['Cmaj7','Am7','Dm7','G7'],
   [[chord('Cmaj7',8),(64,2),(67,2),(71,2),(72,2)],
    [chord('Am7',8),(72,2),(69,2),(67,2),(64,2)],
    [chord('Dm7',8),(65,2),(69,2),(72,2),(69,2)],
    [chord('G7',8),(65,2),(62,2),(59,2),(60,2)]],
   'Ogni accordo dura due movimenti; una breve linea occupa gli altri due. È un’alternanza di tessiture, distinta dalle voci simultanee dell’esercizio precedente.',
   'Suona prima soltanto accordo e ultima nota della frase. Poi riempi lo spazio senza perdere i quattro movimenti.',solo=True),
]
JP.append(S('pass',6,'Studio solo: canto, voci interne e basso',['Cmaj7','Am7','Dm7','G7','Cmaj7','Am7','Dm7','G7'],
 upper(['Cmaj7','Am7','Dm7','G7','Cmaj7','Am7','Dm7','G7']),
 'Il basso procede in quarti con toniche, terze e quinte; le due voci superiori durano due quarti. Nessun basso o accordo viene aggiunto da un altro strumento: tutto il materiale armonico scritto appartiene alla chitarra.',
 'Studia basso, canto e voce interna separatamente, poi in coppie e infine insieme. La base finale contiene soltanto un riferimento ritmico: esegui tu tutte le parti.',solo=True,lower=lower(['Cmaj7','Am7','Dm7','G7','Cmaj7','Am7','Dm7','G7'])))

GB=[
 S('benson',1,'Terza blues e terza maggiore',['C7']*4,
   [b(60,63,64,67,70,69,67,64),b(63,64,67,70,72,70,(67,4)),b(70,69,67,64,63,64,62,60),h(64,60)],
   'Mi♭ e Mi naturale dialogano su C7. La terza maggiore nell’accompagnamento rende udibile la frizione della terza blues.',
   'Canta Mi♭–Mi senza forzare la voce, poi suona le due note distinte. L’audio è temperato: inflessioni e bending richiedono un confronto diretto con l’ascolto.'),
 S('benson',2,'Voce prima delle dita',['C6','C6','G7','C6'],
   [b((64,4),67,69,(72,4),(None,4)),b((69,4),67,64,(60,4),(None,4)),b((59,4),62,65,(69,4),(None,4)),h(67,64)],
   'Frasi brevi e pause offrono il tempo per cantare, ascoltare e riprodurre. Il canto è una verifica della direzione melodica, non un obbligo di raddoppio vocale continuo.',
   'Canta una battuta e suonala nella pausa successiva, fermando il lettore se serve. Poi canta e suona insieme un’ottava comoda per la tua voce.'),
 S('benson',3,'Cromatismi verso il bersaglio',['Dm7','G7','C6','C6'],
   [b(65,64,65,69,72,71,69,67),b(65,64,62,60,58,59,62,65),b(65,63,64,67,69,72,71,69),b(67,66,67,64,(60,8))],
   'Mi prepara Fa nel II, Si♭ prepara Si nel V e Fa–Mi♭ circonda Mi sul I. Gli approcci rimangono brevi e trovano note dell’accordo.',
   'Togli i cromatismi e canta la linea essenziale. Reinseriscili uno alla volta senza trasformarli in punti di riposo.'),
 S('benson',4,'La linea entra nel sedicesimo',['C7']*4,
   [b((None,1),(64,1),67,70,72,70,(67,1),(64,1),63,64),
    b(67,(70,1),(72,1),70,67,64,63,(60,4)),
    b((None,2),(63,1),(64,1),67,70,(72,1),(70,1),67,64,60),h(64,60)],
   'Lo stesso materiale blues viene organizzato in sedicesimi regolari e pause sul groove. Qui l’audio non applica swing.',
   'Mantieni il secondo e quarto movimento del rullante come riferimento. Prova prima tutto con pennate leggere, poi lega due note mantenendo identico il ritmo.',swing=False,style='fusion'),
 S('benson',5,'Risposta sul quarto grado',['C7','F7','C7','G7'],
   [b(60,63,64,67,70,69,(67,4)),b(65,68,69,72,75,74,(72,4)),b(70,67,64,63,60,62,(64,4)),b(65,62,59,57,55,57,(59,4))],
   'La cellula Do–Mi♭–Mi–Sol su C7 diventa Fa–La♭–La–Do su F7. La terza blues si adatta al nuovo accordo.',
   'Canta la seconda battuta come risposta della prima. Poi inserisci la coppia in due finestre corrispondenti del blues di dodici battute.'),
]
GB.append(S('benson',6,'Studio: blues, canto e groove',['C7','C7','F7','F7','C7','C7','G7','C7'],
 [GB[3]['bars'][0],GB[3]['bars'][1],b((None,2),(68,1),(69,1),72,75,(77,1),(75,1),72,69,65),b(72,75,74,72,69,68,(65,4)),
 GB[3]['bars'][2],b(70,69,67,64,63,64,(60,4)),b(59,62,65,69,67,65,62,59),h(64,60)],
 'Otto battute, non un chorus completo di blues: due di C7, due di F7, due di C7, una di G7 e una di C7. Le crome sono regolari; le piccole accelerazioni interne vengono dai sedicesimi scritti.',
 'Canta la prima e l’ultima battuta, poi suona tutto sulla base. Inventa una seconda versione con metà degli attacchi mantenendo terze e risposte.',swing=False,style='fusion'))

PT=[
 S('martino',1,'Un’area minore riconoscibile',['Dm7']*4,
   [b(62,65,69,72,74,72,69,65),b(64,65,69,72,71,69,67,65),b(62,64,65,69,72,74,72,69),b(67,65,64,62,(65,8))],
   'Re–Fa–La–Do organizza l’area di Dm7; Mi e Si la ampliano nel dorico. Si parte da una sonorità conosciuta, non da un’etichetta diversa per ogni nota.',
   'Suona le prime quattro note in due zone della tastiera. Conserva gli intervalli e scegli un punto di arrivo prima di sviluppare la linea.'),
 S('martino',2,'Re minore letto sopra Sol',['G7']*4,
   [b(62,65,69,72,69,65,62,59),b(62,65,69,72,74,72,69,65),b(69,72,74,72,69,65,62,59),h(65,59)],
   'L’arpeggio Dm7 su G7 dà 5–♭7–9–11. Il Si conclusivo rende esplicita la terza della dominante, assente dall’arpeggio minore.',
   'Canta i gradi rispetto a Sol. Tieni brevi i Do quando vuoi un colore di dominante definito e confronta l’arrivo su Si.'),
 S('martino',3,'Un materiale per II e V',['Dm7','G7','Cmaj7','Cmaj7'],
   [b(62,65,69,72,74,72,69,65),b(62,65,69,72,69,65,62,59),b(64,67,71,74,72,71,69,67),h(64,60)],
   'Le prime due battute condividono l’area minore di Re, ma il V termina su Si e il I comincia su Mi. La continuità non cancella la funzione degli accordi.',
   'Collega la seconda e la terza battuta senza pausa: Si → Mi deve avere una direzione udibile. Poi inventa un altro finale della dominante.'),
 S('martino',4,'Una sequenza cambia registro',['Dm7']*4,
   [b(62,65,64,69,65,72,69,74),b(65,69,67,72,69,74,72,77),b(74,72,69,67,65,64,62,60),h(65,62)],
   'Il disegno alterna piccoli ritorni e salti verso note dell’area minore. La terza battuta ricompone il registro prima della chiusura.',
   'Studia gruppi di quattro crome, poi collega due gruppi senza accenti automatici sul cambio di corda. Riduci la velocità finché il suono rimane continuo.'),
 S('martino',5,'Minore un semitono sopra la dominante',['G7b9','G7b9','Cmaj7','Cmaj7'],
   [b(68,71,75,80,77,75,71,68),b(77,75,73,71,68,67,65,59),b(64,67,71,74,72,71,69,67),h(64,60)],
   'La triade di La♭ minore (La♭–Do♭–Mi♭, scritta La♭–Si–Mi♭ in relazione a Sol) produce ♭9–3 enarmonica–♭13 su G7. Fa naturale completa la settima minore e Re♭ aggiunge ♭5 nella seconda battuta. La linea torna al Mi di Cmaj7.',
   'Isola La♭–Si–Mi♭ e canta i tre intervalli rispetto a Sol. Poi esegui le ultime quattro crome della dominante e l’arrivo sul Mi; non applicare automaticamente la stessa collezione a ogni dominante.'),
]
PT.append(S('martino',6,'Studio: continuità minore e risoluzione',['Dm7','G7','Cmaj7','Cmaj7','Dm7','G7b9','Cmaj7','Cmaj7'],
 [PT[0]['bars'][0],PT[1]['bars'][0],PT[2]['bars'][2],PT[2]['bars'][3],PT[3]['bars'][0],PT[4]['bars'][1],PT[2]['bars'][2],h(64,60)],
 'Il primo II–V usa l’area di Re minore e chiarisce Si; il secondo colora G7 con ♭9 e ♭5 prima dell’arrivo su Cmaj7. La rilettura minore è un modo di organizzare la linea, non una sostituzione letterale degli accordi della base.',
 'Confronta le due dominanti e scegli una nota bersaglio per ognuna. Sulla base cambia il percorso intermedio mantenendo gli arrivi.'))

JS=[
 S('scofield',1,'Blues con la terza in vista',['C7']*4,
   [b((None,2),63,64,67,(70,4),67,64),b(66,67,70,69,67,64,(60,4)),b(63,64,67,70,72,70,67,64),h(63,64)],
   'Mi♭–Mi porta la frizione blues dentro C7; Fa♯ passa a Sol. Il finale conserva la distanza fra terza blues e terza maggiore.',
   'Canta il Mi♭ finale e ascolta il Mi nell’accordo, poi suona il Mi scritto. Cerca un attacco espressivo senza cambiare le altezze di riferimento.',swing=False,style='fusion'),
 S('scofield',2,'La pausa entra nel groove',['C7']*4,
   [b((None,1),(64,1),(None,2),67,70,(None,4),67,64),b((60,4),(None,2),63,64,67,(None,4)),
    b((None,2),(67,1),(70,1),(None,4),72,70,67,64),[(60,8),(None,8)]],
   'Gli attacchi lasciano vuoti dentro la griglia di sedicesimi. Il basso e la batteria continuano mentre la chitarra tace.',
   'Suona inizialmente una sola nota con il ritmo scritto. Aggiungi le altezze soltanto quando le pause rimangono precise.',swing=False,style='fusion'),
 S('scofield',3,'Una cellula spostata di semitono',['C7']*4,
   [b(64,67,70,72,70,67,64,60),b(64,67,70,72,65,68,71,73),b(64,67,70,72,70,67,64,60),h(63,64)],
   'Mi–Sol–Si♭–Do viene spostato a Fa–La♭–Si–Re♭ nella seconda metà della seconda battuta, poi torna al disegno iniziale. Fa rimane interno al contesto; La♭, Si e Re♭ rendono evidente l’uscita.',
   'Canta il rientro sul Mi della terza battuta e tieni il piede sui quarti durante il passaggio esterno.',swing=False,style='fusion'),
 S('scofield',4,'Terze e seste a due voci',['C7','F7','C7','G7'],
   [[(dyad((3,5),(2,5)),4),(None,4),(dyad((2,5),(1,8)),8)],
    [(dyad((3,2),(2,1)),4),(None,4),(dyad((3,2),(2,6)),8)],
    [(dyad((3,5),(2,5)),8),(dyad((2,5),(1,8)),8)],
    [(dyad((3,4),(2,3)),8),(dyad((3,4),(2,8)),8)]],
   'Do–Mi e Mi–Do su C7; La–Do e La–Fa su F7; Si–Re e Si–Sol su G7. Le prime coppie sono terze, le seconde seste: note dell’accordo distribuite in due registri diversi.',
   'Suona prima la voce superiore con il ritmo scritto. Aggiungi l’altra voce senza irrigidire l’attacco. Sono coppie melodiche, non voicing completi con tensioni al basso.',swing=False,style='fusion'),
 S('scofield',5,'Accenti ogni tre sedicesimi',['C7']*4,
   [[( [64,67,70][(i*16+j)%3],1) for j in range(16)] for i in range(3)]+[[(64,8),(None,8)]],
   'La cellula Mi–Sol–Si♭ ripete un accento ogni tre sedicesimi per tre battute; la batteria conserva il 4/4. Dopo 48 sedicesimi, sedici cellule tornano all’inizio della misura.',
   'Canta soltanto gli accenti e batti i quarti. Poi aggiungi le note deboli più piano e rispetta il riposo finale.',swing=False,style='fusion',accents=True),
]
JS.append(S('scofield',6,'Studio: groove, attrito e spazio',['C7','C7','F7','F7','C7','C7','G7','C7'],
 [JS[1]['bars'][0],JS[0]['bars'][1],JS[3]['bars'][1],b((None,2),68,69,72,75,72,69,65),
 JS[2]['bars'][1],JS[2]['bars'][2],JS[3]['bars'][3],h(63,64)],
 'Una forma di otto battute combina pause, doppie note, terza blues e un’uscita di semitono. Nella sesta battuta il ritorno al Mi chiarisce il rientro su C7.',
 'Sulla base mantieni i vuoti della prima battuta e il rientro della sesta. Cambia l’uscita senza aumentare il numero totale degli attacchi.',swing=False,style='fusion'))

JM=[
 S('mclaughlin',1,'Quattro note, attacco uniforme',['Dm7']*4,
   [[(p,1) for p in [62,65,69,72]*4],[(p,1) for p in [64,67,71,74]*4],b(74,72,71,69,67,65,64,62),h(65,62)],
   'Due cellule di sedicesimi regolari si alternano su Re dorico. La prima esplicita Dm7; la seconda presenta 9–11–13–1.',
   'Studia a metà velocità e ferma subito la ripetizione se la mano si irrigidisce. Cerca attacchi e durata uniformi prima di aumentare il tempo.',swing=False),
 S('mclaughlin',2,'Cinque quarti cantati tre più due',['Dm7']*4,
   [b(62,65,69,72,74,72,71,69,65,62),b(64,67,71,74,76,74,72,71,67,64),q(62,65,69,67,64),q(65,64,62,60,62)],
   'Dieci crome occupano cinque quarti raggruppati 3+2. Le prime sei crome formano il primo gruppo, le ultime quattro il secondo.',
   'Conta UNO due tre | QUATTRO cinque e canta gli inizi dei gruppi prima di aggiungere tutte le note.',swing=False,style='five',meter=(5,4),groups=(3,2)),
 S('mclaughlin',3,'Sette ottavi su un centro frigio',['Dm7','EbD','Dm7','EbD'],
   [b(62,63,65,69,70,67,65),b(63,67,70,74,72,70,67),b(69,70,72,74,72,70,65),b((63,4),(65,4),67,(62,4))],
   'Re–Mi♭–Fa–Sol–La–Si♭–Do stabilisce il materiale frigio; Mi♭ è il semitono sopra il centro Re. La griglia alterna Dm7 ed E♭maj7/D.',
   'Conta 2+2+3 crome e canta Re–Mi♭. Il conteggio iniziale ha sette crome; non confonderlo con sette quarti.',swing=False,style='seven',meter=(7,8),groups=(2,2,3),bpm=84),
 S('mclaughlin',4,'Gruppi di tre sopra il quattro',['Dm7']*4,
   [[([62,65,69][(i*16+j)%3],1) for j in range(16)] for i in range(3)]+[[(62,16)]],
   'Sedici gruppi di tre sedicesimi attraversano tre battute di 4/4. Gli accenti continuano oltre la stanghetta, mentre basso e batteria mantengono il metro.',
   'Batti soltanto i quarti e canta la cellula. Riduci poi a una sola nota con gli accenti scritti: il ciclo deve restare comprensibile anche senza altezze.',swing=False,accents=True),
 S('mclaughlin',5,'Contrasto fra densità e respiro',['Dm7']*4,
   [[(p,1) for p in [62,65,69,72,74,72,69,65,64,67,71,74,76,74,71,67]],[(62,8),(None,8)],
    [(p,1) for p in [65,69,72,76,77,76,72,69,67,71,74,77,79,77,74,71]],[(65,8),(62,8)]],
   'Una battuta densa trova risposta in una nota lunga e una pausa; il secondo gesto raggiunge un registro più alto e poi si posa.',
   'Suona la parte densa piano e la nota di arrivo più presente. La velocità ha senso se il contrasto fra le frasi rimane udibile.',swing=False),
]
JM.append(S('mclaughlin',6,'Studio: ciclo di sette e risposta modale',['Dm7','EbD','Dm7','EbD','Dm7','EbD','Dm7','Dm7'],
 [JM[2]['bars'][0],JM[2]['bars'][1],JM[2]['bars'][2],JM[2]['bars'][3],
 b(62,65,69,72,74,72,69),b(63,67,70,74,75,74,70),b(69,67,65,63,62,60,57),[(65,4),(63,4),(62,6)]],
 'Otto battute in 7/8, sempre 2+2+3. Le prime quattro espongono il materiale, quinta e sesta lo spingono in alto, settima e ottava riconducono a Re. Le note rimangono nel materiale frigio.',
 'Esegui prima solo la prima nota dei tre gruppi. Poi suona la linea completa e inventa un nuovo finale di sette crome mantenendo la stessa forma.',swing=False,style='seven',meter=(7,8),groups=(2,2,3),bpm=84))

GROUPS=[DJ,CC,WM,JH,PM,JP,GB,PT,JS,JM]
STUDIES=[s for group in GROUPS for s in group]


def pitch_name(p,key=None):
 name=music.pname(p)
 return name.replace('af','gs',1) if key=='E7b9' and p%12==8 else name

def guitar_pitch(p,key=None):
 if isinstance(p,tuple):
  for string,fret,note in p:assert music.OPEN[string]+fret==note and 0<=fret<=20
  return '<'+' '.join(pitch_name(note,key)+f'\\{string}' for string,fret,note in p)+'>'
 string=6 if p<45 else 5 if p<55 else 4 if p<60 else 3 if p<=63 else 2 if p<=68 else 1
 fret=p-music.OPEN[string];assert 0<=fret<=20,(p,string,fret)
 return pitch_name(p,key)+f'\\{string}'

def timed(token,units):
 duration=music.duration(units) if units in (1,2,3,4,6,8,12,14,16,20) else '1*'+str(F(units,16))
 if token.startswith('<') or '\\' not in token:return token+duration
 pitch,string=token.split('\\');return pitch+duration+'\\'+string

def swing_position(position):
 whole=position//4;local=position-whole*4
 return whole*4+(local*F(4,3) if local<=2 else F(8,3)+(local-2)*F(2,3))

def render(study,bars,midi=False,labels=True):
 lines=[];count=0
 for i,bar in enumerate(bars):
  tokens=[];position=F(0)
  for j,(pitch,units) in enumerate(bar):
   sounding=swing_position(position+units)-swing_position(position) if midi and study['swing'] else units
   token=timed('r' if pitch is None else guitar_pitch(pitch,study['keys'][i]),sounding)
   if study['accents'] and count%3==0 and pitch is not None:token+='->'
   if j==0 and labels:token+=f'^\\markup {{ \\small "{H[study["keys"][i]][2]}" }}'
   tokens.append(token);position+=units;count+=1
  lines.append(' '.join(tokens)+' |'+(' \\break' if (i+1)%4==0 and i+1<len(bars) else ''))
 return '\n'.join(lines)

def guitar(study,midi=False):
 upper=render(study,study['bars'],midi=midi,labels=not midi)
 if study['lower']:
  low=render(study,study['lower'],midi=midi,labels=False)
  return '\\absolute { << { \\voiceOne '+upper+' } \\\\ { \\voiceTwo '+low+' } >> \\oneVoice \\bar "|." }'
 return '\\absolute { '+upper+' \\bar "|." }'

def accompaniment(study,part):
 # Quarter bass and ride pattern: the ride eighths swing with the guitar.
 if part!='drums':return music.rhythmic_part(study,part)
 lines=[]
 for index in range(len(study['bars'])):
  position=F(0);tokens=[]
  events=music.drums(study,index)
  for notes,units in events:
   sounding=swing_position(position+units)-swing_position(position) if study['swing'] else units
   token='r' if notes is None else '<'+' '.join(music.DRUM_NAMES[n] for n in notes)+'>'
   tokens.append(timed(token,sounding));position+=units
  lines.append(' '.join(tokens)+' |')
 return '\n'.join(lines)

def source(study,base=False):
 beats=F(study['meter'][0]*4,study['meter'][1]);rest='r1*'+str(beats/4)
 count='hh8 '*7 if study['meter']==(7,8) else 'hh4 '*int(beats)
 lead='' if base else rf'\new Staff {{ \set Staff.midiInstrument = "acoustic grand" {rest} \mf \guitarMidi }}'
 if study['solo']:
  band=''
  rhythm=' '.join(['hh4 '*4+' |']*len(study['bars'])) if base else ' '.join([rest]*len(study['bars']))
  rhythm='\\drummode { '+rhythm+' }'
 else:
  band=rf'''\new Staff {{ \set Staff.midiInstrument = "acoustic grand" {rest} \pp \pad }}
 \new Staff {{ \set Staff.midiInstrument = "electric bass (finger)" {rest} \mf \bassline }}'''
  rhythm='\\drumline'
 text=rf'''% Generated by scripts/generate_artist_studies.py; edit the generator.
% soundfont-overlay: sf/PracticeRhythm.sf2
\version "2.26.0"
\language "english"
\header {{ title = "{study['number']:02} - {study['title']}{' - base' if base else ''}" subtitle = "{ARTISTS[study['artist']]} - studio originale" tagline = ##f }}
\paper {{ page-breaking = #ly:one-page-breaking line-width = 160\mm ragged-right = ##f }}
global = {{ {music.global_music(study)} }}
control = {{ {music.global_music(study,True)} }}
guitar = {guitar(study)}
guitarMidi = {guitar(study,True)}
pad = \absolute {{ {accompaniment(study,'pad')} }}
bassline = \absolute {{ {accompaniment(study,'bass')} }}
drumline = \drummode {{ {accompaniment(study,'drums')} }}
\score {{ \new StaffGroup <<
 \new Staff {{ \clef "treble_8" << \global \guitar >> }}
 \new TabStaff {{ \set TabStaff.stringTunings = #guitar-tuning \omit TextScript << \global \guitar >> }}
 >> \layout {{ indent = 0 system-count = #{ceil(len(study['bars'])/4)}
 \context {{ \Voice \override TextScript.staff-padding = #2 }}
 \context {{ \Score \omit StringNumber }} }} }}
\score {{ <<
 \new Staff {{ \control }}
 {lead}
 {band}
 \new DrumStaff {{ \drummode {{ {count} }} \p {rhythm} }}
 >> \midi {{ }} }}
'''
 return '\n'.join(line.rstrip() for line in text.splitlines())+'\n'

def main():
 assert len(STUDIES)==60
 for study in STUDIES:
  for base in ([False,True] if study['number']==6 else [False]):
   path=ROOT/'src/lilypond'/f"{study['stem']}{'-base' if base else ''}.ly"
   path.write_text(source(study,base=base))
 print('Generated 60 studies and 10 final-study bases.')
if __name__=='__main__':main()
