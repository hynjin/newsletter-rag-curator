from dataclasses import dataclass
from datetime import date, datetime, timezone

from fastapi.testclient import TestClient

from app.api.routes.newsletters import get_newsletter_service
from app.main import create_app
from app.schemas.newsletter import NewsletterCreate


@dataclass
class NewsletterRecord:
    id: str
    title: str
    author: str | None
    source_url: str | None
    published_at: date | None
    tags: list[str]
    body: str
    created_at: datetime
    updated_at: datetime


class FakeNewsletterService:
    def __init__(self) -> None:
        now = datetime(2026, 5, 30, tzinfo=timezone.utc)
        self.newsletters = [
            NewsletterRecord(
                id="newsletter-1",
                title="AI Weekly",
                author="Ada",
                source_url="https://example.com/ai-weekly",
                published_at=date(2026, 5, 29),
                tags=["ai", "research"],
                body="A practical issue about AI systems.",
                created_at=now,
                updated_at=now,
            )
        ]

    def create_newsletter(self, payload: NewsletterCreate) -> NewsletterRecord:
        now = datetime(2026, 5, 30, tzinfo=timezone.utc)
        newsletter = NewsletterRecord(
            id="newsletter-2",
            title=payload.title,
            author=payload.author,
            source_url=payload.source_url,
            published_at=payload.published_at,
            tags=payload.tags,
            body=payload.body,
            created_at=now,
            updated_at=now,
        )
        self.newsletters.insert(0, newsletter)
        return newsletter

    def list_newsletters(self) -> list[NewsletterRecord]:
        return self.newsletters

    def get_newsletter(self, newsletter_id: str) -> NewsletterRecord | None:
        return next(
            (newsletter for newsletter in self.newsletters if newsletter.id == newsletter_id),
            None,
        )


def create_test_client() -> TestClient:
    app = create_app(auto_create_tables=False)
    service = FakeNewsletterService()
    app.dependency_overrides[get_newsletter_service] = lambda: service
    return TestClient(app)


def test_create_newsletter() -> None:
    client = create_test_client()

    response = client.post(
        "/newsletters",
        json={
            "title": "Founder Notes",
            "author": "Grace",
            "source_url": "https://example.com/founder-notes",
            "published_at": "2026-05-30",
            "tags": ["startups", "strategy"],
            "body": "A useful issue about startup strategy.",
        },
    )

    assert response.status_code == 201
    data = response.json()
    assert data["id"] == "newsletter-2"
    assert data["title"] == "Founder Notes"
    assert data["tags"] == ["startups", "strategy"]


def test_list_newsletters() -> None:
    client = create_test_client()

    response = client.get("/newsletters")

    assert response.status_code == 200
    data = response.json()
    assert len(data["newsletters"]) == 1
    assert data["newsletters"][0]["title"] == "AI Weekly"


def test_get_newsletter() -> None:
    client = create_test_client()

    response = client.get("/newsletters/newsletter-1")

    assert response.status_code == 200
    assert response.json()["title"] == "AI Weekly"


def test_get_missing_newsletter() -> None:
    client = create_test_client()

    response = client.get("/newsletters/unknown")

    assert response.status_code == 404
