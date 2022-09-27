"""
Entrypoint for CLI.
"""
import click

from {{cookiecutter.project_slug}}.commands import init, hello


@click.group()
def {{cookiecutter.cli_command}}():
    pass


{{cookiecutter.cli_command}}.add_command(init)
{{cookiecutter.cli_command}}.add_command(hello)
