#!/usr/bin/env python3
"""Generate the editorial artist paths in Pratica and the companion in Teoria."""
from pathlib import Path
from artist_profiles import PROFILES
from generate_artist_studies import GROUPS,H
ROOT=Path(__file__).resolve().parents[1]
THEORY=ROOT.parent/'appunti-teoria'
PRACTICE_URL='https://appunti-pratica-per-chitarra-jazz.readthedocs.io/it/latest/'
THEORY_URL='https://appunti-di-teoria-e-armonia-per-chitarra-jazz.readthedocs.io/it/latest/'

def heading(title,level='-'):return title+'\n'+level*len(title)+'\n\n'
def audio(stem,label):
 return f'''.. raw:: html

   <audio controls preload="none" aria-label="{label}">
     <source src="../_static/music/{stem}.mp3" type="audio/mpeg">
   </audio>

'''
def chapter():
 text=heading('Percorsi d’autore','=')+'''Ascoltare un musicista significa seguire le sue scelte nel tempo: come
costruisce una frase, dialoga, accompagna e trasforma il materiale.
Questi dieci percorsi collegano l’ascolto allo studio della chitarra.
Ogni percorso comprende **cinque esercizi progressivi e uno studio
conclusivo originale**: sessanta esempi con pentagramma, TAB e audio.
Gli studi conclusivi hanno anche una base per lavorare autonomamente.

Gli esempi sono **composizioni didattiche originali** sui concetti discussi,
non trascrizioni delle registrazioni né frasi attribuite agli artisti.
Gli ascolti indicano il repertorio con cui confrontare le idee. Si parte
da alcuni aspetti del linguaggio di ciascun musicista, senza ricondurre
a una sola formula l’intera carriera. Il suono sintetico degli esempi
serve a verificare altezze, ritmo e forma; non replica timbro, inflessioni
o interazione delle esecuzioni di riferimento.

Come organizzare lo studio
-------------------------

#. Ascolta la versione indicata una volta per la forma e una per il dettaglio richiesto.
#. Canta una frase breve, poi descrivine ritmo, registro e punti di arrivo.
#. Leggi l’analisi e studia l’esercizio lentamente, una difficoltà alla volta.
#. Confronta il tuo risultato con l’obiettivo, quindi cambia una sola variabile.
#. Esegui lo studio conclusivo e registra una variante personale sulla base.

Puoi distribuire le cinque attività su più sessioni. Non serve affrontare
tutti i percorsi in ordine: verifica i prerequisiti indicati nella pagina.
Per ogni ascolto annota interpreti, titolo, album/versione e il punto che
hai scelto. Le ristampe possono avere take alternative: usa la versione
principale indicata e aggiungi il tuo minutaggio soltanto dopo averla
identificata. I collegamenti alle fonti conducono a cataloghi, discografie
o pagine degli artisti; l’ascolto integrale dipende dal servizio scelto.

Lettura e audio
--------------

La chitarra è scritta in chiave di violino ottavizzata, con TAB in
accordatura standard. I numeri indicano tasti, non dita. Nelle ottave
si devono smorzare le corde intermedie; le voci sovrapposte di Joe Pass
richiedono di rispettare le durate indipendenti e le corde indicate.
Le posizioni sono soluzioni di riferimento, da adattare con criterio.

Ogni esempio parte dopo **una battuta di conteggio** al charleston:
quattro quarti in 4/4, cinque quarti in 5/4, sette crome in 7/8.
Il tempo ordinario è semiminima = **76**; i due esempi in 7/8 del
percorso McLaughlin sono a semiminima = **84**. La descrizione di ogni
esercizio specifica metro e interpretazione ritmica.

Negli esempi swing le crome sono scritte convenzionalmente e riprodotte
con rapporto **2:1**, comprese quelle del ride; il rapporto è un modello
di studio, non una misura universale dello swing. Negli altri esempi
crome e semicrome sono regolari. Non eseguire automaticamente lo swing
sui passaggi indicati come regolari e non riprodurre insieme due lettori.

Le versioni complete comprendono chitarra, sostegno armonico, basso e
batteria. **Nel percorso Joe Pass sono per sola chitarra**, dopo il
conteggio iniziale. Le basi finali degli altri nove percorsi tolgono
la chitarra scritta e conservano la sezione ritmica; quella di Joe Pass
fornisce soltanto quattro impulsi per battuta, perché basso e accordi
devono essere eseguiti da te. Ogni audio percorre la forma una volta;
attendi la coda e il nuovo conteggio prima di ricominciare.

Per le relazioni armoniche e ritmiche consulta `Ascoltare e analizzare
i percorsi d’autore nel volume di Teoria
<'''+THEORY_URL+'''13-percorsi-autore.html>`_.

Scegliere un percorso
--------------------

.. list-table::
   :header-rows: 1
   :widths: 25 50 25

'''
 for p in PROFILES:
  text+=f'   * - :doc:`autori/{p["id"]}`\n     - {p["focus"]}\n     - Cinque esercizi + studio finale\n'
 text+='\n.. toctree::\n   :maxdepth: 1\n   :hidden:\n\n'+''.join(f'   autori/{p["id"]}\n' for p in PROFILES)
 text+='\n'+heading('Collegare i percorsi')+'''Da :doc:`7-progressioni` scegli il contesto; da :doc:`8-licks` un nucleo
melodico; dai percorsi d’autore ricava un modo per svilupparlo, articolarlo
o distribuirlo fra le voci. :doc:`9-modern-jazz-fusion` prepara vamps,
sovrapposizioni e lavoro ritmico per Metheny, Scofield e McLaughlin.
Una stessa progressione può essere affrontata da più percorsi: confronta
Hall e Pass per l’armonia, Christian e Martino per il II–V–I, Benson e
Scofield per blues e groove, Montgomery per la crescita della tessitura.
'''
 return text

