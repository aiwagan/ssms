clean:
	find . -type f -name "*.pyc" -delete

install:
	pip install pip setuptools pip-tools --upgrade
	pip uninstall appdirs -y && pip install appdirs==1.4.0
	pip-compile requirements.txt > compiled_requirements.txt
	pip install -r compiled_requirements.txt

migrate:
	python ./manage.py makemigrations
	python ./manage.py migrate_schemas

run:
	python ./manage.py runserver 0:8000
