%module "shm"

%{
#include "shm.h"
typedef double timestamp_t;
typedef unsigned long long int gps_mask_t;
%}

%include "shm.h"
typedef double timestamp_t;
typedef unsigned long long gps_mask_t;
