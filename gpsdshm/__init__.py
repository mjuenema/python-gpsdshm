"""
Python interface to GPSd Shared Memory.

"""

import gpsdshm.shm

MAXCHANNELS = gpsdshm.shm.MAXCHANNELS
MAXUSERDEVS = gpsdshm.shm.MAXUSERDEVS
GPSD_API_MAJOR_VERSION = gpsdshm.shm.GPSD_API_MAJOR_VERSION
GPSD_API_MINOR_VERSION = gpsdshm.shm.GPSD_API_MINOR_VERSION
STATUS_NO_FIX = gpsdshm.shm.STATUS_NO_FIX
STATUS_FIX = gpsdshm.shm.STATUS_FIX
STATUS_DGPS_FIX = gpsdshm.shm.STATUS_DGPS_FIX
SEEN_GPS = gpsdshm.shm.SEEN_GPS
SEEN_RTCM2 = gpsdshm.shm.SEEN_RTCM2
SEEN_RTCM3 = gpsdshm.shm.SEEN_RTCM3
SEEN_AIS = gpsdshm.shm.SEEN_AIS

_error = gpsdshm.shm.cvar._error


class Fix(object):
    """Class representing ``gpsd/gps.h:gps_fix_t``."""

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
    """Class representing ``gpsd/gps.h:dop_t``."""

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
    """Class representing ``gpsd/gps.h:satellite_t``."""
    def __init__(self, ss, used, prn, elevation, azimuth):
        self.ss = self.snr = ss
        self.used = used and True
        self.prn = self.PRN = prn
        self.elevation = elevation
        self.azimuth = azimuth


class Satellites(object):
    """List of `GpsdShmSatellite` instances.
  
       This list will always be ``gpsdshm.MAXCHANNELS`` long, regardless
       of how many satellites are in view. The ``Satellite.prn`` attribute
       will be zero for unused channels.
    """

    def __init__(self, shm):
        self.shm = shm

    def __getitem__(self, index):

        if index > gpsdshm.MAXCHANNELS - 1:
            raise IndexError

        ss = gpsdshm.shm.get_satellite_ss(self.shm, index)
        prn = gpsdshm.shm.get_satellite_prn(self.shm, index)
        used = gpsdshm.shm.get_satellite_used(self.shm, prn) is True
        elevation = gpsdshm.shm.get_satellite_elevation(self.shm, index)
        azimuth = gpsdshm.shm.get_satellite_azimuth(self.shm, index)

        return Satellite(ss, used, prn, elevation, azimuth)


class Device(object):
    """Class representing ``gpsd/gps.h:devconfig_t``."""
    def __init__(self, path, flags, driver, subtype, activated,
                 baudrate, stopbits, parity, cycle, mincycle,
                 driver_mode):
        self.path = path
        self.flags = flags
        self.driver = driver
        self.subtype = subtype
        self.activated = activated
        self.baudrate = baudrate
        self.stopbits = stopbits
        self.parity = parity
        self.cycle = cycle
        self.mincycle = mincycle
        self.driver_mode = driver_mode


class Devices(object):
    """List of `GpsdShmDevice` (singular) instances.
    
       With gpsd 3.12 and later this is a list of devices, e.g. ``Device``
       instances. Earlier versions of gpsd embedded this into a C union
       and ``Devices`` will only provide information about the device
       that shipped the last update.
       
       This list will always be ``gpsdshm.MAXDEVICES`` long, regardless
       of how many satellites are in view.
    """

    def __init__(self, shm):
        self.shm = shm

    def __getitem__(self, index):
        
        if index > gpsdshm.MAXUSERDEVS - 1:
            raise IndexError

        path = gpsdshm.shm.get_device_path(self.shm, index)
        flags = gpsdshm.shm.get_device_flags(self.shm, index)
        driver = gpsdshm.shm.get_device_driver(self.shm, index)
        subtype = gpsdshm.shm.get_device_subtype(self.shm, index)
        activated, = gpsdshm.shm.get_device_activated(self.shm, index)
        baudrate = gpsdshm.shm.get_device_baudrate(self.shm, index)
        stopbits = gpsdshm.shm.get_device_stopbits(self.shm, index)
        parity = gpsdshm.shm.get_device_parity(self.shm, index)
        cycle = gpsdshm.shm.get_device_cycle(self.shm, index)
        mincycle = gpsdshm.shm.get_device_mincycle(self.shm, index)
        driver_mode = gpsdshm.shm.get_device_driver_mode(self.shm, index)


class Shm(object):
    """GPSd Shared Memory."""

    def __init__(self):

        self.shm = gpsdshm.shm.shm_get()
        if self.shm is None:
            raise OSError('GPSd shared memory error: %s' % (gpsdshm._error))

        self.fix = Fix(self.shm)
        self.dop = Dop(self.shm)
        self.satellites = Satellites(self.shm)
        self.devices = Devices(self.shm)


    set = property(lambda self: gpsdshm.shm.get_set(self.shm))
    online = property(lambda self: gpsdshm.shm.get_online(self.shm))
    fd = property(lambda self: gpsdshm.shm.get_fd(self.shm))
    status = property(lambda self: gpsdshm.shm.get_status(self.shm))
    dev = device = property(lambda self: gpsdshm.shm.get_dev(self.shm))
    skyview_time = property(lambda self: gpsdshm.shm.get_skyview_time(self.shm))
    satellites_visible = property(lambda self: gpsdshm.shm.get_satellites_visible(self.shm))
    ndevices = property(lambda self: gpsdshm.shm.get_ndevices(self.shm))
