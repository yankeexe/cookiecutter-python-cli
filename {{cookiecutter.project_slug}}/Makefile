SHELL :=/bin/bash
CWD := $(PWD)
TMP_PATH := $(CWD)/.tmp
VENV_PATH := $(CWD)/venv

.PHONY: test clean docs
.DEFAULT_GOAL := help

# Read about configuring Makefile:
## https://dev.to/yankee/streamline-projects-using-makefile-28fe

clean: # remove python temp files
	@rm -rf $(TMP_PATH) __pycache__ .pytest_cache
	@find . -name '*.pyc' -delete
	@find . -name '__pycache__' -delete

test: # run pytest in verbose mode
	@pytest -vvv

venv: # create a virtual env
	@python3 -m venv venv

format: # format all files using black
	@black .

check: # diff changes to be made by black
	@black --check --diff .

install: # install app dependencies for development
	@pip install -e . -r requirements/dev.txt

pre-commit: # install pre-commit hooks
	@echo -e "\nInstalling pre-commit hook..."
	@pre-commit install

docs: # Install documentation related dependencies.
	@pip install -r requirements/docs.txt

serve-docs: # serve docs on localhost
	@mkdocs serve -f docs/mkdocs.yml

distributions: # create distribution wheel and zip for PyPI
	@pip install -r requirements/publish.txt
	@python3 setup.py sdist bdist_wheel
	@echo "Use `twine upload dist/*` to upload to PyPI"

docker-image:
	@docker build -t {{cookiecutter.cli_command.strip().lower().replace(' ', '_').replace('-', '_')}} .

help: # Show this help
	@egrep -h '\s#\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?# "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
