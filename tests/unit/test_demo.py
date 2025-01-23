from fastapi.testclient import TestClient

from app.main import app
from app.models.models import Message, Example

client = TestClient(app)


def test_get_demo_root() -> None:
    response = client.get("/demo")
    assert response.status_code == 200
    assert response.json() == [
        {
            "messageId": 1,
            "example": {
                "placeholder": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
                "sed do eiusmod tempor incididunt"
                "ut labore et dolore magna aliqua."
            },
        }
    ]


def test_post_demo_root() -> None:
    body = Message(
        messageId=2, example=Example(placeholder="Unit Testing")
    ).model_dump_json()
    response = client.post(
        url="/demo", data=body, headers={"Content-type": "application/json"}
    )
    assert response.status_code == 200
    assert response.json() == [
        {
            "example": {
                "placeholder": "Lorem ipsum dolor sit amet, consectetur "
                "adipiscing elit, sed do eiusmod tempor "
                "incididuntut labore et dolore magna aliqua."
            },
            "messageId": 1,
        },
        {"example": {"placeholder": "Unit Testing"}, "messageId": 2},
    ]


def test_delete_demo_root() -> None:
    existing_data = client.get("/demo")
    assert len(existing_data.json()) >= 2

    response = client.delete(
        url="/demo/1", headers={"Content-type": "application/json"}
    )
    assert response.status_code == 204

    after_deletion = client.get("/demo")
    assert len(after_deletion.json()) == 1
