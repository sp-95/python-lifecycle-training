.. _pypi-release-checklist:

PyPI Release Checklist
======================

For Every Release
-------------------

#. Update CHANGELOG.rst

#. Commit the changes:

   .. code-block:: console

        $ git add CHANGELOG.rst
        $ git commit -m "Changelog for upcoming release 0.1.1."

#. Update version number (can also be minor or major)

   .. code-block:: console

        $ poetry version patch

#. Install the package again for local development, but with the new version number:

   .. code-block:: console

        $ poetry install

#. Run the tests:

   .. code-block:: console

        $ tox

#. Create a tag:

   .. code-block:: console

        $ git tag `poetry version -s`

#. Push the commit:

   .. code-block:: console

        $ git push

#. Push the tags:

   .. code-block:: console

        $ git push --tags

#. Create a release on GitHub at https://github.com/sp-fm/python-lifecycle-training/releases.
   Paste the change logs into the release's description, and come up with a title for
   the release.

#. Check the PyPI listing page to make sure that the README, release notes, and roadmap
   display properly. If not, try one of these:

    #. Copy and paste the RestructuredText into http://rst.ninjs.org/ to find out what
       broke the formatting.

    #. Check your long_description locally:

       .. code-block:: console

            $ pip install readme_renderer
            $ python -m readme_renderer PROBLEM.rst >/dev/null

       Replace PROBLEM.rst with the name of the file you are having trouble with
