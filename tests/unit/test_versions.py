from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_python_version():
    response = client.get("/version/python")
    assert response.status_code == 200
    assert response.json() == {
        "version": "sys.version_info(major=3, minor=11, micro=6, "
        "releaselevel='final', serial=0)"
    }


def test_get_fastapi_version():
    response = client.get("/version/fastapi")
    assert response.status_code == 200
    assert response.json()["version"] >= "0.103.2"
