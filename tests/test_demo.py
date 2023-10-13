from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_demo_root():
    response = client.get("/demo")
    assert response.status_code == 200
    assert response.json() == {
        "messages": 1,
        "example": {
            "placeholder": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt"
            "ut labore et dolore magna aliqua."
        },
    }
