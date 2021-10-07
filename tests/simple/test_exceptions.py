import pytest


def test_exception_catching():
    with pytest.raises(FooError):
        do_buggy_function()


class FooError(Exception):
    pass


def do_buggy_function():
    raise FooError("Curses")
