#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z postgres-postgresql 5432; do
      sleep 1
    done

    echo "PostgreSQL started"
fi

python main.py

exec "$@"