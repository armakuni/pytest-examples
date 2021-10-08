import pytest
from unittest import mock
from contextlib import contextmanager


def test_add_and_multiply_unmocked():
    assert add_and_multiply(5, 3) == 45  # (5 + 10) * 3


@mock.patch(__name__+'.add_10')
def test_add_and_multiply_mocked(mock_add10):
    mock_add10.return_value.__enter__ = mock.Mock(return_value=4)
    mock_add10.return_value.__exit__ = mock.Mock(return_value=False)

    assert add_and_multiply(5, 3) == 12  # 4 * 3, rather than (5 + 10) * 3


def test_add_and_multiply_mocked_no_decorator():
    m = mock.patch(__name__ + '.add_10', return_value=mock.Mock(
        __enter__=mock.Mock(return_value=4),
        __exit__=mock.Mock(return_value=False)
    ))
    with m:
        assert add_and_multiply(5, 3) == 12  # 4 * 3, rather than (5 + 10) * 3


def add_and_multiply(input, multiplier):
    with add_10(input) as new_value:
        return new_value * multiplier


@contextmanager
def add_10(value):
    yield(value+10)
