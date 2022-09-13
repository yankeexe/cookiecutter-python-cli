"""
Show command for the CLI.
"""
import click

from {{cookiecutter.project_slug}} import console


@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        console.print(f"Hello, [italic red]{name}[/italic red] :)")
