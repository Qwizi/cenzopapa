#!/bin/sh
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py loaddata initial_images_data.json
exec "$@"
