"""
If you wish to follow the principle of one assertion per test, then turn your subject
into a fixture. Scope the fixture according to how heavy-weight it is to run. An alternative
approach is to use a test class and have the "subject" created by a class-internal fixture,
with the tests able to access self.subject. This feels a bit less obvious, however.
"""
import pytest
import requests
import responses


@pytest.fixture
def result(url, content):
    with responses.RequestsMock() as response:
        response.add(
            responses.GET,
            url,
            body=content,
        )
        yield fetch(url)


def test_ok(result):
    assert result["ok"]


def test_content_type(result):
    assert result["content-type"] == "text/plain"


def test_body(result, content):
    assert result["body"] == content


@pytest.fixture()
def url():
    return "http://foo.bar"


@pytest.fixture()
def content():
    return "The quick brown flox"


def fetch(url):
    r = requests.get(url)
    return {
        "ok": r.status_code == 200,
        "content-type": r.headers["content-type"],
        "body": r.text,
    }
