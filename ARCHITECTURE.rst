=========================================
{{ project_name }} — Architecture
=========================================

:Author: {{ author_name }}
:Status: Active
:Date: {{ current_year }}
:Version: 0.1.0

.. contents:: Table of Contents
   :depth: 3
   :backlinks: none

----

Core Philosophy
===============

.. TODO: Document your project's core philosophy and design principles.

**Principle 1**
    Description of the first core principle.

**Principle 2**
    Description of the second core principle.

----

Package Architecture
====================

.. TODO: Document your package's architecture here. Replace this entire section
   with your actual architecture documentation.

Phase A — Pre-Processing
-------------------------

Role
~~~~

Perform initial validation and setup.

Checks
~~~~~~

.. TODO: List your Phase A checks.

Partially trusted in Phase A
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. TODO: Document what is partially trusted.

Phase B — Processing
--------------------

Role
~~~~

Perform core operations.

Path normalisation pipeline
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. TODO: Document your processing pipeline.

Phase C — Post-Processing
-------------------------

Role
~~~~

Finalize operations and cleanup.

----

Public API
==========

.. TODO: Document your public API here.

.. code-block:: python

    def main_function(input_data):
        """Main entry point for {{ project_name }}."""
        ...

.. code-block:: python

    class MainClass:
        def __init__(self, config=None):
            ...

        def run(self, data):
            """Run the main operation."""
            ...

----

Configuration
=============

.. TODO: Document configuration options.

Environment Variables
=====================

+---------------------------+------------------------------------+
| Environment variable     | Corresponding parameter            |
+===========================+====================================+
| ``PARAM_NAME``            | ``param_name``                    |
+---------------------------+------------------------------------+

----

Exception Hierarchy
===================

.. TODO: Document your exception hierarchy.

.. code-block:: text

    {{ project_name | capitalize }}Error (base)
    ├── SpecificError1
    ├── SpecificError2
    └── ...

----

Testing Strategy
================

Principle: No Mocks for Core Logic
----------------------------------

.. TODO: Document your testing philosophy.

Test cases
----------

.. TODO: Add examples of your test cases.

Directory layout
----------------

.. code-block:: text

    {{ package_name }}/
    ├── pyproject.toml
    ├── ARCHITECTURE.rst
    ├── src/
    │   └── {{ package_name }}/
    │       ├── __init__.py
    │       ├── _core.py
    │       ├── _module1.py
    │       └── py.typed
    └── tests/
        ├── conftest.py
        ├── test_module1.py
        └── ...

----

Background
==========

.. TODO: Add background/context for your project.
