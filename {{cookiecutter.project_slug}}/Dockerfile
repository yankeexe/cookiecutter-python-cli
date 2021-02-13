FROM python:3.8-slim-buster

COPY . /app

WORKDIR /app

RUN python setup.py develop

ENTRYPOINT [ "{{cookiecutter.cli_command.strip().lower().replace(' ', '_').replace('-', '_')}}" ]
