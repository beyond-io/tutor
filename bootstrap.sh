#!/usr/bin/env bash


echo "installing python and postgres"
apt update
apt install -y python3.7 python3-pip python3.7-dev postgresql postgresql-contrib postgresql-common postgresql-client libpq-dev


echo "installing dependencies"
pip3 install pipenv

# Not needed on CI
if [ ! "$CI" ] 
then
  export PIPENV_VENV_IN_PROJECT="enabled"
  export VIRTUALENV_ALWAYS_COPY=1
  cd /vagrant
fi

pipenv sync --dev

# Need to start postgres service on CI
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
pipenv run python3 run.py db init
pipenv run python3 run.py db migrate
pipenv run python3 run.py db upgrade

# No need to run the app on CI
if [ ! "$CI" ] 
then
  echo "run tutor app"
  pipenv run python3 launch_data.py
  nohup pipenv run flask run -h 0.0.0.0 -p 5000
fi
