#!/bin/sh

mkdir -p database
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
python scripts/seed.py

exec "$@"