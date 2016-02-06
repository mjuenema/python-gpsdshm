"""
Python interface to GPSd Shared Memory.

"""

import gpsdshm.shm


class Fix(object):

    def __init__(self, shm):
        self.shm = shm

    time = property(lambda self: gpsdshm.shm.get_fix_time(self.shm))
    mode = property(lambda self: gpsdshm.shm.get_fix_mode(self.shm))
    ept = property(lambda self: gpsdshm.shm.get_fix_ept(self.shm))
    latitude = property(lambda self: gpsdshm.shm.get_fix_latitude(self.shm))
    epy = property(lambda self: gpsdshm.shm.get_fix_epy(self.shm))
    longitude = property(lambda self: gpsdshm.shm.get_fix_longitude(self.shm))
    epx = property(lambda self: gpsdshm.shm.get_fix_epx(self.shm))
    altitude = property(lambda self: gpsdshm.shm.get_fix_altitude(self.shm))
    epv = property(lambda self: gpsdshm.shm.get_fix_epv(self.shm))
    track = property(lambda self: gpsdshm.shm.get_fix_track(self.shm))
    epd = property(lambda self: gpsdshm.shm.get_fix_epd(self.shm))
    speed = property(lambda self: gpsdshm.shm.get_fix_speed(self.shm))
    eps = property(lambda self: gpsdshm.shm.get_fix_eps(self.shm))
    climb = property(lambda self: gpsdshm.shm.get_fix_climb(self.shm))
    epc = property(lambda self: gpsdshm.shm.get_fix_epc(self.shm))


class Dop(object):

    def __init__(self, shm):
        self.shm = shm

    xdop = property(lambda self: gpsdshm.shm.get_dop_xdop(self.shm))
    ydop = property(lambda self: gpsdshm.shm.get_dop_ydop(self.shm))
    pdop = property(lambda self: gpsdshm.shm.get_dop_pdop(self.shm))
    hdop = property(lambda self: gpsdshm.shm.get_dop_hdop(self.shm))
    vdop = property(lambda self: gpsdshm.shm.get_dop_vdop(self.shm))
    tdop = property(lambda self: gpsdshm.shm.get_dop_tdop(self.shm))
    gdop = property(lambda self: gpsdshm.shm.get_dop_gdop(self.shm))


class Satellite(object):
    def __init__(self, ss, used, prn, elevation, azimuth):
        self.ss = self.snr = ss
        self.used = used and True
        self.prn = self.PRN = prn
        self.elevation = elevation
        self.azimuth = azimuth


class Satellites(object):
    """List of `GpsdShmSatellite` instances.

    """
    
    def __init__(self, shm):
        self.shm = shm

    def __getitem__(self, index):

        if index > gpsdshm.shm.MAXCHANNELS-1:
            raise IndexError

        ss = gpsdshm.shm.get_satellite_ss(self.shm, index)
        used = gpsdshm.shm.get_satellite_used(self.shm, index) == True
        prn = gpsdshm.shm.get_satellite_prn(self.shm, index)
        elevation = gpsdshm.shm.get_satellite_elevation(self.shm, index)
        azimuth = gpsdshm.shm.get_satellite_azimuth(self.shm, index)

        return Satellite(ss, used, prn, elevation, azimuth)


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
        if self.shm == None:
            raise OSError('GPSd shared memory error: %s' % (self.shm, gpsdshm._error))

        self.fix = Fix(self.shm)
        self.dop = Dop(self.shm)
        self.satellites = Satellites(self.shm)
        self.devices = Devices(self.shm)


    set = property(lambda self: gpsdshm.shm.get_set(self.shm))
    online = property(lambda self: gpsdshm.shm.get_online(self.shm))
    fd = property(lambda self: gpsdshm.shm.get_fd(self.shm))
    status = property(lambda self: gpsdshm.shm.get_status(self.shm) != 0)
    dev = device = property(lambda self: gpsdshm.shm.get_dev(self.shm))
    skyview_time = property(lambda self: gpsdshm.shm.get_skyview_time(self.shm))
    satellites_visible = property(lambda self: gpsdshm.shm.get_satellites_visible(self.shm))
    
    
    
