# -*- coding: utf-8 -*-

NAME = 'gpsdshm'
VERSION = '0.1.0'
LICENSE = 'BSD License'
AUTHOR = 'Markus Juenemann'
EMAIL = 'markus@juenemann.net'
DESCRIPTION = 'Python interface to gpsd shared memory'
URL = 'https://github.com/mjuenema/python-gpsdshm'

from setuptools import setup, Extension
shm_module = Extension('gpsdshm._shm', sources=['gpsdshm/shm.c', 'gpsdshm/shm_wrap.c'],)

from os.path import join, dirname

readme = open(join(dirname(__file__), 'README.rst')).read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = open(join(dirname(__file__), 'requirements.txt')).read().split()
test_requirements = open(join(dirname(__file__), 'test_requirements.txt')).read().split()

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=readme + '\n\n' + history,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=[
        NAME,
    ],
    package_dir={NAME: NAME},
    include_package_data=True,
    install_requires=requirements,
    ext_modules = [shm_module],
    py_modules = [NAME],
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
    tests_require=test_requirements
)
