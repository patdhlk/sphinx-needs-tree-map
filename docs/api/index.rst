API Reference
=============

This section documents the internal API of sphinx-needs-tree-map for developers
who want to extend or integrate with the extension.

Extension Setup
---------------

.. automodule:: sphinx_needs_tree_map
   :members:
   :undoc-members:
   :show-inheritance:

Directives
----------

.. automodule:: sphinx_needs_tree_map.directives.needtreemap
   :members:
   :undoc-members:
   :show-inheritance:

Utilities
---------

Hierarchy Builder
~~~~~~~~~~~~~~~~~

.. py:module:: sphinx_needs_tree_map.utils.hierarchy

Classes for building hierarchical tree structures from sphinx-needs data.

.. autoclass:: sphinx_needs_tree_map.utils.hierarchy.TreeNode
   :members: add_child, iter_all, compute_values
   :show-inheritance:
   :no-index:

.. autoclass:: sphinx_needs_tree_map.utils.hierarchy.HierarchyBuilder
   :members:
   :undoc-members:
   :show-inheritance:

Filters
~~~~~~~

.. automodule:: sphinx_needs_tree_map.utils.filters
   :members:
   :undoc-members:
   :show-inheritance:

Plotly Renderer
~~~~~~~~~~~~~~~

.. automodule:: sphinx_needs_tree_map.utils.plotly_renderer
   :members:
   :undoc-members:
   :show-inheritance:
