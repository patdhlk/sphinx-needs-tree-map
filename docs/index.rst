sphinx-needs-tree-map
=====================

.. image:: https://img.shields.io/pypi/v/sphinx-needs-tree-map.svg
   :target: https://pypi.org/project/sphinx-needs-tree-map/
   :alt: PyPI version

.. image:: https://img.shields.io/pypi/pyversions/sphinx-needs-tree-map.svg
   :target: https://pypi.org/project/sphinx-needs-tree-map/
   :alt: Python versions

.. image:: https://github.com/patdhlk/sphinx-needs-tree-map/actions/workflows/ci.yaml/badge.svg
   :target: https://github.com/patdhlk/sphinx-needs-tree-map/actions/workflows/ci.yaml
   :alt: CI status

.. image:: https://img.shields.io/github/license/patdhlk/sphinx-needs-tree-map.svg
   :target: https://github.com/patdhlk/sphinx-needs-tree-map/blob/main/LICENSE
   :alt: License

**StrictDoc-style tree map visualizations for sphinx-needs.**

sphinx-needs-tree-map is a Sphinx extension that provides interactive treemap
visualizations for your sphinx-needs documentation. It allows you to visualize
requirements, specifications, and other need types in hierarchical treemaps
using Plotly.js.

.. grid:: 1 2 2 2
   :gutter: 3

   .. grid-item-card:: Installation
      :link: installation
      :link-type: doc

      Get started with sphinx-needs-tree-map

   .. grid-item-card:: Quick Start
      :link: quickstart
      :link-type: doc

      Learn the basics in 5 minutes

   .. grid-item-card:: Directive Reference
      :link: directives/needtreemap
      :link-type: doc

      Complete directive options

   .. grid-item-card:: Examples
      :link: examples
      :link-type: doc

      See treemaps in action

Features
--------

- **Interactive Treemaps**: Visualize your requirements hierarchy using Plotly.js
- **Multiple Hierarchy Modes**: Organize by document structure, link relationships, or need types
- **Flexible Filtering**: Filter by type, status, tags, or custom filter expressions
- **Customizable Colors**: Configure colors for need types and statuses
- **Click-to-Navigate**: Click on any need in the treemap to jump to its documentation
- **Dark Mode Support**: Automatically adapts to light and dark themes
- **Responsive Design**: Works on all screen sizes

.. toctree::
   :maxdepth: 2
   :caption: User Guide

   installation
   quickstart
   directives/needtreemap
   configuration
   examples

.. toctree::
   :maxdepth: 2
   :caption: Development

   api/index
   contributing
   changelog

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
