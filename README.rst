=====
isort
=====

**isort** simply stands for import sort. It is a Python utility/library to sort
imports alphabetically and automatically separated into sections and by type. It
provides a command-line utility, Python library, and `plugins for various editors`_ to
quickly sort all your imports.

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
    import python_lifecycle
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
    import python_lifecycle
    from pytest import fixture

    from python_lifecycle_training import __version__

.. _plugins for various editors: https://github.com/pycqa/isort/wiki/isort-Plugins
