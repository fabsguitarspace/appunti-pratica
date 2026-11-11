project = "Appunti di Pratica per Chitarra Jazz"
author = "Fabrizio's Guitar Space"
copyright = "youtube.com/@fabsguitarspace"
release = "0.1"

extensions = [
    "sphinx.ext.imgconverter",
]

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
}

html_permalinks_icon = "<span>¶</span>"

html_css_files = ["custom.css"]
# Facoltativo: migliora la navigazione del tema

latex_engine = 'lualatex'  # gestisce meglio i font Unicode se hai testo musicale


