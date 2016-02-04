#!/bin/sh -x

# Install expect and expect-lite on RaspberryPi
#
# Markus Juenemann, 03-Feb-2016

VERSION=4.9.0

install_el() {
    cd /tmp
    rm -fv expect-lite_$VERSION.tar.gz
    curl -L -o expect-lite_$VERSION.tar.gz \
         http://sourceforge.net/projects/expect-lite/files/expect-lite/expect-lite_$VERSION/expect-lite_$VERSION.tar.gz/download
    tar xvfz expect-lite_$VERSION.tar.gz
    cd expect-lite.proj
    sudo ./install.sh
}

which expect || sudo apt-get -y install expect expect-dev
which expect-lite || install_el
