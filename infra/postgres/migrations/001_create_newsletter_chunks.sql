CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE IF NOT EXISTS newsletter_chunks (
    id VARCHAR(36) PRIMARY KEY,
    newsletter_id VARCHAR(36) NOT NULL REFERENCES newsletters(id) ON DELETE CASCADE,
    chunk_index INTEGER NOT NULL,
    content TEXT NOT NULL,
    content_hash VARCHAR(64) NOT NULL,
    token_count INTEGER NOT NULL,
    embedding VECTOR(1536),
    embedding_model VARCHAR(120),
    embedding_status VARCHAR(32) NOT NULL DEFAULT 'pending',
    embedding_error TEXT,
    embedded_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    CONSTRAINT uq_newsletter_chunks_position UNIQUE (newsletter_id, chunk_index)
);

CREATE INDEX IF NOT EXISTS idx_newsletter_chunks_newsletter_id
    ON newsletter_chunks (newsletter_id);
CREATE INDEX IF NOT EXISTS idx_newsletter_chunks_embedding_status
    ON newsletter_chunks (embedding_status);
CREATE INDEX IF NOT EXISTS idx_newsletter_chunks_content_hash
    ON newsletter_chunks (content_hash);
