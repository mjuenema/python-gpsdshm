

all: help

help:
	@echo "make -k build         - Build all Docker images"
	@echo "make -k test          - Start all Docker images and run tests"
	@echo "make clean_failed     - Delete failed Docker containers"
	@echo "make clean_dangling   - Delete dangling Docker images"

build: build_3.0 \
       build_3.1 \
       build_3.2 \
       build_3.3 \
       build_3.4 \
       build_3.5 \
       build_3.6 \
       build_3.7 \
       build_3.8 \
       build_3.9 \
       build_3.10 \
       build_3.11 \
       build_3.12 \
       build_3.13 \
       build_3.14 \
       build_3.15 \
       build_3.16

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

build_3.%: Dockerfile
	docker build --build-arg RELEASE=release-$(subst build_,,$@) --build-arg http_proxy=$(http_proxy) \
	             --build-arg https_proxy=$(https_proxy) -t mjuenema/pythons-gpsd-release-$(subst build_,,$@)-gpsdshm .

test_3.%: build_3.%
	docker run --rm -v `pwd`/workdir:/workdir mjuenema/pythons-gpsd-release-$(subst test_,,$@)-gpsdshm


.PHONY: Dockerfile
Dockerfile:
       

clean_dangling:
	[ "`docker images -q -f dangling=true`" != "" ] && \
		docker rmi `docker images -q -f dangling=true`

clean_failed:
	[ "`docker ps -q -a -f exited=1 -f exited=2 -f exited=137`" != "" ] && \
		docker rm `docker ps -q -a -f exited=1 -f exited=2 -f exited=137`
	
