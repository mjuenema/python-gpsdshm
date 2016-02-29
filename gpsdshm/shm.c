

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <errno.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <gps.h>

#include "shm.h"

#if GPSD_API_MAJOR_VERSION < 5
#error "gpsd versions earlier than 2.9.6 are not supported"
#endif

/* The following definitions are in gpsd.h
 * of the gpsd sources but the header file 
 * is not installed through 'scons install'.
 */
#define GPSD_SHM_KEY        0x47505344
struct shmexport_t
{
    int bookend1;
    struct gps_data_t gpsdata;
    int bookend2;
};


char *_error = NULL;


struct shmexport_t *shm_get() {
    int shmid;
    void *shm;
    
    _error = NULL;

    // Try to create a new shared memory segment, in case gpsd has not started yet.
    shmid = shmget((key_t)(GPSD_SHM_KEY), sizeof(struct shmexport_t), IPC_CREAT | IPC_EXCL | 0666);
    if (shmid < 0)
    {
        // Try to open an existing 
        shmid = shmget((key_t)(GPSD_SHM_KEY), 0, 0666);
        if (shmid < 0) {
            _error = strerror(errno);
            return NULL;
        }
    }

    shm = (struct shmexport_t *)shmat(shmid, NULL, SHM_RDONLY);
    if (shm == (void *)(-1)) {
        _error = strerror(errno);
        return NULL;
    }

    return shm;
}


/* gps_fix_t */
timestamp_t get_fix_time(struct shmexport_t *shm) {
    return shm->gpsdata.fix.time;
}

int get_fix_mode(struct shmexport_t *shm) {
    return shm->gpsdata.fix.mode;
}

double get_fix_ept(struct shmexport_t *shm) {
    return shm->gpsdata.fix.ept;
}

double get_fix_latitude(struct shmexport_t *shm) {
    return shm->gpsdata.fix.latitude;
}

double get_fix_epy(struct shmexport_t *shm) {
    return shm->gpsdata.fix.epy;
}

double get_fix_longitude(struct shmexport_t *shm) {
    return shm->gpsdata.fix.longitude;
}

double get_fix_epx(struct shmexport_t *shm) {
    return shm->gpsdata.fix.epx;
}

double get_fix_altitude(struct shmexport_t *shm) {
    return shm->gpsdata.fix.altitude;
}

double get_fix_epv(struct shmexport_t *shm) {
    return shm->gpsdata.fix.epv;
}

double get_fix_track(struct shmexport_t *shm) {
    return shm->gpsdata.fix.track;
}

double get_fix_epd(struct shmexport_t *shm) {
    return shm->gpsdata.fix.epd;
}

double get_fix_speed(struct shmexport_t *shm) {
    return shm->gpsdata.fix.speed;
}

double get_fix_eps(struct shmexport_t *shm) {
    return shm->gpsdata.fix.eps;
}

double get_fix_climb(struct shmexport_t *shm) {
    return shm->gpsdata.fix.climb;
}

double get_fix_epc(struct shmexport_t *shm) {
    return shm->gpsdata.fix.epc;
}


/* dop_t */
double get_dop_xdop(struct shmexport_t *shm) {
    return shm->gpsdata.dop.xdop;
}

double get_dop_ydop(struct shmexport_t *shm) {
    return shm->gpsdata.dop.ydop;
}

double get_dop_pdop(struct shmexport_t *shm) {
    return shm->gpsdata.dop.pdop;
}

double get_dop_hdop(struct shmexport_t *shm) {
    return shm->gpsdata.dop.hdop;
}

double get_dop_vdop(struct shmexport_t *shm) {
    return shm->gpsdata.dop.vdop;
}

double get_dop_tdop(struct shmexport_t *shm) {
    return shm->gpsdata.dop.tdop;
}

double get_dop_gdop(struct shmexport_t *shm) {
    return shm->gpsdata.dop.gdop;
}


/* gps_data_t */
//gps_mask_t get_set(struct shmexport_t *shm) {
//    return shm->gpsdata.set;
//}

timestamp_t get_online(struct shmexport_t *shm) {
    return shm->gpsdata.online;
}

int get_status(struct shmexport_t *shm) {
    return shm->gpsdata.status;
}

timestamp_t get_skyview_time(struct shmexport_t *shm) {
    return shm->gpsdata.skyview_time;
}

int get_satellites_visible(struct shmexport_t *shm) {
    return shm->gpsdata.satellites_visible;
}


/* satellite_t */
double get_satellite_ss(struct shmexport_t *shm, unsigned int index)  {
#if GPSD_API_MAJOR_VERSION == 5
    return shm->gpsdata.ss[index];
#endif
#if GPSD_API_MAJOR_VERSION == 6
    return shm->gpsdata.skyview[index].ss;
#endif
}

#if GPSD_API_MAJOR_VERSION == 5
int get_satellite_used(struct shmexport_t *shm, unsigned int prn)  {
    int i;
    for (i = 0; i < shm->gpsdata.satellites_used; i++) {
        //printf("%d ", shm->gpsdata.used[i]);
        if(shm->gpsdata.used[i] == prn) {
            //printf("\n"); 
            return 1;
        }
    }
    //printf("\n"); 
    return 0;
}
#endif

