#!/bin/sh


# Verify that this script has been executed from
# it's own directory
#
if [ ! -d ../../gpsdshm/shm.i ]; then
    echo "$0 must be executed from within its directory"
    exit 1
fi


# Work inside a temporary directory
#
tmpdir=`mktemp -d`
cd $tmpdir


# Clone GPSD Git repository and check out HEAD.
#
cd $tmpdir
git clone git://git.savannah.nongnu.org/gpsd.git
gpsd_dir=$tmpdir/gpsd


# Create the gpsdshm sub-directory if it does not exist
#
[ -d $gpsd_dir/gpsdshm ] || mkdir $gpsd_dir/gpsdshm


# Copy whatever's needed into that directory
#
cp -r AUTHORS.rst \
      gpsdshm \
      HISTORY.rst \
      LICENSE \
      MANIFEST.in \
      README.rst \
      requirements.txt \
      setup.cfg \
      setup.py \
      test_requirements.txt \
      $gpsd_dir/gpsdshm/


# Create the patch
#
#TODO
