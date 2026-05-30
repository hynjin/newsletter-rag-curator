from app.models.newsletter import Newsletter
from app.repositories.newsletters import NewsletterRepository
from app.schemas.newsletter import NewsletterCreate


class NewsletterService:
    def __init__(self, repository: NewsletterRepository) -> None:
        self.repository = repository

    def create_newsletter(self, payload: NewsletterCreate) -> Newsletter:
        return self.repository.create(payload)

    def list_newsletters(self) -> list[Newsletter]:
        return self.repository.list()

    def get_newsletter(self, newsletter_id: str) -> Newsletter | None:
        return self.repository.get(newsletter_id)
