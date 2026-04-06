.. TODO: Replace {{ project_name }} with your project name throughout this file.

.. image:: https://raw.githubusercontent.com/{{ github_username }}/{{ github_repo }}/main/docs/_static/logo.png
   :alt: {{ project_name }} Logo
   :align: center

{{ project_description }}

.. TODO: Add badges for your project (PyPI version, build status, coverage, etc.)
.. TODO: Add badges for your project. See any popular open-source project for badge examples.

Prerequisites
=============

Python 3.10 or later.

Installation
============

With ``uv``:

.. code-block:: sh

    uv pip install {{ project_name }}

Or with ``pip``:

.. code-block:: sh

    pip install {{ project_name }}

Quick start
===========

.. TODO: Replace this example with your project's core use case.

.. code-block:: python

    from {{ package_name }} import main_function

    main_function("example input")

.. TODO: Add more usage examples and a features list.

Default configuration
=====================

.. TODO: Document your project's default limits or configuration values.

+-------------------+------------+
| Parameter         | Default    |
+===================+============+
| ``param_name``    | value      |
+-------------------+------------+

Environment variable overrides
==============================

.. TODO: Document environment variable configuration if applicable.

.. code-block:: sh

    export PARAM_NAME=value

Testing
=======

All tests run inside Docker to prevent accidental system impact:

.. code-block:: sh

    make test

To test a specific Python version:

.. code-block:: sh

    make test-env ENV=py312

License
=======

MIT

Support
=======

.. TODO: Replace with your support contact information.

For issues, go to `GitHub <https://github.com/{{ github_username }}/{{ github_repo }}/issues>`_.

Author
======

{{ author_name }} <{{ author_email }}>
