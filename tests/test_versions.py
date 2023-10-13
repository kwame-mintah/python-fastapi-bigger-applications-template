from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_python_version():
    response = client.get("/version/python")
    assert response.status_code == 200
    assert (
        response.json()
        == "sys.version_info(major=3, minor=11, micro=5, releaselevel='final', serial=0)"
    )


def test_get_fastapi_version():
    response = client.get("/version/fastapi")
    assert response.status_code == 200
    assert response.json() >= "0.103.2"
