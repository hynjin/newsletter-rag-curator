# DECISIONS.md

## Decision Log

This document records product and technical decisions that should remain visible to future contributors and coding agents.

Use this format for new entries:

```md
## YYYY-MM-DD: Decision Title

Status: Proposed | Accepted | Superseded

Decision:

Context:

Consequences:
```

## 2026-05-29: Use Next.js And TypeScript For Frontend

Status: Accepted

Decision:

The frontend will use Next.js with TypeScript.

Context:

The project should demonstrate modern full-stack development skills and provide a polished portfolio-ready user interface.

Consequences:

- The frontend can support file-based routing, server-aware rendering options, and a strong TypeScript developer experience.
- API integration should use typed request and response shapes.
- UI implementation should prioritize maintainability and clear user workflows.

## 2026-05-29: Use FastAPI And Python For Backend

Status: Accepted

Decision:

The backend will use FastAPI with Python.

Context:

The project should demonstrate Python AI engineering skills while providing a practical API layer for ingestion, retrieval, and generation.

Consequences:

- Backend endpoints should use typed Pydantic models.
- AI, retrieval, and ingestion logic can be implemented in Python service modules.
- Tests should cover core Python services and API behavior.

## 2026-05-29: Use PostgreSQL With pgvector

Status: Accepted

Decision:

The database will use PostgreSQL with pgvector for embedding storage and similarity search.

Context:

The project needs realistic vector retrieval while staying close to a production-shaped relational database architecture.

Consequences:

- The schema should separate source documents from chunks and embeddings.
- Retrieval can combine semantic search with relational metadata filters.
- Local development must include pgvector setup instructions.

## 2026-05-29: Use OpenAI API For AI Capabilities

Status: Accepted

Decision:

The application will use the OpenAI API for embeddings and answer generation.

Context:

The project goal explicitly includes OpenAI API usage and should demonstrate practical RAG implementation.

Consequences:

- API keys must be managed through environment variables.
- AI calls should be isolated behind service boundaries for testability.
- The app should handle API failures and insufficient context gracefully.

## 2026-05-29: Start With Planning Documents Only

Status: Accepted

Decision:

The initial project phase will create planning documents only and will not include application code.

Context:

The user explicitly requested `AGENTS.md`, `PRD.md`, `ROADMAP.md`, and `DECISIONS.md` before writing code.

Consequences:

- No project scaffold, dependencies, migrations, or application files should be created during this phase.
- Implementation should begin only after the user explicitly requests it.

## 2026-05-29: MVP Should Prioritize Manual Ingestion

Status: Proposed

Decision:

The MVP should likely begin with manual newsletter ingestion through pasted text or API submission before adding integrations.

Context:

Manual ingestion reduces integration complexity and lets the project focus first on the RAG pipeline, database design, and user experience.

Consequences:

- The project can reach an end-to-end demo sooner.
- RSS, email import, and URL scraping can remain post-MVP features.
- This decision should be confirmed before implementation begins.
