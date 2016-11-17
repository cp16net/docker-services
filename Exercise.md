# Goal

Make a build deployment of the auth and data api services on /api/auth and /api/data repectively.

# Requirements

* [docker](https://docs.docker.com/engine/installation/) >=1.10.0
* [docker-compose](https://docs.docker.com/compose/install/) >=1.6.0
* [make](https://www.gnu.org/software/make/) installed
* [jq](https://stedolan.github.io/jq/) installed in $PATH (used with tests)

# Getting started

    make            # list the options to run make with
    make up         # brings up the env
    make ping       # tests the health endpoints of services
    make bootstrap  # bootstraps database with a user
    make test       # runs a simple test suite against env
    make down       # tears down the env


# Tooling

* Docker because its simple to setup and portable.
* Docker compose allows for common docker specified files.
* Nomad maybe a good way to manage a production type of deployment via blue-green/rolling upgrades.

# Overview
* setup python application in image
  * custom dockerfile to build the application inside the container image

* setup mongodb image
  * (TODO) need to generate a random user and password (no need to have it known)
  * (TODO) make a custom entry point script to configure docker and start it up

* nginx for proxy routing to applications
  * need a custom confuration to handle the application paths

* docker-compose file to tie everything together

* helpful to have a makefile that handles some of the actions


# Running with Docker Compose

    docker-compose build --pull
    docker-compose up -d
    docker-compose down --rmi all

