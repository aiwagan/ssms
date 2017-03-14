compiled_requirements = './requires/compiled_requirements.txt'

clean:
	find . -type f -name "*.pyc" -delete

install:
	pip install pip-tools==1.8.0
	pip-compile ./requires/requirements.txt > $(compiled_requirements)
	pip install -r $(compiled_requirements)

run:
	python ./manage.py runserver 0:8000
