import pytest
from fizzbuzz.lib.fizzbuzz import fizzbuzz


@pytest.mark.parametrize("input", [(3), (6), (9)])
def test_fizzbuzz_fizz(input):
    assert fizzbuzz(input) == "fizz"


@pytest.mark.parametrize("input", [(5), (10), (20)])
def test_fizzbuzz_buzz(input):
    assert fizzbuzz(input) == "buzz"


@pytest.mark.parametrize("input, expected", [(2, "2"), (4, "4"), (7, "7")])
def test_fizzbuzz_else(input, expected):
    assert fizzbuzz(input) == expected


@pytest.mark.parametrize("input", [(0), (15), (30)])
def test_fizzbuzz_multiple_3_and_5(input):
    assert fizzbuzz(input) == "fizzbuzz"


@pytest.mark.parametrize("input", [("foo"), ("bar")])
def test_fizzbuzz_raises_on_invalid_input(input):
    with pytest.raises(Exception, match=r"^'{}' is not a number$".format(input)):
        fizzbuzz(input)
