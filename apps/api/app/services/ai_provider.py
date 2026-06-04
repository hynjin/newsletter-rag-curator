import math
from typing import Protocol

from google import genai
from google.genai import types

from app.core.config import settings


class AIProvider(Protocol):
    embedding_model: str

    def embed_texts(self, texts: list[str]) -> list[list[float]]:
        pass

    def generate_text(self, prompt: str) -> str:
        pass


class GeminiAIProvider:
    def __init__(
        self,
        api_key: str | None = None,
        embedding_model: str | None = None,
        generation_model: str | None = None,
        dimensions: int | None = None,
    ) -> None:
        self.api_key = api_key if api_key is not None else settings.gemini_api_key
        self.embedding_model = embedding_model or settings.gemini_embedding_model
        self.generation_model = generation_model or settings.gemini_generation_model
        self.dimensions = dimensions or settings.embedding_dimensions

    def embed_texts(self, texts: list[str]) -> list[list[float]]:
        if not texts:
            return []
        if not self.api_key:
            raise RuntimeError("GEMINI_API_KEY is required to generate embeddings")

        client = genai.Client(api_key=self.api_key)
        response = client.models.embed_content(
            model=self.embedding_model,
            contents=texts,
            config=self._embedding_config(),
        )
        embeddings = [list(embedding.values) for embedding in response.embeddings]
        if self.embedding_model == "gemini-embedding-001" and self.dimensions != 3072:
            return [_normalize_embedding(embedding) for embedding in embeddings]
        return embeddings

    def generate_text(self, prompt: str) -> str:
        if not prompt.strip():
            return ""
        if not self.api_key:
            raise RuntimeError("GEMINI_API_KEY is required to generate text")

        client = genai.Client(api_key=self.api_key)
        response = client.models.generate_content(
            model=self.generation_model,
            contents=prompt,
        )
        return response.text or ""

    def _embedding_config(self) -> types.EmbedContentConfig:
        config_kwargs = {"output_dimensionality": self.dimensions}
        if self.embedding_model == "gemini-embedding-001":
            config_kwargs["task_type"] = "RETRIEVAL_DOCUMENT"
        return types.EmbedContentConfig(**config_kwargs)


def _normalize_embedding(values: list[float]) -> list[float]:
    magnitude = math.sqrt(sum(value * value for value in values))
    if magnitude == 0:
        return values
    return [value / magnitude for value in values]
