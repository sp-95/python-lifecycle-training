=====
isort
=====

**isort** simply stands for import sort. It is a Python utility/library to sort imports
alphabetically and automatically separated into sections and by type. It provides a
command-line utility, Python library, and `plugins for various editors`_ to quickly sort
all your imports.

For further information visit https://pycqa.github.io/isort/

Installation
------------

.. code-block:: console

    $ poetry add isort --dev

Configuration
-------------

Add the isort configurations in ``pyproject.toml``

.. code-block:: cfg

    [tool.isort]
    multi_line_output = 3
    include_trailing_comma = true
    force_grid_wrap = 0
    use_parentheses = true
    ensure_newline_before_comments = true
    line_length = 88

Usage
-----

Before
~~~~~~

.. code-block:: python

    from python_lifecycle_training import __version__
    import python_lifecycle_training
    from pytest import fixture
    import pytest
    import os
    from pathlib import Path

After
~~~~~

.. code-block:: python

    import os
    from pathlib import Path

    import pytest
    from pytest import fixture

    import python_lifecycle_training
    from python_lifecycle_training import __version__

Add a badge
-----------

.. image:: https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336
    :target: https://pycqa.github.io/isort/
    :alt: imports: isort

.. code-block:: RST

    .. image:: https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336
        :target: https://pycqa.github.io/isort/
        :alt: imports: isort

Next Step
---------

To move on to the next step commit or stash your changes then checkout to the branch
``init/type-hint/mypy``

.. code-block:: console

    $ git stash
    $ git checkout init/type-hint/mypy

Uninstall
---------

.. code-block:: console

    $ poetry remove isort --dev

.. _plugins for various editors: https://github.com/pycqa/isort/wiki/isort-Plugins
