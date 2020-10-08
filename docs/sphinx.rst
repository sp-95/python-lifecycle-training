=====================
Documentation: Sphinx
=====================

**Sphinx** is a tool that makes it easy to create intelligent and beautiful
documentation, written by Georg Brandl and licensed under the BSD license.

It was originally created for the Python documentation, and it has excellent facilities
for the documentation of software projects in a range of languages. The following
features should be highlighted:

* Output formats: HTML (including Windows HTML Help), LaTeX (for printable PDF
  versions), ePub, Texinfo, manual pages, plain text
* Extensive cross-references: semantic markup and automatic links for functions,
  classes, citations, glossary terms and similar pieces of information
* Hierarchical structure: easy definition of a document tree, with automatic links to
  siblings, parents and children
* Automatic indices: general index as well as a language-specific module indices
* Code handling: automatic highlighting using the Pygments highlighter
* Extensions: automatic testing of code snippets, inclusion of docstrings from Python
  modules (API docs), and more
* Contributed extensions: more than 50 extensions contributed by users in a second
  repository; most of them installable from PyPI

Sphinx uses reStructuredText as its markup language, and many of its strengths come from
the power and straightforwardness of reStructuredText and its parsing and translating
suite, the Docutils.

For more information visit https://www.sphinx-doc.org/en/master/

Installation
------------

.. code-block:: console

    $ poetry add sphinx --dev

Setup
-----

Sphinx comes with a script called ``sphinx-quickstart`` that sets up a source directory
and creates a default ``conf.py`` with the most useful configuration values from a few
questions it asks you.

.. code-block:: console

    $ sphinx-quickstart -v `poetry version -s` docs

.. image:: docs/_static/sphinx/img/sphinx-quickstart.png
   :alt: Sphinx quickstart

After you answer all the prompts the following files will be created::

    docs
    ├── _build/
    ├── _static/
    ├── _templates/
    ├── conf.py
    ├── index.rst
    ├── make.bat
    └── Makefile

Usage
-----

.. code-block:: console

    $ make -C docs html
    $ chromium docs/_build/html/index.html

.. image:: docs/_static/sphinx/img/quickstart-html.png
   :alt: HTML output of sphinx quickstart

Theme
-----

Doesn’t look much right now but it’ll get better. Let’s change the theme to the most
popular theme, Read the Docs.

.. code-block:: console

    $ poetry add sphinx-rtd-theme --dev
    $ poetry remove sphinx --dev

Change the following line in ``conf.py``

.. code-block:: python

    # -- Options for HTML output -------------------------------------------------

    # The theme to use for HTML and HTML Help pages.  See the documentation for
    # a list of builtin themes.

    html_theme = "sphinx_rtd_theme"

Clean the existing build and then build again.

.. code-block:: console

    $ make -C docs clean
    $ make -C docs html
    $ chromium docs/_build/html/index.html

.. image:: docs/_static/sphinx/img/sphinx-rtd-theme.png
   :alt: Sphinx Read the Docs Theme

Does it look better now?

Auto Documentation
------------------

We can convert our code docs into readable sphinx documentation.

First, uncomment the following lines in ``conf.py``:

.. code-block:: python

    # -- Path setup --------------------------------------------------------------

    # If extensions (or modules to document with autodoc) are in another directory,
    # add these directories to sys.path here. If the directory is relative to the
    # documentation root, use os.path.abspath to make it absolute, like shown here.

    import os
    import sys
    sys.path.insert(0, os.path.abspath('.'))

Now add the autodoc extension in the ``conf.py`` file itself.

.. code-block:: python

    # -- General configuration ---------------------------------------------------

    # Add any Sphinx extension module names here, as strings. They can be
    # extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
    # ones.
    extensions = [
        "sphinx.ext.autodoc",
    ]

Generate the docs for your modules

.. code-block:: console

    $ sphinx-apidoc -o docs/ python_lifecycle_training

Add modules as a content in index.rst file

