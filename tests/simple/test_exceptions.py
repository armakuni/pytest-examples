import pytest


def test_exception_catching():
    with pytest.raises(FooError):
        do_buggy_function()


def test_exception_catching_with_match():
    with pytest.raises(FooError, match="[Cc]urses"):
        do_buggy_function()


def test_exception_catching_with_assertions():
    with pytest.raises(FooError) as ex:
        do_buggy_function()
    assert ex.type is FooError
    assert "Curses" in ex.value.args[0]


class FooError(Exception):
    pass


def do_buggy_function():
    raise FooError("Curses")
