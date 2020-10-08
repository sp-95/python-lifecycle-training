======================================
Continuous Integration: GitHub Actions
======================================

Documentation Hosting: GitHub Pages
-----------------------------------

Setup GitHub Pages
~~~~~~~~~~~~~~~~~~

We will be hosting our documents on GitHub Pages. In order to start hosting to GitHub
Pages we must first `create a GitHub Pages site`_.

Generate Docs
~~~~~~~~~~~~~

We have to execute quite a number of commands in order to generate the docs. To make
this process easier let's create a Makefile.

.. code-block:: makefile

    .PHONY: help docs
    .DEFAULT_GOAL := help

    define PRINT_HELP_PYSCRIPT
    import re, sys

    for line in sys.stdin:
        match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
        if match:
            target, help = match.groups()
            print("%-20s %s" % (target, help))
    endef
    export PRINT_HELP_PYSCRIPT

    BROWSER := python -c "$$BROWSER_PYSCRIPT"

    help:
        @python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

    docs: ## generate Sphinx HTML documentation, including API docs
        rm -f docs/python_lifecycle_training.rst
        rm -f docs/modules.rst
        sphinx-apidoc -o docs/ python_lifecycle_training
        $(MAKE) -C docs clean
        $(MAKE) -C docs html
        $(BROWSER) docs/_build/html/index.html

Sample Configuration
~~~~~~~~~~~~~~~~~~~~

.. code-block:: YAML

    name: Documentation

    on:
      push:
        branches:
          - master

    jobs:
      document:
        runs-on: ubuntu-latest

        steps:
          - uses: actions/checkout@v2

          - name: Set up Python
            uses: actions/setup-python@v2
            with:
              python-version: "3.x"

          - name: Install dependencies
            run: |
              python -m pip install --upgrade pip
              pip install sphinx-rtd-theme toml

          - name: Generate Docs
            run: make docs

          - name: Deploy docs to GitHub Pages
            uses: peaceiris/actions-gh-pages@v3
            with:
              github_token: ${{ secrets.GITHUB_TOKEN }}
              publish_dir: docs/_build/html
              allow_empty_commit: true
              keep_files: true

Create one more pull request and merge your changes to master. Check the actions tab
once your changes have been merged.

Once the Documentation test passes check the site you'll be able to find your
documentation at https://sp-fm.github.io/python-lifecycle-training

Add a badge
-----------

.. image:: https://github.com/sp-fm/python-lifecycle-training/workflows/Documentation/badge.svg
    :target: https://sp-fm.github.io/python-lifecycle-training/
    :alt: Documentation

.. code-block:: RST

    .. image:: https://github.com/sp-fm/python-lifecycle-training/workflows/Documentation/badge.svg
        :target: https://sp-fm.github.io/python-lifecycle-training/
        :alt: Documentation

Next Step
---------

To move on to the next step commit or stash your changes then checkout to the branch
``deploy/ci/release``

.. code-block:: console

    $ git stash
    $ git checkout deploy/ci/release

.. _create a GitHub Pages site: https://docs.github.com/en/free-pro-team@latest/github/working-with-github-pages/creating-a-github-pages-site
