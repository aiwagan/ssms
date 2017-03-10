compiled_requirements = 'compiled_requirements.txt'

clean:
	find . -type f -name "*.pyc" -delete

install:
	pip install pip-tools==1.8.0
	pip-compile ./requires/requirements.txt > ./requires/$(compiled_requirements)
	pip install -r ./requires/$(compiled_requirements)

