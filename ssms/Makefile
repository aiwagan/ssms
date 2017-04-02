clean:
	find . -type f -name "*.pyc" -delete

install:
	pip install -r requirements.txt

migrate:
	python ./manage.py makemigrations
	python ./manage.py migrate_schemas

run:
	python ./manage.py runserver 0:8000

tests:
	@echo "Tests will be configured soon"

all: clean install migrate
