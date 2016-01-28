**************
python-gpsdshm
**************

Overview
========

*python-gpsdshm* provides a read-only(!) Python interface to `gpsd`_'s shared memory. It provides
a single class ``GpsdShm`` that exposes the fields of the shared memory structure as attributes.

*python-gpsdshm* is implemented using Swig_ and requires the `gpsd` header files for compilation.

.. important:: Many Linux distributions ship the gpsd package **without** shared memory support.
               See `Compiling gpsd with shared memory support`_ for details how build gpsd
               with shared memory support.

.. _`gpsd`: http://www.catb.org/gpsd/
.. _Swig: http://www.swig.org/Doc1.3/Python.html

Example
=======

.. code-block:: python

   >>> import gpsdshm
   >>> gpsd_shm = gpsdshm.GpsdShm()
   >>> gpsd_shm.



Compiling gpsd with shared memory support
=========================================

.. code-block: console

   $ git clone git://git.sv.gnu.org/gpsd.git
   $ cd gpsd
   $ git tag
   $ git checkout release-3.16
   $ scons shm_export=yes
