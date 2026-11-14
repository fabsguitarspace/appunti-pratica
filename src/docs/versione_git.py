"""Versione e data di aggiornamento ricavate dalla storia git.

Copia identica nei tre volumi (Teoria, Pratica, Repertorio): una modifica va riportata in tutti.

- MAJOR.MINOR è scritto a mano in conf.py, nella riga ``VERSIONE = "X.Y"``.
- PATCH è il numero di commit successivi all'ultimo commit che ha cambiato quella riga.
  Ogni push su main fa quindi avanzare la patch; cambiare la riga (per esempio da "1.1"
  a "1.2") fa ripartire la patch da 0.
- La data è quella dell'ultimo commit, non quella della build, così la stessa revisione
  produce sempre la stessa versione e la stessa data.

Read the Docs clona il repository con una storia parziale: ``.readthedocs.yaml`` la
completa (``git fetch --unshallow``) prima della build, altrimenti il conteggio sarebbe
sbagliato. Senza git, o con una storia parziale, la versione resta ``X.Y`` e la data è
quella della build.
"""
import datetime
import subprocess
from pathlib import Path

MESI = ["gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno", "luglio",
        "agosto", "settembre", "ottobre", "novembre", "dicembre"]


def _git(cartella, *args):
    try:
        out = subprocess.run(["git", *args], cwd=cartella, capture_output=True,
                             text=True, check=True, timeout=30)
    except (OSError, subprocess.SubprocessError):
        return None
    return out.stdout.strip()


def _storia_completa(cartella):
    return _git(cartella, "rev-parse", "--is-shallow-repository") == "false"


def versione(base, conf_py):
    """``base`` = "X.Y" letto da conf.py; restituisce "X.Y.PATCH" (o "X.Y" senza storia)."""
    conf_py = Path(conf_py).resolve()
    cartella = conf_py.parent
    if not _storia_completa(cartella):
        return base
    commit = _git(cartella, "log", "-1", "--format=%H", "-G", r'^VERSIONE = "', "--", conf_py.name)
    if not commit:
        return base + ".0"   # riga non ancora committata
    patch = _git(cartella, "rev-list", "--count", f"{commit}..HEAD")
    return f"{base}.{patch}" if patch is not None else base


def data_aggiornamento(conf_py):
    """Data dell'ultimo commit in italiano, es. "14 novembre 2026"."""
    iso = _git(Path(conf_py).resolve().parent, "log", "-1", "--format=%cs")
    try:
        giorno = datetime.date.fromisoformat(iso)
    except (TypeError, ValueError):
        giorno = datetime.date.today()
    return f"{giorno.day} {MESI[giorno.month - 1]} {giorno.year}"
