"""
Entrypoint for CLI.
"""
import click

from {{cookiecutter.project_slug}}.commands import init, show


@click.group()
def cli():
    pass


cli.add_command(init)
cli.add_command(show)
