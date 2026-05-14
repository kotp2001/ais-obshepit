#!/bin/bash
pip install --upgrade pip
pip install Django==4.2.7
pip install psycopg2-binary==2.9.9
pip install gunicorn==21.2.0
pip install whitenoise==6.6.0
pip install django-environ==0.11.2
python manage.py collectstatic --noinput
