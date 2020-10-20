==========
Pre-commit
==========

**Git hook scripts** are useful for identifying simple issues before submission to code
review. **Pre-commit** runs on every commit to automatically point out issues in code
such as trailing whitespace, and debug statements. By pointing these issues out before
code review, this allows a code reviewer to focus on the architecture of a change while
not wasting time with trivial style nitpicks.

**Pre-commit** is a multi-language package manager for pre-commit hooks. You specify a
list of hooks you want and pre-commit manages the installation and execution of any hook
written in any language before every commit. pre-commit is specifically designed to not
require root access. If one of your developers doesn’t have node installed but modifies
a JavaScript file, pre-commit automatically handles downloading and building node to run
eslint without root.

For further information visit https://pre-commit.com/

Installation
------------

.. code-block:: console

    $ poetry add pre-commit --dev
    $ pre-commit install

Configuration
-------------

Create a ``.pre-commit-config.yaml`` file and add the following:

.. code-block:: YAML

    repos:
      - repo: https://github.com/pre-commit/pre-commit-hooks
        rev: v3.2.0
        hooks:
          - id: check-added-large-files
            name: Check for added large files
            description: Prevent giant files from being committed
            entry: check-added-large-files

          - id: check-ast
            name: Check python ast
            description: Simply check whether the files parse as valid python.
            entry: check-ast
            types: [python]

          - id: check-case-conflict
            name: Check for case conflicts
            description: Check for files that would conflict in case-insensitive filesystems
            entry: check-case-conflict

          - id: check-merge-conflict
            name: Check for merge conflicts
            description: Check for files that contain merge conflict strings.
            entry: check-merge-conflict
            types: [text]

          - id: debug-statements
            name: Debug Statements (Python)
            description: Check for debugger imports and py37+ `breakpoint()` calls in python source.
            entry: debug-statement-hook
            types: [python]

          - id: end-of-file-fixer
            name: Fix End of Files
            description: Ensures that a file is either empty, or ends with one newline.
            entry: end-of-file-fixer
            types: [text]
            stages: [commit, push, manual]

          - id: mixed-line-ending
            name: Mixed line ending
            description: Replaces or checks mixed line ending
            entry: mixed-line-ending
            types: [text]

          - id: no-commit-to-branch
            name: "Don't commit to branch"
            entry: no-commit-to-branch
            pass_filenames: false
            always_run: true

          - id: trailing-whitespace
            name: Trim Trailing Whitespace
            description: This hook trims trailing whitespace.
            entry: trailing-whitespace-fixer
            types: [text]
            stages: [commit, push, manual]

      - repo: https://github.com/asottile/add-trailing-comma
        rev: v2.0.1
        hooks:
          - id: add-trailing-comma
            args: [--py36-plus]

      - repo: https://github.com/psf/black
        rev: 20.8b1
        hooks:
          - id: black
            language_version: python3

      - repo: https://github.com/pycqa/isort
        rev: 5.5.4
        hooks:
          - id: isort

      - repo: https://gitlab.com/pycqa/flake8
        rev: 3.8.4
        hooks:
          - id: flake8

      - repo: https://github.com/pre-commit/mirrors-mypy
        rev: v0.782
        hooks:
          - id: mypy
            exclude: docs

      - repo: https://github.com/prettier/prettier
        rev: 2.1.2
        hooks:
          - id: prettier

Usage
-----

Pre-commit will run automatically every time you make a commit.

.. code-block:: console

    $ git add .
    $ git commit

.. image:: ../_static/pre-commit/img/run.png
    :alt: Pre-commit output

You can run it manually as well.

.. code-block:: console

    $ pre-commit run

.. image:: ../_static/pre-commit/img/run.png
    :alt: Pre-commit run output

If you want to run pre-commit on all your files:

.. code-block:: console

    $ pre-commit run --all-files

.. image:: ../_static/pre-commit/img/run-all-files.png
    :alt: Pre-commit run all-files output

Or if you want to run pre-commit on specific files/folders:

.. code-block:: console

    $ pre-commit run --files python_lifecycle_training tests

.. image:: ../_static/pre-commit/img/run-files.png
    :alt: Pre-commit run files output

You can also run a specific hook:

.. code-block:: console

    $ pre-commit run flake8 --files tests/calculator/test_simple.py

.. image:: ../_static/pre-commit/img/run-flake8.png
    :alt: Pre-commit run flake8 output

Useful Commands
---------------

You can update your hooks to the latest version automatically by running:

.. code-block:: console

    $ pre-commit autoupdate

Advanced features
-----------------

Temporarily disable hooks
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: console

    $ SKIP=flake8,mypy git commit

.. image:: ../_static/pre-commit/img/run-skip.png
    :alt: Pre-commit output by disabling hooks

Automatically enable pre-commit for all repositories
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: console

    $ git config --global init.templateDir ~/.git-template
    $ pre-commit init-templatedir ~/.git-template

Add a badge
~~~~~~~~~~~

.. image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
    :target: https://github.com/pre-commit/pre-commit
    :alt: pre-commit

.. code-block:: RST

    .. image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
        :target: https://github.com/pre-commit/pre-commit
        :alt: pre-commit

.. note:: You can remove the unused imports in ``test_simple.py`` to pass flake8 tests.
    You can remove flake8, black, isort and mypy dependencies as well because pre-commit
    has them all covered

Next Step
---------

To move on to the next step commit or stash your changes then checkout to the branch
``setup/cli/fire``

.. code-block:: console

    $ git stash
    $ git checkout setup/cli/fire

Uninstall
---------

.. code-block:: console

    $ pre-commit uninstall
    $ poetry remove pre-commit --dev
