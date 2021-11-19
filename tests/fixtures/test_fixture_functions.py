import pytest


@pytest.fixture
def hostname():
    return "localhost"


@pytest.fixture
def port():
    return 1234


@pytest.fixture
def api_path():
    return "/api/v1"


@pytest.fixture
def api_url(hostname, port, api_path):
    def construct_url(path):
        return f"https://{hostname}:{port}{api_path}{path}"

    return construct_url


def test_path(api_url):
    assert api_url("/foo/bar") == "https://localhost:1234/api/v1/foo/bar"
