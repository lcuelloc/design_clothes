#!/bin/sh
set -e

until PGPASSWORD=$DB_PASSWORD psql -h design -U "$DB_USER" -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - executing command"

python manage.py migrate
python manage.py collectstatic --noinput

exec "$@"