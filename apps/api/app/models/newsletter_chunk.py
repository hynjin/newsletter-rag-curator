from datetime import datetime
from uuid import uuid4

from pgvector.sqlalchemy import Vector
from sqlalchemy import DateTime, ForeignKey, Index, Integer, String, Text, UniqueConstraint, func
from sqlalchemy.orm import Mapped, mapped_column

from app.core.config import settings
from app.db import Base


class NewsletterChunk(Base):
    __tablename__ = "newsletter_chunks"
    __table_args__ = (
        UniqueConstraint("newsletter_id", "chunk_index", name="uq_newsletter_chunks_position"),
        Index("idx_newsletter_chunks_newsletter_id", "newsletter_id"),
        Index("idx_newsletter_chunks_embedding_status", "embedding_status"),
        Index("idx_newsletter_chunks_content_hash", "content_hash"),
    )

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid4()),
    )
    newsletter_id: Mapped[str] = mapped_column(
        String(36),
        ForeignKey("newsletters.id", ondelete="CASCADE"),
        nullable=False,
    )
    chunk_index: Mapped[int] = mapped_column(Integer, nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    content_hash: Mapped[str] = mapped_column(String(64), nullable=False)
    token_count: Mapped[int] = mapped_column(Integer, nullable=False)
    embedding: Mapped[list[float] | None] = mapped_column(
        Vector(settings.embedding_dimensions),
        nullable=True,
    )
    embedding_model: Mapped[str | None] = mapped_column(String(120), nullable=True)
    embedding_status: Mapped[str] = mapped_column(String(32), nullable=False, default="pending")
    embedding_error: Mapped[str | None] = mapped_column(Text, nullable=True)
    embedded_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )
