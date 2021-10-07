from unittest import mock


@mock.patch("test_mock_functions.b")
def test_call_b(mock_b):
    mock_b.return_value = "buzz"

    assert call_b() == "buzz"


def call_b():
    return b()


def b():
    return "fizz"
