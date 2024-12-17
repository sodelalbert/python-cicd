# Python CICD

Project demonstrates CICD pipeliens configuration using brand new tools

# Installation

1. Clone project from repository
2. Installation of uv using manual: [Installing uv

   MacOS and Linux

   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

   Windows

   ```powershell
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```
3.

# UV commands reference

`uv init --package ` - initialize uv project with packaging
`uv.lock` - file used to synchronize dependencies amongst deployments
`uvx ruff format .` - format code in the project to be consistent
`ruff check --select I --fix` - fix import order, currently ruff format is not taking
for an account import formatting
`uvx ruff format --check .` - check code formatting in the project


`uv run pytest tests -v` - run pytest from uv
