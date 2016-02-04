
#include "gps.h"

/* shared memory */
struct shmexport_t *shm_get();

/* gps_fix_t */
timestamp_t get_fix_time(struct shmexport_t *shm);
int get_fix_mode(struct shmexport_t *shm);
double get_fix_ept(struct shmexport_t *shm);
double get_fix_latitude(struct shmexport_t *shm);
double get_fix_epy(struct shmexport_t *shm);
double get_fix_longitude(struct shmexport_t *shm);
double get_fix_epx(struct shmexport_t *shm);
double get_fix_altitude(struct shmexport_t *shm);
double get_fix_epv(struct shmexport_t *shm);
double get_fix_track(struct shmexport_t *shm);
double get_fix_epd(struct shmexport_t *shm);
double get_fix_speed(struct shmexport_t *shm);
double get_fix_eps(struct shmexport_t *shm);
double get_fix_climb(struct shmexport_t *shm);
double get_fix_epc(struct shmexport_t *shm);

/* dop_t */
double get_dop_xdop(struct shmexport_t *shm);
double get_dop_ydop(struct shmexport_t *shm);
double get_dop_pdop(struct shmexport_t *shm);
double get_dop_hdop(struct shmexport_t *shm);
double get_dop_vdop(struct shmexport_t *shm);
double get_dop_tdop(struct shmexport_t *shm);
double get_dop_gdop(struct shmexport_t *shm);

/* gps_data_t */
//gps_mask_t get_set(struct shmexport_t *shm);
timestamp_t get_online(struct shmexport_t *shm);
int get_status(struct shmexport_t *shm);
timestamp_t get_skyview_time(struct shmexport_t *shm);
int get_satellites_visible(struct shmexport_t *shm);

/* gps_satellite_t */
double get_satellite_ss(struct shmexport_t *shm, unsigned int index);
int get_satellite_used(struct shmexport_t *shm, unsigned int index);
int get_satellite_prn(struct shmexport_t *shm, unsigned int index);
int get_satellite_elevation(struct shmexport_t *shm, unsigned int index);
int get_satellite_azimuth(struct shmexport_t *shm, unsigned int index);
