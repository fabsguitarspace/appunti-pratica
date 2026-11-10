#!/usr/bin/env python3
"""Fifty original bebop studies: ten per category, with explicit contexts.

Run python3 scripts/generate_bebop_licks.py. Build licks-* using build-lilypond.sh.
One authored melody defines notation, TAB and MIDI. Audio uses 2:1 swing at
90 BPM, notation conventional eighths; backing follows the same chord timeline.
"""
from pathlib import Path
from fractions import Fraction
import sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from generate_progressions import CHORDS, OPEN, pitch_name

# Durations are counts of notated eighth-note slots. No random generation.
def b(*pitches):
 return [(p,1) if not isinstance(p,tuple) else p for p in pitches]
def end(*pitches):
 assert len(pitches)==7
 return b(*pitches[:6],(pitches[6],2))
def seed(cat,n,title,keys,bars,tech,link):
 assert len(keys)==len(bars)
 assert all(sum(u for p,u in bar)==8 for bar in bars)
 return dict(category=cat,number=n,id=f'{cat}{n:02}',stem=f'licks-{cat.lower()}{n:02}',title=title,keys=keys,bars=bars,tech=tech,link=link)

MAJOR=[
 ('Alla terza dal basso','Cmaj7',b(63,64,67,71,74,72,71,69),end(67,66,65,64,62,63,64),'Re♯ conduce a Mi; la discesa Sol–Fa♯–Fa–Mi ricompone la terza.'),
 ('Circondare Mi','Cmaj7',b(65,63,64,67,71,69,67,65),end(64,67,69,70,71,74,72),'Fa e Re♯ circondano Mi; Si♭ è un passaggio verso Si.'),
 ('La sesta nel maggiore','C6',b(64,67,68,69,72,71,69,67),end(64,65,66,67,64,62,60),'Sol♯ collega Sol e La, mettendo in luce la sesta di C6.'),
 ('Arpeggio e risposta','Cmaj7',b((72,2),71,67,(64,2),(None,2)),end(66,67,71,74,72,71,72),'Arpeggio discendente, pausa e riattacco cromatico alla quinta.'),
 ('Motivo sulla terza','Cmaj7',b(64,67,71,72,71,69,67,66),end(67,64,62,60,64,67,72),'Fa♯ sul levare conduce a Sol; la risposta torna alla tonica.'),
 ('Cromatismo discendente','Cmaj7',b(67,66,65,64,62,60,59,60),end(64,67,71,74,72,69,67),'Sol–Fa♯–Fa–Mi collega quinta e terza; Si richiama Do.'),
 ('Salto e ritorno','Cmaj7',b(60,64,67,72,71,70,69,67),end(65,64,62,63,64,67,72),'Il salto a Do acuto è seguito dal cromatismo Si–Si♭–La.'),
 ('Pentatonica con un passaggio','C6',b(69,67,64,62,60,62,63,64),end(67,69,72,71,69,67,64),'La linea di C6 include Re♯ come passaggio fra Re e Mi.'),
 ('La nona e la terza','Cmaj7',b(74,72,71,70,69,67,65,64),end(67,71,74,72,69,65,64),'La nona acuta scende verso Mi; le note estranee rimangono brevi.'),
 ('Ingresso in levare','Cmaj7',b(None,63,64,67,71,74,72,71),end(69,67,66,67,64,62,60),'La pausa iniziale lascia spazio; Re♯–Mi e Fa♯–Sol indicano i bersagli.'),
]
MINOR=[
 ('Terza minore e ritorno','Cm7',b(63,67,70,74,72,70,69,67),end(65,64,63,62,60,59,60),'Mi naturale passa fra Fa e Mi♭; Si naturale prepara Do.'),
 ('Circondare Mi bemolle','Cm7',b(65,62,63,67,70,69,68,67),end(65,63,62,61,60,63,67),'Fa e Re circondano Mi♭; Re♭ prepara Do nella risposta.'),
 ('La sesta della tonica minore','Cm6',b(69,67,63,60,62,63,65,66),end(67,70,69,68,67,64,63),'La è la sesta; Fa♯ risolve a Sol e Mi scende a Mi♭.'),
 ('Settima maggiore nel minore','CmMaj7',b(72,71,67,63,62,61,60,59),end(60,63,67,71,74,71,72),'Si naturale appartiene alla sonorità Cm(maj7), non a Cm7.'),
 ('Dalla settima alla terza','Cm7',b(70,69,68,67,65,64,63,62),end(60,63,67,70,69,67,63),'La–La♭ e Mi naturale sono passaggi dentro una discesa verso Mi♭.'),
 ('Dal semitono superiore','Cm6',b(64,63,67,69,72,71,69,67),end(66,67,63,62,60,57,60),'Mi naturale conduce a Mi♭; la chiusura richiama la sesta La.'),
 ('Quinta e undicesima','Cm7',b(72,70,67,63,65,69,68,67),end(65,64,63,62,61,60,67),'Fa e La ampliano il registro; i cromatismi riportano a Do e Sol.'),
 ('La nona sopra Cm(maj7)','CmMaj7',b(74,72,71,70,69,67,65,63),end(67,71,74,72,67,64,63),'Re è nona; Si naturale distingue il colore della settima maggiore.'),
 ('Salita dal registro medio','Cm6',b(60,63,64,65,66,67,69,72),end(71,69,67,65,63,62,60),'Mi e Fa♯ legano la salita; La naturale sostiene il colore m6.'),
 ('Risposta dopo il silenzio','Cm7',b(None,62,63,65,67,70,69,67),end(65,64,63,60,62,59,60),'La frase entra sul levare e chiude con Si–Do.'),
]
DOMINANT=[
 ('Terza e settima di G7','G7',b(67,71,74,77,76,74,73,72),end(71,69,68,67,65,62,59),'L’arpeggio sale a Fa; i semitoni riconducono al Si, terza di G7.'),
 ('Circondare la terza','G7',b(72,70,71,74,77,76,75,74),end(73,72,71,69,67,65,71),'Do e La♯ circondano Si; il bersaglio finale è ancora la terza.'),
 ('Discesa bebop di dominante','G7',b(79,78,77,76,74,72,71,69),end(67,71,74,77,76,74,71),'Fa♯ è il passaggio fra Sol e Fa nella discesa bebop.'),
 ('Nona minore e arpeggio diminuito','G7b9',b(68,71,74,77,76,74,72,71),end(70,69,68,67,65,62,67),'La♭–Si–Re–Fa mette in evidenza la nona minore di G7.'),
 ('Tensioni nel registro acuto','G7b9',b(73,74,77,80,79,77,75,73),end(72,70,71,74,72,69,67),'La♭ e Mi♭ colorano la dominante; Re♭ conduce a Do.'),
 ('Nona e tredicesima','G7',b(71,74,77,81,80,79,77,76),end(75,74,73,72,71,69,67),'La e Mi naturali sono colori di nona e tredicesima; le alterazioni sono passaggi.'),
 ('Dalla settima nel registro medio','G7b9',b(65,64,63,62,61,62,65,68),end(67,66,65,64,62,60,59),'La linea scende dalla settima e torna sulla terza Si.'),
 ('Nona aumentata e terza','G7b9',b(70,71,74,77,75,73,71,68),end(67,65,63,62,61,60,59),'La♯, nona aumentata, conduce a Si; Mi♭ è tredicesima minore.'),
 ('Nona naturale e cromatismi','G7',b(69,68,67,66,65,62,59,60),end(62,65,69,68,67,72,71),'La–La♭–Sol e Fa♯–Fa sono collegamenti brevi fra toni di G7.'),
 ('Risposta nel registro acuto','G7b9',b(None,74,77,81,80,79,77,74),end(72,70,71,69,67,65,71),'Pausa iniziale, salto verso la nona e ritorno alla terza.'),
]
P=[
 ('II–V–I: terze e settime',['Dm7','G7','Cmaj7','Cmaj7'],[b(65,69,72,76,74,72,71,69),b(65,64,63,62,61,60,59,62),b(64,67,71,74,72,71,69,67),end(65,64,62,63,64,67,72)],'Fa è terza del II e settima del V; Mi chiarisce l’arrivo sul I.','progressioni-ii-v-i'),
 ('II–V–I: risposta discendente',['Dm7','G7','Cmaj7','Cmaj7'],[b(62,65,69,72,71,70,69,67),b(69,68,67,65,63,62,61,59),b(60,64,67,71,72,74,71,67),end(69,67,66,67,64,62,60)],'La linea della dominante termina su Si e trova Do sulla tonica.','progressioni-ii-v-i'),
 ('II–V–I minore',['Dhalf','G7b9','Cm6','Cm6'],[b(65,68,72,74,72,68,67,65),b(68,71,74,77,75,73,71,67),b(69,67,63,62,60,63,67,69),end(60,63,67,71,72,67,63)],'La♭ definisce il II semidiminuito e il V♭9; Mi♭ chiarisce la tonica minore.','progressioni-minore'),
 ('Turnaround con VI7',['Cmaj7','A7','Dm7','G7'],[b(64,67,71,72,71,69,67,64),b(67,64,61,64,67,70,69,67),b(65,69,72,76,74,72,69,65),end(71,69,68,67,65,62,59)],'Do♯ identifica A7; il Si finale prepara un nuovo Do nel giro successivo.','progressioni-turnaround'),
 ('III–VI–II–V',['Em7','A7','Dm7','G7'],[b(67,71,74,78,76,74,71,67),b(67,69,70,72,73,76,79,76),b(74,72,69,65,64,65,69,72),end(71,69,68,67,65,62,59)],'Il motivo cambia accordo senza ripartire ogni volta dalla fondamentale.','progressioni-turnaround'),
 ('Dominante del VI',['E7','Am7','Dm7','G7'],[b(68,71,74,77,76,74,72,71),b(72,71,69,67,64,63,64,67),b(65,69,72,74,72,69,67,65),end(67,66,65,64,62,60,59)],'Sol♯ è terza di E7 e conduce verso La; Fa naturale ne colora la nona minore.','progressioni-dominanti'),
 ('Sostituto di tritono',['Dm7','Db7','Cmaj7','Cmaj7'],[b(65,69,72,74,72,69,67,65),b(65,68,71,74,73,71,68,65),b(64,67,71,72,71,69,67,64),end(62,63,64,67,71,62,60)],'Fa e Do♭ appartengono a D♭7; Mi apre la tonica successiva.','progressioni-tritono'),
 ('Ritorno backdoor',['Cmaj7','Fm7','Bb7','Cmaj7'],[b(64,67,71,74,72,71,67,64),b(68,72,75,79,77,75,72,68),b(62,65,68,72,70,68,67,65),end(64,67,69,70,71,74,72)],'La♭ e Mi♭ rendono udibile Fm7; Fa scende a Mi sul ritorno.','progressioni-backdoor'),
 ('Diminuito verso il II',['Cmaj7','Csdim','Dm7','G7'],[b(60,64,67,71,72,71,67,64),b(61,64,67,70,73,76,75,73),b(74,72,69,65,64,65,69,72),end(71,69,68,67,65,62,59)],'Do♯–Mi–Sol–Si♭ appartengono al diminuito; Do♯ conduce a Re.','progressioni-diminuito'),
 ('Due coppie V–I',['G7','Cmaj7','F7','Bbmaj7'],[b(71,74,77,76,74,72,71,69),b(67,64,62,63,64,67,71,72),b(69,72,75,79,77,75,74,72),end(74,77,81,84,82,81,77)],'Si–Do collega Sol a Do; La e Mi♭ sostengono poi il V di Si♭.','progressioni-centri'),
]
BLUES=[
 ('I7: terza blues e terza maggiore',['C7']*4,[b(60,63,64,67,70,69,67,64),b(65,64,63,60,62,63,64,67),b(70,69,68,67,65,64,62,60),end(63,64,67,70,69,67,60)],'Mi♭ si muove verso Mi naturale: il colore blues si collega alla terza del I7.','progressioni-blues','battute 1–4 del blues di base'),
 ('Quick change',['C7','F7','C7','C7'],[b(64,67,70,72,70,67,65,64),b(69,72,75,77,75,72,70,69),b(67,65,64,63,60,62,63,64),end(67,70,69,68,67,64,60)],'Mi su C7 diventa La su F7; Mi♭ distingue il IV7.','progressioni-blues-jazz','battute 1–4 del blues jazz'),
 ('Dal IV al I',['F7','F7','C7','C7'],[b(69,72,75,77,76,75,72,69),b(70,68,69,72,75,74,72,69),b(70,69,67,64,63,62,60,59),end(60,63,64,67,70,67,60)],'La e Mi♭ appartengono al IV7; il ritorno usa Mi naturale sul I7.','progressioni-blues','battute 5–8 del blues di base'),
 ('V–IV–I–V',['G7','F7','C7','G7'],[b(71,74,77,76,74,72,71,69),b(69,68,67,65,63,62,60,57),b(60,63,64,67,70,69,67,64),end(65,64,63,62,61,60,59)],'Le terze Si, La e Mi rendono udibile il cambio di funzione.','progressioni-blues','battute 9–12 del blues di base'),
 ('II–V nel ritorno jazz',['Dm7','G7','C7','G7'],[b(65,69,72,74,72,69,67,65),b(71,74,77,75,74,72,71,67),b(64,67,70,72,70,69,67,64),end(65,64,62,60,59,62,67)],'Il II–V prepara C7 come centro del blues, non Cmaj7.','progressioni-blues-jazz','variante delle battute 9–12 con G7 finale'),
 ('Tredicesima sul I7',['C7']*4,[b(69,67,64,62,60,63,64,67),b(70,69,67,65,64,63,62,60),b(64,67,69,72,70,69,67,65),end(64,63,60,62,63,64,60)],'La è tredicesima di C7; i passaggi Mi♭–Mi conservano il colore blues.','progressioni-blues','battute 1–4: alternativa a B01'),
 ('IV e diminuito',['F7','Fsdim','C7','A7'],[b(69,72,75,77,75,72,70,69),b(66,69,72,75,74,72,69,66),b(67,70,72,76,75,72,70,67),end(67,64,61,64,67,70,69)],'Fa♯–La–Do–Mi♭ segue il diminuito; Do♯ prepara A7.','progressioni-blues-jazz','battute 5–8 del blues jazz'),
 ('Colore minore al IV',['Cm6','Cm6','Fm7','Fm7'],[b(63,67,69,72,71,69,67,63),b(65,64,63,62,60,63,67,69),b(68,72,75,77,75,72,70,68),end(69,68,67,65,63,60,65)],'La naturale della tonica m6 lascia spazio a La♭ sul IV minore.','progressioni-blues-minore','battute 3–6 del blues minore'),
 ('Ritorno nel blues minore',['Ab7','G7','Cm6','G7'],[b(72,75,78,80,78,75,73,72),b(71,74,77,75,73,71,68,67),b(69,67,63,62,60,63,67,69),end(71,69,68,67,65,62,59)],'Do è terza di A♭7; Si chiarisce la dominante prima della tonica minore.','progressioni-blues-minore','battute 9–12 del blues minore'),
 ('Domanda e risposta blues',['C7','F7','C7','G7'],[b(None,63,64,67,70,67,65,64),b(None,68,69,72,75,72,70,69),b(70,69,67,64,63,60,62,64),end(65,64,62,60,59,62,67)],'La stessa idea ritmica cambia terza sul IV e prepara il V finale.','progressioni-blues','riduzione I7–IV7–I7–V7: esercizio, non un chorus intero'),
]

