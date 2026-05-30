from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.newsletter import Newsletter
from app.schemas.newsletter import NewsletterCreate


class NewsletterRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def create(self, payload: NewsletterCreate) -> Newsletter:
        newsletter = Newsletter(**payload.model_dump())
        self.db.add(newsletter)
        self.db.commit()
        self.db.refresh(newsletter)
        return newsletter

    def list(self) -> list[Newsletter]:
        statement = select(Newsletter).order_by(Newsletter.created_at.desc())
        return list(self.db.scalars(statement).all())

    def get(self, newsletter_id: str) -> Newsletter | None:
        return self.db.get(Newsletter, newsletter_id)
