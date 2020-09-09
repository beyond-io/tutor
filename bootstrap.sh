#!/usr/bin/env bash


echo "installing python and postgres"
apt update
apt install -y python3.7 python3-pip postgresql postgresql-contrib


echo "installing dependencies"
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

echo "initializing DB and migrations"
cd /vagrant
pipenv run python3 run.py db init
pipenv run python3 run.py db migrate
pipenv run python3 run.py db upgrade


echo "run tutor app"
pipenv run flask run -h 0.0.0.0 -p 5000
