%module "shm"

%{
#include "shm.h"
typedef double timestamp_t;
%}

%include "shm.h"
%constant MAXCHANNELS = MAXCHANNELS;
typedef double timestamp_t;
