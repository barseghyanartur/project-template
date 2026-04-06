Contributor guidelines
======================

.. _project: https://github.com/{{ github_username }}/{{ github_repo }}/
.. _uv: https://docs.astral.sh/uv/
.. _tox: https://tox.wiki
.. _ruff: https://beta.ruff.rs/docs/
.. _doc8: https://doc8.readthedocs.io/
.. _pre-commit: https://pre-commit.com/#installation
.. _issues: https://github.com/{{ github_username }}/{{ github_repo }}/issues
.. _discussions: https://github.com/{{ github_username }}/{{ github_repo }}/discussions
.. _pull request: https://github.com/{{ github_username }}/{{ github_repo }}/pulls
.. _versions manifest: https://github.com/actions/python-versions/blob/main/versions-manifest.json

Developer prerequisites
------------------------

pre-commit
~~~~~~~~~~

Refer to `pre-commit`_ for installation instructions.

TL;DR:

.. code-block:: sh

    curl -LsSf https://astral.sh/uv/install.sh | sh  # Install uv
    uv tool install pre-commit                        # Install pre-commit
    pre-commit install                                # Install hooks

Installing `pre-commit`_ ensures all contributions adhere to the project's
code quality standards.

Code standards
--------------

`ruff`_ and `doc8`_ are triggered automatically by `pre-commit`_.

To run checks manually:

.. code-block:: sh

    make doc8
    make ruff

Virtual environment
-------------------

.. code-block:: sh

    make create-venv

Installation
------------

.. code-block:: sh

    make install

Testing
-------

**All tests must be run inside Docker** unless you have verified they will
not affect your system.

.. code-block:: sh

    make test

To test a single environment:

.. code-block:: sh

    make test-env ENV=py312

For an interactive shell inside the container:

.. code-block:: sh

    make shell

Releases
--------

**Build the package for releasing:**

.. code-block:: sh

    make package-build

----

**Test the built package:**

.. code-block:: sh

    make check-package-build

----

**Make a test release (test.pypi.org):**

.. code-block:: sh

    make test-release

----

**Release (pypi.org):**

.. code-block:: sh

    make release

Adding tests
------------

.. TODO: Document your testing requirements.

- All tests should be added to the appropriate ``test_*.py`` file.
- Integration tests should verify complete behavior.

Pull requests
-------------

Open a `pull request`_ to the ``dev`` branch only. Never directly to ``main``.

.. note::

    Create pull requests to the ``dev`` branch only!

Examples of welcome contributions:

.. TODO: List types of welcome contributions.

- Fixing documentation typos or improving explanations.
- Adding test cases for new edge cases.
- Improving error messages.

General checklist
~~~~~~~~~~~~~~~~~

- Does your change require documentation updates?
- Does your change require new tests?
- Does your change add any external dependencies?

When fixing bugs
~~~~~~~~~~~~~~~~

- Add a regression test that reproduces the bug before your fix.

When adding a new feature
~~~~~~~~~~~~~~~~~~~~~~~~~

- Update ``README.rst`` with documentation.
- Add appropriate tests.

GitHub Actions
--------------

Tests run on Python 3.10–3.14 (all non-EOL versions).

Questions
---------

Ask on GitHub `discussions`_.

Issues
------

Report bugs or request features on GitHub `issues`_.
