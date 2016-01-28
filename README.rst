**************
python-gpsdshm
**************

**This project has not released any code yet!**

Overview
========

*python-gpsdshm* provides a read-only(!) Python interface to `gpsd`_'s shared memory. It provides
a single class ``GpsdShm`` that exposes the fields of the shared memory structure as attributes.

*python-gpsdshm* is implemented using Swig_ and requires the `gpsd` header files for compilation.

Many Linux distributions ship the gpsd package **without** shared memory support.
See `Compiling gpsd with shared memory support`_ for details how build gpsd
with shared memory support.

.. _`gpsd`: http://www.catb.org/gpsd/
.. _Swig: http://www.swig.org/Doc1.3/Python.html

Example
=======

.. code-block:: python

   >>> import gpsdshm
   >>> gpsd_shm = gpsdshm.GpsdShm()
   >>> gpsd_shm.set
   >>> gpsd_shm.online               # True if GPS is online
   >>> gpsd_shm.fd                   # Unix socket or fildescriptor to GPS 
   >>> gpsd_shm.status               # Do we have a fix (True/False)?
   >>> gpsd_shm.skyview_time         # Skyview timestamp
   >>> gpsd_shm.satellites_visible   # Number of satellites in view
   
   >>> gpsd_shm.fix.time             # Time of update
   >>> gpsd_shm.fix.mode             # Mode of fix (0=not seen, 1=no fix, 2=2D, 3=3D)
   >>> gpsd_shm.fix.ept              # Expected time uncertainty 
   >>> gpsd_shm.fix.latitude         # Latitude in degrees (valid if mode >= 2)
   >>> gpsd_shm.fix.epy              # Latitude position uncertainty, meters
   >>> gpsd_shm.fix.longitude        # Longitude in degrees (valid if mode >= 2)
   >>> gpsd_shm.fix.epx              # Longitude position uncertainty, meters 
   >>> gpsd_shm.fix.alitude          # Altitude in meters (valid if mode == 3)
   >>> gpsd_shm.fix.epv              # Vertical position uncertainty, meters
   >>> gpsd_shm.fix.track            # Course made good (relative to true north)
   >>> gpsd_shm.fix.epd              # Track uncertainty, degrees
   >>> gpsd_shm.fix.speed            # Speed over ground, meters/sec
   >>> gpsd_shm.fix.eps              # Speed uncertainty, meters/sec
   >>> gpsd_shm.fix.climb            # Vertical speed, meters/sec 
   >>> gpsd_shm.fix.epc              # Vertical speed uncertainty
   
   >>> gpsd_shm.dop.xdop              
   >>> gpsd_shm.dop.ydop
   >>> gpsd_shm.dop.pdop
   >>> gpsd_shm.dop.hdop
   >>> gpsd_shm.dop.vdop
   >>> gpsd_shm.dop.tdop
   >>> gpsd_shm.dop.gdop

Information about satellites is contained in the ``skyview`` list.
   
.. code-block:: python
   
   >>> gpsd_shm.skyview[0].ss         # Signal-to-noise ratio (dB)
   >>> gpsd_shm.skyview[0].used       # Used in solution?
   >>> gpsd_shm.skyview[0].prn        # PRNs of satellite
   >>> gpsd_shm.skyview[0].elevation  # Elevation of satellite, degrees
   >>> gpsd_shm.skyview[0].azimuth    # Azimuth, degrees



Compiling gpsd with shared memory support
=========================================

.. code-block:: console

   $ git clone git://git.sv.gnu.org/gpsd.git
   $ cd gpsd
   $ git tag
   $ git checkout release-3.16
   $ scons prefix=/usr/local shm_export=yes
   $ scons install
