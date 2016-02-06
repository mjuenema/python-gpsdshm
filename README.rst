**************
python-gpsdshm
**************

Overview
========

*python-gpsdshm* provides a read-only(!) Python interface to `gpsd`_'s shared memory. It provides
a single class ``Shm`` that exposes the fields of the shared memory structure as attributes. The
*python-gpsdshm* API is (loosely) modelled on gpsd version 3.16 (API 6.1). gpsd releases earlier
than 3.0 are not supported.

*python-gpsdshm* is implemented using Swig_ and requires the `gpsd` header files for compilation.

Many Linux distributions ship the gpsd package **without** shared memory support.
See `Compiling gpsd with shared memory support`_ for details how to build gpsd
with shared memory support.

.. _`gpsd`: http://www.catb.org/gpsd/
.. _Swig: http://www.swig.org/Doc1.3/Python.html

Example
=======

The example below shows all attributes and typical values (of a stationary GPS, placed about one metre inside a window).

.. code-block:: python

   >>> import gpsdshm
   >>> gpsd_shm = gpsdshm.Shm()
   >>> gpsd_shm.set
   TODO: <Swig Object of type 'gps_mask_t *' at 0x133bf50>
   >>> gpsd_shm.online               # True if GPS is online
   gpsd_shm.online
   TODO: Out[6]: 1454057376.6934643
   >>> gpsd_shm.status               # Do we have a fix (True/False)?
   gpsd_shm.status
   TODO Out[7]: 1
   >>> gpsd_shm.skyview_time         # Skyview timestamp
   >>> gpsd_shm.satellites_visible   # Number of satellites in view
   TODO: nan
   >>> gpsd_shm.fix.time             # Time of update
   1454057448.0
   >>> gpsd_shm.fix.mode             # Mode of fix (0=not seen, 1=no fix, 2=2D, 3=3D)
   3
   >>> gpsd_shm.fix.ept              # Expected time uncertainty
   0.005
   >>> gpsd_shm.fix.latitude         # Latitude in degrees (valid if mode >= 2)
   -37.75859333333334
   >>> gpsd_shm.fix.epy              # Latitude position uncertainty, meters
   14.853882022256698
   >>> gpsd_shm.fix.longitude        # Longitude in degrees (valid if mode >= 2)
   144.99911
   >>> gpsd_shm.fix.epx              # Longitude position uncertainty, meters 
   10.040781879264545
   >>> gpsd_shm.fix.alitude          # Altitude in meters (valid if mode == 3)
   68.2
   >>> gpsd_shm.fix.epv              # Vertical position uncertainty, meters
   19.55
   >>> gpsd_shm.fix.track            # Course made good (relative to true north)
   44.45
   >>> gpsd_shm.fix.epd              # Track uncertainty, degrees
   nan
   >>> gpsd_shm.fix.speed            # Speed over ground, meters/sec
   0.3446777748
   >>> gpsd_shm.fix.eps              # Speed uncertainty, meters/sec
   29.707764044513397
   >>> gpsd_shm.fix.climb            # Vertical speed, meters/sec 
   0.0
   >>> gpsd_shm.fix.epc              # Vertical speed uncertainty
   nan
   >>> gpsd_shm.dop.xdop
   0.6693854586176363
   >>> gpsd_shm.dop.ydop
   0.9902588014837799
   >>> gpsd_shm.dop.pdop
   1.17
   >>> gpsd_shm.dop.hdop
   0.99
   >>> gpsd_shm.dop.vdop
   0.82
   >>> gpsd_shm.dop.tdop
   1.2548625723457216
   >>> gpsd_shm.dop.gdop
   2.4342743978108503

Information about satellites is contained in the ``satellites`` list.
   
.. code-block:: python
   
   >>> gpsd_shm.satellites[0].ss         # Signal-to-noise ratio (dB)
   16.0
   >>> gpsd_shm.satellites[0].used       # Used in solution?
   False
   >>> gpsd_shm.satellites[0].prn        # PRNs of satellite
   6
   >>> gpsd_shm.satellites[0].elevation  # Elevation of satellite, degrees
   56
   >>> gpsd_shm.satellites[0].azimuth    # Azimuth, degrees
   59


Compiling gpsd with shared memory support
=========================================

.. code-block:: console

   $ git clone git://git.sv.gnu.org/gpsd.git   # git clone http://git.savannah.gnu.org/r/gpsd.git
   $ cd gpsd
   $ git tag
   $ git checkout release-3.16
   $ scons prefix=/usr/local shm_export=yes
   $ sudo scons install
   
Then run start gpsd and check whether the shared segment has been created. 

.. code-block:: console

   $ sudo /usr/local/sbin/gpsd -n /dev/ttyAMA0
   $ ipcs -m | grep 0x47505344
   ------ Shared Memory Segments --------
   key        shmid      owner      perms      bytes      nattch     status  
   0x47505344 163844     root       666        31616      1
