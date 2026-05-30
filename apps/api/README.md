# Newsletter RAG Curator API

FastAPI service for the Newsletter RAG Curator backend.

## Commands

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -e ".[dev]"
cp .env.example .env
uvicorn app.main:app --reload
```

The API will run at `http://localhost:8000`.

The API requires Python 3.11 or newer. If `.venv/bin/python --version` reports Python 3.9 or
older, recreate the virtual environment with Python 3.11+ before installing dependencies.

## Useful Checks

```bash
ruff check .
pytest
```
