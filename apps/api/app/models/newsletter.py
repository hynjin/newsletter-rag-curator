from datetime import date, datetime
from uuid import uuid4

from sqlalchemy import Date, DateTime, Index, String, Text, func
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class Newsletter(Base):
    __tablename__ = "newsletters"
    __table_args__ = (
        Index("idx_newsletters_created_at", "created_at"),
        Index("idx_newsletters_published_at", "published_at"),
    )

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid4()),
    )
    title: Mapped[str] = mapped_column(String(240), nullable=False)
    author: Mapped[str | None] = mapped_column(String(160), nullable=True)
    source_url: Mapped[str | None] = mapped_column(String(2048), nullable=True)
    published_at: Mapped[date | None] = mapped_column(Date, nullable=True)
    tags: Mapped[list[str]] = mapped_column(JSONB, nullable=False, default=list)
    body: Mapped[str] = mapped_column(Text, nullable=False)
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
