# Python CICD

Project demonstrates CICD pipeliens configuration using brand new tools

# TODO List

- [ ] Add more robust pytest configuration.
- [ ] Ensure docstring documentation is checked by ruff or mypy.

# Installation

Clone project from repository.

Installation of uv using manual: [Installing uv](https://uv.astral.sh/docs/installation)

MacOS and Linux

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Windows

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

# Requirements installation

Install requirements and configure python interpreter using uv sync command.

```bash
uv sync
```

# Testing

```bash
uv run pytest
```

# UV commands reference

`uv init --package ` - initialize uv project with packaging.
`uv.lock` - file used to synchronize dependencies amongst deployments.
`uvx ruff format .` - format code in the project to be consistent.
`ruff check --select I --fix` - fix import order, currently ruff format is not taking
for an account import formatting.
`uvx ruff format --check .` - check code formatting in the project.

`uv run pytest tests -v` - run pytest from uv.

# Ruff configuration

* If you like to require docstring add following configuration to `pyproject.toml` file.

*To be fixed*

```
[tool.ruff]
lint.extend-select = ["D"]
```

# Mypy configuration

Mypy is sometimes complaining about Pycharm configuration

* Pycharm is not recognising package - Mark `src` directory as source root.

  `Skipping analyzing "python_cicd": module is installed, but missing library stubs or py.typed marker  [import-untyped]`.

    * Indicate to mypy src location (library code) file path in `pyproject.toml` file.
  ```
  [tool.mypy]
  mypy_path = "src"
  ```

    * To resolve this issue add `py.typed` file to the `src` / library directory or
      cosider using `pyright`.

# Pytest configuration

* Indicate to mypy src location (library code) file path in `pyproject.toml` file.
  ```
  [tool.mypy]
  mypy_path = "src"
  ```

* Pytest parallel running with xdist plugin
  ```
  [tool.pytest.ini_options]
  addopts = "-v --durations=0 -n auto"
  ``` 
  PyCharm execution is failing - not recognising "-n" option. To run tests in parallel
  use command line.

  Execution possible with command `uv run pytest`

* Pytest pretty output with `pytest-sugar` plugin
  ```
  [tool.pytest.ini_options]
  addopts = "-v --durations=0 --color=yes"
  ```