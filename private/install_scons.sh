#!/bin/sh -x

# Install scons from source. Building gpsd requires
# a newer version of scons.
#
# Markus Juenemann, 03-Feb-2016


which hg || sudo apt-get -y install mercurial 

cd ~
[ -d scons ] || hg clone https://bitbucket.org/scons/scons

cd scons 
python bootstrap.py build/scons
cd build/scons
sudo python setup.py install
