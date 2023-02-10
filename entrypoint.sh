#!/bin/sh

set -e

echo 'INFO:     Starting entrypoint.sh'

env=${APP_ENV:-production}

if [ $env = "production" ]
then
    echo "INFO:     Running in production mode"
    uvicorn app.main:app --host 0.0.0.0 --port 8000
elif [ $env = 'test' ]
then
    echo "INFO:     Running in test mode"
    coverage run -m pytest
    coverage report -m
else
    echo "INFO:     Running in development mode"
    uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
fi
