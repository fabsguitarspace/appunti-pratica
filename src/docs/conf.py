project = "Appunti di Pratica per Chitarra Jazz"
author = "Fabrizio's Guitar Space"
copyright = "youtube.com/@fabsguitarspace"
release = "0.1"

extensions = [
    "sphinx.ext.imgconverter",
]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
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
    "nav_links": [
    		{
    			"title": "Appunti di Pratica",
    			 "url": "index"
    		},
    		{
    			"title": "Appunti di Teoria",
    			 "url": "https://docs.google.com/document/d/1PsSj1DAIIWZE3kTeEPlP5KFYDZARa8qKCm0nHit_XnM/edit?tab=t.0"
    		},
        {
            "title": "Fabrizio's Guitar Space",
            "url": "https://youtube.com/@fabsguitarspace",
            "external": True,
        },
    ],
    "youtube_url": "https://youtube.com/@fabsguitarspace",
    "discord_url": "https://discord.gg/DjwCcuS7SA",
    "announcement": "Il contenuto di questo sito è attualmente in stato di <b>bozza</b>. <i>Ti consiglio</i> di <b>non scaricare</b> i contenuti ma di tornare nei prossimi giorni per trovare nuovi aggiornamenti"
}

html_permalinks_icon = "<span>¶</span>"

html_css_files = ["custom.css"]
# Facoltativo: migliora la navigazione del tema

latex_engine = 'lualatex'  # gestisce meglio i font Unicode se hai testo musicale


