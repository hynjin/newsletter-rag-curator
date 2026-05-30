# Newsletter RAG Curator

Newsletter RAG Curator is a portfolio-ready full-stack RAG application for collecting,
indexing, searching, and synthesizing insights from newsletter content.

Phase 1 establishes the project foundation: a Next.js frontend, FastAPI backend, and local
PostgreSQL database with pgvector enabled.

## Stack

- Frontend: Next.js, TypeScript
- Backend: FastAPI, Python
- Database: PostgreSQL with pgvector
- AI: OpenAI API in later phases

## Repository Structure

```text
apps/
  web/   Next.js frontend
  api/   FastAPI backend
infra/
  postgres/   Local database initialization
docs/
  ARCHITECTURE.md
```

## Prerequisites

- Docker and Docker Compose
- Node.js 20 or newer
- Python 3.11 or newer

## Local Setup

Start PostgreSQL with pgvector:

```bash
docker compose up -d db
```

Configure and run the backend. The API requires Python 3.11 or newer; verify the version before
creating the virtual environment:

```bash
cd apps/api
python --version
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -e ".[dev]"
cp .env.example .env
uvicorn app.main:app --reload
```

The backend health endpoint is available at `http://localhost:8000/health`.

If your virtual environment was created with Python 3.9 or older, recreate it with Python 3.11+:

```bash
cd apps/api
rm -rf .venv
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -e ".[dev]"
```

Configure and run the frontend in a second terminal:

```bash
cd apps/web
npm install
cp .env.example .env.local
npm run dev
```

The frontend is available at `http://localhost:3000`.

If the frontend reports a missing `.next/server` chunk after code changes, stop the dev server,
clear the Next.js cache, and restart it:

```bash
cd apps/web
npm run clean
npm run dev
```

## Development Commands

Backend:

```bash
cd apps/api
ruff check .
pytest
```

Frontend:

```bash
cd apps/web
npm run lint
npm run typecheck
npm run build
```

## Current Scope

Implemented:

- Monorepo app structure.
- FastAPI health endpoint.
- Newsletter create, list, and detail API endpoints.
- Paste-based newsletter ingestion UI and archive list.
- Next.js homepage that displays backend health.
- PostgreSQL with pgvector local setup.
- Environment variable examples.

Not yet implemented:

- Embeddings.
- RAG question answering.
- Authentication.
