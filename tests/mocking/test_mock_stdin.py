import pytest
import sys
import io
from unittest import mock


@mock.patch("test_mock_stdin.sys.stdin", io.StringIO("Bob"))
def test_mock_stdin_patched():
    assert reader() == "Bob"


def test_mock_stdin_fixture(stdin_name):
    # Stdin is mocked within a fixture (below)
    assert reader() == "Bob"


def test_mock_stdin_fixture(stdin_name_local):
    # sys.stdin reassigned. This might result in side effects across tests if you are not careful
    assert reader() == "Bob"


def reader():
    return input("Enter your name: ")


@pytest.fixture
def stdin_name():
    with mock.patch("test_mock_stdin.sys.stdin", io.StringIO("Bob")):
        yield


@pytest.fixture
def stdin_name_local():
    old_stdin = sys.stdin
    sys.stdin = io.StringIO("Bob")
    yield
    sys.stdin = old_stdin
