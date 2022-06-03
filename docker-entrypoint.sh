#!/bin/sh

set -e

echo "Waiting for postgres..."

while ! nc -z db 5432; do
  sleep 0.1
done

echo "PostgreSQL started"

flask db upgrade

python app.py

#gunicorn -c gunicorn.config.py app:app