needtreemap Directive
=====================

The ``needtreemap`` directive creates interactive Plotly.js treemap visualizations
of your sphinx-needs objects.

Basic Usage
-----------

.. code-block:: rst

   .. needtreemap::

Options Reference
-----------------

Filtering Options
~~~~~~~~~~~~~~~~~

``:filter:``
   A sphinx-needs filter expression to select needs.

   Example: ``:filter: type == 'req' and status == 'open'``

``:types:``
   Comma-separated list of need types to include.

   Example: ``:types: req,spec,test``

``:status:``
   Comma-separated list of statuses to include.

   Example: ``:status: open,in progress``

``:tags:``
   Comma-separated list of tags to include (needs must have at least one).

   Example: ``:tags: security,performance``

Hierarchy Options
~~~~~~~~~~~~~~~~~

``:hierarchy:``
   How to organize the treemap hierarchy.

   - ``document`` (default): Group by document, then sections
   - ``links``: Build tree from parent-child link relationships
   - ``type``: Group by need type, then status

``:root:``
   Starting point for the hierarchy.

   - ``document`` (default): Start from document level
   - ``section``: Start from section level
   - ``<need_id>``: Start from a specific need

``:depth:``
   Maximum hierarchy depth. Default: ``3``

   Example: ``:depth: 4``

Visualization Options
~~~~~~~~~~~~~~~~~~~~~

``:size_by:``
   How to calculate node sizes.

   - ``count`` (default): Each need counts as 1
   - ``links``: Size by number of links (incoming + outgoing)
   - ``content_length``: Size by content length

``:color_by:``
   How to determine node colors.

   - ``type`` (default): Color by need type
   - ``status``: Color by status

``:show_values:``
   Flag to show counts in node labels. No value needed.

``:interactive:``
   Flag to enable/disable interactive features. Enabled by default.

Layout Options
~~~~~~~~~~~~~~

``:height:``
   CSS height of the treemap. Default: ``600px``

``:width:``
   CSS width of the treemap. Default: ``100%``

``:title:``
   Optional title displayed above the treemap.

Examples
--------

Filter by Multiple Criteria
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. needtreemap::
      :types: req,spec
      :status: open,in progress
      :hierarchy: document

Link-based Hierarchy with Custom Colors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. needtreemap::
      :hierarchy: links
      :color_by: status
      :show_values:
      :title: Requirements Traceability

Compact Type Overview
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. needtreemap::
      :hierarchy: type
      :depth: 2
      :height: 400px
