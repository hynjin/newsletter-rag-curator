# AGENTS.md

## Project: Newsletter RAG Curator

Newsletter RAG Curator is a portfolio-ready full-stack RAG application for collecting, indexing, searching, and synthesizing insights from newsletter content.

The project should demonstrate strong Python AI engineering skills, practical full-stack development, clean product thinking, and maintainable architecture.

## Core Stack

- Frontend: Next.js, TypeScript
- Backend: FastAPI, Python
- Database: PostgreSQL with pgvector
- AI: Gemini API
- Retrieval: embeddings, semantic search, metadata filtering, source-grounded responses

## Working Principles

- Do not write application code until the planning documents are in place and the implementation phase is explicitly started.
- Prefer simple, production-shaped architecture over experimental complexity.
- Keep the project portfolio-ready: clear setup, readable code, useful UX, documented design tradeoffs, and realistic end-to-end workflows.
- Favor small, verifiable milestones over large unfinished features.
- Make decisions explicit in `DECISIONS.md` when they affect architecture, stack, data model, retrieval strategy, deployment, or user experience.

## Product Expectations

The application should help a user:

- Add newsletter issues or articles.
- Store source content and metadata.
- Generate embeddings for retrieval.
- Ask questions across the newsletter archive.
- Receive grounded answers with citations back to source passages.
- Curate useful summaries, themes, saved insights, or research notes.

## Engineering Expectations

Backend work should emphasize:

- Typed request and response models.
- Clear service boundaries.
- Robust ingestion and retrieval pipelines.
- Testable business logic.
- Safe handling of API keys and environment variables.
- Observability-friendly logging and errors.

Frontend work should emphasize:

- Clean, responsive application UI.
- Type-safe API integration.
- Clear loading, empty, and error states.
- Usable workflows for ingestion, search, chat, and curation.
- Portfolio-quality polish without overbuilding.

Database work should emphasize:

- Explicit schema design.
- pgvector-based similarity search.
- Metadata fields that support filtering and citations.
- Migrations once implementation begins.

AI work should emphasize:

- Grounded generation.
- Prompt clarity.
- Retrieval evaluation.
- Graceful behavior when context is insufficient.
- Clear separation between ingestion, retrieval, and generation.

## Documentation Expectations

Keep these documents current:

- `PRD.md`: product scope, users, requirements, constraints.
- `ROADMAP.md`: implementation phases and milestone checklists.
- `DECISIONS.md`: durable technical and product decisions.
- `AGENTS.md`: guidance for future coding agents and contributors.

## Non-Goals For Initial Planning Phase

- No application source code.
- No dependency installation.
- No generated project scaffold.
- No database migrations.
- No deployment configuration.

## Suggested Future Repo Shape

This is a planning note only. Do not create these directories until implementation begins.

```text
apps/
  web/
services/
  api/
infra/
docs/
```

## Quality Bar

The finished project should feel like a small but real product, not a demo script. It should show that the author can design and implement a modern AI application across frontend, backend, database, and retrieval layers.
