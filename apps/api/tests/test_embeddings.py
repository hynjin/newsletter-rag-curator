import pytest

from app.services.ai_provider import GeminiAIProvider


def test_gemini_provider_returns_empty_list_for_empty_embedding_input() -> None:
    provider = GeminiAIProvider(api_key="", embedding_model="test-model", dimensions=3)

    assert provider.embed_texts([]) == []


def test_gemini_provider_requires_api_key_for_non_empty_embedding_input() -> None:
    provider = GeminiAIProvider(api_key="", embedding_model="test-model", dimensions=3)

    with pytest.raises(RuntimeError, match="GEMINI_API_KEY"):
        provider.embed_texts(["newsletter chunk"])


def test_gemini_provider_returns_empty_text_for_empty_generation_prompt() -> None:
    provider = GeminiAIProvider(api_key="", generation_model="test-model")

    assert provider.generate_text("   ") == ""


def test_gemini_provider_requests_configured_dimensions_and_normalizes_001_embeddings(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    captured: dict[str, object] = {}

    class FakeEmbedContentConfig:
        def __init__(self, **kwargs: object) -> None:
            captured["config"] = kwargs

    class FakeEmbedding:
        values = [3.0, 4.0, 0.0]

    class FakeResponse:
        embeddings = [FakeEmbedding()]

    class FakeModels:
        def embed_content(
            self,
            model: str,
            contents: list[str],
            config: FakeEmbedContentConfig,
        ) -> FakeResponse:
            captured["model"] = model
            captured["contents"] = contents
            captured["config_object"] = config
            return FakeResponse()

    class FakeClient:
        def __init__(self, api_key: str) -> None:
            captured["api_key"] = api_key
            self.models = FakeModels()

    monkeypatch.setattr("app.services.ai_provider.types.EmbedContentConfig", FakeEmbedContentConfig)
    monkeypatch.setattr("app.services.ai_provider.genai.Client", FakeClient)

    provider = GeminiAIProvider(
        api_key="test-key",
        embedding_model="gemini-embedding-001",
        dimensions=3,
    )

    embeddings = provider.embed_texts(["newsletter chunk"])

    assert captured["api_key"] == "test-key"
    assert captured["model"] == "gemini-embedding-001"
    assert captured["contents"] == ["newsletter chunk"]
    assert captured["config"] == {
        "output_dimensionality": 3,
        "task_type": "RETRIEVAL_DOCUMENT",
    }
    assert embeddings == [[0.6, 0.8, 0.0]]


def test_gemini_provider_uses_generation_model(monkeypatch: pytest.MonkeyPatch) -> None:
    captured: dict[str, object] = {}

    class FakeResponse:
        text = "generated text"

    class FakeModels:
        def generate_content(self, model: str, contents: str) -> FakeResponse:
            captured["model"] = model
            captured["contents"] = contents
            return FakeResponse()

    class FakeClient:
        def __init__(self, api_key: str) -> None:
            captured["api_key"] = api_key
            self.models = FakeModels()

    monkeypatch.setattr("app.services.ai_provider.genai.Client", FakeClient)

    provider = GeminiAIProvider(api_key="test-key", generation_model="gemini-test")

    assert provider.generate_text("Summarize this") == "generated text"
    assert captured == {
        "api_key": "test-key",
        "model": "gemini-test",
        "contents": "Summarize this",
    }
