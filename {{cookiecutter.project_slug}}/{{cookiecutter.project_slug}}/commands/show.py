"""
Show command for the CLI.
"""
import click

from {{cookiecutter.project_slug}} import console


@click.command()
def show():
    """
    Generic sub-command to show a message.
    """
    console.print("Get started with your CLI in no time!")
