#!/usr/bin/env bash

python /usr/src/app/manage.py migrate
python /usr/src/app/manage.py collectstatic

uwsgi --ini /usr/src/app/application/uwsgi.ini