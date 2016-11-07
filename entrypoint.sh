#!/usr/bin/env bash

python /usr/src/app/manage.py syncdb
python /usr/src/app/manage.py collectstatic --noinput

uwsgi --ini /usr/src/app/application/uwsgi.ini
