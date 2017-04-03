clean:
	find . -type f -name "*.pyc" -delete

install:
	pip install -r requirements.txt

configdb:
	psql -U postgres -c "CREATE ROLE SSMS_USER PASSWORD 'SSMS_PASS' SUPERUSER CREATEDB CREATEROLE INHERIT LOGIN;"
	psql -U postgres -c "CREATE DATABASE SSMS_DB WITH OWNER SSMS_USER;"
	psql -U postgres -c "CREATE DATABASE TEST_SSMS_DB WITH OWNER SSMS_USER;"

migrate:
	manage.py makemigrations
	manage.py migrate_schemas

run:
	manage.py runserver 0:8000

tests:
	coverage run --source='.' manage.py test customers --noinput
	coverage report

all: clean install migrate
