project = "Appunti di Pratica per Chitarra Jazz"
author = "Fabrizio's Guitar Space"
copyright = ""
release = "0.1"

extensions = [
    "myst_parser",
]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

language = "it"

html_theme = "shibuya"
html_static_path = ["_static"]
html_title = "Appunti di Pratica per Chitarra Jazz"
html_show_copyright = False
html_show_sphinx = False
html_logo = "_static/logo.png"

html_theme_options = {
    "logo_target": "https://example.com",
}
html_css_files = ["custom.css"]
# Facoltativo: migliora la navigazione del tema
html_theme_options = {
    "sidebar_hide_name": False,
}

