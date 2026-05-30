# ROADMAP.md

## Roadmap

This roadmap is intentionally phased so the project can become useful quickly while still leaving room for portfolio polish and deeper AI engineering.

## Phase 0: Planning

Status: Complete

- [x] Create `AGENTS.md`.
- [x] Create `PRD.md`.
- [x] Create `ROADMAP.md`.
- [x] Create `DECISIONS.md`.
- [x] Confirm MVP ingestion path.
- [x] Confirm local development and deployment strategy.

## Phase 1: Project Foundation

Status: Complete

Goal: Establish a clean full-stack foundation.

- [x] Create frontend app with Next.js and TypeScript.
- [x] Create backend service with FastAPI and Python.
- [x] Add local PostgreSQL and pgvector setup.
- [x] Add environment variable examples.
- [x] Add basic developer setup instructions.
- [x] Add formatting, linting, and test commands.
- [x] Add health check endpoint.
- [x] Add frontend shell with app navigation.

## Phase 2: Data Model And Ingestion

Status: In progress

Goal: Store newsletter content in a retrieval-ready shape.

- [x] Design database schema for newsletters.
- [x] Create newsletters table.
- [x] Implement newsletter create and list endpoints.
- [x] Implement newsletter detail endpoint.
- [x] Add ingestion tests.
- [x] Add frontend ingestion flow.
- [x] Add archive browsing UI.
- [ ] Design database schema for chunks, embeddings, and saved insights.
- [ ] Add migrations.
- [ ] Implement text chunking service.
- [ ] Implement embedding generation service using OpenAI API.
- [ ] Store embeddings with pgvector.

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