.. code-block:: RST

    .. toctree::
       :maxdepth: 2
       :caption: Contents:

       modules

Add your module docs in a ``.gitignore`` file within the docs.

.. code-block::

    # Ignore module docs
    python_lifecycle_training*.rst

Clean and build again

.. code-block:: console

    $ make -C docs clean
    $ make -C docs html
    $ chromium docs/_build/html/index.html

.. image:: docs/_static/sphinx/img/autodoc.png
   :alt: Sphinx auto documentation

Google Docstrings
-----------------

Let’s try adding a docstring in our simple calculator to see what happens

.. code-block:: python

    def add(a: Real, b: Real) -> Real:
        """Add two numbers

        Args:
           a (Real): The first number
           b (Real): The second number

        Returns:
           Real: Sum of two numbers
        """
        logger.info(f"Adding {a} to {b}")
        return a + b

.. code-block:: console

    $ make -C docs clean
    $ make -C docs html
    $ chromium docs/_build/html/index.html

.. image:: docs/_static/sphinx/img/google-docs.png
   :alt: Google docstrings

Something doesn’t seem right here. In order for google style docstrings to be displayed
properly we need the napoleon sphinx extension. Go ahead and add it to ``conf.py``

.. code-block:: python

    # -- General configuration ---------------------------------------------------

    # Add any Sphinx extension module names here, as strings. They can be
    # extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
    # ones.
    extensions = [
        "sphinx.ext.autodoc",
        "sphinx.ext.napoleon",
    ]

.. code-block:: console

    $ make -C docs clean
    $ make -C docs html
    $ chromium docs/_build/html/index.html

.. image:: docs/_static/sphinx/img/google-docs-fix.png
   :alt: Fix google docstrings

This seems better, doesn’t it?

Document Build Test
-------------------

Add the following lines in your tox file

.. code-block:: ini

    [tox]
    envlist = ..., docs
    ...

    [testenv:docs]
    basepython = python
    changedir = docs
    deps =
       sphinx-rtd-theme
       toml
    commands =
       sphinx-build -b html -d {envtmpdir}/doctrees . {envtmpdir}

Run tox

.. code-block:: console

    $ tox

Miscellaneous
-------------

Useful sphinx extensions
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    # -- General configuration ---------------------------------------------------

    # Add any Sphinx extension module names here, as strings. They can be
    # extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
    # ones.
    extensions = [
       "sphinx.ext.autodoc",
       "sphinx.ext.coverage",
       "sphinx.ext.doctest",
       "sphinx.ext.githubpages",
       "sphinx.ext.napoleon",
       "sphinx.ext.todo",
       "sphinx.ext.viewcode",
    ]

Don’t show todos
~~~~~~~~~~~~~~~~

.. code-block:: python

    # -- Options for todo extension ----------------------------------------------

    # If true, `todo` and `todoList` produce output, else they produce nothing.
    todo_include_todos = False

Better syntax highlighting
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    # The name of the Pygments (syntax highlighting) style to use.
    pygments_style = "sphinx"

Auto-generate your project meta
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: console

    $ poetry add toml --dev

.. code-block:: python

    import toml

    sys.path.insert(0, os.path.abspath('.'))


    # -- Project information -----------------------------------------------------

    def _get_project_meta():
        return toml.load("../pyproject.toml")["tool"]["poetry"]


    pkg_meta = _get_project_meta()
    project = str(pkg_meta["name"])
    copyright = "2020, Shashanka Prajapati"
    authors = str(pkg_meta["authors"])

    # The short X.Y version
    version = str(pkg_meta["version"])

    # The full version, including alpha/beta/rc tags
    release = version

Next Step
---------

To move on to the next step commit or stash your changes then checkout to the branch
``deploy/ci/test``

.. code-block:: console

    $ git stash
    $ git checkout deploy/ci/test

Uninstall
---------

.. code-block:: console

    $ poetry remove sphinx-rtd-theme --dev
