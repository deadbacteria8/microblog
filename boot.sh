#!/bin/sh

source .venv/bin/activate
flask db upgrade
exec gunicorn -b :5000 -w 4 --access-logfile /var/log/microblog/gunicorn-access.log --error-logfile /var/log/microblog/gunicorn-error.log microblog:app
