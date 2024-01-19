import requests
from pytest_bdd import scenario, given, parsers, then

result = {}


@scenario(
    feature_name="test_service_is_running.feature",
    scenario_name="Service should be up and running",
)
def test_service_is_running(service):
    """
    Cucumber scenario
    """


@given(name=parsers.parse("an API call is made to {url}"))
def check_service_via_api_call(url: str):
    endpoint = "http://localhost:8000" + url
    response = requests.get(endpoint)
    result["status_code"] = response.status_code


@then(name=parsers.parse("the response status code should be {status}"))
def check_response_status_code(status: int):
    assert result["status_code"] == int(status)
