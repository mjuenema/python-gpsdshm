#
# Python versions and specific gpsd version
# for testing python-gpsdshm.
#
# Markus Juenemann, 04-Feb-2016

FROM mjuenema/pythons
MAINTAINER Markus Juenemann <markus@juenemann.net>
USER root
ARG RELEASE

# Yum proxy
#
RUN [ "$http_proxy" == "" ] || echo "proxy=$http_proxy" >> /etc/yum.conf
RUN yum clean all

# Install scons
#
RUN pip2.7 install SCons

RUN yum -y install python-devel chrpath automake pcre-devel bison byacc gcc-c++

RUN cd /tmp && \
    git clone https://github.com/swig/swig.git && \
    cd swig && \
    git checkout rel-3.0.8 && \
    sh autogen.sh && \
    ./configure && \
    make && \
    make install

RUN cd /tmp && git clone https://git.savannah.gnu.org/r/gpsd.git && \
    cd gpsd && \
    git checkout $RELEASE && \
    python2.7 /usr/local/bin/scons -c && \
    python2.7 /usr/local/bin/scons shm_export=True python=False leapfetch=False manbuild=False && \
    python2.7 /usr/local/bin/scons install

RUN cd /tmp && git clone https://github.com/mjuenema/python-gpsdshm.git

RUN echo $RELEASE > /gpsd.release

VOLUME workdir /workdir

CMD /bin/bash

# Undo yum proxy
#
RUN [ "$http_proxy" == "" ] || sed --in-place 's/^proxy=http.*$//g' /etc/yum.conf
    
