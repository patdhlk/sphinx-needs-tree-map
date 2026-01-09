.. Task Management System documentation master file

==============================================
Task Management System - Requirements & Design
==============================================

Welcome to the Task Management System documentation. This project demonstrates
the use of **sphinx-needs** for requirements engineering and **sphinx-needs-tree-map**
for interactive treemap visualizations.

Project Overview
================

The Task Management System (TMS) is a web-based application that allows teams to:

* Create, assign, and track tasks
* Manage project workflows
* Generate reports and analytics
* Integrate with external tools via API

Documentation Structure
=======================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   requirements/index
   specifications/index
   test_plan/index
   visualizations

Quick Stats
===========

This documentation contains:

* **Requirements**: High-level system requirements
* **Specifications**: Detailed technical specifications
* **Test Cases**: Verification test cases
* **User Stories**: User-focused feature descriptions

Requirements Overview Treemap
=============================

The treemap below shows all requirements organized by document and section:

.. needtreemap::
   :hierarchy: document
   :depth: 4
   :color_by: type
   :show_values:
   :title: All Needs by Document Structure
   :height: 500px

Traceability Overview
=====================

The treemap below shows requirements traceability through link relationships:

.. needtreemap::
   :hierarchy: links
   :depth: 4
   :color_by: status
   :show_values:
   :title: Requirements Traceability
   :height: 500px

Indices and tables
==================

* :ref:`genindex`
* :ref:`search`
