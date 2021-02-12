FROM python:3.8 as main

COPY . /app

WORKDIR /app

RUN make install

ENTRYPOINT [ "{{cookiecutter.cli_command}}" ]
