%module "shm"

%{
#define SWIG_FILE_WITH_INIT
#include <gps.h>
%}

%include <gps.h>

