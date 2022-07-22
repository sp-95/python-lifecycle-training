.. highlight:: shell

============
Contributing
============

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/sp-95/python-lifecycle-training/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs that are tagged with ``bug``.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for features that are tagged with ``enhancement``.

Write Documentation
~~~~~~~~~~~~~~~~~~~

Fusemachines Utilities could always use more documentation, whether as part of the
official Fusemachines Utilities docs, in docstrings, or even on the web in blog posts,
articles, and such.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at
https://github.com/sp-95/python-lifecycle-training/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.

Get Started!
------------

Ready to contribute? Here's how to set up **python-lifecycle-training** for local development. Please
note this documentation assumes you already have ``poetry`` and ``git`` installed and
ready to go.

#. Clone the **python-lifecycle-training** repo locally:

   .. code-block:: console

        $ git clone git@github.com:sp-95/python-lifecycle-training.git

#. Assuming you have poetry installed, you can create a new environment for your local
   development by typing:

   .. code-block:: console

        $ poetry shell
        $ poetry install

#. Create a branch for local development:

   .. code-block:: console

        $ git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

#. Before raising a pull request you should run tox. This will run the tests
   across different versions of Python, perform pre-commit checks and tests your
   documentation build.

   .. code-block:: console

        $ tox

#. If your contribution is a bug fix or new feature, you may want to add a test
   to the existing test suite. See the section `Add a New Test`_ below for details.

#. Commit your changes and push your branch to GitHub:

   .. code-block:: console

        $ git add .
        $ git commit -m "Your detailed description of your changes."
        $ git push origin name-of-your-bugfix-or-feature

#. Submit a pull request through the GitHub website.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

#. The pull request should include tests.

#. If the pull request adds functionality, the docs should be updated. Put your new
   functionality into a function with a docstring, and add the feature to the list in
   ``README.rst``.

#. The pull request should work for Python 3.7 and 3.8. Check
   https://github.com/sp-95/python-lifecycle-training/actions?query=workflow%3ATests
   and make sure that the tests pass for all supported Python versions.

.. _new_test:

Add a New Test
--------------

When fixing a bug or adding features, it's good practice to add a test to demonstrate
your fix or new feature behaves as expected. These tests should focus on one tiny bit
of functionality and prove changes are correct.

To write and run your new test, follow these steps:

#. Add the new test to ``tests/<module>/test_<feature>.py``. Focus your test on the
   specific bug or a small part of the new feature.

#. If you have already made changes to the code, stash your changes and confirm all
   your changes were stashed:

   .. code-block:: console

        $ git stash
        $ git stash list

#. Run your test and confirm that your test fails. If your test does not fail, rewrite
   the test until it fails on the original code:

   .. code-block:: console

        $ pytest

#. (Optional) Run the tests with tox to ensure that the code changes work with
   different Python versions:

   .. code-block:: console

        $ tox

#. Proceed work on your bug fix or the new feature or restore your changes. To restore
   your stashed changes and confirm their restoration:

   .. code-block:: console

        $ git stash pop
        $ git stash list

#. Rerun your test and confirm that your test passes. If it passes, congratulations!

Deploying
---------

A reminder for the maintainers on how to deploy. Make sure all your changes are
committed (including an entry in CHANGELOG.rst). Then run:

   .. code-block:: console

         $ poetry version patch
         $ git tag `poetry version -s`
         $ git push --tags

GitHub Actions will then deploy to PyPI once you make a release if tests pass.

See pypi-release-checklist_ for more information.

.. _pypi-release-checklist: https://sp-95.github.io/python-lifecycle-training/pypi_release_checklist.html
.. _Add a New Test: new_test_
