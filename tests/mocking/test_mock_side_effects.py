from unittest import mock
import pytest

from lib.fancy import do_something_fancy


@mock.patch("test_mock_side_effects.do_something_fancy")
def test_fancy_exception_side_effect(mock_do_something_fancy):
    mock_do_something_fancy.side_effect = RuntimeError("foo bar")
    with pytest.raises(RuntimeError) as error:
        call_fancy()

    assert "foo bar" in str(error.value)


@mock.patch("test_mock_side_effects.do_something_fancy")
def test_fancy_swap_implementation_using_side_effects(mock_do_something_fancy):
    mock_do_something_fancy.side_effect = lambda: " ".join(["not", "fancy"])

    assert call_fancy() == "not fancy"


@mock.patch("test_mock_side_effects.do_something_fancy")
def test_multiple_fancy_side_effects(mock_do_something_fancy):
    mock_do_something_fancy.side_effect = ["ooh", "so fancy"]

    assert call_fancy() == "ooh"
    assert call_fancy() == "so fancy"
    with pytest.raises(StopIteration):
        call_fancy()


def call_fancy():
    return do_something_fancy()
