#!/bin/sh

# Prepare log files and start outputting logs to stdout
# touch ./logs/gunicorn.log
#touch ./logs/gunicorn-access.log
#tail -n 0 -f ./logs/gunicorn*.log &

export DJANGO_SETTINGS_MODULE=openstack.settings
exec gunicorn openstack.wsgi:application \
    --name ui_service \
    --bind 0.0.0.0:8086 \
    --workers 4 \
    --log-level=info \
    --log-file=../logs/gunicorn.log \
"$@"

# --log-level=info \
#    --log-file=./logs/gunicorn.log \
#    --access-logfile=./logs/gunicorn-access.log \
