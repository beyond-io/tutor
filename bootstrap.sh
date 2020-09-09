#!/usr/bin/env bash


echo "installing python and postgres"
apt update
apt install -y python3.7 python3-pip postgresql postgresql-contrib


echo "installing flask"
pip3 install --upgrade pip
pip3 install pipenv
export PIPENV_VENV_IN_PROJECT=1
cd /vagrant/ && pipenv sync


echo "initializing new DB"
sudo -u postgres createdb tutor
sudo -u postgres psql -c "ALTER ROLE postgres WITH PASSWORD 'tutor';"


echo "configure flask variables"
export FLASK_APP=/vagrant/run.py
export FLASK_ENV=development    


echo "run tutor app"
pipenv run flask run -h 0.0.0.0 -p 5000
