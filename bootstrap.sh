#!/usr/bin/env bash


echo "installing python and postgres"
apt update
apt install -y python3.7 python3-pip python3.7-dev postgresql postgresql-contrib postgresql-common postgresql-client libpq-dev


echo "installing dependencies"
pip3 install pipenv
cd /vagrant/ && pipenv sync --dev


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
nohup pipenv run flask run -h 0.0.0.0 -p 5000
