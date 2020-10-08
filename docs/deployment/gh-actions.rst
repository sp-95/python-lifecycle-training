======================================
Continuous Integration: GitHub Actions
======================================

**GitHub Actions** can be used to automate, customize, and execute your software
development workflows right in your repository with GitHub Actions. You can discover,
create, and share actions to perform any job you'd like, including CI/CD, and combine
actions in a completely customized workflow.

For more information visit https://docs.github.com/en/free-pro-team@latest/actions

Testing
-------

Sample Configurations
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: YAML

    #.github/workflows/python-package.yml
    name: Branch Tests

    on:
      push:
        branches-ignore:
          - master
      pull_request:
        branches-ignore:
          - master

    jobs:
      test:
        runs-on: ubuntu-latest

        strategy:
          matrix:
            python-version: [3.7, 3.8]

        steps:
          - uses: actions/checkout@v2

          - name: Set up Python ${{ matrix.python-version }}
            uses: actions/setup-python@v2
            with:
              python-version: ${{ matrix.python-version }}

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

          - name: Run pre-commit action
            uses: pre-commit/action@v2.0.0

          - name: Run Tox
            run: poetry run tox -e py

.. code-block:: YAML

    #.github/workflows/master-python-package.yml
    name: Tests

    on:
      push:
        branches:
          - master
      pull_request:
        branches:
          - master

    jobs:
      test:
        runs-on: ubuntu-latest

        strategy:
          matrix:
            python-version: [3.7, 3.8]

        steps:
          - uses: actions/checkout@v2

          - name: Set up Python ${{ matrix.python-version }}
            uses: actions/setup-python@v2
            with:
              python-version: ${{ matrix.python-version }}

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

          - name: Run pre-commit action
            env:
              SKIP: no-commit-to-branch
            uses: pre-commit/action@v2.0.0

          - name: Run Tox
            run: poetry run tox -e py

Once you commit and push these files check the actions tab in your project repo in
GitHub to check whether your tests are running or not. Try creating a pull request from
dev branch to master and see what happens.

Here is a sample message to write for your pull request.

.. code-block::

    ## Features
    * Simple Calculator
    * Complex Calculator
    * Broken Calculator

    ## Changes
    * [Pre-commit Hooks](https://pre-commit.com/)
    * CLI: [Fire](https://google.github.io/python-fire/guide/)
    * Logging: [Loguru](https://loguru.readthedocs.io/en/stable/)
    * Configuration Management: [Dynaconf](https://www.dynaconf.com/)
    * Testing: Pytest, Coverage, Tox
    * Documentation: Sphinx

Did the tests start running as soon as you created a PR?

Add a badge
-----------

.. image:: https://github.com/sp-fm/python-lifecycle-training/workflows/Tests/badge.svg
    :target: https://github.com/sp-fm/python-lifecycle-training/actions?query=workflow%3ATests
    :alt: Tests

.. code-block:: RST

    .. image:: https://github.com/sp-fm/python-lifecycle-training/workflows/Tests/badge.svg
        :target: https://github.com/sp-fm/python-lifecycle-training/actions?query=workflow%3ATests
        :alt: Tests

Next Step
---------

To move on to the next step commit or stash your changes then checkout to the branch
``deploy/ci/docs``

.. code-block:: console

    $ git stash
    $ git checkout deploy/ci/docs
