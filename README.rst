============================
Command Line Interface: fire
============================

**Python Fire** is a library for automatically generating command line interfaces (CLIs)
from absolutely any Python object.

* Python Fire is a simple way to create a CLI in Python.
* Python Fire is a helpful tool for developing and debugging Python code.
* Python Fire helps with exploring existing code or turning other people's code into a
  CLI.
* Python Fire makes transitioning between Bash and Python easier.
* Python Fire makes using a Python REPL easier by setting up the REPL with the modules
  and variables you'll need already imported and created.

For more information visit https://google.github.io/python-fire/

Installation
------------

.. code-block:: console

    $ poetry add fire

Basic Usage
-----------

You can call ``Fire`` on any Python object:
functions, classes, modules, objects, dictionaries, lists, tuples, etc. They all work!

Here's an example of calling Fire on a function.

.. code-block:: python

    from numbers import Real

    import fire


    def add(a: Real, b: Real) -> Real:
        return a + b


    if __name__ == '__main__':
        fire.Fire(add)

Then, from the command line, you can run:

.. code-block:: console

    $ python -m python_lifecycle_training.calculator.simple 2 2
    4

Now, let us try calling Fire on a class by creating a complex calculator.

.. code-block:: python

    # python_lifecycle_training/calculator/complex.py
    import fire


    class Calculator:
        @staticmethod
        def add(a, b):
            return a + b

        @staticmethod
        def sub(a, b):
            return a - b

        @staticmethod
        def mul(a, b):
            return a * b

        @staticmethod
        def div(a, b):
            return a / b


    if __name__ == "__main__":
        fire.Fire(Calculator)

Then, from the command line, you can run:

.. code-block:: console

    $ python -m python_lifecycle_training.calculator.complex add 2 2
    4

    $ python -m python_lifecycle_training.calculator.complex sub 2 2
    0

    $ python -m python_lifecycle_training.calculator.complex mul 2 2
    4

    $ python -m python_lifecycle_training.calculator.complex div 2 2
    1.0

Self-defined Commands
---------------------

It is pretty tedious run our commands like this so let us create some entry points.
First replace the file executable ``if __name__ == "__main__":`` with a main method that
calls your fire command.

Before
~~~~~~

.. code-block:: python

    if __name__ == "__main__":
        fire.Fire(Calculator)

After
~~~~~~

.. code-block:: python

    def main():
        fire.Fire(Calculator)

Now create entry points in ``pyproject.toml`` below *dev-dependencies*.

.. code-block:: cfg

    [tool.poetry.scripts]
    calc-simp = "python_lifecycle_training.calculator.simple:main"
    calc-complex = "python_lifecycle_training.calculator.complex:main"

Install your package via poetry

.. code-block:: console

    $ poetry install

Now you can run:

.. code-block:: console

    $ calc-simp 2 2
    4

    $ calc-complex add 2 2
    4

.. note:: Comment out ``disallow_untyped_defs = true`` for *mypy* in ``setup.cfg`` for
   convenience

Next Step
---------

To move on to the next step commit or stash your changes then checkout to the branch
``setup/log/loguru``

.. code-block:: console

    $ git stash
    $ git checkout setup/log/loguru

Uninstall
---------

.. code-block:: console

    $ poetry remove fire
