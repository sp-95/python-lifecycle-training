=================
Testing: coverage
=================

**Coverage.py** is a tool for measuring code coverage of Python programs. It monitors
your program, noting which parts of the code have been executed, then analyzes the
source to identify code that could have been executed but was not.

**Coverage** measurement is typically used to gauge the effectiveness of tests. It can
show which parts of your code are being exercised by tests, and which are not.

For more information visit https://coverage.readthedocs.io/en/coverage-5.3/

Installation
------------

.. code-block:: console

    $ poetry add coverage --dev

Configuration
-------------

Add coverage configurations in ``pyproject.toml``

.. code-block:: cfg

    [tool.coverage.run]
    branch = true
    source = [
        "python_lifecycle_training",
    ]

    [tool.coverage.report]
    # Regexes for lines to exclude from consideration
    exclude_lines = [
        # Have to re-enable the standard pragma
        "pragma: no cover",

        # Don't complain about missing debug-only code:
        "def __repr__",
        "if self.debug",

        # Don't complain if tests don't hit defensive assertion code:
        "raise AssertionError",
        "raise NotImplementedError",

        # Don't complain if non-runnable code isn't run:
        "if 0:",
        "if __name__ == .__main__.:",

        # Don't complain about fire commands
        "fire.Fire",
    ]
    fail_under = 90
    ignore_errors = true
    skip_empty = true

Usage
-----

Use ``coverage run`` to run your test suite and gather data. However you normally run
your test suite, you can run your test runner under coverage. If your test runner
command starts with “python”, just replace the initial “python” with “coverage run”.

.. code-block:: console

    $ coverage run -m pytest

.. image:: ../_static/coverage/img/run.png
   :alt: Coverage run pytest

Use ``coverage report`` to report on the results:

.. code-block:: console

    $ coverage report -m

.. image:: ../_static/coverage/img/report.png
   :alt: Coverage report

For a nicer presentation, use ``coverage html`` to get annotated HTML listings detailing
missed lines:

.. code-block:: console

    $ coverage html
    $ chromium htmlcov/index.html

.. image:: ../_static/coverage/img/html.png
   :alt: Coverage HTML report

Next Step
---------

To move on to the next step commit or stash your changes then checkout to the branch
``setup/test/pytest-cov``

.. code-block:: console

    $ git stash
    $ git checkout setup/test/pytest-cov

Uninstall
---------

.. code-block:: console

    $ poetry remove coverage --dev
