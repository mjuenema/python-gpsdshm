# Temporary, until meregd into ../setup.py
gcc -O2 -fPIC -c shm.c 
gcc -O2 -fPIC -c shm_wrap.c `python-config --includes` 
gcc -shared shm.o shm_wrap.o -o _shm.so `/usr/bin/python-config --ldflags`
