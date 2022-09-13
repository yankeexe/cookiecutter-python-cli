"""
Entrypoint for CLI.
"""
import click

from {{cookiecutter.project_slug}}.commands import init, hello


@click.group()
def {{cookiecutter.cli_command}}():
    pass


cli.add_command(init)
cli.add_command(hello)
