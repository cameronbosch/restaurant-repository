#!bin/bash
docker-compose -f docker-compose.prod.yml exec web python manage.py create_db