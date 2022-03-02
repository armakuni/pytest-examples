import responses
import requests
import pytest


@responses.activate
def test_http_get():
    responses.add(responses.GET, "http://localhost/weee", body="foobar", status=400)
    status_code, text = get_http("http://localhost/weee")
    assert status_code == 400
    assert text == "foobar"


def get_http(url):
    response = requests.get(url)
    return response.status_code, response.text


@pytest.fixture
def base_url():
    return "http://foo"


@pytest.fixture
def mock_responses():
    # responses by default expects all registered calls to be made by the code, so turn this off
    with responses.RequestsMock(assert_all_requests_are_fired=False) as rsps:
        yield rsps


@pytest.fixture
def mock_api(mock_responses, base_url):
    mock_responses.add(responses.GET, f"{base_url}/foo", body="foobar")
    mock_responses.add(responses.GET, f"{base_url}/bar", status=404)
    yield mock_responses  # yield so you can chain fixtures to add more API responses


def test_mock_api(mock_api, base_url):
    response = requests.get(f"{base_url}/foo")
    assert response.status_code == 200
    assert response.text == "foobar"
    response = requests.get(f"{base_url}/bar")
    assert response.status_code == 404
    with pytest.raises(
        requests.exceptions.ConnectionError,
        match="the call doesn't match any registered mock",
    ):
        requests.get(f"{base_url}/notmocked")
