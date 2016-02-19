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
Please note that some Linux distributions contain Swig_ releases that are too old for working with Python 3.

Many Linux distributions ship the gpsd package **without** shared memory support.
See `Compiling gpsd with shared memory support`_ for details how to build gpsd
with shared memory support.

Status
======

*python-gpsdshm* is automatically tested against the following Python versions:

* Python 2.6
* Python 2.7
* Python 3.3
* Python 3.4
* Python 3.5

+--------------+-------------------+-------------------+--------------------+--------------------+
| Branch       | Travis-CI         | Codecov           | Codacy             | Landscape          |
+==============+===================+===================+====================+====================+
| master       | |traviscimaster|  | |codecovmaster|   | |codacymaster|     | |landscapemaster|  |
+--------------+-------------------+-------------------+--------------------+--------------------+
| develop      | |traviscidevelop| | |codecovdevelop|  | |codacydevelop|    | |landscapedevelop| |
+--------------+-------------------+-------------------+--------------------+--------------------+

.. |traviscimaster| image:: https://img.shields.io/travis/mjuenema/python-gpsdshm/master.svg
    :target: https://travis-ci.org/mjuenema/python-gpsdshm/branches

.. |traviscidevelop| image:: https://img.shields.io/travis/mjuenema/python-gpsdshm/develop.svg
    :target: https://travis-ci.org/mjuenema/python-gpsdshm/branches
   
.. |codecovmaster| image:: https://codecov.io/github/mjuenema/python-gpsdshm/coverage.svg?branch=master
    :target: https://codecov.io/github/mjuenema/python-gpsdshm?branch=master
    
.. |codecovdevelop| image:: https://codecov.io/github/mjuenema/python-gpsdshm/coverage.svg?branch=develop
    :target: https://codecov.io/github/mjuenema/python-gpsdshm?branch=develop
    
.. |codacymaster| image:: https://img.shields.io/codacy/aa369a5a5f1c4eccb69ba738ae1a93dd/master.svg
    :target: https://www.codacy.com/app/markus_2/python-gpsdshm/dashboard

.. |codacydevelop| image:: https://img.shields.io/codacy/aa369a5a5f1c4eccb69ba738ae1a93dd/develop.svg
    :target: https://www.codacy.com/app/markus_2/python-gpsdshm/dashboard
    
.. |landscapemaster| image:: https://landscape.io/github/mjuenema/python-gpsdshm/master/landscape.svg?style=flat
   :target: https://landscape.io/github/mjuenema/python-gpsdshm/master
   
.. |landscapedevelop| image:: https://landscape.io/github/mjuenema/python-gpsdshm/develop/landscape.svg?style=flat
   :target: https://landscape.io/github/mjuenema/python-gpsdshm/develop

.. _`python-gpsdshm Travis-CI page`: https://travis-ci.org/mjuenema/python-gpsdshm



.. _`gpsd`: http://www.catb.org/gpsd/
.. _Swig: http://www.swig.org/Doc1.3/Python.html

Example
=======

The ``gpsdshm.Shm`` class provides the interface to gpsd's shared memory.

.. code-block:: python

   >>> import gpsdshm
   >>> gpsd_shm = gpsdshm.Shm()
   >>> gpsd_shm.online               # Timestamp if GPS is online, 0 otherwise
   1454057376.6934643
   >>> gpsd_shm.status               # Do we have a fix?
   1
   >>> gpsd_shm.status == gpsdshm.STATUS_FIX 
   True
   >>> gpsd_shm.status == gpsdshm.STATUS_NO_FIX 
   False
   >>> gpsd_shm.skyview_time         # Skyview timestamp
   >>> gpsd_shm.satellites_visible   # Number of satellites in view
   6

GPS Fix
-------

.. code-block:: python

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

Dilution of precisions (DOP)
----------------------------

.. code-block:: python

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

Satellites
----------

Information about satellites is contained in the ``satellites`` list. The
list is always ``gpsdshm.MAXCHANNELS`` entries long, even if only a few
satellites are visible.

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

Devices
-------

The ``devices`` list contains either information about all devices gpsd is currently
monitoring (gpsd release 3.12 and later, ``gpsdshm.GPSD_API_MAJOR_VERSION`` == 6) or a 
single entry with information about the device that shipped the most recent update 
(gpsd release 3.11 and earlier,  ``gpsdshm.GPSD_API_MAJOR_VERSION`` == 5).

.. code-block:: python

   >>> gpsd_shm.devices[0].path
   /dev/ttyAMA0
   >>> gpsd_shm.devices[0].flags && gpsdshm.SEEN_GPS
   1
   >>> gpsd_shm.devices[0].flags && gpsdshm.SEEN_RTCM2
   0
   >>> gpsd_shm.devices[0].flags && gpsdshm.SEEN_RTCM3
   0
   >>> gpsd_shm.devices[0].flags && gpsdshm.SEEN_AIS
   0
   >>> gpsd_shm.devices[0].driver
   >>> gpsd_shm.devices[0].subtype
   >>> gpsd_shm.devices[0].activated
   >>> gpsd_shm.devices[0].baudrate
   4800
   >>> gpsd_shm.devices[0].stopbits
   1
   >>> gpsd_shm.devices[0].parity         # 'N', 'O', or 'E'
   N
   >>> gpsd_shm.devices[0].cylce
   >>> gpsd_shm.devices[0].mincylce
   >>> gpsd_shm.devices[0].driver_mode


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
