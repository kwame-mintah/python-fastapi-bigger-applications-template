from typing import Generator
from unittest.mock import Mock, patch

import pytest
from fastapi.testclient import TestClient

from app.dependencies import get_demo_service
from app.main import app
from app.models.models import Message, Example


@pytest.fixture(scope="function")
def client() -> Generator:
    """
    Provide a TestClient that can override any dependency
    overrides set.
    :return: TestClient
    """
    with TestClient(app) as client:
        app.dependency_overrides.clear()
        yield client


@pytest.fixture(scope="function", autouse=False)
def mock_dependency_client() -> TestClient:
    """
    Provide a TestClient that has dependency overrides as an example.
    Overrides `DemoService` as an example.
    :return: TestClient
    """

    def mock_example_function() -> Mock:
        """
        Override function and return a specific value.
        :return: Mock
        """
        mock_demo_service = Mock()
        mock_demo_service.return_stub_data.return_value = [
            Message(
                messageId=1,
                example=Example(placeholder="Example mocked dependency override."),
            )
        ]
        return mock_demo_service

    app.dependency_overrides.update({get_demo_service: mock_example_function})
    return TestClient(app=app)


def test_get_demo_root_should_return_existing_messages_return_200_status_code(
    mock_dependency_client: TestClient,
) -> None:
    response = mock_dependency_client.get("/demo")
    assert response.status_code == 200
    assert response.json() == [
        {
            "messageId": 1,
            "example": {"placeholder": "Example mocked dependency override."},
        }
    ]


def test_post_demo_root_should_insert_new_message_returning_200_status_code(
    client: TestClient,
) -> None:
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


@pytest.mark.xfail(
    reason="Test should be isolated from previous tests", raises=AssertionError
)
def test_delete_demo_root_should_return_204_status_code(client: TestClient) -> None:
    existing_data = client.get("/demo")
    assert len(existing_data.json()) == 1

    response = client.delete(
        url="/demo/1", headers={"Content-type": "application/json"}
    )
    assert response.status_code == 204

    after_deletion = client.get("/demo")
    assert len(after_deletion.json()) == 0
