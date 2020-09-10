#!/bin/sh

set -euo pipefail

./manage.py collectstatic --noinput
./manage.py makemigrations --noinput
./manage.py migrate --noinput

daphne -b 0.0.0.0 -p 8000 snorlax.asgi:application
