CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE IF NOT EXISTS newsletters (
    id VARCHAR(36) PRIMARY KEY,
    title VARCHAR(240) NOT NULL,
    author VARCHAR(160),
    source_url VARCHAR(2048),
    published_at DATE,
    tags JSONB NOT NULL DEFAULT '[]'::jsonb,
    body TEXT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_newsletters_created_at ON newsletters (created_at DESC);
CREATE INDEX IF NOT EXISTS idx_newsletters_published_at ON newsletters (published_at);
