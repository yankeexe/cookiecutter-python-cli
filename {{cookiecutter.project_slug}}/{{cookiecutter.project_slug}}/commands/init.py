"""
CLI initialization command.
"""
import click
from rich.prompt import Prompt

from {{cookiecutter.project_slug}} import console
from {{cookiecutter.project_slug}}.constants import WELCOME_MESSAGE


@click.command()
def init():
    """
    CLI Initialization demo.
    """
    console.print(WELCOME_MESSAGE)
