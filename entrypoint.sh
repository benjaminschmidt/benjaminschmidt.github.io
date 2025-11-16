#! /bin/sh

python manage.py migrate
python manage.py collectstatic --noinput
python manage.py deleteallusers
python manage.py createsuperuser --no-input
gunicorn --bind 0.0.0.0 personal_site.wsgi
