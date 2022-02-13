container_name="kali"

dev:
	docker-compose up --build -d

into:
	docker exec -it  ${container_name} bash
	