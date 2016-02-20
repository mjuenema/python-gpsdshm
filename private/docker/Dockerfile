#
# Python versions and specific gpsd version
# for testing python-gpsdshm.
#
# Markus Juenemann, 04-Feb-2016

FROM mjuenema/pythons
MAINTAINER Markus Juenemann <markus@juenemann.net>
USER root

# Yum proxy
#
RUN [ "$http_proxy" == "" ] || echo "proxy=$http_proxy" >> /etc/yum.conf
RUN yum clean all

# Install scons
#
RUN pip2.7 install SCons

RUN yum -y install python-devel chrpath automake pcre-devel \
           bison byacc gcc-c++ libxslt xmlto

RUN git clone http://git.savannah.gnu.org/r/gpsd.git

RUN cd ~/gpsd && \
    git checkout release-3.16 && \
    python2.7 /usr/local/bin/scons -c && \
    python2.7 /usr/local/bin/scons shm_export=yes python=yes leapfetch=no prefix=/opt/gpsd/3.16 && \
    python2.7 /usr/local/bin/scons install

RUN cd ~/gpsd && \
    git checkout release-3.15 && \
    python2.7 /usr/local/bin/scons -c && \
    python2.7 /usr/local/bin/scons shm_export=yes python=yes leapfetch=no prefix=/opt/gpsd/3.15 && \
    python2.7 /usr/local/bin/scons install

RUN cd ~/gpsd && \
    git checkout release-3.14 && \
    python2.7 /usr/local/bin/scons -c && \
    python2.7 /usr/local/bin/scons shm_export=yes python=yes leapfetch=no prefix=/opt/gpsd/3.14 && \
    python2.7 /usr/local/bin/scons install

RUN cd ~/gpsd && \
    git checkout release-3.13 && \
    python2.7 /usr/local/bin/scons -c && \
    python2.7 /usr/local/bin/scons shm_export=yes python=yes leapfetch=no prefix=/opt/gpsd/3.13 && \
    python2.7 /usr/local/bin/scons install

RUN cd ~ && \
    git clone https://github.com/mjuenema/python-gpsdshm.git

RUN cd ~ && \
    git clone https://github.com/swig/swig.git && \
    cd swig && \
    git checkout rel-3.0.8 && \
    sh autogen.sh && \
    ./configure && \
    make && \
    make install

VOLUME workdir /workdir

COPY tests.run /run_tests.sh

CMD /bin/bash

# Undo yum proxy
#
RUN [ "$http_proxy" == "" ] || sed --in-place 's/^proxy=http.*$//g' /etc/yum.conf
    
