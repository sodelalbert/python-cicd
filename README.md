# Python CICD

Project demonstrates CICD pipeliens configuration using brand new tools

# Installation

1. Clone project from repository
2. Installation of uv using manual: [Installing uv](https://uv.astral.sh/docs/installation)

   MacOS and Linux

   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

   Windows

   ```powershell
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```
3. Synchronize repository with uv

   ```bash
   uv sync
   ```

# UV commands reference

`uv init --package ` - initialize uv project with packaging.  
`uv.lock` - file used to synchronize dependencies amongst deployments.  
`uvx ruff format .` - format code in the project to be consistent.  
`ruff check --select I --fix` - fix import order, currently ruff format is not taking
for an account import formatting.  
`uvx ruff format --check .` - check code formatting in the project.   

`uv run pytest tests -v` - run pytest from uv.   

# Mypy configuration

Mypy is sometimes complaining about 


# Pycharm configuration
* Pycharm is not recognising package - Mark `src` directory as source root.
<br></br>
   `Skipping analyzing "python_cicd": module is installed, but missing library stubs or py.typed marker  [import-untyped]`. 
<br></br>
   To resolve this issue add `py.typed` file to the `src` / library directory  or cosider using `pyright`.
