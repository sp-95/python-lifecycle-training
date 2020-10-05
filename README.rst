=====
Black
=====

**Black** gives you speed, determinism, and freedom from **pycodestyle** nagging about
formatting. You will save time and mental energy for more important matters.

**Black** makes code review faster by producing the smallest diffs possible. Blackened
code looks the same regardless of the project you’re reading. Formatting becomes
transparent after a while and you can focus on the content instead.

Installation
------------

.. code-block:: console

    $ poetry add black --dev

Check
-----

.. code-block:: console

    $ black python_lifecycle_training tests --diff --color

.. image:: docs/_static/black/img/check.png
   :alt: Colored output of black diff

Usage
-----

.. code-block:: console

    $ black python_lifecycle_training tests

.. image:: docs/_static/black/img/usage.png
   :alt: The output when your run black
