======================================
Continuous Integration: GitHub Actions
======================================

Package Hosting: PyPi
---------------------

Project Description
~~~~~~~~~~~~~~~~~~~

Add some description for your project.

.. code-block:: cfg

    [tool.poetry]
    name = "python-lifecycle-training"
    version = "0.1.0"
    repository = "https://github.com/sp-95/python-lifecycle-training"
    documentation = "https://sp-95.github.io/python-lifecycle-training/"
    description = "A training program to learn the Python Development Cycle"
    authors = ["Shashanka Prajapati <shashanka@fusemachines.com>"]
    readme = "README.rst"
    license =  "MIT license"
    keywords = []
    classifiers = [
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ]
    packages = [
        { include = "python_lifecycle_training" },
        { include = "tests", format = "sdist" },
    ]

    [tool.poetry.urls]
    "Bug Tracker" = "https://github.com/sp-95/python-lifecycle-training/issues"

Token Setup
~~~~~~~~~~~

* Create a PyPi account if you don’t have one.
* Goto **Account Settings** from the top right corner
* Click **Add API token**
* Set the **Token name** and **Scope**
* Click **Add token**

**IMPORTANT NOTICE**: Save this token ID somewhere very safe as it represents your PyPi
identity. You’ll need this to deploy packages. If you lose it then you’ll have to
generate a new one. If others get hold of this token then they can host packages in
your name.

Add Token to your Project
~~~~~~~~~~~~~~~~~~~~~~~~~

* Go to your project settings
* Click on **Secrets**
* Click on **New secret**
* Add your token as PYPI_TOKEN

Sample Configuration
~~~~~~~~~~~~~~~~~~~~

.. code-block:: YAML

    #.github/workflows/upload-python-package.yml
    name: Release

    on:
      release:
        types: [created]

    jobs:
      deploy:
        runs-on: ubuntu-latest

        steps:
          - uses: actions/checkout@v2

          - name: Set up Python
            uses: actions/setup-python@v2
            with:
              python-version: "3.x"

          - name: Get full python version
            id: full-python-version
            run: echo ::set-output name=version::$(python -c "import sys; print('-'.join(str(v) for v in sys.version_info[:3]))")

          - name: Install and set up Poetry
            run: |
              python -m pip install --upgrade pip
              pip install --upgrade poetry --pre
              poetry config virtualenvs.in-project true

          - name: Set up cache
            uses: actions/cache@v1
            with:
              path: .venv
              key: venv-${{ runner.os }}-${{ steps.full-python-version.outputs.version }}-${{ hashFiles('**/poetry.lock') }}

          - name: Install dependencies
            run: poetry install

          - name: Build and publish
            env:
              PYPI_TOKEN: ${{ secrets.PYPI_TOKEN }}
            run: |
              poetry config pypi-token.pypi $PYPI_TOKEN
              poetry publish --build

Most of the commands meant for PyPi hosting are handled by poetry.

Tagged Commit
~~~~~~~~~~~~~

When you push a tag to GitHub it's called as a tagged commit.

.. code-block:: console

    $ poetry version minor
    $ git add pyproject.toml
    $ git commit -m "chore: bump version from 0.1.0 to 0.2.0"
    $ git tag `poetry version -s`
    $ git push --tags

Release
~~~~~~~

* Click on tags in your project repo
* Go to Releases
* Draft a new release
* Add the tag version, release title, and the description. You can edit the PR
  description
* Click on Publish Release
* Check if your package is there in PyPi

.. note:: Generally a pre-release is published until it’s stable. It’s published as an
   official release at a later date.

Add a badge
-----------

.. image:: https://github.com/sp-95/python-lifecycle-training/workflows/Release/badge.svg
    :target: https://pypi.python.org/pypi/python-lifecycle-training
    :alt: Release

.. code-block:: RST

    .. image:: https://github.com/sp-95/python-lifecycle-training/workflows/Release/badge.svg
        :target: https://pypi.python.org/pypi/python-lifecycle-training
        :alt: Release

.. image:: https://img.shields.io/pypi/v/python-lifecycle-training.svg
    :target: https://pypi.python.org/pypi/python-lifecycle-training
    :alt: PyPi Version

.. code-block:: RST

    .. image:: https://img.shields.io/pypi/v/python-lifecycle-training.svg
        :target: https://pypi.python.org/pypi/python-lifecycle-training
        :alt: PyPi Version
