# PetStore API Tests

Automated API test suite for PetStore and ReqRes APIs.

## Setup

```bash
# Install Poetry (if not installed)
curl -sSL https://install.python-poetry.org | python3 -

# Install dependencies
poetry install

# Run all tests
poetry run pytest

# Run specific markers
poetry run pytest -m smoke
poetry run pytest -m regression
poetry run pytest -m performance

# Run specific test file
poetry run pytest tests/test_petstore.py
poetry run pytest tests/test_reqres.py

# Run with parallel execution
poetry run pytest -n 4

# Run with HTML report
poetry run pytest --html=results/report.html