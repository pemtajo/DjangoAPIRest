#!/bin/bash

sudo fuser -k 8000/tcp
sudo rm -rf db.sqlite3
./manage.py makemigrations && ./manage.py migrate && ./manage.py runserver