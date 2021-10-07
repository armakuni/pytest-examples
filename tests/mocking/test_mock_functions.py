from unittest import mock


@mock.patch("test_mock_functions.b")
def test_call_b(mock_b):
    mock_b.return_value = "buzz"

    assert call_b() == "buzz"


def call_b():
    return b()


def b():
    return "fizz"


# this is an equivalent test without using a decorator
def test_call_b_no_decorator():
    with mock.patch("test_mock_functions.b", return_value="buzz"):
        assert call_b() == "buzz"


# this shows how you can set attributes on the mock
def test_call_b_no_decorator_as():
    with mock.patch("test_mock_functions.b") as mock_b:
        mock_b.return_value = "buzz"

        assert call_b() == "buzz"
