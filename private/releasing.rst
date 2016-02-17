***************
Release process
***************

This document describes the release process for *python-gpsdshm*.
It is mainly meant for my own use.

The *python-gpsdshm* project follows the development model described
by Vincent Driessen in `A successful GIT branching model`_.

.. _`A successful GIT branching model`: http://nvie.com/posts/a-successful-git-branching-model

The steps for preparing a new release are as follows:

#. Ensure that there are no open issues for this release (https://github.com/mjuenema/python-gpsdshm/issues)
#. Fix the issue listed on Codacy (https://www.codacy.com/app/markus_2/python-gpsdshm)
#. Merge all "feature" branches into the "develop" branch.
#. Create the ``gpsdshm/shm.i`` file by running ``make swig``.
#. Push the 'develop" branch to Github.
#. Verify that the "develop" branch passes all tests on Travis-CI (https://travis-ci.org/mjuenema/python-gpsdshm/branches)
#. Start a new "release" branch.
#. Update the version numbers in the following files.
   * ``setup.py``
   * ``gpsdshm/__init__.py``
   * ``docs/source/conf.py``
#. Update the ``HISTORY.rst`` file.
#. Verify that the code examples in ``README.rst`` and ``docs/source/*.rst`` aare current.
#. Push the "release" branch to Github.
#. Verify that the "release" branch has no issues on Codacy.
#. Verify that the "release" branch passes all tests on Travis-CI.
#. Finish the "release' branch.
#. Upload the package to PyPi.

Markus Juenemann, 17-Feb-2016