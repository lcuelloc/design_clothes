#!/bin/sh
set -e

python manage.py migrate
python manage.py collectstatic --noinput

PORT="5000"
MAX_REQUESTS=0
REQUEST_TIMEOUT=300
NUM_WORKERS="$((2 * $(getconf _NPROCESSORS_ONLN) + 1))"
DJANGO_WSGI_MODULE="config.wsgi"

exec gunicorn \
    --log-level debug \
    --bind :"$PORT" \
    --max-requests "$MAX_REQUESTS" \
    --timeout "$REQUEST_TIMEOUT" \
    --workers "$NUM_WORKERS" \
    "$DJANGO_WSGI_MODULE":application