CATEGORIES={'M':'Maggiori','N':'Minori','D':'Dominanti','P':'Progressioni bebop','B':'Blues'}

def catalogue():
 result=[]
 for cat,rows,link in [('M',MAJOR,'progressioni-ii-v-i'),('N',MINOR,'progressioni-minore'),('D',DOMINANT,'progressioni-ii-v-i')]:
  for i,(title,key,a,z,tech) in enumerate(rows,1):result.append(seed(cat,i,title,[key,key],[a,z],tech,link))
 for i,(title,keys,bars,tech,link) in enumerate(P,1):result.append(seed('P',i,title,keys,bars,tech,link))
 for i,(title,keys,bars,tech,link,placement) in enumerate(BLUES,1):
  item=seed('B',i,title,keys,bars,tech,link);item['placement']=placement;result.append(item)
 return result

# Playback/naming reuse the authored progression chord vocabulary; add C6 only.
BACKING=dict(CHORDS)
BACKING['C6']=dict(label='C6',voices=((5,3,48),(4,2,52),(3,2,57)),spell={},shell=True)

def finger(pitch,previous=None):
 # A consistent reference position keeps semitone lines on adjacent frets.
 # The high register continues on the first string instead of drifting to low strings.
 if pitch < 60:
  string=4
 elif pitch <= 63:
  string=3
 elif pitch <= 68:
  string=2
 else:
  string=1
 fret=pitch-OPEN[string]
 assert 2<=fret<=20,(pitch,string,fret)
 return string,fret


