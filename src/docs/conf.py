import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from versione_git import data_aggiornamento, versione  # noqa: E402

project = "Appunti di Pratica per Chitarra Jazz"
author = "Fabrizio's Guitar Space"
copyright = "youtube.com/@fabsguitarspace"
# Versione MAJOR.MINOR, scritta a mano: cambiarla fa ripartire la patch da 0.
# La patch conta i commit successivi e la data è quella dell'ultimo commit (versione_git.py).
VERSIONE = "1.1"
version = VERSIONE
release = versione(VERSIONE, __file__)
today = data_aggiornamento(__file__)

extensions = [
    "sphinx.ext.extlinks",
    "sphinx.ext.imgconverter",
]

# Strumenti per la pratica (ADR 0005): pubblicati su GitHub Pages dal repository
# appunti-strumenti. L'indirizzo base è definito solo qui; i link del capitolo usano
# il ruolo :strumento:`testo <pagina#v=1&...>` (schema in appunti-strumenti/Docs/deep-link.md).
strumenti_url = "https://fabsguitarspace.github.io/appunti-strumenti/"
extlinks = {"strumento": (strumenti_url + "%s", None)}

source_suffix = {
    ".rst": "restructuredtext",
}

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

language = "it"

html_theme = "shibuya"
html_static_path = ["_static"]
html_title = "Appunti di Pratica per Chitarra Jazz"
html_show_copyright = False
html_show_sphinx = False
html_logo = "_static/logo_256.png"

html_theme_options = {
    "accent_color": "red",  # colore del volume, coerente con il logo della homepage
    "nav_links": [
        {
            "title": "Appunti di Teoria",
            "url": "https://appunti-di-teoria-e-armonia-per-chitarra-jazz.readthedocs.io"
        },
        {
            "title": "Appunti di Pratica",
            "url": "index"
        },
        {
            "title": "Appunti di Repertorio",
            "url": "https://appunti-di-repertorio-per-chitarra-jazz.readthedocs.io"
        },
        {
            "title": "Fabrizio's Guitar Space",
            "url": "https://youtube.com/@fabsguitarspace",
            "external": True,
        },
    ],
    "youtube_url": "https://youtube.com/@fabsguitarspace",
    "discord_url": "https://discord.gg/DjwCcuS7SA",
    # Sidebar sinistra: mostra anche le sezioni di ogni capitolo (espandibili
    # con la freccia), non solo le pagine figlie. Profondità 2 = capitolo +
    # sezioni di primo livello (o pagine figlie, come in Percorsi d'autore).
    "toctree_titles_only": False,
    "toctree_maxdepth": 2,
}

html_permalinks_icon = "<span>¶</span>"

html_css_files = ["custom.css"]
# Aggiunge ai link verso gli strumenti il tema chiaro/scuro corrente (ADR 0005, punto 7).
html_js_files = [("strumenti.js", {"defer": "defer", "data-base": strumenti_url})]
# Facoltativo: migliora la navigazione del tema

latex_engine = 'lualatex'  # gestisce meglio i font Unicode se hai testo musicale



# Nel frontespizio del PDF: «Versione 1.1.3» invece di «Release 1.1.3».
latex_elements = {"releasename": "Versione"}
