testes:
	python -m pytest

coverage:
	coverage run -m pytest
	coverage report -m
	coverage html

style:
	flake8 .

requirements:
	pipenv lock
	pipenv requirements > requirements.txt
	pipenv requirements --dev > requirements-dev.txt

lint:
	@echo "Running flake8 ..."
	@echo $(SRC_FILES) | xargs flake8 --max-line-length=119

	@echo "Running pycodestyle ..."
	@echo $(SRC_FILES) | xargs pycodestyle --show-pep8 --show-source --max-line-length=119

	@echo "Running blue ..."
	@blue --diff --color --check --line-length=119 .

install-dev:
	@pip install -U pipenv
	@pipenv install --dev --system -v

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

worker:
	celery -A core worker -l info

beat:
	celery -A core beat -l info

check:
	make style
	make testes
	make requirements
