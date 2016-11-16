# Goal
Make a build deployment of the auth and data api services on /api/auth and /api/data repectively.

# Tooling
* Docker because its simple to setup and portable.
* Docker compose allows for common docker specified files.
* Nomad maybe a good way to manage a production type of deployment via blue-green/rolling upgrades.

# TODO
* setup python application in image
** custom dockerfile to build the application inside the container image

* setup mongodb image with a random user/pass setup
** make a custom entry point script to configure docker and start it up
** need to generate a random user and password (no need to have it known)

* setup haproxy to allow routing and scale
** route for /api/auth
** route for /api/data
** use /api/auth/health and /api/data/health as a health check of service

* docker-compose file to tie everything together
** use a private network for app to db
** use a private network for app to haproxy
** use a public network for haproxy to the main endpoint

* maybe helpful to have a makefile that handles some of the actions


# Manual setup

## Simple

### building services

    docker build -t exercise:auth ./auth_service
    docker build -t exercise:data ./data_service
    docker build -t exercise:nginx ./nginx

### running services

    docker run -d --name mongo mongo
    docker run -d --name authservice -e MONGODB="mongodb://mongo:21017/" --link mongo -p 8080:5000 exercise:auth
    docker run -d --name dataservice -e MONGODB="mongodb://mongo:21017/" --link mongo -p 8081:5000 exercise:data

## running with proxy

    docker run -d --name mongo mongo
    docker run -d --name authservice -e MONGODB="mongodb://mongo:21017/" --link mongo exercise:auth
    docker run -d --name dataservice -e MONGODB="mongodb://mongo:21017/" --link mongo exercise:data
    docker run -d --name nginx --link authservice --link dataservice -p 80:80 exercise:nginx

## Mongo With Auth

    docker run -d -e MONGODB_USER="test" -e MONGODB_DATABASE="auth" -e MONGODB_PASS="pass" tutum/mongodb
    docker run -d --name authervice -e MONGODB="mongodb://test:pass@mongo:21017/" --link modest_visvesvaraya -p 8081:5000 devopsexercise_auth
    docker run -d --name dataservice -e MONGODB="mongodb://test:pass@mongo:21017/" --link modest_visvesvaraya -p 8080:5000 devopsexercise_data

## Cleanup

    docker kill authservice && docker rm authservice
    docker kill dataservice && docker rm dataservice

    docker kill nginx && docker rm nginx && docker rmi exercise:nginx && docker build -t exercise:nginx ./nginx

**WARNING** this will remove ALL docker images and processes from your machine.

    docker ps -q | xargs docker kill
    docker ps -aq | xargs docker rm -f
    docker images -q | xargs docker rmi -f


## Running with Docker Compose

    docker-compose build --pull
    docker-compose up -d
    docker-compose down --rmi all




