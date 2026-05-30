# ROADMAP.md

## Roadmap

This roadmap is intentionally phased so the project can become useful quickly while still leaving room for portfolio polish and deeper AI engineering.

## Phase 0: Planning

Status: In progress

- [x] Create `AGENTS.md`.
- [x] Create `PRD.md`.
- [x] Create `ROADMAP.md`.
- [x] Create `DECISIONS.md`.
- [ ] Confirm MVP ingestion path.
- [ ] Confirm local development and deployment strategy.

## Phase 1: Project Scaffold

Goal: Establish a clean full-stack foundation.

- [ ] Create frontend app with Next.js and TypeScript.
- [ ] Create backend service with FastAPI and Python.
- [ ] Add local PostgreSQL and pgvector setup.
- [ ] Add environment variable examples.
- [ ] Add basic developer setup instructions.
- [ ] Add formatting, linting, and test commands.
- [ ] Add health check endpoint.
- [ ] Add frontend shell with app navigation.

## Phase 2: Data Model And Ingestion

Goal: Store newsletter content in a retrieval-ready shape.

- [ ] Design database schema for newsletters, chunks, embeddings, and saved insights.
- [ ] Add migrations.
- [ ] Implement newsletter create and list endpoints.
- [ ] Implement newsletter detail endpoint.
- [ ] Implement text chunking service.
- [ ] Implement embedding generation service using OpenAI API.
- [ ] Store embeddings with pgvector.
- [ ] Add ingestion tests.
- [ ] Add frontend ingestion flow.
- [ ] Add archive browsing UI.

## Phase 3: Semantic Search

Goal: Let users find relevant newsletter passages through natural language.

- [ ] Implement vector similarity search query.
- [ ] Add semantic search endpoint.
- [ ] Return passage text, similarity score, and source metadata.
- [ ] Add result limit controls.
- [ ] Add optional metadata filter design.
- [ ] Add retrieval tests with sample data.
- [ ] Build frontend search interface.
- [ ] Add empty and weak-result states.

## Phase 4: RAG Question Answering

Goal: Generate grounded answers with citations.

- [ ] Implement retrieval orchestration for questions.
- [ ] Design prompt template for grounded answers.
- [ ] Call OpenAI API for answer generation.
- [ ] Include source citations in response format.
- [ ] Handle insufficient context.
- [ ] Add API tests for answer shape and failure modes.
- [ ] Build frontend Q&A interface.
- [ ] Show citations and source passages in the UI.

## Phase 5: Curation

Goal: Turn generated answers into reusable research artifacts.

- [ ] Add saved insights database model.
- [ ] Add endpoints to save and list insights.
- [ ] Preserve answer text, user note, question, and citations.
- [ ] Build saved insights UI.
- [ ] Add tags or collections if scope allows.

## Phase 6: Quality And Portfolio Polish

Goal: Make the project feel complete, credible, and easy to evaluate.

- [ ] Add representative seed data or sample ingestion guide.
- [ ] Add backend unit and integration test coverage.
- [ ] Add frontend smoke tests or component tests.
- [ ] Improve error handling and logging.
- [ ] Add retrieval quality notes or simple evaluation script.
- [ ] Add screenshots or demo walkthrough.
- [ ] Write final README.
- [ ] Document architecture and tradeoffs.
- [ ] Prepare deployment or hosted demo if feasible.

## Phase 7: Stretch Features

Goal: Deepen the project without compromising the MVP.

- [ ] RSS ingestion.
- [ ] Email export ingestion.
- [ ] URL extraction and cleanup.
- [ ] Hybrid search.
- [ ] Reranking.
- [ ] Summaries by newsletter, author, tag, or time period.
- [ ] Trend and theme detection.
- [ ] Evaluation dashboard.
- [ ] Authentication.
- [ ] Export saved insights.

## Milestone Definition Of Done

Each implementation milestone should include:

- Working frontend and backend behavior.
- Clear API contract.
- Tests proportional to the risk of the change.
- Updated documentation when behavior or setup changes.
- A short decision entry when a durable tradeoff is made.