def author_page(profile,studies):
 p=profile;text=f'.. _autore-{p["id"]}:\n\n'+heading(p['name'],'=')+p['intro']+'\n\n'
 text+=heading('Obiettivi e prerequisiti')+'**Obiettivo:** '+p['focus']+'.\n\n'
 text+='Riprendi '+', '.join(f':doc:`{label} <../{doc}>`' for doc,label in p['links'])+'. '
 text+=f'Per l’analisi consulta `il percorso in Teoria <{THEORY_URL}13-percorsi-autore.html#autore-{p["id"]}>`_.\n\n'
 text+=heading('Ascolti guidati')
 for title,task in p['listens']:text+='**'+title+'**\n\n'+task+'\n\n'
 text+='Fonti e accesso agli ascolti: '+', '.join(f'`{label} <{url}>`_' for label,url in p['sources'])+'.\n\n'
 text+=heading('Che cosa osservare')+p['analysis']+'\n\n**Confronto:** '+p['compare']+'\n\n'
 for s in studies:
  n=s['number'];title=f'{n:02} — '+s['title']
  text+=f'.. _autore-{p["id"]}-{n:02}:\n\n'+heading(title)
  meter='/'.join(map(str,s['meter']));feel='crome swing 2:1' if s['swing'] else 'suddivisioni regolari'
  text+=f'**{len(s["bars"])} battute in {meter}; semiminima = {s["bpm"]}; {feel}.** '
  if s['groups']:text+='Raggruppamento: '+' + '.join(map(str,s['groups']))+(' crome. ' if meter=='7/8' else ' semiminime. ')
  text+='Una sigla per battuta.\n\n'
  text+='**Griglia:** ``| '+' | '.join(H[k][2] for k in s['keys'])+' |``.\n\n'
  text+=s['explain']+'\n\n**Al lavoro:** '+s['task']+'\n\n'
  text+=f'.. image:: ../_static/music/{s["stem"]}.*\n   :alt: {p["name"]}, esercizio originale {n:02}: {s["title"]}\n\n'
  text+=audio(s['stem'],f'{p["name"]}, esempio originale {n:02}')
  if n==6:
   text+=('**Riferimento ritmico per eseguire tutte le parti della chitarra:**\n\n' if s['solo'] else '**Base senza la chitarra scritta:**\n\n')+audio(s['stem']+'-base',f'Base dello studio conclusivo, percorso {p["name"]}')
 text+=heading('Autovalutazione e approfondimento')+p['criterion']+'\n\n'+p['continuation']+'\n\n'
 text+='Per passare a un altro linguaggio, torna a :doc:`../10-percorsi-autore` e\nscegli un percorso che cambi una sola dimensione del tuo studio attuale.\n'
 return text

