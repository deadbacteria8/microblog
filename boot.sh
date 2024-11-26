#!/bin/sh

source .venv/bin/activate
while true; do
    flask db upgrade
    if [[ "$?" == "0" ]]; then
        break
    fi
    echo Upgrade command failed, retrying in 5 secs...
    sleep 5
done
exec gunicorn -b :5000 -w 4 --access-logfile /var/log/microblog/gunicorn-access.log --error-logfile /var/log/microblog/gunicorn-error.log microblog:app
