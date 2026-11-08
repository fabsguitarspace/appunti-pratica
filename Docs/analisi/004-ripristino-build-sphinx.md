# Ripristino build Sphinx

Data: 2026-11-08. Intervento eseguito su entrambi i progetti.

- Ripristinati gli ambienti locali dopo lo spostamento dei repository; selezionato Python 3.13 per la verifica locale.
- Fissate le dipendenze dirette: Sphinx 8.2.3 e Shibuya 2026.1.9. Le dipendenze transitive non sono bloccate: non è un lock completo.
- `build.sh` individua la radice del progetto, usa Python dell'ambiente locale se presente e richiama Sphinx come modulo, evitando gli avviatori con percorsi obsoleti. Gli avvisi causano esito negativo e la compilazione prosegue per raccoglierli.
- Corrette le directory del Makefile: sorgenti nella directory corrente, output in `../../out`. Stessa correzione nel comando Windows presente in Teoria.
- Rimossa la dichiarazione Markdown senza parser; i contenuti pubblicati esistenti sono RST. La KB Markdown resta fuori dalla build.

## Validazione

Build HTML pulita di entrambi i progetti con `-E -a -W --keep-going`, output isolati sotto `/private/tmp/appunti-final-pratica` e `/private/tmp/appunti-final-teoria`: entrambe riuscite senza avvisi. Verificata sintassi shell di `build.sh` e avvio Sphinx tramite Python locale. Non eseguita validazione visiva, PDF/ePub o build Windows. Read the Docs resta configurato con Python 3.12: la verifica locale su 3.13 non equivale a una prova remota su 3.12.

Per preparare un ambiente dopo un nuovo checkout: creare `.venv` con una versione Python compatibile e installare `requirements.txt`; eseguire `sh build.sh`. I percorsi interni degli ambienti virtuali non sono portabili: dopo uno spostamento vanno ricreati.

## Lavoro successivo

Restano separati gli interventi sulla pipeline musicale: dipendenze degli output, recupero dei MIDI mancanti, gestione dei risultati parziali e verifica SVG nativo. Nessuna modifica agli script musicali in questo intervento.
