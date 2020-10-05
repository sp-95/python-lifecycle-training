======
Flake8
======

Flake8 is a Python library that wraps **PyFlakes**, **pycodestyle** and **Ned
Batchelder’s McCabe script**. It is a great toolkit for checking your codebase against
coding style (PEP8), programming errors (like “library imported but unused” and
“Undefined name”) and to check cyclomatic complexity.

If you are not familiar with the term **cyclomatic complexity**, it is a software metric
created by Thomas J. McCabe to measure the number of independent paths through the
source code. Generally speaking, the higher number of **ifs** inside a function, the
higher number of paths it will have, thus a higher **cyclomatic complexity**. Of course,
there are other control flow operations that impact the calculus of the cyclomatic
complexity. It is also referred to as McCabe complexity.

Installation
~~~~~~~~~~~~

.. code-block:: console

    $ poetry add flake8 --dev

Configuration
~~~~~~~~~~~~~

Create a ``setup.cfg`` file and add the following:

.. code-block:: cfg

    [flake8]
    max-line-length = 88
    max-complexity = 10
    show-source = true
    per-file-ignores =
        # imported but unused
        __init__.py: F401

Usage
~~~~~

.. code-block:: console

    $ flake8 python_lifecycle tests

Output
######

.. code-block:: console

    python_lifecycle:0:1: E902 FileNotFoundError: [Errno 2] No such file or directory: 'python_lifecycle'
    tests/calculator/test_simple.py:2:1: F401 'python_lifecycle' imported but unused
    import python_lifecycle
    ^
    tests/calculator/test_simple.py:3:1: F401 'pytest.fixture' imported but unused
    from pytest import fixture
    ^
    tests/calculator/test_simple.py:4:1: F401 'pytest' imported but unused
    import pytest
    ^
    tests/calculator/test_simple.py:5:1: F401 'os' imported but unused
    import os
    ^
    tests/calculator/test_simple.py:6:1: F401 'pathlib.Path' imported but unused
    from pathlib import Path
    ^
