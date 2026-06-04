from dataclasses import dataclass
from datetime import UTC, datetime

from app.schemas.newsletter import NewsletterCreate
from app.services.chunking import ChunkCandidate
from app.services.newsletters import NewsletterService


@dataclass
class NewsletterRecord:
    id: str
    title: str
    body: str


@dataclass
class ChunkRecord:
    newsletter_id: str
    chunk_index: int
    content: str
    content_hash: str
    token_count: int
    embedding: list[float] | None = None
    embedding_model: str | None = None
    embedding_status: str = "pending"
    embedding_error: str | None = None
    embedded_at: datetime | None = None


class FakeNewsletterRepository:
    def create(self, payload: NewsletterCreate) -> NewsletterRecord:
        return NewsletterRecord(
            id="newsletter-1",
            title=payload.title,
            body=payload.body,
        )

    def list(self) -> list[NewsletterRecord]:
        return []

    def get(self, newsletter_id: str) -> NewsletterRecord | None:
        return None


class FakeChunkRepository:
    def __init__(self) -> None:
        self.chunks: list[ChunkRecord] = []
        self.committed = False

    def replace_for_newsletter(
        self,
        newsletter_id: str,
        chunks: list[ChunkCandidate],
    ) -> list[ChunkRecord]:
        self.chunks = [
            ChunkRecord(
                newsletter_id=newsletter_id,
                chunk_index=chunk.chunk_index,
                content=chunk.content,
                content_hash=chunk.content_hash,
                token_count=chunk.token_count,
            )
            for chunk in chunks
        ]
        return self.chunks

    def mark_embedded(
        self,
        chunk: ChunkRecord,
        embedding: list[float],
        embedding_model: str,
    ) -> ChunkRecord:
        chunk.embedding = embedding
        chunk.embedding_model = embedding_model
        chunk.embedding_status = "embedded"
        chunk.embedded_at = datetime.now(UTC)
        return chunk

    def mark_failed(self, chunk: ChunkRecord, error: str) -> ChunkRecord:
        chunk.embedding_status = "failed"
        chunk.embedding_error = error
        return chunk

    def commit(self) -> None:
        self.committed = True


class FakeChunkingService:
    def chunk_text(self, text: str) -> list[ChunkCandidate]:
        return [
            ChunkCandidate(
                chunk_index=0,
                content=text,
                content_hash="hash-1",
                token_count=len(text.split()),
            )
        ]


class FakeAIProvider:
    embedding_model = "fake-embedding-model"

    def embed_texts(self, texts: list[str]) -> list[list[float]]:
        return [[0.1, 0.2, 0.3] for _ in texts]

    def generate_text(self, prompt: str) -> str:
        return "generated text"


class FailingAIProvider:
    embedding_model = "fake-embedding-model"

    def embed_texts(self, texts: list[str]) -> list[list[float]]:
        raise RuntimeError("embedding failed")

    def generate_text(self, prompt: str) -> str:
        return "generated text"


def test_create_newsletter_stores_embedded_chunks() -> None:
    chunk_repository = FakeChunkRepository()
    service = NewsletterService(
        repository=FakeNewsletterRepository(),
        chunk_repository=chunk_repository,
        chunking_service=FakeChunkingService(),
        ai_provider=FakeAIProvider(),
    )

    newsletter = service.create_newsletter(
        NewsletterCreate(title="AI Weekly", body="Useful AI notes.")
    )

    assert newsletter.id == "newsletter-1"
    assert chunk_repository.committed is True
    assert len(chunk_repository.chunks) == 1
    chunk = chunk_repository.chunks[0]
    assert chunk.newsletter_id == "newsletter-1"
    assert chunk.embedding == [0.1, 0.2, 0.3]
    assert chunk.embedding_model == "fake-embedding-model"
    assert chunk.embedding_status == "embedded"


def test_create_newsletter_marks_chunks_failed_when_embedding_fails() -> None:
    chunk_repository = FakeChunkRepository()
    service = NewsletterService(
        repository=FakeNewsletterRepository(),
        chunk_repository=chunk_repository,
        chunking_service=FakeChunkingService(),
        ai_provider=FailingAIProvider(),
    )

    newsletter = service.create_newsletter(
        NewsletterCreate(title="AI Weekly", body="Useful AI notes.")
    )

    assert newsletter.id == "newsletter-1"
    assert chunk_repository.committed is True
    assert chunk_repository.chunks[0].embedding_status == "failed"
    assert chunk_repository.chunks[0].embedding_error == "embedding failed"
