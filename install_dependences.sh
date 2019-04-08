#!/bin/bash

sudo apt-get update && sudo apt-get -y upgrade
sudo apt-get install python3
sudo apt-get install curl
sudo apt-get install -y python3-pip
sudo pip3 install virtualenv
sudo pip3 install django
sudo pip3 install djangorestframework
sudo pip3 install model_mommy