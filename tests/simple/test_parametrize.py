import pytest


@pytest.mark.parametrize("input,divisor,expected", [(3, 3, True), (3, 2, False)])
def test_is_divisible(input, divisor, expected):
    test = input % divisor == 0
    assert test == expected
