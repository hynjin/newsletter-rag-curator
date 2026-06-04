from datetime import UTC, datetime

from sqlalchemy import delete, select
from sqlalchemy.orm import Session

from app.models.newsletter_chunk import NewsletterChunk
from app.services.chunking import ChunkCandidate


class NewsletterChunkRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def replace_for_newsletter(
        self,
        newsletter_id: str,
        chunks: list[ChunkCandidate],
    ) -> list[NewsletterChunk]:
        self.db.execute(
            delete(NewsletterChunk).where(NewsletterChunk.newsletter_id == newsletter_id)
        )
        records = [
            NewsletterChunk(
                newsletter_id=newsletter_id,
                chunk_index=chunk.chunk_index,
                content=chunk.content,
                content_hash=chunk.content_hash,
                token_count=chunk.token_count,
                embedding_status="pending",
            )
            for chunk in chunks
        ]
        self.db.add_all(records)
        self.db.commit()
        for record in records:
            self.db.refresh(record)
        return records

    def list_by_newsletter(self, newsletter_id: str) -> list[NewsletterChunk]:
        statement = (
            select(NewsletterChunk)
            .where(NewsletterChunk.newsletter_id == newsletter_id)
            .order_by(NewsletterChunk.chunk_index)
        )
        return list(self.db.scalars(statement).all())

    def mark_embedded(
        self,
        chunk: NewsletterChunk,
        embedding: list[float],
        embedding_model: str,
    ) -> NewsletterChunk:
        chunk.embedding = embedding
        chunk.embedding_model = embedding_model
        chunk.embedding_status = "embedded"
        chunk.embedding_error = None
        chunk.embedded_at = datetime.now(UTC)
        self.db.add(chunk)
        return chunk

    def mark_failed(self, chunk: NewsletterChunk, error: str) -> NewsletterChunk:
        chunk.embedding_status = "failed"
        chunk.embedding_error = error[:1000]
        self.db.add(chunk)
        return chunk

    def commit(self) -> None:
        self.db.commit()
