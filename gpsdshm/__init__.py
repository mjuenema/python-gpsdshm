"""
Python interface to GPSd Shared Memory.

"""

import time 
import gpsdshm.shm


class Fix(object):

    def __init__(self, shm):
        self.shm = shm

    time = property(lambda self: gpsdshm.shm.get_time(self.shm))
    mode = property(lambda self: gpsdshm.shm.get_mode(self.shm))
    ept = property(lambda self: gpsdshm.shm.get_ept(self.shm))
    latitude = property(lambda self: gpsdshm.shm.get_latitude(self.shm))
    epy = property(lambda self: gpsdshm.shm.get_epy(self.shm))
    longitude = property(lambda self: gpsdshm.shm.get_longitude(self.shm))
    epx = property(lambda self: gpsdshm.shm.get_epx(self.shm))
    altitude = property(lambda self: gpsdshm.shm.get_altitude(self.shm))
    epv = property(lambda self: gpsdshm.shm.get_epv(self.shm))
    track = property(lambda self: gpsdshm.shm.get_track(self.shm))
    epd = property(lambda self: gpsdshm.shm.get_epd(self.shm))
    speed = property(lambda self: gpsdshm.shm.get_speed(self.shm))
    eps = property(lambda self: gpsdshm.shm.get_eps(self.shm))
    climb = property(lambda self: gpsdshm.shm.get_climb(self.shm))
    epc = property(lambda self: gpsdshm.shm.get_epc(self.shm))


class Dop(object):

    def __init__(self, shm):
        self.shm = shm

    xdop = property(lambda self: gpsdshm.shm.get_xdop(self.shm))
    ydop = property(lambda self: gpsdshm.shm.get_ydop(self.shm))
    pdop = property(lambda self: gpsdshm.shm.get_pdop(self.shm))
    hdop = property(lambda self: gpsdshm.shm.get_hdop(self.shm))
    vdop = property(lambda self: gpsdshm.shm.get_vdop(self.shm))
    tdop = property(lambda self: gpsdshm.shm.get_tdop(self.shm))
    gdop = property(lambda self: gpsdshm.shm.get_gdop(self.shm))


class Satellite(object):
    def __init__(self, ss, used, prn, elevation, azimuth):
        self.ss = self.snr = ss
        self.used = used and True
        self.prn = prn
        self.elevation = elevation
        self.azimuth = azimuth


class Skyview(object):
    """List of `GpsdShmSatellite` instances.

    """
    
    def __init__(self, shm):
        self.shm = shm

    def __getitem__(self, index):
        return None


class Device(object):
    def __init__(self, path, flags, driver, subtype, activated,
                 baudrate, stopbits, parity, cycle, mincycle,
                 driver_mode):
        pass


class Devices(object):
    """List of `GpsdShmDevice` (singular) instances.

    """
    
    def __init__(self, shm):
        self.shm = shm

    def __getitem__(self, index):
        return None


class Shm(object):
    """GPSd Shared Memory.

    """

    def __init__(self):

        self.shm = gpsdshm.shm.shm_get()
        if self.shm is None:
            raise OSError('Unable to attach to GPSd shared memory')

        self.fix = Fix(self.shm)
        self.dop = Dop(self.shm)
        self.skyview = Skyview(self.shm)
        self.devices = Devices(self.shm)


    set = property(lambda self: gpsdshm.shm.get_set(self.shm))
    online = property(lambda self: gpsdshm.shm.get_online(self.shm))
    fd = property(lambda self: gpsdshm.shm.get_fd(self.shm))
    status = property(lambda self: gpsdshm.shm.get_status(self.shm))
    dev = device = property(lambda self: gpsdshm.shm.get_dev(self.shm))
    skyview_time = property(lambda self: gpsdshm.shm.get_skyview_time(self.shm))
    satellites_visible = property(lambda self: gpsdshm.shm.get_satellites_visible(self.shm))
    
    
    
