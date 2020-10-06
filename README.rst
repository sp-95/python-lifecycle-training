==================================
Configuration Management: dynaconf
==================================

Features
--------

* Inspired by the 12-factor application guide
* **Settings management** (default values, validation, parsing, templating)
* Protection of **sensitive information** (passwords/tokens)
* Multiple **file formats** ``toml|yaml|json|ini|py`` and also customizable loaders.
* Full support for **environment variables** to override existing settings (dotenv
  support included).
* Optional layered system for **multi environments** ``[default, development, testing,
  production]`` (also called multi profiles)
* Built-in support for **Hashicorp Vault** and **Redis** as settings and secrets
  storage.
* Built-in extensions for **Django** and **Flask** web frameworks.
* **CLI** for common operations such as ``init, list, write, validate, export``.

For more information visit https://www.dynaconf.com/

Installation
------------

.. code-block:: console

    $ poetry add dynaconf

Initialization
--------------

.. code-block:: console

    $ mkdir configs
    $ dynaconf init -p configs -f yaml

.. image:: docs/_static/dynaconf/img/init.png
    :alt: Dynaconf initialization

This command creates the following files::

    .
    ├── configs/
    │   ├── .gitignore
    │   ├── .secrets.toml # Sensitive data like passwords and tokens (optional)
    │   └── settings.toml # Application setttings (optional)
    └── config.py         # Where you import your settings object (required)

Fix the paths for your settings files in ``config.py``

.. code-block:: python

    settings_files=["configs/settings.yaml", "configs/.secrets.yaml"]

Basic Usage
-----------

Let us create a broken calculator to see how dynaconf works.

.. code-block:: python

    # python_lifecycle_training/calculator/broken.py
    import fire
    from loguru import logger

    from config import settings
    from python_lifecycle_training.calculator.complex import Calculator


    class BrokenCalculator(Calculator):
        def __init__(self):
            offset = settings.offset
            logger.info(f"Offset: {offset}")
            self.offset = offset

        def add(self, a, b):
            return super(BrokenCalculator, self).add(a, b) - self.offset

        def sub(self, a, b):
            return super(BrokenCalculator, self).sub(a, b) - self.offset

        def mul(self, a, b):
            return super(BrokenCalculator, self).mul(a, b) - self.offset

        def div(self, a, b):
            return super(BrokenCalculator, self).div(a, b) - self.offset


    def main():
        fire.Fire(BrokenCalculator)

Add an offset in ``settings.yaml`` file:

.. code-block:: YAML

    offset: 2

Add an entry point in ``pyproject.toml``

.. code-block:: cfg

    calc-broken = "python_lifecycle_training.calculator.broken:main"

Install your package

.. code-block:: console

    $ poetry install

Run the command

.. code-block:: console

    $ calc-broken add 2 2

.. image:: docs/_static/dynaconf/img/broken.png
    :alt: Broken Calculator
