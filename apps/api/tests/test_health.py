from fastapi.testclient import TestClient

from app.main import create_app


def test_health_endpoint() -> None:
    app = create_app(auto_create_tables=False)
    client = TestClient(app)

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "service": "Newsletter RAG Curator API",
    }
