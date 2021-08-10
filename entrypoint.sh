#!/usr/bin/env sh

python manage.py migrate

python manage.py collectstatic

python manage.py loaddata dump_db.json

gunicorn clothing_store.wsgi:application --bind 0.0.0.0:8000 --reload -w 4