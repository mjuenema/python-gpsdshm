#
# Python versions and specific gpsd version
# for testing python-gpsdshm.
#
# Markus Juenemann, 04-Feb-2016

FROM mjuenema/pythons
MAINTAINER Markus Juenemann <markus@juenemann.net>
USER root
ARG RELEASE

RUN cd / ; \
    wget http://downloads.sourceforge.net/scons/scons-2.4.1.tar.gz ; \
    tar xvfz scons-2.4.1.tar.gz ; \
    cd scons-2.4.1 ; \
    python2.7 bootstrap.py build/scons; \
    cd build/scons; \
    python2.7 setup.py install

RUN yum -y install python-devel chrpath swig

RUN cd / ; git clone http://git.savannah.gnu.org/r/gpsd.git 

RUN cd /gpsd ; \
    git checkout $RELEASE ; \
    python2.7 /usr/local/bin/scons -c ; \
    python2.7 /usr/local/bin/scons shm_export=True python=False leapfetch=False manbuild=False ; \
    python2.7 /usr/local/bin/scons install

RUN cd / ; git clone https://github.com/mjuenema/python-gpsdshm.git

RUN echo $RELEASE > /gpsd.release

VOLUME results /results

CMD /bin/bash
    
