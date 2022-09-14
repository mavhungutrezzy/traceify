.PHONY: typehint
typehint:
	poetry run mypy --ignore-missing-imports .

.PHONY: isort
isort:
	poetry run isort .
	

.PHONY: safety
safety:
	poetry run safety check

.PHONY: bandit
bandit:
	poetry run bandit -r .

.PHONY: black
black:
	poetry run black -l 79 *.py


.PHONY: lint
lint:
	poetry run pylint .


.PHONY: flake8
flake8:
	poetry run flake8 .


.PHONY: server
server:
	poetry run python manage.py runserver

.PHONY: test
test:
	poetry run python manage.py test

.PHONY: migrate
migrate:
	poetry run python manage.py makemigrations
	poetry run python manage.py migrate

.PHONY: clean
clean:
	find . -type f -name "*.pyc" | xargs rm -fr
	find . -type d -name __pycache__ | xargs rm -fr
	find . -type d -name .pytest_cache | xargs rm -fr
	find . -type d -name .mypy_cache | xargs rm -fr
	find . -type d -name .coverage | xargs rm -fr


.PHONY: checklist
checklist:
	@echo "Running Checklist... \n"
	@echo "Running isort... \n"
	@make isort
	@echo "Running Type Hinting... \n"
	@make typehint
	@echo "Running black... \n"
	@make black
	@echo "Running flake8... \n"
	@make flake8
	# @echo "Running lint... \n"
	# @make lint
	@echo "Running safety... \n"
	@make safety
	@echo "Running bandit... \n"
	@make bandit
	# @echo "Running test... \n"
	# @make test
	@echo "Checklist Completed"
	@echo "Cache cleaning... \n"
	@make clean