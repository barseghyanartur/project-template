# Sphinx configuration for {{ project_name }} documentation
#
# This file is skeletons for your project. Adapt it to your needs.

import os
import sys

# -- Path setup --------------------------------------------------------------

sys.path.insert(0, os.path.abspath("../src"))

# -- Project information -----------------------------------------------------

project = "{{ project_name }}"
copyright = "{{ current_year }}, {{ author_name }}"
author = "{{ author_name }}"
version = "0.1.0"
release = "0.1.0"

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------

html_theme = "alabaster"
html_static_path = ["_static"]

# -- Options for intersphinx -------------------------------------------------

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

# -- Options for autodoc -----------------------------------------------------

autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "show-inheritance": True,
}
