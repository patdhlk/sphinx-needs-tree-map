======================
Treemap Visualizations
======================

This page demonstrates the different visualization modes available in the
**sphinx-needs-tree-map** extension. Each treemap provides a different
perspective on the requirements data.

Document Hierarchy Mode
=======================

The **document** hierarchy mode organizes needs by their location in the
documentation structure: documents, sections, and subsections.

All Needs by Document
---------------------

.. needtreemap::
   :hierarchy: document
   :depth: 4
   :color_by: type
   :show_values:
   :title: All Needs Organized by Document Structure
   :height: 600px
   :width: 100%

This view is useful for:

* Understanding how needs are distributed across documentation
* Identifying documents with many or few needs
* Navigating to specific sections of documentation

Requirements Only
-----------------

.. needtreemap::
   :types: req
   :hierarchy: document
   :depth: 3
   :color_by: status
   :show_values:
   :title: Requirements by Document (Colored by Status)
   :height: 450px

Link Hierarchy Mode
===================

The **links** hierarchy mode builds a tree based on traceability relationships.
Parent needs appear at the top, with linked child needs below.

Full Traceability Tree
----------------------

.. needtreemap::
   :hierarchy: links
   :depth: 5
   :color_by: type
   :show_values:
   :title: Requirements Traceability Tree
   :height: 600px

This view shows:

* How requirements flow down to specifications
* How specifications are verified by test cases
* Orphaned needs (those without parent links)

Requirements to Specifications
------------------------------

.. needtreemap::
   :types: req, spec
   :hierarchy: links
   :depth: 3
   :color_by: status
   :show_values:
   :title: Requirements and Their Specifications
   :height: 450px

Type Hierarchy Mode
===================

The **type** hierarchy mode groups needs first by their type (requirement,
specification, test, etc.) and then by status.

All Needs by Type and Status
----------------------------

.. needtreemap::
   :hierarchy: type
   :depth: 3
   :color_by: status
   :show_values:
   :title: All Needs Grouped by Type and Status
   :height: 600px

This view helps with:

* Understanding the overall composition of needs
* Identifying status distribution within each type
* Tracking project progress by need type

Test Cases by Status
--------------------

.. needtreemap::
   :types: test
   :hierarchy: type
   :depth: 3
   :color_by: status
   :show_values:
   :title: Test Case Status Distribution
   :height: 400px

Filtered Views
==============

Treemaps can be filtered using various options to focus on specific subsets
of needs.

By Status
---------

Show only needs that are not yet verified:

.. needtreemap::
   :status: open, in_progress, implemented
   :hierarchy: type
   :depth: 3
   :color_by: status
   :show_values:
   :title: Needs Pending Verification
   :height: 400px

By Tags
-------

Show only security-related needs:

.. needtreemap::
   :tags: security
   :hierarchy: document
   :depth: 3
   :color_by: type
   :show_values:
   :title: Security-Related Needs
   :height: 400px

Using Filter Expressions
------------------------

Complex filtering using sphinx-needs filter syntax:

.. needtreemap::
   :filter: type == 'req' and status in ['open', 'in_progress']
   :hierarchy: document
   :depth: 3
   :color_by: status
   :show_values:
   :title: Requirements Still In Progress
   :height: 400px

Sizing Options
==============

Treemaps can use different metrics to determine the relative size of nodes.

Size by Count (Default)
-----------------------

Each need contributes equally to its parent's size:

.. needtreemap::
   :types: req, spec
   :hierarchy: type
   :depth: 3
   :size_by: count
   :color_by: type
   :show_values:
   :title: Size by Need Count
   :height: 400px

Size by Links
-------------

Needs with more links appear larger:

.. needtreemap::
   :hierarchy: type
   :depth: 3
   :size_by: links
   :color_by: type
   :show_values:
   :title: Size by Link Count
   :height: 400px

Summary
=======

The **sphinx-needs-tree-map** extension provides three primary hierarchy modes:

1. **document**: View needs organized by their documentation location
2. **links**: View needs organized by traceability relationships
3. **type**: View needs grouped by type and status

Combined with filtering options and sizing modes, these visualizations provide
powerful insights into requirements data and project status.
