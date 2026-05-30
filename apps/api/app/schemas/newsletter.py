from datetime import date, datetime

from pydantic import BaseModel, ConfigDict, Field, field_validator


class NewsletterBase(BaseModel):
    title: str = Field(min_length=1, max_length=240)
    author: str | None = Field(default=None, max_length=160)
    source_url: str | None = Field(default=None, max_length=2048)
    published_at: date | None = None
    tags: list[str] = Field(default_factory=list)
    body: str = Field(min_length=1)

    @field_validator("title", "author", "source_url", "body", mode="before")
    @classmethod
    def trim_optional_text(cls, value: str | None) -> str | None:
        if value is None:
            return None
        if isinstance(value, str):
            trimmed = value.strip()
            return trimmed or None
        return value

    @field_validator("tags", mode="before")
    @classmethod
    def normalize_tags(cls, value: list[str] | str | None) -> list[str]:
        if value is None:
            return []
        if isinstance(value, str):
            value = value.split(",")
        normalized: list[str] = []
        for tag in value:
            trimmed = tag.strip()
            if trimmed and trimmed not in normalized:
                normalized.append(trimmed)
        return normalized


class NewsletterCreate(NewsletterBase):
    pass


class NewsletterRead(NewsletterBase):
    id: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class NewsletterListResponse(BaseModel):
    newsletters: list[NewsletterRead]
