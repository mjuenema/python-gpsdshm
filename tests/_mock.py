"""
Mock `gpsdshm.Shm` for testing without a real GPS.

Markus Juenemann, 04-Feb-2016

"""

import time
from gpsdshm.shm import MAXCHANNELS

class MockFix(object):
    def __init__(self):
        self.time = time.time()
        self.mode = 3
        self.ept = 0.005
        self.latitude = -36.75859333333334
        self.epy = 14.853882022256698
        self.longitude = 143.99911
        self.epx = 10.040781879264545
        self.altitude = 68.2
        self.epv = 19.55
        self.track = 44.45
        self.epd = float('nan')
        self.speed = 0.3446777748
        self.eps = 29.707764044513397
        self.climb = 0.0
        self.epc = float('nan')


class MockDop(object):
    def __init__(self):
        self.xdop = 0.6693854586176363
        self.ydop = 0.9902588014837799
        self.pdop = 1.17
        self.hdop = 0.99
        self.vdop = 0.82
        self.tdop = 1.2548625723457216
        self.gdop = 2.4342743978108503


class MockSatellite(object):
    def __init__(self, prn):
        self.ss = 0.0 
        self.prn = self.PRN = prn
        self.used = True
        self.elevation = prn
        self.azimuth = prn
        

class MockShm(object):

    def __init__(self):
        self.online = time.time()
        self.status = True
        self.fix_time = time.time()
        self.satellites_visible = 8
        self.fix = MockFix()
        self.dop = MockDop()
        self.skyview_time = float('nan')
        self.satellites = [MockSatellite(prn) for prn in range(MAXCHANNELS)]
         
    
