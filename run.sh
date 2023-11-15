#!/bin/sh

cd vpn

python manage.py collectstatic --no-input --clear

python manage.py makemigrations

python manage.py migrate

gunicorn vpn.wsgi:application --bind 0.0.0.0:8000