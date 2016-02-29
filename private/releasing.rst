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
#. Merge all "feature" branches into the "develop" branch.
#. Run ``make lint``.
#. Run ``make test`` to check for problems.
#. Run ``make test_gpsfake`` to run the test suite against *gpsfake* inside a Docker container.
#. Create the ``gpsdshm/shm.i`` file by running ``make swig``.
#. Push the 'develop" branch to Github.
#. Fix the issue listed on Codacy (https://www.codacy.com/app/markus_2/python-gpsdshm)
#. Fix the issues listed on Landscape (https://landscape.io/github/mjuenema/python-gpsdshm)
#. Verify that the "develop" branch passes all tests on Travis-CI (https://travis-ci.org/mjuenema/python-gpsdshm/branches)
#. Verify that the tests cover 100% of the code on Codecov (https://www.codacy.com/app/markus_2/python-gpsdshm) 
#. Start a new "release" branch.
#. Update the version number in ``setup.py``.
#. Update the ``HISTORY.rst`` file.
#. Verify that the code examples in ``README.rst`` are correct.
#. Push the "release" branch to Github.
#. Verify that the "release" branch has no issues on Codacy.
#. Verify that the "release" branch has no issues on Landscape.
#. Verify that the "release" branch passes all tests on Travis-CI.
#. Verify that the "release" branch has 100% test coverage on Codecov.
#. Fix any problems above in the "release' branch.
#. Finish the "release' branch.
#. Upload the package to PyPi.

Markus Juenemann, 17-Feb-2016
