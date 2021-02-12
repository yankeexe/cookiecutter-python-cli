FROM python:3.8-slim-buster as main

COPY . /app

WORKDIR /app

RUN pip install -e . -r requirements/dev.txt

ENTRYPOINT [ "{{cookiecutter.cli_command}}" ]
