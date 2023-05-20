"""Sphinx configuration."""
project = "Panti"
author = "Nutchanon Ninyawee"
copyright = "2023, Nutchanon Ninyawee"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
