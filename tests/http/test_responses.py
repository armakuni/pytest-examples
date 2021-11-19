import pytest
import responses
import requests
from fizzbuzz.lib.client import Client


@responses.activate
def test_http_get():
    responses.add(responses.GET, "http://localhost/weee", body="foobar", status=400)
    status_code, text = get_http("http://localhost/weee")
    assert status_code == 400
    assert text == "foobar"


def get_http(url):
    response = requests.get(url)
    return response.status_code, response.text
