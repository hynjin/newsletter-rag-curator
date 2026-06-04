from dataclasses import dataclass
from hashlib import sha256
import re

from app.core.config import settings


@dataclass(frozen=True)
class ChunkCandidate:
    chunk_index: int
    content: str
    content_hash: str
    token_count: int


class ChunkingService:
    def __init__(
        self,
        target_tokens: int | None = None,
        max_tokens: int | None = None,
        overlap_tokens: int | None = None,
    ) -> None:
        self.target_tokens = target_tokens or settings.chunk_target_tokens
        self.max_tokens = max_tokens or settings.chunk_max_tokens
        self.overlap_tokens = overlap_tokens or settings.chunk_overlap_tokens

    def chunk_text(self, text: str) -> list[ChunkCandidate]:
        paragraphs = self._split_paragraphs(text)
        chunks: list[str] = []
        current_words: list[str] = []

        for paragraph in paragraphs:
            paragraph_words = paragraph.split()
            if len(paragraph_words) > self.max_tokens:
                chunks.extend(self._flush(current_words))
                current_words = []
                chunks.extend(self._split_large_paragraph(paragraph_words))
                continue

            if current_words and len(current_words) + len(paragraph_words) > self.target_tokens:
                chunks.extend(self._flush(current_words))
                current_words = self._overlap_words(current_words)

            current_words.extend(paragraph_words)

        chunks.extend(self._flush(current_words))
        return [self._candidate(index, content) for index, content in enumerate(chunks)]

    def _split_paragraphs(self, text: str) -> list[str]:
        normalized = text.replace("\r\n", "\n").replace("\r", "\n").strip()
        if not normalized:
            return []
        return [
            re.sub(r"\s+", " ", paragraph).strip()
            for paragraph in re.split(r"\n\s*\n", normalized)
            if paragraph.strip()
        ]

    def _split_large_paragraph(self, words: list[str]) -> list[str]:
        chunks: list[str] = []
        start = 0
        while start < len(words):
            end = min(start + self.max_tokens, len(words))
            chunks.append(" ".join(words[start:end]))
            if end == len(words):
                break
            start = max(end - self.overlap_tokens, start + 1)
        return chunks

    def _flush(self, words: list[str]) -> list[str]:
        if not words:
            return []
        return [" ".join(words)]

    def _overlap_words(self, words: list[str]) -> list[str]:
        if self.overlap_tokens <= 0:
            return []
        return words[-self.overlap_tokens :]

    def _candidate(self, index: int, content: str) -> ChunkCandidate:
        return ChunkCandidate(
            chunk_index=index,
            content=content,
            content_hash=sha256(content.encode("utf-8")).hexdigest(),
            token_count=len(content.split()),
        )