#if GPSD_API_MAJOR_VERSION == 6
int get_satellite_used(struct shmexport_t *shm, unsigned int index)  {
    return shm->gpsdata.skyview[index].used;
}
#endif


int get_satellite_prn(struct shmexport_t *shm, unsigned int index)  {
#if GPSD_API_MAJOR_VERSION == 5
    return shm->gpsdata.PRN[index];
#endif
#if GPSD_API_MAJOR_VERSION == 6
    return shm->gpsdata.skyview[index].PRN;
#endif
}

int get_satellite_elevation(struct shmexport_t *shm, unsigned int index)  {
#if GPSD_API_MAJOR_VERSION == 5
    return shm->gpsdata.elevation[index];
#endif
#if GPSD_API_MAJOR_VERSION == 6
    return shm->gpsdata.skyview[index].elevation;
#endif
}

int get_satellite_azimuth(struct shmexport_t *shm, unsigned int index)  {
#if GPSD_API_MAJOR_VERSION == 5
    return shm->gpsdata.azimuth[index];
#endif
#if GPSD_API_MAJOR_VERSION == 6
    return shm->gpsdata.skyview[index].azimuth;
#endif
}


// Devices
//
// Index checks are done in the calling Python code!
//
int get_ndevices(struct shmexport_t *shm) {
#if GPSD_API_MAJOR_VERSION == 5
    return 1;
#endif
#if GPSD_API_MAJOR_VERSION == 6
    return shm->gpsdata.devices.ndevices;
#endif
}

char *get_device_path(struct shmexport_t *shm, unsigned int index) {
#if GPSD_API_MAJOR_VERSION == 5
    return shm->gpsdata.dev.path;
#endif
#if GPSD_API_MAJOR_VERSION == 6
    return shm->gpsdata.devices.list[index].path;
#endif
} 

int get_device_flags(struct shmexport_t *shm, unsigned int index) {
#if GPSD_API_MAJOR_VERSION == 5
    return shm->gpsdata.dev.flags;
#endif
#if GPSD_API_MAJOR_VERSION == 6
    return shm->gpsdata.devices.list[index].flags;
#endif
} 

char *get_device_driver(struct shmexport_t *shm, unsigned int index) {
#if GPSD_API_MAJOR_VERSION == 5
    return shm->gpsdata.dev.driver;
#endif
#if GPSD_API_MAJOR_VERSION == 6
    return shm->gpsdata.devices.list[index].driver;
#endif
} 

char *get_device_subtype(struct shmexport_t *shm, unsigned int index) {
#if GPSD_API_MAJOR_VERSION == 5
    return shm->gpsdata.dev.subtype;
#endif
#if GPSD_API_MAJOR_VERSION == 6
    return shm->gpsdata.devices.list[index].subtype;
#endif
} 

double get_device_activated(struct shmexport_t *shm, unsigned int index) {
#if GPSD_API_MAJOR_VERSION == 5
    return shm->gpsdata.dev.activated;
#endif
#if GPSD_API_MAJOR_VERSION == 6
    return shm->gpsdata.devices.list[index].activated;
#endif
} 

unsigned int get_device_baudrate(struct shmexport_t *shm, unsigned int index) {
#if GPSD_API_MAJOR_VERSION == 5
    return shm->gpsdata.dev.baudrate;
#endif
#if GPSD_API_MAJOR_VERSION == 6
    return shm->gpsdata.devices.list[index].baudrate;
#endif
} 

unsigned int get_device_stopbits(struct shmexport_t *shm, unsigned int index) {
#if GPSD_API_MAJOR_VERSION == 5
    return shm->gpsdata.dev.stopbits;
#endif
#if GPSD_API_MAJOR_VERSION == 6
    return shm->gpsdata.devices.list[index].stopbits;
#endif
} 

char *get_device_parity(struct shmexport_t *shm, unsigned int index) {
#if GPSD_API_MAJOR_VERSION == 5
    return shm->gpsdata.dev.parity;
#endif
#if GPSD_API_MAJOR_VERSION == 6
    return shm->gpsdata.devices.list[index].parity;
#endif
} 

double get_device_cycle(struct shmexport_t *shm, unsigned int index) {
#if GPSD_API_MAJOR_VERSION == 5
    return shm->gpsdata.dev.cycle;
#endif
#if GPSD_API_MAJOR_VERSION == 6
    return shm->gpsdata.devices.list[index].cycle;
#endif
} 

double get_device_mincycle(struct shmexport_t *shm, unsigned int index) {
#if GPSD_API_MAJOR_VERSION == 5
    return shm->gpsdata.dev.mincycle;
#endif
#if GPSD_API_MAJOR_VERSION == 6
    return shm->gpsdata.devices.list[index].mincycle;
#endif
} 

int get_device_driver_mode(struct shmexport_t *shm, unsigned int index) {
#if GPSD_API_MAJOR_VERSION == 5
    return shm->gpsdata.dev.driver_mode;
#endif
#if GPSD_API_MAJOR_VERSION == 6
    return shm->gpsdata.devices.list[index].driver_mode;
#endif
} 
