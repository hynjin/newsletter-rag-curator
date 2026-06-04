from app.models.newsletter import Newsletter
from app.repositories.newsletter_chunks import NewsletterChunkRepository
from app.repositories.newsletters import NewsletterRepository
from app.schemas.newsletter import NewsletterCreate
from app.services.ai_provider import AIProvider, GeminiAIProvider
from app.services.chunking import ChunkingService


class NewsletterService:
    def __init__(
        self,
        repository: NewsletterRepository,
        chunk_repository: NewsletterChunkRepository | None = None,
        chunking_service: ChunkingService | None = None,
        ai_provider: AIProvider | None = None,
    ) -> None:
        self.repository = repository
        self.chunk_repository = chunk_repository
        self.chunking_service = chunking_service or ChunkingService()
        self.ai_provider = ai_provider or GeminiAIProvider()

    def create_newsletter(self, payload: NewsletterCreate) -> Newsletter:
        newsletter = self.repository.create(payload)
        if self.chunk_repository is None:
            return newsletter

        chunk_candidates = self.chunking_service.chunk_text(newsletter.body)
        chunk_records = self.chunk_repository.replace_for_newsletter(
            newsletter.id,
            chunk_candidates,
        )
        if not chunk_records:
            return newsletter

        try:
            embeddings = self.ai_provider.embed_texts(
                [chunk.content for chunk in chunk_records]
            )
            for chunk, embedding in zip(chunk_records, embeddings, strict=True):
                self.chunk_repository.mark_embedded(
                    chunk,
                    embedding,
                    self.ai_provider.embedding_model,
                )
        except Exception as exc:
            for chunk in chunk_records:
                self.chunk_repository.mark_failed(chunk, str(exc))
        finally:
            self.chunk_repository.commit()

        return newsletter

    def list_newsletters(self) -> list[Newsletter]:
        return self.repository.list()

    def get_newsletter(self, newsletter_id: str) -> Newsletter | None:
        return self.repository.get(newsletter_id)
