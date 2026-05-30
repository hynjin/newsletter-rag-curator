from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db import get_db
from app.repositories.newsletters import NewsletterRepository
from app.schemas.newsletter import NewsletterCreate, NewsletterListResponse, NewsletterRead
from app.services.newsletters import NewsletterService

router = APIRouter(prefix="/newsletters", tags=["newsletters"])


def get_newsletter_service(db: Session = Depends(get_db)) -> NewsletterService:
    return NewsletterService(NewsletterRepository(db))


@router.post("", response_model=NewsletterRead, status_code=status.HTTP_201_CREATED)
def create_newsletter(
    payload: NewsletterCreate,
    service: NewsletterService = Depends(get_newsletter_service),
) -> NewsletterRead:
    return service.create_newsletter(payload)


@router.get("", response_model=NewsletterListResponse)
def list_newsletters(
    service: NewsletterService = Depends(get_newsletter_service),
) -> NewsletterListResponse:
    return NewsletterListResponse(newsletters=service.list_newsletters())


@router.get("/{newsletter_id}", response_model=NewsletterRead)
def get_newsletter(
    newsletter_id: str,
    service: NewsletterService = Depends(get_newsletter_service),
) -> NewsletterRead:
    newsletter = service.get_newsletter(newsletter_id)
    if newsletter is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Newsletter not found",
        )
    return newsletter
