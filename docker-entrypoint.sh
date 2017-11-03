#!/bin/sh

exec gosu user /home/user/.virtualenvs/app/bin/python /app/manage.py "$@"
