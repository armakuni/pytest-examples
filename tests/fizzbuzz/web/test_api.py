import pytest

from fizzbuzz.web.api import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


@pytest.mark.parametrize(
    "input,expected",
    [
        (3, b"fizz"),
        (5, b"buzz"),
        (15, b"fizzbuzz"),
    ],
)
def test_fizzbuzz(client, input, expected):
    actual = client.get(f"/fizzbuzz/{input}")

    assert expected == actual.data
