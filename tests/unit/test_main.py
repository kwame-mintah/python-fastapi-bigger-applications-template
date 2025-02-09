from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_main_should_return_welcome_message_returning_200_status_code() -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "What a wonderful kind of day."}
