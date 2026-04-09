project = "Appunti di Pratica per Chitarra Jazz"
author = "Fabrizio's Guitar Space"
copyright = "youtube.com/@fabsguitarspace"
release = "0.1"

extensions = [
    "myst_parser",
    "sphinxnotes.lilypond",
    "sphinx.ext.imgconverter",
]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

language = "it"

html_theme = "sphinx_book_theme"
html_static_path = ["_static"]
html_title = "Appunti di Pratica per Chitarra Jazz"
html_show_copyright = False
html_show_sphinx = False
html_logo = "_static/logo.png"

html_theme_options = {
    "logo_target": "https://example.com",
    "use_download_button": False
}
html_css_files = ["custom.css"]
# Facoltativo: migliora la navigazione del tema
html_theme_options = {
}

latex_engine = 'lualatex'  # gestisce meglio i font Unicode se hai testo musicale


