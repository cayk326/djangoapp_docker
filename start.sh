#!/bin/bash -e
(docker-compose up -d --build)&PID1=$!
wait $PID1


DJANGOID=`docker ps -f "name=django" --format "{{.ID}}"`


docker exec -it ${DJANGOID} python manage.py collectstatic
docker exec -it ${DJANGOID} chmod -R 755 app/static/app /opt
docker exec -it ${DJANGOID} cp -r app/static/app /opt
docker-compose restart
docker-compose logs -f
