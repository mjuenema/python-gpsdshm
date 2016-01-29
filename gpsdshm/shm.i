%module "shm"

%{
#include "shm.h"
typedef double timestamp_t;
%}

%include "shm.h"
typedef double timestamp_t;
