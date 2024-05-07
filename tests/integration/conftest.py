import os

import pytest
import requests

from requests.exceptions import ConnectionError


def is_responsive(url) -> bool:
    """
    Check the service is response.

    :param url: URL to check
    :return: Response result
    """
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
    except ConnectionError:
        return False


@pytest.fixture(scope="session")
def service(docker_ip, docker_services) -> str:
    """
    Ensure that HTTP service is up and responsive.

    :param docker_ip: IP address for TCP connections to Docker containers.
    :param docker_services: Start all services from the docker compose file (docker-compose up)
    :return: URL for the service(s)
    """
    port = docker_services.port_for("fastapi", 8000)
    url = "http://{}:{}".format(docker_ip, port)
    docker_services.wait_until_responsive(
        timeout=30.0, pause=0.1, check=lambda: is_responsive(url)
    )
    return url


@pytest.fixture(scope="session")
def docker_compose_file(pytestconfig) -> str:
    """
    Locate the `docker-compose.yml` file to be used for integration tests.
    :param pytestconfig:
    :return: OS Path
    """
    return os.path.join(str(pytestconfig.rootdir), "docker", "docker-compose.yml")
