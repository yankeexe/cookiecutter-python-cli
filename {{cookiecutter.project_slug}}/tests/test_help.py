from click.testing import CliRunner
from {{cookiecutter.project_slug}} import app


def test_help():
    runner = CliRunner()
    result = runner.invoke(app.cli)
    assert result.exit_code == 0
    assert "Usage: " in result.output
