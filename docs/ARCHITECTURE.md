# Architecture

Newsletter RAG Curator is organized as a small monorepo with separate frontend and backend
applications.

```text
apps/
  web/   Next.js and TypeScript frontend
  api/   FastAPI and Python backend
infra/
  postgres/   Local database initialization
docs/
  ARCHITECTURE.md
```

## Phase 1 Foundation

- `apps/web` owns the browser experience and calls the backend API through
  `NEXT_PUBLIC_API_BASE_URL`.
- `apps/api` owns HTTP API routes, request and response schemas, future services, and future
  repository/database access.
- `docker-compose.yml` runs PostgreSQL with the `pgvector` extension enabled by
  `infra/postgres/init.sql`.

## Phase 2 Ingestion

- `newsletters` stores raw newsletter source records and metadata.
- The backend exposes `POST /newsletters`, `GET /newsletters`, and `GET /newsletters/{id}`.
- The frontend exposes a paste-based ingestion form and archive list at `/newsletters`.
- Chunking, embeddings, AI provider calls, and vector search were intentionally deferred from this
  phase.

## Phase 3 Chunking And Embeddings

- `newsletter_chunks` stores ordered chunks for each newsletter.
- `apps/api/app/services/chunking.py` owns deterministic text chunking.
- `apps/api/app/services/ai_provider.py` owns the AI provider boundary and Gemini API calls for
  embedding generation and future text generation.
- `apps/api/app/repositories/newsletter_chunks.py` stores chunk rows and embedding metadata.
- Newsletter creation synchronously chunks text and attempts embedding generation.
- Semantic search, RAG answering, and saved insights remain deferred.

## Future Boundaries

- Ingestion, chunking, embeddings, retrieval, and generation should live behind backend service
  modules.
- Database access should be isolated in repository modules.
- Frontend pages should call typed API helpers rather than embedding fetch logic throughout the UI.
