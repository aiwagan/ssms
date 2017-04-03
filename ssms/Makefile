clean:
	find . -type f -name "*.pyc" -delete

install:
	pip install -r requirements.txt

migrate:
	manage.py makemigrations
	manage.py migrate_schemas

run:
	manage.py runserver 0:8000

tests:
	coverage run --source='.' manage.py test customers --noinput
	coverage report

all: clean install migrate
