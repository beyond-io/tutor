#!/usr/bin/env bash

echo "installing python"
apt update
apt install -y python3.7 python3-pip

echo "installing flask"
pip3 install --upgrade pip
pip3 install flask

echo "configure flask variables"
export FLASK_APP=/vagrant/tutor/run.py
export FLASK_ENV=development    

echo "run tutor app"
flask run -h 0.0.0.0 -p 5000