def theory_chapter():
 text=heading('Ascoltare e analizzare i percorsi d’autore','=')+'''I concetti dei capitoli precedenti diventano più chiari quando li
riconosciamo nelle scelte di un musicista: un punto di arrivo, una pausa,
un rapporto fra le voci o una diversa organizzazione del tempo. Questo
capitolo accompagna i dieci percorsi del volume di Pratica con analisi
di esempi originali e domande da portare all’ascolto.

Le analisi qui sotto riguardano **i nostri esercizi**, non pretendono di
trascrivere o spiegare integralmente gli assoli citati. Nelle pagine di
Pratica trovi le versioni di riferimento, le fonti discografiche, cinque
esercizi progressivi e uno studio conclusivo per ciascun artista.
I sessanta esempi hanno spartito, tablatura e audio; le dieci basi finali
permettono di lavorare in autonomia. Il materiale non esaurisce né
uniforma carriere che comprendono contesti e periodi differenti.

Un metodo di analisi
-------------------

#. Identifica la registrazione e separa tema, solo e accompagnamento.
#. Canta una frase breve e descrivine attacchi, pause, registro e conclusione.
#. Scrivi le note reali e i loro gradi rispetto al basso e all’accordo.
#. Distingui note dell’accordo, tensioni, approcci e punti di riposo.
#. Verifica che una lettura armonica corrisponda alla durata e alla posizione ritmica.
#. Trasforma una sola relazione e confronta il risultato con l’idea di partenza.

Una nota comune può cambiare funzione; un voicing parziale non equivale
alla sigla completa; un accento spostato non cambia necessariamente metro.
Per le tre questioni riprendi rispettivamente :doc:`6-armonia-funzionale`,
:doc:`5-accordi` e :doc:`12-ritmo-sviluppo`.

'''
 for p in PROFILES:
  text+=f'.. _autore-{p["id"]}:\n\n'+heading(p['name'])+'**Fuoco dell’analisi:** '+p['focus']+'.\n\n'+p['analysis']+'\n\n'
  text+='**Verifica all’ascolto e sullo strumento:** '+p['compare']+'\n\n'
  text+='Riprendi '+', '.join(f':doc:`{doc}`' for doc in p['theory'])+'. '
  text+=f'Continua con `Ascolti e studi del percorso {p["name"]} in Pratica <{PRACTICE_URL}autori/{p["id"]}.html>`_.\n\n'
 text+=heading('Confrontare senza uniformare')+'''Scegli un II–V–I e prepara tre versioni: bersagli in una linea singola,
risposte a due voci, basso e canto indipendenti. Confronta Christian,
Hall e Pass come ingressi didattici differenti. Poi mantieni una frase
e cambiane soltanto tessitura, pensando al lavoro sulle ottave del
percorso Montgomery. Valuta quali relazioni diventano più udibili.

Sul blues confronta le terze, le pause e i punti di rientro dei percorsi
Benson e Scofield; su un pedale confronta arco melodico e organizzazione
ritmica nei percorsi Metheny e McLaughlin. Nel lavoro sugli arpeggi
confronta la dominante diminuita del percorso Django e l’area minore
riletta sulla dominante in quello Martino: scrivi prima gli intervalli,
perché procedure diverse non producono automaticamente le stesse note.

Un confronto utile conserva contesto e tempo mentre modifica una scelta.
Se cambi insieme tonalità, accordi, ritmo e registro, diventa difficile
capire da quale decisione dipenda il risultato. Torna infine a
:doc:`11-letture-armoniche` e aggiungi alle sigle una mappa del fraseggio.
'''
 return text

def normalize(text):
 lines=text.splitlines()
 for i,line in enumerate(lines):
  if i and line and len(set(line))==1 and line[0] in '-=~' and lines[i-1]:
   lines[i]=line[0]*len(lines[i-1])
 return '\n'.join(lines)+'\n'

def main():
 (ROOT/'src/docs/10-percorsi-autore.rst').write_text(normalize(chapter()))
 for profile,studies in zip(PROFILES,GROUPS):
  assert all(s['artist']==profile['id'] for s in studies)
  (ROOT/f'src/docs/autori/{profile["id"]}.rst').write_text(normalize(author_page(profile,studies)))
 (THEORY/'src/docs/13-percorsi-autore.rst').write_text(normalize(theory_chapter()))
 print('Generated 10 artist paths, Pratica overview and Teoria companion.')
if __name__=='__main__':main()
