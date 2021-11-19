import pytest
import responses
from fizzbuzz.lib.client import Client


@pytest.fixture
def api_url():
    return "http://localhost:48881"


@pytest.fixture
def client(api_url):
    return Client(api_url)


@responses.activate
def test_client_fizz(api_url, client):
    responses.add(responses.GET, f"{api_url}/fizzbuzz/3", body="fizz", status=200)
    assert client.fizzbuzz(3) == "fizz"
    assert len(responses.calls) == 1
