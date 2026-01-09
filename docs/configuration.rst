Configuration
=============

Global configuration options for sphinx-needs-tree-map are set in your ``conf.py``.

Plotly.js CDN
-------------

``needtreemap_plotly_cdn``
   URL to load Plotly.js from. Default uses the official CDN.

   .. code-block:: python

      needtreemap_plotly_cdn = "https://cdn.plot.ly/plotly-2.35.2.min.js"

Default Dimensions
------------------

``needtreemap_default_height``
   Default height for treemaps.

   .. code-block:: python

      needtreemap_default_height = "600px"

``needtreemap_default_width``
   Default width for treemaps.

   .. code-block:: python

      needtreemap_default_width = "100%"

Type Colors
-----------

``needtreemap_colors``
   Dictionary mapping need types to CSS colors.

   .. code-block:: python

      needtreemap_colors = {
          "req": "#E3F2FD",       # Light blue
          "spec": "#FFF3E0",      # Light orange
          "impl": "#E8F5E9",      # Light green
          "test": "#FCE4EC",      # Light pink
          "story": "#F3E5F5",     # Light purple
          "default": "#ECEFF1",   # Light grey (fallback)
      }

Status Colors
-------------

``needtreemap_status_colors``
   Dictionary mapping status values to CSS colors.

   .. code-block:: python

      needtreemap_status_colors = {
          "open": "#FFCDD2",           # Light red
          "in progress": "#FFF9C4",    # Light yellow
          "implemented": "#C8E6C9",    # Light green
          "verified": "#B2DFDB",       # Light teal
          "default": "#ECEFF1",        # Light grey (fallback)
      }

Full Example
------------

.. code-block:: python

   # conf.py

   extensions = [
       "sphinx_needs",
       "sphinx_needs_tree_map",
   ]

   # sphinx-needs-tree-map configuration
   needtreemap_default_height = "700px"
   needtreemap_default_width = "100%"

   needtreemap_colors = {
       "req": "#BBDEFB",
       "spec": "#FFECB3",
       "impl": "#C8E6C9",
       "test": "#F8BBD9",
       "default": "#E0E0E0",
   }

   needtreemap_status_colors = {
       "draft": "#E1BEE7",
       "open": "#FFCDD2",
       "in_progress": "#FFF9C4",
       "done": "#C8E6C9",
       "default": "#E0E0E0",
   }
