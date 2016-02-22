

all: help

help:
	@echo "make build           - Build all Docker image"
	@echo "make test            - Start all Docker images and run tests"
	@echo "make clean_failed    - Delete failed Docker containers"
	@echo "make clean_dangling  - Delete dangling Docker images"

#build: build_3.0 \
#       build_3.1 \
#       build_3.2 \
#       build_3.3 \
#       build_3.4 \
#       build_3.5 \
#       build_3.6 \
#       build_3.7 \
#       build_3.8 \
#       build_3.9 \
#       build_3.10 \
#       build_3.11 \
#       build_3.12 \
#       build_3.13 \
#       build_3.14 \
#       build_3.15 \
#       build_3.16

test: test_3.0 \
      test_3.1 \
      test_3.2 \
      test_3.3 \
      test_3.4 \
      test_3.5 \
      test_3.6 \
      test_3.7 \
      test_3.8 \
      test_3.9 \
      test_3.10 \
      test_3.11 \
      test_3.12 \
      test_3.13 \
      test_3.14 \
      test_3.15 \
      test_3.16

#build_3.%: Dockerfile
#	docker build --build-arg RELEASE=release-$(subst build_,,$@) --build-arg http_proxy=$(http_proxy) \
#	             --build-arg https_proxy=$(https_proxy) -t mjuenema/pythons-gpsd-release-$(subst build_,,$@)-gpsdshm .
build: Dockerfile
	docker build --build-arg http_proxy=$(http_proxy) \
	             --build-arg https_proxy=$(https_proxy) \
                     -t mjuenema/pythons-gpsd-gpsdshm .

#test: build
#	docker run -it --rm -e "BRANCH=develop" -e "RELEASE=3.15" \
#		-v `pwd`/workdir/cache:/home/developer/.cache \
#		-v `pwd`/workdir/ccache:/home/developer/.ccache \
#		-v `pwd`/workdir/tox:/home/developer/python-gpsdshm/.tox \
#		-v `pwd`/../..:/home/developer/src \
#		mjuenema/pythons-gpsd-gpsdshm /run_tests.sh

test_3.%: build
	docker run -it --rm -e "BRANCH=`git branch | awk '$$1 ~ /\*/ { print $$2 }'`" -e "RELEASE=$(subst test_,,$@)" \
		-v `pwd`/workdir/cache:/home/developer/.cache \
		-v `pwd`/workdir/ccache:/home/developer/.ccache \
		-v `pwd`/../..:/home/developer/src \
		mjuenema/pythons-gpsd-gpsdshm /run_tests.sh
	

.PHONY: Dockerfile
Dockerfile:
       

clean_dangling:
	[ "`docker images -q -f dangling=true`" != "" ] && \
		docker rmi `docker images -q -f dangling=true`

clean_failed:
	[ "`docker ps -a | egrep 'Exited \([^0]' | cut -c 1-16`" != "" ] && \
		docker rm `docker ps -a | egrep 'Exited \([^0]' | cut -c 1-16`	
	
