#!/bin/bash
if [[ -z "${ENVIRONMENT}" ]]; then
    echo "Runing web application: development"
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver 0.0.0.0:8000
elif [[ ${ENVIRONMENT} == "production" ]]; then
    python manage.py makemigrations
    python manage.py migrate
    python manage.py collectstatic --noinput --clear
    gunicorn bywhats.wsgi --bind 0.0.0.0:8000
fi