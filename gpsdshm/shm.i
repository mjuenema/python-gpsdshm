%module "shm"

%{
#include "shm.h"
typedef double timestamp_t;
%}

%include "shm.h"
%constant int MAXCHANNELS = MAXCHANNELS;
%constant int GPSD_API_MAJOR_VERSION = GPSD_API_MAJOR_VERSION;
%constant int GPSD_API_MINOR_VERSION = GPSD_API_MINOR_VERSION;
typedef double timestamp_t;
