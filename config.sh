#!/bin/bash

sudo fuser -k 8000/tcp
sudo rm -rf db.sqlite3
python3 manage.py makemigrations && python3 manage.py migrate --run-syncdb && python3 manage.py runserver