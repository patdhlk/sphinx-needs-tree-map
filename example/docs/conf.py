# Configuration file for the Sphinx documentation builder.
#
# Task Management System - Example Documentation
# Demonstrates sphinx-needs-tree-map extension

# -- Project information -----------------------------------------------------
project = "Task Management System"
copyright = "2025, Example Corp"
author = "Example Corp"
release = "1.0.0"

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx_needs",
    "sphinx_needs_tree_map",
]

# -- Sphinx-needs configuration ----------------------------------------------
# Load sphinx-needs configuration from ubproject.toml
# All needs_* settings (types, extra_options, extra_links, statuses, etc.)
# are defined in ubproject.toml under the [needs] section.
needs_from_toml = "ubproject.toml"

# -- sphinx-needs-tree-map configuration ------------------------------------
# Color mapping for need types
needtreemap_colors = {
    "req": "#E3F2FD",       # Light blue for requirements
    "spec": "#FFF3E0",      # Light orange for specifications
    "impl": "#E8F5E9",      # Light green for implementations
    "test": "#FFF9C4",      # Light yellow for tests
    "story": "#F3E5F5",     # Light purple for user stories
    "default": "#ECEFF1",   # Light grey for unknown types
}

# Color mapping for status values
needtreemap_status_colors = {
    "open": "#FFCDD2",           # Light red
    "in_progress": "#FFE0B2",    # Light orange
    "implemented": "#C8E6C9",    # Light green
    "verified": "#B2DFDB",       # Light teal
    "default": "#E0E0E0",        # Grey
}

# Default dimensions for treemaps
needtreemap_default_height = "600px"
needtreemap_default_width = "100%"

# Use CDN for Plotly.js (defaults to latest stable version)
# needtreemap_plotly_cdn = "https://cdn.plot.ly/plotly-2.35.2.min.js"

# -- Options for HTML output -------------------------------------------------
html_theme = "alabaster"
html_static_path = ["_static"]

# Theme options
html_theme_options = {
    "description": "Task Management System Documentation",
    "github_button": False,
    "fixed_sidebar": True,
}
