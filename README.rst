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
