# PRD.md

## Product Overview

Newsletter RAG Curator is a full-stack application for turning a personal archive of newsletters into a searchable, source-grounded research assistant.

Users can ingest newsletter content, organize it with metadata, ask natural language questions, and curate useful answers into reusable notes or insights. The product is designed as a portfolio project that demonstrates Python AI engineering, retrieval-augmented generation, and full-stack application development.

## Goals

- Build a portfolio-ready RAG application with a polished end-to-end user experience.
- Demonstrate practical AI engineering using embeddings, vector search, retrieval, prompts, and grounded generation.
- Demonstrate full-stack development with Next.js, TypeScript, FastAPI, PostgreSQL, and pgvector.
- Show thoughtful product design around ingestion, search, citations, and curation.
- Keep the architecture understandable, testable, and deployable.

## Target Users

- Primary user: a knowledge worker who subscribes to many newsletters and wants to search, synthesize, and reuse insights.
- Portfolio reviewer: a hiring manager or engineer evaluating full-stack and AI engineering ability.
- Developer user: the project author or contributor extending ingestion, retrieval, and evaluation features.

## Problem Statement

Newsletter archives contain valuable information, but they are scattered across emails, web pages, and saved notes. Keyword search is limited, and manual synthesis is slow. Users need a way to ask higher-level questions, retrieve relevant source passages, and produce grounded summaries with citations.

## Core Use Cases

### Ingest Newsletter Content

The user can add newsletter content with title, author, source, publication date, URL, tags, and body text.

### Browse Archive

The user can browse stored newsletters, inspect metadata, and open individual source records.

### Semantic Search

The user can search across the archive using natural language and receive relevant passages ranked by semantic similarity.

### Ask Questions

The user can ask a question and receive an answer grounded in retrieved newsletter passages.

### View Citations

The user can see which source passages were used to produce an answer.

### Curate Insights

The user can save useful answers, summaries, themes, or extracted ideas for later reference.

## MVP Scope

- Manual newsletter ingestion through the app or API.
- Backend ingestion endpoint that stores source content and chunks.
- Embedding generation using the OpenAI API.
- PostgreSQL schema with pgvector embeddings.
- Semantic search endpoint.
- RAG question-answering endpoint with citations.
- Next.js UI for ingestion, archive browsing, search, and Q&A.
- Basic saved insight workflow.
- README-level setup documentation once implementation begins.

## Post-MVP Scope

- Email import or newsletter provider integrations.
- RSS feed ingestion.
- Scheduled ingestion jobs.
- Advanced tagging and collections.
- Hybrid search with keyword plus vector retrieval.
- Reranking.
- Retrieval evaluation dashboard.
- Multi-user authentication.
- Deployment hardening.
- Export to Markdown, Notion, or PDF.

## Non-Goals

- The MVP will not attempt to become a full email client.
- The MVP will not require browser extensions.
- The MVP will not support every newsletter format automatically.
- The MVP will not implement multi-tenant enterprise permissions.
- The planning phase will not include application code.

## Functional Requirements

### Content Management

- Users can create newsletter records.
- Users can view a list of stored newsletter records.
- Users can view newsletter details and associated chunks.
- Users can add metadata such as title, author, date, source URL, and tags.

### Ingestion Pipeline

- The backend accepts raw newsletter text.
- The backend chunks content into retrievable passages.
- The backend generates embeddings for chunks.
- The backend stores content, chunks, metadata, and embeddings.
- The backend reports ingestion success or failure clearly.

### Retrieval

- The backend supports semantic search over newsletter chunks.
- Search results include source metadata and passage text.
- Retrieval supports configurable result limits.
- Retrieval should be designed to support metadata filters.

### Question Answering

- The backend retrieves relevant chunks for a user question.
- The backend sends context to the OpenAI API.
- The answer should cite source passages.
- The answer should acknowledge insufficient context when retrieval is weak.

### Curation

- Users can save useful generated answers or notes.
- Saved insights preserve source references.
- Users can browse saved insights.

### Frontend

- The app provides pages or views for ingestion, archive, search, Q&A, and saved insights.
- The UI includes loading, empty, success, and error states.
- The UI should be responsive and portfolio-ready.

## Non-Functional Requirements

- Use type hints and validation throughout backend code.
- Use TypeScript throughout frontend code.
- Keep secrets in environment variables.
- Keep API contracts documented and stable.
- Add tests around ingestion, chunking, retrieval, and API behavior during implementation.
- Keep local development setup reproducible.
- Make the project understandable to a reviewer within a few minutes.

## Success Criteria

- A reviewer can run the app locally from documented instructions.
- A user can ingest sample newsletter content and ask questions about it.
- Answers include citations to retrieved source passages.
- The project clearly demonstrates FastAPI, PostgreSQL, pgvector, OpenAI API usage, Next.js, and TypeScript.
- The codebase is organized, readable, and supported by meaningful tests.

## Risks

- Retrieval quality may be poor without careful chunking and metadata handling.
- OpenAI API costs can grow during repeated ingestion and testing.
- Full-stack scope can expand too quickly without milestone discipline.
- Newsletter content formats may vary significantly.

## Open Questions

- Will ingestion begin with pasted text, uploaded files, URLs, RSS feeds, or email export?
- Should the MVP include authentication or remain single-user local-first?
- What deployment target should be used for the portfolio version?
- What sample newsletter dataset should be included or documented for demos?
