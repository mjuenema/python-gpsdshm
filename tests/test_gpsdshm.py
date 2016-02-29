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

from nose.tools import *

import minimock

import gpsdshm
import gpsdshm.shm
import time

gpsd_shm = None


def setup():
    global gpsd_shm

    gpsd_shm = gpsdshm.Shm()

    assert gpsdshm._error is None

    if gpsd_shm.fix.latitude != 0.0:
        sys.stderr.write('Using real gpsd data for tests...\n')
    else:
        sys.stderr.write('Using mock gpsd data for tests...\n')
        import _mock
        gpsd_shm = _mock.MockShm()

@raises(IndexError)
def test_satellites_index_error():
    d = gpsd_shm.satellites[gpsdshm.shm.MAXCHANNELS]

@raises(IndexError)
def test_devices_index_error():
    if gpsdshm.GPSD_API_MAJOR_VERSION == 6:
        d = gpsd_shm.devices[gpsdshm.shm.MAXUSERDEVS]
    else:
        d = gpsd_shm.devices[1]

def test_gpsdshm_Shm_error():
    gpsdshm.shm.shm_get = minimock.Mock('gpsdshm.shm.shm_get')
    gpsdshm.shm.shm_get.mock_returns = None
    try:
        gpsdshm.Shm()
    except OSError:
        minimock.restore()
        return
    raise Exception('gpsdshm.shm.shm_get did nto raise OSError')

@raises(OSError)
def test_gpsdshm_error():
    gpsdshm._error = 'test'
    assert gpsdshm._error == 'test'

    os_error = OSError('GPSd shared memory error: %s' % (gpsdshm._error))
    assert str(os_error) == 'GPSd shared memory error: test'

    raise os_error

