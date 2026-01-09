"""Sphinx configuration for sphinx-needs-tree-map documentation."""

import os
import sys
from datetime import datetime

# Add the project root to the path for autodoc
sys.path.insert(0, os.path.abspath(".."))

from sphinx_needs_tree_map import __version__

# -- Project information -----------------------------------------------------
project = "sphinx-needs-tree-map"
copyright = f"{datetime.now().year}, patdhlk"
author = "patdhlk"
version = __version__
release = __version__

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
    "sphinx_copybutton",
    "sphinx_design",
    "myst_parser",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------
html_theme = "furo"
html_title = "sphinx-needs-tree-map"
html_static_path = ["_static"]

html_theme_options = {
    "source_repository": "https://github.com/patdhlk/sphinx-needs-tree-map",
    "source_branch": "main",
    "source_directory": "docs/",
    "light_css_variables": {
        "color-brand-primary": "#2962FF",
        "color-brand-content": "#2962FF",
    },
    "dark_css_variables": {
        "color-brand-primary": "#82B1FF",
        "color-brand-content": "#82B1FF",
    },
}

# -- Options for autodoc -----------------------------------------------------
autodoc_default_options = {
    "members": True,
    "member-order": "bysource",
    "special-members": "__init__",
    "undoc-members": True,
    "exclude-members": "__weakref__",
}

autodoc_typehints = "description"
autodoc_typehints_description_target = "documented"
autodoc_class_signature = "separated"

# -- Options for intersphinx -------------------------------------------------
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master", None),
    "sphinx-needs": ("https://sphinx-needs.readthedocs.io/en/latest", None),
}

# -- Options for MyST parser -------------------------------------------------
myst_enable_extensions = [
    "colon_fence",
    "deflist",
]

# -- Options for copybutton --------------------------------------------------
copybutton_prompt_text = r">>> |\.\.\. |\$ "
copybutton_prompt_is_regexp = True
