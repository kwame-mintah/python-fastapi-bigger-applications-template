from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_python_version_should_return_current_system_version_return_200_status_code() -> (
    None
):
    response = client.get("/version/python")
    assert response.status_code == 200
    assert response.json() == {
        "version": "sys.version_info(major=3, minor=11, micro=6, "
        "releaselevel='final', serial=0)"
    }


def test_get_fastapi_version_should_return_current_library_version_returning_200_status_code() -> (
    None
):
    response = client.get("/version/fastapi")
    assert response.status_code == 200
    assert response.json()["version"] >= "0.115.0"
