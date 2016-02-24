# -*- coding: utf-8 -*-
"""setup.py for python-gpsdshm."""

NAME = 'gpsdshm'
VERSION = '0.2'
LICENSE = 'BSD License'
AUTHOR = 'Markus Juenemann'
EMAIL = 'markus@juenemann.net'
DESCRIPTION = 'Python interface to gpsd shared memory'
URL = 'https://github.com/mjuenema/python-gpsdshm'

from setuptools import setup, Extension
shmmodule = Extension('gpsdshm._shm', sources=['gpsdshm/shm.c', 'gpsdshm/shm_wrap.c'],)

from os.path import join, dirname

README = open(join(dirname(__file__), 'README.rst')).read()
HISTORY = open('HISTORY.rst').read().replace('.. :changelog:', '')

REQUIREMENTS = open(join(dirname(__file__), 'requirements.txt')).read().split()
TEST_REQUIREMENTS = open(join(dirname(__file__), 'test_requirements.txt')).read().split()

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=README + '\n\n' + HISTORY,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=[
        NAME,
    ],
    package_dir={NAME: NAME},
    include_package_data=True,
    install_requires=REQUIREMENTS,
    ext_modules=[shmmodule],
    py_modules=[NAME],
    license=LICENSE,
    zip_safe=False,
    keywords='gpsd, shared memory',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: C',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=TEST_REQUIREMENTS
)
