Examples
========

This page shows various configurations and use cases for the ``needtreemap`` directive.

For a complete working example project, see the ``example/`` directory in the repository.

Document Overview
-----------------

Visualize the structure of your documentation:

.. code-block:: rst

   .. needtreemap::
      :hierarchy: document
      :depth: 3
      :show_values:
      :title: Documentation Structure

This shows all needs organized by their document location, with section hierarchy
preserved up to 3 levels deep.

Requirements Traceability
-------------------------

Show parent-child relationships through links:

.. code-block:: rst

   .. needtreemap::
      :hierarchy: links
      :filter: type in ['req', 'spec', 'test']
      :color_by: type
      :show_values:
      :title: Requirements Traceability Matrix

This is useful for visualizing how requirements flow down to specifications and tests.

Status Dashboard
----------------

Quick overview of requirement statuses:

.. code-block:: rst

   .. needtreemap::
      :hierarchy: type
      :depth: 2
      :color_by: status
      :show_values:
      :title: Status Overview

Groups needs by type first, then shows the count of each status within each type.

Filtered Views
--------------

Security Requirements Only
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. needtreemap::
      :filter: 'security' in tags
      :color_by: status
      :title: Security Requirements

Open Items
~~~~~~~~~~

.. code-block:: rst

   .. needtreemap::
      :status: open,in progress
      :color_by: type
      :show_values:
      :title: Open Work Items

Specific Need Types
~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. needtreemap::
      :types: req
      :hierarchy: document
      :title: Requirements Only

Compact Visualizations
----------------------

Small treemap for sidebar or summary:

.. code-block:: rst

   .. needtreemap::
      :hierarchy: type
      :depth: 1
      :height: 300px
      :title: Needs by Type

Large detailed view:

.. code-block:: rst

   .. needtreemap::
      :hierarchy: document
      :depth: 5
      :height: 800px
      :show_values:
      :title: Complete Documentation Map

Size by Content Length
----------------------

Size nodes by the amount of content in each need:

.. code-block:: rst

   .. needtreemap::
      :size_by: content_length
      :color_by: type
      :title: Needs by Content Size

Size by Link Count
------------------

Highlight highly connected needs:

.. code-block:: rst

   .. needtreemap::
      :size_by: links
      :color_by: type
      :title: Needs by Connectivity

Example Project
---------------

The repository includes a complete example project in the ``example/`` directory
demonstrating:

- 45+ needs (requirements, specifications, test cases, user stories)
- Multiple documents organized hierarchically
- Traceability links between needs
- Examples of all three hierarchy modes
- Various filtering and visualization options

To build the example:

.. code-block:: bash

   cd example
   uv sync
   make html
   # Open _build/html/index.html
