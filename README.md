# Cookiecutter for Python Click CLI

## Comes with:

 - [x] Pre-commit hooks
 - [x] mypy
 - [x] flake8
 - [x] mkdocs-material
 - [x] packaging

## Usage

Install cookiecutter.

```bash
$ pip install --user cookiecutter
```

Generate your project template using cookiecutter.

```bash
$ cookiecutter gh:yankeexe/cookiecutter-python-cli
```

## Project Setup

1. `cd` into project directory.

2. Create a virtual environment.

```bash
$ make venv
```

3. Activate it.

```bash
$ source venv/bin/activate
```

4. Install development dependencies with editable mode to test the CLI.

```bash
$ make install
```

## Documentation

1. Install documentation-related dependencies.

```bash
$ make docs
```

2. Serve the docs locally.

```bash
$ make serve-docs
```

## Help

For help related to make commands.

```bash
$ make help
```
