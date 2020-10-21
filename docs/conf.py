# pylint: disable-all
# type: ignore

project = "template-python-vscode"
copyright = "2020, Blake Naccarato"
author = "Blake Naccarato"
extensions = ["sphinx.ext.napoleon", "sphinx.ext.autodoc"]
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
