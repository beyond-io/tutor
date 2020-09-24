#!/usr/bin/env bash


echo "installing python and postgres"
sudo apt update
sudo apt install -y python3.7 python3-pip python3.7-dev postgresql postgresql-contrib postgresql-common postgresql-client libpq-dev


echo "installing dependencies"
pip3 install pipenv

if [ ! "$CI" ] 
then
  export PIPENV_VENV_IN_PROJECT="enabled"
  export VIRTUALENV_ALWAYS_COPY=1
  cd /vagrant
fi

pipenv sync --dev

if [ "$CI" ]
then
  sudo systemctl start postgresql
fi

echo "initializing new DB"
sudo -u postgres createdb tutor
sudo -u postgres psql -c "ALTER ROLE postgres WITH PASSWORD 'tutor';"


echo "configure flask variables"
export FLASK_APP=/vagrant/run.py
export FLASK_ENV=development    

echo "initializing DB and migrations"

if [ ! "$CI" ] 
then
  cd /vagrant
fi

pipenv run python3 run.py db init
pipenv run python3 run.py db migrate
pipenv run python3 run.py db upgrade


echo "run tutor app"
nohup pipenv run flask run -h 0.0.0.0 -p 5000
