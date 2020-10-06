===============
Logging: loguru
===============

**Loguru** is a library which aims to bring enjoyable logging in Python.

Also, this library is intended to make Python logging less painful by adding a bunch of
useful functionalities that solve caveats of the standard loggers. Using logs in your
application should be an automatism, **Loguru** tries to make it both pleasant and
powerful.

For more information visit https://loguru.readthedocs.io/en/stable/

Installation
------------

.. code-block:: console

    $ poetry add loguru

Basic Usage
-----------

The main concept of *Loguru* is that **there is one and only one logger**.

For convenience, it is pre-configured and outputs to ``stderr`` to begin with (but
that’s entirely configurable).

.. code-block:: python

    from loguru import logger


    def add(a: Real, b: Real) -> Real:
        logger.info(f"Adding {a} to {b}")
        return a + b

The ``logger`` is just an interface which dispatches log messages to configured
handlers.

To see the log run:

.. code-block:: console

    $ calc-simp 1 2

.. image:: docs/_static/loguru/img/calc-simp.png
    :alt: Logged output

Configuration
-------------

If you want to send logged messages to a file, you just have to use a string path as the
sink. It is also easily configurable if you need rotating logger.

Add the following in your package __init__.py file:

.. code-block:: python

    from loguru import logger

    logger.add("logs/critical.log", level="CRITICAL", rotation="10MB")
    logger.add("logs/error.log", level="ERROR", rotation="10MB")
    logger.add("logs/warning.log", level="WARNING", rotation="10MB")
    logger.add("logs/info.log", level="INFO", rotation="10MB")
    logger.add("logs/debug.log", level="DEBUG", rotation="10MB")

If you run the command ``calc-simp 1 2`` once more you can see that your log files have
been created in the directory ``logs``.
