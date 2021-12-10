import pytest


@pytest.fixture
def base_url():
    return "https://foo.bar"


@pytest.fixture
def resource():
    return "widgets"


@pytest.fixture
def widget_url(base_url, resource):
    return f"{base_url}/{resource}"


def test_composed_fixtures(widget_url):
    assert widget_url == "https://foo.bar/widgets"