def spelling(lick,pitch,key):
 # Functional spellings for chromatic approaches and applied dominants.
 overrides={}
 if lick['category']=='M':overrides.update({63:"ds'",66:"fs'",68:"gs'"})
 if lick['category']=='N':overrides[66]="fs'"
 if key in ('Em7','Gmaj7') and pitch==78:overrides[78]="fs''"
 if key=='A7':overrides.update({61:"cs'",73:"cs''",70:"bf'"})
 if key=='E7':overrides.update({68:"gs'",80:"gs''"})
 if key in ('G7','G7b9') and pitch in (66,78):overrides[pitch]='fs'+("'" if pitch==66 else "''")
 if key in ('G7','G7b9') and pitch==70:overrides[70]="as'"
 if key=='Db7':overrides.update({71:"cf''",73:"df''",74:"eff''"})
 if key=='Csdim':overrides.update({61:"cs'",73:"cs''"})
 if key=='Fsdim':overrides[66]="fs'"
 return overrides.get(pitch,pitch_name(pitch))

def swing_position(slot):
 return Fraction(slot//2,1)+(Fraction(2,3) if slot%2 else 0)

def duration(units):return {1:'8',2:'4',3:'4.',4:'2',6:'2.',8:'1'}[units]

def melodies(lick):
 printed=[];played=[];previous=None
 for i,(key,bar) in enumerate(zip(lick['keys'],lick['bars'])):
  a=[];z=[];slot=0
  for j,(pitch,units) in enumerate(bar):
   if pitch is None:token='r'
   else:
    string,fret=finger(pitch,previous);previous=(string,fret)
    token=spelling(lick,pitch,key)+f'\\{string}'
   label=f'^\\markup {{ \\small "{BACKING[key]["label"]}" }}' if j==0 else ''
   # Duration follows pitch before string annotation in LilyPond.
   if pitch is None:a.append('r'+duration(units)+label)
   else:a.append(spelling(lick,pitch,key)+duration(units)+f'\\{string}'+label)
   whole=(swing_position(slot+units)-swing_position(slot))/4
   z.append(token.split('\\')[0]+f'1*{whole.numerator}/{whole.denominator}')
   slot+=units
  printed.append(' '.join(a)+' |')
  played.append(' '.join(z)+' |')
 return '\n'.join(printed),'\n'.join(played)

def backing(lick):
 bars=[]
 for key in lick['keys']:
  c=BACKING[key]
  notes=' '.join(c['spell'].get(p) or pitch_name(p) for s,f,p in c['voices'])
  bars.append('<'+notes+'>1 |')
 return '\n'.join(bars)

def source(lick):
 printed,played=melodies(lick)
 return rf"""% Generated by scripts/generate_bebop_licks.py; edit the generator.
\version "2.26.0"
\language "english"
\header {{ title = "{lick['id']} - {lick['title']}" tagline = ##f }}
\paper {{ page-breaking = #ly:one-page-breaking line-width = 160\mm ragged-right = ##f }}
notation = \absolute {{ \time 4/4 \key c \major {printed} \bar "|." }}
playback = \absolute {{ \time 4/4 {played} \bar "|." }}
backing = \absolute {{ \time 4/4 {backing(lick)} \bar "|." }}
\score {{
 \new StaffGroup <<
  \new Staff {{ \clef "treble_8" \tempo \markup {{ "Swing" }} 4 = 90 \notation }}
  \new TabStaff {{ \set TabStaff.stringTunings = #guitar-tuning \omit TextScript \notation }}
 >>
 \layout {{ indent = 0 system-count = #1
  \context {{ \Voice \override TextScript.staff-padding = #2 }}
  \context {{ \Score \omit StringNumber }} }}
}}
\score {{
 <<
  \new Staff {{ \tempo 4 = 90 c'''4\p c''' c''' c''' \mf \playback }}
  \new Staff {{ \tempo 4 = 90 r1 \pp \backing }}
 >>
 \midi {{ }}
}}
"""

CATEGORY_NOTES={
 'M':('licks-maggiori','Accordi maggiori','Usa M01–M10 su Cmaj7 o C6 come indicato nella singola griglia. M01, M02 e gli altri esempi Cmaj7 entrano nelle due battute di tonica del II–V–I maggiore. Per i due esempi C6 scegli esplicitamente quel colore di tonica.'),
 'N':('licks-minori','Accordi minori','Distingui Cm7, Cm6 e Cm(maj7): ogni lick dichiara la propria sonorità. Per studiare una frase statica prolunga quell’accordo per due battute; non sovrapporla senza controllo ai cambi del II–V–I minore.'),
 'D':('licks-dominanti','Accordi dominanti','Questi dieci esempi lavorano su due battute di G7, con nona minore quando indicata. Se nel giro G7 dura una sola battuta, estrai una cellula. La frase può terminare su un tono del V e trovare il completamento sul Do dell’accordo successivo.'),
 'P':('licks-progressioni','Progressioni bebop tipiche','Le frasi seguono quattro battute con accordi diversi: II–V–I, turnaround, dominanti secondarie, tritono, backdoor e cambi di centro. Leggi la variante scritta qui e confrontala con il percorso collegato in Progressioni.'),
 'B':('licks-blues','Blues','Ogni frase ha quattro battute. Il testo indica la finestra della forma o la variante: blues di base, jazz, minore o una riduzione didattica. Prima conta il chorus, poi scegli dove entrare.'),
}

def chapter_catalogue():
 parts=[]
 for cat in CATEGORIES:
  anchor,heading,intro=CATEGORY_NOTES[cat]
  parts.append(f'.. _{anchor}:\n\n{heading}\n'+ '-'*(len(heading)+2)+'\n\n'+intro+'\n\n')
  items=[lick for lick in catalogue() if lick['category']==cat]
  parts.append(' · '.join(f":ref:`{l['id']} <lick-{l['id'].lower()}>`" for l in items)+'\n\n')
  for lick in items:
   heading=lick['id']+' — '+lick['title']
   keys=' | '.join(BACKING[key]['label'] for key in lick['keys'])
   target=next(p for bar in reversed(lick['bars']) for p,u in reversed(bar) if p is not None)
   names=['Do','Re♭','Re','Mi♭','Mi','Fa','Sol♭','Sol','La♭','La','Si♭','Si']
   final_note=names[target%12]
   parts.append(f".. _lick-{lick['id'].lower()}:\n\n{heading}\n"+'~'*(len(heading)+2)+'\n\n')
   parts.append(f"**Contesto:** | {keys} | — **{len(lick['bars'])} battute**. **Ultima nota:** {final_note}.\n\n")
   parts.append(lick['tech']+'\n\n')
   if lick['id']=='P07':parts.append('Mi doppio bemolle nel secondo accordo suona Re naturale: è la nona minore di Re♭7.\n\n')
   if 'placement' in lick:parts.append('**Nella forma:** '+lick['placement']+'.\n\n')
   parts.append(f"**Dove provarlo:** :ref:`{lick['link']}`.\n\n")
   parts.append(f".. image:: _static/music/{lick['stem']}.*\n   :width: 100%\n\n.. raw:: html\n\n   <audio controls class=\"audio-controls\" preload=\"none\">\n      <source src=\"_static/music/{lick['stem']}.mp3\" type=\"audio/mpeg\">\n   </audio>\n\n")
 return ''.join(parts)

def update_chapter_catalogue():
 path=ROOT/'src/docs/8-licks.rst'
 text=path.read_text()
 start='.. BEGIN GENERATED LICKS CATALOGUE'
 end='.. END GENERATED LICKS CATALOGUE'
 if start in text:
  before,rest=text.split(start,1);_,after=rest.split(end,1)
  path.write_text(before+start+'\n\n'+chapter_catalogue()+end+after)


def main():
 licks=catalogue();assert len(licks)==50
 for lick in licks:(ROOT/'src/lilypond'/f"{lick['stem']}.ly").write_text(source(lick))
 update_chapter_catalogue()
 print('Generated fifty original licks: ten per category.')
if __name__=='__main__':main()