def test_gpsdshm():

    now = time.time()

    assert gpsdshm.GPSD_API_MAJOR_VERSION in [5,6]
    assert isinstance(gpsdshm.GPSD_API_MINOR_VERSION, (int))

    assert gpsdshm.STATUS_NO_FIX == 0
    assert gpsdshm.STATUS_FIX == 1
    assert gpsdshm.STATUS_DGPS_FIX == 2

    assert isinstance(gpsd_shm.online, (float))
    assert 1060820354.0 <= gpsd_shm.online < now+2

    assert isinstance(gpsd_shm.status, (int))
    assert not isinstance(gpsd_shm.status, (bool))      # issue 6
    assert gpsd_shm.status in [gpsdshm.STATUS_NO_FIX, gpsdshm.STATUS_FIX, gpsdshm.STATUS_DGPS_FIX]

    assert isinstance(gpsd_shm.skyview_time, (float))
    assert now-2 < gpsd_shm.skyview_time < now+2 or math.isnan(gpsd_shm.skyview_time)

    assert isinstance(gpsd_shm.satellites_visible, (int))
    assert 0 < gpsd_shm.satellites_visible < 73

    assert isinstance(gpsd_shm.fix.time, (float))
    assert 1060820354.0 <= gpsd_shm.fix.time < now+2

    assert gpsd_shm.fix.mode in [2,3]

    assert isinstance(gpsd_shm.fix.ept, (float))
    assert 0.0 < gpsd_shm.fix.ept < 0.1

    assert isinstance(gpsd_shm.fix.latitude, (float))
    assert -90.0 < gpsd_shm.fix.latitude < 90.0

    assert isinstance(gpsd_shm.fix.epy, (float))
    assert 1.0 < gpsd_shm.fix.epy < 100.0

    assert isinstance(gpsd_shm.fix.longitude, (float))
    assert -180.0 < gpsd_shm.fix.longitude < 180.0

    assert isinstance(gpsd_shm.fix.epx, (float))
    assert 1.0 < gpsd_shm.fix.epx < 100.0

    assert isinstance(gpsd_shm.fix.altitude, (float))
    assert -100.0 < gpsd_shm.fix.altitude < 12000.0

    assert isinstance(gpsd_shm.fix.epv, (float))
    assert 1.0 < gpsd_shm.fix.epv < 100.0

    assert isinstance(gpsd_shm.fix.track, (float))
    assert 0.0 <= gpsd_shm.fix.track <= 365.0

    assert isinstance(gpsd_shm.fix.epd, (float))
    assert 0.0 <= gpsd_shm.fix.epd <= 365 or math.isnan(gpsd_shm.fix.epd)

    assert isinstance(gpsd_shm.fix.speed, (float))
    assert 0.0 <= gpsd_shm.fix.speed <= 343.0

    assert isinstance(gpsd_shm.fix.eps, (float))
    assert 0.0 <= gpsd_shm.fix.eps <= 343.0 or math.isnan(gpsd_shm.fix.eps)

    assert isinstance(gpsd_shm.fix.climb, (float))
    assert -100.0 < gpsd_shm.fix.climb < 100.0

    assert isinstance(gpsd_shm.fix.epc, (float))
    assert -100.0 < gpsd_shm.fix.epc < 100.0 or math.isnan(gpsd_shm.fix.epc)

    assert isinstance(gpsd_shm.dop.xdop, (float))
    assert 0.0 < gpsd_shm.dop.xdop < 10.0 or math.isnan(gpsd_shm.dop.xdop)

    assert isinstance(gpsd_shm.dop.ydop, (float))
    assert 0.0 < gpsd_shm.dop.ydop < 10.0 or math.isnan(gpsd_shm.dop.ydop)

    assert isinstance(gpsd_shm.dop.pdop, (float))
    assert 0.0 < gpsd_shm.dop.pdop < 10.0 or math.isnan(gpsd_shm.dop.pdop)

    assert isinstance(gpsd_shm.dop.hdop, (float))
    assert 0.0 < gpsd_shm.dop.hdop < 10.0 or math.isnan(gpsd_shm.dop.hdop)

    assert isinstance(gpsd_shm.dop.vdop, (float))
    assert 0.0 < gpsd_shm.dop.vdop < 10.0 or math.isnan(gpsd_shm.dop.vdop)

    assert isinstance(gpsd_shm.dop.tdop, (float))
    assert 0.0 < gpsd_shm.dop.tdop < 10.0 or math.isnan(gpsd_shm.dop.tdop)

    assert isinstance(gpsd_shm.dop.gdop, (float))
    assert 0.0 < gpsd_shm.dop.gdop < 10.0 or math.isnan(gpsd_shm.dop.gdop)

    for i in range(gpsdshm.MAXCHANNELS):
        assert isinstance(gpsd_shm.satellites[i].ss, (float))
        assert 0.0 <= gpsd_shm.satellites[i].ss < 50.0

        assert isinstance(gpsd_shm.satellites[i].used, (bool))

        assert isinstance(gpsd_shm.satellites[i].prn, (int))
        assert 0 <= gpsd_shm.satellites[i].prn

        assert isinstance(gpsd_shm.satellites[i].PRN, (int))
        assert gpsd_shm.satellites[i].prn == gpsd_shm.satellites[i].PRN

        assert isinstance(gpsd_shm.satellites[i].elevation, (int))
        assert -10 <= gpsd_shm.satellites[i].elevation <= 90

        assert isinstance(gpsd_shm.satellites[i].azimuth, (int))
        assert 0 <= gpsd_shm.satellites[i].azimuth , 360.0

    assert isinstance(gpsd_shm.ndevices, (int))

    for i in range(gpsdshm.MAXUSERDEVS):
        assert isinstance(gpsd_shm.devices[i].path, (str)) or gpsd_shm.devices[i].path is None

        assert isinstance(gpsd_shm.devices[i].flags, (int))
        assert gpsd_shm.devices[i].flags in [gpsdshm.SEEN_GPS, gpsdshm.SEEN_RTCM2, gpsdshm.SEEN_RTCM3, gpsdshm.SEEN_AIS, 0]

        assert isinstance(gpsd_shm.devices[i].driver, (str))

        assert isinstance(gpsd_shm.devices[i].subtype, (str))

        assert isinstance(gpsd_shm.devices[i].activated, (float))

        assert isinstance(gpsd_shm.devices[i].baudrate, (int))

        assert isinstance(gpsd_shm.devices[i].stopbits, (int))
        assert gpsd_shm.devices[i].stopbits in [0, 1, 2]

        assert isinstance(gpsd_shm.devices[i].parity, (str)) or gpsd_shm.devices[i].parity is None
        assert gpsd_shm.devices[i].parity in ['N', 'O', 'E', None]

        assert isinstance(gpsd_shm.devices[i].cycle, (float))

        assert isinstance(gpsd_shm.devices[i].mincycle, (float))

        assert isinstance(gpsd_shm.devices[i].driver_mode, (int))
