Quick Start
===========

This guide will get you up and running with sphinx-needs-tree-map in 5 minutes.

Basic Treemap
-------------

Once installed, add a treemap to any document with the ``needtreemap`` directive:

.. code-block:: rst

   .. needtreemap::

This creates a treemap of all needs in your documentation, organized by document.

Customizing the View
--------------------

Filter by Type
~~~~~~~~~~~~~~

Show only specific need types:

.. code-block:: rst

   .. needtreemap::
      :types: req,spec

Or use a filter expression:

.. code-block:: rst

   .. needtreemap::
      :filter: type == 'req' or type == 'spec'

Change Hierarchy Mode
~~~~~~~~~~~~~~~~~~~~~

The extension supports three hierarchy modes:

**Document mode** (default) - Groups needs by document and sections:

.. code-block:: rst

   .. needtreemap::
      :hierarchy: document

**Links mode** - Uses parent-child link relationships:

.. code-block:: rst

   .. needtreemap::
      :hierarchy: links

**Type mode** - Groups by need type and status:

.. code-block:: rst

   .. needtreemap::
      :hierarchy: type

Color by Status
~~~~~~~~~~~~~~~

Color nodes by their status instead of type:

.. code-block:: rst

   .. needtreemap::
      :color_by: status

Show Values
~~~~~~~~~~~

Display counts in node labels:

.. code-block:: rst

   .. needtreemap::
      :show_values:

Complete Example
----------------

Here's a full-featured treemap configuration:

.. code-block:: rst

   .. needtreemap::
      :filter: type in ['req', 'spec', 'test']
      :hierarchy: document
      :depth: 3
      :color_by: type
      :show_values:
      :height: 600px
      :title: Requirements Overview

Next Steps
----------

- See :doc:`directives/needtreemap` for all available options
- Check out :doc:`configuration` for global settings
- Browse :doc:`examples` for more use cases
