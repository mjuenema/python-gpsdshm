# Temporary, until meregd into ../setup.py
rm -fv shm.o shm.py shm_wrap.c shm_wrap.o
swig -python shm.i
gcc -O2 -fPIC -c shm.c 
gcc -O2 -fPIC -c shm_wrap.c `python-config --includes` 
gcc -shared shm.o shm_wrap.o -o _shm.so `/usr/bin/python-config --ldflags`
