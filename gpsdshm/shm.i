%module "shm"

%{
#include "shm.h"
typedef double timestamp_t;
%}

%include "shm.h"
%constant int MAXCHANNELS = MAXCHANNELS;
%constant int GPSD_API_MAJOR_VERSION = GPSD_API_MAJOR_VERSION;
%constant int GPSD_API_MINOR_VERSION = GPSD_API_MINOR_VERSION;
%constant int STATUS_NO_FIX = STATUS_NO_FIX;
%constant int STATUS_FIX = STATUS_FIX;
%constant int STATUS_DGPS_FIX = STATUS_DGPS_FIX;
typedef double timestamp_t;
