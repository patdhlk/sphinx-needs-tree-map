Installation
============

Requirements
------------

- Python 3.9 or later
- Sphinx 5.0 or later (up to 8.x)
- sphinx-needs 4.1.0 or later

Installing with pip
-------------------

.. code-block:: bash

   pip install sphinx-needs-tree-map

Installing with uv
------------------

.. code-block:: bash

   uv add sphinx-needs-tree-map

Development Installation
------------------------

For development, clone the repository and install in editable mode:

.. code-block:: bash

   git clone https://github.com/patdhlk/sphinx-needs-tree-map.git
   cd sphinx-needs-tree-map
   pip install -e ".[dev,docs]"

Or with uv:

.. code-block:: bash

   git clone https://github.com/patdhlk/sphinx-needs-tree-map.git
   cd sphinx-needs-tree-map
   uv sync --group dev --group docs

Enabling the Extension
----------------------

Add the extension to your Sphinx ``conf.py``:

.. code-block:: python

   extensions = [
       "sphinx_needs",
       "sphinx_needs_tree_map",
   ]

.. note::

   ``sphinx_needs`` must be listed before ``sphinx_needs_tree_map`` in the
   extensions list, or it will be automatically loaded as a dependency.

Verifying Installation
----------------------

After installation, you can verify it works by adding a simple treemap to any
document:

.. code-block:: rst

   .. needtreemap::

Build your documentation and you should see an interactive treemap visualization.
