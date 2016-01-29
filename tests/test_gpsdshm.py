"""
Tests for gpsdshm.

These tests can be run against a real gpsd with shared memory 
or a mock-up. This is determined by whether the `shm.fix.latitude`
attribute returns a "real" value or 0.0. The mock-up version is
useful when running 'python setup.py test' or testing under tox
and there is no gpsd process running.

The threshholds for valid values are somewhat arbitrary with the
hope that they pass in most common scenarios. If testing against 
a real GPS, let the GPS settle-in for a while. Also don't run
the tests while at supersonic speed or at higher altitude than 
Mt Everest. They are guaranteed to fail!

Markus Juenemann, 29-Jan-2016

"""

import sys
import math

#from nose.tools import *

import gpsdshm
import time
import types

gpsd_shm = None


def setup():
    global gpsd_shm

    gpsd_shm = gpsdshm.Shm()

    if gpsd_shm.fix.latitude <> 0.0:
        sys.stderr.write('Using real gpsd data for tests...\n')
    else:
        sys.stderr.write('Using mock gpsd data for tests...\n')


def test_gpsdshm():

    now = time.time()

    assert isinstance(gpsd_shm.online, types.FloatType)
    assert now-1 < gpsd_shm.online < now+1

    assert gpsd_shm.status is True

    assert isinstance(gpsd_shm.skyview_time, types.FloatType)
    assert now-1 < gpsd_shm.skyview_time < now+1 or math.isnan(gpsd_shm.skyview_time)

    assert isinstance(gpsd_shm.satellites_visible, types.IntType)
    assert 0 < gpsd_shm.satellites_visible < 73

    assert isinstance(gpsd_shm.fix.time, types.FloatType)
    assert now-2 < gpsd_shm.fix.time < now+2

    assert gpsd_shm.fix.mode in [2,3]

    assert isinstance(gpsd_shm.fix.ept, types.FloatType)
    assert 0.0 < gpsd_shm.fix.ept < 0.1

    assert isinstance(gpsd_shm.fix.latitude, types.FloatType)
    assert -90.0 < gpsd_shm.fix.latitude < 90.0

    assert isinstance(gpsd_shm.fix.epy, types.FloatType)
    assert 1.0 < gpsd_shm.fix.epy < 100.0

    assert isinstance(gpsd_shm.fix.longitude, types.FloatType)
    assert -180.0 < gpsd_shm.fix.longitude < 180.0

    assert isinstance(gpsd_shm.fix.epx, types.FloatType)
    assert 1.0 < gpsd_shm.fix.epx < 100.0

    assert isinstance(gpsd_shm.fix.altitude, types.FloatType)
    assert -100.0 < gpsd_shm.fix.altitude < 12000.0

    assert isinstance(gpsd_shm.fix.epv, types.FloatType)
    assert 1.0 < gpsd_shm.fix.epv < 100.0

    assert isinstance(gpsd_shm.fix.track, types.FloatType)
    assert 0.0 <= gpsd_shm.fix.track <= 365.0

    assert isinstance(gpsd_shm.fix.epd, types.FloatType)
    assert 0.0 <= gpsd_shm.fix.epd <= 365 or math.isnan(gpsd_shm.fix.epd)

    assert isinstance(gpsd_shm.fix.speed, types.FloatType)
    assert 0.0 <= gpsd_shm.fix.speed <= 343.0

    assert isinstance(gpsd_shm.fix.eps, types.FloatType)
    assert 0.0 <= gpsd_shm.fix.eps <= 343.0

    assert isinstance(gpsd_shm.fix.climb, types.FloatType)
    assert -100.0 < gpsd_shm.fix.climb < 100.0

    assert isinstance(gpsd_shm.fix.epc, types.FloatType)
    assert -100.0 < gpsd_shm.fix.epc < 100.0 or math.isnan(gpsd_shm.fix.epc)

    assert isinstance(gpsd_shm.dop.xdop, types.FloatType)
    assert 0.0 < gpsd_shm.dop.xdop < 2.0

    assert isinstance(gpsd_shm.dop.ydop, types.FloatType)
    assert 0.0 < gpsd_shm.dop.ydop < 2.0

    assert isinstance(gpsd_shm.dop.pdop, types.FloatType)
    assert 0.0 < gpsd_shm.dop.pdop < 2.0

    assert isinstance(gpsd_shm.dop.hdop, types.FloatType)
    assert 0.0 < gpsd_shm.dop.hdop < 2.0

    assert isinstance(gpsd_shm.dop.vdop, types.FloatType)
    assert 0.0 < gpsd_shm.dop.vdop < 2.0

    assert isinstance(gpsd_shm.dop.tdop, types.FloatType)
    assert 0.0 < gpsd_shm.dop.tdop < 2.0

    assert isinstance(gpsd_shm.dop.gdop, types.FloatType)
    assert 0.0 < gpsd_shm.dop.gdop < 3.0
