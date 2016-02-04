#!/bin/sh -x

# Install all 3.x releases of gpsd.
#
# Markus Juenemann, 03-Feb-2016

BASEDIR=/opt/gpsd

[ -d $PREFIX ] || mkdir -vp $PREFIX

cd ~
[ -d gpsd ] || git clone git://git.savannah.nongnu.org/gpsd.git
cd gpsd
git pull origin master


cat <<EOF>> scons-option-cache
ashtech = False
earthmate = False
evermore = False
fv18 = False
geostar = False
itrax = False
mtk3301 = False
oncore = False
sirf = False
tnt = False
tripmate = False
ubx = False
pps = False
usb = False
fury = False
nmea = True
tsip = False
aivdm = False
oceanserver = False
rtcm104v2 = False
rtcm104v3 = False
bluez = False
ipv6 = False
oldstyle = False
libgpsmm = False
libQgpsmm = False
ncurses = False
python = False
chrpath = False
strip = False
squelch = False
reconfigure = True
manbuild = False
shared = True
shm_export = True
EOF


releases=`git tag | grep release-3 | sort`
 
for release in $releases; do
    if [ ! -d $BASEDIR/$release ]; then
        scons -c
        scons prefix=$BASEDIR/$release
        sudo scons install
    fi
done
