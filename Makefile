default:
	@echo "Manages the Dev Environment"
	@echo
	@echo "up          brings up the env"
	@echo "ping        tests the health endpoints of services"
	@echo "bootstrap   bootstraps database with a user"
	@echo "test        runs a simple test suite against env"
	@echo "down        tears down the env"

up:
	docker-compose build --pull
	docker-compose up -d
	docker-compose ps

down:
	docker-compose down --rmi all

bootstrap:
	docker exec -it dockerservices_mongo_1 mongo /app/bootstrap.js

ping:
	curl http://localhost/api/auth/health
	curl http://localhost/api/data/health

test:
	./test.sh
