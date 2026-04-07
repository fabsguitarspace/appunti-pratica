project = "Titolo del libro"
author = "Nome Autore"
copyright = "2026, Nome Autore"
release = "0.1"

extensions = []

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

language = "it"

html_theme = "furo"
html_static_path = ["_static"]
html_title = "Titolo del libro"

# Facoltativo: migliora la navigazione del tema
html_theme_options = {
    "sidebar_hide_name": False,
}