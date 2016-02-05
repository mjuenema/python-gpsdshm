

all: help

help:
	@echo "make build            - Build all Docker images"
	@echo "make clean_failed     - Delete failed Docker containers"
	@echo "make clean_dangling   - Delete dangling Docker images"

build: 3.0 3.1 3.2 3.3 3.4 3.5 3.6 3.7 3.8 3.9 3.10 3.11 3.12 3.13 3.14 3.15 3.16

3.%: Dockerfile
	docker build --build-arg RELEASE=release-$@ --build-arg http_proxy=$(http_proxy) \
	             --build-arg https_proxy=$(https_proxy) -t mjuenema/pythons-gpsd-release-$@-gpsdshm .

#3.1: Dockerfile
#	docker build --build-arg RELEASE=release-$@ -t mjuenema/pythons-gpsd-release-$@-gpsdshm .
#
#3.2: Dockerfile
#	docker build --build-arg RELEASE=release-$@ -t mjuenema/pythons-gpsd-release-$@-gpsdshm .
#
#3.3: Dockerfile
#	docker build --build-arg RELEASE=release-$@ -t mjuenema/pythons-gpsd-release-$@-gpsdshm .
#
#3.4: Dockerfile
#	docker build --build-arg RELEASE=release-$@ -t mjuenema/pythons-gpsd-release-$@-gpsdshm .
#
#3.5: Dockerfile
#	docker build --build-arg RELEASE=release-$@ -t mjuenema/pythons-gpsd-release-$@-gpsdshm .
#
#3.6: Dockerfile
#	docker build --build-arg RELEASE=release-$@ -t mjuenema/pythons-gpsd-release-$@-gpsdshm .
#
#3.7: Dockerfile
#	docker build --build-arg RELEASE=release-$@ -t mjuenema/pythons-gpsd-release-$@-gpsdshm .
#
#3.8: Dockerfile
#	docker build --build-arg RELEASE=release-$@ -t mjuenema/pythons-gpsd-release-$@-gpsdshm .
#
#3.9: Dockerfile
#	docker build --build-arg RELEASE=release-$@ -t mjuenema/pythons-gpsd-release-$@-gpsdshm .
#
#3.10: Dockerfile
#	docker build --build-arg RELEASE=release-$@ -t mjuenema/pythons-gpsd-release-$@-gpsdshm .
#
#3.10: Dockerfile
#	docker build --build-arg RELEASE=release-$@ -t mjuenema/pythons-gpsd-release-$@-gpsdshm .
#
#3.10: Dockerfile
#	docker build --build-arg RELEASE=release-$@ -t mjuenema/pythons-gpsd-release-$@-gpsdshm .
#
#3.10: Dockerfile
#	docker build --build-arg RELEASE=release-$@ -t mjuenema/pythons-gpsd-release-$@-gpsdshm .
#
#3.10: Dockerfile
#	docker build --build-arg RELEASE=release-$@ -t mjuenema/pythons-gpsd-release-$@-gpsdshm .
#
#3.10: Dockerfile
#	docker build --build-arg RELEASE=release-$@ -t mjuenema/pythons-gpsd-release-$@-gpsdshm .
#
#3.10: Dockerfile
#	docker build --build-arg RELEASE=release-$@ -t mjuenema/pythons-gpsd-release-$@-gpsdshm .



.PHONY: Dockerfile
Dockerfile:
       

clean_dangling:
	[ "`docker images -q -f dangling=true`" != "" ] && \
		docker rmi `docker images -q -f dangling=true`

clean_failed:
	[ "`docker ps -q -a -f exited=1 -f exited=2 -f exited=137`" != "" ] && \
		docker rm `docker ps -q -a -f exited=1 -f exited=2 -f exited=137`
	
